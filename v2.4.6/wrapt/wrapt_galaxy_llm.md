# ARCHITECTURAL_BRIEF: wrapt
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/wrapt` |
| **Timestamp** | `2026-08-03T21:26:24.103772+00:00` |
| **Scan Duration** | `0.48s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 79 malicious artifacts.

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
| Total Artifacts | 120 |
| Analyzed Artifacts (Scanned) | 81 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 39 |
| Total LOC | 8872 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 67.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4002 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.303 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.4396 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 78 | 8471 | 96.3% |
| PLAINTEXT | 1 | 0 | 1.2% |
| MARKDOWN | 1 | 0 | 1.2% |
| C | 1 | 401 | 1.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.486`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_16 | 30 | 37.0% |
| file_cluster_8 | 24 | 29.6% |
| file_cluster_13 | 15 | 18.5% |
| file_cluster_0 | 9 | 11.1% |
| file_cluster_4 | 1 | 1.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 2.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 39*

**Composition by Extension & Reason:**
- `.out`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 65.0 | 12.1 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.6 | 43.1 | 53.8 | 80.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 6.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.2 | 0.0 | 0.0 |
| API Exposure | 0.0 | 12.9 | 4.9 | 4.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 5.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 7.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 76.4 | 2.8 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 88.4 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 10.1 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 57.7 | 98.1 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 41.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `wrapt-2.1.2/tests/core/test_lazy_object_proxy.py` (Hits: 16)
- `wrapt-2.1.2/tests/core/test_post_import_hooks.py` (Hits: 6)
- `wrapt-2.1.2/src/wrapt/importer.py` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__wrapt__.py** (`wrapt-2.1.2/src/wrapt/__wrapt__.py`) — 6 inbound connections
2. **importer.py** (`wrapt-2.1.2/src/wrapt/importer.py`) — 3 inbound connections
3. **arguments.py** (`wrapt-2.1.2/src/wrapt/arguments.py`) — 3 inbound connections
4. **decorators.py** (`wrapt-2.1.2/src/wrapt/decorators.py`) — 2 inbound connections
5. **compat.py** (`wrapt-2.1.2/tests/core/compat.py`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **importer.py** (`wrapt-2.1.2/src/wrapt/importer.py`) — 16 outbound dependencies
2. **test_post_import_hooks.py** (`wrapt-2.1.2/tests/core/test_post_import_hooks.py`) — 12 outbound dependencies
3. **test_entry_points.py** (`wrapt-2.1.2/tests/core/test_entry_points.py`) — 8 outbound dependencies
4. **test_object_proxy.py** (`wrapt-2.1.2/tests/core/test_object_proxy.py`) — 8 outbound dependencies
5. **mypy_post_import_hooks_t1.py** (`wrapt-2.1.2/tests/mypy/mypy_post_import_hooks_t1.py`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `decorator` (@ `wrapt-2.1.2/src/wrapt/decorators.py`) -> Impact: **419.4** | LOC: 239
  * *Intent:* # Decorator for creating other decorators. This decorator and the # wrappers which they use are designed to properly preserve any name # attributes, f...
- `__new__` (@ `wrapt-2.1.2/src/wrapt/proxies.py`) -> Impact: **217.4** | LOC: 55
- `__init__` (@ `wrapt-2.1.2/src/wrapt/wrappers.py`) -> Impact: **179.9** | LOC: 109
- `__new__` (@ `wrapt-2.1.2/src/wrapt/proxies.py`) -> Impact: **168.9** | LOC: 52
- `__wrapped_setattr_fixups__` (@ `wrapt-2.1.2/src/wrapt/proxies.py`) -> Impact: **150.8** | LOC: 72
- `__setattr__` (@ `wrapt-2.1.2/src/wrapt/wrappers.py`) -> Impact: **122.2** | LOC: 44
- `synchronized` (@ `wrapt-2.1.2/src/wrapt/decorators.py`) -> Impact: **108.7** | LOC: 95
  * *Intent:* # We first return our magic function wrapper here so we can # determine in what context the decorator factory was used. In # other words, it is itself...
- `WraptFunctionWrapper_init` (@ `wrapt-2.1.2/src/wrapt/_wrappers.c`) -> Impact: **100.4** | LOC: 118
- `find_spec` (@ `wrapt-2.1.2/src/wrapt/importer.py`) -> Impact: **91.5** | LOC: 41
  * *Intent:* # from the importlib.util module. It doesn't actually # import the target module and only finds the # loader. If a loader is found, we need to return ...
- `raise_uninitialized_wrapper_error` (@ `wrapt-2.1.2/src/wrapt/_wrappers.c`) -> Impact: **78.2** | LOC: 165
  * *Intent:* /* ------------------------------------------------------------------------- */

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `decorator` (@ `wrapt-2.1.2/src/wrapt/decorators.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Decorator for creating other decorators. This decorator and the # wrappers which they use are designed to properly preserve any name # attributes, f...
- `synchronized` (@ `wrapt-2.1.2/src/wrapt/decorators.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # We first return our magic function wrapper here so we can # determine in what context the decorator factory was used. In # other words, it is itself...
- `__init__` (@ `wrapt-2.1.2/src/wrapt/weakrefs.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `wrapt-2.1.2/src/wrapt/wrappers.py`) -> **O(2^N) [Recursive]**
- `find_spec` (@ `wrapt-2.1.2/src/wrapt/importer.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # from the importlib.util module. It doesn't actually # import the target module and only finds the # loader. If a loader is found, we need to return ...
- `test_update_qualname_modified_on_origina` (@ `wrapt-2.1.2/tests/core/test_update_attributes.py`) -> **O(2^N) [Recursive]**
- `__setattr__` (@ `wrapt-2.1.2/src/wrapt/wrappers.py`) -> **O(2^N) [Recursive]**
- `__get__` (@ `wrapt-2.1.2/src/wrapt/wrappers.py`) -> **O(2^N) [Recursive]**
- `__signature__` (@ `wrapt-2.1.2/src/wrapt/decorators.py`) -> **O(2^N) [Recursive]**
- `__signature__` (@ `wrapt-2.1.2/src/wrapt/decorators.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `WraptFunctionWrapper_init` (@ `wrapt-2.1.2/src/wrapt/_wrappers.c`) -> DB Complexity: **33**
- `raise_uninitialized_wrapper_error` (@ `wrapt-2.1.2/src/wrapt/_wrappers.c`) -> DB Complexity: **21**
  * *Intent:* /* ------------------------------------------------------------------------- */
- `test_lazy_import_iterable` (@ `wrapt-2.1.2/tests/core/test_lazy_object_proxy.py`) -> DB Complexity: **12**
- `test_lazy_import_attribute` (@ `wrapt-2.1.2/tests/core/test_lazy_object_proxy.py`) -> DB Complexity: **12**
- `test_lazy_import` (@ `wrapt-2.1.2/tests/core/test_lazy_object_proxy.py`) -> DB Complexity: **12**
- `test_lazy_import_dotted` (@ `wrapt-2.1.2/tests/core/test_lazy_object_proxy.py`) -> DB Complexity: **12**
- `__wrapped_setattr_fixups__` (@ `wrapt-2.1.2/src/wrapt/proxies.py`) -> DB Complexity: **11**
- `register_post_import_hook` (@ `wrapt-2.1.2/src/wrapt/importer.py`) -> DB Complexity: **9**
- `test_import_deadlock_3` (@ `wrapt-2.1.2/tests/core/test_post_import_hooks.py`) -> DB Complexity: **8**
  * *Intent:* # This tries to verify that we haven't created a deadlock situation when # code executed from a post module import hook imports another module. hooks_...
- `test_descriptor` (@ `wrapt-2.1.2/tests/core/test_auto_object_proxy.py`) -> DB Complexity: **6**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `wrapt-2.1.2/tests/core` | 36 | 4660.82 | 11.5% | 0.0% |
| `wrapt-2.1.2/src/wrapt` | 11 | 3905.7 | 35.31% | 45.82% |
| `wrapt-2.1.2/tests/mypy` | 31 | 474.48 | 4.52% | 0.0% |
| `wrapt-2.1.2` | 3 | 19.28 | 4.1% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `wrapt-2.1.2/src/wrapt/__init__.pyi` -> **100.0%** Exposure
- `wrapt-2.1.2/src/wrapt/decorators.py` -> **100.0%** Exposure
- `wrapt-2.1.2/src/wrapt/wrappers.py` -> **99.3845%** Exposure
- `wrapt-2.1.2/src/wrapt/importer.py` -> **98.6851%** Exposure
- `wrapt-2.1.2/src/wrapt/proxies.py` -> **85.5459%** Exposure
### Highest State Flux (Mutation/Volatility)
- `wrapt-2.1.2/src/wrapt/_wrappers.c` -> **100.0%** Exposure
- `wrapt-2.1.2/src/wrapt/proxies.py` -> **99.8775%** Exposure
- `wrapt-2.1.2/src/wrapt/weakrefs.py` -> **99.8367%** Exposure
- `wrapt-2.1.2/src/wrapt/arguments.py` -> **99.2754%** Exposure
- `wrapt-2.1.2/src/wrapt/importer.py` -> **84.0157%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `wrapt-2.1.2/tests/core/test_object_proxy.py` -> **142** Orphaned Functions | **42** Duplicates
- `wrapt-2.1.2/tests/core/test_inplace_operators.py` -> **50** Orphaned Functions | **17** Duplicates
- `wrapt-2.1.2/tests/core/test_instancemethod.py` -> **1** Orphaned Functions | **36** Duplicates
- `wrapt-2.1.2/tests/core/test_function_wrapper.py` -> **28** Orphaned Functions | **2** Duplicates
- `wrapt-2.1.2/src/wrapt/__init__.pyi` -> **0** Orphaned Functions | **24** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`wrapt-2.1.2/src/wrapt/importer.py`** -> AI Confidence: **99.24%**
2. **`wrapt-2.1.2/src/wrapt/proxies.py`** -> AI Confidence: **99.13%**
3. **`wrapt-2.1.2/setup.py`** -> AI Confidence: **99.09%**
4. **`wrapt-2.1.2/tests/core/test_post_import_hooks.py`** -> AI Confidence: **99.09%**
5. **`wrapt-2.1.2/tests/mypy/mypy_post_import_hooks_t1.py`** -> AI Confidence: **99.08%**
6. **`wrapt-2.1.2/tests/core/test_object_proxy.py`** -> AI Confidence: **99.07%**
7. **`wrapt-2.1.2/tests/core/test_entry_points.py`** -> AI Confidence: **99.06%**
8. **`wrapt-2.1.2/src/wrapt/arguments.py`** -> AI Confidence: **99.06%**
9. **`wrapt-2.1.2/src/wrapt/_wrappers.c`** -> AI Confidence: **99.06%**
10. **`wrapt-2.1.2/src/wrapt/weakrefs.py`** -> AI Confidence: **99.0%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `wrapt-2.1.2/src/wrapt/__init__.pyi` -> **100.0%** Exposure
- `wrapt-2.1.2/src/wrapt/decorators.py` -> **100.0%** Exposure
- `wrapt-2.1.2/src/wrapt/importer.py` -> **100.0%** Exposure
- `wrapt-2.1.2/tests/core/test_auto_object_proxy.py` -> **100.0%** Exposure
- `wrapt-2.1.2/tests/core/test_callable_object_proxy.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `wrapt-2.1.2/src/wrapt/__init__.pyi` -> **100.0%** Exposure
- `wrapt-2.1.2/src/wrapt/decorators.py` -> **100.0%** Exposure
- `wrapt-2.1.2/src/wrapt/importer.py` -> **100.0%** Exposure
- `wrapt-2.1.2/tests/core/test_adapter.py` -> **100.0%** Exposure
- `wrapt-2.1.2/tests/core/test_adapter_py3.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `245` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `wrapt-2.1.2/src/wrapt/proxies.py` (PYTHON) -> Cumulative Risk: **805.04**
- **Archetype:** `file_cluster_13` (Distance: 12.973 IQR)
- **Magnitude:** 689.44 | **LOC:** 352 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.8775%)
- **Heaviest Functions:** `__new__` (Impact: 217.4), `__new__` (Impact: 168.9), `__wrapped_setattr_fixups__` (Impact: 150.8)

