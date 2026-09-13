# ARCHITECTURAL_BRIEF: greenlet
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. A high Structural Surface Profile reading (formerly called Risk Exposure; e.g., Complexity Load, formerly Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict. These are activity/content surface meters, not defect-probability estimates (gitgalaxy#2991, evidence in #2982) -- describe what is there, don't imply it predicts a bug.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates the Structural Surface Profile (Lower 0 - Higher Surface Presence 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws. These 13 vectors are activity/content surface meters -- they describe what is present in a file, not the probability of a defect. The temporal-crucible validation record (gitgalaxy#2982, ~3,550 scanned snapshots, two repositories, pre-registered) tested the per-file-standing-risk claim to exhaustion and found it does not hold; see docs/vectors.md for the full record and gitgalaxy#2991 for the rename this drove. `risk_*` names remain the underlying column/key names for schema compatibility -- see the 'formerly' aliases below.
> 
> 1. **Complexity Load** (formerly Cognitive Load Exposure)**:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Guard Balance** (formerly Error & Exception Risk Exposure)**:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Debt Markers** (formerly Tech Debt Exposure)**:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Test Surface** (formerly Verification Risk Exposure)**:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **Connectivity** (formerly API Risk Exposure)**:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Surface** (formerly Concurrency Risk Exposure)**:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **Mutation Surface** (formerly State Flux Risk Exposure)**:** Measures the frequency of data mutation and variable reassignment.
> 8. **Dead Code Surface** (formerly Commented Logic (dead code))**:** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Alignment** (formerly Spec Match Risk Exposure)**:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Historical Stability** (formerly Stability; predictive layer, promotion pending #2987)**:** Measures the recency of edits relative to the repository's entire lifespan. Part of the family the validation record actually supports as predictive -- currently ablated to zero in every scan (`GITGALAXY_DISABLE_GIT_HISTORY`, temporal-crucible#29).
> 11. **Historical Churn** (formerly Deep Churn; predictive layer, promotion pending #2987)**:** Measures the historical volatility and frequency of modification. Same predictive-layer status and ablation caveat as Historical Stability above.
> 12. **Documentation Surface** (formerly Documentation Risk Exposure)**:** Of the units extracted from a file, the weight-share a reader cannot recover from documentation -- public units count double, runtime-dynamic units count more, and a folder-level documentation umbrella shields the whole file. A ratio over units, not a density over lines; files with no extracted units have no value.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Credential Material** (formerly Secrets Risk Exposure)**:** Measures the presence of hardcoded credentials exposed to logs or globals.
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
| Total LOC | 9672 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 87.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4048 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6254 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.9111 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 54 | 6127 | 59.3% |
| PYTHON | 28 | 3153 | 30.8% |
| PLAINTEXT | 3 | 0 | 3.3% |
| ASSEMBLY | 2 | 120 | 2.2% |
| YAML | 1 | 20 | 1.1% |
| SHELL | 1 | 44 | 1.1% |
| BATCH | 1 | 2 | 1.1% |
| C | 1 | 206 | 1.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 88 | 96.7% |

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

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 78.6 | 19.6 | 12.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.5 | 54.2 | 64.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 81.8 | 11.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.8 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 57.7 | 18.0 | 16.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 18.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 91.6 | 3.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 86.4 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 83.4 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1257 | 60 | 29 | `greenlet-3.3.2/src/greenlet/TPythonState.cpp` |
| cleanup | 13 | 8 | 0 | `greenlet-3.3.2/src/greenlet/tests/test_tracing.py` |
| guards | 880 | 51 | 19 | `greenlet-3.3.2/src/greenlet/TGreenlet.hpp` |
| danger | 301 | 58 | 9 | `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py` |
| concurrency | 86 | 9 | 0 | `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py` |
| connectivity | 589 | 72 | 16 | `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py` |
| io | 68 | 14 | 1 | `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 12 | 3 | 0 | `greenlet-3.3.2/src/greenlet/tests/__init__.py` |
| time | 4 | 2 | 0 | `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 9 | 4 | 0 | `greenlet-3.3.2/src/greenlet/tests/test_contextvars.py` |
| tests | 221 | 18 | 6 | `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py` |
| docs | 86 | 34 | 2 | `greenlet-3.3.2/src/greenlet/tests/test_interpreter_shutdown.py` |
| debt | 164 | 36 | 6 | `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py` |
| mutation | 2001 | 56 | 61 | `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py` |
| dead_code | 207 | 32 | 5 | `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py` |
| credential | 0 | 0 | 0 | - |
| threat | 213 | 62 | 6 | `greenlet-3.3.2/src/greenlet/greenlet.h` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py` (Hits: 21)
- `greenlet-3.3.2/setup.py` (Hits: 8)
- `greenlet-3.3.2/src/greenlet/tests/test_version.py` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **TGreenlet.hpp** (`greenlet-3.3.2/src/greenlet/TGreenlet.hpp`) — 12 inbound connections
2. **greenlet_internal.hpp** (`greenlet-3.3.2/src/greenlet/greenlet_internal.hpp`) — 10 inbound connections
3. **greenlet_refs.hpp** (`greenlet-3.3.2/src/greenlet/greenlet_refs.hpp`) — 10 inbound connections
4. **greenlet_compiler_compat.hpp** (`greenlet-3.3.2/src/greenlet/greenlet_compiler_compat.hpp`) — 9 inbound connections
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

- `_test_context` (@ `greenlet-3.3.2/src/greenlet/tests/test_contextvars.py`) -> Impact: **42.8** | LOC: 60
  * *Intent:* # pylint:disable=too-many-branches ID_VAR.set(0) callback = getcurrent().switch counts = dict((i, 0) for i in range(5)) lets = [ greenlet(partial( par...
- `UserGreenlet::inner_bootstrap` (@ `greenlet-3.3.2/src/greenlet/TUserGreenlet.cpp`) -> Impact: **32.7** | LOC: 187
- `_check_deltas` (@ `greenlet-3.3.2/src/greenlet/tests/leakcheck.py`) -> Impact: **31.8** | LOC: 48
  * *Intent:* # Return false when we have decided there is no leak, # true if we should keep looping, raises an assertion # if we have decided there is a leak. delt...
- `~ThreadState` (@ `greenlet-3.3.2/src/greenlet/TThreadState.hpp`) -> Impact: **31.4** | LOC: 147
- `_check_untracked_memory_thread` (@ `greenlet-3.3.2/src/greenlet/tests/test_leaks.py`) -> Impact: **25.0** | LOC: 85
- `_check_issue251` (@ `greenlet-3.3.2/src/greenlet/tests/test_leaks.py`) -> Impact: **24.2** | LOC: 125
- `PythonState::operator<<` (@ `greenlet-3.3.2/src/greenlet/TPythonState.cpp`) -> Impact: **21.7** | LOC: 66
- `wait_for_pending_cleanups` (@ `greenlet-3.3.2/src/greenlet/tests/__init__.py`) -> Impact: **21.6** | LOC: 33
- `PythonState::operator>>` (@ `greenlet-3.3.2/src/greenlet/TPythonState.cpp`) -> Impact: **21.5** | LOC: 62
  * *Intent:* #endif
- `green_repr` (@ `greenlet-3.3.2/src/greenlet/PyGreenlet.cpp`) -> Impact: **20.2** | LOC: 64

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `greenlet-3.3.2/src/greenlet/tests` | 26 | 3122.28 | 22.82% | 0.0% |
| `greenlet-3.3.2/src/greenlet` | 30 | 2226.2 | 23.73% | 26.5% |
| `greenlet-3.3.2/src/greenlet/platform` | 28 | 205.6 | 10.61% | 6.66% |
| `greenlet-3.3.2/benchmarks` | 1 | 191.26 | 54.95% | 0.0% |
| `greenlet-3.3.2` | 6 | 109.34 | 10.67% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `greenlet-3.3.2/src/greenlet/__init__.py` -> **81.7574%** Exposure
- `greenlet-3.3.2/src/greenlet/PyGreenlet.hpp` -> **81.7574%** Exposure
- `greenlet-3.3.2/src/greenlet/platform/switch_ppc64_aix.h` -> **81.7574%** Exposure
- `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp` -> **81.492%** Exposure
- `greenlet-3.3.2/src/greenlet/platform/switch_ppc64_linux.h` -> **80.5584%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `greenlet-3.3.2/benchmarks/chain.py` -> **100.0%** Exposure
- `greenlet-3.3.2/setup.py` -> **100.0%** Exposure
- `greenlet-3.3.2/src/greenlet/TExceptionState.cpp` -> **100.0%** Exposure
- `greenlet-3.3.2/src/greenlet/TPythonState.cpp` -> **100.0%** Exposure
- `greenlet-3.3.2/src/greenlet/TStackState.cpp` -> **99.9289%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py` -> **70** Orphaned Functions | **6** Duplicates
- `greenlet-3.3.2/src/greenlet/tests/test_leaks.py` -> **16** Orphaned Functions | **0** Duplicates
- `greenlet-3.3.2/src/greenlet/tests/test_extension_interface.py` -> **11** Orphaned Functions | **0** Duplicates
- `greenlet-3.3.2/src/greenlet/tests/test_contextvars.py` -> **10** Orphaned Functions | **0** Duplicates
- `greenlet-3.3.2/src/greenlet/tests/test_tracing.py` -> **10** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

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

### 1. `greenlet-3.3.2/src/greenlet/TPythonState.cpp` (CPP) -> Cumulative Risk: **690.12**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 274.3 | **LOC:** 440 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.1914%)
- **Heaviest Functions:** `PythonState::operator<<` (Impact: 21.7), `PythonState::operator>>` (Impact: 21.5), `PythonState::did_finish` (Impact: 15.3)

### 2. `greenlet-3.3.2/src/greenlet/TStackState.cpp` (CPP) -> Cumulative Risk: **611.77**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 148.88 | **LOC:** 266 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9289%), Safety Score (79.7358%)
- **Heaviest Functions:** `StackState::copy_from_stack` (Impact: 13.7), `StackState::copy_stack_to_heap` (Impact: 13.6), `StackState::copy_heap_to_stack` (Impact: 8.0)

### 3. `greenlet-3.3.2/src/greenlet/TGreenlet.cpp` (CPP) -> Cumulative Risk: **607.58**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 242.56 | **LOC:** 726 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (92.0776%), Documentation (82.9787%), Verification (80.0%)
- **Heaviest Functions:** `Greenlet::on_switchstack_or_initialstub_failure` (Impact: 19.3), `operator<<=` (Impact: 15.3), `Greenlet::check_switch_allowed` (Impact: 13.2)

### 4. `greenlet-3.3.2/benchmarks/chain.py` (PYTHON) -> Cumulative Risk: **596.15**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 191.26 | **LOC:** 252 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.428%)
- **Heaviest Functions:** `_bm_recur_frame` (Impact: 10.5), `bm_switch_deep` (Impact: 10.3), `bm_switch_shallow` (Impact: 5.6)

### 5. `greenlet-3.3.2/src/greenlet/TUserGreenlet.cpp` (CPP) -> Cumulative Risk: **563.6**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 196.9 | **LOC:** 663 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.6714%), Documentation (95.0%), Safety Score (63.8061%)
- **Heaviest Functions:** `UserGreenlet::inner_bootstrap` (Impact: 32.7), `UserGreenlet::g_switch` (Impact: 15.8), `UserGreenlet::g_initialstub` (Impact: 13.0)

### 6. `greenlet-3.3.2/src/greenlet/TExceptionState.cpp` (CPP) -> Cumulative Risk: **557.65**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 44.9 | **LOC:** 63 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (84.7391%)
- **Heaviest Functions:** `ExceptionState::tp_traverse` (Impact: 3.9), `ExceptionState::operator>>` (Impact: 3.2), `ExceptionState::clear` (Impact: 2.5)

### 7. `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp` (CPP) -> Cumulative Risk: **533.9**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 287.72 | **LOC:** 1119 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.1736%), Tech Debt (81.492%), Verification (80.0%)
- **Heaviest Functions:** `normalize` (Impact: 12.9), `GreenletChecker` (Impact: 6.8), `operator=` (Impact: 6.6)

### 8. `greenlet-3.3.2/src/greenlet/platform/switch_x86_msvc.h` (CPP) -> Cumulative Risk: **533.52**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 69.14 | **LOC:** 327 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (96.4916%), Safety Score (85.6832%)
- **Heaviest Functions:** `GreenletVectorHandler` (Impact: 17.0), `x86_slp_get_third_oldest_handler` (Impact: 7.1), `x86_slp_show_seh_chain` (Impact: 6.0)

### 9. `greenlet-3.3.2/src/greenlet/greenlet_cpython_compat.hpp` (CPP) -> Cumulative Risk: **520.21**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 35.88 | **LOC:** 157 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.7728%), Safety Score (77.7373%)
- **Heaviest Functions:** `PyThreadState_LeaveTracing` (Impact: 6.2), `PyThreadState_EnterTracing` (Impact: 4.7)

### 10. `greenlet-3.3.2/src/greenlet/PyGreenlet.cpp` (CPP) -> Cumulative Risk: **513.36**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 206.3 | **LOC:** 796 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (92.0%), Verification (80.0%), State Flux (61.5073%)
- **Heaviest Functions:** `green_repr` (Impact: 20.2), `_green_dealloc_kill_started_non_main_greenlet` (Impact: 18.0), `green_init` (Impact: 13.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `greenlet-3.3.2/src/greenlet/tests/test_greenlet.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 999.08 | **LOC:** 1366 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.5532%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_do_test_throw_to_dead_thread_doesnt_crash` (Impact: 20.1)
  * `test_implicit_parent_with_threads` (Impact: 18.3)
  * `test_two_recursive_children` (Impact: 10.9)
  * `attempt` (Impact: 9.2)
  * `test_issue_245_reference_counting_subclass_threads` (Impact: 9.1)
    * *Intent:* # https://github.com/python-greenlet/greenlet/issues/245 from threading import Thread from threading...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 27 instances
* *Amplified Cascading Flux:* 44 instances
* *Concurrency (weighted view):* 164
* *State Mutation (weighted view):* 326
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 305`, `args: 163`, `func_start: 139`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 238`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 9`, `duplicate_logic: 6`, `unreferenced_by_name: 70`
* *Architecture:* `io: 21`, `api: 136`, `concurrency: 29`, `import: 24`
* *Defense:* `safety: 24`, `test: 82`, `sync_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` , .leakcheck, abc, copy, functools, gc, greenlet, io...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/tests/test_leaks.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 343.52 | **LOC:** 475 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.8562%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_check_untracked_memory_thread` (Impact: 25.0)
  * `_check_issue251` (Impact: 24.2)
  * `test_untracked_memory_doesnt_increase` (Impact: 10.0)
    * *Intent:* # Because we're just trying to track raw memory, not objects, and running # the leakcheck makes an a...
  * `test_kwarg_refs` (Impact: 9.0)
  * `test_threaded_adv_leak` (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 32 instances
* *Concurrency (weighted view):* 43
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 78`, `args: 35`, `func_start: 33`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 60`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 16`
* *Architecture:* `io: 7`, `api: 26`, `concurrency: 8`, `import: 15`
* *Defense:* `safety: 10`, `doc: 1`, `test: 15`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` , .leakcheck, __future__, gc, greenlet, sys, threading, time...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 287.72 | **LOC:** 1119 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.1591%), Tech Debt (81.492%)
**Top Internal Functions/Classes:**
  * `normalize` (Impact: 12.9)
  * `GreenletChecker` (Impact: 6.8)
  * `operator=` (Impact: 6.6)
  * `ContextExactChecker` (Impact: 4.8)
  * `operator=` (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 248`, `args: 110`, `func_start: 99`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 24`, `dead_code: 5`, `planned_debt: 5`, `fragile_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `api: 41`, `import: 6`
* *Defense:* `safety: 36`, `doc: 1`, `immutability_locks: 121`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 33.721
  * `Choke Point (Betweenness):` 0.002075 | `Ripple Effect (Closeness):` 0.148148
  * `Imports (Out-Degree: 3):` Python.h, greenlet_compiler_compat.hpp, greenlet_cpython_compat.hpp, greenlet_exceptions.hpp, iostream, string
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/TPythonState.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 274.3 | **LOC:** 440 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.6497%), Tech Debt (36.837%)
**Top Internal Functions/Classes:**
  * `PythonState::operator<<` (Impact: 21.7)
  * `PythonState::operator>>` (Impact: 21.5)
    * *Intent:* #endif
  * `PythonState::did_finish` (Impact: 15.3)
  * `PythonState::PythonState` (Impact: 12.0)
  * `PythonState::tp_traverse` (Impact: 6.9)
    * *Intent:* // TODO: Better state management about when we own the top frame.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 160
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 18`, `args: 10`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 64`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 2`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `safety: 11`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.672
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011111
  * `Imports (Out-Degree: 1):` Python.h, TGreenlet.hpp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/tests/leakcheck.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 245.44 | **LOC:** 337 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.5609%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_check_deltas` (Impact: 31.8)
    * *Intent:* # Return false when we have decided there is no leak, # true if we should keep looping, raises an as...
  * `_include_object_p` (Impact: 19.4)
    * *Intent:* # pylint:disable=too-many-return-statements # # See the comment block at the top. We must be careful...
  * `__call__` (Impact: 17.3)
  * `wrap_refcount` (Impact: 9.1)
  * `wrapper` (Impact: 8.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 57`, `args: 17`, `func_start: 17`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 44`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 5`, `api: 9`, `import: 7`
* *Defense:* `safety: 7`, `doc: 3`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 32.381
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.044444
  * `Imports (Out-Degree: 0):` __future__, functools, gc, objgraph, os, sys, the, unittest
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/TGreenlet.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 242.56 | **LOC:** 726 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.2616%), Tech Debt (57.899%)
**Top Internal Functions/Classes:**
  * `Greenlet::on_switchstack_or_initialstub_failure` (Impact: 19.3)
    * *Intent:* /** * CAUTION: This will allocate memory and may trigger garbage * collection and arbitrary Python c...
  * `operator<<=` (Impact: 15.3)
    * *Intent:* * CAUTION: May invoke arbitrary Python code. * * Figure out what the result of ``greenlet.switch(arg...
  * `Greenlet::check_switch_allowed` (Impact: 13.2)
  * `Greenlet::g_switch_finish` (Impact: 12.4)
    * *Intent:* /** * May run arbitrary Python code. */
  * `Greenlet::g_switchstack` (Impact: 11.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 46`, `args: 25`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 26`, `dead_code: 5`, `planned_debt: 4`, `fragile_debt: 6`
* *Architecture:* `api: 21`, `import: 4`
* *Defense:* `safety: 34`, `doc: 5`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.397
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.022222
  * `Imports (Out-Degree: 4):` TGreenlet.hpp, TGreenletGlobals.cpp, TThreadStateDestroy.cpp, greenlet_internal.hpp
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/tests/test_contextvars.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 210.18 | **LOC:** 313 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.3036%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_test_context` (Impact: 42.8)
    * *Intent:* # pylint:disable=too-many-branches ID_VAR.set(0) callback = getcurrent().switch counts = dict((i, 0)...
  * `test_context_assignment_while_running` (Impact: 10.7)
    * *Intent:* # pylint:disable=too-many-statements ID_VAR.set(None) def target(): self.assertIsNone(ID_VAR.get()) ...
  * `_increment` (Impact: 10.3)
  * `test_context_assignment_different_thread` (Impact: 4.7)
  * `test_context_assignment_wrong_type` (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 36
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 57`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 48`, `fragile_debt: 1`, `unreferenced_by_name: 10`
* *Architecture:* `io: 2`, `api: 15`, `concurrency: 6`, `import: 15`
* *Defense:* `safety: 3`, `test: 17`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , __future__, contextvars, functools, gc, greenlet, sys, threading...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/PyGreenlet.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 206.3 | **LOC:** 796 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.5228%), Tech Debt (48.107%)
**Top Internal Functions/Classes:**
  * `green_repr` (Impact: 20.2)
  * `_green_dealloc_kill_started_non_main_greenlet` (Impact: 18.0)
    * *Intent:* /** * Returns 0 on failure (the object was resurrected) or 1 on success. **/
  * `green_init` (Impact: 13.3)
    * *Intent:* // green_init is used in the tp_init slot. So it's important that // it can be called directly from ...
  * `green_switch` (Impact: 13.2)
  * `green_dealloc` (Impact: 11.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 72`, `args: 38`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 18`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 7`
* *Architecture:* `import: 12`
* *Defense:* `safety: 25`, `doc: 3`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.672
  * `Choke Point (Betweenness):` 4.2e-05 | `Ripple Effect (Closeness):` 0.011111
  * `Imports (Out-Degree: 8):` PyGreenlet.hpp, Python.h, TGreenlet.hpp, TGreenletGlobals.cpp, TThreadStateDestroy.cpp, greenlet_internal.hpp, greenlet_refs.hpp, greenlet_slp_switch.hpp...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/TUserGreenlet.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 196.9 | **LOC:** 663 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.0593%), Tech Debt (45.2071%)
**Top Internal Functions/Classes:**
  * `UserGreenlet::inner_bootstrap` (Impact: 32.7)
  * `UserGreenlet::g_switch` (Impact: 15.8)
  * `UserGreenlet::g_initialstub` (Impact: 13.0)
  * `UserGreenlet::parent` (Impact: 11.3)
  * `UserGreenlet::find_main_greenlet_in_lineage` (Impact: 3.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 18 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 29`, `args: 14`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 2`, `state_mutation: 28`, `dead_code: 3`, `planned_debt: 5`, `fragile_debt: 3`
* *Architecture:* `api: 19`, `import: 3`
* *Defense:* `safety: 28`, `doc: 2`, `immutability_locks: 19`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.672
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011111
  * `Imports (Out-Degree: 3):` TGreenlet.hpp, TThreadStateDestroy.cpp, greenlet_internal.hpp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/tests/test_generator_nested.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 191.94 | **LOC:** 169 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.0541%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `perms` (Impact: 10.3)
  * `__next__` (Impact: 7.9)
  * `Yield` (Impact: 7.5)
  * `test_genlet_simple` (Impact: 6.0)
    * *Intent:* # XXX Test to make sure we are working as a generator expression
  * `a` (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 35`, `args: 20`, `func_start: 20`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 37`, `fragile_debt: 1`, `unreferenced_by_name: 8`
* *Architecture:* `api: 19`, `import: 3`
* *Defense:* `safety: 4`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` , .leakcheck, greenlet
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/benchmarks/chain.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 191.26 | **LOC:** 252 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.9479%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_bm_recur_frame` (Impact: 10.5)
  * `bm_switch_deep` (Impact: 10.3)
    * *Intent:* # pylint:disable=attribute-defined-outside-init class G(greenlet.greenlet): other = None def run(sel...
  * `bm_switch_shallow` (Impact: 5.6)
    * *Intent:* # pylint:disable=attribute-defined-outside-init class G(greenlet.greenlet): other = None def run(sel...
  * `recur_then_switch` (Impact: 5.4)
  * `bm_chain` (Impact: 4.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 42`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `state_mutation: 49`, `dead_code: 1`
* *Architecture:* `api: 14`, `import: 3`
* *Defense:* `safety: 7`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` greenlet, os, pyperf
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/tests/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 167.0 | **LOC:** 249 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.5845%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `wait_for_pending_cleanups` (Impact: 21.6)
  * `count_objects` (Impact: 14.8)
    * *Intent:* # pylint:disable=unidiomatic-typecheck # Collect the garbage. for _ in range(3): collect() if exact_...
  * `__new__` (Impact: 12.0)
    * *Intent:* # wrap each test method with # a) leak checks # pylint and pep8 fight over what this should be calle...
  * `get_expected_returncodes_for_aborted_process` (Impact: 6.4)
  * `run_script` (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 60`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `state_mutation: 32`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 7`, `api: 12`, `concurrency: 1`, `import: 18`
* *Defense:* `safety: 5`, `doc: 3`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , gc, greenlet, greenlet._greenlet, os, psutil, signal, subprocess...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/TStackState.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 148.88 | **LOC:** 266 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.6359%), Tech Debt (50.3141%)
**Top Internal Functions/Classes:**
  * `StackState::copy_from_stack` (Impact: 13.7)
  * `StackState::copy_stack_to_heap` (Impact: 13.6)
  * `StackState::copy_heap_to_stack` (Impact: 8.0)
  * `StackState::copy_stack_to_heap_up_to` (Impact: 5.6)
  * `StackState::operator=` (Impact: 5.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 41`, `args: 8`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 32`, `fragile_debt: 3`
* *Architecture:* `api: 16`, `import: 2`
* *Defense:* `safety: 15`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.672
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011111
  * `Imports (Out-Degree: 1):` TGreenlet.hpp, iostream
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/TThreadState.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 132.96 | **LOC:** 544 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.8426%), Tech Debt (25.709%)
**Top Internal Functions/Classes:**
  * `~ThreadState` (Impact: 31.4)
  * `clear_deleteme_list` (Impact: 8.7)
    * *Intent:* /** * Deref and remove the greenlets from the deleteme list. Must be * holding the GIL. * * If *murd...
  * `tp_traverse` (Impact: 8.6)
    * *Intent:* // Called from the ThreadStateCreator when we're in non-standard // threading mode. In that case, th...
  * `set_tracefunc` (Impact: 4.7)
  * `set_clocks_used_doing_gc` (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 63`, `args: 16`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 12`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 17`, `import: 6`
* *Defense:* `safety: 18`, `doc: 8`, `immutability_locks: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.069
  * `Choke Point (Betweenness):` 0.000114 | `Ripple Effect (Closeness):` 0.06
  * `Imports (Out-Degree: 3):` atomic, ctime, greenlet_internal.hpp, greenlet_refs.hpp, greenlet_thread_support.hpp, stdexcept
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/tests/test_tracing.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 128.16 | **LOC:** 300 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.3236%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_trace_events_multiple_greenlets_switching_siblings` (Impact: 3.8)
    * *Intent:* # Like the first version, but get both greenlets running first # as "siblings" and then establish th...
  * `__call__` (Impact: 3.7)
  * `test_trace_events_multiple_greenlets_switching` (Impact: 3.2)
  * `_check_trace_events_from_greenlet_sets_profiler` (Impact: 2.7)
  * `test_a_greenlet_tracing` (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 86`, `args: 33`, `func_start: 33`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 32`, `unreferenced_by_name: 10`
* *Architecture:* `io: 2`, `api: 27`, `import: 7`
* *Defense:* `safety: 1`, `doc: 2`, `test: 17`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , __future__, greenlet, sys, sysconfig, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/TGreenlet.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 126.4 | **LOC:** 838 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.8043%), Tech Debt (40.3739%)
**Top Internal Functions/Classes:**
  * `single_result` (Impact: 6.3)
    * *Intent:* //TODO: Greenlet::g_switch() should call this automatically on its //return value. As it is, the mod...
  * `CallTraceFunction` (Impact: 5.9)
  * `run` (Impact: 3.4)
  * `operator<<=` (Impact: 3.3)
    * *Intent:* /** * Moves ownership from the argument to this object. */
  * `switchstack_result_t` (Impact: 2.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 2 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 214`, `args: 69`, `func_start: 42`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 14`, `dead_code: 4`, `planned_debt: 7`, `fragile_debt: 5`
* *Architecture:* `api: 22`, `import: 5`
* *Defense:* `safety: 52`, `doc: 8`, `immutability_locks: 114`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 52.958
  * `Choke Point (Betweenness):` 0.006538 | `Ripple Effect (Closeness):` 0.14596
  * `Imports (Out-Degree: 5):` Python.h, greenlet_allocator.hpp, greenlet_compiler_compat.hpp, greenlet_cpython_compat.hpp, greenlet_msvc_compat.hpp, greenlet_refs.hpp, pycore_frame.h, pycore_interpframe.h...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/tests/_test_extension.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 91.92 | **LOC:** 259 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.8%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_switch_kwargs` (Impact: 15.2)
  * `test_switch` (Impact: 13.2)
    * *Intent:* // // In C23, there is a standard syntax for attributes, and // GCC defines an attribute to use with...
  * `test_setparent` (Impact: 11.6)
  * `test_getcurrent` (Impact: 6.3)
  * `test_new_greenlet` (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 26`, `args: 18`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` greenlet.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/tests/test_greenlet_trash.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 84.46 | **LOC:** 188 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.7598%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `check_it` (Impact: 16.6)
  * `__del__` (Impact: 9.9)
  * `test_it` (Impact: 3.5)
  * `make_some` (Impact: 2.5)
  * `__init__` (Impact: 2.1)
    * *Intent:* """ :param sequence_number: The ordinal of this object during one particular creation run. This is u...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 28`, `args: 6`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `state_mutation: 23`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `io: 1`, `api: 6`, `import: 7`
* *Defense:* `safety: 7`, `doc: 3`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, gc, greenlet, greenlet._greenlet, sys, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/tests/_test_extension_cpp.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 83.1 | **LOC:** 230 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.422%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_exception_switch_and_do_in_g2` (Impact: 14.1)
    * *Intent:* /* test_exception_switch_and_do_in_g2(g2func) * - creates new greenlet g2 to run g2func * - switches...
  * `test_exception_switch_recurse` (Impact: 12.1)
  * `PyInit__test_extension_cpp` (Impact: 4.2)
  * `test_exception_switch` (Impact: 3.9)
    * *Intent:* /* test_exception_switch(int depth) * - recurses depth times * - switches to parent inside try/catch...
  * `py_test_exception_throw_nonstd` (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 30`, `args: 17`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 13`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `import: 4`
* *Defense:* `safety: 7`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` greenlet.h, greenlet_compiler_compat.hpp, exception, stdexcept
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/tests/test_throw.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 72.48 | **LOC:** 129 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.3741%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_val` (Impact: 3.9)
  * `test_throw_goes_to_original_parent` (Impact: 3.4)
  * `test_not_throwable` (Impact: 3.2)
  * `f` (Impact: 2.5)
  * `test_class` (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 33`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 26`, `unreferenced_by_name: 7`
* *Architecture:* `io: 1`, `api: 11`, `import: 3`
* *Defense:* `safety: 8`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , greenlet, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/platform/switch_x86_msvc.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 69.14 | **LOC:** 327 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.4741%), Tech Debt (24.242%)
**Top Internal Functions/Classes:**
  * `GreenletVectorHandler` (Impact: 17.0)
    * *Intent:* //addVectoredExceptionHandler constants: //CALL_FIRST means call this exception handler first; //CAL...
  * `x86_slp_get_third_oldest_handler` (Impact: 7.1)
  * `x86_slp_show_seh_chain` (Impact: 6.0)
  * `IS_ON_STACK` (Impact: 3.1)
    * *Intent:* #endif /* * further self-processing support */ /* we have IsBadReadPtr available, so we can peek at ...
  * `slp_switch` (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 21`, `args: 12`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 8`, `fragile_debt: 1`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.712
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.023148
  * `Imports (Out-Degree: 0):` windows.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/setup.py` (PYTHON | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 65.24 | **LOC:** 202 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.4925%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_find_platform_headers` (Impact: 1.1)
  * `_find_impl_headers` (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 17`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 31`, `dead_code: 2`
* *Architecture:* `io: 8`, `import: 8`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, glob, os, platform, setuptools, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/tests/test_generator.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 62.74 | **LOC:** 60 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.8874%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_generator` (Impact: 6.3)
  * `Yield` (Impact: 4.6)
  * `__next__` (Impact: 3.2)
  * `g` (Impact: 3.0)
  * `__init__` (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 18`, `args: 8`, `func_start: 8`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 13`, `unreferenced_by_name: 4`
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `safety: 1`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , greenlet
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `greenlet-3.3.2/src/greenlet/CObjects.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 58.26 | **LOC:** 158 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.7531%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `PyGreenlet_Switch` (Impact: 10.9)
  * `PyGreenlet_New` (Impact: 8.4)
  * `PyGreenlet_Throw` (Impact: 5.2)
  * `Extern_PyGreenlet_MAIN` (Impact: 3.3)
  * `Extern_PyGreenlet_ACTIVE` (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 22`, `args: 9`, `func_start: 9`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 9`, `import: 5`
* *Defense:* `safety: 4`, `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.672
  * `Choke Point (Betweenness):` 7.3e-05 | `Ripple Effect (Closeness):` 0.011111
  * `Imports (Out-Degree: 5):` PyGreenlet.hpp, TThreadStateDestroy.cpp, greenlet_exceptions.hpp, greenlet_internal.hpp, greenlet_refs.hpp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `greenlet-3.3.2/src/greenlet/PyModule.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 53.42 | **LOC:** 293 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.2064%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mod_enable_optional_cleanup` (Impact: 9.7)
  * `mod_set_thread_local` (Impact: 6.1)
  * `mod_settrace` (Impact: 6.0)
  * `mod_get_tstate_trash_delete_nesting` (Impact: 5.7)
  * `mod_get_clocks_used_doing_optional_cleanup` (Impact: 4.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 26`, `args: 15`, `func_start: 9`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `import: 4`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.672
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011111
  * `Imports (Out-Degree: 4):` TGreenletGlobals.cpp, TMainGreenlet.cpp, TThreadStateDestroy.cpp, greenlet_internal.hpp
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `greenlet-3.3.2/src/greenlet/greenlet_slp_switch.hpp` -> **Severity: 0.849** (Bridge: 0.0094 * Flux: 90.1623%)
- `greenlet-3.3.2/src/greenlet/greenlet_internal.hpp` -> **Severity: 0.317** (Bridge: 0.0046 * Flux: 69.5467%)
- `greenlet-3.3.2/src/greenlet/TThreadStateDestroy.cpp` -> **Severity: 0.025** (Bridge: 0.0026 * Flux: 9.8428%)
- `greenlet-3.3.2/src/greenlet/TThreadStateCreator.hpp` -> **Severity: 0.007** (Bridge: 0.0001 * Flux: 60.1687%)
- `greenlet-3.3.2/src/greenlet/TThreadState.hpp` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 56.5096%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `greenlet-3.3.2/src/greenlet/greenlet_cpython_compat.hpp` -> **Severity: 11.144** (Embedded: 0.1434 * Error Risk: 77.7373%)
- `greenlet-3.3.2/src/greenlet/greenlet_allocator.hpp` -> **Severity: 8.882** (Embedded: 0.1059 * Error Risk: 83.8891%)
- `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp` -> **Severity: 7.457** (Embedded: 0.1481 * Error Risk: 50.3329%)
- `greenlet-3.3.2/src/greenlet/greenlet_internal.hpp` -> **Severity: 7.308** (Embedded: 0.112 * Error Risk: 65.2324%)
- `greenlet-3.3.2/src/greenlet/greenlet.h` -> **Severity: 6.501** (Embedded: 0.0926 * Error Risk: 70.2063%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `greenlet-3.3.2/src/greenlet/greenlet_cpython_compat.hpp` -> **Severity: 5178.3** (Blast Radius: 51.783 * Doc Risk: 100.0%)
- `greenlet-3.3.2/src/greenlet/TGreenlet.hpp` -> **Severity: 4978.052** (Blast Radius: 52.958 * Doc Risk: 94.0%)
- `greenlet-3.3.2/src/greenlet/greenlet_refs.hpp` -> **Severity: 3344.233** (Blast Radius: 33.721 * Doc Risk: 99.1736%)
- `greenlet-3.3.2/src/greenlet/tests/leakcheck.py` -> **Severity: 2698.416** (Blast Radius: 32.381 * Doc Risk: 83.3333%)
- `greenlet-3.3.2/src/greenlet/greenlet_internal.hpp` -> **Severity: 2480.7** (Blast Radius: 24.807 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
