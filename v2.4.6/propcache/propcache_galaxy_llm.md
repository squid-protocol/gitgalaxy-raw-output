# ARCHITECTURAL_BRIEF: propcache
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/propcache` |
| **Timestamp** | `2026-08-03T21:23:22.000122+00:00` |
| **Scan Duration** | `0.18s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 18 malicious artifacts.

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
| Total Artifacts | 43 |
| Analyzed Artifacts (Scanned) | 28 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 15 |
| Total LOC | 970 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 65.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5237 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1623 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 18 | 970 | 64.3% |
| PLAINTEXT | 9 | 0 | 32.1% |
| MARKDOWN | 1 | 0 | 3.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.57`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 9 | 32.1% |
| file_cluster_16 | 5 | 17.9% |
| file_cluster_8 | 4 | 14.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 10 | 35.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 15*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 3x Excluded (Unsupported Extension: '.rst'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.ini`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 1.7 | 42.6 | 8.7 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 9.5 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 11.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 10.0 | 2.2 | 0.0 |
| API Exposure | 0.0 | 6.3 | 2.3 | 1.2 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 99.5 | 15.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 83.3 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 33.1 | 25.8 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 49.6 | 39.6 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 20.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `propcache-0.4.1/tests/test_under_cached_property.py` (Hits: 11)
- `propcache-0.4.1/tests/test_cached_property.py` (Hits: 8)
- `propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py` (Hits: 7)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **api.py** (`propcache-0.4.1/src/propcache/api.py`) — 3 inbound connections
2. **_compat.py** (`propcache-0.4.1/packaging/pep517_backend/_compat.py`) — 2 inbound connections
3. **_cython_configuration.py** (`propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py`) — 2 inbound connections
4. **_transformers.py** (`propcache-0.4.1/packaging/pep517_backend/_transformers.py`) — 2 inbound connections
5. **_backend.py** (`propcache-0.4.1/packaging/pep517_backend/_backend.py`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **_backend.py** (`propcache-0.4.1/packaging/pep517_backend/_backend.py`) — 19 outbound dependencies
2. **_cython_configuration.py** (`propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py`) — 10 outbound dependencies
3. **cli.py** (`propcache-0.4.1/packaging/pep517_backend/cli.py`) — 8 outbound dependencies
4. **_compat.py** (`propcache-0.4.1/packaging/pep517_backend/_compat.py`) — 7 outbound dependencies
5. **test_cached_property.py** (`propcache-0.4.1/tests/test_cached_property.py`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `run_main_program` (@ `propcache-0.4.1/packaging/pep517_backend/cli.py`) -> Impact: **21.5** | LOC: 30
  * *Intent:* """Invoke ``translate-cython`` or fail."""
- `patched_env` (@ `propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py`) -> Impact: **20.9** | LOC: 17
  * *Intent:* # This section can contain args that have values: # * exclude=PATTERN exclude certain file patterns from the compilation # * parallel=N run builds in ...
- `__get__` (@ `propcache-0.4.1/src/propcache/_helpers_c.pyx`) -> Impact: **20.7** | LOC: 14
- `__set_name__` (@ `propcache-0.4.1/src/propcache/_helpers_c.pyx`) -> Impact: **20.4** | LOC: 8
- `test_under_cached_property_no_refcount_l` (@ `propcache-0.4.1/tests/test_under_cached_property.py`) -> Impact: **16.1** | LOC: 83
- `test_cached_property_no_refcount_leak` (@ `propcache-0.4.1/tests/test_cached_property.py`) -> Impact: **16.0** | LOC: 80
- `_in_temporary_directory` (@ `propcache-0.4.1/packaging/pep517_backend/_backend.py`) -> Impact: **15.8** | LOC: 16
- `test_set_name` (@ `propcache-0.4.1/tests/test_cached_property.py`) -> Impact: **15.8** | LOC: 16
- `test_get_without_set_name` (@ `propcache-0.4.1/tests/test_cached_property.py`) -> Impact: **15.7** | LOC: 13
- `_emit_opt_pairs` (@ `propcache-0.4.1/packaging/pep517_backend/_transformers.py`) -> Impact: **13.9** | LOC: 9

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `__doc__` (@ `propcache-0.4.1/src/propcache/_helpers_c.pyx`) -> **O(2^N) [Recursive]**
- `__doc__` (@ `propcache-0.4.1/src/propcache/_helpers_c.pyx`) -> **O(2^N) [Recursive]**
- `_in_temporary_directory` (@ `propcache-0.4.1/packaging/pep517_backend/_backend.py`) -> **O(N^4)**
- `run_main_program` (@ `propcache-0.4.1/packaging/pep517_backend/cli.py`) -> **O(N^4)**
  * *Intent:* """Invoke ``translate-cython`` or fail."""
- `__get__` (@ `propcache-0.4.1/src/propcache/_helpers_c.pyx`) -> **O(N^4)**
- `__set_name__` (@ `propcache-0.4.1/src/propcache/_helpers_c.pyx`) -> **O(N^4)**
- `chdir_cm` (@ `propcache-0.4.1/packaging/pep517_backend/_compat.py`) -> **O(N^3)**
- `patched_env` (@ `propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py`) -> **O(N^3)**
  * *Intent:* # This section can contain args that have values: # * exclude=PATTERN exclude certain file patterns from the compilation # * parallel=N run builds in ...
- `sanitize_rst_roles` (@ `propcache-0.4.1/packaging/pep517_backend/_transformers.py`) -> **O(N^3)**
  * *Intent:* """ pep_substitution_pattern = ( r"`PEP \g<pep_number> <https://peps.python.org/pep-\g<pep_number>>`__" ) user_role_regex = r"""(?x) :user:`(?P<github...
- `__get__` (@ `propcache-0.4.1/src/propcache/_helpers_c.pyx`) -> **O(N^3)**

### Highest Data Gravity (Database Complexity)
- `patched_env` (@ `propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py`) -> DB Complexity: **21**
  * *Intent:* # This section can contain args that have values: # * exclude=PATTERN exclude certain file patterns from the compilation # * parallel=N run builds in ...
- `test_cached_property_no_refcount_leak` (@ `propcache-0.4.1/tests/test_cached_property.py`) -> DB Complexity: **18**
- `test_under_cached_property_no_refcount_l` (@ `propcache-0.4.1/tests/test_under_cached_property.py`) -> DB Complexity: **18**
- `chdir_cm` (@ `propcache-0.4.1/packaging/pep517_backend/_compat.py`) -> DB Complexity: **9**
- `test_under_cached_property_typeddict` (@ `propcache-0.4.1/tests/test_under_cached_property.py`) -> DB Complexity: **6**
  * *Intent:* """Test static typing passes with TypedDict."""
- `test_under_cached_property` (@ `propcache-0.4.1/tests/test_under_cached_property.py`) -> DB Complexity: **6**
- `_in_temporary_directory` (@ `propcache-0.4.1/packaging/pep517_backend/_backend.py`) -> DB Complexity: **3**
- `test_cached_property` (@ `propcache-0.4.1/tests/test_cached_property.py`) -> DB Complexity: **3**
- `__init__` (@ `propcache-0.4.1/src/propcache/_helpers_py.py`) -> DB Complexity: **3**
- `__init__` (@ `propcache-0.4.1/src/propcache/_helpers_c.pyx`) -> DB Complexity: **2**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `propcache-0.4.1/tests` | 5 | 315.2 | 4.41% | 0.0% |
| `propcache-0.4.1/packaging/pep517_backend` | 8 | 241.2 | 6.26% | 0.0% |
| `propcache-0.4.1/src/propcache` | 5 | 139.02 | 16.99% | 40.0% |
| `propcache-0.4.1/requirements` | 7 | 7.0 | 0.0% | 0.0% |
| `propcache-0.4.1` | 2 | 2.0 | 0.0% | 0.0% |
| `propcache-0.4.1/packaging` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `propcache-0.4.1/src/propcache/_helpers_c.pyx` -> **100.0%** Exposure
- `propcache-0.4.1/src/propcache/_helpers_py.py` -> **99.9996%** Exposure
### Highest State Flux (Mutation/Volatility)
- `propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py` -> **99.5411%** Exposure
- `propcache-0.4.1/src/propcache/_helpers_c.pyx` -> **88.3674%** Exposure
- `propcache-0.4.1/src/propcache/_helpers_py.py` -> **72.3771%** Exposure
- `propcache-0.4.1/packaging/pep517_backend/_backend.py` -> **13.8373%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `propcache-0.4.1/tests/test_cached_property.py` -> **9** Orphaned Functions | **0** Duplicates
- `propcache-0.4.1/tests/test_under_cached_property.py` -> **9** Orphaned Functions | **0** Duplicates
- `propcache-0.4.1/src/propcache/_helpers_c.pyx` -> **0** Orphaned Functions | **6** Duplicates
- `propcache-0.4.1/tests/test_init.py` -> **5** Orphaned Functions | **0** Duplicates
- `propcache-0.4.1/tests/test_benchmarks.py` -> **4** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`propcache-0.4.1/packaging/pep517_backend/_backend.py`** -> AI Confidence: **99.18%**
2. **`propcache-0.4.1/packaging/pep517_backend/_compat.py`** -> AI Confidence: **99.07%**
3. **`propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py`** -> AI Confidence: **99.07%**
4. **`propcache-0.4.1/packaging/pep517_backend/cli.py`** -> AI Confidence: **99.07%**
5. **`propcache-0.4.1/tests/test_cached_property.py`** -> AI Confidence: **99.07%**
6. **`propcache-0.4.1/tests/test_init.py`** -> AI Confidence: **98.92%**
7. **`propcache-0.4.1/packaging/pep517_backend/__main__.py`** -> AI Confidence: **98.89%**
8. **`propcache-0.4.1/src/propcache/_helpers_c.pyx`** -> AI Confidence: **98.89%**
9. **`propcache-0.4.1/packaging/pep517_backend/_transformers.py`** -> AI Confidence: **98.88%**
10. **`propcache-0.4.1/packaging/pep517_backend/hooks.py`** -> AI Confidence: **98.87%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `propcache-0.4.1/tests/test_cached_property.py` -> **100.0%** Exposure
- `propcache-0.4.1/tests/test_under_cached_property.py` -> **100.0%** Exposure
- `propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py` -> **82.6532%** Exposure
- `propcache-0.4.1/packaging/pep517_backend/_backend.py` -> **82.201%** Exposure
- `propcache-0.4.1/tests/test_benchmarks.py` -> **0.8701%** Exposure
### Algorithmic DoS Exposure
- `propcache-0.4.1/packaging/pep517_backend/_compat.py` -> **100.0%** Exposure
- `propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py` -> **100.0%** Exposure
- `propcache-0.4.1/tests/test_benchmarks.py` -> **100.0%** Exposure
- `propcache-0.4.1/tests/test_cached_property.py` -> **100.0%** Exposure
- `propcache-0.4.1/tests/test_under_cached_property.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `74` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `propcache-0.4.1/src/propcache/_helpers_c.pyx` (PYTHON) -> Cumulative Risk: **643.71**
- **Archetype:** `file_cluster_8` (Distance: 9.802 IQR)
- **Magnitude:** 82.0 | **LOC:** 104 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (99.991%), Documentation (99.9484%)
- **Heaviest Functions:** `__get__` (Impact: 20.7), `__set_name__` (Impact: 20.4), `__get__` (Impact: 12.5)

### 2. `propcache-0.4.1/src/propcache/_helpers_py.py` (PYTHON) -> Cumulative Risk: **595.51**
- **Archetype:** `file_cluster_16` (Distance: 10.521 IQR)
- **Magnitude:** 17.24 | **LOC:** 63 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9996%), Algorithmic Dos (97.129%), Documentation (84.9205%)
- **Heaviest Functions:** `__init__` (Impact: 3.2), `__set__` (Impact: 3.1), `__get__` (Impact: 1.6)

### 3. `propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py` (PYTHON) -> Cumulative Risk: **515.17**
- **Archetype:** `file_cluster_13` (Distance: 11.636 IQR)
- **Magnitude:** 49.34 | **LOC:** 128 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.5411%), Logic Bomb (82.6532%)
- **Heaviest Functions:** `patched_env` (Impact: 20.9), `_configure_cython_line_tracing` (Impact: 7.2), `make_cythonize_cli_args_from_config` (Impact: 2.3)

