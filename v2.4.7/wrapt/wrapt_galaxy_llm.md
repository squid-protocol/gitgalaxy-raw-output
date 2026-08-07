# ARCHITECTURAL_BRIEF: wrapt
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/wrapt` |
| **Timestamp** | `2026-08-07T05:27:33.720839+00:00` |
| **Scan Duration** | `0.39s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 79 malicious artifacts.

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
| Modularity | 0.3764 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
> **Architectural Drift Z-Score:** `4.44`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_16 | 30 | 37.0% |
| file_cluster_8 | 22 | 27.2% |
| file_cluster_13 | 15 | 18.5% |
| file_cluster_0 | 11 | 13.6% |
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
| Cognitive Load Exposure | 0.0 | 65.0 | 11.7 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 56.1 | 60.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 7.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 5.3 | 0.0 | 0.0 |
| API Exposure | 0.0 | 12.9 | 4.9 | 4.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 4.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 7.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 76.4 | 2.8 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 88.4 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 99.5 | 6.1 | 0.0 | 0.0 |
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

- `decorator` (@ `wrapt-2.1.2/src/wrapt/decorators.py`) -> Impact: **70.2** | LOC: 239
  * *Intent:* # Decorator for creating other decorators. This decorator and the # wrappers which they use are designed to properly preserve any name # attributes, f...
- `__wrapped_setattr_fixups__` (@ `wrapt-2.1.2/src/wrapt/proxies.py`) -> Impact: **62.5** | LOC: 72
- `__new__` (@ `wrapt-2.1.2/src/wrapt/proxies.py`) -> Impact: **56.4** | LOC: 55
- `__new__` (@ `wrapt-2.1.2/src/wrapt/proxies.py`) -> Impact: **44.2** | LOC: 52
- `_wrapper` (@ `wrapt-2.1.2/src/wrapt/decorators.py`) -> Impact: **39.7** | LOC: 167
- `__init__` (@ `wrapt-2.1.2/src/wrapt/wrappers.py`) -> Impact: **34.5** | LOC: 109
- `WraptFunctionWrapper_init` (@ `wrapt-2.1.2/src/wrapt/_wrappers.c`) -> Impact: **32.9** | LOC: 118
- `raise_uninitialized_wrapper_error` (@ `wrapt-2.1.2/src/wrapt/_wrappers.c`) -> Impact: **28.2** | LOC: 165
  * *Intent:* /* ------------------------------------------------------------------------- */
- `__setattr__` (@ `wrapt-2.1.2/src/wrapt/wrappers.py`) -> Impact: **26.2** | LOC: 44
- `__call__` (@ `wrapt-2.1.2/src/wrapt/wrappers.py`) -> Impact: **26.0** | LOC: 70

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `wrapt-2.1.2/tests/core` | 36 | 4314.42 | 10.93% | 0.0% |
| `wrapt-2.1.2/src/wrapt` | 11 | 1839.3 | 34.27% | 53.23% |
| `wrapt-2.1.2/tests/mypy` | 31 | 422.68 | 4.52% | 0.0% |
| `wrapt-2.1.2` | 3 | 19.28 | 4.1% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `wrapt-2.1.2/src/wrapt/__init__.pyi` -> **100.0%** Exposure
- `wrapt-2.1.2/src/wrapt/decorators.py` -> **100.0%** Exposure
- `wrapt-2.1.2/src/wrapt/patches.py` -> **99.9994%** Exposure
- `wrapt-2.1.2/src/wrapt/importer.py` -> **99.9955%** Exposure
- `wrapt-2.1.2/src/wrapt/wrappers.py` -> **99.9404%** Exposure
### Highest State Flux (Mutation/Volatility)
- `wrapt-2.1.2/src/wrapt/_wrappers.c` -> **100.0%** Exposure
- `wrapt-2.1.2/src/wrapt/proxies.py` -> **99.8775%** Exposure
- `wrapt-2.1.2/src/wrapt/weakrefs.py` -> **99.8367%** Exposure
- `wrapt-2.1.2/src/wrapt/arguments.py` -> **99.2754%** Exposure
- `wrapt-2.1.2/src/wrapt/importer.py` -> **84.0157%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `wrapt-2.1.2/tests/core/test_object_proxy.py` -> **149** Orphaned Functions | **143** Duplicates
- `wrapt-2.1.2/tests/core/test_function_wrapper.py` -> **28** Orphaned Functions | **57** Duplicates
- `wrapt-2.1.2/tests/core/test_inplace_operators.py` -> **52** Orphaned Functions | **23** Duplicates
- `wrapt-2.1.2/tests/core/test_instancemethod.py` -> **1** Orphaned Functions | **60** Duplicates
- `wrapt-2.1.2/tests/core/test_monkey_patching.py` -> **17** Orphaned Functions | **35** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `245` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `wrapt-2.1.2/src/wrapt/proxies.py` (PYTHON) -> Cumulative Risk: **595.51**
- **Archetype:** `file_cluster_13` (Distance: 12.972 IQR)
- **Magnitude:** 278.94 | **LOC:** 352 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8775%), Tech Debt (85.5459%), Verification (80.0%)
- **Heaviest Functions:** `__wrapped_setattr_fixups__` (Impact: 62.5), `__new__` (Impact: 56.4), `__new__` (Impact: 44.2)

