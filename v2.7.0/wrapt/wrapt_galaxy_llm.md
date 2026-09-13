# ARCHITECTURAL_BRIEF: wrapt
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
| Total Artifacts | 120 |
| Analyzed Artifacts (Scanned) | 82 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 38 |
| Total LOC | 11562 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 68.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3764 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.303 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.4396 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 79 | 8584 | 96.3% |
| PLAINTEXT | 1 | 0 | 1.2% |
| MARKDOWN | 1 | 0 | 1.2% |
| C | 1 | 2978 | 1.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 80 | 97.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 2.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 38*

**Composition by Extension & Reason:**
- `.out`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 82.5 | 16.0 | 3.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 74.4 | 80.8 | 87.4 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.2 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 11.4 | 8.8 | 5.6 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 6.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 13.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 76.4 | 2.8 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 92.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 73.7 | 90.3 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1040 | 18 | 2 | `wrapt-2.1.2/src/wrapt/_wrappers.c` |
| cleanup | 2 | 2 | 0 | `wrapt-2.1.2/tests/core/test_object_proxy.py` |
| guards | 877 | 42 | 24 | `wrapt-2.1.2/tests/core/test_object_proxy.py` |
| danger | 787 | 67 | 18 | `wrapt-2.1.2/src/wrapt/_wrappers.c` |
| concurrency | 43 | 12 | 1 | `wrapt-2.1.2/tests/core/test_auto_object_proxy.py` |
| connectivity | 1510 | 75 | 37 | `wrapt-2.1.2/tests/core/test_object_proxy.py` |
| io | 49 | 15 | 1 | `wrapt-2.1.2/tests/core/test_lazy_object_proxy.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 4 | 1 | 0 | `wrapt-2.1.2/tests/conftest.py` |
| time | 2 | 2 | 0 | `wrapt-2.1.2/tests/core/module1.py` |
| serialization | 1 | 1 | 0 | `wrapt-2.1.2/tests/core/test_pickle.py` |
| regex | 26 | 2 | 0 | `wrapt-2.1.2/tests/core/test_object_proxy.py` |
| events | 57 | 8 | 0 | `wrapt-2.1.2/src/wrapt/_wrappers.c` |
| tests | 782 | 34 | 20 | `wrapt-2.1.2/tests/core/test_object_proxy.py` |
| docs | 163 | 56 | 5 | `wrapt-2.1.2/tests/core/test_entry_points.py` |
| debt | 434 | 33 | 17 | `wrapt-2.1.2/tests/core/test_object_proxy.py` |
| mutation | 3766 | 77 | 81 | `wrapt-2.1.2/tests/core/test_object_proxy.py` |
| dead_code | 574 | 50 | 14 | `wrapt-2.1.2/tests/core/test_object_proxy.py` |
| credential | 0 | 0 | 0 | - |
| threat | 446 | 37 | 15 | `wrapt-2.1.2/tests/core/test_object_proxy.py` |
| ml_ai | 3 | 1 | 0 | `wrapt-2.1.2/src/wrapt/wrappers.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0273**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `wrapt-2.1.2/tests/core/test_lazy_object_proxy.py` (Hits: 16)
- `wrapt-2.1.2/tests/conftest.py` (Hits: 10)
- `wrapt-2.1.2/tests/core/test_post_import_hooks.py` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__wrapt__.py** (`wrapt-2.1.2/src/wrapt/__wrapt__.py`) — 6 inbound connections
2. **importer.py** (`wrapt-2.1.2/src/wrapt/importer.py`) — 3 inbound connections
3. **arguments.py** (`wrapt-2.1.2/src/wrapt/arguments.py`) — 3 inbound connections
4. **decorators.py** (`wrapt-2.1.2/src/wrapt/decorators.py`) — 2 inbound connections
5. **compat.py** (`wrapt-2.1.2/tests/core/compat.py`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **README.md** (`wrapt-2.1.2/README.md`) — 16 outbound dependencies
2. **importer.py** (`wrapt-2.1.2/src/wrapt/importer.py`) — 16 outbound dependencies
3. **test_post_import_hooks.py** (`wrapt-2.1.2/tests/core/test_post_import_hooks.py`) — 12 outbound dependencies
4. **conftest.py** (`wrapt-2.1.2/tests/conftest.py`) — 9 outbound dependencies
5. **test_entry_points.py** (`wrapt-2.1.2/tests/core/test_entry_points.py`) — 8 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `WraptFunctionWrapperBase_descr_get` (@ `wrapt-2.1.2/src/wrapt/_wrappers.c`) -> Impact: **65.2** | LOC: 145
  * *Intent:* /* ------------------------------------------------------------------------- */
- `decorator` (@ `wrapt-2.1.2/src/wrapt/decorators.py`) -> Impact: **62.2** | LOC: 261
  * *Intent:* # Decorator for creating other decorators. This decorator and the # wrappers which they use are designed to properly preserve any name # attributes, f...
- `WraptBoundFunctionWrapper_call` (@ `wrapt-2.1.2/src/wrapt/_wrappers.c`) -> Impact: **60.1** | LOC: 203
  * *Intent:* /* ------------------------------------------------------------------------- */
- `WraptFunctionWrapper_init` (@ `wrapt-2.1.2/src/wrapt/_wrappers.c`) -> Impact: **59.9** | LOC: 118
  * *Intent:* /* ------------------------------------------------------------------------- */
- `__wrapped_setattr_fixups__` (@ `wrapt-2.1.2/src/wrapt/proxies.py`) -> Impact: **51.7** | LOC: 73
  * *Intent:* """Adjusts special dunder methods on the class as needed based on the wrapped object, when `__wrapped__` is changed. """
- `__new__` (@ `wrapt-2.1.2/src/wrapt/proxies.py`) -> Impact: **50.8** | LOC: 56
  * *Intent:* """Injects special dunder methods into a dynamically created subclass as needed based on the wrapped object. """
- `formatargspec` (@ `wrapt-2.1.2/src/wrapt/arguments.py`) -> Impact: **47.1** | LOC: 44
- `WraptFunctionWrapperBase_call` (@ `wrapt-2.1.2/src/wrapt/_wrappers.c`) -> Impact: **44.5** | LOC: 91
  * *Intent:* /* ------------------------------------------------------------------------- */
- `__new__` (@ `wrapt-2.1.2/src/wrapt/proxies.py`) -> Impact: **44.2** | LOC: 53
  * *Intent:* """Injects special dunder methods into a dynamically created subclass as needed based on the wrapped object. """
- `_wrapper` (@ `wrapt-2.1.2/src/wrapt/decorators.py`) -> Impact: **39.7** | LOC: 167
  * *Intent:* # The wrapper has been provided so return the final decorator. # The decorator is itself one of our function wrappers so we # can determine when it is...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `wrapt-2.1.2/tests/core` | 36 | 5304.02 | 19.72% | 0.0% |
| `wrapt-2.1.2/src/wrapt` | 11 | 3934.54 | 44.54% | 17.85% |
| `wrapt-2.1.2/tests/mypy` | 31 | 569.18 | 0.43% | 0.0% |
| `wrapt-2.1.2/tests` | 1 | 127.36 | 27.04% | 0.0% |
| `wrapt-2.1.2` | 3 | 43.28 | 14.41% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `wrapt-2.1.2/src/wrapt/__init__.pyi` -> **99.9898%** Exposure
- `wrapt-2.1.2/src/wrapt/wrappers.py` -> **48.362%** Exposure
- `wrapt-2.1.2/src/wrapt/patches.py` -> **20.365%** Exposure
- `wrapt-2.1.2/src/wrapt/importer.py` -> **14.9005%** Exposure
- `wrapt-2.1.2/src/wrapt/decorators.py` -> **12.6909%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `wrapt-2.1.2/setup.py` -> **100.0%** Exposure
- `wrapt-2.1.2/src/wrapt/decorators.py` -> **100.0%** Exposure
- `wrapt-2.1.2/src/wrapt/importer.py` -> **100.0%** Exposure
- `wrapt-2.1.2/src/wrapt/arguments.py` -> **100.0%** Exposure
- `wrapt-2.1.2/src/wrapt/patches.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `wrapt-2.1.2/tests/core/test_object_proxy.py` -> **161** Orphaned Functions | **88** Duplicates
- `wrapt-2.1.2/tests/core/test_function_wrapper.py` -> **30** Orphaned Functions | **50** Duplicates
- `wrapt-2.1.2/tests/core/test_inplace_operators.py` -> **67** Orphaned Functions | **2** Duplicates
- `wrapt-2.1.2/tests/core/test_monkey_patching.py` -> **20** Orphaned Functions | **23** Duplicates
- `wrapt-2.1.2/tests/core/test_inner_classmethod.py` -> **20** Orphaned Functions | **22** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `270` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `wrapt-2.1.2/src/wrapt/__init__.pyi` (PYTHON) -> Cumulative Risk: **705.89**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 182.82 | **LOC:** 389 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9898%)
- **Heaviest Functions:** `wrap_object` (Impact: 2.8), `wrap_object_attribute` (Impact: 2.8), `__init__` (Impact: 2.5)

### 2. `wrapt-2.1.2/src/wrapt/decorators.py` (PYTHON) -> Cumulative Risk: **701.5**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 293.3 | **LOC:** 523 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (91.2995%), Documentation (88.8889%)
- **Heaviest Functions:** `decorator` (Impact: 62.2), `_wrapper` (Impact: 39.7), `_build` (Impact: 17.6)

### 3. `wrapt-2.1.2/src/wrapt/wrappers.py` (PYTHON) -> Cumulative Risk: **691.19**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 604.98 | **LOC:** 985 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.8067%), Documentation (94.4882%), Cognitive Load (80.5581%)
- **Heaviest Functions:** `__init__` (Impact: 34.9), `__call__` (Impact: 26.0), `__setattr__` (Impact: 18.2)

### 4. `wrapt-2.1.2/src/wrapt/importer.py` (PYTHON) -> Cumulative Risk: **613.32**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 195.74 | **LOC:** 333 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.4909%), Documentation (79.5455%)
- **Heaviest Functions:** `find_spec` (Impact: 13.2), `find_module` (Impact: 11.9), `register_post_import_hook` (Impact: 10.8)

### 5. `wrapt-2.1.2/src/wrapt/patches.py` (PYTHON) -> Cumulative Risk: **601.63**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 166.16 | **LOC:** 240 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.0414%), Verification (80.0%)
- **Heaviest Functions:** `resolve_path` (Impact: 16.4), `lookup_attribute` (Impact: 10.8), `_wrapper` (Impact: 9.9)

### 6. `wrapt-2.1.2/src/wrapt/proxies.py` (PYTHON) -> Cumulative Risk: **581.56**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 368.14 | **LOC:** 352 | **CtrlFlow:** 46.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.4841%), Verification (80.0%)
- **Heaviest Functions:** `__wrapped_setattr_fixups__` (Impact: 51.7), `__new__` (Impact: 50.8), `__new__` (Impact: 44.2)

### 7. `wrapt-2.1.2/src/wrapt/_wrappers.c` (C) -> Cumulative Risk: **565.4**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1959.66 | **LOC:** 4098 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.8292%), Safety Score (90.4607%)
- **Heaviest Functions:** `WraptFunctionWrapperBase_descr_get` (Impact: 65.2), `WraptBoundFunctionWrapper_call` (Impact: 60.1), `WraptFunctionWrapper_init` (Impact: 59.9)

### 8. `wrapt-2.1.2/src/wrapt/arguments.py` (PYTHON) -> Cumulative Risk: **530.98**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 73.1 | **LOC:** 60 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.7311%)
- **Heaviest Functions:** `formatargspec` (Impact: 47.1)

### 9. `wrapt-2.1.2/tests/core/test_post_import_hooks.py` (PYTHON) -> Cumulative Risk: **476.22**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 108.84 | **LOC:** 183 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9888%), Safety Score (84.3145%)
- **Heaviest Functions:** `test_import_deadlock_3` (Impact: 2.9), `test_before_and_after_import` (Impact: 2.6), `test_import_deadlock_1` (Impact: 2.5)

### 10. `wrapt-2.1.2/src/wrapt/weakrefs.py` (PYTHON) -> Cumulative Risk: **467.25**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 59.92 | **LOC:** 122 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (85.3924%), Documentation (71.4286%)
- **Heaviest Functions:** `__init__` (Impact: 12.8), `__call__` (Impact: 11.8), `_weak_function_proxy_callback` (Impact: 6.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `wrapt-2.1.2/src/wrapt/_wrappers.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1959.66 | **LOC:** 4098 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.1195%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `WraptFunctionWrapperBase_descr_get` (Impact: 65.2)
    * *Intent:* /* ------------------------------------------------------------------------- */
  * `WraptBoundFunctionWrapper_call` (Impact: 60.1)
    * *Intent:* /* ------------------------------------------------------------------------- */
  * `WraptFunctionWrapper_init` (Impact: 59.9)
    * *Intent:* /* ------------------------------------------------------------------------- */
  * `WraptFunctionWrapperBase_call` (Impact: 44.5)
    * *Intent:* /* ------------------------------------------------------------------------- */
  * `WraptObjectProxy_raw_init` (Impact: 30.1)
    * *Intent:* /* ------------------------------------------------------------------------- */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 216 instances
* *State Mutation (weighted view):* 655
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 494`, `structural_boundaries: 366`, `args: 149`, `func_start: 114`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 155`, `state_mutation: 223`, `dead_code: 9`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 38.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.052632
  * `Imports (Out-Degree: 0):` Python.h, structmember.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wrapt-2.1.2/tests/core/test_object_proxy.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1617.96 | **LOC:** 2694 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.5475%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_self_keyword_argument_on_class_init_overloaded_2a` (Impact: 8.6)
  * `test_self_keyword_argument_on_class_init_overloaded_2b` (Impact: 8.6)
  * `test_self_keyword_argument_on_class_init_1` (Impact: 8.6)
  * `test_self_keyword_argument_on_class_init_2` (Impact: 8.6)
  * `test_self_keyword_argument_on_class_init_overloaded_2` (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 18 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 22
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 536
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 613`, `args: 295`, `func_start: 295`, `class_start: 98`
* *Risk/State:* `safety_bypasses: 64`, `high_risk_execution: 1`, `state_mutation: 500`, `dead_code: 1`, `duplicate_logic: 88`, `unreferenced_by_name: 161`
* *Architecture:* `io: 1`, `api: 356`, `concurrency: 7`, `import: 8`
* *Defense:* `safety: 153`, `doc: 1`, `test: 236`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.967
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` asyncio, decimal, fractions, re, sys, types, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/src/wrapt/wrappers.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 604.98 | **LOC:** 985 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.5581%), Tech Debt (48.362%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 34.9)
    * *Intent:* """ Initialize the `FunctionWrapper` with the `wrapped` callable, the `wrapper` function, and an opt...
  * `__call__` (Impact: 26.0)
  * `__setattr__` (Impact: 18.2)
  * `__get__` (Impact: 17.8)
    * *Intent:* # This method is actually doing double duty for both unbound and bound # derived wrapper classes. It...
  * `__call__` (Impact: 15.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 280`, `args: 118`, `func_start: 118`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 41`, `dead_code: 5`, `duplicate_logic: 5`
* *Architecture:* `api: 100`, `import: 3`
* *Defense:* `safety: 43`, `doc: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 38.246
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.052632
  * `Imports (Out-Degree: 0):` inspect, operator, sys
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wrapt-2.1.2/tests/core/test_inplace_operators.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 384.0 | **LOC:** 825 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.4341%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_inplace_matmul` (Impact: 4.3)
  * `test_inplace_matmul_immutable` (Impact: 4.3)
  * `__eq__` (Impact: 3.7)
  * `__eq__` (Impact: 3.7)
  * `test_inplace_add_integer` (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 148
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 159`, `args: 75`, `func_start: 75`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 138`, `duplicate_logic: 2`, `unreferenced_by_name: 67`
* *Architecture:* `api: 71`, `import: 2`
* *Defense:* `safety: 2`, `test: 68`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.967
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/src/wrapt/proxies.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 368.14 | **LOC:** 352 | **CtrlFlow:** 46.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.9901%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__wrapped_setattr_fixups__` (Impact: 51.7)
    * *Intent:* """Adjusts special dunder methods on the class as needed based on the wrapped object, when `__wrappe...
  * `__new__` (Impact: 50.8)
    * *Intent:* """Injects special dunder methods into a dynamically created subclass as needed based on the wrapped...
  * `__new__` (Impact: 44.2)
    * *Intent:* """Injects special dunder methods into a dynamically created subclass as needed based on the wrapped...
  * `lazy_import` (Impact: 13.2)
    * *Intent:* """Lazily imports the module `name`, returning a `LazyObjectProxy` which will import the module when...
  * `__init__` (Impact: 4.5)
    * *Intent:* """Initialize the object proxy with wrapped object as `None` but due to presence of special `__wrapp...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 156
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 65`, `args: 23`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 52`, `dead_code: 1`
* *Architecture:* `api: 8`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 10`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.379
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012346
  * `Imports (Out-Degree: 2):` .__wrapt__, .decorators, collections.abc, the, types
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wrapt-2.1.2/tests/core/test_function_wrapper.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 356.96 | **LOC:** 599 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.2845%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_boolean_dynamic_guard_on_decorator` (Impact: 3.1)
  * `test_guard_on_instancemethod` (Impact: 3.1)
  * `test_re_bind_after_none` (Impact: 3.1)
  * `test_double_binding` (Impact: 3.0)
  * `test_function_guard_on_decorator` (Impact: 2.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 192`, `args: 92`, `func_start: 92`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 58`, `duplicate_logic: 50`, `unreferenced_by_name: 30`
* *Architecture:* `api: 102`, `import: 2`
* *Defense:* `safety: 21`, `test: 48`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.967
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_monkey_patching.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 339.62 | **LOC:** 572 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.0986%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_patch_function_module_name_enabled_callable` (Impact: 3.1)
  * `test_transient_function_wrapper_instance_method` (Impact: 2.9)
  * `test_function_wrapper_instance_method` (Impact: 2.8)
  * `__call__` (Impact: 2.8)
  * `__call__` (Impact: 2.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 122`, `args: 61`, `func_start: 61`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 118`, `duplicate_logic: 23`, `unreferenced_by_name: 20`
* *Architecture:* `io: 2`, `api: 71`, `import: 3`
* *Defense:* `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.967
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/src/wrapt/decorators.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 293.3 | **LOC:** 523 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.4608%), Tech Debt (12.6909%)
**Top Internal Functions/Classes:**
  * `decorator` (Impact: 62.2)
    * *Intent:* # Decorator for creating other decorators. This decorator and the # wrappers which they use are desi...
  * `_wrapper` (Impact: 39.7)
    * *Intent:* # The wrapper has been provided so return the final decorator. # The decorator is itself one of our ...
  * `_build` (Impact: 17.6)
    * *Intent:* # Helper function for creating wrapper of the appropriate # time when we need it down below.
  * `synchronized` (Impact: 15.1)
    * *Intent:* # Decorator for implementing thread synchronization. It can be used as a # decorator, in which case ...
  * `_synchronized_wrapper` (Impact: 7.1)
    * *Intent:* # Execute the wrapped function while the lock for the # desired context is held. If instance is None...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 21 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 94`, `args: 33`, `func_start: 33`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 33`, `dead_code: 22`, `planned_debt: 1`
* *Architecture:* `api: 11`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 4`, `doc: 3`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.214
  * `Choke Point (Betweenness):` 0.000309 | `Ripple Effect (Closeness):` 0.024691
  * `Imports (Out-Degree: 2):` .__wrapt__, .arguments, functools, inspect, sys, threading
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `wrapt-2.1.2/tests/core/test_instancemethod.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 242.16 | **LOC:** 459 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.9625%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_class_object_qualname` (Impact: 3.3)
    * *Intent:* # Test preservation of instance method __qualname__ attribute. try: __qualname__ = OldClass1o.origin...
  * `test_instance_object_qualname` (Impact: 3.3)
    * *Intent:* # Test preservation of instance method __qualname__ attribute. try: __qualname__ = OldClass1o().orig...
  * `test_class_object_qualname` (Impact: 3.3)
    * *Intent:* # Test preservation of instance method __qualname__ attribute. try: __qualname__ = NewClass1o.origin...
  * `test_instance_object_qualname` (Impact: 3.3)
    * *Intent:* # Test preservation of instance method __qualname__ attribute. try: __qualname__ = NewClass1o().orig...
  * `test_class_call_function_nested` (Impact: 2.9)
    * *Intent:* # Test calling instancemethod via class and passing in the class # instance directly. _args = (1, 2)...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 117`, `args: 61`, `func_start: 61`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 44`, `duplicate_logic: 32`, `unreferenced_by_name: 1`
* *Architecture:* `api: 53`, `import: 4`
* *Defense:* `safety: 12`, `doc: 5`, `test: 43`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.967
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inspect, types, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/src/wrapt/importer.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 195.74 | **LOC:** 333 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.7195%), Tech Debt (14.9005%)
**Top Internal Functions/Classes:**
  * `find_spec` (Impact: 13.2)
    * *Intent:* # Since Python 3.4, you are meant to implement find_spec() method # instead of find_module() and sin...
  * `find_module` (Impact: 11.9)
    * *Intent:* # If the module being imported is not one we have registered # post import hooks for, we can return ...
  * `register_post_import_hook` (Impact: 10.8)
    * *Intent:* """ Register a post import hook for the target module `name`. The `hook` function will be called onc...
  * `_self_set_loader` (Impact: 8.2)
    * *Intent:* # Set module's loader to self.__wrapped__ unless it's already set to # something else. Import machin...
  * `__init__` (Impact: 7.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 26 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 85
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 55`, `args: 18`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 33`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `io: 5`, `api: 13`, `concurrency: 2`, `import: 8`
* *Defense:* `safety: 14`, `doc: 5`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.321
  * `Choke Point (Betweenness):` 0.000926 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 1):` .__wrapt__, finder., hook, hook., hooks, hooks., importlib.metadata, importlib.util...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `wrapt-2.1.2/tests/core/test_decorators.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 189.28 | **LOC:** 344 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.7738%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_call_semantics_for_assorted_decorator_use_cases` (Impact: 4.6)
  * `test_decorated_function_as_instance_attribute` (Impact: 3.5)
  * `test_decorated_function_as_class_attribute` (Impact: 3.4)
  * `test_call_semantics_for_assorted_wrapped_descriptor_use_cases` (Impact: 3.3)
  * `test_decorated_builtin_as_class_attribute` (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 89`, `args: 41`, `func_start: 41`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 55`, `duplicate_logic: 17`, `unreferenced_by_name: 10`
* *Architecture:* `api: 36`, `import: 3`
* *Defense:* `safety: 1`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.967
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` operator, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/src/wrapt/__init__.pyi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 182.82 | **LOC:** 389 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.1736%), Tech Debt (99.9898%)
**Top Internal Functions/Classes:**
  * `wrap_object` (Impact: 2.8)
  * `wrap_object_attribute` (Impact: 2.8)
    * *Intent:* # wrap_object_attribute()
  * `__init__` (Impact: 2.5)
  * `__exit__` (Impact: 2.5)
  * `__init__` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 113`, `args: 60`, `func_start: 60`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 88`, `state_mutation: 15`, `dead_code: 1`, `duplicate_logic: 12`