### 4. `propcache-0.4.1/packaging/pep517_backend/_backend.py` (PYTHON) -> Cumulative Risk: **453.96**
- **Archetype:** `file_cluster_13` (Distance: 9.367 IQR)
- **Magnitude:** 76.62 | **LOC:** 392 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.7226%), Logic Bomb (82.201%), Verification (80.0%)
- **Heaviest Functions:** `_in_temporary_directory` (Impact: 15.8), `patched_dist_get_long_description` (Impact: 8.6), `patched_distutils_cmd_install` (Impact: 8.5)

### 5. `propcache-0.4.1/packaging/pep517_backend/_compat.py` (PYTHON) -> Cumulative Risk: **364.28**
- **Archetype:** `file_cluster_13` (Distance: 9.572 IQR)
- **Magnitude:** 14.78 | **LOC:** 29 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9988%), Stability (50.0%)
- **Heaviest Functions:** `chdir_cm` (Impact: 12.4)

### 6. `propcache-0.4.1/tests/test_cached_property.py` (PYTHON) -> Cumulative Risk: **359.06**
- **Archetype:** `file_cluster_16` (Distance: 12.521 IQR)
- **Magnitude:** 116.2 | **LOC:** 227 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Stability (50.0%)
- **Heaviest Functions:** `test_cached_property_no_refcount_leak` (Impact: 16.0), `test_set_name` (Impact: 15.8), `test_get_without_set_name` (Impact: 15.7)

