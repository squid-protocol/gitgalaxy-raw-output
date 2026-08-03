# ARCHITECTURAL_BRIEF: tenacity
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/tenacity` |
| **Timestamp** | `2026-08-03T21:25:41.595979+00:00` |
| **Scan Duration** | `0.32s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 21 malicious artifacts.

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
| Total Artifacts | 81 |
| Analyzed Artifacts (Scanned) | 65 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 16 |
| Total LOC | 3436 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 80.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3715 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.58 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.5455 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| YAML | 44 | 182 | 67.7% |
| PYTHON | 21 | 3254 | 32.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.721`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 50 | 76.9% |
| file_cluster_16 | 8 | 12.3% |
| file_cluster_13 | 4 | 6.2% |
| file_cluster_4 | 2 | 3.1% |
| file_cluster_0 | 1 | 1.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 16*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 4x Excluded (Unsupported Extension: '.rst')
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 2.2 | 53.7 | 10.7 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 7.1 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 10.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 9.2 | 0.6 | 0.5 |
| API Exposure | 0.0 | 9.1 | 1.1 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 12.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 99.7 | 10.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 48.0 | 33.3 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 35.8 | 26.7 | 20.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 21.1 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 14.8 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tenacity-9.1.4/doc/source/conf.py` (Hits: 7)
- `tenacity-9.1.4/tenacity/asyncio/__init__.py` (Hits: 2)
- `tenacity-9.1.4/tenacity/__init__.py` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **wait.py** (`tenacity-9.1.4/tenacity/wait.py`) — 3 inbound connections
2. **stop.py** (`tenacity-9.1.4/tenacity/stop.py`) — 2 inbound connections
3. **test_tenacity.py** (`tenacity-9.1.4/tests/test_tenacity.py`) — 2 inbound connections
4. **after.py** (`tenacity-9.1.4/tenacity/after.py`) — 1 inbound connections
5. **before.py** (`tenacity-9.1.4/tenacity/before.py`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`tenacity-9.1.4/tenacity/__init__.py`) — 22 outbound dependencies
2. **test_tenacity.py** (`tenacity-9.1.4/tests/test_tenacity.py`) — 14 outbound dependencies
3. **__init__.py** (`tenacity-9.1.4/tenacity/asyncio/__init__.py`) — 12 outbound dependencies
4. **test_asyncio.py** (`tenacity-9.1.4/tests/test_asyncio.py`) — 9 outbound dependencies
5. **_utils.py** (`tenacity-9.1.4/tenacity/_utils.py`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `test_callstate_repr` (@ `tenacity-9.1.4/tests/test_tenacity.py`) -> Impact: **650.8** | LOC: 1688
- `__repr__` (@ `tenacity-9.1.4/tenacity/__init__.py`) -> Impact: **91.8** | LOC: 174
- `__call__` (@ `tenacity-9.1.4/tenacity/retry.py`) -> Impact: **52.6** | LOC: 12
- `before_sleep_log` (@ `tenacity-9.1.4/tenacity/before_sleep.py`) -> Impact: **52.5** | LOC: 44
- `__call__` (@ `tenacity-9.1.4/tenacity/asyncio/retry.py`) -> Impact: **43.9** | LOC: 11
- `__call__` (@ `tenacity-9.1.4/tenacity/retry.py`) -> Impact: **43.9** | LOC: 11
- `find_ordinal` (@ `tenacity-9.1.4/tenacity/_utils.py`) -> Impact: **42.7** | LOC: 14
- `test_async` (@ `tenacity-9.1.4/tests/test_issue_478.py`) -> Impact: **37.3** | LOC: 46
- `test_retry_with_async_result_or` (@ `tenacity-9.1.4/tests/test_asyncio.py`) -> Impact: **36.5** | LOC: 29
- `test_retry_with_async_result_ror` (@ `tenacity-9.1.4/tests/test_asyncio.py`) -> Impact: **36.5** | LOC: 29

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `__call__` (@ `tenacity-9.1.4/tenacity/retry.py`) -> **O(2^N) [Recursive]**
- `__call__` (@ `tenacity-9.1.4/tenacity/asyncio/retry.py`) -> **O(2^N) [Recursive]**
- `__call__` (@ `tenacity-9.1.4/tenacity/retry.py`) -> **O(2^N) [Recursive]**
- `statistics` (@ `tenacity-9.1.4/tenacity/__init__.py`) -> **O(2^N) [Recursive]**
- `iter_state` (@ `tenacity-9.1.4/tenacity/__init__.py`) -> **O(2^N) [Recursive]**
- `wraps` (@ `tenacity-9.1.4/tenacity/__init__.py`) -> **O(2^N) [Recursive]**
- `wraps` (@ `tenacity-9.1.4/tenacity/asyncio/__init__.py`) -> **O(2^N) [Recursive]**
- `__call__` (@ `tenacity-9.1.4/tenacity/asyncio/retry.py`) -> **O(2^N) [Recursive]**
- `__call__` (@ `tenacity-9.1.4/tenacity/retry.py`) -> **O(2^N) [Recursive]**
- `__call__` (@ `tenacity-9.1.4/tenacity/retry.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `test_callstate_repr` (@ `tenacity-9.1.4/tests/test_tenacity.py`) -> DB Complexity: **34**
- `reset` (@ `tenacity-9.1.4/tenacity/__init__.py`) -> DB Complexity: **5**
- `prepare_for_next_attempt` (@ `tenacity-9.1.4/tenacity/__init__.py`) -> DB Complexity: **3**
  * *Intent:* #: Last outcome (result or exception) produced by the function #: Timestamp of the last outcome self.outcome_timestamp: t.Optional[float] = None #: Ti...
- `get_callback_name` (@ `tenacity-9.1.4/tenacity/_utils.py`) -> DB Complexity: **3**
- `_portable_async_sleep` (@ `tenacity-9.1.4/tenacity/asyncio/__init__.py`) -> DB Complexity: **3**
  * *Intent:* # If trio is already imported, then importing it is cheap. # If trio isn't already imported, then it's definitely not running, so we # can skip furthe...
- `setUp` (@ `tenacity-9.1.4/tests/test_after.py`) -> DB Complexity: **2**
- `test_async` (@ `tenacity-9.1.4/tests/test_issue_478.py`) -> DB Complexity: **2**
- `test_issue` (@ `tenacity-9.1.4/tests/test_issue_478.py`) -> DB Complexity: **2**
- `set_result` (@ `tenacity-9.1.4/tenacity/__init__.py`) -> DB Complexity: **1**
  * *Intent:* #: Next action as decided by the retry manager #: Next sleep time as decided by the retry manager. self.upcoming_sleep: float = 0.0 @property def seco...
- `__init__` (@ `tenacity-9.1.4/tenacity/__init__.py`) -> DB Complexity: **1**
  * *Intent:* """Encapsulates the last attempt instance right before giving up."""

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `tenacity-9.1.4/tests` | 7 | 1691.84 | 17.85% | 0.0% |
| `tenacity-9.1.4/tenacity` | 10 | 1211.26 | 23.78% | 49.61% |
| `tenacity-9.1.4/releasenotes/notes` | 43 | 523.6 | 5.0% | 2.33% |
| `tenacity-9.1.4/tenacity/asyncio` | 2 | 278.52 | 51.26% | 50.0% |
| `tenacity-9.1.4` | 2 | 24.16 | 5.0% | 0.0% |
| `tenacity-9.1.4/doc/source` | 1 | 16.26 | 5.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `tenacity-9.1.4/tenacity/asyncio/retry.py` -> **100.0%** Exposure
- `tenacity-9.1.4/tenacity/retry.py` -> **100.0%** Exposure
- `tenacity-9.1.4/tenacity/stop.py` -> **100.0%** Exposure
- `tenacity-9.1.4/tenacity/wait.py` -> **100.0%** Exposure
- `tenacity-9.1.4/releasenotes/notes/wait_exponential_jitter-6ffc81dddcbaa6d3.yaml` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `tenacity-9.1.4/tenacity/wait.py` -> **99.6731%** Exposure
- `tenacity-9.1.4/tenacity/_utils.py` -> **96.5941%** Exposure
- `tenacity-9.1.4/tenacity/stop.py` -> **88.1396%** Exposure
- `tenacity-9.1.4/tenacity/asyncio/retry.py` -> **87.3308%** Exposure
- `tenacity-9.1.4/tenacity/nap.py` -> **79.5168%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tenacity-9.1.4/tenacity/retry.py` -> **0** Orphaned Functions | **22** Duplicates
- `tenacity-9.1.4/tests/test_asyncio.py` -> **22** Orphaned Functions | **0** Duplicates
- `tenacity-9.1.4/tenacity/wait.py` -> **0** Orphaned Functions | **19** Duplicates
- `tenacity-9.1.4/tenacity/stop.py` -> **0** Orphaned Functions | **14** Duplicates
- `tenacity-9.1.4/tenacity/__init__.py` -> **0** Orphaned Functions | **13** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`tenacity-9.1.4/tests/test_tenacity.py`** -> AI Confidence: **99.18%**
2. **`tenacity-9.1.4/tenacity/__init__.py`** -> AI Confidence: **99.07%**
3. **`tenacity-9.1.4/tenacity/asyncio/__init__.py`** -> AI Confidence: **99.07%**
4. **`tenacity-9.1.4/tenacity/before_sleep.py`** -> AI Confidence: **99.06%**
5. **`tenacity-9.1.4/tests/test_asyncio.py`** -> AI Confidence: **99.06%**
6. **`tenacity-9.1.4/tests/test_after.py`** -> AI Confidence: **98.96%**
7. **`tenacity-9.1.4/tests/test_issue_478.py`** -> AI Confidence: **98.96%**
8. **`tenacity-9.1.4/tenacity/tornadoweb.py`** -> AI Confidence: **98.94%**
9. **`tenacity-9.1.4/tenacity/_utils.py`** -> AI Confidence: **98.93%**
10. **`tenacity-9.1.4/tenacity/asyncio/retry.py`** -> AI Confidence: **98.92%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `tenacity-9.1.4/tenacity/__init__.py` -> **100.0%** Exposure
- `tenacity-9.1.4/tenacity/retry.py` -> **100.0%** Exposure
- `tenacity-9.1.4/tests/test_asyncio.py` -> **100.0%** Exposure
- `tenacity-9.1.4/tests/test_issue_478.py` -> **100.0%** Exposure
- `tenacity-9.1.4/tests/test_tenacity.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `tenacity-9.1.4/tenacity/__init__.py` -> **100.0%** Exposure
- `tenacity-9.1.4/tenacity/retry.py` -> **100.0%** Exposure
- `tenacity-9.1.4/tests/test_after.py` -> **100.0%** Exposure
- `tenacity-9.1.4/tests/test_asyncio.py` -> **100.0%** Exposure
- `tenacity-9.1.4/tests/test_issue_478.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `97` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `tenacity-9.1.4/tenacity/asyncio/retry.py` (PYTHON) -> Cumulative Risk: **876.52**
- **Archetype:** `file_cluster_16` (Distance: 10.832 IQR)
- **Magnitude:** 153.42 | **LOC:** 126 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (99.9998%)
- **Heaviest Functions:** `__call__` (Impact: 43.9), `__call__` (Impact: 28.1), `__call__` (Impact: 17.7)

### 2. `tenacity-9.1.4/tenacity/__init__.py` (PYTHON) -> Cumulative Risk: **872.93**
- **Archetype:** `file_cluster_13` (Distance: 10.423 IQR)
- **Magnitude:** 425.86 | **LOC:** 751 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.3374%)
- **Heaviest Functions:** `__repr__` (Impact: 91.8), `_post_stop_check_actions` (Impact: 27.4), `_begin_iter` (Impact: 22.5)

### 3. `tenacity-9.1.4/tenacity/_utils.py` (PYTHON) -> Cumulative Risk: **811.72**
- **Archetype:** `file_cluster_13` (Distance: 12.166 IQR)
- **Magnitude:** 124.48 | **LOC:** 114 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9999%), Documentation (99.8195%), Tech Debt (98.9347%)
- **Heaviest Functions:** `find_ordinal` (Impact: 42.7), `get_callback_name` (Impact: 31.4), `is_coroutine_callable` (Impact: 13.4)

