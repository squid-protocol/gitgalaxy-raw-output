# ARCHITECTURAL_BRIEF: tornado
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/tornado` |
| **Timestamp** | `2026-08-03T19:43:11.709497+00:00` |
| **Scan Duration** | `0.94s` |
| **Git Branch** | `master` |
| **Git Commit** | `0ca3c5f8279d402b245718d16522bc18a8f5d958` |
| **Git Remote** | `https://github.com/tornadoweb/tornado.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 78 malicious artifacts.

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
| Total Artifacts | 318 |
| Analyzed Artifacts (Scanned) | 110 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 208 |
| Total LOC | 14316 |
| Volatility Index | 0.036 |
| % Scanned of codebase = | 34.6% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3165 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2106 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 12.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.249 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 61 | 13451 | 55.5% |
| HTML | 14 | 240 | 12.7% |
| MARKDOWN | 7 | 0 | 6.4% |
| SHELL | 7 | 79 | 6.4% |
| PLAINTEXT | 4 | 0 | 3.6% |
| CSS | 4 | 243 | 3.6% |
| JAVASCRIPT | 3 | 156 | 2.7% |
| RUBY | 3 | 22 | 2.7% |
| YAML | 2 | 18 | 1.8% |
| DOCKERFILE | 1 | 8 | 0.9% |
| SQLITE | 1 | 19 | 0.9% |
| XML | 1 | 0 | 0.9% |
| M4 | 1 | 8 | 0.9% |
| C | 1 | 72 | 0.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.134`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 46 | 41.8% |
| file_cluster_13 | 27 | 24.5% |
| file_cluster_16 | 14 | 12.7% |
| file_cluster_4 | 5 | 4.5% |
| file_cluster_0 | 5 | 4.5% |
| file_cluster_9 | 2 | 1.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 11 | 10.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 208*

**Composition by Extension & Reason:**
- `.rst`: 110x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.rst')
- `.py`: 48x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 5x Excluded (Unsupported Extension: '.ini'), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cfg`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.cfg')
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.in`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pyx`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.9 | 23.2 | 15.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 84.8 | 28.2 | 9.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 36.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 30.9 | 2.4 | 80.0 |
| API Exposure | 0.0 | 11.7 | 3.1 | 2.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 27.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 37.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 64.6 | 1.8 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 82.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.7 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 23.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 69.1 | 93.9 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 44.7 | 4.8 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 42.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 5.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tornado/netutil.py` (Hits: 69)
- `tornado/iostream.py` (Hits: 54)
- `tornado/web.py` (Hits: 27)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **asyncio.py** (`tornado/platform/asyncio.py`) — 25 inbound connections
2. **options.py** (`tornado/options.py`) — 18 inbound connections
3. **log.py** (`tornado/log.py`) — 17 inbound connections
4. **util.py** (`tornado/util.py`) — 17 inbound connections
5. **ioloop.py** (`tornado/ioloop.py`) — 15 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **web.py** (`tornado/web.py`) — 33 outbound dependencies
2. **ioloop.py** (`tornado/ioloop.py`) — 25 outbound dependencies
3. **testing.py** (`tornado/testing.py`) — 25 outbound dependencies
4. **websocket.py** (`tornado/websocket.py`) — 25 outbound dependencies
5. **simple_httpclient.py** (`tornado/simple_httpclient.py`) — 23 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_has_stream_request_body` (@ `tornado/web.py`) -> Impact: **1001.3** | LOC: 426
- `_read_message` (@ `tornado/http1connection.py`) -> Impact: **947.5** | LOC: 278
  * *Intent:* # Save the start lines after we read or write them; they # have content-length but no bodies) self._request_start_line: httputil.RequestStartLine | No...
