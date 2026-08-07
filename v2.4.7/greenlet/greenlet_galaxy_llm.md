# ARCHITECTURAL_BRIEF: greenlet
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/greenlet` |
| **Timestamp** | `2026-08-07T05:23:00.423380+00:00` |
| **Scan Duration** | `0.39s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 85 malicious artifacts.

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
| Cognitive Load Exposure | 1.6 | 87.8 | 31.9 | 25.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 51.3 | 63.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 19.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 5.1 | 2.3 | 0.0 |
| API Exposure | 0.0 | 11.6 | 4.0 | 3.3 | 0.0 |
| Concurrency Exposure | 0.0 | 89.5 | 2.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 32.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 91.6 | 2.6 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 96.6 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 93.2 | 16.5 | 11.9 | 11.9 |
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

- `__repr__` (@ `greenlet-3.3.2/src/greenlet/tests/test_leaks.py`) -> Impact: **98.6** | LOC: 413
- `_report_diff` (@ `greenlet-3.3.2/src/greenlet/tests/leakcheck.py`) -> Impact: **73.9** | LOC: 127
- `green_dealloc` (@ `greenlet-3.3.2/src/greenlet/PyGreenlet.cpp`) -> Impact: **53.4** | LOC: 132
  * *Intent:* // During interpreter finalization, we cannot safely throw GreenletExit // into the greenlet. Doing so calls g_switch(), which performs a stack // swi...
- `_test_context` (@ `greenlet-3.3.2/src/greenlet/tests/test_contextvars.py`) -> Impact: **42.8** | LOC: 60
  * *Intent:* # pylint:disable=too-many-branches ID_VAR.set(0) callback = getcurrent().switch counts = dict((i, 0) for i in range(5)) lets = [ greenlet(partial( par...