### 2. `wrapt-2.1.2/src/wrapt/decorators.py` (PYTHON) -> Cumulative Risk: **565.84**
- **Archetype:** `file_cluster_0` (Distance: 18.663 IQR)
- **Magnitude:** 253.8 | **LOC:** 523 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Verification (80.0%), Dead Code (76.4436%)
- **Heaviest Functions:** `decorator` (Impact: 70.2), `_wrapper` (Impact: 39.7), `synchronized` (Impact: 22.1)

### 3. `wrapt-2.1.2/src/wrapt/wrappers.py` (PYTHON) -> Cumulative Risk: **552.05**
- **Archetype:** `file_cluster_0` (Distance: 11.566 IQR)
- **Magnitude:** 525.18 | **LOC:** 985 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9404%), Documentation (88.0699%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Impact: 34.5), `__setattr__` (Impact: 26.2), `__call__` (Impact: 26.0)

### 4. `wrapt-2.1.2/src/wrapt/patches.py` (PYTHON) -> Cumulative Risk: **549.32**
- **Archetype:** `file_cluster_13` (Distance: 12.854 IQR)
- **Magnitude:** 135.16 | **LOC:** 240 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9994%), Verification (80.0%), Documentation (76.0347%)
- **Heaviest Functions:** `resolve_path` (Impact: 16.0), `_wrapper` (Impact: 14.4), `transient_function_wrapper` (Impact: 11.8)

### 5. `wrapt-2.1.2/src/wrapt/_wrappers.c` (C) -> Cumulative Risk: **510.39**
- **Archetype:** `file_cluster_8` (Distance: 13.658 IQR)
- **Magnitude:** 314.72 | **LOC:** 4098 | **CtrlFlow:** 65.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (87.6106%), Verification (80.0%)
- **Heaviest Functions:** `WraptFunctionWrapper_init` (Impact: 32.9), `raise_uninitialized_wrapper_error` (Impact: 28.2), `moduleinit` (Impact: 14.1)

### 6. `wrapt-2.1.2/src/wrapt/__init__.pyi` (PYTHON) -> Cumulative Risk: **480.56**
- **Archetype:** `file_cluster_16` (Distance: 8.587 IQR)
- **Magnitude:** 101.42 | **LOC:** 389 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (99.5321%), Safety Score (98.6505%)
- **Heaviest Functions:** `wrap_object_attribute` (Impact: 2.5), `__call__` (Impact: 2.1), `wrap_object` (Impact: 1.3)

### 7. `wrapt-2.1.2/src/wrapt/importer.py` (PYTHON) -> Cumulative Risk: **478.85**
- **Archetype:** `file_cluster_13` (Distance: 13.159 IQR)
- **Magnitude:** 145.84 | **LOC:** 333 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9955%), State Flux (84.0157%), Stability (50.0%)
- **Heaviest Functions:** `find_spec` (Impact: 19.9), `find_module` (Impact: 17.9), `register_post_import_hook` (Impact: 12.1)

### 8. `wrapt-2.1.2/src/wrapt/arguments.py` (PYTHON) -> Cumulative Risk: **393.31**
- **Archetype:** `file_cluster_16` (Distance: 10.943 IQR)
- **Magnitude:** 15.2 | **LOC:** 60 | **CtrlFlow:** 59.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.2754%), Safety Score (90.4724%), Stability (50.0%)
- **Heaviest Functions:** `formatargspec` (Impact: 4.2)

### 9. `wrapt-2.1.2/src/wrapt/weakrefs.py` (PYTHON) -> Cumulative Risk: **354.9**
- **Archetype:** `file_cluster_13` (Distance: 11.179 IQR)
- **Magnitude:** 47.52 | **LOC:** 122 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8367%), Safety Score (60.5657%), Stability (50.0%)
- **Heaviest Functions:** `__init__` (Impact: 14.4), `__call__` (Impact: 11.8), `_weak_function_proxy_callback` (Impact: 6.6)