- `load_translations` (@ `tornado/locale.py`) -> Impact: **499.3** | LOC: 407
- `print_help` (@ `tornado/options.py`) -> Impact: **456.3** | LOC: 154
- `__repr__` (@ `tornado/locks.py`) -> Impact: **449.7** | LOC: 265
- `cpu_count` (@ `tornado/process.py`) -> Impact: **448.3** | LOC: 236
- `handle_callback_exception` (@ `tornado/curl_httpclient.py`) -> Impact: **366.4** | LOC: 261
- `filter_whitespace` (@ `tornado/template.py`) -> Impact: **358.4** | LOC: 135
- `get` (@ `tornado/web.py`) -> Impact: **352.1** | LOC: 82
- `_do_ssl_handshake` (@ `tornado/iostream.py`) -> Impact: **321.6** | LOC: 197

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `main` (@ `maint/benchmark/chunk_benchmark.py`) -> **O(2^N) [Recursive]**
- `filter_whitespace` (@ `tornado/template.py`) -> **O(2^N) [Recursive]**
- `_has_stream_request_body` (@ `tornado/web.py`) -> **O(2^N) [Recursive]**
- `_read_message` (@ `tornado/http1connection.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Save the start lines after we read or write them; they # have content-length but no bodies) self._request_start_line: httputil.RequestStartLine | No...
- `data_received` (@ `tornado/http1connection.py`) -> **O(2^N) [Recursive]**
- `cookies` (@ `tornado/httputil.py`) -> **O(2^N) [Recursive]**
- `__repr__` (@ `tornado/locks.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `tornado/log.py`) -> **O(2^N) [Recursive]**
- `print_help` (@ `tornado/options.py`) -> **O(2^N) [Recursive]**
- `post` (@ `demos/blog/blog.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `cpu_count` (@ `tornado/process.py`) -> DB Complexity: **94**
- `_handle_write` (@ `tornado/iostream.py`) -> DB Complexity: **62**
  * *Intent:* # Read from the socket until we get EWOULDBLOCK or equivalent. # SSL sockets do some internal buffering, and if the data is # sitting in the SSL objec...
- `_check_file` (@ `tornado/autoreload.py`) -> DB Complexity: **57**
- `load_translations` (@ `tornado/locale.py`) -> DB Complexity: **43**
- `_do_ssl_handshake` (@ `tornado/iostream.py`) -> DB Complexity: **39**
- `_has_stream_request_body` (@ `tornado/web.py`) -> DB Complexity: **33**
- `_read_message` (@ `tornado/http1connection.py`) -> DB Complexity: **25**
  * *Intent:* # Save the start lines after we read or write them; they # have content-length but no bodies) self._request_start_line: httputil.RequestStartLine | No...
- `validate_absolute_path` (@ `tornado/web.py`) -> DB Complexity: **24**
- `print_help` (@ `tornado/options.py`) -> DB Complexity: **24**
- `set_nodelay` (@ `tornado/iostream.py`) -> DB Complexity: **21**
  * *Intent:* # Broken pipe errors are usually caused by connection # minimize log spam gen_log.warning("Write error on %s: %s", self.fileno(), e) self.close(exc_in...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `tornado` | 33 | 17765.9 | 28.13% | 48.36% |
| `demos/blog` | 6 | 435.18 | 13.51% | 32.6% |
| `tornado/platform` | 4 | 397.5 | 22.75% | 2.92% |
| `maint/benchmark` | 5 | 253.2 | 27.47% | 16.51% |
| `demos/file_upload` | 2 | 203.38 | 28.93% | 0.0% |
| `demos/webspider` | 1 | 169.1 | 67.44% | 0.0% |
| `demos/chat/static` | 2 | 135.14 | 44.05% | 46.52% |
| `demos/blog/templates` | 8 | 133.52 | 16.53% | 0.0% |
| `demos/chat` | 1 | 125.54 | 45.65% | 99.93% |
| `maint/scripts` | 4 | 102.14 | 6.74% | 50.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `maint/scripts/custom_fixers/fix_unicode_literal.py` -> **100.0%** Exposure
- `tornado/template.py` -> **100.0%** Exposure
- `tornado/httpserver.py` -> **100.0%** Exposure
- `tornado/queues.py` -> **100.0%** Exposure
- `tornado/routing.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `tornado/httpclient.py` -> **100.0%** Exposure
- `demos/websocket/static/chat.js` -> **100.0%** Exposure
- `tornado/speedups.c` -> **100.0%** Exposure
- `maint/benchmark/benchmark.py` -> **99.9999%** Exposure
- `demos/chat/static/chat.js` -> **99.9998%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tornado/web.py` -> **0** Orphaned Functions | **50** Duplicates
- `tornado/websocket.py` -> **0** Orphaned Functions | **47** Duplicates
- `tornado/template.py` -> **0** Orphaned Functions | **40** Duplicates
- `tornado/routing.py` -> **0** Orphaned Functions | **19** Duplicates
- `tornado/iostream.py` -> **0** Orphaned Functions | **18** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`tornado/autoreload.py`** -> AI Confidence: **99.31%**
2. **`tornado/curl_httpclient.py`** -> AI Confidence: **99.31%**
3. **`tornado/http1connection.py`** -> AI Confidence: **99.31%**
4. **`tornado/httputil.py`** -> AI Confidence: **99.31%**
5. **`tornado/locale.py`** -> AI Confidence: **99.31%**
6. **`tornado/log.py`** -> AI Confidence: **99.31%**
7. **`tornado/simple_httpclient.py`** -> AI Confidence: **99.31%**
8. **`maint/vm/freebsd/Vagrantfile`** -> AI Confidence: **99.29%**
9. **`maint/vm/ubuntu12.04/Vagrantfile`** -> AI Confidence: **99.29%**
10. **`maint/vm/ubuntu14.04/Vagrantfile`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `demos/blog/blog.py` -> **100.0%** Exposure
- `demos/chat/chatdemo.py` -> **100.0%** Exposure
- `demos/facebook/facebook.py` -> **100.0%** Exposure
- `demos/file_upload/file_receiver.py` -> **100.0%** Exposure
- `maint/vm/windows/bootstrap.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `demos/blog/blog.py` -> **100.0%** Exposure
- `setup.py` -> **100.0%** Exposure
- `tornado/autoreload.py` -> **100.0%** Exposure
- `tornado/process.py` -> **100.0%** Exposure
- `tornado/web.py` -> **98.2353%** Exposure
### Algorithmic DoS Exposure
- `demos/blog/blog.py` -> **100.0%** Exposure
- `demos/chat/chatdemo.py` -> **100.0%** Exposure
- `demos/facebook/facebook.py` -> **100.0%** Exposure
- `demos/file_upload/file_receiver.py` -> **100.0%** Exposure
- `demos/file_upload/file_uploader.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `599` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `tornado/web.py` (PYTHON) -> Cumulative Risk: **1039.21**
- **Archetype:** `file_cluster_16` (Distance: 13.045 IQR)
- **Magnitude:** 3495.0 | **LOC:** 3804 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 83.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_has_stream_request_body` (Impact: 1001.3), `get` (Impact: 352.1), `write` (Impact: 295.9)

### 2. `tornado/websocket.py` (PYTHON) -> Cumulative Risk: **970.54**
- **Archetype:** `file_cluster_16` (Distance: 12.692 IQR)
- **Magnitude:** 1245.66 | **LOC:** 1721 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 70.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `close` (Impact: 157.6), `_receive_frame` (Impact: 119.1), `get` (Impact: 74.5)

### 3. `tornado/testing.py` (PYTHON) -> Cumulative Risk: **961.03**
- **Archetype:** `file_cluster_13` (Distance: 11.97 IQR)
- **Magnitude:** 647.38 | **LOC:** 864 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 87.5%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `filter` (Impact: 156.5), `_callTestMethod` (Impact: 112.3), `tearDown` (Impact: 85.3)

### 4. `tornado/ioloop.py` (PYTHON) -> Cumulative Risk: **931.65**
- **Archetype:** `file_cluster_13` (Distance: 12.722 IQR)
- **Magnitude:** 467.72 | **LOC:** 979 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 87.5%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `make_current` (Impact: 163.5), `current` (Impact: 74.6), `configure` (Impact: 32.4)

### 5. `tornado/httpserver.py` (PYTHON) -> Cumulative Risk: **929.13**
- **Archetype:** `file_cluster_13` (Distance: 11.614 IQR)
- **Magnitude:** 197.48 | **LOC:** 406 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 85.7%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `_apply_xheaders` (Impact: 31.4), `__str__` (Impact: 14.4), `close_all_connections` (Impact: 8.3)

### 6. `tornado/process.py` (PYTHON) -> Cumulative Risk: **929.05**
- **Archetype:** `file_cluster_13` (Distance: 12.972 IQR)
- **Magnitude:** 542.24 | **LOC:** 363 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 83.3%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `cpu_count` (Impact: 448.3)

### 7. `tornado/httpclient.py` (PYTHON) -> Cumulative Risk: **905.54**
- **Archetype:** `file_cluster_13` (Distance: 12.785 IQR)
- **Magnitude:** 440.0 | **LOC:** 789 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 62.5%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `__new__` (Impact: 48.9), `main` (Impact: 31.8), `handle_response` (Impact: 24.3)

### 8. `tornado/tcpclient.py` (PYTHON) -> Cumulative Risk: **903.8**
- **Archetype:** `file_cluster_13` (Distance: 11.32 IQR)
- **Magnitude:** 169.58 | **LOC:** 324 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 85.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `try_connect` (Impact: 30.9), `close` (Impact: 14.0), `__init__` (Impact: 10.7)

### 9. `tornado/wsgi.py` (PYTHON) -> Cumulative Risk: **898.2**
- **Archetype:** `file_cluster_13` (Distance: 11.444 IQR)
- **Magnitude:** 211.58 | **LOC:** 267 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 83.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `handle_request` (Impact: 76.2), `environ` (Impact: 71.1), `_log` (Impact: 16.9)

### 10. `tornado/http1connection.py` (PYTHON) -> Cumulative Risk: **891.16**
- **Archetype:** `file_cluster_16` (Distance: 12.775 IQR)
- **Magnitude:** 1772.38 | **LOC:** 887 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 83.3%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_read_message` (Impact: 947.5), `finish` (Impact: 225.3), `finish` (Impact: 119.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tornado/web.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.045 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.49 IQR)
- **Top Global Matches:** file_cluster_16: 13.045, file_cluster_13: 13.147, file_cluster_0: 13.238
- **Magnitude:** 3495.0 | **LOC:** 3804 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (28.4196%), Tech Debt (99.9468%)
**Top Internal Functions/Classes:**
  * `_has_stream_request_body` (Impact: 1001.3 | O(2^N) | DB: 33)
  * `get` (Impact: 352.1 | O(2^N) | DB: 3)
  * `write` (Impact: 295.9 | O(2^N) | DB: 10)
  * `compute_etag` (Impact: 157.9 | O(2^N) | DB: 1)
  * `get_browser_locale` (Impact: 119.2 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 438`, `structural_boundaries: 522`, `args: 199`, `func_start: 196`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 101`, `state_mutation: 247`, `dead_code: 4`, `planned_debt: 8`, `duplicate_logic: 50`
* *Architecture:* `io: 27`, `api: 171`, `concurrency: 19`, `import: 36`
* *Defense:* `safety: 120`, `doc: 236`, `test: 25`, `sync_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.077
  * `Choke Point (Betweenness):` 0.002962 | `Ripple Effect (Closeness):` 0.047182
  * `Imports (Out-Degree: 7):` tornado, warnings, collections.abc, base64, asyncio, gzip, types, tornado.escape...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `tornado/http1connection.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.775 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.775 IQR)
- **Top Global Matches:** file_cluster_16: 12.775, file_cluster_13: 12.777, file_cluster_8: 12.802
- **Magnitude:** 1772.38 | **LOC:** 887 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (46.3316%), Tech Debt (93.299%)
**Top Internal Functions/Classes:**
  * `_read_message` (Impact: 947.5 | O(2^N) | DB: 25)
    * *Intent:* # Save the start lines after we read or write them; they # have content-length but no bodies) self._...
  * `finish` (Impact: 225.3 | O(N^6) | DB: 5)
  * `finish` (Impact: 119.2 | O(2^N) | DB: 4)
  * `data_received` (Impact: 110.1 | O(2^N))
  * `_read_chunked_body` (Impact: 68.3 | O(N^6))
    * *Intent:* % headers["Content-Length"]
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 137`, `args: 40`, `func_start: 39`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 145`, `planned_debt: 5`, `duplicate_logic: 7`
* *Architecture:* `api: 23`, `concurrency: 42`, `import: 11`
* *Defense:* `safety: 35`, `doc: 46`, `test: 9`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.878
  * `Choke Point (Betweenness):` 0.000394 | `Ripple Effect (Closeness):` 0.047182
  * `Imports (Out-Degree: 5):` tornado, tornado.concurrent, collections.abc, tornado.escape, asyncio, types, tornado.util, logging...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tornado/iostream.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.482 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.096 IQR)
- **Top Global Matches:** file_cluster_13: 13.482, file_cluster_11: 13.589, file_cluster_16: 13.603
- **Magnitude:** 1689.58 | **LOC:** 1609 | **CtrlFlow:** 46.0% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 62
- **Risk Profile:** Cognitive Load (39.087%), Tech Debt (99.8256%)
**Top Internal Functions/Classes:**
  * `_do_ssl_handshake` (Impact: 321.6 | O(2^N) | DB: 39)
  * `_handle_read` (Impact: 214.1 | O(N^6) | DB: 10)
  * `_handle_events` (Impact: 194.6 | O(2^N) | DB: 3)
  * `_handle_write` (Impact: 142.6 | O(N^5) | DB: 62)
    * *Intent:* # Read from the socket until we get EWOULDBLOCK or equivalent. # SSL sockets do some internal buffer...
  * `append` (Impact: 78.9 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 235`, `args: 78`, `func_start: 71`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 217`, `dead_code: 3`, `planned_debt: 5`, `fragile_debt: 1`, `duplicate_logic: 18`
* *Architecture:* `io: 54`, `api: 53`, `concurrency: 3`, `import: 21`
* *Defense:* `safety: 83`, `doc: 80`, `test: 10`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.831
  * `Choke Point (Betweenness):` 0.002917 | `Ripple Effect (Closeness):` 0.173259
  * `Imports (Out-Degree: 5):` tornado, collections, collections.abc, asyncio, ssl, errno, types, io...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `tornado/websocket.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.692 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.284 IQR)