* *Architecture:* `io: 1`, `api: 47`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.967
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inspect, sys, types, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_inner_classmethod.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 171.18 | **LOC:** 331 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.9179%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_class_object_qualname` (Impact: 3.3)
    * *Intent:* # Test preservation of instance method __qualname__ attribute. try: __qualname__ = Original.original...
  * `test_instance_object_qualname` (Impact: 3.3)
    * *Intent:* # Test preservation of instance method __qualname__ attribute. try: __qualname__ = Original().origin...
  * `test_class_call_function_nested_decorators` (Impact: 2.8)
    * *Intent:* # Test calling classmethod. _args = (1, 2) _kwargs = {"one": 1, "two": 2} @wrapt.decorator def _deco...
  * `test_instance_call_function_nested_decorators` (Impact: 2.8)
    * *Intent:* # Test calling classmethod via class instance. _args = (1, 2) _kwargs = {"one": 1, "two": 2} @wrapt....
  * `test_class_call_function` (Impact: 2.7)
    * *Intent:* # Test calling classmethod. _args = (1, 2) _kwargs = {"one": 1, "two": 2} @wrapt.decorator def _deco...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 84`, `args: 42`, `func_start: 42`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 35`, `duplicate_logic: 22`, `unreferenced_by_name: 20`
* *Architecture:* `api: 34`, `import: 4`
* *Defense:* `safety: 6`, `doc: 3`, `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.967
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inspect, types, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/src/wrapt/patches.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 166.16 | **LOC:** 240 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.5977%), Tech Debt (20.365%)
**Top Internal Functions/Classes:**
  * `resolve_path` (Impact: 16.4)
    * *Intent:* # Helper functions for applying wrappers to existing functions. """ Resolves the dotted path supplie...
  * `lookup_attribute` (Impact: 10.8)
    * *Intent:* # We can't just always use getattr() because in doing # that on a class it will cause binding to occ...
  * `_wrapper` (Impact: 9.9)
  * `_wrapper` (Impact: 9.4)
  * `transient_function_wrapper` (Impact: 8.6)
    * *Intent:* """Creates a decorator that patches a target function with a wrapper function, but only for the dura...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 42`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 25`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 13`, `import: 4`
* *Defense:* `safety: 3`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.379
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012346
  * `Imports (Out-Degree: 1):` .__wrapt__, inspect, sys
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wrapt-2.1.2/tests/core/test_synchronized_lock.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 151.06 | **LOC:** 311 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.9853%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_synchronized_outer_classmethod` (Impact: 14.7)
    * *Intent:* # Prior to Python 3.9 this isn't detected as a class method # call, as the classmethod decorator doe...
  * `test_synchronized_instancemethod` (Impact: 4.6)
  * `test_synchronized_inner_classmethod` (Impact: 4.0)
  * `test_synchronized_type_new_style` (Impact: 4.0)
  * `test_synchronized_type_old_style` (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 35`, `args: 17`, `func_start: 17`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 50`, `dead_code: 2`, `duplicate_logic: 6`, `unreferenced_by_name: 9`
* *Architecture:* `api: 22`, `import: 3`
* *Defense:* `safety: 4`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.967
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` compat, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_entry_points.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 148.22 | **LOC:** 252 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.6984%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_threading_safety_with_entry_points` (Impact: 5.9)
    * *Intent:* """Test that entry point discovery is thread-safe"""
  * `test_entry_point_hook_exception_handling` (Impact: 3.7)
    * *Intent:* """Test that exceptions in entry point hooks are properly propagated"""
  * `test_entry_point_load_failure` (Impact: 3.5)
    * *Intent:* """Test handling of entry point load failures"""
  * `setup_method` (Impact: 3.1)
    * *Intent:* """Clean up modules and hooks before each test"""
  * `test_discover_post_import_hooks_python38_style` (Impact: 3.1)
    * *Intent:* """Test entry point discovery using Python 3.8-3.9 style entry_points()"""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 75`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 58`, `unreferenced_by_name: 10`
* *Architecture:* `io: 1`, `api: 21`, `concurrency: 2`, `import: 14`
* *Defense:* `safety: 15`, `doc: 10`, `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.967
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` importlib.metadata, pytest, sys, this, threading, unittest.mock, wrapt, wrapt.importer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_inner_staticmethod.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 141.54 | **LOC:** 279 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.6883%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_class_object_qualname` (Impact: 3.3)
    * *Intent:* # Test preservation of instance method __qualname__ attribute. try: __qualname__ = Original.original...
  * `test_instance_object_qualname` (Impact: 3.3)
    * *Intent:* # Test preservation of instance method __qualname__ attribute. try: __qualname__ = Original().origin...
  * `test_class_call_function_nested_decorator` (Impact: 2.8)
    * *Intent:* # Test calling staticmethod. _args = (1, 2) _kwargs = {"one": 1, "two": 2} @wrapt.decorator def _dec...
  * `test_instance_call_function_nested_decorator` (Impact: 2.8)
    * *Intent:* # Test calling staticmethod via class instance. _args = (1, 2) _kwargs = {"one": 1, "two": 2} @wrapt...
  * `test_class_call_function` (Impact: 2.7)
    * *Intent:* # Test calling staticmethod. _args = (1, 2) _kwargs = {"one": 1, "two": 2} @wrapt.decorator def _dec...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 72`, `args: 36`, `func_start: 36`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 27`, `duplicate_logic: 18`, `unreferenced_by_name: 18`
* *Architecture:* `api: 30`, `import: 4`
* *Defense:* `safety: 6`, `doc: 3`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.967
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inspect, types, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_auto_object_proxy.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 140.24 | **LOC:** 185 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.8423%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_descriptor` (Impact: 5.2)
  * `test_aiter` (Impact: 4.4)
  * `__get__` (Impact: 4.3)
  * `test_next` (Impact: 2.5)
  * `test_await` (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 34
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 54`, `args: 24`, `func_start: 23`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 27`, `unreferenced_by_name: 7`
* *Architecture:* `api: 18`, `concurrency: 9`, `import: 5`
* *Defense:* `safety: 31`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.967
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` asyncio, operator, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_weak_function_proxy.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 136.26 | **LOC:** 222 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.8318%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_instancemethod_delete_function` (Impact: 2.7)
  * `test_instancemethod_delete_function_and_instance` (Impact: 2.7)
  * `test_classmethod` (Impact: 2.7)
  * `test_instancemethod_delete_instance` (Impact: 2.6)
  * `test_staticmethod` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 61`, `args: 30`, `func_start: 30`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 36`, `duplicate_logic: 14`, `unreferenced_by_name: 11`
* *Architecture:* `api: 38`, `import: 3`
* *Defense:* `safety: 1`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.967
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` gc, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_adapter_py3.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 131.2 | **LOC:** 261 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.6722%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_dynamic_adapter_classmethod` (Impact: 3.7)
  * `test_dynamic_adapter_instancemethod` (Impact: 3.6)
  * `test_dynamic_adapter_function` (Impact: 3.2)
  * `_adapter1` (Impact: 2.7)
  * `_adapter2` (Impact: 2.7)
    * *Intent:* # Can't use a function signature with adapter factory which has # annotations which reference a non ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 77`, `args: 35`, `func_start: 35`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 28`, `duplicate_logic: 17`, `unreferenced_by_name: 8`
* *Architecture:* `api: 24`, `import: 5`
* *Defense:* `safety: 1`, `doc: 5`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.967
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inspect, types, typing, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_update_attributes.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 130.06 | **LOC:** 238 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.4622%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_update_qualname_modified_on_original` (Impact: 2.5)
  * `test_delete_qualname_modified_on_original` (Impact: 2.4)
  * `test_delete_annotations_modified_on_original` (Impact: 2.4)
  * `passthru_decorator` (Impact: 2.3)
  * `wrapper` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 63`, `args: 36`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 26`, `duplicate_logic: 21`, `unreferenced_by_name: 14`
* *Architecture:* `api: 37`, `import: 2`
* *Defense:* `doc: 2`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.967
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/conftest.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 127.36 | **LOC:** 186 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.0391%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pytest_pycollect_makemodule` (Impact: 16.7)
  * `pytest_collect_file` (Impact: 11.5)
    * *Intent:* """ Hook that allows adding our MypyPairCollector when pytest collects files. We attach the collecto...
  * `collect` (Impact: 9.7)
    * *Intent:* # Only run this custom collection on Python 3.10+ if version < (3, 10): return # Skip mypy tests if ...
  * `runtest` (Impact: 6.7)
    * *Intent:* # Try to run mypy; if it's not found, skip the test try: actual_output = run_custom_action(self.py_p...
  * `construct_dummy` (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 42`, `args: 9`, `func_start: 9`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 24`, `unreferenced_by_name: 5`
* *Architecture:* `io: 10`, `api: 11`, `import: 10`
* *Defense:* `safety: 7`, `doc: 3`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.967
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, pathlib, platform, pytest, pytest.collect, re, subprocess, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_adapter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 125.76 | **LOC:** 232 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.4492%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_object_qualname` (Impact: 3.3)
    * *Intent:* # Test preservation of function __qualname__ attribute. try: __qualname__ = function1o.__qualname__ ...
  * `test_dynamic_adapter_classmethod` (Impact: 3.3)
  * `test_dynamic_adapter_instancemethod` (Impact: 3.2)
  * `test_dynamic_adapter_function` (Impact: 2.8)
  * `_adapter` (Impact: 2.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 68`, `args: 33`, `func_start: 33`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 24`, `duplicate_logic: 16`, `unreferenced_by_name: 11`
* *Architecture:* `api: 25`, `import: 4`
* *Defense:* `safety: 3`, `doc: 3`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.967
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inspect, types, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_outer_classmethod.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 111.1 | **LOC:** 207 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.2735%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_decorator` (Impact: 7.4)
  * `_decorator` (Impact: 7.4)
  * `test_class_call_function` (Impact: 6.4)
    * *Intent:* # Test calling classmethod. Prior to Python 3.9, the instance # and class passed to the wrapper will...
  * `test_instance_call_function` (Impact: 6.3)
    * *Intent:* # Test calling classmethod via class instance. Prior to Python # 3.9, the instance and class passed ...
  * `test_class_object_qualname` (Impact: 3.3)
    * *Intent:* # Test preservation of instance method __qualname__ attribute. try: __qualname__ = Original.original...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 46`, `args: 22`, `func_start: 22`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 15`, `dead_code: 1`, `duplicate_logic: 8`, `unreferenced_by_name: 14`
* *Architecture:* `api: 22`, `import: 5`
* *Defense:* `safety: 6`, `doc: 3`, `test: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.967
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` compat, inspect, types, unittest, wrapt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_post_import_hooks.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 108.84 | **LOC:** 183 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.4174%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_import_deadlock_3` (Impact: 2.9)
    * *Intent:* # This tries to verify that we haven't created a deadlock situation when # code executed from a post...
  * `test_before_and_after_import` (Impact: 2.6)
  * `test_import_deadlock_1` (Impact: 2.5)
    * *Intent:* # This tries to verify that we haven't created a deadlock situation when # code executed from a post...
  * `test_import_deadlock_2` (Impact: 2.5)
    * *Intent:* # This tries to verify that we haven't created a deadlock situation when # code executed from a post...
  * `test_remove_from_sys_modules` (Impact: 2.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Concurrency (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 50`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 18`, `fragile_debt: 2`, `duplicate_logic: 9`, `unreferenced_by_name: 12`
* *Architecture:* `io: 6`, `api: 25`, `concurrency: 4`, `import: 16`
* *Defense:* `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.967
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` hook, hook., hooks, hooks., importlib.machinery, sys, this, threading...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `wrapt-2.1.2/src/wrapt/__wrapt__.py` -> **Severity: 0.237** (Bridge: 0.0025 * Flux: 96.0834%)
- `wrapt-2.1.2/src/wrapt/importer.py` -> **Severity: 0.093** (Bridge: 0.0009 * Flux: 100.0%)
- `wrapt-2.1.2/src/wrapt/decorators.py` -> **Severity: 0.031** (Bridge: 0.0003 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `wrapt-2.1.2/src/wrapt/__wrapt__.py` -> **Severity: 5.49** (Embedded: 0.079 * Error Risk: 69.4842%)
- `wrapt-2.1.2/src/wrapt/_wrappers.c` -> **Severity: 4.761** (Embedded: 0.0526 * Error Risk: 90.4607%)
- `wrapt-2.1.2/src/wrapt/arguments.py` -> **Severity: 4.353** (Embedded: 0.0441 * Error Risk: 98.7311%)
- `wrapt-2.1.2/src/wrapt/importer.py` -> **Severity: 3.5** (Embedded: 0.037 * Error Risk: 94.4909%)
- `wrapt-2.1.2/src/wrapt/wrappers.py` -> **Severity: 3.119** (Embedded: 0.0526 * Error Risk: 59.2601%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `wrapt-2.1.2/src/wrapt/_wrappers.c` -> **Severity: 3824.6** (Blast Radius: 38.246 * Doc Risk: 100.0%)
- `wrapt-2.1.2/src/wrapt/wrappers.py` -> **Severity: 3613.796** (Blast Radius: 38.246 * Doc Risk: 94.4882%)
- `wrapt-2.1.2/src/wrapt/arguments.py` -> **Severity: 3380.1** (Blast Radius: 33.801 * Doc Risk: 100.0%)
- `wrapt-2.1.2/src/wrapt/importer.py` -> **Severity: 2252.808** (Blast Radius: 28.321 * Doc Risk: 79.5455%)
- `wrapt-2.1.2/src/wrapt/decorators.py` -> **Severity: 1441.245** (Blast Radius: 16.214 * Doc Risk: 88.8889%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