### 7. `propcache-0.4.1/tests/test_under_cached_property.py` (PYTHON) -> Cumulative Risk: **358.73**
- **Archetype:** `file_cluster_16` (Distance: 12.012 IQR)
- **Magnitude:** 109.1 | **LOC:** 253 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Stability (50.0%)
- **Heaviest Functions:** `test_under_cached_property_no_refcount_l` (Impact: 16.1), `test_under_cached_property_typeddict` (Impact: 13.3), `test_under_cached_property` (Impact: 13.0)

### 8. `propcache-0.4.1/tests/test_benchmarks.py` (PYTHON) -> Cumulative Risk: **270.04**
- **Archetype:** `file_cluster_16` (Distance: 12.231 IQR)
- **Magnitude:** 56.22 | **LOC:** 93 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Stability (50.0%), Cognitive Load (7.8272%)
- **Heaviest Functions:** `test_under_cached_property_cache_miss` (Impact: 9.1), `test_under_cached_property_cache_hit` (Impact: 9.0), `test_cached_property_cache_hit` (Impact: 9.0)

### 9. `propcache-0.4.1/packaging/pep517_backend/cli.py` (PYTHON) -> Cumulative Risk: **258.59**
- **Archetype:** `file_cluster_13` (Distance: 7.185 IQR)
- **Magnitude:** 23.28 | **LOC:** 55 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (64.0921%), Stability (50.0%), Documentation (37.0876%)
- **Heaviest Functions:** `run_main_program` (Impact: 21.5)