### 10. `wrapt-2.1.2/tests/core/test_post_import_hooks.py` (PYTHON) -> Cumulative Risk: **337.42**
- **Archetype:** `file_cluster_13` (Distance: 9.817 IQR)
- **Magnitude:** 98.24 | **LOC:** 183 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (96.8185%), Safety Score (71.095%), Stability (50.0%)
- **Heaviest Functions:** `test_import_deadlock_3` (Impact: 3.2), `test_before_and_after_import` (Impact: 2.9), `test_import_deadlock_1` (Impact: 2.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `wrapt-2.1.2/tests/core/test_object_proxy.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.253 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.01 IQR)
- **Top Global Matches:** file_cluster_8: 11.253, file_cluster_0: 11.554, file_cluster_17: 11.846
- **Magnitude:** 1290.86 | **LOC:** 2694 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.6746%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_self_keyword_argument_on_class_init` (Impact: 13.7)
  * `test_self_keyword_argument_on_class_init` (Impact: 13.6)
  * `test_self_keyword_argument_on_class_init` (Impact: 13.6)
  * `test_self_keyword_argument_on_class_init` (Impact: 13.6)
  * `test_self_keyword_argument_on_class_init` (Impact: 13.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 587`, `args: 295`, `func_start: 295`, `class_start: 98`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 31`, `dead_code: 1`, `duplicate_logic: 143`, `orphaned_logic: 149`
* *Architecture:* `io: 1`, `api: 356`, `concurrency: 7`, `import: 8`
* *Defense:* `safety: 157`, `doc: 2`, `test: 262`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` wrapt, unittest, asyncio, re, types, fractions, sys, decimal
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/src/wrapt/wrappers.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.566 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.429 IQR)
- **Top Global Matches:** file_cluster_0: 11.566, file_cluster_8: 11.695, file_cluster_12: 11.854
- **Magnitude:** 525.18 | **LOC:** 985 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.8794%), Tech Debt (99.9404%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 34.5)
  * `__setattr__` (Impact: 26.2)
  * `__call__` (Impact: 26.0)
  * `__get__` (Impact: 17.8)
  * `__call__` (Impact: 15.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 280`, `args: 118`, `func_start: 118`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 17`, `dead_code: 5`, `duplicate_logic: 21`
* *Architecture:* `api: 73`, `import: 3`
* *Defense:* `safety: 48`, `doc: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 38.632
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.053289
  * `Imports (Out-Degree: 0):` inspect, sys, operator
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wrapt-2.1.2/tests/core/test_function_wrapper.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_0` (Drift: 9.472 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.132 IQR)
- **Top Global Matches:** file_cluster_0: 9.472, file_cluster_8: 9.485, file_cluster_7: 10.184
- **Magnitude:** 320.36 | **LOC:** 599 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.2524%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_boolean_dynamic_guard_on_decorator` (Impact: 3.4)
  * `test_guard_on_instancemethod` (Impact: 3.4)
  * `test_re_bind_after_none` (Impact: 3.4)
  * `test_double_binding` (Impact: 3.3)
  * `test_function_guard_on_decorator` (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 192`, `args: 92`, `func_start: 92`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 3`, `duplicate_logic: 57`, `orphaned_logic: 28`
* *Architecture:* `api: 102`, `import: 2`
* *Defense:* `safety: 21`, `test: 48`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` wrapt, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/src/wrapt/_wrappers.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.658 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.679 IQR)
- **Top Global Matches:** file_cluster_8: 13.658, file_cluster_0: 13.67, file_cluster_13: 13.699
- **Magnitude:** 314.72 | **LOC:** 4098 | **CtrlFlow:** 65.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.9867%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `WraptFunctionWrapper_init` (Impact: 32.9)
  * `raise_uninitialized_wrapper_error` (Impact: 28.2)
    * *Intent:* /* ------------------------------------------------------------------------- */
  * `moduleinit` (Impact: 14.1)
  * `PyInit__wrappers` (Impact: 1.5)
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

### `wrapt-2.1.2/src/wrapt/proxies.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.972 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.764 IQR)
- **Top Global Matches:** file_cluster_13: 12.972, file_cluster_12: 13.044, file_cluster_8: 13.213
- **Magnitude:** 278.94 | **LOC:** 352 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.9493%), Tech Debt (85.5459%)
**Top Internal Functions/Classes:**
  * `__wrapped_setattr_fixups__` (Impact: 62.5)
  * `__new__` (Impact: 56.4)
  * `__new__` (Impact: 44.2)
  * `lazy_import` (Impact: 14.4)
    * *Intent:* # We were called because `__wrapped__` was not set, but because of # we get the lock. So check again...
  * `__wrapped_get__` (Impact: 6.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 64`, `args: 23`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 42`, `dead_code: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 8`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 22`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0125
  * `Imports (Out-Degree: 2):` .decorators, .__wrapt__, types, collections.abc, the
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wrapt-2.1.2/tests/core/test_inplace_operators.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.735 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.458 IQR)
- **Top Global Matches:** file_cluster_8: 7.735, file_cluster_7: 8.669, file_cluster_1: 8.896
- **Magnitude:** 265.1 | **LOC:** 825 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.0623%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_inplace_matmul` (Impact: 5.0)
  * `test_inplace_matmul_immutable` (Impact: 4.9)
  * `__eq__` (Impact: 3.7)
  * `__eq__` (Impact: 3.7)
  * `test_inplace_add_integer` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 159`, `args: 75`, `func_start: 75`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 8`, `duplicate_logic: 23`, `orphaned_logic: 52`
* *Architecture:* `api: 71`, `import: 2`
* *Defense:* `safety: 2`, `test: 68`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` wrapt, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/src/wrapt/decorators.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_0` (Drift: 18.663 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.191 IQR)
- **Top Global Matches:** file_cluster_0: 18.663, file_cluster_11: 18.99, file_cluster_6: 19.022
- **Magnitude:** 253.8 | **LOC:** 523 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.4457%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `decorator` (Impact: 70.2)
    * *Intent:* # Decorator for creating other decorators. This decorator and the # wrappers which they use are desi...
  * `_wrapper` (Impact: 39.7)
  * `synchronized` (Impact: 22.1)
    * *Intent:* # We first return our magic function wrapper here so we can # determine in what context the decorato...
  * `_build` (Impact: 17.6)
  * `_synchronized_wrapper` (Impact: 9.3)
    * *Intent:* # Following only apply when the lock is being created automatically # based on the context of what w...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 91`, `args: 33`, `func_start: 33`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 7`, `dead_code: 22`, `planned_debt: 1`, `duplicate_logic: 19`
* *Architecture:* `api: 10`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 4`, `doc: 6`, `sync_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.378
  * `Choke Point (Betweenness):` 0.000316 | `Ripple Effect (Closeness):` 0.025
  * `Imports (Out-Degree: 2):` inspect, functools, .__wrapt__, sys, threading, .arguments
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `wrapt-2.1.2/tests/core/test_monkey_patching.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.516 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.351 IQR)
- **Top Global Matches:** file_cluster_8: 8.516, file_cluster_0: 8.891, file_cluster_7: 9.197
- **Magnitude:** 249.32 | **LOC:** 572 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.8861%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_patch_function_module_name_enabled_` (Impact: 3.4)
  * `test_transient_function_wrapper_instance` (Impact: 3.2)
  * `test_function_wrapper_instance_method` (Impact: 3.1)
  * `test_patch_instance_method_class` (Impact: 3.1)
  * `test_patch_instance_method_dict` (Impact: 3.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 122`, `args: 61`, `func_start: 61`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 21`, `duplicate_logic: 35`, `orphaned_logic: 17`
* *Architecture:* `io: 2`, `api: 71`, `import: 3`
* *Defense:* `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` wrapt, unittest, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_instancemethod.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.46 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.418 IQR)
- **Top Global Matches:** file_cluster_8: 9.46, file_cluster_0: 9.556, file_cluster_7: 9.936
- **Magnitude:** 206.06 | **LOC:** 459 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.3266%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_class_object_qualname` (Impact: 5.6)
    * *Intent:* # Test preservation of instance method __name__ attribute.
  * `test_instance_object_qualname` (Impact: 5.6)
  * `test_class_object_qualname` (Impact: 5.6)
  * `test_instance_object_qualname` (Impact: 5.6)
  * `test_class_call_function_nested` (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 117`, `args: 61`, `func_start: 61`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `duplicate_logic: 60`, `orphaned_logic: 1`
* *Architecture:* `api: 53`, `import: 4`
* *Defense:* `safety: 12`, `doc: 10`, `test: 43`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inspect, unittest, wrapt, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/src/wrapt/importer.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.159 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.6 IQR)
- **Top Global Matches:** file_cluster_13: 13.159, file_cluster_11: 13.427, file_cluster_0: 13.496
- **Magnitude:** 145.84 | **LOC:** 333 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.654%), Tech Debt (99.9955%)
**Top Internal Functions/Classes:**
  * `find_spec` (Impact: 19.9)
    * *Intent:* # from the importlib.util module. It doesn't actually # import the target module and only finds the ...
  * `find_module` (Impact: 17.9)
    * *Intent:* # Python 3.4 introduced create_module() and exec_module() instead of
  * `register_post_import_hook` (Impact: 12.1)
  * `_self_set_loader` (Impact: 10.0)
  * `__init__` (Impact: 7.4)
    * *Intent:* # A custom module import finder. This intercepts attempts to import # interest. When a module of int...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 51`, `args: 18`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 13`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 5`, `api: 16`, `concurrency: 2`, `import: 8`