### 4. `tenacity-9.1.4/tenacity/stop.py` (PYTHON) -> Cumulative Risk: **780.56**
- **Archetype:** `file_cluster_16` (Distance: 11.711 IQR)
- **Magnitude:** 94.42 | **LOC:** 131 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9994%), Concurrency (99.988%)
- **Heaviest Functions:** `__call__` (Impact: 14.2), `__call__` (Impact: 14.1), `__call__` (Impact: 5.3)

### 5. `tenacity-9.1.4/tenacity/asyncio/__init__.py` (PYTHON) -> Cumulative Risk: **773.16**
- **Archetype:** `file_cluster_13` (Distance: 9.074 IQR)
- **Magnitude:** 125.1 | **LOC:** 211 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9976%), Documentation (99.9583%)
- **Heaviest Functions:** `__anext__` (Impact: 30.6), `_portable_async_sleep` (Impact: 12.8), `_run_wait` (Impact: 10.7)

### 6. `tenacity-9.1.4/tenacity/retry.py` (PYTHON) -> Cumulative Risk: **757.54**
- **Archetype:** `file_cluster_16` (Distance: 11.176 IQR)
- **Magnitude:** 317.68 | **LOC:** 283 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__call__` (Impact: 52.6), `__call__` (Impact: 43.9), `__call__` (Impact: 28.3)

### 7. `tenacity-9.1.4/tenacity/wait.py` (PYTHON) -> Cumulative Risk: **757.1**
- **Archetype:** `file_cluster_16` (Distance: 11.85 IQR)
- **Magnitude:** 131.7 | **LOC:** 274 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9952%), State Flux (99.6731%)
- **Heaviest Functions:** `__call__` (Impact: 21.2), `__call__` (Impact: 7.3), `__call__` (Impact: 7.3)

### 8. `tenacity-9.1.4/tests/test_issue_478.py` (PYTHON) -> Cumulative Risk: **582.16**
- **Archetype:** `file_cluster_4` (Distance: 11.684 IQR)
- **Magnitude:** 125.44 | **LOC:** 118 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `test_async` (Impact: 37.3), `test_issue` (Impact: 32.6), `wrapper` (Impact: 2.7)

### 9. `tenacity-9.1.4/tests/test_asyncio.py` (PYTHON) -> Cumulative Risk: **489.36**
- **Archetype:** `file_cluster_4` (Distance: 11.176 IQR)
- **Magnitude:** 532.8 | **LOC:** 493 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `test_retry_with_async_result_or` (Impact: 36.5), `test_retry_with_async_result_ror` (Impact: 36.5), `test_retry_with_async_exc` (Impact: 36.4)

### 10. `tenacity-9.1.4/tenacity/nap.py` (PYTHON) -> Cumulative Risk: **376.39**
- **Archetype:** `file_cluster_16` (Distance: 11.741 IQR)
- **Magnitude:** 16.92 | **LOC:** 44 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (79.5168%), Spec Match (73.3333%), Documentation (73.28%), Concurrency (59.4409%)
- **Heaviest Functions:** `sleep` (Impact: 4.2), `__call__` (Impact: 2.8), `__init__` (Impact: 2.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tenacity-9.1.4/tests/test_tenacity.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.365 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.53 IQR)
- **Top Global Matches:** file_cluster_8: 11.365, file_cluster_0: 11.518, file_cluster_13: 11.561
- **Magnitude:** 937.64 | **LOC:** 1807 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (4.9949%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_callstate_repr` (Impact: 650.8 | O(N^5) | DB: 34)
  * `_make_unset_exception` (Impact: 14.2 | O(N^3) | DB: 1)
  * `test_retrying_repr` (Impact: 4.6 | O(N^4))
  * `_set_delay_since_start` (Impact: 2.0 | O(N^1))
    * *Intent:* # Ensure outcome_timestamp - start_time is *exactly* equal to the delay to # avoid complexity in tes...
  * `make_retry_state` (Impact: 1.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 378`, `args: 221`, `func_start: 203`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 75`
* *Architecture:* `api: 163`, `import: 20`
* *Defense:* `safety: 77`, `doc: 48`, `test: 149`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 33.26
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.03125
  * `Imports (Out-Degree: 0):` copy, pytest, time, typing, re, tenacity, fractions, logging...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tenacity-9.1.4/tests/test_asyncio.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.176 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.026 IQR)