### 10. `propcache-0.4.1/packaging/pep517_backend/hooks.py` (PYTHON) -> Cumulative Risk: **242.07**
- **Archetype:** `file_cluster_8` (Distance: 6.841 IQR)
- **Magnitude:** 15.28 | **LOC:** 22 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (93.3333%), Safety Score (65.7143%), Stability (50.0%), Documentation (25.8753%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `propcache-0.4.1/tests/test_cached_property.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.521 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 6.334 IQR)
- **Top Global Matches:** file_cluster_16: 12.521, file_cluster_0: 12.657, file_cluster_13: 12.663
- **Magnitude:** 116.2 | **LOC:** 227 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (2.3537%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_cached_property_no_refcount_leak` (Impact: 16.0 | O(N^3) | DB: 18)
  * `test_set_name` (Impact: 15.8 | O(N^2))
  * `test_get_without_set_name` (Impact: 15.7 | O(N^2))
  * `test_cached_property_class_docstring` (Impact: 9.8 | O(N^2))
    * *Intent:* """Docstring."""
  * `test_cached_property_without_cache` (Impact: 8.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 77`, `args: 26`, `func_start: 26`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `orphaned_logic: 9`
* *Architecture:* `io: 8`, `api: 21`, `import: 8`
* *Defense:* `safety: 22`, `doc: 40`, `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` typing, collections.abc, sys, gc, operator, propcache.api, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/tests/test_under_cached_property.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.012 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 6.474 IQR)
- **Top Global Matches:** file_cluster_16: 12.012, file_cluster_0: 12.174, file_cluster_13: 12.296
- **Magnitude:** 109.1 | **LOC:** 253 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (1.686%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_under_cached_property_no_refcount_l` (Impact: 16.1 | O(N^3) | DB: 18)
  * `test_under_cached_property_typeddict` (Impact: 13.3 | O(N^3) | DB: 6)
    * *Intent:* """Test static typing passes with TypedDict."""
  * `test_under_cached_property` (Impact: 13.0 | O(N^3) | DB: 6)
  * `test_under_cached_property_class_docstri` (Impact: 9.9 | O(N^2))
  * `test_under_cached_property_without_cache` (Impact: 8.8 | O(N^3))
    * *Intent:* """Init."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 85`, `args: 31`, `func_start: 31`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 11`, `orphaned_logic: 9`
* *Architecture:* `io: 11`, `api: 24`, `import: 7`
* *Defense:* `safety: 24`, `doc: 34`, `test: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` typing, collections.abc, sys, gc, propcache.api, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/src/propcache/_helpers_c.pyx` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.802 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.552 IQR)
- **Top Global Matches:** file_cluster_8: 9.802, file_cluster_13: 10.168, file_cluster_0: 10.202
- **Magnitude:** 82.0 | **LOC:** 104 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (17.7172%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__get__` (Impact: 20.7 | O(N^4))
  * `__set_name__` (Impact: 20.4 | O(N^4) | DB: 1)
  * `__get__` (Impact: 12.5 | O(N^3))
  * `__doc__` (Impact: 5.3 | O(2^N))
  * `__doc__` (Impact: 5.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 21`, `args: 8`, `func_start: 8`
* *Risk/State:* `state_mutation: 7`, `duplicate_logic: 6`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 2`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 64.045
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.07716
  * `Imports (Out-Degree: 0):` types
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `propcache-0.4.1/packaging/pep517_backend/_backend.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.367 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.111 IQR)
- **Top Global Matches:** file_cluster_13: 9.367, file_cluster_16: 9.685, file_cluster_8: 9.759
- **Magnitude:** 76.62 | **LOC:** 392 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (4.4605%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_in_temporary_directory` (Impact: 15.8 | O(N^4) | DB: 3)
  * `patched_dist_get_long_description` (Impact: 8.6 | O(N^2))
    * *Intent:* """ # Without this, build_lib puts stuff under `*.data/platlib/` folder _orig_func = _DistutilsDistr...
  * `patched_distutils_cmd_install` (Impact: 8.5 | O(N^2) | DB: 1)
  * `patched_dist_has_ext_modules` (Impact: 8.3 | O(N^2))
  * `_make_pure_python` (Impact: 4.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 96`, `args: 16`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`
* *Architecture:* `io: 3`, `api: 9`, `import: 26`
* *Defense:* `safety: 9`, `doc: 39`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 43.764
  * `Choke Point (Betweenness):` 0.004274 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 3):` distutils.dist, pathlib, collections.abc, ._compat, ._cython_configuration, warnings, distutils.core, ._transformers...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `propcache-0.4.1/tests/test_benchmarks.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.231 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.883 IQR)
- **Top Global Matches:** file_cluster_16: 12.231, file_cluster_0: 12.389, file_cluster_13: 12.45
- **Magnitude:** 56.22 | **LOC:** 93 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (7.8272%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_under_cached_property_cache_miss` (Impact: 9.1 | O(N^3) | DB: 1)
  * `test_under_cached_property_cache_hit` (Impact: 9.0 | O(N^3) | DB: 1)
  * `test_cached_property_cache_hit` (Impact: 9.0 | O(N^3))
  * `test_cached_property_cache_miss` (Impact: 9.0 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 26`, `args: 15`, `func_start: 15`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`, `orphaned_logic: 4`
* *Architecture:* `api: 12`, `import: 3`
* *Defense:* `safety: 2`, `doc: 18`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pytest_codspeed, propcache, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.636 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 7.18 IQR)
- **Top Global Matches:** file_cluster_13: 11.636, file_cluster_16: 12.019, file_cluster_0: 12.296
- **Magnitude:** 49.34 | **LOC:** 128 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (14.7384%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `patched_env` (Impact: 20.9 | O(N^3) | DB: 21)
    * *Intent:* # This section can contain args that have values: # * exclude=PATTERN exclude certain file patterns ...
  * `_configure_cython_line_tracing` (Impact: 7.2 | O(N^2))
    * *Intent:* # Env vars provisioned during cythonize call src = ["src/**/*.pyx"] [tool.local.cythonize.env] # Env...
  * `make_cythonize_cli_args_from_config` (Impact: 2.3 | O(N^1))
    * *Intent:* # This section can contain the following booleans: # * annotate — generate annotated HTML page for s...
  * `get_local_cython_config` (Impact: 2.0 | O(N^1))
    * *Intent:* """Grab optional build dependencies from pyproject.toml config. :returns: config section from ``pypr...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 28`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `io: 7`, `api: 7`, `import: 10`
* *Defense:* `safety: 4`, `doc: 9`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 56.163
  * `Choke Point (Betweenness):` 0.002849 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 2):` expandvars, pathlib, contextlib, __future__, typing, os, collections.abc, sys...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `propcache-0.4.1/packaging/pep517_backend/_transformers.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.056 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.794 IQR)
