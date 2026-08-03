# ARCHITECTURAL_BRIEF: greenlet
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/greenlet` |
| **Timestamp** | `2026-08-03T21:21:13.834369+00:00` |
| **Scan Duration** | `0.43s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 85 malicious artifacts.

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
| Total Artifacts | 104 |
| Analyzed Artifacts (Scanned) | 91 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 13 |
| Total LOC | 7842 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 87.5% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2426 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3859 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8916 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 54 | 4298 | 59.3% |
| PYTHON | 28 | 3152 | 30.8% |
| PLAINTEXT | 3 | 0 | 3.3% |
| ASSEMBLY | 2 | 120 | 2.2% |
| YAML | 1 | 20 | 1.1% |
| SHELL | 1 | 44 | 1.1% |
| BATCH | 1 | 2 | 1.1% |
| C | 1 | 206 | 1.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.867`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 57 | 62.6% |
| file_cluster_13 | 28 | 30.8% |
| file_cluster_4 | 1 | 1.1% |
| file_cluster_11 | 1 | 1.1% |
| file_cluster_9 | 1 | 1.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 3.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 13*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 2x Excluded (Unsupported Extension: '.rst')
- `.obj`: 2x Excluded (Explicitly Denied Extension: '.obj')
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.psf`: 1x Excluded (Unsupported Extension: '.PSF')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 2.1 | 93.5 | 31.9 | 25.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 26.9 | 19.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 19.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 12.2 | 2.3 | 0.0 |
| API Exposure | 0.0 | 11.6 | 4.0 | 3.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 32.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 91.6 | 2.6 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 96.6 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 27.3 | 11.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 48.2 | 19.7 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 22.4 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.3 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py` (Hits: 21)
- `greenlet-3.3.2/src/greenlet/tests/leakcheck.py` (Hits: 12)
- `greenlet-3.3.2/src/greenlet/tests/__init__.py` (Hits: 11)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **TGreenlet.hpp** (`greenlet-3.3.2/src/greenlet/TGreenlet.hpp`) — 12 inbound connections
2. **greenlet_internal.hpp** (`greenlet-3.3.2/src/greenlet/greenlet_internal.hpp`) — 10 inbound connections
3. **greenlet_refs.hpp** (`greenlet-3.3.2/src/greenlet/greenlet_refs.hpp`) — 10 inbound connections
4. **greenlet_compiler_compat.hpp** (`greenlet-3.3.2/src/greenlet/greenlet_compiler_compat.hpp`) — 8 inbound connections
5. **TThreadStateDestroy.cpp** (`greenlet-3.3.2/src/greenlet/TThreadStateDestroy.cpp`) — 7 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **greenlet.cpp** (`greenlet-3.3.2/src/greenlet/greenlet.cpp`) — 26 outbound dependencies
2. **slp_platformselect.h** (`greenlet-3.3.2/src/greenlet/slp_platformselect.h`) — 25 outbound dependencies
3. **__init__.py** (`greenlet-3.3.2/src/greenlet/tests/__init__.py`) — 13 outbound dependencies
4. **test_greenlet.py** (`greenlet-3.3.2/src/greenlet/tests/test_greenlet.py`) — 12 outbound dependencies
5. **PyGreenletUnswitchable.cpp** (`greenlet-3.3.2/src/greenlet/PyGreenletUnswitchable.cpp`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_report_diff` (@ `greenlet-3.3.2/src/greenlet/tests/leakcheck.py`) -> Impact: **479.2** | LOC: 127
- `__repr__` (@ `greenlet-3.3.2/src/greenlet/tests/test_leaks.py`) -> Impact: **293.4** | LOC: 413
- `green_dealloc` (@ `greenlet-3.3.2/src/greenlet/PyGreenlet.cpp`) -> Impact: **123.5** | LOC: 132
  * *Intent:* // During interpreter finalization, we cannot safely throw GreenletExit // into the greenlet. Doing so calls g_switch(), which performs a stack // swi...
- `_test_context` (@ `greenlet-3.3.2/src/greenlet/tests/test_contextvars.py`) -> Impact: **122.5** | LOC: 60
  * *Intent:* # pylint:disable=too-many-branches ID_VAR.set(0) callback = getcurrent().switch counts = dict((i, 0) for i in range(5)) lets = [ greenlet(partial( par...
- `_include_object_p` (@ `greenlet-3.3.2/src/greenlet/tests/leakcheck.py`) -> Impact: **97.3** | LOC: 41
  * *Intent:* # This appears in Python3.14 with the JIT enabled. It # doesn't seem to be directly exposed to Python; the only way to get # one is to cause code to g...
- `normalize` (@ `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp`) -> Impact: **81.5** | LOC: 54
- `wait_for_pending_cleanups` (@ `greenlet-3.3.2/src/greenlet/tests/__init__.py`) -> Impact: **71.7** | LOC: 33
- `__new__` (@ `greenlet-3.3.2/src/greenlet/tests/__init__.py`) -> Impact: **67.9** | LOC: 17
  * *Intent:* # a) leak checks def __new__(cls, classname, bases, classDict): # pylint and pep8 fight over what this should be called (mcs or cls). # pylint gets it...