### 2. `wrapt-2.1.2/src/wrapt/decorators.py` (PYTHON) -> Cumulative Risk: **781.53**
- **Archetype:** `file_cluster_0` (Distance: 18.74 IQR)
- **Magnitude:** 695.4 | **LOC:** 523 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `decorator` (Impact: 419.4), `synchronized` (Impact: 108.7), `__signature__` (Impact: 21.0)

### 3. `wrapt-2.1.2/src/wrapt/importer.py` (PYTHON) -> Cumulative Risk: **774.67**
- **Archetype:** `file_cluster_13` (Distance: 13.164 IQR)
- **Magnitude:** 295.94 | **LOC:** 333 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (98.6851%)
- **Heaviest Functions:** `find_spec` (Impact: 91.5), `find_module` (Impact: 42.0), `__init__` (Impact: 28.2)

### 4. `wrapt-2.1.2/src/wrapt/__init__.pyi` (PYTHON) -> Cumulative Risk: **753.86**
- **Archetype:** `file_cluster_16` (Distance: 8.589 IQR)
- **Magnitude:** 132.92 | **LOC:** 389 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__call__` (Impact: 7.0), `wrap_object_attribute` (Impact: 4.0), `__init__` (Impact: 2.2)

### 5. `wrapt-2.1.2/src/wrapt/wrappers.py` (PYTHON) -> Cumulative Risk: **729.27**
- **Archetype:** `file_cluster_0` (Distance: 11.568 IQR)
- **Magnitude:** 1337.68 | **LOC:** 985 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9995%)
- **Heaviest Functions:** `__init__` (Impact: 179.9), `__setattr__` (Impact: 122.2), `__get__` (Impact: 73.8)

### 6. `wrapt-2.1.2/src/wrapt/patches.py` (PYTHON) -> Cumulative Risk: **659.52**
- **Archetype:** `file_cluster_13` (Distance: 12.874 IQR)
- **Magnitude:** 140.66 | **LOC:** 240 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9157%)
- **Heaviest Functions:** `resolve_path` (Impact: 43.7), `transient_function_wrapper` (Impact: 32.6), `function_wrapper` (Impact: 14.6)

### 7. `wrapt-2.1.2/src/wrapt/weakrefs.py` (PYTHON) -> Cumulative Risk: **594.43**
- **Archetype:** `file_cluster_13` (Distance: 11.184 IQR)
- **Magnitude:** 119.12 | **LOC:** 122 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9747%), State Flux (99.8367%)
- **Heaviest Functions:** `__init__` (Impact: 74.4), `__call__` (Impact: 22.2), `_weak_function_proxy_callback` (Impact: 9.6)

### 8. `wrapt-2.1.2/src/wrapt/_wrappers.c` (C) -> Cumulative Risk: **583.1**
- **Archetype:** `file_cluster_8` (Distance: 13.658 IQR)
- **Magnitude:** 454.82 | **LOC:** 4098 | **CtrlFlow:** 65.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Verification (80.0%)
- **Heaviest Functions:** `WraptFunctionWrapper_init` (Impact: 100.4), `raise_uninitialized_wrapper_error` (Impact: 78.2), `moduleinit` (Impact: 36.7)

### 9. `wrapt-2.1.2/tests/core/test_post_import_hooks.py` (PYTHON) -> Cumulative Risk: **539.68**
- **Archetype:** `file_cluster_13` (Distance: 9.783 IQR)
- **Magnitude:** 90.44 | **LOC:** 183 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `test_import_deadlock_1` (Impact: 6.3), `test_import_deadlock_2` (Impact: 6.3), `test_import_deadlock_3` (Impact: 5.8)

### 10. `wrapt-2.1.2/tests/core/test_auto_object_proxy.py` (PYTHON) -> Cumulative Risk: **503.38**
- **Archetype:** `file_cluster_4` (Distance: 12.578 IQR)
- **Magnitude:** 127.44 | **LOC:** 185 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `test_aiter` (Impact: 17.1), `test_descriptor` (Impact: 12.8), `test_next` (Impact: 5.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `wrapt-2.1.2/tests/core/test_object_proxy.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.516 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.976 IQR)
- **Top Global Matches:** file_cluster_8: 11.516, file_cluster_0: 11.759, file_cluster_17: 12.034
- **Magnitude:** 1660.66 | **LOC:** 2694 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (13.3515%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_self_keyword_argument_on_class_init` (Impact: 31.9 | O(N^4))
  * `test_self_keyword_argument_on_class_init` (Impact: 31.8 | O(N^4) | DB: 2)
  * `test_self_keyword_argument_on_class_init` (Impact: 31.8 | O(N^4) | DB: 2)
  * `test_self_keyword_argument_on_class_init` (Impact: 31.8 | O(N^4) | DB: 2)
  * `test_self_keyword_argument_on_class_init` (Impact: 31.8 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 587`, `args: 295`, `func_start: 295`, `class_start: 98`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 63`, `dead_code: 1`, `duplicate_logic: 42`, `orphaned_logic: 142`
* *Architecture:* `io: 1`, `api: 356`, `concurrency: 7`, `import: 8`
* *Defense:* `safety: 157`, `doc: 2`, `test: 262`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, decimal, asyncio, types, unittest, wrapt, re, fractions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/src/wrapt/wrappers.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.568 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.424 IQR)
- **Top Global Matches:** file_cluster_0: 11.568, file_cluster_8: 11.694, file_cluster_12: 11.853
- **Magnitude:** 1337.68 | **LOC:** 985 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (57.7566%), Tech Debt (99.3845%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 179.9 | O(2^N))
  * `__setattr__` (Impact: 122.2 | O(2^N))
  * `__get__` (Impact: 73.8 | O(2^N) | DB: 2)
  * `__call__` (Impact: 71.0 | O(N^5) | DB: 2)
  * `__delattr__` (Impact: 49.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 280`, `args: 118`, `func_start: 118`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 17`, `dead_code: 5`, `duplicate_logic: 16`
* *Architecture:* `api: 73`, `import: 3`
* *Defense:* `safety: 48`, `doc: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 38.632
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.053289
  * `Imports (Out-Degree: 0):` operator, sys, inspect
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wrapt-2.1.2/src/wrapt/decorators.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_0` (Drift: 18.74 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.187 IQR)
- **Top Global Matches:** file_cluster_0: 18.74, file_cluster_11: 19.054, file_cluster_6: 19.099
- **Magnitude:** 695.4 | **LOC:** 523 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (61.5197%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `decorator` (Impact: 419.4 | O(2^N))
    * *Intent:* # Decorator for creating other decorators. This decorator and the # wrappers which they use are desi...
  * `synchronized` (Impact: 108.7 | O(2^N) | DB: 1)
    * *Intent:* # We first return our magic function wrapper here so we can # determine in what context the decorato...
  * `__signature__` (Impact: 21.0 | O(2^N))
  * `__signature__` (Impact: 21.0 | O(2^N))
  * `__code__` (Impact: 7.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 91`, `args: 33`, `func_start: 33`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`, `dead_code: 22`, `planned_debt: 1`, `duplicate_logic: 15`
* *Architecture:* `api: 10`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 4`, `doc: 6`, `sync_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.378
  * `Choke Point (Betweenness):` 0.000316 | `Ripple Effect (Closeness):` 0.025
  * `Imports (Out-Degree: 2):` sys, threading, functools, .__wrapt__, .arguments, inspect
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `wrapt-2.1.2/src/wrapt/proxies.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.973 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.764 IQR)
- **Top Global Matches:** file_cluster_13: 12.973, file_cluster_12: 13.046, file_cluster_8: 13.215
- **Magnitude:** 689.44 | **LOC:** 352 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (49.9478%), Tech Debt (85.5459%)
**Top Internal Functions/Classes:**
  * `__new__` (Impact: 217.4 | O(2^N))
  * `__new__` (Impact: 168.9 | O(2^N))
  * `__wrapped_setattr_fixups__` (Impact: 150.8 | O(N^4) | DB: 11)
  * `lazy_import` (Impact: 27.8 | O(N^3))
    * *Intent:* # We were called because `__wrapped__` was not set, but because of # we get the lock. So check again...
  * `__init__` (Impact: 18.3 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 64`, `args: 23`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 42`, `dead_code: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 8`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 22`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0125
  * `Imports (Out-Degree: 2):` types, the, .__wrapt__, .decorators, collections.abc
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wrapt-2.1.2/src/wrapt/_wrappers.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.658 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.679 IQR)
- **Top Global Matches:** file_cluster_8: 13.658, file_cluster_0: 13.67, file_cluster_13: 13.699
- **Magnitude:** 454.82 | **LOC:** 4098 | **CtrlFlow:** 65.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (64.9867%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `WraptFunctionWrapper_init` (Impact: 100.4 | O(N^6) | DB: 33)
  * `raise_uninitialized_wrapper_error` (Impact: 78.2 | O(N^6) | DB: 21)
    * *Intent:* /* ------------------------------------------------------------------------- */
  * `moduleinit` (Impact: 36.7 | O(N^5) | DB: 6)
  * `PyInit__wrappers` (Impact: 1.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 29`, `args: 2`, `func_start: 4`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 170`, `dead_code: 8`
* *Architecture:* `api: 60`, `import: 2`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 38.632
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.053289
  * `Imports (Out-Degree: 0):` structmember.h, Python.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wrapt-2.1.2/tests/core/test_inplace_operators.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.723 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.431 IQR)
- **Top Global Matches:** file_cluster_8: 7.723, file_cluster_7: 8.658, file_cluster_1: 8.885
- **Magnitude:** 314.4 | **LOC:** 825 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (3.0685%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_inplace_matmul` (Impact: 11.9 | O(N^5) | DB: 2)
  * `test_inplace_matmul_immutable` (Impact: 11.8 | O(N^5) | DB: 2)
  * `test_inplace_add_list` (Impact: 3.2 | O(N^2))
  * `test_inplace_add_integer` (Impact: 3.1 | O(N^2))
  * `test_inplace_add_string` (Impact: 3.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 159`, `args: 75`, `func_start: 75`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 8`, `duplicate_logic: 17`, `orphaned_logic: 50`
* *Architecture:* `api: 71`, `import: 2`
* *Defense:* `safety: 2`, `test: 68`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/src/wrapt/importer.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.164 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.598 IQR)
- **Top Global Matches:** file_cluster_13: 13.164, file_cluster_11: 13.429, file_cluster_0: 13.502
- **Magnitude:** 295.94 | **LOC:** 333 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (31.654%), Tech Debt (98.6851%)
**Top Internal Functions/Classes:**
  * `find_spec` (Impact: 91.5 | O(2^N))
    * *Intent:* # from the importlib.util module. It doesn't actually # import the target module and only finds the ...
  * `find_module` (Impact: 42.0 | O(N^4))
    * *Intent:* # Python 3.4 introduced create_module() and exec_module() instead of
  * `__init__` (Impact: 28.2 | O(2^N))
    * *Intent:* # A custom module import finder. This intercepts attempts to import # interest. When a module of int...
  * `_self_set_loader` (Impact: 23.0 | O(N^4))
  * `register_post_import_hook` (Impact: 22.5 | O(N^3) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 51`, `args: 18`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 13`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `api: 16`, `concurrency: 2`, `import: 8`
* *Defense:* `safety: 22`, `doc: 10`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.606
  * `Choke Point (Betweenness):` 0.000949 | `Ripple Effect (Closeness):` 0.0375
  * `Imports (Out-Degree: 1):` finder., sys, system, that, typing, hooks, importlib.metadata, threading...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `wrapt-2.1.2/tests/core/test_function_wrapper.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.439 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.053 IQR)
- **Top Global Matches:** file_cluster_8: 9.439, file_cluster_0: 9.47, file_cluster_7: 10.145
- **Magnitude:** 260.56 | **LOC:** 599 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (4.2524%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_boolean_dynamic_guard_on_decorator` (Impact: 6.0 | O(N^4) | DB: 1)
  * `test_guard_on_instancemethod` (Impact: 6.0 | O(N^4) | DB: 1)
  * `test_instancemethod_attributes` (Impact: 5.4 | O(N^4))
  * `test_classmethod_attributes` (Impact: 5.4 | O(N^4))
  * `test_instancemethod_attributes_external_` (Impact: 5.3 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 192`, `args: 92`, `func_start: 92`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 3`, `duplicate_logic: 2`, `orphaned_logic: 28`
* *Architecture:* `api: 102`, `import: 2`
* *Defense:* `safety: 21`, `test: 48`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_monkey_patching.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.473 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.305 IQR)
- **Top Global Matches:** file_cluster_8: 8.473, file_cluster_0: 8.879, file_cluster_7: 9.161
- **Magnitude:** 223.92 | **LOC:** 572 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (4.8861%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_transient_function_wrapper_instance` (Impact: 5.8 | O(N^4) | DB: 1)
  * `test_function_wrapper_instance_method` (Impact: 5.7 | O(N^4) | DB: 1)
  * `test_patch_instance_method_class` (Impact: 5.7 | O(N^4) | DB: 1)
  * `test_patch_instance_method_dict` (Impact: 5.7 | O(N^4) | DB: 1)
  * `test_patch_instance_method_instance` (Impact: 5.7 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 122`, `args: 61`, `func_start: 61`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 21`, `duplicate_logic: 6`, `orphaned_logic: 17`
* *Architecture:* `io: 2`, `api: 71`, `import: 3`
* *Defense:* `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_instancemethod.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.434 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.367 IQR)
- **Top Global Matches:** file_cluster_8: 9.434, file_cluster_0: 9.54, file_cluster_7: 9.912
- **Magnitude:** 219.86 | **LOC:** 459 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.7636%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_class_object_qualname` (Impact: 10.8 | O(N^3))
    * *Intent:* # Test preservation of instance method __name__ attribute.
  * `test_instance_object_qualname` (Impact: 10.8 | O(N^3))
  * `test_class_object_qualname` (Impact: 10.8 | O(N^3))
  * `test_instance_object_qualname` (Impact: 10.8 | O(N^3))
  * `test_class_call_function_nested` (Impact: 5.8 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 117`, `args: 61`, `func_start: 61`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `duplicate_logic: 36`, `orphaned_logic: 1`
* *Architecture:* `api: 53`, `import: 4`
* *Defense:* `safety: 12`, `doc: 10`, `test: 43`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inspect, types, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_entry_points.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.187 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.076 IQR)
- **Top Global Matches:** file_cluster_13: 12.187, file_cluster_8: 12.522, file_cluster_4: 12.609
- **Magnitude:** 162.02 | **LOC:** 252 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (7.0778%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_threading_safety_with_entry_points` (Impact: 19.0 | O(N^4) | DB: 2)
  * `test_entry_point_hook_exception_handling` (Impact: 18.3 | O(N^4))
  * `test_entry_point_load_failure` (Impact: 18.0 | O(N^4))
    * *Intent:* # Should propagate the ImportError with pytest.raises(ImportError, match="Cannot load entry point"):...
  * `test_discover_post_import_hooks_python38` (Impact: 10.4 | O(N^4) | DB: 1)
  * `test_multiple_entry_points_same_group` (Impact: 8.6 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 64`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 17`, `orphaned_logic: 10`
* *Architecture:* `io: 1`, `api: 21`, `concurrency: 7`, `import: 14`
* *Defense:* `safety: 15`, `doc: 20`, `test: 49`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sys, pytest, importlib.metadata, threading, unittest.mock, wrapt.importer, this, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_synchronized_lock.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.768 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.032 IQR)
- **Top Global Matches:** file_cluster_0: 11.768, file_cluster_8: 12.076, file_cluster_12: 12.147
- **Magnitude:** 144.06 | **LOC:** 311 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (49.0308%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_synchronized_outer_classmethod` (Impact: 33.2 | O(N^3))
    * *Intent:* # Prior to Python 3.9 this isn't detected as a class method # call, as the classmethod decorator doe...
  * `test_synchronized_instancemethod` (Impact: 8.7 | O(N^3))
  * `test_synchronized_inner_classmethod` (Impact: 8.1 | O(N^3))
  * `test_synchronized_type_new_style` (Impact: 8.1 | O(N^3))
  * `test_synchronized_type_old_style` (Impact: 8.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 35`, `args: 17`, `func_start: 17`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `dead_code: 2`, `duplicate_logic: 6`, `orphaned_logic: 9`
* *Architecture:* `api: 22`, `import: 3`
* *Defense:* `safety: 44`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` compat, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/src/wrapt/patches.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.874 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.56 IQR)
- **Top Global Matches:** file_cluster_13: 12.874, file_cluster_12: 13.097, file_cluster_11: 13.149
- **Magnitude:** 140.66 | **LOC:** 240 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (46.8979%), Tech Debt (20.365%)
**Top Internal Functions/Classes:**
  * `resolve_path` (Impact: 43.7 | O(N^5) | DB: 3)
    * *Intent:* # Helper functions for applying wrappers to existing functions. """ Resolves the dotted path supplie...
  * `transient_function_wrapper` (Impact: 32.6 | O(N^5))
  * `function_wrapper` (Impact: 14.6 | O(N^3))
  * `__init__` (Impact: 3.9 | O(N^2) | DB: 4)
  * `patch_function_wrapper` (Impact: 3.4 | O(N^2))
    * *Intent:* # Functions for creating a simple decorator using a FunctionWrapper, # plus short cut functions for ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 42`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 18`, `import: 4`
* *Defense:* `safety: 5`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0125
  * `Imports (Out-Degree: 1):` sys, inspect, .__wrapt__
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wrapt-2.1.2/tests/core/test_inner_classmethod.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.396 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.655 IQR)
- **Top Global Matches:** file_cluster_8: 9.396, file_cluster_0: 9.453, file_cluster_7: 9.885
- **Magnitude:** 138.18 | **LOC:** 331 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (15.7322%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_class_object_qualname` (Impact: 10.8 | O(N^3))
    * *Intent:* # Test preservation of instance method __name__ attribute.
  * `test_instance_object_qualname` (Impact: 10.8 | O(N^3))
  * `test_class_call_function_nested_decorato` (Impact: 5.7 | O(N^4))
  * `test_instance_call_function_nested_decor` (Impact: 5.7 | O(N^4))
  * `test_class_call_function` (Impact: 5.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 84`, `args: 42`, `func_start: 42`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `duplicate_logic: 2`, `orphaned_logic: 20`
* *Architecture:* `api: 34`, `import: 4`
* *Defense:* `safety: 6`, `doc: 6`, `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types, inspect, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/src/wrapt/__init__.pyi` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_16` (Drift: 8.589 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.173 IQR)
- **Top Global Matches:** file_cluster_16: 8.589, file_cluster_0: 9.075, file_cluster_8: 9.11
- **Magnitude:** 132.92 | **LOC:** 389 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (14.1292%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__call__` (Impact: 7.0 | O(N^4))
  * `wrap_object_attribute` (Impact: 4.0 | O(N^2))
    * *Intent:* # wrap_object_attribute()
  * `__init__` (Impact: 2.2 | O(N^3))
  * `__get__` (Impact: 2.2 | O(N^3))
    * *Intent:* # Note that for following overloads, testing with mypy and ty they still do # not handle static meth...
  * `__get__` (Impact: 2.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 113`, `args: 60`, `func_start: 60`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 88`, `dead_code: 1`, `duplicate_logic: 24`
* *Architecture:* `io: 1`, `api: 54`, `import: 4`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, types, inspect, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_auto_object_proxy.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.578 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.266 IQR)
- **Top Global Matches:** file_cluster_4: 12.578, file_cluster_13: 12.922, file_cluster_8: 12.994
- **Magnitude:** 127.44 | **LOC:** 185 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (49.1549%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_aiter` (Impact: 17.1 | O(N^5) | DB: 2)
  * `test_descriptor` (Impact: 12.8 | O(N^5) | DB: 6)
  * `test_next` (Impact: 5.4 | O(N^4) | DB: 1)
  * `test_await` (Impact: 5.3 | O(N^4))
  * `test_length_hint` (Impact: 5.2 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 54`, `args: 23`, `func_start: 23`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 17`, `orphaned_logic: 7`
* *Architecture:* `api: 18`, `concurrency: 34`, `import: 5`
* *Defense:* `safety: 31`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` asyncio, operator, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_inner_staticmethod.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.633 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.682 IQR)
- **Top Global Matches:** file_cluster_8: 9.633, file_cluster_0: 9.635, file_cluster_13: 10.067
- **Magnitude:** 122.34 | **LOC:** 279 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (16.0472%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_class_object_qualname` (Impact: 10.8 | O(N^3))
    * *Intent:* # Test preservation of instance method __module__ attribute.
  * `test_instance_object_qualname` (Impact: 10.8 | O(N^3))
  * `test_class_call_function_nested_decorato` (Impact: 5.7 | O(N^4))
  * `test_instance_call_function_nested_decor` (Impact: 5.7 | O(N^4))
  * `test_class_call_function` (Impact: 5.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 72`, `args: 36`, `func_start: 36`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `duplicate_logic: 2`, `orphaned_logic: 18`
* *Architecture:* `api: 30`, `import: 4`
* *Defense:* `safety: 6`, `doc: 6`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types, inspect, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/src/wrapt/weakrefs.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.184 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.195 IQR)
- **Top Global Matches:** file_cluster_13: 11.184, file_cluster_8: 11.319, file_cluster_7: 11.618
- **Magnitude:** 119.12 | **LOC:** 122 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (29.8298%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 74.4 | O(2^N) | DB: 4)
  * `__call__` (Impact: 22.2 | O(N^3))
  * `_weak_function_proxy_callback` (Impact: 9.6 | O(N^2))
    * *Intent:* # A weak function proxy. This will work on instance methods, class # methods, static methods and reg...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 15`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 3`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0125
  * `Imports (Out-Degree: 1):` weakref, functools, .__wrapt__
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wrapt-2.1.2/tests/core/test_weak_function_proxy.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.148 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.115 IQR)
- **Top Global Matches:** file_cluster_8: 9.148, file_cluster_0: 9.595, file_cluster_13: 9.673
- **Magnitude:** 117.36 | **LOC:** 222 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (5.038%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_instancemethod_delete_instance` (Impact: 9.9 | O(N^4) | DB: 1)
  * `test_instancemethod_delete_function` (Impact: 9.9 | O(N^4) | DB: 1)
  * `test_instancemethod_delete_function_and_` (Impact: 9.9 | O(N^4) | DB: 1)
  * `test_classmethod` (Impact: 9.9 | O(N^4) | DB: 1)
  * `test_staticmethod` (Impact: 5.4 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 57`, `args: 30`, `func_start: 30`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 6`, `orphaned_logic: 11`
* *Architecture:* `api: 38`, `import: 3`
* *Defense:* `safety: 1`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` gc, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_update_attributes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.983 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.083 IQR)
- **Top Global Matches:** file_cluster_8: 7.983, file_cluster_7: 8.6, file_cluster_0: 8.77
- **Magnitude:** 110.06 | **LOC:** 238 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (1.9729%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_update_qualname_modified_on_origina` (Impact: 9.7 | O(2^N))
  * `test_update_qualname` (Impact: 7.6 | O(2^N))
  * `test_delete_qualname_modified_on_origina` (Impact: 4.5 | O(N^3))
  * `test_delete_annotations_modified_on_orig` (Impact: 4.4 | O(N^3))
  * `test_delete_qualname` (Impact: 4.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 63`, `args: 36`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `orphaned_logic: 13`
* *Architecture:* `api: 37`, `import: 2`
* *Defense:* `doc: 4`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_outer_classmethod.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.653 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.77 IQR)
- **Top Global Matches:** file_cluster_0: 10.653, file_cluster_13: 10.953, file_cluster_8: 11.073
- **Magnitude:** 109.7 | **LOC:** 207 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (15.4055%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_class_call_function` (Impact: 15.1 | O(N^4))
  * `test_instance_call_function` (Impact: 15.0 | O(N^4))
  * `test_class_object_qualname` (Impact: 10.8 | O(N^3))
    * *Intent:* # Test preservation of instance method __name__ attribute.
  * `test_instance_object_qualname` (Impact: 10.8 | O(N^3))
  * `test_class_argspec` (Impact: 2.9 | O(N^2))
    * *Intent:* # Test preservation of instance method __doc__ attribute.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 46`, `args: 22`, `func_start: 22`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `dead_code: 1`, `duplicate_logic: 2`, `orphaned_logic: 14`
* *Architecture:* `api: 22`, `import: 5`
* *Defense:* `safety: 6`, `doc: 6`, `test: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` types, unittest, inspect, wrapt, compat
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_decorators.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.226 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.493 IQR)
- **Top Global Matches:** file_cluster_8: 8.226, file_cluster_0: 8.626, file_cluster_7: 8.989
- **Magnitude:** 101.18 | **LOC:** 344 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (5.0846%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_call_semantics_for_assorted_decorat` (Impact: 7.5 | O(N^4) | DB: 1)
  * `test_decorated_function_as_instance_attr` (Impact: 6.4 | O(N^4) | DB: 2)
  * `test_call_semantics_for_assorted_wrapped` (Impact: 6.2 | O(N^4))
  * `test_instance_method_as_decorator` (Impact: 5.7 | O(N^4) | DB: 1)
  * `test_class_method_as_decorator` (Impact: 5.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 89`, `args: 41`, `func_start: 41`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 4`, `orphaned_logic: 10`
* *Architecture:* `api: 36`, `import: 3`
* *Defense:* `safety: 1`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` operator, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_outer_staticmethod.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.398 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.763 IQR)
- **Top Global Matches:** file_cluster_0: 10.398, file_cluster_8: 10.482, file_cluster_13: 10.639
- **Magnitude:** 90.94 | **LOC:** 180 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (16.567%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_class_object_qualname` (Impact: 10.8 | O(N^3))
    * *Intent:* # Test preservation of instance method __name__ attribute.
  * `test_instance_object_qualname` (Impact: 10.8 | O(N^3))
  * `test_class_call_function` (Impact: 5.8 | O(N^4))
  * `test_instance_call_function` (Impact: 5.8 | O(N^4))
  * `test_class_argspec` (Impact: 2.9 | O(N^2))
    * *Intent:* # Test preservation of instance method __doc__ attribute.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 44`, `args: 22`, `func_start: 22`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `duplicate_logic: 2`, `orphaned_logic: 14`
* *Architecture:* `api: 22`, `import: 4`
* *Defense:* `safety: 6`, `doc: 6`, `test: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types, inspect, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_post_import_hooks.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.783 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.083 IQR)
- **Top Global Matches:** file_cluster_13: 9.783, file_cluster_0: 9.945, file_cluster_4: 10.098
- **Magnitude:** 90.44 | **LOC:** 183 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (10.829%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_import_deadlock_1` (Impact: 6.3 | O(N^5) | DB: 3)
    * *Intent:* # This tries to verify that we haven't created a deadlock situation when # code executed from a post...
  * `test_import_deadlock_2` (Impact: 6.3 | O(N^5) | DB: 3)
    * *Intent:* # This tries to verify that we haven't created a deadlock situation when # code executed from a post...
  * `test_import_deadlock_3` (Impact: 5.8 | O(N^4) | DB: 8)
    * *Intent:* # This tries to verify that we haven't created a deadlock situation when # code executed from a post...
  * `setUp` (Impact: 5.6 | O(2^N) | DB: 5)
  * `test_before_and_after_import` (Impact: 4.7 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 50`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 9`, `fragile_debt: 2`, `orphaned_logic: 8`
* *Architecture:* `io: 6`, `api: 25`, `concurrency: 9`, `import: 16`
* *Defense:* `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sys, importlib.machinery, hook., hooks, unittest, threading, hook, wrapt.importer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_adapter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_0` (Drift: 9.795 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.376 IQR)
- **Top Global Matches:** file_cluster_0: 9.795, file_cluster_8: 9.851, file_cluster_12: 9.991
- **Magnitude:** 84.36 | **LOC:** 232 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (23.243%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_object_qualname` (Impact: 10.8 | O(N^3))
    * *Intent:* # Test preservation of function __name__ attribute. self.assertEqual(function1d.__name__, function1o...
  * `test_dynamic_adapter_classmethod` (Impact: 6.2 | O(N^4))
  * `test_dynamic_adapter_instancemethod` (Impact: 6.1 | O(N^4))
  * `test_dynamic_adapter_function` (Impact: 4.8 | O(N^3))
    * *Intent:* # Test preservation of isinstance() checks.
  * `test_argspec` (Impact: 4.4 | O(N^3))
    * *Intent:* # Test preservation of function __doc__ attribute. It is # still the documentation from the wrapped ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 68`, `args: 33`, `func_start: 33`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 1`, `duplicate_logic: 2`, `orphaned_logic: 11`
* *Architecture:* `api: 25`, `import: 4`
* *Defense:* `safety: 3`, `doc: 8`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` types, inspect, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `wrapt-2.1.2/tests/core/test_adapter.py` (PYTHON) | Magnitude: 84.36 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 117, structural_boundaries: 68, encapsulation: 44, args: 33
- `wrapt-2.1.2/tests/core/test_outer_staticmethod.py` (PYTHON) | Magnitude: 90.94 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 84, encapsulation: 52, structural_boundaries: 44, args: 22
- `wrapt-2.1.2/src/wrapt/wrappers.py` (PYTHON) | Magnitude: 1337.68 | Delta: **0.126 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 521, encapsulation: 468, structural_boundaries: 280, args: 118
- `wrapt-2.1.2/tests/core/test_class_py37.py` (PYTHON) | Magnitude: 36.66 | Delta: **0.171 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 40, encapsulation: 24, api: 16
- `wrapt-2.1.2/tests/core/test_outer_classmethod.py` (PYTHON) | Magnitude: 109.7 | Delta: **0.3 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 96, encapsulation: 66, structural_boundaries: 46, args: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `wrapt-2.1.2/tests/core/test_descriptors_py36.py` (PYTHON) | Magnitude: 12.2 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 14, encapsulation: 12, args: 6
- `wrapt-2.1.2/tests/mypy/mypy_function_wrapper_fn_t3.py` (PYTHON) | Magnitude: 6.16 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 8, doc: 4, safety_bypasses: 3, args: 2
- `wrapt-2.1.2/tests/mypy/mypy_function_wrapper_fn_t5.py` (PYTHON) | Magnitude: 11.56 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, doc: 2, import: 1
- `wrapt-2.1.2/tests/core/compat.py` (PYTHON) | Magnitude: 11.04 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, io: 1, import: 1, explicit_casts: 1
- `wrapt-2.1.2/src/wrapt/proxies.py` (PYTHON) | Magnitude: 689.44 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: encapsulation: 236, indent_spaces: 168, branch: 87, structural_boundaries: 64

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `wrapt-2.1.2/tests/mypy/mypy_function_wrapper_cls_t4.py` (PYTHON) | Magnitude: 6.14 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, doc: 4, safety_bypasses: 3, args: 2
- `wrapt-2.1.2/tests/mypy/mypy_synchronized_lock_t1.py` (PYTHON) | Magnitude: 56.58 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 33, api: 15, decorators: 14
- `wrapt-2.1.2/tests/core/test_adapter_py3.py` (PYTHON) | Magnitude: 72.2 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 118, structural_boundaries: 77, encapsulation: 43, args: 35
- `wrapt-2.1.2/tests/mypy/mypy_post_import_hooks_t1.py` (PYTHON) | Magnitude: 14.82 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 8, doc: 6, args: 4
- `wrapt-2.1.2/tests/mypy/mypy_function_wrapper_cls_t6.py` (PYTHON) | Magnitude: 3.0 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, doc: 4, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `wrapt-2.1.2/tests/core/test_auto_object_proxy.py` (PYTHON) | Magnitude: 127.44 | Delta: **0.344 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 119, structural_boundaries: 54, encapsulation: 44, concurrency: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `wrapt-2.1.2/tests/core/test_inner_staticmethod.py` (PYTHON) | Magnitude: 122.34 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 154, encapsulation: 108, structural_boundaries: 72, args: 36
- `wrapt-2.1.2/src/wrapt/_wrappers.c` (C) | Magnitude: 454.82 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 359, state_mutation: 170, pointers: 67, api: 60
- `wrapt-2.1.2/tests/mypy/mypy_patching_primitives_t1.py` (PYTHON) | Magnitude: 11.08 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 12, safety_bypasses: 9, indent_spaces: 6, doc: 4
- `wrapt-2.1.2/tests/core/test_function_wrapper.py` (PYTHON) | Magnitude: 260.56 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 367, structural_boundaries: 192, encapsulation: 141, api: 102
- `wrapt-2.1.2/tests/core/test_nested_function.py` (PYTHON) | Magnitude: 51.6 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 31, encapsulation: 27, args: 15

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `wrapt-2.1.2/src/wrapt/importer.py` -> **Severity: 0.08** (Bridge: 0.0009 * Flux: 84.0157%)
- `wrapt-2.1.2/src/wrapt/decorators.py` -> **Severity: 0.014** (Bridge: 0.0003 * Flux: 44.4515%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `wrapt-2.1.2/src/wrapt/__wrapt__.py` -> **Severity: 4.139** (Embedded: 0.08 * Error Risk: 51.7391%)
- `wrapt-2.1.2/src/wrapt/arguments.py` -> **Severity: 3.571** (Embedded: 0.0446 * Error Risk: 80.0%)
- `wrapt-2.1.2/src/wrapt/_wrappers.c` -> **Severity: 2.149** (Embedded: 0.0533 * Error Risk: 40.3254%)
- `wrapt-2.1.2/src/wrapt/wrappers.py` -> **Severity: 0.174** (Embedded: 0.0533 * Error Risk: 3.262%)
- `wrapt-2.1.2/src/wrapt/decorators.py` -> **Severity: 0.164** (Embedded: 0.025 * Error Risk: 6.562%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `wrapt-2.1.2/src/wrapt/__wrapt__.py` -> **Severity: 4213.436** (Blast Radius: 67.195 * Doc Risk: 62.7046%)
- `wrapt-2.1.2/src/wrapt/wrappers.py` -> **Severity: 3863.181** (Blast Radius: 38.632 * Doc Risk: 99.9995%)
- `wrapt-2.1.2/src/wrapt/importer.py` -> **Severity: 2763.125** (Blast Radius: 28.606 * Doc Risk: 96.5925%)
- `wrapt-2.1.2/src/wrapt/weakrefs.py` -> **Severity: 1149.009** (Blast Radius: 11.493 * Doc Risk: 99.9747%)
- `wrapt-2.1.2/src/wrapt/patches.py` -> **Severity: 1148.331** (Blast Radius: 11.493 * Doc Risk: 99.9157%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