- **Top Global Matches:** file_cluster_16: 9.056, file_cluster_7: 9.316, file_cluster_8: 9.329
- **Magnitude:** 39.3 | **LOC:** 112 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.6454%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_emit_opt_pairs` (Impact: 13.9 | O(N^2))
  * `sanitize_rst_roles` (Impact: 11.5 | O(N^3))
    * *Intent:* """ pep_substitution_pattern = ( r"`PEP \g<pep_number> <https://peps.python.org/pep-\g<pep_number>>`...
  * `get_enabled_cli_flags_from_config` (Impact: 5.4 | O(N^1))
  * `get_cli_kwargs_from_config` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 17`, `args: 4`, `func_start: 4`
* *Risk/State:* None
* *Architecture:* `api: 6`, `import: 4`
* *Defense:* `safety: 1`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 59.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.098765
  * `Imports (Out-Degree: 0):` collections.abc, itertools, typing, re
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `propcache-0.4.1/tests/test_init.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.316 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.291 IQR)
- **Top Global Matches:** file_cluster_13: 13.316, file_cluster_16: 13.376, file_cluster_0: 13.726
- **Magnitude:** 30.46 | **LOC:** 44 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.1699%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_importing_invalid_attr_raises` (Impact: 13.3 | O(N^2))
  * `test_import_error_invalid_attr` (Impact: 5.5 | O(N^2))
    * *Intent:* # No match here because the error is raised by the import system # and may vary between Python versi...
  * `test_public_api_is_discoverable_in_dir` (Impact: 2.2 | O(N^1))
  * `test_api_at_top_level` (Impact: 2.1 | O(N^1))
  * `test_no_wildcard_imports` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 17`, `args: 5`, `func_start: 5`