* *Defense:* `safety: 22`, `doc: 10`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.606
  * `Choke Point (Betweenness):` 0.000949 | `Ripple Effect (Closeness):` 0.0375
  * `Imports (Out-Degree: 1):` system, hook, finder., that, target, .__wrapt__, hooks, hook....
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `wrapt-2.1.2/tests/core/test_inner_classmethod.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.432 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.709 IQR)
- **Top Global Matches:** file_cluster_8: 9.432, file_cluster_0: 9.454, file_cluster_7: 9.916
- **Magnitude:** 140.18 | **LOC:** 331 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.758%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_class_object_qualname` (Impact: 5.6)
    * *Intent:* # Test preservation of instance method __name__ attribute.
  * `test_instance_object_qualname` (Impact: 5.6)
  * `test_class_call_function_nested_decorato` (Impact: 3.1)
  * `test_instance_call_function_nested_decor` (Impact: 3.1)
  * `test_class_call_function` (Impact: 3.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 84`, `args: 42`, `func_start: 42`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `duplicate_logic: 22`, `orphaned_logic: 20`
* *Architecture:* `api: 34`, `import: 4`
* *Defense:* `safety: 6`, `doc: 6`, `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inspect, unittest, wrapt, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_decorators.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.264 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.525 IQR)
- **Top Global Matches:** file_cluster_8: 8.264, file_cluster_0: 8.609, file_cluster_7: 9.018
- **Magnitude:** 139.88 | **LOC:** 344 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0846%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_call_semantics_for_assorted_decorat` (Impact: 4.9)
  * `test_decorated_function_as_instance_attr` (Impact: 3.8)
  * `test_decorated_function_as_class_attribu` (Impact: 3.7)
  * `test_call_semantics_for_assorted_wrapped` (Impact: 3.6)
  * `test_decorated_builtin_as_class_attribut` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 89`, `args: 41`, `func_start: 41`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 4`, `duplicate_logic: 26`, `orphaned_logic: 10`
* *Architecture:* `api: 36`, `import: 3`
* *Defense:* `safety: 1`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` wrapt, unittest, operator
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/src/wrapt/patches.py` (PYTHON | Tier 4 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.854 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.529 IQR)
- **Top Global Matches:** file_cluster_13: 12.854, file_cluster_12: 13.094, file_cluster_11: 13.137
- **Magnitude:** 135.16 | **LOC:** 240 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.4276%), Tech Debt (99.9994%)
**Top Internal Functions/Classes:**
  * `resolve_path` (Impact: 16.0)
    * *Intent:* # Helper functions for applying wrappers to existing functions. """ Resolves the dotted path supplie...
  * `_wrapper` (Impact: 14.4)
  * `transient_function_wrapper` (Impact: 11.8)
  * `_decorator` (Impact: 11.5)
  * `lookup_attribute` (Impact: 10.8)
    * *Intent:* # We can't just always use getattr() because in doing # that on a class it will cause binding to occ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 42`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `io: 1`, `api: 18`, `import: 4`