- **Top Global Matches:** file_cluster_4: 11.176, file_cluster_0: 11.177, file_cluster_8: 11.233
- **Magnitude:** 532.8 | **LOC:** 493 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (28.8984%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_retry_with_async_result_or` (Impact: 36.5 | O(N^6))
  * `test_retry_with_async_result_ror` (Impact: 36.5 | O(N^6))
  * `test_retry_with_async_exc` (Impact: 36.4 | O(N^6))
  * `test_reraise` (Impact: 30.7 | O(N^5))
  * `test_retry_function_attributes` (Impact: 26.5 | O(N^5))
    * *Intent:* """Test that the wrapped function attributes are exposed as intended. - statistics contains the valu...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 157`, `args: 53`, `func_start: 52`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 1`, `orphaned_logic: 22`
* *Architecture:* `api: 58`, `concurrency: 89`, `import: 13`
* *Defense:* `safety: 36`, `doc: 4`, `test: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.62
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` inspect, pytest, asyncio, tenacity, trio, unittest, tenacity.wait, .test_tenacity...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/tenacity/__init__.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.423 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.871 IQR)
- **Top Global Matches:** file_cluster_13: 10.423, file_cluster_16: 10.491, file_cluster_8: 10.912
- **Magnitude:** 425.86 | **LOC:** 751 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (16.6262%), Tech Debt (97.1304%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 91.8 | O(N^5))
  * `_post_stop_check_actions` (Impact: 27.4 | O(N^5))
  * `_begin_iter` (Impact: 22.5 | O(N^4))
  * `__iter__` (Impact: 22.3 | O(N^4))
  * `_post_retry_check_actions` (Impact: 14.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 210`, `args: 54`, `func_start: 51`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 34`, `duplicate_logic: 13`
* *Architecture:* `io: 1`, `api: 40`, `concurrency: 9`, `import: 59`
* *Defense:* `safety: 15`, `doc: 29`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.62
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` .stop, functools, dataclasses, time, typing, sys, tenacity.tornadoweb, warnings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/tenacity/retry.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.176 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.301 IQR)
- **Top Global Matches:** file_cluster_16: 11.176, file_cluster_8: 11.623, file_cluster_13: 11.633
- **Magnitude:** 317.68 | **LOC:** 283 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (43.7971%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__call__` (Impact: 52.6 | O(2^N))
  * `__call__` (Impact: 43.9 | O(2^N))
  * `__call__` (Impact: 28.3 | O(2^N))
  * `__call__` (Impact: 28.3 | O(2^N))
  * `__call__` (Impact: 28.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 70`, `args: 32`, `func_start: 28`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 14`, `duplicate_logic: 22`
* *Architecture:* `api: 16`, `import: 4`
* *Defense:* `safety: 4`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.62
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typing, abc, re, tenacity
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/tenacity/asyncio/retry.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.832 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.665 IQR)
- **Top Global Matches:** file_cluster_16: 10.832, file_cluster_13: 11.083, file_cluster_8: 11.343
- **Magnitude:** 153.42 | **LOC:** 126 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (48.7982%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__call__` (Impact: 43.9 | O(2^N))
  * `__call__` (Impact: 28.1 | O(2^N))
  * `__call__` (Impact: 17.7 | O(N^4))
  * `__call__` (Impact: 17.7 | O(N^4))
  * `__init__` (Impact: 3.1 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 43`, `args: 13`, `func_start: 13`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 8`, `duplicate_logic: 9`
* *Architecture:* `api: 9`, `concurrency: 9`, `import: 5`
* *Defense:* `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.62
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typing, abc, tenacity
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/tenacity/wait.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.85 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.14 IQR)
- **Top Global Matches:** file_cluster_16: 11.85, file_cluster_13: 12.068, file_cluster_8: 12.296
- **Magnitude:** 131.7 | **LOC:** 274 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (46.502%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__call__` (Impact: 21.2 | O(2^N))
    * *Intent:* """Wait strategy that waits the amount of time returned by the predicate. The predicate is passed th...
  * `__call__` (Impact: 7.3 | O(N^3))
  * `__call__` (Impact: 7.3 | O(N^3))
  * `__radd__` (Impact: 7.2 | O(N^3))
  * `__init__` (Impact: 5.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 53`, `args: 21`, `func_start: 21`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 23`, `duplicate_logic: 19`
* *Architecture:* `api: 12`, `import: 5`
* *Defense:* `safety: 4`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 28.822
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.046875
  * `Imports (Out-Degree: 0):` typing, abc, tenacity, random
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tenacity-9.1.4/tests/test_issue_478.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.684 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.926 IQR)
- **Top Global Matches:** file_cluster_4: 11.684, file_cluster_13: 11.999, file_cluster_0: 12.007
- **Magnitude:** 125.44 | **LOC:** 118 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (46.7165%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_async` (Impact: 37.3 | O(N^4) | DB: 2)
  * `test_issue` (Impact: 32.6 | O(N^4) | DB: 2)
  * `wrapper` (Impact: 2.7 | O(N^2))
  * `asynctest` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 44`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 8`, `orphaned_logic: 2`
* *Architecture:* `api: 11`, `concurrency: 31`, `import: 5`
* *Defense:* `safety: 12`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.62
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typing, asyncio, tenacity, unittest, functools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/tenacity/asyncio/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.074 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.418 IQR)
- **Top Global Matches:** file_cluster_13: 9.074, file_cluster_16: 9.286, file_cluster_8: 9.422
- **Magnitude:** 125.1 | **LOC:** 211 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (53.7296%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__anext__` (Impact: 30.6 | O(N^4))
  * `_portable_async_sleep` (Impact: 12.8 | O(N^3) | DB: 3)
    * *Intent:* # If trio is already imported, then importing it is cheap. # If trio isn't already imported, then it...
  * `_run_wait` (Impact: 10.7 | O(N^3))
  * `wraps` (Impact: 7.9 | O(2^N))
  * `__init__` (Impact: 6.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 75`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 2`
* *Architecture:* `io: 2`, `api: 13`, `concurrency: 19`, `import: 24`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.62
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` tenacity.stop, typing, asyncio, tenacity, sys, trio, sniffio, overhead...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/tenacity/_utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.166 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.994 IQR)
- **Top Global Matches:** file_cluster_13: 12.166, file_cluster_16: 12.233, file_cluster_11: 12.541
- **Magnitude:** 124.48 | **LOC:** 114 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (38.3147%), Tech Debt (98.9347%)
**Top Internal Functions/Classes:**
  * `find_ordinal` (Impact: 42.7 | O(2^N))
  * `get_callback_name` (Impact: 31.4 | O(N^4) | DB: 3)
  * `is_coroutine_callable` (Impact: 13.4 | O(N^2))
  * `to_seconds` (Impact: 9.2 | O(N^2))
  * `inner` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 33`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 9`, `orphaned_logic: 4`
* *Architecture:* `io: 1`, `api: 9`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 9`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.62
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inspect, typing, sys, datetime, functools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/tenacity/stop.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.711 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.332 IQR)
- **Top Global Matches:** file_cluster_16: 11.711, file_cluster_13: 11.896, file_cluster_12: 12.17
- **Magnitude:** 94.42 | **LOC:** 131 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (49.8549%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__call__` (Impact: 14.2 | O(2^N))
  * `__call__` (Impact: 14.1 | O(2^N))
  * `__call__` (Impact: 5.3 | O(N^2))
  * `__call__` (Impact: 5.3 | O(N^2))
  * `__call__` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 41`, `args: 16`, `func_start: 16`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `duplicate_logic: 14`
* *Architecture:* `api: 9`, `concurrency: 7`, `import: 5`
* *Defense:* `doc: 16`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 22.609
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.03125
  * `Imports (Out-Degree: 0):` typing, abc, tenacity, threading
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tenacity-9.1.4/tenacity/before_sleep.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.293 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.339 IQR)
- **Top Global Matches:** file_cluster_8: 8.293, file_cluster_16: 8.417, file_cluster_13: 8.598
- **Magnitude:** 57.26 | **LOC:** 72 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.8401%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `before_sleep_log` (Impact: 52.5 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 9`, `args: 3`, `func_start: 3`
* *Risk/State:* None
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.015625
  * `Imports (Out-Degree: 0):` typing, tenacity
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tenacity-9.1.4/tests/test_tornado.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.427 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.306 IQR)
- **Top Global Matches:** file_cluster_0: 10.427, file_cluster_13: 10.524, file_cluster_8: 10.97
- **Magnitude:** 37.08 | **LOC:** 78 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.7349%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_old_tornado` (Impact: 13.6 | O(N^4))
  * `test_stop_after_attempt` (Impact: 7.3 | O(N^3))
  * `test_retry` (Impact: 2.8 | O(N^2))
  * `test_repr` (Impact: 2.7 | O(N^2))
  * `_retryable_coroutine` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 25`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 8`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 14.62
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .test_tenacity, tornado, tenacity, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/tests/test_after.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.674 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.096 IQR)
- **Top Global Matches:** file_cluster_8: 8.674, file_cluster_13: 8.811, file_cluster_7: 9.138
- **Magnitude:** 35.44 | **LOC:** 76 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (2.167%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_01_default` (Impact: 11.7 | O(N^3))
    * *Intent:* """Test log formatting."""
  * `test_02_custom_sec_format` (Impact: 11.6 | O(N^3))
  * `setUp` (Impact: 4.9 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 13`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `orphaned_logic: 3`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `doc: 4`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.62
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , tenacity, logging, unittest.mock, random
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/tenacity/before.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_16` (Drift: 8.878 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.167 IQR)
- **Top Global Matches:** file_cluster_16: 8.878, file_cluster_13: 9.082, file_cluster_8: 9.172
- **Magnitude:** 18.08 | **LOC:** 47 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.242%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `log_it` (Impact: 12.6 | O(N^3))
  * `before_log` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 9`, `args: 3`, `func_start: 3`
* *Risk/State:* None
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.015625
  * `Imports (Out-Degree: 0):` typing, tenacity
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tenacity-9.1.4/tenacity/after.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_16` (Drift: 8.715 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.891 IQR)
- **Top Global Matches:** file_cluster_16: 8.715, file_cluster_8: 8.919, file_cluster_13: 8.921
- **Magnitude:** 17.54 | **LOC:** 50 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.4992%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `after_log` (Impact: 13.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 9`, `args: 3`, `func_start: 3`
* *Risk/State:* None
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.015625
  * `Imports (Out-Degree: 0):` typing, tenacity
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tenacity-9.1.4/tenacity/nap.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.741 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 8.298 IQR)
- **Top Global Matches:** file_cluster_16: 11.741, file_cluster_13: 11.755, file_cluster_4: 12.395
- **Magnitude:** 16.92 | **LOC:** 44 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sleep` (Impact: 4.2 | O(2^N))
    * *Intent:* """ Sleep strategy that delays execution for a given number of seconds. This is the default strategy...
  * `__call__` (Impact: 2.8 | O(N^2))
  * `__init__` (Impact: 2.7 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 7`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 4`, `concurrency: 2`, `import: 3`
* *Defense:* `doc: 4`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.395
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.015625
  * `Imports (Out-Degree: 0):` time, typing, threading
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tenacity-9.1.4/doc/source/conf.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.425 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.946 IQR)
- **Top Global Matches:** file_cluster_8: 7.425, file_cluster_13: 7.568, file_cluster_7: 8.386
- **Magnitude:** 16.26 | **LOC:** 42 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 7`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.62
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/releasenotes/notes/fix-async-retry-type-overloads-27f3e0c239ed6b.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.658 IQR)
- **Top Global Matches:** file_cluster_8: 4.658, file_cluster_7: 6.346, file_cluster_1: 6.522
- **Magnitude:** 14.68 | **LOC:** 10 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.62
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/releasenotes/notes/add-stop-before-delay-a775f88ac872c923.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.54 IQR)
- **Top Global Matches:** file_cluster_8: 4.54, file_cluster_7: 6.269, file_cluster_1: 6.442
- **Magnitude:** 13.64 | **LOC:** 7 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.62
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/releasenotes/notes/async-sleep-retrying-32de5866f5d041.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 13.64 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.62
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/releasenotes/notes/no-async-iter-6132a42e52348a75.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 13.64 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.62
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/setup.py` (PYTHON | Tier 1 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.582 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.904 IQR)
- **Top Global Matches:** file_cluster_8: 5.582, file_cluster_13: 6.527, file_cluster_7: 7.061
- **Magnitude:** 13.12 | **LOC:** 22 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.62
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` setuptools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/releasenotes/notes/fix-retry-wrapper-attributes-f7a3a45b8e90f257.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.514 IQR)
- **Top Global Matches:** file_cluster_8: 4.514, file_cluster_7: 6.237, file_cluster_1: 6.414
- **Magnitude:** 13.12 | **LOC:** 7 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.62
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/releasenotes/notes/trio-support-retry-22bd544800cd1f36.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.514 IQR)
- **Top Global Matches:** file_cluster_8: 4.514, file_cluster_7: 6.237, file_cluster_1: 6.414
- **Magnitude:** 13.12 | **LOC:** 7 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.62
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tenacity-9.1.4/tests/test_utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.57 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.865 IQR)
- **Top Global Matches:** file_cluster_16: 12.57, file_cluster_8: 12.601, file_cluster_13: 12.701
- **Magnitude:** 12.92 | **LOC:** 42 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (32.4301%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_is_coroutine_callable` (Impact: 5.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 26`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `orphaned_logic: 1`
* *Architecture:* `api: 5`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 12`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 14.62
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tenacity, functools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tenacity-9.1.4/tests/test_tornado.py` (PYTHON) | Magnitude: 37.08 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 25, test: 10, safety: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tenacity-9.1.4/tenacity/_utils.py` (PYTHON) | Magnitude: 124.48 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 33, branch: 19, safety_bypasses: 13
- `tenacity-9.1.4/tenacity/__init__.py` (PYTHON) | Magnitude: 425.86 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 460, structural_boundaries: 210, generics: 113, encapsulation: 102
- `tenacity-9.1.4/tenacity/asyncio/__init__.py` (PYTHON) | Magnitude: 125.1 | Delta: **0.212 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 129, structural_boundaries: 75, generics: 27, encapsulation: 26
- `tenacity-9.1.4/tenacity/tornadoweb.py` (PYTHON) | Magnitude: 7.32 | Delta: **0.641 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 17, safety_bypasses: 8, import: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tenacity-9.1.4/tenacity/nap.py` (PYTHON) | Magnitude: 16.92 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 6, api: 4, doc: 4
- `tenacity-9.1.4/tests/test_utils.py` (PYTHON) | Magnitude: 12.92 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 26, encapsulation: 17, test: 13
- `tenacity-9.1.4/tenacity/stop.py` (PYTHON) | Magnitude: 94.42 | Delta: **0.185 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 41, encapsulation: 25, generics: 17
- `tenacity-9.1.4/tenacity/after.py` (PYTHON) | Magnitude: 17.54 | Delta: **0.204 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 9, api: 4, doc: 4
- `tenacity-9.1.4/tenacity/before.py` (PYTHON) | Magnitude: 18.08 | Delta: **0.204 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 9, api: 4, doc: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tenacity-9.1.4/tests/test_asyncio.py` (PYTHON) | Magnitude: 532.8 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 323, structural_boundaries: 157, concurrency: 89, api: 58
- `tenacity-9.1.4/tests/test_issue_478.py` (PYTHON) | Magnitude: 125.44 | Delta: **0.315 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 44, concurrency: 31, generics: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `tenacity-9.1.4/tenacity/before_sleep.py` (PYTHON) | Magnitude: 57.26 | Delta: **0.124 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 32, branch: 9, structural_boundaries: 9, encapsulation: 5
- `tenacity-9.1.4/tests/test_after.py` (PYTHON) | Magnitude: 35.44 | Delta: **0.137 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 13, test: 9, test_skip: 8
- `tenacity-9.1.4/doc/source/conf.py` (PYTHON) | Magnitude: 16.26 | Delta: **0.143 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: io: 7, indent_spaces: 3, structural_boundaries: 2, import: 2
- `tenacity-9.1.4/tests/test_tenacity.py` (PYTHON) | Magnitude: 937.64 | Delta: **0.153 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1247, structural_boundaries: 378, args: 221, func_start: 203

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tenacity-9.1.4/tenacity/tornadoweb.py` -> **Severity: 1.25** (Embedded: 0.0156 * Error Risk: 80.0%)
- `tenacity-9.1.4/tenacity/wait.py` -> **Severity: 0.496** (Embedded: 0.0469 * Error Risk: 10.5731%)
- `tenacity-9.1.4/tenacity/stop.py` -> **Severity: 0.315** (Embedded: 0.0312 * Error Risk: 10.0795%)
- `tenacity-9.1.4/tenacity/nap.py` -> **Severity: 0.161** (Embedded: 0.0156 * Error Risk: 10.3042%)
- `tenacity-9.1.4/tests/test_tenacity.py` -> **Severity: 0.092** (Embedded: 0.0312 * Error Risk: 2.9537%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tenacity-9.1.4/tenacity/wait.py` -> **Severity: 2843.011** (Blast Radius: 28.822 * Doc Risk: 98.6403%)
- `tenacity-9.1.4/tenacity/stop.py` -> **Severity: 2259.763** (Blast Radius: 22.609 * Doc Risk: 99.9497%)
- `tenacity-9.1.4/tenacity/before.py` -> **Severity: 1639.498** (Blast Radius: 16.395 * Doc Risk: 99.9999%)
- `tenacity-9.1.4/tenacity/after.py` -> **Severity: 1639.482** (Blast Radius: 16.395 * Doc Risk: 99.9989%)
- `tenacity-9.1.4/tenacity/before_sleep.py` -> **Severity: 1638.867** (Blast Radius: 16.395 * Doc Risk: 99.9614%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