* *Risk/State:* `orphaned_logic: 5`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `safety: 6`, `doc: 12`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` propcache, pytest, system
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/packaging/pep517_backend/cli.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 7.185 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.29 IQR)
- **Top Global Matches:** file_cluster_13: 7.185, file_cluster_8: 7.294, file_cluster_7: 7.94
- **Magnitude:** 23.28 | **LOC:** 55 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.7584%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_main_program` (Impact: 21.5 | O(N^4))
    * *Intent:* """Invoke ``translate-cython`` or fail."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 28`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 3`, `api: 1`, `import: 10`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pathlib, ._cython_configuration, __future__, collections.abc, sys, Cython.Compiler.CmdLine, Cython.Compiler.Main, itertools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/src/propcache/_helpers_py.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.521 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.442 IQR)
- **Top Global Matches:** file_cluster_16: 10.521, file_cluster_13: 10.539, file_cluster_0: 10.931
- **Magnitude:** 17.24 | **LOC:** 63 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (7.7056%), Tech Debt (99.9996%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 3.2 | O(N^2) | DB: 3)
  * `__set__` (Impact: 3.1 | O(N^2))
  * `__get__` (Impact: 1.6 | O(N^2))
  * `__get__` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 22`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 4`, `import: 5`
* *Defense:* `safety: 2`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 64.045
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.07716
  * `Imports (Out-Degree: 0):` collections.abc, sys, typing, functools
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `propcache-0.4.1/src/propcache/_helpers.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 7.638 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.181 IQR)
- **Top Global Matches:** file_cluster_13: 7.638, file_cluster_8: 7.915, file_cluster_7: 8.925
- **Magnitude:** 16.56 | **LOC:** 40 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (11.9203%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 28`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 1`, `import: 11`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 95.037
  * `Choke Point (Betweenness):` 0.011396 | `Ripple Effect (Closeness):` 0.084656
  * `Imports (Out-Degree: 2):` ._helpers_py, typing, os, sys, ._helpers_c
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `propcache-0.4.1/packaging/pep517_backend/hooks.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.841 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.467 IQR)
- **Top Global Matches:** file_cluster_8: 6.841, file_cluster_13: 6.959, file_cluster_7: 7.506
- **Magnitude:** 15.28 | **LOC:** 22 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 9`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `import: 4`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ._backend, setuptools.build_meta, contextlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/packaging/pep517_backend/_compat.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.572 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.97 IQR)
- **Top Global Matches:** file_cluster_13: 9.572, file_cluster_0: 10.351, file_cluster_16: 10.615
- **Magnitude:** 14.78 | **LOC:** 29 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (7.4857%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `chdir_cm` (Impact: 12.4 | O(N^3) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 18`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 5`, `api: 2`, `import: 8`
* *Defense:* `safety: 2`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 59.925
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.098765
  * `Imports (Out-Degree: 0):` pathlib, contextlib, tomli, os, collections.abc, sys, tomllib
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `propcache-0.4.1/src/propcache/api.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.11 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.383 IQR)
- **Top Global Matches:** file_cluster_8: 8.11, file_cluster_13: 8.197, file_cluster_7: 8.369
- **Magnitude:** 13.6 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 83.979
  * `Choke Point (Betweenness):` 0.012821 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 1):` ._helpers
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `propcache-0.4.1/packaging/pep517_backend/__main__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 6.712 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.951 IQR)
- **Top Global Matches:** file_cluster_13: 6.712, file_cluster_8: 6.906, file_cluster_7: 7.983
- **Magnitude:** 12.08 | **LOC:** 7 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 3`
* *Risk/State:* None
* *Architecture:* `io: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/packaging/pep517_backend/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.367 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.685 IQR)
- **Top Global Matches:** file_cluster_8: 9.367, file_cluster_7: 9.551, file_cluster_1: 9.639
- **Magnitude:** 10.52 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/src/propcache/__init__.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.559 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.029 IQR)
- **Top Global Matches:** file_cluster_13: 10.559, file_cluster_16: 10.66, file_cluster_8: 10.956
- **Magnitude:** 9.62 | **LOC:** 33 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (42.5976%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_import_facade` (Impact: 6.4 | O(N^2))
  * `_dir_facade` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 14`, `args: 2`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 1`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 23.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` typing, , .api
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/tests/test_api.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.683 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.219 IQR)
- **Top Global Matches:** file_cluster_13: 14.683, file_cluster_16: 14.72, file_cluster_8: 14.96
- **Magnitude:** 3.22 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_api` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 1`, `func_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 4`, `doc: 4`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` propcache
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/MANIFEST.in` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 22 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/NOTICE` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/requirements/codspeed.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/requirements/cython.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/requirements/dev.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/requirements/doc-spelling.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `propcache-0.4.1/requirements/doc.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 23.656
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `propcache-0.4.1/tests/test_api.py` (PYTHON) | Magnitude: 3.22 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 7, test: 5, safety: 4, doc: 4
- `propcache-0.4.1/tests/test_init.py` (PYTHON) | Magnitude: 30.46 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 17, test: 15, indent_spaces: 13, doc: 12
- `propcache-0.4.1/src/propcache/__init__.py` (PYTHON) | Magnitude: 9.62 | Delta: **0.101 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 14, encapsulation: 12, indent_spaces: 7, doc: 6
- `propcache-0.4.1/packaging/pep517_backend/cli.py` (PYTHON) | Magnitude: 23.28 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 28, indent_spaces: 25, encapsulation: 19, import: 10
- `propcache-0.4.1/packaging/pep517_backend/__main__.py` (PYTHON) | Magnitude: 12.08 | Delta: **0.194 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, io: 2, import: 2, encapsulation: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `propcache-0.4.1/src/propcache/_helpers_py.py` (PYTHON) | Magnitude: 17.24 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: encapsulation: 27, indent_spaces: 26, structural_boundaries: 22, generics: 13
- `propcache-0.4.1/tests/test_cached_property.py` (PYTHON) | Magnitude: 116.2 | Delta: **0.136 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 103, structural_boundaries: 77, doc: 40, test: 34
- `propcache-0.4.1/tests/test_benchmarks.py` (PYTHON) | Magnitude: 56.22 | Delta: **0.158 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 26, doc: 18, generics: 16
- `propcache-0.4.1/tests/test_under_cached_property.py` (PYTHON) | Magnitude: 109.1 | Delta: **0.162 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 128, structural_boundaries: 85, generics: 38, test: 35
- `propcache-0.4.1/packaging/pep517_backend/_transformers.py` (PYTHON) | Magnitude: 39.3 | Delta: **0.26 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 61, doc: 24, structural_boundaries: 17, generics: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `propcache-0.4.1/src/propcache/api.py` (PYTHON) | Magnitude: 13.6 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, doc: 2, encapsulation: 2, indent_spaces: 2
- `propcache-0.4.1/packaging/pep517_backend/hooks.py` (PYTHON) | Magnitude: 15.28 | Delta: **0.118 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 9, import: 4, encapsulation: 4
- `propcache-0.4.1/packaging/pep517_backend/__init__.py` (PYTHON) | Magnitude: 10.52 | Delta: **0.184 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 2
- `propcache-0.4.1/src/propcache/_helpers_c.pyx` (PYTHON) | Magnitude: 82.0 | Delta: **0.366 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 21, encapsulation: 16, branch: 8

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py` -> **Severity: 0.284** (Bridge: 0.0028 * Flux: 99.5411%)
- `propcache-0.4.1/packaging/pep517_backend/_backend.py` -> **Severity: 0.059** (Bridge: 0.0043 * Flux: 13.8373%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `propcache-0.4.1/src/propcache/_helpers_py.py` -> **Severity: 6.173** (Embedded: 0.0772 * Error Risk: 80.0%)
- `propcache-0.4.1/src/propcache/_helpers_c.pyx` -> **Severity: 0.579** (Embedded: 0.0772 * Error Risk: 7.5054%)
- `propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py` -> **Severity: 0.546** (Embedded: 0.0833 * Error Risk: 6.5503%)
- `propcache-0.4.1/packaging/pep517_backend/_backend.py` -> **Severity: 0.153** (Embedded: 0.037 * Error Risk: 4.1398%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `propcache-0.4.1/src/propcache/_helpers_c.pyx` -> **Severity: 6401.195** (Blast Radius: 64.045 * Doc Risk: 99.9484%)
- `propcache-0.4.1/src/propcache/_helpers.py` -> **Severity: 6258.548** (Blast Radius: 95.037 * Doc Risk: 65.8538%)
- `propcache-0.4.1/packaging/pep517_backend/_compat.py` -> **Severity: 5992.428** (Blast Radius: 59.925 * Doc Risk: 99.9988%)
- `propcache-0.4.1/src/propcache/_helpers_py.py` -> **Severity: 5438.733** (Blast Radius: 64.045 * Doc Risk: 84.9205%)
- `propcache-0.4.1/packaging/pep517_backend/_cython_configuration.py` -> **Severity: 3083.596** (Blast Radius: 56.163 * Doc Risk: 54.9044%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