- `normalize` (@ `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp`) -> Impact: **25.2** | LOC: 54
- `green_switch` (@ `greenlet-3.3.2/src/greenlet/PyGreenlet.cpp`) -> Impact: **24.8** | LOC: 55
  * *Intent:* /* Better to use tp_finalizer slot (PEP 442)
- `_do_test_throw_to_dead_thread_doesnt_cra` (@ `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py`) -> Impact: **23.6** | LOC: 56
- `MarkGreenletDeadIfNeeded` (@ `greenlet-3.3.2/src/greenlet/TThreadStateDestroy.cpp`) -> Impact: **23.6** | LOC: 73
- `test_implicit_parent_with_threads` (@ `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py`) -> Impact: **21.8** | LOC: 54
- `wait_for_pending_cleanups` (@ `greenlet-3.3.2/src/greenlet/tests/__init__.py`) -> Impact: **21.6** | LOC: 33

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `greenlet-3.3.2/src/greenlet` | 30 | 3080.64 | 49.75% | 46.03% |
| `greenlet-3.3.2/src/greenlet/tests` | 26 | 2417.46 | 13.93% | 0.0% |
| `greenlet-3.3.2/src/greenlet/platform` | 28 | 286.1 | 30.07% | 6.89% |
| `greenlet-3.3.2/benchmarks` | 1 | 85.06 | 6.11% | 62.37% |
| `greenlet-3.3.2` | 6 | 72.74 | 17.1% | 16.54% |

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
- `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py` -> **66** Orphaned Functions | **45** Duplicates
- `greenlet-3.3.2/src/greenlet/tests/test_tracing.py` -> **9** Orphaned Functions | **20** Duplicates
- `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp` -> **0** Orphaned Functions | **15** Duplicates
- `greenlet-3.3.2/src/greenlet/tests/test_contextvars.py` -> **10** Orphaned Functions | **0** Duplicates
- `greenlet-3.3.2/src/greenlet/tests/test_throw.py` -> **7** Orphaned Functions | **3** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `282` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `greenlet-3.3.2/src/greenlet/TGreenlet.cpp` (CPP) -> Cumulative Risk: **607.1**
- **Archetype:** `file_cluster_13` (Distance: 13.218 IQR)
- **Magnitude:** 161.54 | **LOC:** 726 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Tech Debt (99.8867%), Verification (80.0%)
- **Heaviest Functions:** `Greenlet::on_switchstack_or_initialstub_` (Impact: 19.3), `Greenlet::g_switchstack_success` (Impact: 11.7), `Greenlet::tp_traverse` (Impact: 11.0)

### 2. `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp` (CPP) -> Cumulative Risk: **592.63**
- **Archetype:** `file_cluster_8` (Distance: 12.67 IQR)
- **Magnitude:** 307.12 | **LOC:** 1119 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9962%), State Flux (99.8747%), Verification (80.0%)
- **Heaviest Functions:** `normalize` (Impact: 25.2), `operator=` (Impact: 8.9), `GreenletChecker` (Impact: 8.0)

### 3. `greenlet-3.3.2/make-manylinux` (SHELL) -> Cumulative Risk: **583.37**
- **Archetype:** `file_cluster_8` (Distance: 9.548 IQR)
- **Magnitude:** 33.48 | **LOC:** 72 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.2508%), Documentation (93.2138%), State Flux (82.2935%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 15.7), `__global_context__` (Impact: 1.9)

### 4. `greenlet-3.3.2/src/greenlet/TStackState.cpp` (CPP) -> Cumulative Risk: **579.5**
- **Archetype:** `file_cluster_8` (Distance: 12.766 IQR)
- **Magnitude:** 136.02 | **LOC:** 266 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Tech Debt (99.8906%), Safety Score (92.2814%)
- **Heaviest Functions:** `StackState::copy_from_stack` (Impact: 13.7), `StackState::copy_stack_to_heap` (Impact: 13.6), `StackState::StackState` (Impact: 4.0)

### 5. `greenlet-3.3.2/src/greenlet/PyGreenlet.cpp` (CPP) -> Cumulative Risk: **562.01**
- **Archetype:** `file_cluster_13` (Distance: 12.96 IQR)
- **Magnitude:** 312.12 | **LOC:** 796 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (92.1432%), Verification (80.0%)
- **Heaviest Functions:** `green_dealloc` (Impact: 53.4), `green_switch` (Impact: 24.8), `_green_dealloc_kill_started_non_main_gre` (Impact: 19.1)

### 6. `greenlet-3.3.2/src/greenlet/TUserGreenlet.cpp` (CPP) -> Cumulative Risk: **543.61**
- **Archetype:** `file_cluster_11` (Distance: 13.727 IQR)
- **Magnitude:** 150.4 | **LOC:** 663 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (93.9913%), Cognitive Load (86.6524%)
- **Heaviest Functions:** `UserGreenlet::parent` (Impact: 15.4), `UserGreenlet::thread_state` (Impact: 5.0), `UserGreenlet::run` (Impact: 4.5)

### 7. `greenlet-3.3.2/src/greenlet/greenlet_allocator.hpp` (CPP) -> Cumulative Risk: **528.57**
- **Archetype:** `file_cluster_13` (Distance: 11.298 IQR)
- **Magnitude:** 43.1 | **LOC:** 77 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9556%), Safety Score (84.3895%)
- **Heaviest Functions:** `allocate` (Impact: 7.7), `deallocate` (Impact: 7.6), `PythonAllocator` (Impact: 2.2)

### 8. `greenlet-3.3.2/src/greenlet/TGreenlet.hpp` (CPP) -> Cumulative Risk: **521.77**
- **Archetype:** `file_cluster_13` (Distance: 12.94 IQR)
- **Magnitude:** 63.16 | **LOC:** 838 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9998%), State Flux (99.9171%), Safety Score (78.9114%)
- **Heaviest Functions:** `single_result` (Impact: 8.6), `GCDisabledGuard` (Impact: 2.3), `operator<<` (Impact: 2.0)

### 9. `greenlet-3.3.2/src/greenlet/TExceptionState.cpp` (CPP) -> Cumulative Risk: **500.6**
- **Archetype:** `file_cluster_13` (Distance: 13.373 IQR)
- **Magnitude:** 48.4 | **LOC:** 63 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (88.0797%), Safety Score (80.1048%)
- **Heaviest Functions:** `operator>>` (Impact: 4.3), `operator<<` (Impact: 2.5), `ExceptionState::clear` (Impact: 2.5)

### 10. `greenlet-3.3.2/src/greenlet/TThreadState.hpp` (CPP) -> Cumulative Risk: **499.21**
- **Archetype:** `file_cluster_13` (Distance: 13.377 IQR)
- **Magnitude:** 105.84 | **LOC:** 544 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (90.5545%), Cognitive Load (73.038%)
- **Heaviest Functions:** `alloc_main` (Impact: 3.6), `operator new` (Impact: 2.2), `operator delete` (Impact: 2.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.241 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.968 IQR)
- **Top Global Matches:** file_cluster_4: 11.241, file_cluster_8: 11.307, file_cluster_13: 11.34
- **Magnitude:** 805.38 | **LOC:** 1366 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.2274%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_do_test_throw_to_dead_thread_doesnt_cra` (Impact: 23.6)
  * `test_implicit_parent_with_threads` (Impact: 21.8)
  * `attempt` (Impact: 14.4)
  * `test_two_recursive_children` (Impact: 13.2)
  * `test_issue_245_reference_counting_subcla` (Impact: 10.7)
    * *Intent:* # https://github.com/python-greenlet/greenlet/issues/245 # Before the fix, this crashed pretty relia...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 285`, `args: 163`, `func_start: 139`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 80`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 9`, `duplicate_logic: 45`, `orphaned_logic: 66`
* *Architecture:* `io: 21`, `api: 136`, `concurrency: 69`, `import: 24`
* *Defense:* `safety: 27`, `test: 84`, `sync_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` io, , greenlet, functools, time, sys, unittest, .leakcheck...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/greenlet.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.304 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.281 IQR)
- **Top Global Matches:** file_cluster_13: 11.304, file_cluster_8: 11.547, file_cluster_11: 12.087
- **Magnitude:** 654.22 | **LOC:** 324 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.4207%), Tech Debt (29.4819%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 53`, `args: 13`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 56`, `fragile_debt: 2`
* *Architecture:* `import: 26`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` TMainGreenlet.cpp, PyGreenlet.cpp, Python.h, algorithm, exception, TGreenlet.hpp, CObjects.cpp, TExceptionState.cpp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/PyGreenlet.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.96 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.689 IQR)
- **Top Global Matches:** file_cluster_13: 12.96, file_cluster_8: 13.115, file_cluster_11: 13.225
- **Magnitude:** 312.12 | **LOC:** 796 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.9882%), Tech Debt (53.0556%)
**Top Internal Functions/Classes:**
  * `green_dealloc` (Impact: 53.4)
    * *Intent:* // During interpreter finalization, we cannot safely throw GreenletExit // into the greenlet. Doing ...
  * `green_switch` (Impact: 24.8)
    * *Intent:* /* Better to use tp_finalizer slot (PEP 442)
  * `_green_dealloc_kill_started_non_main_gre` (Impact: 19.1)
    * *Intent:* // // - stack_prev is not visited: holds previous stack pointer, but it's not // referenced // - fra...
  * `green_init` (Impact: 13.3)
  * `internal_green_throw` (Impact: 5.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 32`, `args: 17`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 179`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 4`
* *Architecture:* `api: 2`, `import: 12`
* *Defense:* `safety: 8`, `doc: 2`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.837
  * `Choke Point (Betweenness):` 4.2e-05 | `Ripple Effect (Closeness):` 0.011111
  * `Imports (Out-Degree: 8):` TThreadStateDestroy.cpp, greenlet_internal.hpp, greenlet_slp_switch.hpp, TGreenlet.hpp, TGreenletGlobals.cpp, PyGreenlet.hpp, Python.h, structmember.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.72%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.67 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.837 IQR)
- **Top Global Matches:** file_cluster_8: 12.67, file_cluster_13: 12.681, file_cluster_11: 12.696
- **Magnitude:** 307.12 | **LOC:** 1119 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.1187%), Tech Debt (99.9962%)
**Top Internal Functions/Classes:**
  * `normalize` (Impact: 25.2)
  * `operator=` (Impact: 8.9)
  * `GreenletChecker` (Impact: 8.0)
  * `ListChecker` (Impact: 6.5)
  * `ContextExactChecker` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 182`, `args: 61`, `func_start: 48`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 148`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 1`, `duplicate_logic: 15`
* *Architecture:* `api: 20`, `import: 6`
* *Defense:* `safety: 28`, `immutability_locks: 76`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.444
  * `Choke Point (Betweenness):` 0.002075 | `Ripple Effect (Closeness):` 0.148148
  * `Imports (Out-Degree: 3):` Python.h, greenlet_cpython_compat.hpp, iostream, greenlet_exceptions.hpp, string, greenlet_compiler_compat.hpp
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/slp_platformselect.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.44%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.762 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.262 IQR)
- **Top Global Matches:** file_cluster_8: 15.762, file_cluster_13: 15.898, file_cluster_11: 16.184
- **Magnitude:** 298.44 | **LOC:** 78 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.8182%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `args: 5`
* *Risk/State:* `state_mutation: 282`
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.183
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.025397
  * `Imports (Out-Degree: 0):` switch_csky_gcc.h, switch_arm32_ios.h, TargetConditionals.h, switch_alpha_unix.h, switch_s390_unix.h, switch_sh_gcc.h, switch_x86_msvc.h, switch_arm64_msvc.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/tests/test_leaks.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.766 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.018 IQR)
- **Top Global Matches:** file_cluster_13: 10.766, file_cluster_0: 10.887, file_cluster_4: 10.901
- **Magnitude:** 192.22 | **LOC:** 475 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.7724%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 98.6)
  * `test_untracked_memory_doesnt_increase_un` (Impact: 7.6)
    * *Intent:* # Because the main greenlets from the background threads do not exit in a timely fashion,
  * `__init__` (Impact: 1.9)
  * `__del__` (Impact: 1.8)
  * `test_untracked_memory_doesnt_increase_un` (Impact: 1.8)
    * *Intent:* # Because we're just trying to track raw memory, not objects, and running
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 78`, `args: 35`, `func_start: 33`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 31`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `io: 7`, `api: 26`, `concurrency: 18`, `import: 15`
* *Defense:* `safety: 10`, `doc: 2`, `test: 19`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, , greenlet, time, sys, weakref, .leakcheck, unittest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/TPythonState.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.73 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.747 IQR)
- **Top Global Matches:** file_cluster_8: 13.73, file_cluster_13: 13.911, file_cluster_11: 13.926
- **Magnitude:** 162.88 | **LOC:** 440 | **CtrlFlow:** 79.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.8498%), Tech Debt (44.3425%)
**Top Internal Functions/Classes:**
  * `PythonState::did_finish` (Impact: 12.2)
    * *Intent:* #endif // GREENLET_PY312 #if GREENLET_PY313
  * `PythonState::set_initial_state` (Impact: 7.7)
    * *Intent:* #if GREENLET_PY311 // PyThreadState_GetFrame is probably going to have to allocate a // new frame ob...
  * `PythonState::will_switch_from` (Impact: 6.5)
  * `PythonState::tp_traverse` (Impact: 4.8)
  * `PythonState::set_new_cframe` (Impact: 1.4)
    * *Intent:* #endif
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 8`, `args: 4`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 120`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `safety: 6`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.837
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011111
  * `Imports (Out-Degree: 1):` Python.h, TGreenlet.hpp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/TGreenlet.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.218 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.504 IQR)
- **Top Global Matches:** file_cluster_13: 13.218, file_cluster_8: 13.292, file_cluster_11: 13.354
- **Magnitude:** 161.54 | **LOC:** 726 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.6285%), Tech Debt (99.8867%)
**Top Internal Functions/Classes:**
  * `Greenlet::on_switchstack_or_initialstub_` (Impact: 19.3)
    * *Intent:* // If we're killed because we lost all references in the
  * `Greenlet::g_switchstack_success` (Impact: 11.7)
    * *Intent:* #endif
  * `Greenlet::tp_traverse` (Impact: 11.0)
    * *Intent:* /* Currently running greenlet: context is stored in the thread state,
  * `Greenlet::check_switch_allowed` (Impact: 3.1)
  * `Greenlet::g_switch_finish` (Impact: 2.8)
    * *Intent:* // TODO: Make this take a parameter of the current greenlet, // or current main greenlet, to make th...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 26`, `args: 12`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 86`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `api: 9`, `import: 4`
* *Defense:* `safety: 17`, `doc: 4`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.577
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.022222
  * `Imports (Out-Degree: 4):` TThreadStateDestroy.cpp, greenlet_internal.hpp, TGreenlet.hpp, TGreenletGlobals.cpp
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/TUserGreenlet.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.727 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.647 IQR)
- **Top Global Matches:** file_cluster_11: 13.727, file_cluster_13: 13.744, file_cluster_0: 13.807
- **Magnitude:** 150.4 | **LOC:** 663 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.6524%), Tech Debt (93.9913%)
**Top Internal Functions/Classes:**
  * `UserGreenlet::parent` (Impact: 15.4)
    * *Intent:* // the successful switch cleared these out, we need to // restore our version. They will be copied o...
  * `UserGreenlet::thread_state` (Impact: 5.0)
  * `UserGreenlet::run` (Impact: 4.5)
  * `UserGreenlet::belongs_to_thread` (Impact: 4.2)
  * `operator new` (Impact: 2.2)
    * *Intent:* /** * Implementation of greenlet::UserGreenlet. * * Format with: * clang-format -i --style=file src/...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 18`, `args: 10`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 91`, `dead_code: 2`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 10`, `import: 3`
* *Defense:* `safety: 15`, `doc: 1`, `immutability_locks: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.837
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011111
  * `Imports (Out-Degree: 3):` TThreadStateDestroy.cpp, greenlet_internal.hpp, TGreenlet.hpp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/tests/leakcheck.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.118 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.92 IQR)
- **Top Global Matches:** file_cluster_13: 12.118, file_cluster_0: 12.299, file_cluster_11: 12.304
- **Magnitude:** 147.62 | **LOC:** 337 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.5141%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_report_diff` (Impact: 73.9)
  * `_include_object_p` (Impact: 21.1)
    * *Intent:* # This appears in Python3.14 with the JIT enabled. It # doesn't seem to be directly exposed to Pytho...
  * `fails_leakcheck` (Impact: 3.8)
  * `__init__` (Impact: 2.5)
    * *Intent:* # Some builtin things that we ignore # XXX: Those things were ignored by gevent, but they're importa...
  * `ignores_leakcheck` (Impact: 2.0)
    * *Intent:* """ Ignore the given object during leakchecks. Can be applied to a method, in which case the method ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 57`, `args: 17`, `func_start: 17`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 19`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 12`, `api: 11`, `import: 7`
* *Defense:* `safety: 13`, `doc: 6`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 33.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.044444
  * `Imports (Out-Degree: 0):` __future__, os, the, functools, sys, unittest, objgraph, gc
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/tests/test_generator_nested.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.452 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.307 IQR)
- **Top Global Matches:** file_cluster_13: 11.452, file_cluster_8: 11.469, file_cluster_0: 11.605
- **Magnitude:** 139.94 | **LOC:** 169 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.7951%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `perms` (Impact: 12.5)
  * `__next__` (Impact: 9.5)
  * `Yield` (Impact: 7.5)
  * `test_genlet_simple` (Impact: 7.3)
    * *Intent:* # XXX Test to make sure we are working as a generator expression
  * `a` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 35`, `args: 20`, `func_start: 20`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 31`, `fragile_debt: 1`, `orphaned_logic: 7`
* *Architecture:* `api: 19`, `import: 3`
* *Defense:* `safety: 4`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .leakcheck, greenlet, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/tests/test_contextvars.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.858 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.822 IQR)
- **Top Global Matches:** file_cluster_8: 8.858, file_cluster_13: 9.111, file_cluster_7: 9.57
- **Magnitude:** 139.68 | **LOC:** 313 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.2434%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_test_context` (Impact: 42.8)
    * *Intent:* # pylint:disable=too-many-branches ID_VAR.set(0) callback = getcurrent().switch counts = dict((i, 0)...
  * `test_context_assignment_while_running` (Impact: 14.0)
    * *Intent:* # pylint:disable=too-many-statements ID_VAR.set(None) def target(): self.assertIsNone(ID_VAR.get()) ...
  * `_increment` (Impact: 10.3)
  * `test_contextvars_errors` (Impact: 9.6)
  * `test_context_assignment_different_thread` (Impact: 8.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 49`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`, `fragile_debt: 1`, `orphaned_logic: 10`
* *Architecture:* `io: 2`, `api: 15`, `concurrency: 6`, `import: 15`
* *Defense:* `safety: 6`, `test: 17`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, contextvars, , greenlet, functools, sys, unittest, gc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/TStackState.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.766 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 6.191 IQR)
- **Top Global Matches:** file_cluster_8: 12.766, file_cluster_13: 12.909, file_cluster_0: 12.997
- **Magnitude:** 136.02 | **LOC:** 266 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.8093%), Tech Debt (99.8906%)
**Top Internal Functions/Classes:**
  * `StackState::copy_from_stack` (Impact: 13.7)
  * `StackState::copy_stack_to_heap` (Impact: 13.6)
  * `StackState::StackState` (Impact: 4.0)
    * *Intent:* #endif
  * `StackState::set_inactive` (Impact: 2.9)
  * `operator<<` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 34`, `args: 5`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 4`, `state_mutation: 73`, `fragile_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `safety: 12`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.837
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011111
  * `Imports (Out-Degree: 1):` iostream, TGreenlet.hpp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/tests/_test_extension_cpp.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.41 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.39 IQR)
- **Top Global Matches:** file_cluster_8: 12.41, file_cluster_13: 12.444, file_cluster_17: 12.637
- **Magnitude:** 136.0 | **LOC:** 230 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.1565%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_exception_switch_recurse` (Impact: 15.6)
  * `test_exception_switch_and_do_in_g2` (Impact: 15.6)
  * `PyInit__test_extension_cpp` (Impact: 5.5)
  * `test_exception_switch` (Impact: 3.9)
  * `py_test_exception_throw_nonstd` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 30`, `args: 17`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 77`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `import: 4`
* *Defense:* `safety: 7`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdexcept, greenlet_compiler_compat.hpp, exception, greenlet.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/platform/switch_x86_msvc.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.862 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.738 IQR)
- **Top Global Matches:** file_cluster_8: 12.862, file_cluster_13: 13.166, file_cluster_12: 13.209
- **Magnitude:** 130.14 | **LOC:** 327 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.261%), Tech Debt (27.1931%)
**Top Internal Functions/Classes:**
  * `GreenletVectorHandler` (Impact: 20.2)
    * *Intent:* * Walking the SEH list at key points can also be helpful. * * References: * https://en.wikipedia.org...
  * `x86_slp_show_seh_chain` (Impact: 8.0)
    * *Intent:* * returns control to greenlet A, we have replaced the contents of the stack * in memory, so all the ...
  * `IS_ON_STACK` (Impact: 3.1)
    * *Intent:* * * Stack switching breaks SEH because the call stack no longer necessarily * matches the SEH list. ...
  * `slp_switch` (Impact: 2.6)
    * *Intent:* */ #define WIN32_LEAN_AND_MEAN #include <windows.h> #pragma optimize("", off) /* so that autos are s...
  * `slp_get_exception_state` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 15`, `args: 10`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 88`, `fragile_debt: 1`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` windows.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/tests/test_tracing.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.777 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.543 IQR)
- **Top Global Matches:** file_cluster_8: 8.777, file_cluster_13: 9.124, file_cluster_7: 9.353
- **Magnitude:** 121.66 | **LOC:** 300 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.2725%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_a_greenlet_tracing` (Impact: 4.4)
  * `test_trace_events_trivial` (Impact: 4.4)
    * *Intent:* """ maxDiff = None def test_trace_events_trivial(self): with PythonTracer() as actions: tpt_callback...
  * `test_b_exception_disables_tracing` (Impact: 4.1)
  * `test_trace_events_multiple_greenlets_swi` (Impact: 4.1)
  * `test_set_same_tracer_twice` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 81`, `args: 33`, `func_start: 33`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 9`, `duplicate_logic: 20`, `orphaned_logic: 9`
* *Architecture:* `io: 2`, `api: 27`, `import: 7`
* *Defense:* `safety: 1`, `doc: 4`, `test: 17`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, , greenlet, sys, unittest, sysconfig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/tests/_test_extension.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.442 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.813 IQR)
- **Top Global Matches:** file_cluster_8: 10.442, file_cluster_7: 10.996, file_cluster_13: 11.057
- **Magnitude:** 106.72 | **LOC:** 259 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.5398%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `PyInit__test_extension` (Impact: 3.6)
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

### `greenlet-3.3.2/src/greenlet/TThreadState.hpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.95%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.377 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.456 IQR)
- **Top Global Matches:** file_cluster_13: 13.377, file_cluster_8: 13.574, file_cluster_11: 13.662
- **Magnitude:** 105.84 | **LOC:** 544 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.038%), Tech Debt (65.6922%)
**Top Internal Functions/Classes:**
  * `alloc_main` (Impact: 3.6)
    * *Intent:* * compilers or ``__thread``/``declspec(thread)`` for older GCC/clang * or MSVC, respectively.) * * P...
  * `operator new` (Impact: 2.2)
    * *Intent:* * greenlet), and did not invoke one of the greenlet APIs *in that * thread, immediately before it ex...
  * `operator delete` (Impact: 2.2)
    * *Intent:* * instead of the Python thread dictionary, thus avoiding a cycle. * * To fully solve this problem, w...
  * `restore_exception_state` (Impact: 1.6)
  * `ThreadState` (Impact: 1.5)
    * *Intent:* * longer be switched to. * * There are two small wrinkles. The first is that when the thread * exits...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 25`, `args: 8`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 86`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `safety: 11`, `doc: 1`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.327
  * `Choke Point (Betweenness):` 0.000114 | `Ripple Effect (Closeness):` 0.06
  * `Imports (Out-Degree: 3):` greenlet_internal.hpp, atomic, greenlet_refs.hpp, stdexcept, greenlet_thread_support.hpp, ctime
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/tests/__init__.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.109 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.667 IQR)
- **Top Global Matches:** file_cluster_13: 10.109, file_cluster_8: 10.525, file_cluster_17: 10.745
- **Magnitude:** 104.8 | **LOC:** 249 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.2425%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `wait_for_pending_cleanups` (Impact: 21.6)
  * `count_objects` (Impact: 14.8)
  * `__new__` (Impact: 12.0)
    * *Intent:* # a) leak checks def __new__(cls, classname, bases, classDict): # pylint and pep8 fight over what th...
  * `get_expected_returncodes_for_aborted_pro` (Impact: 7.4)
  * `run_script` (Impact: 7.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 59`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `state_mutation: 6`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 11`, `api: 14`, `concurrency: 1`, `import: 18`
* *Defense:* `safety: 6`, `doc: 6`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , os, subprocess, greenlet, time, sys, unittest, signal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/PyModule.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.001 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.419 IQR)
- **Top Global Matches:** file_cluster_8: 11.001, file_cluster_13: 11.29, file_cluster_7: 11.575
- **Magnitude:** 91.52 | **LOC:** 293 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.8204%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mod_enable_optional_cleanup` (Impact: 6.4)
  * `mod_set_thread_local` (Impact: 6.1)
  * `mod_settrace` (Impact: 6.0)
  * `mod_get_clocks_used_doing_optional_clean` (Impact: 4.1)
  * `mod_gettrace` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 22`, `args: 13`, `func_start: 8`
* *Risk/State:* `state_mutation: 49`
* *Architecture:* `api: 7`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.837
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011111
  * `Imports (Out-Degree: 4):` TMainGreenlet.cpp, TThreadStateDestroy.cpp, greenlet_internal.hpp, TGreenletGlobals.cpp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/benchmarks/chain.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.273 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.96 IQR)
- **Top Global Matches:** file_cluster_8: 8.273, file_cluster_7: 9.027, file_cluster_13: 9.046
- **Magnitude:** 85.06 | **LOC:** 252 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.1077%), Tech Debt (62.3743%)
**Top Internal Functions/Classes:**
  * `_bm_recur_frame` (Impact: 10.5)
  * `bm_switch_deep` (Impact: 10.3)
  * `bm_switch_shallow` (Impact: 6.6)
  * `bm_chain` (Impact: 5.8)
  * `recur_then_switch` (Impact: 5.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 42`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 14`, `import: 3`
* *Defense:* `safety: 7`, `doc: 2`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyperf, greenlet, os
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/CObjects.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.659 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.947 IQR)
- **Top Global Matches:** file_cluster_8: 10.659, file_cluster_13: 10.745, file_cluster_7: 11.149
- **Magnitude:** 77.26 | **LOC:** 158 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.8967%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `PyGreenlet_Switch` (Impact: 10.9)
  * `PyGreenlet_New` (Impact: 10.1)
  * `PyGreenlet_Throw` (Impact: 7.5)
  * `Extern_PyGreenlet_GET_PARENT` (Impact: 4.0)
  * `Extern_PyGreenlet_MAIN` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 22`, `args: 9`, `func_start: 9`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 9`, `import: 5`
* *Defense:* `safety: 4`, `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.837
  * `Choke Point (Betweenness):` 7.3e-05 | `Ripple Effect (Closeness):` 0.011111
  * `Imports (Out-Degree: 5):` TThreadStateDestroy.cpp, greenlet_internal.hpp, PyGreenlet.hpp, greenlet_refs.hpp, greenlet_exceptions.hpp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/PyGreenletUnswitchable.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.469 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.541 IQR)
- **Top Global Matches:** file_cluster_13: 11.469, file_cluster_8: 11.579, file_cluster_7: 12.101
- **Magnitude:** 73.14 | **LOC:** 148 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.4749%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `green_unswitchable_setforce` (Impact: 6.9)
  * `green_unswitchable_setforceslp` (Impact: 6.9)
  * `green_unswitchable_new` (Impact: 4.0)
  * `green_unswitchable_getforce` (Impact: 2.0)
  * `green_unswitchable_getforceslp` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 26`, `args: 9`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 49`
* *Architecture:* `import: 11`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.837
  * `Choke Point (Betweenness):` 4.2e-05 | `Ripple Effect (Closeness):` 0.011111
  * `Imports (Out-Degree: 9):` TThreadStateDestroy.cpp, greenlet_internal.hpp, greenlet_slp_switch.hpp, TGreenlet.hpp, TGreenletGlobals.cpp, PyGreenlet.hpp, Python.h, structmember.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/tests/test_throw.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.117 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.554 IQR)
- **Top Global Matches:** file_cluster_8: 9.117, file_cluster_13: 9.852, file_cluster_7: 10.013
- **Magnitude:** 64.98 | **LOC:** 129 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.4687%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_throw_goes_to_original_parent` (Impact: 7.1)
  * `test_val` (Impact: 6.3)
  * `f` (Impact: 5.6)
  * `test_not_throwable` (Impact: 5.5)
  * `test_class` (Impact: 4.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 29`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `duplicate_logic: 3`, `orphaned_logic: 7`
* *Architecture:* `io: 1`, `api: 11`, `import: 3`
* *Defense:* `safety: 8`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, greenlet, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/tests/test_extension_interface.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.548 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.209 IQR)
- **Top Global Matches:** file_cluster_8: 9.548, file_cluster_13: 9.671, file_cluster_7: 10.291
- **Magnitude:** 64.72 | **LOC:** 116 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.4449%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_throw` (Impact: 6.2)
  * `test_not_throwable` (Impact: 5.7)
  * `test_non_traceback_param` (Impact: 4.0)
  * `test_instance_of_wrong_type` (Impact: 4.0)
  * `foo` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 31`, `args: 17`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `duplicate_logic: 2`, `orphaned_logic: 4`
* *Architecture:* `io: 1`, `api: 16`, `import: 7`
* *Defense:* `safety: 4`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.517
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, , greenlet, sys, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `greenlet-3.3.2/src/greenlet/TUserGreenlet.cpp` (CPP) | Magnitude: 150.4 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 137, state_mutation: 91, pointers: 56, branch: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `greenlet-3.3.2/src/greenlet/tests/fail_clearing_run_switches.py` (PYTHON) | Magnitude: 17.84 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 9, state_mutation: 8, encapsulation: 5
- `greenlet-3.3.2/src/greenlet/tests/test_generator_nested.py` (PYTHON) | Magnitude: 139.94 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 101, structural_boundaries: 35, state_mutation: 31, branch: 27
- `greenlet-3.3.2/src/greenlet/TGreenlet.hpp` (CPP) | Magnitude: 63.16 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 88, structural_boundaries: 41, state_mutation: 38, macros: 18
- `greenlet-3.3.2/src/greenlet/TExceptionState.cpp` (CPP) | Magnitude: 48.4 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 26, pointers: 26, indent_spaces: 19, macros: 8
- `greenlet-3.3.2/src/greenlet/greenlet_allocator.hpp` (CPP) | Magnitude: 43.1 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 43, state_mutation: 17, structural_boundaries: 15, args: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py` (PYTHON) | Magnitude: 805.38 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 914, structural_boundaries: 285, args: 163, func_start: 139

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp` (CPP) | Magnitude: 307.12 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 466, structural_boundaries: 182, state_mutation: 148, pointers: 83
- `greenlet-3.3.2/src/greenlet/tests/_test_extension_cpp.cpp` (CPP) | Magnitude: 136.0 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 122, state_mutation: 77, structural_boundaries: 30, branch: 20
- `greenlet-3.3.2/src/greenlet/greenlet_msvc_compat.hpp` (CPP) | Magnitude: 46.36 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 34, pointers: 24, indent_spaces: 19, macros: 13
- `greenlet-3.3.2/src/greenlet/tests/fail_cpp_exception.py` (PYTHON) | Magnitude: 5.48 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 6, encapsulation: 6, branch: 4
- `greenlet-3.3.2/src/greenlet/greenlet_slp_switch.hpp` (CPP) | Magnitude: 18.84 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_13`
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

- `greenlet-3.3.2/src/greenlet/greenlet_compiler_compat.hpp` -> **Severity: 12.961** (Embedded: 0.1547 * Error Risk: 83.7902%)
- `greenlet-3.3.2/src/greenlet/TGreenlet.hpp` -> **Severity: 11.518** (Embedded: 0.146 * Error Risk: 78.9114%)
- `greenlet-3.3.2/src/greenlet/greenlet_cpython_compat.hpp` -> **Severity: 11.16** (Embedded: 0.1434 * Error Risk: 77.8435%)
- `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp` -> **Severity: 10.957** (Embedded: 0.1481 * Error Risk: 73.9589%)
- `greenlet-3.3.2/src/greenlet/greenlet_allocator.hpp` -> **Severity: 8.935** (Embedded: 0.1059 * Error Risk: 84.3895%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `greenlet-3.3.2/src/greenlet/greenlet_compiler_compat.hpp` -> **Severity: 764.926** (Blast Radius: 64.17 * Doc Risk: 11.9203%)
- `greenlet-3.3.2/src/greenlet/greenlet_allocator.hpp` -> **Severity: 700.77** (Blast Radius: 20.301 * Doc Risk: 34.519%)
- `greenlet-3.3.2/make-manylinux` -> **Severity: 700.688** (Blast Radius: 7.517 * Doc Risk: 93.2138%)
- `greenlet-3.3.2/src/greenlet/greenlet_thread_support.hpp` -> **Severity: 696.381** (Blast Radius: 20.628 * Doc Risk: 33.759%)
- `greenlet-3.3.2/src/greenlet/TExceptionState.cpp` -> **Severity: 690.281** (Blast Radius: 7.837 * Doc Risk: 88.0797%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
