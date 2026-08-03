# ARCHITECTURAL_BRIEF: cachetools
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/cachetools` |
| **Timestamp** | `2026-08-03T21:19:49.047359+00:00` |
| **Scan Duration** | `0.22s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 19 malicious artifacts.

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
| Total Artifacts | 27 |
| Analyzed Artifacts (Scanned) | 20 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7 |
| Total LOC | 3401 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 74.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.64 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6667 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3333 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 19 | 3401 | 95.0% |
| PLAINTEXT | 1 | 0 | 5.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `7.025`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 16 | 80.0% |
| file_cluster_13 | 3 | 15.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 5.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7*

**Composition by Extension & Reason:**
- `.rst`: 2x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 2.8 | 48.3 | 13.2 | 5.0 | 40.6 |
| Error & Exception Exposure | 0.0 | 15.5 | 4.9 | 4.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 10.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 12.6 | 0.0 | 0.0 |
| API Exposure | 1.8 | 11.3 | 6.6 | 7.0 | 1.8 |
| Concurrency Exposure | 0.0 | 99.9 | 5.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 19.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 33.3 | 100.0 | 96.5 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 25.2 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 91.6 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 66.4 | 100.0 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 5.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `cachetools-7.0.5/tests/__init__.py` (Hits: 1)
- `cachetools-7.0.5/MANIFEST.in` (Hits: 0)
- `cachetools-7.0.5/src/cachetools/__init__.py` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **keys.py** (`cachetools-7.0.5/src/cachetools/keys.py`) — 2 inbound connections
2. **_cached.py** (`cachetools-7.0.5/src/cachetools/_cached.py`) — 1 inbound connections
3. **_cachedmethod.py** (`cachetools-7.0.5/src/cachetools/_cachedmethod.py`) — 1 inbound connections
4. **func.py** (`cachetools-7.0.5/src/cachetools/func.py`) — 1 inbound connections
5. **MANIFEST.in** (`cachetools-7.0.5/MANIFEST.in`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`cachetools-7.0.5/src/cachetools/__init__.py`) — 9 outbound dependencies
2. **test_cachedmethod.py** (`cachetools-7.0.5/tests/test_cachedmethod.py`) — 8 outbound dependencies
3. **func.py** (`cachetools-7.0.5/src/cachetools/func.py`) — 6 outbound dependencies
4. **test_cached.py** (`cachetools-7.0.5/tests/test_cached.py`) — 5 outbound dependencies
5. **test_threading.py** (`cachetools-7.0.5/tests/test_threading.py`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `popitem` (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> Impact: **353.9** | LOC: 219
- `_condition_info` (@ `cachetools-7.0.5/src/cachetools/_cachedmethod.py`) -> Impact: **94.9** | LOC: 46
- `_wrapper` (@ `cachetools-7.0.5/src/cachetools/_cached.py`) -> Impact: **91.5** | LOC: 31
- `__repr__` (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> Impact: **89.0** | LOC: 134
- `_condition_info` (@ `cachetools-7.0.5/src/cachetools/_cached.py`) -> Impact: **81.5** | LOC: 42
- `_wrapper` (@ `cachetools-7.0.5/src/cachetools/_cachedmethod.py`) -> Impact: **80.7** | LOC: 27
- `popitem` (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> Impact: **76.5** | LOC: 76
- `popitem` (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> Impact: **72.6** | LOC: 67
- `_condition` (@ `cachetools-7.0.5/src/cachetools/_cachedmethod.py`) -> Impact: **68.6** | LOC: 49
- `__get__` (@ `cachetools-7.0.5/src/cachetools/_cachedmethod.py`) -> Impact: **68.0** | LOC: 39
  * *Intent:* # through the class to support class-level introspection, such # as for mocking with autospec=True in unittest.mock. pass elif self.__attrname is not ...

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `popitem` (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> **O(2^N) [Recursive]**
- `popitem` (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> **O(2^N) [Recursive]**
- `__setitem__` (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> **O(2^N) [Recursive]**
- `__getitem__` (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # removing an existing item would break the heap structure, so # only mark it as removed for now try: self.__getitem(key).removed = True except KeyErr...
- `__setitem__` (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> **O(2^N) [Recursive]**
- `__delitem__` (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> **O(2^N) [Recursive]**
- `__setitem__` (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> **O(2^N) [Recursive]**
- `__delitem__` (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> **O(2^N) [Recursive]**
- `__delitem__` (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> **O(2^N) [Recursive]**
- `__getitem__` (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `popitem` (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> DB Complexity: **20**
- `test_pop` (@ `cachetools-7.0.5/tests/__init__.py`) -> DB Complexity: **9**
- `_condition_info` (@ `cachetools-7.0.5/src/cachetools/_cachedmethod.py`) -> DB Complexity: **7**
- `__repr__` (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> DB Complexity: **6**
- `popitem` (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> DB Complexity: **6**
- `test_pickle_maxsize` (@ `cachetools-7.0.5/tests/__init__.py`) -> DB Complexity: **6**
- `__init__` (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> DB Complexity: **5**
- `_locked_info` (@ `cachetools-7.0.5/src/cachetools/_cachedmethod.py`) -> DB Complexity: **5**
- `__init__` (@ `cachetools-7.0.5/src/cachetools/_cachedmethod.py`) -> DB Complexity: **5**
- `_unlocked_info` (@ `cachetools-7.0.5/src/cachetools/_cachedmethod.py`) -> DB Complexity: **5**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `cachetools-7.0.5/src/cachetools` | 5 | 2392.96 | 31.52% | 39.21% |
| `cachetools-7.0.5/tests` | 14 | 1309.86 | 6.61% | 0.0% |
| `cachetools-7.0.5` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `cachetools-7.0.5/src/cachetools/__init__.py` -> **99.9584%** Exposure
- `cachetools-7.0.5/src/cachetools/_cachedmethod.py` -> **96.0691%** Exposure
### Highest State Flux (Mutation/Volatility)
- `cachetools-7.0.5/src/cachetools/__init__.py` -> **99.9615%** Exposure
- `cachetools-7.0.5/src/cachetools/_cachedmethod.py` -> **99.7704%** Exposure
- `cachetools-7.0.5/src/cachetools/_cached.py` -> **99.7517%** Exposure
- `cachetools-7.0.5/src/cachetools/keys.py` -> **79.5168%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `cachetools-7.0.5/tests/test_cachedmethod.py` -> **29** Orphaned Functions | **4** Duplicates
- `cachetools-7.0.5/tests/test_cached.py` -> **17** Orphaned Functions | **14** Duplicates
- `cachetools-7.0.5/src/cachetools/__init__.py` -> **0** Orphaned Functions | **23** Duplicates
- `cachetools-7.0.5/tests/__init__.py` -> **20** Orphaned Functions | **2** Duplicates
- `cachetools-7.0.5/tests/test_tlru.py` -> **10** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`cachetools-7.0.5/src/cachetools/__init__.py`** -> AI Confidence: **99.15%**
2. **`cachetools-7.0.5/tests/test_cachedmethod.py`** -> AI Confidence: **99.07%**
3. **`cachetools-7.0.5/src/cachetools/_cached.py`** -> AI Confidence: **98.96%**
4. **`cachetools-7.0.5/src/cachetools/func.py`** -> AI Confidence: **98.93%**
5. **`cachetools-7.0.5/tests/test_threading.py`** -> AI Confidence: **98.93%**
6. **`cachetools-7.0.5/tests/test_keys.py`** -> AI Confidence: **98.92%**
7. **`cachetools-7.0.5/tests/test_lfu.py`** -> AI Confidence: **98.92%**
8. **`cachetools-7.0.5/src/cachetools/_cachedmethod.py`** -> AI Confidence: **98.89%**
9. **`cachetools-7.0.5/src/cachetools/keys.py`** -> AI Confidence: **98.89%**
10. **`cachetools-7.0.5/tests/__init__.py`** -> AI Confidence: **98.89%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `cachetools-7.0.5/src/cachetools/__init__.py` -> **100.0%** Exposure
- `cachetools-7.0.5/src/cachetools/_cached.py` -> **100.0%** Exposure
- `cachetools-7.0.5/src/cachetools/_cachedmethod.py` -> **100.0%** Exposure
- `cachetools-7.0.5/tests/__init__.py` -> **100.0%** Exposure
- `cachetools-7.0.5/tests/test_cachedmethod.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `cachetools-7.0.5/tests/__init__.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `cachetools-7.0.5/src/cachetools/__init__.py` -> **100.0%** Exposure
- `cachetools-7.0.5/src/cachetools/_cached.py` -> **100.0%** Exposure
- `cachetools-7.0.5/src/cachetools/_cachedmethod.py` -> **100.0%** Exposure
- `cachetools-7.0.5/tests/__init__.py` -> **100.0%** Exposure
- `cachetools-7.0.5/tests/test_cachedmethod.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `61` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `cachetools-7.0.5/src/cachetools/__init__.py` (PYTHON) -> Cumulative Risk: **785.81**
- **Archetype:** `file_cluster_13` (Distance: 12.642 IQR)
- **Magnitude:** 1170.38 | **LOC:** 773 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9692%)
- **Heaviest Functions:** `popitem` (Impact: 353.9), `__repr__` (Impact: 89.0), `popitem` (Impact: 76.5)

### 2. `cachetools-7.0.5/src/cachetools/_cachedmethod.py` (PYTHON) -> Cumulative Risk: **705.52**
- **Archetype:** `file_cluster_8` (Distance: 12.31 IQR)
- **Magnitude:** 653.42 | **LOC:** 420 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9953%)
- **Heaviest Functions:** `_condition_info` (Impact: 94.9), `_wrapper` (Impact: 80.7), `_condition` (Impact: 68.6)

### 3. `cachetools-7.0.5/src/cachetools/keys.py` (PYTHON) -> Cumulative Risk: **637.52**
- **Archetype:** `file_cluster_8` (Distance: 10.693 IQR)
- **Magnitude:** 62.86 | **LOC:** 67 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (99.9978%), Documentation (99.9887%), Algorithmic Dos (98.919%)
- **Heaviest Functions:** `__hash__` (Impact: 14.1), `typedkey` (Impact: 13.6), `hashkey` (Impact: 8.2)

### 4. `cachetools-7.0.5/src/cachetools/_cached.py` (PYTHON) -> Cumulative Risk: **599.78**
- **Archetype:** `file_cluster_8` (Distance: 12.048 IQR)
- **Magnitude:** 419.06 | **LOC:** 260 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9963%)
- **Heaviest Functions:** `_wrapper` (Impact: 91.5), `_condition_info` (Impact: 81.5), `_condition` (Impact: 67.7)

### 5. `cachetools-7.0.5/tests/__init__.py` (PYTHON) -> Cumulative Risk: **495.78**
- **Archetype:** `file_cluster_8` (Distance: 10.546 IQR)
- **Magnitude:** 270.86 | **LOC:** 384 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `test_missing` (Impact: 46.2), `test_pop` (Impact: 14.8), `_test_getsizeof` (Impact: 12.5)

### 6. `cachetools-7.0.5/src/cachetools/func.py` (PYTHON) -> Cumulative Risk: **422.88**
- **Archetype:** `file_cluster_13` (Distance: 8.979 IQR)
- **Magnitude:** 87.24 | **LOC:** 106 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (98.5163%), Verification (80.0%), Documentation (79.3354%)
- **Heaviest Functions:** `ttl_cache` (Impact: 13.9), `rr_cache` (Impact: 12.4), `fifo_cache` (Impact: 10.8)

### 7. `cachetools-7.0.5/tests/test_classmethod.py` (PYTHON) -> Cumulative Risk: **372.71**
- **Archetype:** `file_cluster_8` (Distance: 8.36 IQR)
- **Magnitude:** 90.92 | **LOC:** 152 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Stability (50.0%)
- **Heaviest Functions:** `test` (Impact: 11.6), `test_typed` (Impact: 11.5), `test_locked` (Impact: 7.5)

### 8. `cachetools-7.0.5/tests/test_keys.py` (PYTHON) -> Cumulative Risk: **370.06**
- **Archetype:** `file_cluster_8` (Distance: 7.353 IQR)
- **Magnitude:** 49.72 | **LOC:** 93 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9982%), Logic Bomb (98.9743%), Stability (50.0%)
- **Heaviest Functions:** `test_methodkey` (Impact: 7.8), `test_hashkey` (Impact: 7.7), `test_typedkey` (Impact: 7.7)

### 9. `cachetools-7.0.5/tests/test_threading.py` (PYTHON) -> Cumulative Risk: **368.28**
- **Archetype:** `file_cluster_8` (Distance: 9.158 IQR)
- **Magnitude:** 58.62 | **LOC:** 63 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9234%), Algorithmic Dos (94.516%), Stability (50.0%)
- **Heaviest Functions:** `func` (Impact: 15.9), `test_cached_stampede` (Impact: 14.5), `test_cachedmethod_stampede` (Impact: 14.5)

### 10. `cachetools-7.0.5/tests/test_ttl.py` (PYTHON) -> Cumulative Risk: **367.12**
- **Archetype:** `file_cluster_8` (Distance: 8.32 IQR)
- **Magnitude:** 94.02 | **LOC:** 246 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9996%), Stability (50.0%)
- **Heaviest Functions:** `test_ttl` (Impact: 16.6), `test_ttl_expire` (Impact: 9.4), `test_ttl_tuple_key` (Impact: 7.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `cachetools-7.0.5/src/cachetools/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.642 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.928 IQR)
- **Top Global Matches:** file_cluster_13: 12.642, file_cluster_8: 12.665, file_cluster_0: 12.751
- **Magnitude:** 1170.38 | **LOC:** 773 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (40.5596%), Tech Debt (99.9584%)
**Top Internal Functions/Classes:**
  * `popitem` (Impact: 353.9 | O(2^N) | DB: 20)
  * `__repr__` (Impact: 89.0 | O(N^4) | DB: 6)
  * `popitem` (Impact: 76.5 | O(N^5) | DB: 3)
  * `popitem` (Impact: 72.6 | O(2^N) | DB: 6)
  * `__setitem__` (Impact: 45.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 212`, `args: 99`, `func_start: 98`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 143`, `duplicate_logic: 23`
* *Architecture:* `api: 51`, `import: 9`
* *Defense:* `safety: 31`, `doc: 58`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` random, heapq, ._cached, , collections, collections.abc, ._cachedmethod, functools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/src/cachetools/_cachedmethod.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.31 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.861 IQR)
- **Top Global Matches:** file_cluster_8: 12.31, file_cluster_0: 12.436, file_cluster_13: 12.459
- **Magnitude:** 653.42 | **LOC:** 420 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (48.2654%), Tech Debt (96.0691%)
**Top Internal Functions/Classes:**
  * `_condition_info` (Impact: 94.9 | O(N^6) | DB: 7)
  * `_wrapper` (Impact: 80.7 | O(N^3))
  * `_condition` (Impact: 68.6 | O(N^5) | DB: 3)
  * `__get__` (Impact: 68.0 | O(N^5))
    * *Intent:* # through the class to support class-level introspection, such # as for mocking with autospec=True i...
  * `_locked_info` (Impact: 61.9 | O(N^6) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 123`, `args: 51`, `func_start: 51`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 66`, `duplicate_logic: 7`
* *Architecture:* `api: 37`, `import: 3`
* *Defense:* `safety: 32`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 60.897
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.052632
  * `Imports (Out-Degree: 0):` weakref, warnings, functools
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cachetools-7.0.5/src/cachetools/_cached.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.048 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.911 IQR)
- **Top Global Matches:** file_cluster_8: 12.048, file_cluster_13: 12.404, file_cluster_0: 12.462
- **Magnitude:** 419.06 | **LOC:** 260 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (37.6632%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_wrapper` (Impact: 91.5 | O(N^3))
  * `_condition_info` (Impact: 81.5 | O(N^5) | DB: 4)
  * `_condition` (Impact: 67.7 | O(N^5) | DB: 2)
  * `_locked_info` (Impact: 44.7 | O(N^4) | DB: 3)
  * `_locked` (Impact: 34.7 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 69`, `args: 26`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 42`
* *Architecture:* `api: 19`, `import: 1`
* *Defense:* `safety: 28`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 60.897
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.052632
  * `Imports (Out-Degree: 0):` functools
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cachetools-7.0.5/tests/test_cachedmethod.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.794 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.06 IQR)
- **Top Global Matches:** file_cluster_8: 8.794, file_cluster_0: 9.454, file_cluster_7: 9.5
- **Magnitude:** 304.44 | **LOC:** 698 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (3.8318%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_decorator_immutable_dict` (Impact: 14.8 | O(N^4) | DB: 2)
  * `test_decorator_slots` (Impact: 14.5 | O(N^4) | DB: 1)
  * `test_decorator_cond_error` (Impact: 11.1 | O(N^3))
  * `test_decorator_different_names` (Impact: 10.9 | O(N^5))
  * `test_decorator_cond_info` (Impact: 10.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 103`, `args: 81`, `func_start: 55`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 12`, `duplicate_logic: 4`, `orphaned_logic: 29`
* *Architecture:* `api: 62`, `import: 8`
* *Defense:* `safety: 4`, `doc: 2`, `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, unittest.mock, gc, weakref, , warnings, cachetools, fractions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.546 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.778 IQR)
- **Top Global Matches:** file_cluster_8: 10.546, file_cluster_13: 10.935, file_cluster_0: 11.157
- **Magnitude:** 270.86 | **LOC:** 384 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (23.2176%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_missing` (Impact: 46.2 | O(N^4) | DB: 5)
  * `test_pop` (Impact: 14.8 | O(N^3) | DB: 9)
  * `_test_getsizeof` (Impact: 12.5 | O(N^3) | DB: 2)
  * `test_missing_getsizeof` (Impact: 12.0 | O(N^5))
  * `test_pickle` (Impact: 11.6 | O(N^2) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 46`, `args: 29`, `func_start: 26`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 3`, `state_mutation: 55`, `duplicate_logic: 2`, `orphaned_logic: 20`
* *Architecture:* `io: 1`, `api: 25`, `import: 4`
* *Defense:* `safety: 5`, `test: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, pickle, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_cached.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.371 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.996 IQR)
- **Top Global Matches:** file_cluster_8: 7.371, file_cluster_7: 8.361, file_cluster_1: 8.587
- **Magnitude:** 152.78 | **LOC:** 399 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (2.8066%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `func` (Impact: 12.3 | O(N^3) | DB: 1)
  * `test_decorator_lock_condition_info` (Impact: 4.8 | O(N^3))
  * `test_decorator_typed` (Impact: 4.0 | O(N^2))
  * `test_decorator` (Impact: 3.8 | O(N^2))
  * `test_decorator_lock_info` (Impact: 3.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 45`, `args: 31`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `state_mutation: 3`, `duplicate_logic: 14`, `orphaned_logic: 17`
* *Architecture:* `api: 35`, `import: 5`
* *Defense:* `safety: 1`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unittest, cachetools.keys, , warnings, cachetools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_tlru.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.256 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.099 IQR)
- **Top Global Matches:** file_cluster_8: 8.256, file_cluster_7: 9.124, file_cluster_13: 9.283
- **Magnitude:** 110.44 | **LOC:** 330 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (4.2508%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_ttu` (Impact: 17.7 | O(N^3) | DB: 1)
  * `test_ttu_expire` (Impact: 9.4 | O(N^3))
  * `test_ttu_heap_cleanup` (Impact: 8.3 | O(N^3))
  * `test_ttu_tuple_key` (Impact: 7.4 | O(N^3))
  * `__call__` (Impact: 7.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 28`, `args: 23`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `state_mutation: 8`, `duplicate_logic: 2`, `orphaned_logic: 10`
* *Architecture:* `api: 14`, `import: 4`
* *Defense:* `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, , cachetools, math
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_ttl.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.32 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.99 IQR)
- **Top Global Matches:** file_cluster_8: 8.32, file_cluster_13: 9.141, file_cluster_7: 9.17
- **Magnitude:** 94.02 | **LOC:** 246 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (5.0497%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_ttl` (Impact: 16.6 | O(N^3) | DB: 1)
  * `test_ttl_expire` (Impact: 9.4 | O(N^3))
  * `test_ttl_tuple_key` (Impact: 7.4 | O(N^3))
  * `__call__` (Impact: 7.1 | O(N^3))
  * `__init__` (Impact: 6.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 27`, `args: 12`, `func_start: 12`, `class_start: 3`
* *Risk/State:* `state_mutation: 8`, `duplicate_logic: 2`, `orphaned_logic: 9`
* *Architecture:* `api: 12`, `import: 5`
* *Defense:* `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, , datetime, math, cachetools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_classmethod.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.36 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.189 IQR)
- **Top Global Matches:** file_cluster_8: 8.36, file_cluster_0: 8.844, file_cluster_13: 8.957
- **Magnitude:** 90.92 | **LOC:** 152 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (7.9435%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 11.6 | O(N^3) | DB: 1)
  * `test_typed` (Impact: 11.5 | O(N^3))
  * `test_locked` (Impact: 7.5 | O(N^3))
  * `test_condition` (Impact: 7.5 | O(N^3))
  * `test_clear` (Impact: 7.5 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 26`, `args: 17`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `state_mutation: 1`, `orphaned_logic: 7`
* *Architecture:* `api: 13`, `concurrency: 3`, `import: 4`
* *Defense:* `test: 9`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, threading, cachetools, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/src/cachetools/func.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.979 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.499 IQR)
- **Top Global Matches:** file_cluster_13: 8.979, file_cluster_8: 9.044, file_cluster_7: 9.278
- **Magnitude:** 87.24 | **LOC:** 106 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (12.4378%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ttl_cache` (Impact: 13.9 | O(N^2))
    * *Intent:* """ if maxsize is None: return _cache({}, None, typed) elif callable(maxsize): return _cache(RRCache...
  * `rr_cache` (Impact: 12.4 | O(N^2))
  * `fifo_cache` (Impact: 10.8 | O(N^2))
  * `lfu_cache` (Impact: 10.8 | O(N^2))
  * `lru_cache` (Impact: 10.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 40`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 8`, `concurrency: 1`, `import: 8`
* *Defense:* `doc: 12`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 79.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.052632
  * `Imports (Out-Degree: 0):` random, threading, , math, functools, time
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cachetools-7.0.5/src/cachetools/keys.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.693 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.646 IQR)
- **Top Global Matches:** file_cluster_8: 10.693, file_cluster_7: 10.811, file_cluster_1: 11.08
- **Magnitude:** 62.86 | **LOC:** 67 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (18.6867%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__hash__` (Impact: 14.1 | O(2^N) | DB: 1)
  * `typedkey` (Impact: 13.6 | O(N^2))
  * `hashkey` (Impact: 8.2 | O(N^2))
    * *Intent:* # A sentinel for separating args from kwargs. Using the class itself # ensures uniqueness and preser...
  * `__add__` (Impact: 6.1 | O(2^N))
  * `__radd__` (Impact: 3.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 20`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 7`
* *Defense:* `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 115.385
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.105263
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `cachetools-7.0.5/tests/test_threading.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.158 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.073 IQR)
- **Top Global Matches:** file_cluster_8: 9.158, file_cluster_13: 9.197, file_cluster_0: 9.431
- **Magnitude:** 58.62 | **LOC:** 63 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (15.2237%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `func` (Impact: 15.9 | O(2^N))
  * `test_cached_stampede` (Impact: 14.5 | O(N^3))
  * `test_cachedmethod_stampede` (Impact: 14.5 | O(N^3))
  * `meth` (Impact: 2.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 14`, `args: 6`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 2`
* *Architecture:* `api: 5`, `concurrency: 5`, `import: 5`
* *Defense:* `safety: 1`, `test: 6`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, threading, os, time, cachetools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_func.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.905 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.653 IQR)
- **Top Global Matches:** file_cluster_8: 8.905, file_cluster_7: 9.502, file_cluster_13: 9.607
- **Magnitude:** 54.22 | **LOC:** 125 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (3.6884%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_decorator_needs_rlock` (Impact: 11.6 | O(N^5) | DB: 2)
    * *Intent:* """This will deadlock on a cache that uses a regular lock. https://github.com/python/cpython/blob/3....
  * `test_decorator_typed` (Impact: 3.2 | O(N^2))
  * `decorator` (Impact: 3.1 | O(N^2))
  * `test_decorator` (Impact: 3.1 | O(N^2))
  * `test_decorator_clear` (Impact: 3.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 23`, `args: 18`, `func_start: 11`, `class_start: 7`
* *Risk/State:* `state_mutation: 4`, `orphaned_logic: 7`
* *Architecture:* `api: 15`, `import: 2`
* *Defense:* `doc: 2`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unittest, cachetools.func
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_keys.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.353 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.652 IQR)
- **Top Global Matches:** file_cluster_8: 7.353, file_cluster_13: 8.296, file_cluster_7: 8.375
- **Magnitude:** 49.72 | **LOC:** 93 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (8.5472%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_methodkey` (Impact: 7.8 | O(N^3))
    * *Intent:* # similar to hashkey(), but ignores its first positional argument self.assertEqual(key("x"), key("y"...
  * `test_hashkey` (Impact: 7.7 | O(N^3))
  * `test_typedkey` (Impact: 7.7 | O(N^3))
  * `test_typedmethodkey` (Impact: 7.7 | O(N^3))
    * *Intent:* # similar to typedkey(), but ignores its first positional argument self.assertEqual(key("x"), key("y...
  * `test_pickle` (Impact: 7.5 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 13`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unittest, pickle, cachetools.keys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_rr.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.528 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.728 IQR)
- **Top Global Matches:** file_cluster_8: 7.528, file_cluster_13: 8.386, file_cluster_7: 8.548
- **Magnitude:** 33.54 | **LOC:** 89 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.9729%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_rr_getsizeof` (Impact: 8.0 | O(N^3))
  * `test_rr_bad_choice` (Impact: 7.6 | O(N^3))
  * `test_rr` (Impact: 3.8 | O(N^2))
  * `test_rr_update_existing` (Impact: 3.1 | O(N^2))
  * `test_rr_default_choice` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 13`, `args: 7`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 5`
* *Architecture:* `api: 7`, `import: 4`
* *Defense:* `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, , random, cachetools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_lfu.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.485 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.451 IQR)
- **Top Global Matches:** file_cluster_8: 7.485, file_cluster_13: 8.283, file_cluster_7: 8.474
- **Magnitude:** 31.0 | **LOC:** 91 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (3.5573%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_lfu` (Impact: 8.9 | O(N^2))
  * `test_lfu_getsizeof` (Impact: 8.0 | O(N^3))
  * `test_lfu_clear` (Impact: 3.7 | O(N^2) | DB: 1)
  * `test_lfu_update_existing` (Impact: 3.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 10`, `args: 5`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, , cachetools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_lru.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.3 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.45 IQR)
- **Top Global Matches:** file_cluster_8: 7.3, file_cluster_13: 8.16, file_cluster_7: 8.325
- **Magnitude:** 25.8 | **LOC:** 90 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (3.5319%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_lru_getsizeof` (Impact: 8.0 | O(N^3))
  * `test_lru` (Impact: 3.8 | O(N^2))
  * `test_lru_clear` (Impact: 3.6 | O(N^2) | DB: 1)
  * `test_lru_update_existing` (Impact: 3.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 10`, `args: 5`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, , cachetools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_fifo.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.086 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.596 IQR)
- **Top Global Matches:** file_cluster_8: 7.086, file_cluster_13: 8.029, file_cluster_7: 8.175
- **Magnitude:** 19.9 | **LOC:** 69 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.9762%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_fifo_getsizeof` (Impact: 8.0 | O(N^3))
  * `test_fifo` (Impact: 3.8 | O(N^2))
  * `test_fifo_update_existing` (Impact: 3.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 9`, `args: 4`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 3`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, , cachetools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_cache.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.177 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.267 IQR)
- **Top Global Matches:** file_cluster_13: 8.177, file_cluster_8: 8.447, file_cluster_7: 9.347
- **Magnitude:** 13.6 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, , cachetools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/MANIFEST.in` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `cachetools-7.0.5/src/cachetools/__init__.py` (PYTHON) | Magnitude: 1170.38 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 541, encapsulation: 280, structural_boundaries: 212, state_mutation: 143
- `cachetools-7.0.5/src/cachetools/func.py` (PYTHON) | Magnitude: 87.24 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 40, encapsulation: 21, branch: 17
- `cachetools-7.0.5/tests/test_cache.py` (PYTHON) | Magnitude: 13.6 | Delta: **0.27 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, test: 3, import: 3, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `cachetools-7.0.5/tests/test_threading.py` (PYTHON) | Magnitude: 58.62 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 14, branch: 8, args: 6
- `cachetools-7.0.5/src/cachetools/keys.py` (PYTHON) | Magnitude: 62.86 | Delta: **0.118 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 26, encapsulation: 22, structural_boundaries: 20, doc: 12
- `cachetools-7.0.5/src/cachetools/_cachedmethod.py` (PYTHON) | Magnitude: 653.42 | Delta: **0.126 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 299, encapsulation: 145, structural_boundaries: 123, state_mutation: 66
- `cachetools-7.0.5/src/cachetools/_cached.py` (PYTHON) | Magnitude: 419.06 | Delta: **0.356 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 192, structural_boundaries: 69, branch: 48, state_mutation: 42
- `cachetools-7.0.5/tests/__init__.py` (PYTHON) | Magnitude: 270.86 | Delta: **0.389 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 289, state_mutation: 55, structural_boundaries: 46, args: 29

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `cachetools-7.0.5/src/cachetools/keys.py` -> **Severity: 0.845** (Embedded: 0.1053 * Error Risk: 8.0284%)
- `cachetools-7.0.5/src/cachetools/_cachedmethod.py` -> **Severity: 0.472** (Embedded: 0.0526 * Error Risk: 8.9713%)
- `cachetools-7.0.5/src/cachetools/_cached.py` -> **Severity: 0.375** (Embedded: 0.0526 * Error Risk: 7.1234%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cachetools-7.0.5/src/cachetools/keys.py` -> **Severity: 11537.196** (Blast Radius: 115.385 * Doc Risk: 99.9887%)
- `cachetools-7.0.5/src/cachetools/func.py` -> **Severity: 6272.257** (Blast Radius: 79.06 * Doc Risk: 79.3354%)
- `cachetools-7.0.5/src/cachetools/_cached.py` -> **Severity: 6089.475** (Blast Radius: 60.897 * Doc Risk: 99.9963%)
- `cachetools-7.0.5/src/cachetools/_cachedmethod.py` -> **Severity: 6089.414** (Blast Radius: 60.897 * Doc Risk: 99.9953%)
- `cachetools-7.0.5/src/cachetools/__init__.py` -> **Severity: 4272.184** (Blast Radius: 42.735 * Doc Risk: 99.9692%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