* *Defense:* `safety: 5`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.493
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0125
  * `Imports (Out-Degree: 1):` inspect, sys, .__wrapt__
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wrapt-2.1.2/tests/core/test_auto_object_proxy.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.457 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.236 IQR)
- **Top Global Matches:** file_cluster_4: 12.457, file_cluster_13: 12.81, file_cluster_8: 12.886
- **Magnitude:** 132.34 | **LOC:** 185 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.1059%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_aiter` (Impact: 6.7)
  * `test_descriptor` (Impact: 5.9)
  * `__get__` (Impact: 4.3)
  * `__anext__` (Impact: 4.2)
  * `iterate` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 54`, `args: 24`, `func_start: 23`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15`, `duplicate_logic: 4`, `orphaned_logic: 7`
* *Architecture:* `api: 18`, `concurrency: 34`, `import: 5`
* *Defense:* `safety: 31`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` wrapt, unittest, operator, asyncio
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_entry_points.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.173 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.043 IQR)
- **Top Global Matches:** file_cluster_13: 12.173, file_cluster_8: 12.518, file_cluster_4: 12.587
- **Magnitude:** 124.72 | **LOC:** 252 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.0778%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_threading_safety_with_entry_points` (Impact: 8.6)
  * `test_entry_point_hook_exception_handling` (Impact: 7.9)
  * `test_entry_point_load_failure` (Impact: 7.6)
    * *Intent:* # Should propagate the ImportError with pytest.raises(ImportError, match="Cannot load entry point"):...
  * `test_discover_post_import_hooks_python38` (Impact: 5.2)
  * `test_multiple_entry_points_same_group` (Impact: 5.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 64`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 17`, `duplicate_logic: 2`, `orphaned_logic: 10`
* *Architecture:* `io: 1`, `api: 21`, `concurrency: 7`, `import: 14`
* *Defense:* `safety: 15`, `doc: 20`, `test: 49`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` this, wrapt, unittest.mock, wrapt.importer, importlib.metadata, sys, threading, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_weak_function_proxy.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.167 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.153 IQR)
- **Top Global Matches:** file_cluster_8: 9.167, file_cluster_0: 9.566, file_cluster_13: 9.652
- **Magnitude:** 118.86 | **LOC:** 222 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.8686%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_instancemethod_delete_instance` (Impact: 4.7)
  * `test_instancemethod_delete_function` (Impact: 4.7)
  * `test_instancemethod_delete_function_and_` (Impact: 4.7)
  * `test_classmethod` (Impact: 4.7)
  * `test_staticmethod` (Impact: 2.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 57`, `args: 30`, `func_start: 30`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 6`, `duplicate_logic: 16`, `orphaned_logic: 11`
* *Architecture:* `api: 38`, `import: 3`
* *Defense:* `safety: 1`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` wrapt, unittest, gc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_inner_staticmethod.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_0` (Drift: 9.63 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.735 IQR)
- **Top Global Matches:** file_cluster_0: 9.63, file_cluster_8: 9.659, file_cluster_13: 10.067
- **Magnitude:** 118.54 | **LOC:** 279 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.9093%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_class_object_qualname` (Impact: 5.6)
    * *Intent:* # Test preservation of instance method __module__ attribute.
  * `test_instance_object_qualname` (Impact: 5.6)
  * `test_class_call_function_nested_decorato` (Impact: 3.1)
  * `test_instance_call_function_nested_decor` (Impact: 3.1)
  * `test_class_call_function` (Impact: 3.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 72`, `args: 36`, `func_start: 36`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `duplicate_logic: 18`, `orphaned_logic: 18`
* *Architecture:* `api: 30`, `import: 4`
* *Defense:* `safety: 6`, `doc: 6`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inspect, unittest, wrapt, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_update_attributes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.013 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.135 IQR)
- **Top Global Matches:** file_cluster_8: 8.013, file_cluster_7: 8.622, file_cluster_0: 8.743
- **Magnitude:** 118.36 | **LOC:** 238 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (1.9729%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_update_qualname_modified_on_origina` (Impact: 2.8)
  * `test_delete_qualname_modified_on_origina` (Impact: 2.7)
  * `test_delete_annotations_modified_on_orig` (Impact: 2.7)
  * `test_update_doc_modified_on_original` (Impact: 2.6)
    * *Intent:* """documentation"""
  * `test_update_name_modified_on_original` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 63`, `args: 36`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `duplicate_logic: 21`, `orphaned_logic: 13`
* *Architecture:* `api: 37`, `import: 2`
* *Defense:* `doc: 4`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` wrapt, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_adapter_py3.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.896 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.107 IQR)
- **Top Global Matches:** file_cluster_16: 9.896, file_cluster_0: 9.959, file_cluster_8: 10.07
- **Magnitude:** 109.5 | **LOC:** 261 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.2765%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_dynamic_adapter_classmethod` (Impact: 4.0)
  * `test_dynamic_adapter_instancemethod` (Impact: 3.9)
  * `test_dynamic_adapter_function` (Impact: 3.5)
  * `_adapter1` (Impact: 2.7)
  * `_adapter2` (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 77`, `args: 35`, `func_start: 35`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 1`, `duplicate_logic: 25`, `orphaned_logic: 8`
* *Architecture:* `api: 24`, `import: 5`
* *Defense:* `safety: 1`, `doc: 14`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inspect, unittest, wrapt, types, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_adapter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_0` (Drift: 9.813 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.462 IQR)
- **Top Global Matches:** file_cluster_0: 9.813, file_cluster_8: 9.904, file_cluster_12: 10.043
- **Magnitude:** 106.96 | **LOC:** 232 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.383%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_object_qualname` (Impact: 5.6)
    * *Intent:* # Test preservation of function __name__ attribute. self.assertEqual(function1d.__name__, function1o...
  * `test_dynamic_adapter_classmethod` (Impact: 3.6)
  * `test_dynamic_adapter_instancemethod` (Impact: 3.5)
  * `test_dynamic_adapter_function` (Impact: 3.1)
    * *Intent:* # Test preservation of isinstance() checks.
  * `_adapter` (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 68`, `args: 33`, `func_start: 33`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 1`, `duplicate_logic: 20`, `orphaned_logic: 11`
* *Architecture:* `api: 25`, `import: 4`
* *Defense:* `safety: 3`, `doc: 8`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inspect, unittest, wrapt, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/src/wrapt/__init__.pyi` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_16` (Drift: 8.587 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.173 IQR)
- **Top Global Matches:** file_cluster_16: 8.587, file_cluster_0: 9.074, file_cluster_8: 9.108
- **Magnitude:** 101.42 | **LOC:** 389 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.1292%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `wrap_object_attribute` (Impact: 2.5)
    * *Intent:* # wrap_object_attribute()
  * `__call__` (Impact: 2.1)
  * `wrap_object` (Impact: 1.3)
  * `__init__` (Impact: 1.2)
  * `__get__` (Impact: 1.2)
    * *Intent:* # Note that for following overloads, testing with mypy and ty they still do # not handle static meth...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 113`, `args: 60`, `func_start: 60`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 88`, `dead_code: 1`, `duplicate_logic: 24`
* *Architecture:* `io: 1`, `api: 54`, `import: 4`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typing, inspect, sys, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_post_import_hooks.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.817 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.177 IQR)
- **Top Global Matches:** file_cluster_13: 9.817, file_cluster_0: 9.968, file_cluster_4: 10.106
- **Magnitude:** 98.24 | **LOC:** 183 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.829%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_import_deadlock_3` (Impact: 3.2)
    * *Intent:* # This tries to verify that we haven't created a deadlock situation when # code executed from a post...
  * `test_before_and_after_import` (Impact: 2.9)
  * `test_import_deadlock_1` (Impact: 2.8)
    * *Intent:* # This tries to verify that we haven't created a deadlock situation when # code executed from a post...
  * `test_import_deadlock_2` (Impact: 2.8)
    * *Intent:* # This tries to verify that we haven't created a deadlock situation when # code executed from a post...
  * `test_remove_from_sys_modules` (Impact: 2.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 50`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 9`, `fragile_debt: 2`, `duplicate_logic: 12`, `orphaned_logic: 11`
* *Architecture:* `io: 6`, `api: 25`, `concurrency: 9`, `import: 16`
* *Defense:* `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` this, wrapt, unittest, hook, importlib.machinery, wsgiref, wrapt.importer, hooks...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_outer_classmethod.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.651 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.801 IQR)
- **Top Global Matches:** file_cluster_0: 10.651, file_cluster_13: 10.954, file_cluster_8: 11.089
- **Magnitude:** 95.5 | **LOC:** 207 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.5753%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_decorator` (Impact: 7.4)
  * `_decorator` (Impact: 7.4)
  * `test_class_call_function` (Impact: 7.3)
  * `test_instance_call_function` (Impact: 7.2)
  * `test_class_object_qualname` (Impact: 5.6)
    * *Intent:* # Test preservation of instance method __name__ attribute.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 46`, `args: 22`, `func_start: 22`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `dead_code: 1`, `duplicate_logic: 8`, `orphaned_logic: 14`