- `MarkGreenletDeadIfNeeded` (@ `greenlet-3.3.2/src/greenlet/TThreadStateDestroy.cpp`) -> Impact: **63.6** | LOC: 73
- `test_implicit_parent_with_threads` (@ `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py`) -> Impact: **59.9** | LOC: 54

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `__getattribute__` (@ `greenlet-3.3.2/src/greenlet/tests/fail_initialstub_already_started.py`) -> **O(2^N) [Recursive]**
- `_report_diff` (@ `greenlet-3.3.2/src/greenlet/tests/leakcheck.py`) -> **O(2^N) [Recursive]**
- `__new__` (@ `greenlet-3.3.2/src/greenlet/tests/__init__.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # a) leak checks def __new__(cls, classname, bases, classDict): # pylint and pep8 fight over what this should be called (mcs or cls). # pylint gets it...
- `Greenlet` (@ `greenlet-3.3.2/src/greenlet/TGreenlet.cpp`) -> **O(2^N) [Recursive]**
- `_include_object_p` (@ `greenlet-3.3.2/src/greenlet/tests/leakcheck.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # This appears in Python3.14 with the JIT enabled. It # doesn't seem to be directly exposed to Python; the only way to get # one is to cause code to g...
- `test_throw` (@ `greenlet-3.3.2/src/greenlet/tests/test_extension_interface.py`) -> **O(2^N) [Recursive]**
- `test_setparent` (@ `greenlet-3.3.2/src/greenlet/tests/test_extension_interface.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # pylint:disable=disallowed-name def foo(): def bar(): greenlet.getcurrent().parent.switch() # This final switch should go back to the main greenlet, ...
- `GreenletChecker` (@ `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp`) -> **O(2^N) [Recursive]**
- `tearDown` (@ `greenlet-3.3.2/src/greenlet/tests/__init__.py`) -> **O(2^N) [Recursive]**
- `__getattribute__` (@ `greenlet-3.3.2/src/greenlet/tests/fail_clearing_run_switches.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `__repr__` (@ `greenlet-3.3.2/src/greenlet/tests/test_leaks.py`) -> DB Complexity: **29**
- `test_version` (@ `greenlet-3.3.2/src/greenlet/tests/test_version.py`) -> DB Complexity: **22**
- `green_dealloc` (@ `greenlet-3.3.2/src/greenlet/PyGreenlet.cpp`) -> DB Complexity: **22**
  * *Intent:* // During interpreter finalization, we cannot safely throw GreenletExit // into the greenlet. Doing so calls g_switch(), which performs a stack // swi...
- `_report_diff` (@ `greenlet-3.3.2/src/greenlet/tests/leakcheck.py`) -> DB Complexity: **16**
- `test_two_recursive_children` (@ `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py`) -> DB Complexity: **12**
- `PythonState::did_finish` (@ `greenlet-3.3.2/src/greenlet/TPythonState.cpp`) -> DB Complexity: **12**
  * *Intent:* #endif // GREENLET_PY312 #if GREENLET_PY313
- `normalize` (@ `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp`) -> DB Complexity: **12**
- `test_issue_245_reference_counting_subcla` (@ `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py`) -> DB Complexity: **11**
  * *Intent:* # https://github.com/python-greenlet/greenlet/issues/245 # Before the fix, this crashed pretty reliably on # Python 3.10, at least on macOS; but much ...
- `StackState::copy_from_stack` (@ `greenlet-3.3.2/src/greenlet/TStackState.cpp`) -> DB Complexity: **10**
- `operator<<` (@ `greenlet-3.3.2/src/greenlet/TStackState.cpp`) -> DB Complexity: **10**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `greenlet-3.3.2/src/greenlet/tests` | 26 | 4091.46 | 13.99% | 0.0% |
| `greenlet-3.3.2/src/greenlet` | 30 | 3773.92 | 49.94% | 46.03% |
| `greenlet-3.3.2/src/greenlet/platform` | 28 | 322.1 | 30.07% | 6.89% |
| `greenlet-3.3.2/benchmarks` | 1 | 111.06 | 6.11% | 0.0% |
| `greenlet-3.3.2` | 6 | 81.74 | 16.4% | 16.54% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `greenlet-3.3.2/src/greenlet/TMainGreenlet.cpp` -> **100.0%** Exposure
- `greenlet-3.3.2/src/greenlet/greenlet_allocator.hpp` -> **100.0%** Exposure
- `greenlet-3.3.2/src/greenlet/TThreadStateCreator.hpp` -> **99.9999%** Exposure
- `greenlet-3.3.2/src/greenlet/TGreenlet.hpp` -> **99.9998%** Exposure
- `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp` -> **99.9962%** Exposure
### Highest State Flux (Mutation/Volatility)
- `greenlet-3.3.2/src/greenlet/PyGreenlet.cpp` -> **100.0%** Exposure
- `greenlet-3.3.2/src/greenlet/TExceptionState.cpp` -> **100.0%** Exposure
- `greenlet-3.3.2/src/greenlet/TPythonState.cpp` -> **100.0%** Exposure
- `greenlet-3.3.2/src/greenlet/TThreadState.hpp` -> **100.0%** Exposure
- `greenlet-3.3.2/src/greenlet/TUserGreenlet.cpp` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py` -> **66** Orphaned Functions | **4** Duplicates
- `greenlet-3.3.2/src/greenlet/tests/test_tracing.py` -> **9** Orphaned Functions | **10** Duplicates
- `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp` -> **0** Orphaned Functions | **15** Duplicates
- `greenlet-3.3.2/src/greenlet/tests/test_contextvars.py` -> **10** Orphaned Functions | **0** Duplicates
- `greenlet-3.3.2/src/greenlet/tests/test_interpreter_shutdown.py` -> **9** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`greenlet-3.3.2/src/greenlet/slp_platformselect.h`** -> AI Confidence: **99.44%**
2. **`greenlet-3.3.2/src/greenlet/tests/leakcheck.py`** -> AI Confidence: **99.31%**
3. **`greenlet-3.3.2/src/greenlet/PyGreenlet.cpp`** -> AI Confidence: **99.31%**
4. **`greenlet-3.3.2/src/greenlet/TPythonState.cpp`** -> AI Confidence: **99.29%**
5. **`greenlet-3.3.2/src/greenlet/tests/test_contextvars.py`** -> AI Confidence: **99.23%**
6. **`greenlet-3.3.2/src/greenlet/greenlet_compiler_compat.hpp`** -> AI Confidence: **99.23%**
7. **`greenlet-3.3.2/src/greenlet/greenlet_cpython_compat.hpp`** -> AI Confidence: **99.23%**
8. **`greenlet-3.3.2/src/greenlet/tests/test_greenlet.py`** -> AI Confidence: **99.18%**
9. **`greenlet-3.3.2/src/greenlet/tests/__init__.py`** -> AI Confidence: **99.16%**
10. **`greenlet-3.3.2/src/greenlet/tests/test_leaks.py`** -> AI Confidence: **99.15%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `greenlet-3.3.2/src/greenlet/tests/__init__.py` -> **100.0%** Exposure
- `greenlet-3.3.2/src/greenlet/tests/fail_initialstub_already_started.py` -> **100.0%** Exposure
- `greenlet-3.3.2/src/greenlet/tests/leakcheck.py` -> **100.0%** Exposure
- `greenlet-3.3.2/src/greenlet/tests/test_contextvars.py` -> **100.0%** Exposure
- `greenlet-3.3.2/src/greenlet/tests/test_extension_interface.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `greenlet-3.3.2/src/greenlet/tests/test_interpreter_shutdown.py` -> **100.0%** Exposure
### Raw Memory Manipulation
- `greenlet-3.3.2/src/greenlet/TPythonState.cpp` -> **10.0%** Exposure
- `greenlet-3.3.2/src/greenlet/TGreenlet.cpp` -> **6.6919%** Exposure
- `greenlet-3.3.2/src/greenlet/TStackState.cpp` -> **5.3531%** Exposure
- `greenlet-3.3.2/src/greenlet/TUserGreenlet.cpp` -> **1.192%** Exposure
- `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp` -> **0.1148%** Exposure
### Algorithmic DoS Exposure
- `greenlet-3.3.2/src/greenlet/tests/__init__.py` -> **100.0%** Exposure
- `greenlet-3.3.2/src/greenlet/tests/fail_initialstub_already_started.py` -> **100.0%** Exposure
- `greenlet-3.3.2/src/greenlet/tests/leakcheck.py` -> **100.0%** Exposure
- `greenlet-3.3.2/src/greenlet/tests/test_contextvars.py` -> **100.0%** Exposure
- `greenlet-3.3.2/src/greenlet/tests/test_cpp.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `282` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `greenlet-3.3.2/src/greenlet/TStackState.cpp` (CPP) -> Cumulative Risk: **805.85**
- **Archetype:** `file_cluster_8` (Distance: 12.766 IQR)
- **Magnitude:** 182.42 | **LOC:** 266 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9999%), Tech Debt (99.8906%)
- **Heaviest Functions:** `StackState::copy_stack_to_heap` (Impact: 43.9), `StackState::copy_from_stack` (Impact: 19.6), `StackState::StackState` (Impact: 9.2)

### 2. `greenlet-3.3.2/src/greenlet/greenlet_allocator.hpp` (CPP) -> Cumulative Risk: **762.24**
- **Archetype:** `file_cluster_13` (Distance: 11.264 IQR)
- **Magnitude:** 70.8 | **LOC:** 77 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `deallocate` (Impact: 18.0), `allocate` (Impact: 14.9), `PythonAllocator` (Impact: 8.2)

### 3. `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp` (CPP) -> Cumulative Risk: **746.29**
- **Archetype:** `file_cluster_8` (Distance: 12.682 IQR)
- **Magnitude:** 492.32 | **LOC:** 1119 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9962%), Documentation (99.9872%)
- **Heaviest Functions:** `normalize` (Impact: 81.5), `GreenletChecker` (Impact: 35.7), `operator=` (Impact: 20.9)

### 4. `greenlet-3.3.2/src/greenlet/TUserGreenlet.cpp` (CPP) -> Cumulative Risk: **695.93**
- **Archetype:** `file_cluster_11` (Distance: 13.761 IQR)
- **Magnitude:** 189.8 | **LOC:** 663 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (93.9913%)
- **Heaviest Functions:** `UserGreenlet::parent` (Impact: 29.4), `UserGreenlet::run` (Impact: 14.5), `UserGreenlet::thread_state` (Impact: 11.0)

### 5. `greenlet-3.3.2/src/greenlet/TMainGreenlet.cpp` (CPP) -> Cumulative Risk: **682.22**
- **Archetype:** `file_cluster_8` (Distance: 10.965 IQR)
- **Magnitude:** 80.74 | **LOC:** 161 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (97.8429%), Documentation (97.0871%)
- **Heaviest Functions:** `MainGreenlet::g_switch` (Impact: 13.2), `MainGreenlet::tp_traverse` (Impact: 6.6), `MainGreenlet::parent` (Impact: 6.4)

### 6. `greenlet-3.3.2/src/greenlet/TGreenlet.cpp` (CPP) -> Cumulative Risk: **681.34**
- **Archetype:** `file_cluster_13` (Distance: 13.212 IQR)
- **Magnitude:** 229.44 | **LOC:** 726 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9999%), Tech Debt (99.8867%)
- **Heaviest Functions:** `Greenlet::on_switchstack_or_initialstub_` (Impact: 37.2), `Greenlet::g_switchstack_success` (Impact: 31.6), `Greenlet::tp_traverse` (Impact: 28.3)

### 7. `greenlet-3.3.2/make-manylinux` (SHELL) -> Cumulative Risk: **670.91**
- **Archetype:** `file_cluster_8` (Distance: 9.507 IQR)
- **Magnitude:** 42.48 | **LOC:** 72 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9919%), Documentation (99.99%), Tech Debt (99.2508%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 24.7), `__global_context__` (Impact: 1.9)

### 8. `greenlet-3.3.2/src/greenlet/PyGreenlet.cpp` (CPP) -> Cumulative Risk: **647.93**
- **Archetype:** `file_cluster_13` (Distance: 12.982 IQR)
- **Magnitude:** 380.92 | **LOC:** 796 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Verification (80.0%)
- **Heaviest Functions:** `green_dealloc` (Impact: 123.5), `_green_dealloc_kill_started_non_main_gre` (Impact: 34.7), `green_init` (Impact: 25.4)

### 9. `greenlet-3.3.2/src/greenlet/platform/switch_x86_msvc.h` (CPP) -> Cumulative Risk: **643.12**
- **Archetype:** `file_cluster_8` (Distance: 12.978 IQR)
- **Magnitude:** 163.44 | **LOC:** 327 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Verification (80.0%)
- **Heaviest Functions:** `GreenletVectorHandler` (Impact: 37.5), `x86_slp_show_seh_chain` (Impact: 22.6), `slp_switch` (Impact: 4.0)

### 10. `greenlet-3.3.2/src/greenlet/TThreadStateCreator.hpp` (CPP) -> Cumulative Risk: **618.81**
- **Archetype:** `file_cluster_13` (Distance: 11.081 IQR)
- **Magnitude:** 53.68 | **LOC:** 103 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9999%), State Flux (99.9826%), Algorithmic Dos (99.8947%)
- **Heaviest Functions:** `state` (Impact: 13.1), `tp_traverse` (Impact: 8.3), `ThreadStateCreator` (Impact: 4.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.308 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.965 IQR)
- **Top Global Matches:** file_cluster_4: 11.308, file_cluster_8: 11.359, file_cluster_13: 11.398
- **Magnitude:** 1009.38 | **LOC:** 1366 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (25.5945%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_implicit_parent_with_threads` (Impact: 59.9 | O(N^5) | DB: 3)
  * `_do_test_throw_to_dead_thread_doesnt_cra` (Impact: 54.8 | O(N^4) | DB: 4)
  * `test_unexpected_reparenting_thread_runni` (Impact: 27.7 | O(N^5) | DB: 2)
    * *Intent:* # Like ``test_unexpected_reparenting``, except the background thread is # actually still alive. anot...
  * `test_two_recursive_children` (Impact: 25.3 | O(N^3) | DB: 12)
  * `test_issue_245_reference_counting_subcla` (Impact: 23.7 | O(N^4) | DB: 11)
    * *Intent:* # https://github.com/python-greenlet/greenlet/issues/245 # Before the fix, this crashed pretty relia...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 285`, `args: 140`, `func_start: 139`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 88`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 9`, `duplicate_logic: 4`, `orphaned_logic: 66`
* *Architecture:* `io: 21`, `api: 136`, `concurrency: 69`, `import: 24`
* *Defense:* `safety: 27`, `test: 84`, `sync_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` greenlet, sys, unittest, time, copy, abc, .leakcheck, threading...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/greenlet.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.337 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.284 IQR)
- **Top Global Matches:** file_cluster_13: 11.337, file_cluster_8: 11.579, file_cluster_11: 12.118
- **Magnitude:** 703.8 | **LOC:** 324 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (33.4207%), Tech Debt (29.4819%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 53`, `args: 16`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 56`, `fragile_debt: 2`
* *Architecture:* `import: 26`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` exception, TGreenlet.cpp, TThreadStateCreator.hpp, TThreadState.hpp, CObjects.cpp, TMainGreenlet.cpp, TThreadStateDestroy.cpp, PyModule.cpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/tests/leakcheck.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.118 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.92 IQR)
- **Top Global Matches:** file_cluster_13: 12.118, file_cluster_0: 12.299, file_cluster_11: 12.304
- **Magnitude:** 647.52 | **LOC:** 337 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (30.5141%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_report_diff` (Impact: 479.2 | O(2^N) | DB: 16)
  * `_include_object_p` (Impact: 97.3 | O(2^N))
    * *Intent:* # This appears in Python3.14 with the JIT enabled. It # doesn't seem to be directly exposed to Pytho...
  * `fails_leakcheck` (Impact: 10.7 | O(2^N))
  * `_growth` (Impact: 6.2 | O(N^6))
    * *Intent:* # Similarly, we need to check identity in our __dict__ to avoid mock explosions.
  * `get_objects` (Impact: 3.6 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 57`, `args: 17`, `func_start: 17`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 19`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 12`, `api: 11`, `import: 7`
* *Defense:* `safety: 13`, `doc: 6`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 33.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.044444
  * `Imports (Out-Degree: 0):` sys, unittest, the, functools, gc, __future__, objgraph, os
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.72%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.682 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.839 IQR)
- **Top Global Matches:** file_cluster_8: 12.682, file_cluster_13: 12.693, file_cluster_11: 12.707
- **Magnitude:** 492.32 | **LOC:** 1119 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (62.1187%), Tech Debt (99.9962%)
**Top Internal Functions/Classes:**
  * `normalize` (Impact: 81.5 | O(N^6) | DB: 12)
  * `GreenletChecker` (Impact: 35.7 | O(2^N) | DB: 4)
  * `operator=` (Impact: 20.9 | O(N^4) | DB: 8)
  * `ContextExactChecker` (Impact: 16.2 | O(N^5))
  * `ListChecker` (Impact: 12.5 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 182`, `args: 63`, `func_start: 48`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 148`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 1`, `duplicate_logic: 15`
* *Architecture:* `api: 20`, `import: 6`
* *Defense:* `safety: 28`, `immutability_locks: 76`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.444
  * `Choke Point (Betweenness):` 0.002075 | `Ripple Effect (Closeness):` 0.148148
  * `Imports (Out-Degree: 3):` greenlet_cpython_compat.hpp, greenlet_exceptions.hpp, string, iostream, greenlet_compiler_compat.hpp, Python.h
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/tests/test_leaks.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.766 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.018 IQR)
- **Top Global Matches:** file_cluster_13: 10.766, file_cluster_0: 10.887, file_cluster_4: 10.901
- **Magnitude:** 396.52 | **LOC:** 475 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (32.7724%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 293.4 | O(N^6) | DB: 29)
  * `test_untracked_memory_doesnt_increase_un` (Impact: 14.5 | O(N^3))
    * *Intent:* # Because the main greenlets from the background threads do not exit in a timely fashion,
  * `__init__` (Impact: 2.7 | O(N^2) | DB: 4)
  * `__del__` (Impact: 2.7 | O(N^2) | DB: 1)
  * `test_untracked_memory_doesnt_increase_un` (Impact: 2.7 | O(N^2))
    * *Intent:* # Because we're just trying to track raw memory, not objects, and running
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 78`, `args: 35`, `func_start: 33`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 31`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `io: 7`, `api: 26`, `concurrency: 18`, `import: 15`
* *Defense:* `safety: 10`, `doc: 2`, `test: 19`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` greenlet, sys, unittest, weakref, time, .leakcheck, threading, gc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/PyGreenlet.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.982 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.671 IQR)
- **Top Global Matches:** file_cluster_13: 12.982, file_cluster_8: 13.125, file_cluster_11: 13.248
- **Magnitude:** 380.92 | **LOC:** 796 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (63.9882%), Tech Debt (53.0556%)
**Top Internal Functions/Classes:**
  * `green_dealloc` (Impact: 123.5 | O(N^4) | DB: 22)
    * *Intent:* // During interpreter finalization, we cannot safely throw GreenletExit // into the greenlet. Doing ...
  * `_green_dealloc_kill_started_non_main_gre` (Impact: 34.7 | O(N^3) | DB: 6)
    * *Intent:* // // - stack_prev is not visited: holds previous stack pointer, but it's not // referenced // - fra...
  * `green_init` (Impact: 25.4 | O(N^3) | DB: 5)
  * `green_new` (Impact: 6.0 | O(N^2) | DB: 2)
  * `green_traverse` (Impact: 3.5 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 32`, `args: 19`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 179`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 4`
* *Architecture:* `api: 1`, `import: 12`
* *Defense:* `safety: 8`, `doc: 2`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.837
  * `Choke Point (Betweenness):` 4.2e-05 | `Ripple Effect (Closeness):` 0.011111
  * `Imports (Out-Degree: 8):` TGreenlet.hpp, greenlet_refs.hpp, TThreadStateDestroy.cpp, PyGreenlet.hpp, greenlet_internal.hpp, greenlet_thread_support.hpp, greenlet_slp_switch.hpp, TGreenletGlobals.cpp...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/slp_platformselect.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.44%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.762 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.262 IQR)
- **Top Global Matches:** file_cluster_8: 15.762, file_cluster_13: 15.898, file_cluster_11: 16.184
- **Magnitude:** 298.44 | **LOC:** 78 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (75.8182%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `args: 5`
* *Risk/State:* `state_mutation: 282`
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.183
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025397
  * `Imports (Out-Degree: 0):` switch_alpha_unix.h, switch_x64_msvc.h, switch_aarch64_gcc.h, switch_ppc_linux.h, switch_ppc_macosx.h, switch_ppc_aix.h, switch_s390_unix.h, switch_amd64_unix.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/tests/__init__.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.109 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.667 IQR)
- **Top Global Matches:** file_cluster_13: 10.109, file_cluster_8: 10.525, file_cluster_17: 10.745
- **Magnitude:** 276.2 | **LOC:** 249 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (7.2425%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `wait_for_pending_cleanups` (Impact: 71.7 | O(N^6))
  * `__new__` (Impact: 67.9 | O(2^N) | DB: 1)
    * *Intent:* # a) leak checks def __new__(cls, classname, bases, classDict): # pylint and pep8 fight over what th...
  * `count_objects` (Impact: 35.9 | O(N^4))
  * `run_script` (Impact: 21.9 | O(N^6) | DB: 9)
  * `tearDown` (Impact: 14.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 59`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `state_mutation: 6`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 11`, `api: 14`, `concurrency: 1`, `import: 18`
* *Defense:* `safety: 6`, `doc: 6`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` greenlet, unittest, sys, sysconfig, greenlet._greenlet, time, signal, threading...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/tests/test_contextvars.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.86 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.822 IQR)
- **Top Global Matches:** file_cluster_8: 8.86, file_cluster_13: 9.113, file_cluster_7: 9.572
- **Magnitude:** 264.58 | **LOC:** 313 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (12.9381%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_test_context` (Impact: 122.5 | O(N^5))
    * *Intent:* # pylint:disable=too-many-branches ID_VAR.set(0) callback = getcurrent().switch counts = dict((i, 0)...
  * `test_context_assignment_while_running` (Impact: 24.4 | O(N^3) | DB: 6)
    * *Intent:* # pylint:disable=too-many-statements ID_VAR.set(None) def target(): self.assertIsNone(ID_VAR.get()) ...
  * `_increment` (Impact: 20.1 | O(N^3))
  * `test_context_assignment_wrong_type` (Impact: 18.4 | O(N^6))
  * `test_contextvars_errors` (Impact: 18.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 49`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`, `fragile_debt: 1`, `orphaned_logic: 10`
* *Architecture:* `io: 2`, `api: 15`, `concurrency: 6`, `import: 15`
* *Defense:* `safety: 6`, `test: 17`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` greenlet, sys, unittest, threading, functools, gc, __future__, contextvars...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/tests/test_generator_nested.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.452 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.307 IQR)
- **Top Global Matches:** file_cluster_13: 11.452, file_cluster_8: 11.469, file_cluster_0: 11.605
- **Magnitude:** 239.54 | **LOC:** 169 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (24.7951%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `perms` (Impact: 48.9 | O(2^N))
  * `__next__` (Impact: 22.5 | O(N^4) | DB: 1)
  * `test_genlet_simple` (Impact: 21.1 | O(N^5) | DB: 1)
    * *Intent:* # XXX Test to make sure we are working as a generator expression
  * `Yield` (Impact: 14.5 | O(N^3))
  * `a` (Impact: 8.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 35`, `args: 20`, `func_start: 20`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 31`, `fragile_debt: 1`, `orphaned_logic: 7`
* *Architecture:* `api: 19`, `import: 3`
* *Defense:* `safety: 4`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` greenlet, .leakcheck, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/TGreenlet.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.212 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.504 IQR)
- **Top Global Matches:** file_cluster_13: 13.212, file_cluster_8: 13.286, file_cluster_11: 13.348
- **Magnitude:** 229.44 | **LOC:** 726 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (73.6285%), Tech Debt (99.8867%)
**Top Internal Functions/Classes:**
  * `Greenlet::on_switchstack_or_initialstub_` (Impact: 37.2 | O(N^3) | DB: 3)
    * *Intent:* // If we're killed because we lost all references in the
  * `Greenlet::g_switchstack_success` (Impact: 31.6 | O(N^6) | DB: 9)
    * *Intent:* #endif
  * `Greenlet::tp_traverse` (Impact: 28.3 | O(N^5) | DB: 9)
    * *Intent:* /* Currently running greenlet: context is stored in the thread state,
  * `Greenlet::slp_save_state` (Impact: 7.7 | O(N^6))
  * `Greenlet` (Impact: 6.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 26`, `args: 12`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 86`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `api: 9`, `import: 4`
* *Defense:* `safety: 17`, `doc: 4`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.577
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.022222
  * `Imports (Out-Degree: 4):` TGreenletGlobals.cpp, greenlet_internal.hpp, TGreenlet.hpp, TThreadStateDestroy.cpp
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/tests/_test_extension_cpp.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.41 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.39 IQR)
- **Top Global Matches:** file_cluster_8: 12.41, file_cluster_13: 12.444, file_cluster_17: 12.637
- **Magnitude:** 191.6 | **LOC:** 230 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (32.4784%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_exception_switch_recurse` (Impact: 50.2 | O(N^6) | DB: 6)
  * `test_exception_switch_and_do_in_g2` (Impact: 29.4 | O(N^3) | DB: 8)
  * `PyInit__test_extension_cpp` (Impact: 7.6 | O(N^2) | DB: 6)
  * `test_exception_switch` (Impact: 5.6 | O(N^2) | DB: 1)
  * `py_test_exception_throw_nonstd` (Impact: 5.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 30`, `args: 17`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 77`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `import: 4`
* *Defense:* `safety: 7`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` exception, greenlet_compiler_compat.hpp, stdexcept, greenlet.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/TUserGreenlet.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.761 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.65 IQR)
- **Top Global Matches:** file_cluster_11: 13.761, file_cluster_13: 13.778, file_cluster_0: 13.841
- **Magnitude:** 189.8 | **LOC:** 663 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (86.6524%), Tech Debt (93.9913%)
**Top Internal Functions/Classes:**
  * `UserGreenlet::parent` (Impact: 29.4 | O(N^3) | DB: 6)
    * *Intent:* // the successful switch cleared these out, we need to // restore our version. They will be copied o...
  * `UserGreenlet::run` (Impact: 14.5 | O(N^6) | DB: 1)
  * `UserGreenlet::thread_state` (Impact: 11.0 | O(N^4) | DB: 3)
  * `UserGreenlet::ParentIsCurrentGuard::Pare` (Impact: 6.4 | O(N^6) | DB: 2)
    * *Intent:* // Getting a C++ exception here isn't good. It's probably a // bug in the underlying greenlet, meani...
  * `operator delete` (Impact: 6.3 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 18`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 91`, `dead_code: 2`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 10`, `import: 3`
* *Defense:* `safety: 15`, `doc: 1`, `immutability_locks: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.837
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011111
  * `Imports (Out-Degree: 3):` greenlet_internal.hpp, TGreenlet.hpp, TThreadStateDestroy.cpp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/TStackState.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.766 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 6.191 IQR)
- **Top Global Matches:** file_cluster_8: 12.766, file_cluster_13: 12.909, file_cluster_0: 12.997
- **Magnitude:** 182.42 | **LOC:** 266 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (93.5026%), Tech Debt (99.8906%)
**Top Internal Functions/Classes:**
  * `StackState::copy_stack_to_heap` (Impact: 43.9 | O(N^6) | DB: 7)
  * `StackState::copy_from_stack` (Impact: 19.6 | O(N^2) | DB: 10)
  * `StackState::StackState` (Impact: 9.2 | O(N^4) | DB: 2)
    * *Intent:* #endif
  * `StackState` (Impact: 6.3 | O(2^N))
  * `StackState::set_inactive` (Impact: 3.9 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 34`, `args: 5`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 4`, `state_mutation: 73`, `fragile_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `safety: 12`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.837
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011111
  * `Imports (Out-Degree: 1):` TGreenlet.hpp, iostream
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/TPythonState.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.73 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.747 IQR)
- **Top Global Matches:** file_cluster_8: 13.73, file_cluster_13: 13.911, file_cluster_11: 13.926
- **Magnitude:** 175.28 | **LOC:** 440 | **CtrlFlow:** 79.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (72.8498%), Tech Debt (44.3425%)
**Top Internal Functions/Classes:**
  * `PythonState::did_finish` (Impact: 22.6 | O(N^3) | DB: 12)
    * *Intent:* #endif // GREENLET_PY312 #if GREENLET_PY313
  * `PythonState::set_initial_state` (Impact: 7.7 | O(N^1) | DB: 7)
    * *Intent:* #if GREENLET_PY311 // PyThreadState_GetFrame is probably going to have to allocate a // new frame ob...
  * `PythonState::tp_traverse` (Impact: 6.8 | O(N^2))
  * `PythonState::will_switch_from` (Impact: 6.5 | O(N^1) | DB: 3)
  * `PythonState::set_new_cframe` (Impact: 1.4 | O(N^1) | DB: 6)
    * *Intent:* #endif
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 8`, `args: 4`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 120`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `safety: 6`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.837
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011111
  * `Imports (Out-Degree: 1):` TGreenlet.hpp, Python.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/platform/switch_x86_msvc.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.978 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.763 IQR)
- **Top Global Matches:** file_cluster_8: 12.978, file_cluster_13: 13.279, file_cluster_12: 13.321
- **Magnitude:** 163.44 | **LOC:** 327 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (69.261%), Tech Debt (27.1931%)
**Top Internal Functions/Classes:**
  * `GreenletVectorHandler` (Impact: 37.5 | O(N^3) | DB: 10)
    * *Intent:* * Walking the SEH list at key points can also be helpful. * * References: * https://en.wikipedia.org...
  * `x86_slp_show_seh_chain` (Impact: 22.6 | O(N^4) | DB: 4)
    * *Intent:* * returns control to greenlet A, we have replaced the contents of the stack * in memory, so all the ...
  * `slp_switch` (Impact: 4.0 | O(N^3) | DB: 1)
    * *Intent:* */ #define WIN32_LEAN_AND_MEAN #include <windows.h> #pragma optimize("", off) /* so that autos are s...
  * `IS_ON_STACK` (Impact: 3.1 | O(N^1) | DB: 5)
    * *Intent:* * * Stack switching breaks SEH because the call stack no longer necessarily * matches the SEH list. ...
  * `slp_get_exception_state` (Impact: 1.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 15`, `args: 19`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 88`, `fragile_debt: 1`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` windows.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/tests/test_tracing.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.77 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.502 IQR)
- **Top Global Matches:** file_cluster_8: 8.77, file_cluster_13: 9.127, file_cluster_7: 9.348
- **Magnitude:** 146.06 | **LOC:** 300 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (5.1171%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_a_greenlet_tracing` (Impact: 7.9 | O(N^3))
  * `test_trace_events_trivial` (Impact: 7.8 | O(N^3))
    * *Intent:* """ maxDiff = None def test_trace_events_trivial(self): with PythonTracer() as actions: tpt_callback...
  * `test_b_exception_disables_tracing` (Impact: 7.6 | O(N^3))
  * `test_set_same_tracer_twice` (Impact: 7.3 | O(N^3))
  * `__call__` (Impact: 7.1 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 81`, `args: 33`, `func_start: 33`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 9`, `duplicate_logic: 10`, `orphaned_logic: 9`
* *Architecture:* `io: 2`, `api: 27`, `import: 7`
* *Defense:* `safety: 1`, `doc: 4`, `test: 17`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` greenlet, sys, sysconfig, unittest, __future__, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/tests/test_extension_interface.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.518 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.234 IQR)
- **Top Global Matches:** file_cluster_8: 9.518, file_cluster_13: 9.659, file_cluster_7: 10.264
- **Magnitude:** 137.02 | **LOC:** 116 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (4.3906%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_throw` (Impact: 27.0 | O(2^N) | DB: 4)
  * `test_not_throwable` (Impact: 18.7 | O(N^6))
  * `test_instance_of_wrong_type` (Impact: 12.7 | O(N^6))
  * `test_non_traceback_param` (Impact: 12.6 | O(N^6))
  * `test_setparent` (Impact: 9.6 | O(2^N))
    * *Intent:* # pylint:disable=disallowed-name def foo(): def bar(): greenlet.getcurrent().parent.switch() # This ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 31`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `orphaned_logic: 4`
* *Architecture:* `io: 1`, `api: 16`, `import: 7`
* *Defense:* `safety: 4`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` greenlet, sys, unittest, __future__, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/TThreadState.hpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.95%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.396 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.46 IQR)
- **Top Global Matches:** file_cluster_13: 13.396, file_cluster_8: 13.592, file_cluster_11: 13.682
- **Magnitude:** 124.04 | **LOC:** 544 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (73.038%), Tech Debt (65.6922%)
**Top Internal Functions/Classes:**
  * `alloc_main` (Impact: 14.7 | O(2^N) | DB: 3)
    * *Intent:* * compilers or ``__thread``/``declspec(thread)`` for older GCC/clang * or MSVC, respectively.) * * P...
  * `operator delete` (Impact: 6.3 | O(N^6))
    * *Intent:* * instead of the Python thread dictionary, thus avoiding a cycle. * * To fully solve this problem, w...
  * `restore_exception_state` (Impact: 3.5 | O(N^5))
  * `ThreadState` (Impact: 2.5 | O(N^3) | DB: 4)
    * *Intent:* * longer be switched to. * * There are two small wrinkles. The first is that when the thread * exits...
  * `init` (Impact: 1.8 | O(N^2) | DB: 1)
    * *Intent:* * reliably invokes its destructor when the thread it belongs to exits * (non-C++11 compilers offer `...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 25`, `args: 10`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 86`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `safety: 11`, `doc: 1`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.327
  * `Choke Point (Betweenness):` 0.000114 | `Ripple Effect (Closeness):` 0.06
  * `Imports (Out-Degree: 3):` greenlet_refs.hpp, stdexcept, greenlet_internal.hpp, ctime, greenlet_thread_support.hpp, atomic
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/PyModule.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.015 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.422 IQR)
- **Top Global Matches:** file_cluster_8: 11.015, file_cluster_13: 11.304, file_cluster_7: 11.588
- **Magnitude:** 113.12 | **LOC:** 293 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (51.8204%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mod_set_thread_local` (Impact: 19.1 | O(N^6) | DB: 4)
  * `mod_enable_optional_cleanup` (Impact: 9.0 | O(N^2) | DB: 5)
  * `mod_settrace` (Impact: 8.6 | O(N^2) | DB: 5)
  * `mod_get_clocks_used_doing_optional_clean` (Impact: 5.8 | O(N^2) | DB: 1)
  * `mod_gettrace` (Impact: 5.6 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 22`, `args: 14`, `func_start: 8`
* *Risk/State:* `state_mutation: 49`
* *Architecture:* `api: 7`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.837
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011111
  * `Imports (Out-Degree: 4):` greenlet_internal.hpp, TGreenletGlobals.cpp, TMainGreenlet.cpp, TThreadStateDestroy.cpp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/benchmarks/chain.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.279 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.012 IQR)
- **Top Global Matches:** file_cluster_8: 8.279, file_cluster_7: 9.034, file_cluster_13: 9.064
- **Magnitude:** 111.06 | **LOC:** 252 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.1077%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_bm_recur_frame` (Impact: 23.5 | O(N^4))
  * `bm_switch_deep` (Impact: 23.3 | O(N^4))
  * `bm_switch_shallow` (Impact: 14.4 | O(N^4))
  * `bm_chain` (Impact: 11.0 | O(N^3))
  * `bm_getcurrent` (Impact: 6.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 42`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `dead_code: 1`
* *Architecture:* `io: 1`, `api: 14`, `import: 3`
* *Defense:* `safety: 7`, `doc: 2`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` greenlet, pyperf, os
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/tests/_test_extension.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.442 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.813 IQR)
- **Top Global Matches:** file_cluster_8: 10.442, file_cluster_7: 10.996, file_cluster_13: 11.057
- **Magnitude:** 108.12 | **LOC:** 259 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (27.5398%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `PyInit__test_extension` (Impact: 5.0 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 26`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 62`, `orphaned_logic: 1`
* *Architecture:* `api: 37`, `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` greenlet.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/tests/test_throw.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.122 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.599 IQR)
- **Top Global Matches:** file_cluster_8: 9.122, file_cluster_13: 9.876, file_cluster_7: 10.019
- **Magnitude:** 105.48 | **LOC:** 129 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (3.4687%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_not_throwable` (Impact: 18.5 | O(N^6))
  * `test_val` (Impact: 16.7 | O(N^5) | DB: 3)
  * `test_throw_goes_to_original_parent` (Impact: 14.9 | O(N^4))
  * `test_non_traceback_param` (Impact: 12.6 | O(N^6))
  * `test_instance_of_wrong_type` (Impact: 12.6 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 29`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 7`
* *Architecture:* `io: 1`, `api: 11`, `import: 3`
* *Defense:* `safety: 8`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` greenlet, sys, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/CObjects.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.697 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.953 IQR)
- **Top Global Matches:** file_cluster_8: 10.697, file_cluster_13: 10.783, file_cluster_7: 11.185
- **Magnitude:** 100.96 | **LOC:** 158 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (21.8967%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `PyGreenlet_New` (Impact: 18.7 | O(N^3) | DB: 3)
  * `PyGreenlet_Switch` (Impact: 15.9 | O(N^2) | DB: 2)
  * `PyGreenlet_Throw` (Impact: 10.8 | O(N^2) | DB: 1)
  * `Extern_PyGreenlet_GET_PARENT` (Impact: 5.7 | O(N^2))
  * `Extern_PyGreenlet_MAIN` (Impact: 5.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 22`, `args: 11`, `func_start: 9`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 9`, `import: 5`
* *Defense:* `safety: 4`, `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.837
  * `Choke Point (Betweenness):` 7.3e-05 | `Ripple Effect (Closeness):` 0.011111
  * `Imports (Out-Degree: 5):` greenlet_refs.hpp, TThreadStateDestroy.cpp, PyGreenlet.hpp, greenlet_internal.hpp, greenlet_exceptions.hpp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/PyGreenletUnswitchable.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.469 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.541 IQR)
- **Top Global Matches:** file_cluster_13: 11.469, file_cluster_8: 11.579, file_cluster_7: 12.101
- **Magnitude:** 86.84 | **LOC:** 148 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (59.4749%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `green_unswitchable_setforce` (Impact: 12.9 | O(N^3) | DB: 3)
  * `green_unswitchable_setforceslp` (Impact: 12.9 | O(N^3) | DB: 3)
  * `green_unswitchable_new` (Impact: 5.7 | O(N^2) | DB: 1)
  * `green_unswitchable_getforce` (Impact: 2.0 | O(N^1) | DB: 1)
  * `green_unswitchable_getforceslp` (Impact: 2.0 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 26`, `args: 9`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 49`
* *Architecture:* `import: 11`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.837
  * `Choke Point (Betweenness):` 4.2e-05 | `Ripple Effect (Closeness):` 0.011111
  * `Imports (Out-Degree: 9):` TGreenlet.hpp, greenlet_refs.hpp, TThreadStateDestroy.cpp, PyGreenlet.hpp, greenlet_internal.hpp, TGreenlet.cpp, Python.h, greenlet_thread_support.hpp...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `greenlet-3.3.2/src/greenlet/TUserGreenlet.cpp` (CPP) | Magnitude: 189.8 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 137, state_mutation: 91, pointers: 56, branch: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `greenlet-3.3.2/src/greenlet/tests/fail_clearing_run_switches.py` (PYTHON) | Magnitude: 33.44 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 9, state_mutation: 8, encapsulation: 5
- `greenlet-3.3.2/src/greenlet/tests/test_generator_nested.py` (PYTHON) | Magnitude: 239.54 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 101, structural_boundaries: 35, state_mutation: 31, branch: 27
- `greenlet-3.3.2/src/greenlet/TGreenlet.hpp` (CPP) | Magnitude: 78.56 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 88, structural_boundaries: 41, state_mutation: 38, macros: 18
- `greenlet-3.3.2/src/greenlet/TExceptionState.cpp` (CPP) | Magnitude: 50.4 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 26, pointers: 26, indent_spaces: 19, macros: 8
- `greenlet-3.3.2/src/greenlet/greenlet_allocator.hpp` (CPP) | Magnitude: 70.8 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 43, state_mutation: 17, structural_boundaries: 15, args: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py` (PYTHON) | Magnitude: 1009.38 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 914, structural_boundaries: 285, args: 140, func_start: 139

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp` (CPP) | Magnitude: 492.32 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 466, structural_boundaries: 182, state_mutation: 148, pointers: 83
- `greenlet-3.3.2/src/greenlet/tests/_test_extension_cpp.cpp` (CPP) | Magnitude: 191.6 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 122, state_mutation: 77, structural_boundaries: 30, branch: 20
- `greenlet-3.3.2/src/greenlet/greenlet_msvc_compat.hpp` (CPP) | Magnitude: 58.16 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 34, pointers: 24, indent_spaces: 19, macros: 13
- `greenlet-3.3.2/src/greenlet/tests/fail_cpp_exception.py` (PYTHON) | Magnitude: 5.28 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 6, encapsulation: 6, branch: 4
- `greenlet-3.3.2/src/greenlet/greenlet_slp_switch.hpp` (CPP) | Magnitude: 18.14 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 12, macros: 12, indent_spaces: 12, globals: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `greenlet-3.3.2/src/greenlet/platform/switch_arm64_masm.asm` (ASSEMBLY) | Magnitude: 18.76 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 24, pointers: 11, args: 8

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `greenlet-3.3.2/src/greenlet/TGreenlet.hpp` -> **Severity: 0.653** (Bridge: 0.0065 * Flux: 99.9171%)
- `greenlet-3.3.2/src/greenlet/greenlet_internal.hpp` -> **Severity: 0.451** (Bridge: 0.0046 * Flux: 99.1972%)
- `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp` -> **Severity: 0.207** (Bridge: 0.0021 * Flux: 99.8747%)
- `greenlet-3.3.2/src/greenlet/TGreenletGlobals.cpp` -> **Severity: 0.079** (Bridge: 0.0008 * Flux: 99.9894%)
- `greenlet-3.3.2/src/greenlet/greenlet_slp_switch.hpp` -> **Severity: 0.043** (Bridge: 0.0004 * Flux: 99.9043%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `greenlet-3.3.2/src/greenlet/TGreenlet.hpp` -> **Severity: 7.23** (Embedded: 0.146 * Error Risk: 49.5312%)
- `greenlet-3.3.2/src/greenlet/greenlet_allocator.hpp` -> **Severity: 5.824** (Embedded: 0.1059 * Error Risk: 55.0%)
- `greenlet-3.3.2/src/greenlet/greenlet_compiler_compat.hpp` -> **Severity: 5.103** (Embedded: 0.1547 * Error Risk: 32.9898%)
- `greenlet-3.3.2/src/greenlet/greenlet.h` -> **Severity: 3.698** (Embedded: 0.0751 * Error Risk: 49.2308%)
- `greenlet-3.3.2/src/greenlet/greenlet_msvc_compat.hpp` -> **Severity: 3.463** (Embedded: 0.09 * Error Risk: 38.4798%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp` -> **Severity: 3443.959** (Blast Radius: 34.444 * Doc Risk: 99.9872%)
- `greenlet-3.3.2/src/greenlet/greenlet_exceptions.hpp` -> **Severity: 2528.969** (Blast Radius: 25.433 * Doc Risk: 99.4365%)
- `greenlet-3.3.2/src/greenlet/greenlet_allocator.hpp` -> **Severity: 2030.1** (Blast Radius: 20.301 * Doc Risk: 100.0%)
- `greenlet-3.3.2/src/greenlet/greenlet_msvc_compat.hpp` -> **Severity: 1521.648** (Blast Radius: 16.712 * Doc Risk: 91.0512%)
- `greenlet-3.3.2/src/greenlet/greenlet_thread_support.hpp` -> **Severity: 1460.545** (Blast Radius: 20.628 * Doc Risk: 70.804%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