- **Top Global Matches:** file_cluster_16: 12.692, file_cluster_13: 12.726, file_cluster_4: 12.785
- **Magnitude:** 1245.66 | **LOC:** 1721 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 70.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (43.1705%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `close` (Impact: 157.6 | O(2^N) | DB: 4)
  * `_receive_frame` (Impact: 119.1 | O(N^4) | DB: 7)
  * `get` (Impact: 74.5 | O(2^N) | DB: 3)
  * `_handle_message` (Impact: 72.5 | O(N^4) | DB: 4)
  * `_accept_connection` (Impact: 64.9 | O(N^5) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 271`, `args: 103`, `func_start: 100`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 158`, `dead_code: 2`, `planned_debt: 8`, `duplicate_logic: 47`
* *Architecture:* `io: 6`, `api: 74`, `concurrency: 93`, `import: 26`
* *Defense:* `safety: 46`, `doc: 84`, `test: 17`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.59
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` tornado, warnings, collections.abc, base64, asyncio, abc, struct, tornado.escape...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tornado/template.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.952 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.678 IQR)
- **Top Global Matches:** file_cluster_16: 11.952, file_cluster_13: 12.06, file_cluster_8: 12.172
- **Magnitude:** 844.42 | **LOC:** 1043 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 85.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (42.7421%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `filter_whitespace` (Impact: 358.4 | O(2^N) | DB: 11)
  * `resolve_path` (Impact: 30.6 | O(N^4) | DB: 15)
  * `generate` (Impact: 22.4 | O(N^4))
  * `resolve_path` (Impact: 20.5 | O(N^3))
  * `load` (Impact: 15.4 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 180`, `args: 71`, `func_start: 69`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 115`, `dead_code: 1`, `fragile_debt: 2`, `duplicate_logic: 40`
* *Architecture:* `io: 9`, `api: 44`, `concurrency: 7`, `import: 14`
* *Defense:* `safety: 21`, `doc: 26`, `test: 7`, `sync_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.691
  * `Choke Point (Betweenness):` 0.000156 | `Ripple Effect (Closeness):` 0.009174
  * `Imports (Out-Degree: 2):` linecache, threading, tornado, os.path, posixpath, re, collections.abc, missing...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tornado/httputil.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.792 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.867 IQR)
- **Top Global Matches:** file_cluster_16: 12.792, file_cluster_13: 12.795, file_cluster_11: 12.982
- **Magnitude:** 777.44 | **LOC:** 1373 | **CtrlFlow:** 47.7% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (33.3868%), Tech Debt (67.0958%)
**Top Internal Functions/Classes:**
  * `_encode_header` (Impact: 113.2 | O(N^3) | DB: 2)
    * *Intent:* """ start = start or 0 end = (end or total) - 1 return f"bytes {start}-{end}/{total}" def _int_or_no...
  * `_parseparam` (Impact: 112.0 | O(2^N) | DB: 2)
  * `cookies` (Impact: 85.9 | O(2^N))
  * `parse_line` (Impact: 82.1 | O(N^5) | DB: 2)
  * `parse_request_start_line` (Impact: 46.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 170`, `args: 55`, `func_start: 55`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 104`, `planned_debt: 9`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 68`, `concurrency: 1`, `import: 23`
* *Defense:* `safety: 35`, `doc: 102`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.425
  * `Choke Point (Betweenness):` 0.001019 | `Ripple Effect (Closeness):` 0.018349
  * `Imports (Out-Degree: 4):` collections.abc, ssl, asyncio, tornado.escape, copy, __future__, calendar, typing...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tornado/options.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.667 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 6.027 IQR)
- **Top Global Matches:** file_cluster_16: 11.667, file_cluster_13: 11.809, file_cluster_8: 12.002
- **Magnitude:** 674.72 | **LOC:** 734 | **CtrlFlow:** 42.7% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (34.8829%), Tech Debt (59.1182%)
**Top Internal Functions/Classes:**
  * `print_help` (Impact: 456.3 | O(2^N) | DB: 24)
  * `_parse_timedelta` (Impact: 32.0 | O(N^5))
  * `group_dict` (Impact: 14.3 | O(N^3))
  * `_parse_datetime` (Impact: 14.2 | O(N^4))
  * `__getattr__` (Impact: 10.9 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 114`, `args: 38`, `func_start: 37`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 44`, `duplicate_logic: 4`
* *Architecture:* `io: 6`, `api: 28`, `import: 11`
* *Defense:* `safety: 15`, `doc: 40`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 37.32
  * `Choke Point (Betweenness):` 0.013212 | `Ripple Effect (Closeness):` 0.220183
  * `Imports (Out-Degree: 4):` os, tornado, myapp.db, sys, myapp.server, re, collections.abc, numbers...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `tornado/curl_httpclient.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.896 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.005 IQR)
- **Top Global Matches:** file_cluster_13: 10.896, file_cluster_8: 10.913, file_cluster_16: 11.086
- **Magnitude:** 655.26 | **LOC:** 594 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (25.1205%), Tech Debt (17.287%)
**Top Internal Functions/Classes:**
  * `handle_callback_exception` (Impact: 366.4 | O(N^5) | DB: 1)
  * `_process_queue` (Impact: 44.4 | O(N^6) | DB: 2)
  * `_handle_socket` (Impact: 32.0 | O(N^4))
  * `_curl_debug` (Impact: 31.0 | O(N^4) | DB: 1)
  * `_handle_events` (Impact: 30.8 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 65`, `args: 19`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 33`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 9`, `concurrency: 3`, `import: 15`
* *Defense:* `safety: 22`, `doc: 14`, `test: 7`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.031
  * `Choke Point (Betweenness):` 8.1e-05 | `Ripple Effect (Closeness):` 0.009174
  * `Imports (Out-Degree: 3):` threading, tornado, collections, inspect, collections.abc, tornado.escape, functools, time...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tornado/testing.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.97 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.089 IQR)
- **Top Global Matches:** file_cluster_13: 11.97, file_cluster_16: 12.169, file_cluster_11: 12.332
- **Magnitude:** 647.38 | **LOC:** 864 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 87.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (35.9309%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `filter` (Impact: 156.5 | O(N^5) | DB: 14)
    * *Intent:* """Returns the port used by the server. A new port is chosen for each test. """
  * `_callTestMethod` (Impact: 112.3 | O(N^6) | DB: 12)
    * *Intent:* # raising a CancelledError inside the coroutine). This may # just transform the "task was destroyed ...
  * `tearDown` (Impact: 85.3 | O(2^N))
  * `wrap` (Impact: 56.5 | O(N^5) | DB: 2)
  * `setUp` (Impact: 35.5 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 132`, `args: 40`, `func_start: 40`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 59`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 15`, `orphaned_logic: 3`
* *Architecture:* `io: 14`, `api: 37`, `concurrency: 12`, `import: 25`
* *Defense:* `safety: 16`, `doc: 46`, `test: 12`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.59
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` tornado.platform.asyncio, tornado, warnings, collections.abc, asyncio, types, tornado.httpserver, inspect...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tornado/locale.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.984 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.959 IQR)
- **Top Global Matches:** file_cluster_13: 10.984, file_cluster_8: 11.09, file_cluster_16: 11.101
- **Magnitude:** 572.98 | **LOC:** 589 | **CtrlFlow:** 47.3% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (13.1165%), Tech Debt (14.2609%)
**Top Internal Functions/Classes:**
  * `load_translations` (Impact: 499.3 | O(N^6) | DB: 43)
  * `set_default_locale` (Impact: 2.4 | O(N^1) | DB: 2)
  * `get` (Impact: 2.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 87`, `args: 20`, `func_start: 20`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 42`, `orphaned_logic: 2`
* *Architecture:* `io: 9`, `api: 20`, `import: 13`
* *Defense:* `safety: 7`, `doc: 34`, `test: 4`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.59
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` os, tornado, tornado._locale_data, re, __future__, collections.abc, gettext, codecs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tornado/process.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.972 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.589 IQR)
- **Top Global Matches:** file_cluster_13: 12.972, file_cluster_4: 13.174, file_cluster_0: 13.218
- **Magnitude:** 542.24 | **LOC:** 363 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 94
- **Risk Profile:** Cognitive Load (44.3268%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `cpu_count` (Impact: 448.3 | O(2^N) | DB: 94)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 60`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 64`, `dead_code: 1`
* *Architecture:* `io: 24`, `api: 10`, `concurrency: 16`, `import: 15`
* *Defense:* `safety: 15`, `doc: 18`, `test: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.08
  * `Choke Point (Betweenness):` 0.000123 | `Ripple Effect (Closeness):` 0.148856
  * `Imports (Out-Degree: 4):` os, tornado, subprocess, random, sys, signal, collections.abc, tornado.concurrent...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tornado/locks.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.931 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.099 IQR)
- **Top Global Matches:** file_cluster_16: 11.931, file_cluster_13: 12.19, file_cluster_8: 12.415
- **Magnitude:** 537.48 | **LOC:** 567 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (24.0983%), Tech Debt (18.7084%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 449.7 | O(2^N) | DB: 12)
  * `_garbage_collect` (Impact: 14.2 | O(N^3) | DB: 2)
  * `__init__` (Impact: 2.7 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 68`, `args: 39`, `func_start: 35`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 39`, `fragile_debt: 1`
* *Architecture:* `api: 20`, `concurrency: 8`, `import: 7`
* *Defense:* `safety: 2`, `doc: 38`, `sync_locks: 15`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.187
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012232
  * `Imports (Out-Degree: 3):` tornado, collections, tornado.concurrent, collections.abc, asyncio, tornado.locks, types, typing...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tornado/routing.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.507 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.597 IQR)
- **Top Global Matches:** file_cluster_16: 12.507, file_cluster_13: 12.58, file_cluster_0: 12.882
- **Magnitude:** 477.88 | **LOC:** 723 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (26.8669%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 186.3 | O(N^6) | DB: 6)
  * `reverse_url` (Impact: 60.5 | O(2^N))
  * `match` (Impact: 43.6 | O(2^N))
  * `match` (Impact: 28.0 | O(2^N))
    * *Intent:* """Rule-based router implementation."""
  * `__init__` (Impact: 17.7 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 113`, `args: 37`, `func_start: 37`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 48`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 19`
* *Architecture:* `api: 33`, `import: 10`
* *Defense:* `safety: 22`, `doc: 52`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.328
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.03211
  * `Imports (Out-Degree: 4):` tornado, collections.abc, tornado.escape, functools, the, tornado.util, tornado.httpserver, typing...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tornado/ioloop.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.722 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.943 IQR)
- **Top Global Matches:** file_cluster_13: 12.722, file_cluster_16: 12.732, file_cluster_0: 12.946
- **Magnitude:** 467.72 | **LOC:** 979 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 87.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (32.2633%), Tech Debt (79.35%)
**Top Internal Functions/Classes:**
  * `make_current` (Impact: 163.5 | O(2^N) | DB: 3)
    * *Intent:* # These constants were originally based on constants from the epoll module.
  * `current` (Impact: 74.6 | O(2^N))
  * `configure` (Impact: 32.4 | O(2^N))
  * `_update_next` (Impact: 18.8 | O(N^4))
  * `close_fd` (Impact: 17.8 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 136`, `args: 59`, `func_start: 55`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 34`, `planned_debt: 2`, `duplicate_logic: 3`
* *Architecture:* `io: 2`, `api: 50`, `concurrency: 18`, `import: 25`
* *Defense:* `safety: 31`, `doc: 72`, `test: 4`, `sync_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 142.219
  * `Choke Point (Betweenness):` 0.012162 | `Ripple Effect (Closeness):` 0.217914
  * `Imports (Out-Degree: 6):` tornado.platform.asyncio, tornado, warnings, collections.abc, asyncio, errno, tornado.iostream, tornado.gen...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `tornado/httpclient.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.785 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.599 IQR)
- **Top Global Matches:** file_cluster_13: 12.785, file_cluster_16: 12.823, file_cluster_0: 13.02
- **Magnitude:** 440.0 | **LOC:** 789 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 62.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (47.9079%), Tech Debt (99.9994%)
**Top Internal Functions/Classes:**
  * `__new__` (Impact: 48.9 | O(2^N))
    * *Intent:* # Initialize self._closed at the beginning of the constructor # so that an exception raised here doe...
  * `main` (Impact: 31.8 | O(N^4))
  * `handle_response` (Impact: 24.3 | O(N^5))
  * `close` (Impact: 22.4 | O(N^4) | DB: 2)
  * `__getattr__` (Impact: 14.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 90`, `args: 29`, `func_start: 29`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 149`, `planned_debt: 1`, `duplicate_logic: 13`
* *Architecture:* `api: 29`, `concurrency: 2`, `import: 15`
* *Defense:* `safety: 8`, `doc: 31`, `test: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.052
  * `Choke Point (Betweenness):` 0.001258 | `Ripple Effect (Closeness):` 0.029358
  * `Imports (Out-Degree: 6):` weakref, tornado, tornado.concurrent, collections.abc, tornado.escape, ssl, tornado.simple_httpclient, functools...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `demos/blog/blog.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 9.659 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.288 IQR)
- **Top Global Matches:** file_cluster_4: 9.659, file_cluster_8: 9.787, file_cluster_13: 9.834
- **Magnitude:** 395.86 | **LOC:** 321 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (47.7139%), Tech Debt (95.6035%)
**Top Internal Functions/Classes:**
  * `post` (Impact: 99.3 | O(2^N))
  * `queryone` (Impact: 40.9 | O(2^N) | DB: 1)
  * `post` (Impact: 32.8 | O(N^4))
  * `get` (Impact: 22.3 | O(2^N))
  * `maybe_create_tables` (Impact: 20.5 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 91`, `args: 22`, `func_start: 22`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`, `duplicate_logic: 5`
* *Architecture:* `io: 8`, `api: 33`, `concurrency: 59`, `import: 10`
* *Defense:* `safety: 6`, `doc: 8`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.59
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` tornado, psycopg2, os.path, re, asyncio, tornado.options, bcrypt, aiopg...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tornado/log.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.655 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.282 IQR)
- **Top Global Matches:** file_cluster_13: 10.655, file_cluster_8: 10.705, file_cluster_16: 11.008
- **Magnitude:** 353.2 | **LOC:** 345 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (15.4084%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 239.5 | O(2^N) | DB: 5)
  * `_stderr_supports_color` (Impact: 42.4 | O(N^5) | DB: 9)
  * `format` (Impact: 36.9 | O(N^4) | DB: 1)
  * `_safe_unicode` (Impact: 6.2 | O(N^2))
  * `enable_pretty_logging` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 38`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 18`
* *Architecture:* `io: 3`, `api: 5`, `import: 10`
* *Defense:* `safety: 15`, `doc: 10`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 58.616
  * `Choke Point (Betweenness):` 0.00891 | `Ripple Effect (Closeness):` 0.245786
  * `Imports (Out-Degree: 3):` logging.handlers, sys, to, curses, tornado.util, tornado.options, logging, typing...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `tornado/util.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.311 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.565 IQR)
- **Top Global Matches:** file_cluster_16: 12.311, file_cluster_13: 12.315, file_cluster_0: 12.645
- **Magnitude:** 316.44 | **LOC:** 435 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (40.3947%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `configure` (Impact: 116.2 | O(N^4) | DB: 11)
  * `import_object` (Impact: 62.9 | O(N^3))
  * `__new__` (Impact: 51.0 | O(2^N) | DB: 2)
  * `__getattr__` (Impact: 7.2 | O(N^3))
    * *Intent:* # no longer our own TimeoutError, use standard asyncio class TimeoutError = asyncio.TimeoutError cla...
  * `decompress` (Impact: 6.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 89`, `args: 27`, `func_start: 27`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 13`
* *Architecture:* `io: 3`, `api: 25`, `concurrency: 2`, `import: 18`
* *Defense:* `safety: 18`, `doc: 40`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 137.934
  * `Choke Point (Betweenness):` 0.003528 | `Ripple Effect (Closeness):` 0.25467
  * `Imports (Out-Degree: 2):` os, unittest, inspect, __future__, collections.abc, tornado.escape, asyncio, x.y...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `tornado/platform/asyncio.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.405 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.267 IQR)
- **Top Global Matches:** file_cluster_4: 13.405, file_cluster_13: 13.648, file_cluster_11: 13.734
- **Magnitude:** 295.78 | **LOC:** 749 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (63.1699%), Tech Debt (11.6843%)
**Top Internal Functions/Classes:**
  * `close` (Impact: 35.4 | O(2^N) | DB: 1)
    * *Intent:* # If an asyncio loop was closed through an asyncio interface # instead of IOLoop.close(), we'd never...
  * `_atexit_callback` (Impact: 18.1 | O(N^3) | DB: 1)
  * `fileno` (Impact: 2.7 | O(N^2))
  * `initialize` (Impact: 1.6 | O(N^2))
  * `add_handler` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 121`, `args: 48`, `func_start: 48`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 67`, `dead_code: 6`, `planned_debt: 3`
* *Architecture:* `io: 3`, `api: 38`, `concurrency: 123`, `import: 17`
* *Defense:* `safety: 41`, `doc: 16`, `test: 2`, `sync_locks: 1`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 139.469
  * `Choke Point (Betweenness):` 0.008672 | `Ripple Effect (Closeness):` 0.278127
  * `Imports (Out-Degree: 1):` threading, select, sys, socket, warnings, collections.abc, contextvars, asyncio...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `tornado/simple_httpclient.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.79 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.209 IQR)
- **Top Global Matches:** file_cluster_13: 11.79, file_cluster_8: 11.981, file_cluster_16: 12.029
- **Magnitude:** 273.7 | **LOC:** 697 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (37.6127%), Tech Debt (66.0414%)
**Top Internal Functions/Classes:**
  * `finish` (Impact: 63.8 | O(N^6) | DB: 2)
    * *Intent:* # TODO: this may cause a StreamClosedError to be raised # by the connection's Future. Should we canc...
  * `_should_follow_redirect` (Impact: 22.2 | O(N^4))
  * `data_received` (Impact: 14.3 | O(N^3) | DB: 1)
  * `close` (Impact: 14.1 | O(2^N))
  * `__init__` (Impact: 5.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 114`, `args: 31`, `func_start: 29`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 89`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 6`, `api: 13`, `concurrency: 19`, `import: 23`
* *Defense:* `safety: 27`, `doc: 10`, `test: 10`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.605
  * `Choke Point (Betweenness):` 0.0011 | `Ripple Effect (Closeness):` 0.024465
  * `Imports (Out-Degree: 8):` tornado, collections, collections.abc, base64, ssl, tornado.escape, types, copy...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tornado/escape.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.529 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.451 IQR)
- **Top Global Matches:** file_cluster_16: 10.529, file_cluster_13: 10.694, file_cluster_0: 10.837
- **Magnitude:** 265.94 | **LOC:** 400 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.9264%), Tech Debt (99.9912%)
**Top Internal Functions/Classes:**
  * `make_link` (Impact: 116.9 | O(N^5))
  * `recursive_unicode` (Impact: 54.6 | O(2^N))
  * `utf8` (Impact: 31.5 | O(N^2))
  * `url_escape` (Impact: 5.4 | O(N^1))
  * `xhtml_escape` (Impact: 2.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 64`, `args: 21`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 14`, `duplicate_logic: 7`
* *Architecture:* `api: 28`, `import: 8`
* *Defense:* `safety: 9`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 91.735
  * `Choke Point (Betweenness):` 6.2e-05 | `Ripple Effect (Closeness):` 0.222501
  * `Imports (Out-Degree: 1):` html, collections.abc, urllib.parse, json, tornado.util, typing, re
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `tornado/autoreload.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.678 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.217 IQR)
- **Top Global Matches:** file_cluster_13: 10.678, file_cluster_16: 11.048, file_cluster_8: 11.078
- **Magnitude:** 238.76 | **LOC:** 351 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 57
- **Risk Profile:** Cognitive Load (18.2731%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_check_file` (Impact: 162.3 | O(N^4) | DB: 57)
  * `_reload_on_update` (Impact: 32.4 | O(N^3) | DB: 3)
  * `start` (Impact: 22.7 | O(2^N))
  * `watch` (Impact: 2.2 | O(N^1))
  * `wait` (Impact: 2.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 46`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 6`
* *Architecture:* `io: 23`, `api: 6`, `import: 18`
* *Defense:* `safety: 16`, `doc: 14`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.59
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` tornado, collections.abc, tornado.autoreload, types, optparse, subprocess, sys, signal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tornado/queues.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.932 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.787 IQR)
- **Top Global Matches:** file_cluster_16: 11.932, file_cluster_13: 12.049, file_cluster_8: 12.414
- **Magnitude:** 230.8 | **LOC:** 419 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (26.1248%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `task_done` (Impact: 21.2 | O(2^N) | DB: 1)
  * `_format` (Impact: 17.9 | O(N^3))
  * `_consume_expired` (Impact: 17.7 | O(N^3))
  * `get_nowait` (Impact: 14.6 | O(N^3))
  * `put_nowait` (Impact: 14.5 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 75`, `args: 31`, `func_start: 30`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 25`, `duplicate_logic: 11`
* *Architecture:* `api: 22`, `import: 9`
* *Defense:* `safety: 7`, `doc: 28`, `test: 2`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.81
  * `Choke Point (Betweenness):` 8.5e-05 | `Ripple Effect (Closeness):` 0.009174
  * `Imports (Out-Degree: 4):` tornado, collections, heapq, __future__, collections.abc, tornado.concurrent, tornado.queues, asyncio...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tornado/wsgi.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.444 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.27 IQR)
- **Top Global Matches:** file_cluster_13: 11.444, file_cluster_16: 11.761, file_cluster_8: 11.845
- **Magnitude:** 211.58 | **LOC:** 267 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (30.947%), Tech Debt (65.1355%)
**Top Internal Functions/Classes:**
  * `handle_request` (Impact: 76.2 | O(N^5) | DB: 4)
  * `environ` (Impact: 71.1 | O(2^N) | DB: 5)
  * `_log` (Impact: 16.9 | O(N^3))
    * *Intent:* # StopIteration is special and is not allowed to pass through # coroutines normally.
  * `__call__` (Impact: 2.7 | O(N^2))
  * `to_wsgi_str` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 46`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 24`, `planned_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 6`, `concurrency: 8`, `import: 13`
* *Defense:* `safety: 10`, `doc: 6`, `test: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.59
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` tornado, sys, tornado.concurrent, collections.abc, typing, _typeshed.wsgi, types, tornado.ioloop...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tornado/httpserver.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.614 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.828 IQR)
- **Top Global Matches:** file_cluster_13: 11.614, file_cluster_16: 11.643, file_cluster_11: 11.917
- **Magnitude:** 197.48 | **LOC:** 406 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 85.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (45.722%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_apply_xheaders` (Impact: 31.4 | O(N^4) | DB: 2)
  * `__str__` (Impact: 14.4 | O(N^3) | DB: 6)
  * `close_all_connections` (Impact: 8.3 | O(N^3))
  * `data_received` (Impact: 5.3 | O(2^N))
  * `finish` (Impact: 5.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 61`, `args: 23`, `func_start: 23`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 54`, `planned_debt: 2`, `duplicate_logic: 12`
* *Architecture:* `io: 7`, `api: 23`, `concurrency: 2`, `import: 10`
* *Defense:* `safety: 4`, `doc: 10`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.256
  * `Choke Point (Betweenness):` 0.001713 | `Ripple Effect (Closeness):` 0.04194
  * `Imports (Out-Degree: 4):` tornado, tornado.http1connection, socket, collections.abc, tornado.tcpserver, ssl, tornado.util, typing...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `demos/blog/templates/modules/entry.html` (HTML) | Magnitude: 14.16 | Delta: **0.136 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: ssr_boundaries: 8, indent_spaces: 6, structural_boundaries: 5, io: 4
- `demos/facebook/templates/modules/post.html` (HTML) | Magnitude: 16.34 | Delta: **0.237 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, ssr_boundaries: 12, io: 8, decorators: 7
- `demos/blog/templates/compose.html` (HTML) | Magnitude: 27.74 | Delta: **0.422 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, ssr_boundaries: 16, args: 10, structural_boundaries: 9
- `demos/chat/templates/message.html` (HTML) | Magnitude: 11.52 | Delta: **0.618 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: ssr_boundaries: 2, structural_boundaries: 1, api: 1, decorators: 1
- `demos/websocket/templates/message.html` (HTML) | Magnitude: 11.52 | Delta: **0.618 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: ssr_boundaries: 2, structural_boundaries: 1, api: 1, decorators: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tornado/ioloop.py` (PYTHON) | Magnitude: 467.72 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 325, structural_boundaries: 136, encapsulation: 76, doc: 72
- `tornado/curl_httpclient.py` (PYTHON) | Magnitude: 655.26 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 407, branch: 105, encapsulation: 78, structural_boundaries: 65
- `tornado/httpserver.py` (PYTHON) | Magnitude: 197.48 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 179, structural_boundaries: 61, state_mutation: 54, encapsulation: 33
- `tornado/httpclient.py` (PYTHON) | Magnitude: 440.0 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 322, state_mutation: 149, structural_boundaries: 90, encapsulation: 60
- `tornado/log.py` (PYTHON) | Magnitude: 353.2 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 186, branch: 48, structural_boundaries: 38, encapsulation: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tornado/http1connection.py` (PYTHON) | Magnitude: 1772.38 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 575, encapsulation: 172, branch: 165, state_mutation: 145
- `tornado/httputil.py` (PYTHON) | Magnitude: 777.44 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 537, structural_boundaries: 170, branch: 155, encapsulation: 110
- `tornado/util.py` (PYTHON) | Magnitude: 316.44 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 156, structural_boundaries: 89, generics: 49, encapsulation: 42
- `tornado/websocket.py` (PYTHON) | Magnitude: 1245.66 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 938, structural_boundaries: 271, encapsulation: 221, branch: 163
- `tornado/routing.py` (PYTHON) | Magnitude: 477.88 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 268, structural_boundaries: 113, branch: 67, generics: 55

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `demos/chat/chatdemo.py` (PYTHON) | Magnitude: 125.54 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 25, state_mutation: 18, concurrency: 18
- `demos/blog/blog.py` (PYTHON) | Magnitude: 395.86 | Delta: **0.128 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 201, structural_boundaries: 91, concurrency: 59, api: 33
- `demos/webspider/webspider.py` (PYTHON) | Magnitude: 169.1 | Delta: **0.196 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 34, concurrency: 20, branch: 13
- `tornado/platform/asyncio.py` (PYTHON) | Magnitude: 295.78 | Delta: **0.243 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 385, encapsulation: 166, concurrency: 123, structural_boundaries: 121
- `maint/benchmark/benchmark.py` (PYTHON) | Magnitude: 64.44 | Delta: **0.413 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 21, concurrency: 21, indent_spaces: 21, state_mutation: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `tornado/speedups.c` (C) | Magnitude: 90.54 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 55, indent_spaces: 52, api: 15, branch: 12
- `maint/test/mypy/setup.py` (PYTHON) | Magnitude: 11.04 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, import: 1
- `demos/helloworld/helloworld.py` (PYTHON) | Magnitude: 13.32 | Delta: **0.122 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 8, concurrency: 5, api: 3
- `maint/benchmark/chunk_benchmark.py` (PYTHON) | Magnitude: 61.82 | Delta: **0.173 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 16, import: 6, branch: 5
- `demos/file_upload/file_uploader.py` (PYTHON) | Magnitude: 167.86 | Delta: **0.239 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 30, branch: 14, concurrency: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `runtests.sh` (SHELL) | Magnitude: 2.16 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, safety: 1, safety_bypasses: 1
- `demos/blog/schema.sql` (SQLITE) | Magnitude: 6.48 | Delta: **0.112 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 12, duplicate_logic: 5, safety: 4, safety_bypasses: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tornado/httputil.py` -> Churn: **100.0%** | Cog Load: 33.3868% | Debt: 67.0958%
- `tornado/web.py` -> Churn: **92.05%** | Cog Load: 28.4196% | Debt: 99.9468%
- `tornado/websocket.py` -> Churn: **85.67%** | Cog Load: 43.1705% | Debt: 100.0%
- `tornado/httpclient.py` -> Churn: **78.04%** | Cog Load: 47.9079% | Debt: 99.9994%
- `tornado/ioloop.py` -> Churn: **78.04%** | Cog Load: 32.2633% | Debt: 79.35%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tornado/web.py` -> **Ben Darnell** (83.3% isolated ownership) | Magnitude: 3495.0
- `tornado/http1connection.py` -> **Ben Darnell** (83.3% isolated ownership) | Magnitude: 1772.38
- `tornado/template.py` -> **Ben Darnell** (85.7% isolated ownership) | Magnitude: 844.42
- `tornado/options.py` -> **Ben Darnell** (83.3% isolated ownership) | Magnitude: 674.72
- `tornado/testing.py` -> **Ben Darnell** (87.5% isolated ownership) | Magnitude: 647.38

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `tornado/options.py` -> **Severity: 1.224** (Bridge: 0.0132 * Flux: 92.6132%)
- `tornado/ioloop.py` -> **Severity: 1.011** (Bridge: 0.0122 * Flux: 83.1268%)
- `tornado/platform/asyncio.py` -> **Severity: 0.853** (Bridge: 0.0087 * Flux: 98.3955%)
- `tornado/log.py` -> **Severity: 0.69** (Bridge: 0.0089 * Flux: 77.4203%)
- `tornado/iostream.py` -> **Severity: 0.292** (Bridge: 0.0029 * Flux: 99.9686%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tornado/util.py` -> **Severity: 20.374** (Embedded: 0.2547 * Error Risk: 80.0%)
- `tornado/platform/asyncio.py` -> **Severity: 18.964** (Embedded: 0.2781 * Error Risk: 68.1862%)
- `tornado/escape.py` -> **Severity: 16.922** (Embedded: 0.2225 * Error Risk: 76.0526%)
- `tornado/ioloop.py` -> **Severity: 16.16** (Embedded: 0.2179 * Error Risk: 74.1595%)
- `tornado/options.py` -> **Severity: 15.93** (Embedded: 0.2202 * Error Risk: 72.3497%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tornado/ioloop.py` -> **Severity: 14221.9** (Blast Radius: 142.219 * Doc Risk: 100.0%)
- `tornado/util.py` -> **Severity: 13793.4** (Blast Radius: 137.934 * Doc Risk: 100.0%)
- `tornado/platform/asyncio.py` -> **Severity: 12937.061** (Blast Radius: 139.469 * Doc Risk: 92.7594%)
- `tornado/escape.py` -> **Severity: 9173.5** (Blast Radius: 91.735 * Doc Risk: 100.0%)
- `tornado/log.py` -> **Severity: 5861.6** (Blast Radius: 58.616 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