* *Architecture:* `api: 22`, `import: 5`
* *Defense:* `safety: 6`, `doc: 6`, `test: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` inspect, unittest, wrapt, compat, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_synchronized_lock.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.768 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.032 IQR)
- **Top Global Matches:** file_cluster_0: 11.768, file_cluster_8: 12.076, file_cluster_12: 12.147
- **Magnitude:** 87.26 | **LOC:** 311 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.0308%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_synchronized_outer_classmethod` (Impact: 17.6)
    * *Intent:* # Prior to Python 3.9 this isn't detected as a class method # call, as the classmethod decorator doe...
  * `test_synchronized_instancemethod` (Impact: 5.3)
  * `test_synchronized_inner_classmethod` (Impact: 4.6)
  * `test_synchronized_type_new_style` (Impact: 4.6)
  * `test_synchronized_type_old_style` (Impact: 4.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 35`, `args: 17`, `func_start: 17`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `dead_code: 2`, `duplicate_logic: 6`, `orphaned_logic: 9`
* *Architecture:* `api: 22`, `import: 3`
* *Defense:* `safety: 44`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` wrapt, unittest, compat
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wrapt-2.1.2/tests/core/test_outer_staticmethod.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.394 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.8 IQR)
- **Top Global Matches:** file_cluster_0: 10.394, file_cluster_8: 10.497, file_cluster_13: 10.638
- **Magnitude:** 76.74 | **LOC:** 180 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.0807%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_class_object_qualname` (Impact: 5.6)
    * *Intent:* # Test preservation of instance method __name__ attribute.
  * `test_instance_object_qualname` (Impact: 5.6)
  * `test_class_call_function` (Impact: 3.2)
  * `test_instance_call_function` (Impact: 3.2)
  * `_decorator` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 44`, `args: 22`, `func_start: 22`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `duplicate_logic: 8`, `orphaned_logic: 14`
* *Architecture:* `api: 22`, `import: 4`
* *Defense:* `safety: 6`, `doc: 6`, `test: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inspect, unittest, wrapt, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `wrapt-2.1.2/tests/core/test_function_wrapper.py` (PYTHON) | Magnitude: 320.36 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 367, structural_boundaries: 192, encapsulation: 141, api: 102
- `wrapt-2.1.2/tests/core/test_inner_staticmethod.py` (PYTHON) | Magnitude: 118.54 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 154, encapsulation: 108, structural_boundaries: 72, args: 36
- `wrapt-2.1.2/tests/core/test_adapter.py` (PYTHON) | Magnitude: 106.96 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 117, structural_boundaries: 68, encapsulation: 44, args: 33
- `wrapt-2.1.2/tests/core/test_outer_staticmethod.py` (PYTHON) | Magnitude: 76.74 | Delta: **0.103 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 84, encapsulation: 52, structural_boundaries: 44, args: 22
- `wrapt-2.1.2/src/wrapt/wrappers.py` (PYTHON) | Magnitude: 525.18 | Delta: **0.129 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 521, encapsulation: 468, structural_boundaries: 280, args: 118

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `wrapt-2.1.2/tests/core/test_descriptors_py36.py` (PYTHON) | Magnitude: 19.7 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 14, encapsulation: 12, args: 6
- `wrapt-2.1.2/tests/mypy/mypy_function_wrapper_fn_t3.py` (PYTHON) | Magnitude: 6.16 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 8, doc: 4, safety_bypasses: 3, args: 2
- `wrapt-2.1.2/tests/mypy/mypy_function_wrapper_fn_t5.py` (PYTHON) | Magnitude: 11.56 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, doc: 2, import: 1
- `wrapt-2.1.2/tests/core/compat.py` (PYTHON) | Magnitude: 11.04 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, io: 1, import: 1, explicit_casts: 1
- `wrapt-2.1.2/src/wrapt/proxies.py` (PYTHON) | Magnitude: 278.94 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: encapsulation: 236, indent_spaces: 168, branch: 87, structural_boundaries: 64

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `wrapt-2.1.2/tests/core/test_adapter_py3.py` (PYTHON) | Magnitude: 109.5 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 118, structural_boundaries: 77, encapsulation: 43, args: 35
- `wrapt-2.1.2/tests/mypy/mypy_function_wrapper_cls_t4.py` (PYTHON) | Magnitude: 6.14 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, doc: 4, safety_bypasses: 3, args: 2
- `wrapt-2.1.2/tests/mypy/mypy_synchronized_lock_t1.py` (PYTHON) | Magnitude: 46.08 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 33, api: 15, decorators: 14
- `wrapt-2.1.2/tests/mypy/mypy_post_import_hooks_t1.py` (PYTHON) | Magnitude: 14.82 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 8, doc: 6, args: 4
- `wrapt-2.1.2/tests/mypy/mypy_function_wrapper_cls_t6.py` (PYTHON) | Magnitude: 3.0 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, doc: 4, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `wrapt-2.1.2/tests/core/test_auto_object_proxy.py` (PYTHON) | Magnitude: 132.34 | Delta: **0.353 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 119, structural_boundaries: 54, encapsulation: 44, concurrency: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `wrapt-2.1.2/src/wrapt/_wrappers.c` (C) | Magnitude: 314.72 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 359, state_mutation: 170, pointers: 67, api: 60
- `wrapt-2.1.2/tests/mypy/mypy_patching_primitives_t1.py` (PYTHON) | Magnitude: 9.88 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 12, safety_bypasses: 9, indent_spaces: 6, doc: 4
- `wrapt-2.1.2/tests/core/test_inner_classmethod.py` (PYTHON) | Magnitude: 140.18 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 186, encapsulation: 136, structural_boundaries: 84, args: 42
- `wrapt-2.1.2/tests/core/test_nested_function.py` (PYTHON) | Magnitude: 49.5 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 31, encapsulation: 27, args: 15
- `wrapt-2.1.2/tests/core/test_function.py` (PYTHON) | Magnitude: 37.94 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, encapsulation: 26, structural_boundaries: 23, test: 15

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `wrapt-2.1.2/src/wrapt/importer.py` -> **Severity: 0.08** (Bridge: 0.0009 * Flux: 84.0157%)
- `wrapt-2.1.2/src/wrapt/decorators.py` -> **Severity: 0.011** (Bridge: 0.0003 * Flux: 33.6261%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `wrapt-2.1.2/src/wrapt/_wrappers.c` -> **Severity: 4.669** (Embedded: 0.0533 * Error Risk: 87.6106%)
- `wrapt-2.1.2/src/wrapt/__wrapt__.py` -> **Severity: 4.326** (Embedded: 0.08 * Error Risk: 54.0724%)
- `wrapt-2.1.2/src/wrapt/arguments.py` -> **Severity: 4.039** (Embedded: 0.0446 * Error Risk: 90.4724%)
- `wrapt-2.1.2/src/wrapt/wrappers.py` -> **Severity: 1.987** (Embedded: 0.0533 * Error Risk: 37.2937%)
- `wrapt-2.1.2/src/wrapt/decorators.py` -> **Severity: 1.345** (Embedded: 0.025 * Error Risk: 53.7851%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `wrapt-2.1.2/src/wrapt/wrappers.py` -> **Severity: 3402.316** (Blast Radius: 38.632 * Doc Risk: 88.0699%)
- `wrapt-2.1.2/src/wrapt/__wrapt__.py` -> **Severity: 2301.2** (Blast Radius: 67.195 * Doc Risk: 34.2466%)
- `wrapt-2.1.2/src/wrapt/importer.py` -> **Severity: 1334.673** (Blast Radius: 28.606 * Doc Risk: 46.6571%)
- `wrapt-2.1.2/src/wrapt/__init__.pyi` -> **Severity: 1001.99** (Blast Radius: 10.067 * Doc Risk: 99.5321%)
- `wrapt-2.1.2/src/wrapt/patches.py` -> **Severity: 873.867** (Blast Radius: 11.493 * Doc Risk: 76.0347%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
