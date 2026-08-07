# ARCHITECTURAL_BRIEF: micropython-ulab
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/micropython-ulab` |
| **Timestamp** | `2026-08-07T05:09:49.124886+00:00` |
| **Scan Duration** | `0.57s` |
| **Git Branch** | `master` |
| **Git Commit** | `2a94125bdabe02144875abe1dd5665acbba95620` |
| **Git Remote** | `https://github.com/v923z/micropython-ulab` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 170 malicious artifacts.

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
| Total Artifacts | 333 |
| Analyzed Artifacts (Scanned) | 174 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 159 |
| Total LOC | 16320 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 52.3% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7213 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.126 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7143 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 13 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 103 | 3225 | 59.2% |
| C | 66 | 13059 | 37.9% |
| MARKDOWN | 2 | 0 | 1.1% |
| PLAINTEXT | 2 | 0 | 1.1% |
| MAKEFILE | 1 | 36 | 0.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.086`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 112 | 64.4% |
| file_cluster_13 | 56 | 32.2% |
| file_cluster_11 | 2 | 1.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 2.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 159*

**Composition by Extension & Reason:**
- `.exp`: 88x Excluded (Unsupported Extension: '.exp'), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.exp)
- `.ipynb`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tpl`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cmake`: 1x Excluded (Unsupported Extension: '.cmake')
- `.bat`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 2.6 | 95.7 | 23.4 | 5.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 48.0 | 56.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 6.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 6.5 | 0.0 | 0.0 |
| API Exposure | 0.0 | 15.8 | 3.5 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 41.0 | 0.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 26.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 23.5 | 0.8 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 85.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 6.9 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 3.9 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 27.2 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `run-tests` (Hits: 30)
- `code/numpy/io/io.c` (Hits: 11)
- `tests/2d/numpy/savetxt.py` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **ndarray.h** (`code/ndarray.h`) — 8 inbound connections
2. **ulab.h** (`code/ulab.h`) — 6 inbound connections
3. **numerical.h** (`code/numpy/numerical.h`) — 3 inbound connections
4. **ulab_tools.h** (`code/ulab_tools.h`) — 3 inbound connections
5. **ndarray_operators.h** (`code/ndarray_operators.h`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **numpy.c** (`code/numpy/numpy.c`) — 19 outbound dependencies
2. **ulab.c** (`code/ulab.c`) — 18 outbound dependencies
3. **ndarray.c** (`code/ndarray.c`) — 15 outbound dependencies
4. **transform.c** (`code/numpy/transform.c`) — 13 outbound dependencies
5. **run-tests** (`run-tests`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `iirfilter` (@ `snippets/scipy/signal/filter_design.py`) -> Impact: **426.9** | LOC: 633
- `ndarray_copy_view_convert_type` (@ `code/ndarray.c`) -> Impact: **363.5** | LOC: 990
- `run_micropython` (@ `run-tests`) -> Impact: **329.7** | LOC: 512
- `ndarray_binary_more` (@ `code/ndarray_operators.c`) -> Impact: **120.1** | LOC: 142
- `ndarray_binary_logical` (@ `code/ndarray_operators.c`) -> Impact: **114.2** | LOC: 184
- `io_load` (@ `code/numpy/io/io.c`) -> Impact: **113.1** | LOC: 183
- `ndarray_binary_op` (@ `code/ndarray.c`) -> Impact: **107.8** | LOC: 295
- `ndarray_binary_equality` (@ `code/ndarray_operators.c`) -> Impact: **90.2** | LOC: 125
  * *Intent:* * * https://github.com/v923z/micropython-ulab * * The MIT License (MIT) * * Copyright (c) 2020-2021 Zoltán Vörös */ #include <math.h> #include "py/run...
- `io_loadtxt` (@ `code/numpy/io/io.c`) -> Impact: **87.4** | LOC: 154
- `ndarray_assign_from_boolean_index` (@ `code/ndarray.c`) -> Impact: **71.6** | LOC: 112

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `code` | 11 | 6743.98 | 62.33% | 19.66% |
| `code/numpy` | 22 | 6600.68 | 49.99% | 4.58% |
| `code/numpy/carray` | 4 | 1540.74 | 41.89% | 29.41% |
| `code/numpy/linalg` | 4 | 1106.3 | 39.67% | 13.61% |
| `code/numpy/io` | 2 | 817.56 | 42.07% | 6.83% |
| `tests/2d/numpy` | 46 | 695.92 | 6.53% | 0.0% |
| `code/utils` | 2 | 540.24 | 42.65% | 0.0% |
| `snippets/scipy/signal` | 2 | 505.54 | 9.14% | 6.01% |
| `code/numpy/fft` | 4 | 407.66 | 30.04% | 3.6% |
| `code/scipy/optimize` | 2 | 340.0 | 38.95% | 15.85% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `code/numpy/carray/carray_tools.c` -> **99.9881%** Exposure
- `code/ulab_tools.c` -> **99.7847%** Exposure
- `snippets/numpy/core/fromnumeric.py` -> **96.9302%** Exposure
- `code/numpy/ndarray/ndarray_iter.h` -> **95.5022%** Exposure
- `code/numpy/ndarray/ndarray_iter.c` -> **93.7517%** Exposure
### Highest State Flux (Mutation/Volatility)
- `code/micropython.mk` -> **100.0%** Exposure
- `code/ndarray.c` -> **100.0%** Exposure
- `code/ndarray.h` -> **100.0%** Exposure
- `code/ndarray_operators.c` -> **100.0%** Exposure
- `code/ndarray_operators.h` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `code/ndarray.c` -> **21** Orphaned Functions | **0** Duplicates
- `code/ndarray_operators.c` -> **14** Orphaned Functions | **0** Duplicates
- `code/ulab_tools.c` -> **10** Orphaned Functions | **0** Duplicates
- `code/numpy/carray/carray.c` -> **6** Orphaned Functions | **0** Duplicates
- `code/scipy/optimize/optimize.c` -> **3** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`code/ndarray.c`** -> AI Confidence: **99.48%**
2. **`code/ndarray_operators.c`** -> AI Confidence: **99.48%**
3. **`code/ndarray_properties.c`** -> AI Confidence: **99.48%**
4. **`code/ndarray_properties.h`** -> AI Confidence: **99.48%**
5. **`code/numpy/approx.c`** -> AI Confidence: **99.48%**
6. **`code/numpy/bitwise.c`** -> AI Confidence: **99.48%**
7. **`code/numpy/carray/carray.c`** -> AI Confidence: **99.48%**
8. **`code/numpy/compare.c`** -> AI Confidence: **99.48%**
9. **`code/numpy/create.c`** -> AI Confidence: **99.48%**
10. **`code/numpy/fft/fft_tools.c`** -> AI Confidence: **99.48%**
11. **`code/numpy/filter.c`** -> AI Confidence: **99.48%**
12. **`code/numpy/io/io.c`** -> AI Confidence: **99.48%**
13. **`code/numpy/linalg/linalg.c`** -> AI Confidence: **99.48%**
14. **`code/numpy/numerical.c`** -> AI Confidence: **99.48%**
15. **`code/numpy/numpy.c`** -> AI Confidence: **99.48%**
16. **`code/numpy/poly.c`** -> AI Confidence: **99.48%**
17. **`code/numpy/transform.c`** -> AI Confidence: **99.48%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `522` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `code/ulab_tools.c` (C) -> Cumulative Risk: **677.98**
- **Archetype:** `file_cluster_13` (Distance: 12.325 IQR)
- **Magnitude:** 278.62 | **LOC:** 332 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9996%), Tech Debt (99.7847%), Documentation (99.707%)
- **Heaviest Functions:** `ndarray_upcast_dtype` (Impact: 25.5), `ulab_tools_restore_dims` (Impact: 24.0), `ndarray_get_float_index` (Impact: 18.7)

### 2. `code/ndarray.c` (C) -> Cumulative Risk: **666.97**
- **Archetype:** `file_cluster_11` (Distance: 15.537 IQR)
- **Magnitude:** 2538.6 | **LOC:** 2118 | **CtrlFlow:** 80.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.7761%)
- **Heaviest Functions:** `ndarray_copy_view_convert_type` (Impact: 363.5), `ndarray_binary_op` (Impact: 107.8), `ndarray_assign_from_boolean_index` (Impact: 71.6)

### 3. `code/numpy/compare.c` (C) -> Cumulative Risk: **600.42**
- **Archetype:** `file_cluster_13` (Distance: 14.548 IQR)
- **Magnitude:** 868.94 | **LOC:** 774 | **CtrlFlow:** 85.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.5865%)
- **Heaviest Functions:** `compare_function` (Impact: 67.0), `compare_bincount` (Impact: 43.2), `compare_nonzero` (Impact: 39.2)

### 4. `code/ndarray_operators.c` (C) -> Cumulative Risk: **596.1**
- **Archetype:** `file_cluster_8` (Distance: 13.303 IQR)
- **Magnitude:** 1460.88 | **LOC:** 1246 | **CtrlFlow:** 93.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (95.0342%), Safety Score (91.8934%)
- **Heaviest Functions:** `ndarray_binary_more` (Impact: 120.1), `ndarray_binary_logical` (Impact: 114.2), `ndarray_binary_equality` (Impact: 90.2)

### 5. `code/numpy/carray/carray.c` (C) -> Cumulative Risk: **595.39**
- **Archetype:** `file_cluster_13` (Distance: 15.108 IQR)
- **Magnitude:** 1199.26 | **LOC:** 835 | **CtrlFlow:** 91.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.5576%), Documentation (99.3384%)
- **Heaviest Functions:** `carray_binary_subtract` (Impact: 44.1), `carray_binary_equal_not_equal` (Impact: 35.9), `carray_binary_add` (Impact: 35.1)

### 6. `code/numpy/ndarray/ndarray_iter.c` (C) -> Cumulative Risk: **589.86**
- **Archetype:** `file_cluster_13` (Distance: 13.274 IQR)
- **Magnitude:** 68.96 | **LOC:** 67 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9834%), Safety Score (95.2574%)
- **Heaviest Functions:** `ndarray_flatiter_next` (Impact: 5.0), `ndarray_new_flatiterator` (Impact: 1.5), `ndarray_flatiter_make_new` (Impact: 1.4)

### 7. `code/numpy/numerical.c` (C) -> Cumulative Risk: **587.79**
- **Archetype:** `file_cluster_13` (Distance: 15.255 IQR)
- **Magnitude:** 1889.6 | **LOC:** 1430 | **CtrlFlow:** 84.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.907%), Safety Score (98.4663%)
- **Heaviest Functions:** `numerical_all_any` (Impact: 70.6), `numerical_sum_mean_std_ndarray` (Impact: 55.4), `numerical_roll` (Impact: 50.0)

### 8. `code/numpy/io/io.c` (C) -> Cumulative Risk: **586.37**
- **Archetype:** `file_cluster_13` (Distance: 14.72 IQR)
- **Magnitude:** 803.92 | **LOC:** 807 | **CtrlFlow:** 90.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.4552%), Documentation (97.3746%)
- **Heaviest Functions:** `io_load` (Impact: 113.1), `io_loadtxt` (Impact: 87.4), `io_sprintf` (Impact: 13.4)

### 9. `code/numpy/bitwise.c` (C) -> Cumulative Risk: **573.86**
- **Archetype:** `file_cluster_8` (Distance: 13.767 IQR)
- **Magnitude:** 530.86 | **LOC:** 431 | **CtrlFlow:** 89.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (97.7136%), Safety Score (95.8244%)
- **Heaviest Functions:** `bitwise_left_shift_loop` (Impact: 35.2), `bitwise_right_shift_loop` (Impact: 35.2), `bitwise_binary_operators` (Impact: 33.2)

### 10. `code/utils/utils.c` (C) -> Cumulative Risk: **564.98**
- **Archetype:** `file_cluster_13` (Distance: 14.591 IQR)
- **Magnitude:** 526.12 | **LOC:** 415 | **CtrlFlow:** 89.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.0473%), Documentation (89.9957%)
- **Heaviest Functions:** `utils_spectrogram` (Impact: 54.6), `utils_from_intbuffer_helper` (Impact: 50.4), `utils_from_int16_buffer` (Impact: 1.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `code/ndarray.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.537 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 6.038 IQR)
- **Top Global Matches:** file_cluster_11: 15.537, file_cluster_0: 15.596, file_cluster_13: 15.596
- **Magnitude:** 2538.6 | **LOC:** 2118 | **CtrlFlow:** 80.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (95.7481%), Tech Debt (51.128%)
**Top Internal Functions/Classes:**
  * `ndarray_copy_view_convert_type` (Impact: 363.5)
  * `ndarray_binary_op` (Impact: 107.8)
  * `ndarray_assign_from_boolean_index` (Impact: 71.6)
  * `ndarray_print` (Impact: 38.2)
  * `ndarray_from_mp_obj` (Impact: 30.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 465`, `structural_boundaries: 110`, `args: 2`, `func_start: 60`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 1266`, `dead_code: 12`, `planned_debt: 4`, `orphaned_logic: 21`
* *Architecture:* `api: 294`, `import: 15`
* *Defense:* `safety: 81`, `test: 1`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` math.h, runtime.h, binary.h, ulab_tools.h, unistd.h, objtuple.h, obj.h, carray.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/numerical.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.255 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.967 IQR)
- **Top Global Matches:** file_cluster_13: 15.255, file_cluster_11: 15.265, file_cluster_0: 15.293
- **Magnitude:** 1889.6 | **LOC:** 1430 | **CtrlFlow:** 84.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.6243%), Tech Debt (8.575%)
**Top Internal Functions/Classes:**
  * `numerical_all_any` (Impact: 70.6)
  * `numerical_sum_mean_std_ndarray` (Impact: 55.4)
  * `numerical_roll` (Impact: 50.0)
    * *Intent:* #endif
  * `numerical_cross` (Impact: 49.9)
  * `numerical_argmin_argmax_ndarray` (Impact: 44.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 399`, `structural_boundaries: 71`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 1147`, `dead_code: 4`, `planned_debt: 2`
* *Architecture:* `api: 258`, `import: 12`
* *Defense:* `safety: 75`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` math.h, runtime.h, ulab.h, obj.h, objint.h, numerical.h, carray_tools.h, misc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/ndarray_operators.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.303 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.217 IQR)
- **Top Global Matches:** file_cluster_8: 13.303, file_cluster_13: 13.556, file_cluster_0: 13.666
- **Magnitude:** 1460.88 | **LOC:** 1246 | **CtrlFlow:** 93.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.1533%), Tech Debt (22.6715%)
**Top Internal Functions/Classes:**
  * `ndarray_binary_more` (Impact: 120.1)
  * `ndarray_binary_logical` (Impact: 114.2)
  * `ndarray_binary_equality` (Impact: 90.2)
    * *Intent:* * * https://github.com/v923z/micropython-ulab * * The MIT License (MIT) * * Copyright (c) 2020-2021 ...
  * `ndarray_binary_true_divide` (Impact: 64.5)
  * `ndarray_binary_subtract` (Impact: 63.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 716`, `structural_boundaries: 53`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 554`, `dead_code: 1`, `orphaned_logic: 14`
* *Architecture:* `api: 112`, `import: 8`
* *Defense:* `safety: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` math.h, runtime.h, ulab_tools.h, objtuple.h, carray.h, ndarray.h, ulab.h, ndarray_operators.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/carray/carray.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.108 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 6.371 IQR)
- **Top Global Matches:** file_cluster_13: 15.108, file_cluster_8: 15.199, file_cluster_11: 15.233
- **Magnitude:** 1199.26 | **LOC:** 835 | **CtrlFlow:** 91.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.622%), Tech Debt (17.6347%)
**Top Internal Functions/Classes:**
  * `carray_binary_subtract` (Impact: 44.1)
    * *Intent:* // align the complex array to the left
  * `carray_binary_equal_not_equal` (Impact: 35.9)
  * `carray_binary_add` (Impact: 35.1)
  * `carray_binary_divide` (Impact: 33.7)
  * `carray_binary_multiply` (Impact: 23.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 21`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 782`, `dead_code: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 127`, `import: 12`
* *Defense:* `safety: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` math.h, runtime.h, obj.h, ulab_tools.h, objint.h, ulab.h, carray.h, misc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/ndarray.h` (C | Tier 0 | 🚨 AI THREAT: 99.28%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.064 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.617 IQR)
- **Top Global Matches:** file_cluster_11: 16.064, file_cluster_8: 16.132, file_cluster_0: 16.136
- **Magnitude:** 1106.48 | **LOC:** 809 | **CtrlFlow:** 84.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (76.714%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 29`, `args: 4`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 923`, `dead_code: 1`
* *Architecture:* `api: 155`, `import: 5`
* *Defense:* `safety: 94`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 27.827
  * `Choke Point (Betweenness):` 0.000101 | `Ripple Effect (Closeness):` 0.046243
  * `Imports (Out-Degree: 1):` objlist.h, binary.h, objarray.h, objstr.h, ulab.h
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `code/ndarray_operators.h` (C | Tier 0 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.551 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.917 IQR)
- **Top Global Matches:** file_cluster_8: 15.551, file_cluster_11: 15.736, file_cluster_0: 15.762
- **Magnitude:** 1022.22 | **LOC:** 714 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.3783%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 211`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 907`
* *Architecture:* `api: 87`, `import: 1`
* *Defense:* `safety: 65`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.156
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011561
  * `Imports (Out-Degree: 1):` ndarray.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `code/numpy/compare.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.548 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 6.17 IQR)
- **Top Global Matches:** file_cluster_13: 14.548, file_cluster_11: 14.683, file_cluster_0: 14.702
- **Magnitude:** 868.94 | **LOC:** 774 | **CtrlFlow:** 85.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (81.6195%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `compare_function` (Impact: 67.0)
  * `compare_bincount` (Impact: 43.2)
    * *Intent:* * * https://github.com/v923z/micropython-ulab * * The MIT License (MIT) * * Copyright (c) 2020-2025 ...
  * `compare_nonzero` (Impact: 39.2)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_ISINF //| def isinf(x: _ScalarOrNdArray) -> Union[_bool, ulab.numpy.ndarra...
  * `compare_where` (Impact: 29.4)
  * `compare_isinf_isfinite` (Impact: 21.4)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_EQUAL //| def equal(x: _ScalarOrArrayLike, y: _ScalarOrArrayLike) -> _Scal...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 33`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 513`, `dead_code: 2`
* *Architecture:* `api: 115`, `import: 11`
* *Defense:* `safety: 22`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` runtime.h, math.h, carray_tools.h, ulab.h, obj.h, ndarray_operators.h, misc.h, ulab_tools.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/linalg/linalg.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.72 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 6.01 IQR)
- **Top Global Matches:** file_cluster_13: 15.72, file_cluster_11: 15.814, file_cluster_0: 15.867
- **Magnitude:** 824.6 | **LOC:** 543 | **CtrlFlow:** 87.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.9563%), Tech Debt (9.5623%)
**Top Internal Functions/Classes:**
  * `linalg_qr` (Impact: 32.0)
  * `linalg_norm` (Impact: 27.2)
  * `linalg_cholesky` (Impact: 17.8)
    * *Intent:* #include <stdlib.h> #include <string.h> #include <math.h> #include "py/obj.h" #include "py/runtime.h...
  * `linalg_det` (Impact: 16.9)
  * `linalg_eig` (Impact: 10.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 14`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 631`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 76`, `import: 10`
* *Defense:* `safety: 48`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` runtime.h, math.h, obj.h, ulab_tools.h, carray_tools.h, ulab.h, misc.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/io/io.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.72 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.912 IQR)
- **Top Global Matches:** file_cluster_13: 14.72, file_cluster_11: 14.915, file_cluster_0: 14.95
- **Magnitude:** 803.92 | **LOC:** 807 | **CtrlFlow:** 90.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.1391%), Tech Debt (13.6599%)
**Top Internal Functions/Classes:**
  * `io_load` (Impact: 113.1)
  * `io_loadtxt` (Impact: 87.4)
  * `io_sprintf` (Impact: 13.4)
  * `io_save` (Impact: 12.2)
  * `io_assign_value` (Impact: 10.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 13`, `args: 13`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 485`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 11`, `api: 68`, `import: 12`
* *Defense:* `safety: 15`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` math.h, runtime.h, obj.h, stream.h, ulab_tools.h, io.h, vfs.h, builtin.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/numerical.h` (C | Tier 0 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.23 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.412 IQR)
- **Top Global Matches:** file_cluster_8: 15.23, file_cluster_11: 15.327, file_cluster_0: 15.429
- **Magnitude:** 746.38 | **LOC:** 524 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.536%), Tech Debt (10.1545%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 673`, `planned_debt: 2`
* *Architecture:* `api: 49`, `import: 2`
* *Defense:* `safety: 41`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.253
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.017341
  * `Imports (Out-Degree: 0):` ndarray.h, ulab.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `code/numpy/transform.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.575 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.944 IQR)
- **Top Global Matches:** file_cluster_13: 15.575, file_cluster_11: 15.659, file_cluster_0: 15.727
- **Magnitude:** 590.3 | **LOC:** 457 | **CtrlFlow:** 89.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.8868%), Tech Debt (11.0727%)
**Top Internal Functions/Classes:**
  * `transform_delete` (Impact: 47.9)
  * `transform_compress` (Impact: 33.7)
    * *Intent:* * * The MIT License (MIT) * * Copyright (c) 2019-2021 Zoltán Vörös * */ #include <sys/types.h> #incl...
  * `transform_dot` (Impact: 16.8)
    * *Intent:* #endif /* ULAB_NUMPY_HAS_DELETE */
  * `transform_size` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 10`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 407`, `dead_code: 3`, `planned_debt: 2`
* *Architecture:* `api: 70`, `import: 13`
* *Defense:* `safety: 48`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` math.h, runtime.h, carray_tools.h, ulab.h, unistd.h, obj.h, numerical.h, misc.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/bitwise.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.767 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.616 IQR)
- **Top Global Matches:** file_cluster_8: 13.767, file_cluster_13: 13.817, file_cluster_11: 14.032
- **Magnitude:** 530.86 | **LOC:** 431 | **CtrlFlow:** 89.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.8794%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bitwise_left_shift_loop` (Impact: 35.2)
  * `bitwise_right_shift_loop` (Impact: 35.2)
  * `bitwise_binary_operators` (Impact: 33.2)
  * `bitwise_bitwise_and_loop` (Impact: 29.7)
    * *Intent:* /* * This file is part of the micropython-ulab project, * * https://github.com/v923z/micropython-ula...
  * `bitwise_bitwise_or_loop` (Impact: 29.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 20`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 267`
* *Architecture:* `api: 58`, `import: 7`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` math.h, runtime.h, obj.h, stdio.h, bitwise.h, string.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/utils/utils.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.591 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.831 IQR)
- **Top Global Matches:** file_cluster_13: 14.591, file_cluster_8: 14.77, file_cluster_11: 14.789
- **Magnitude:** 526.12 | **LOC:** 415 | **CtrlFlow:** 89.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.2925%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `utils_spectrogram` (Impact: 54.6)
    * *Intent:* #endif #endif /* ULAB_UTILS_HAS_FROM_INT16_BUFFER | ULAB_UTILS_HAS_FROM_UINT16_BUFFER | ULAB_UTILS_H...
  * `utils_from_intbuffer_helper` (Impact: 50.4)
    * *Intent:* #include <math.h> #include <stdlib.h> #include <string.h> #include "py/obj.h" #include "py/runtime.h...
  * `utils_from_int16_buffer` (Impact: 1.1)
  * `utils_from_uint16_buffer` (Impact: 1.1)
    * *Intent:* #ifdef ULAB_UTILS_HAS_FROM_INT16_BUFFER
  * `utils_from_int32_buffer` (Impact: 1.1)
    * *Intent:* #endif #ifdef ULAB_UTILS_HAS_FROM_UINT16_BUFFER
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 11`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 372`, `dead_code: 1`
* *Architecture:* `api: 38`, `import: 9`
* *Defense:* `safety: 21`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` runtime.h, math.h, utils.h, obj.h, fft_tools.h, misc.h, ulab_tools.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `snippets/scipy/signal/filter_design.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.36 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.789 IQR)
- **Top Global Matches:** file_cluster_8: 10.36, file_cluster_7: 10.69, file_cluster_13: 10.713
- **Magnitude:** 495.02 | **LOC:** 1480 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.289%), Tech Debt (12.0169%)
**Top Internal Functions/Classes:**
  * `iirfilter` (Impact: 426.9)
  * `fft` (Impact: 7.3)
    * *Intent:* """ # TODO in the near future: # 1. Add SOS capability to `filtfilt`, `freqz`, etc. somehow (#3259)....
  * `buttap` (Impact: 6.0)
  * `butter` (Impact: 2.9)
  * `butter_bandpass_filter` (Impact: 2.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 77`, `args: 23`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 21`, `dead_code: 2`, `planned_debt: 4`
* *Architecture:* `api: 16`, `import: 5`
* *Defense:* `safety: 17`, `doc: 30`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ulab, math, ...numpy, scipy, matplotlib.pyplot
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/vector.h` (C | Tier 0 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.891 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.642 IQR)
- **Top Global Matches:** file_cluster_8: 14.891, file_cluster_13: 15.083, file_cluster_11: 15.092
- **Magnitude:** 375.66 | **LOC:** 320 | **CtrlFlow:** 95.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.677%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 326`
* *Architecture:* `api: 29`, `import: 2`
* *Defense:* `safety: 27`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011561
  * `Imports (Out-Degree: 0):` ndarray.h, ulab.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `code/numpy/fft/fft_tools.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.924 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.487 IQR)
- **Top Global Matches:** file_cluster_13: 14.924, file_cluster_11: 15.032, file_cluster_8: 15.096
- **Magnitude:** 349.78 | **LOC:** 267 | **CtrlFlow:** 88.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.2508%), Tech Debt (14.402%)
**Top Internal Functions/Classes:**
  * `fft_fft_ifft` (Impact: 16.4)
  * `fft_kernel` (Impact: 10.2)
    * *Intent:* */ #include <math.h> #include <string.h> #include "py/runtime.h" #include "../../ndarray.h" #include...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 6`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 292`, `planned_debt: 2`
* *Architecture:* `api: 27`, `import: 7`
* *Defense:* `safety: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` math.h, runtime.h, ulab_tools.h, carray_tools.h, fft_tools.h, string.h, ndarray.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/scipy/linalg/linalg.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.637 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 6.621 IQR)
- **Top Global Matches:** file_cluster_13: 14.637, file_cluster_8: 14.951, file_cluster_11: 15.007
- **Magnitude:** 325.04 | **LOC:** 282 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.7672%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `solve_triangular` (Impact: 17.9)
    * *Intent:* #include "py/runtime.h" #include "py/misc.h" #include "../../ulab.h" #include "../../ulab_tools.h" #...
  * `cho_solve` (Impact: 15.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 8`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 251`
* *Architecture:* `api: 37`, `import: 10`
* *Defense:* `safety: 10`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` runtime.h, math.h, obj.h, ulab_tools.h, ulab.h, linalg_tools.h, misc.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/scipy/optimize/optimize.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.592 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.585 IQR)
- **Top Global Matches:** file_cluster_13: 13.592, file_cluster_8: 13.724, file_cluster_11: 13.978
- **Magnitude:** 323.54 | **LOC:** 418 | **CtrlFlow:** 88.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.3182%), Tech Debt (31.7058%)
**Top Internal Functions/Classes:**
  * `optimize_fmin` (Impact: 25.5)
  * `optimize_bisect` (Impact: 12.2)
    * *Intent:* #if ULAB_SCIPY_OPTIMIZE_HAS_BISECT //| def bisect(
  * `optimize_jacobi` (Impact: 6.0)
  * `optimize_python_call` (Impact: 1.4)
    * *Intent:* * This file is part of the micropython-ulab project, * * https://github.com/v923z/micropython-ulab *...
  * `optimize_curve_fit` (Impact: 1.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 229`, `orphaned_logic: 3`
* *Architecture:* `api: 43`, `import: 8`
* *Defense:* `safety: 3`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` math.h, runtime.h, optimize.h, obj.h, ulab_tools.h, ulab.h, misc.h, ndarray.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/carray/carray.h` (C | Tier 0 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.245 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.589 IQR)
- **Top Global Matches:** file_cluster_8: 15.245, file_cluster_11: 15.452, file_cluster_0: 15.46
- **Magnitude:** 321.0 | **LOC:** 238 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.9303%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`
* *Risk/State:* `state_mutation: 275`
* *Architecture:* `api: 27`
* *Defense:* `safety: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.85
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00578
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `code/numpy/vector.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.31 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.942 IQR)
- **Top Global Matches:** file_cluster_13: 13.31, file_cluster_8: 13.348, file_cluster_11: 13.568
- **Magnitude:** 319.12 | **LOC:** 979 | **CtrlFlow:** 81.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.0976%), Tech Debt (9.7372%)
**Top Internal Functions/Classes:**
  * `vector_sqrt` (Impact: 25.2)
    * *Intent:* *narray++ = MICROPY_FLOAT_C_FUN(round)(f * mul) / mul;
  * `vector_vectorized_function_call` (Impact: 13.2)
  * `vector_vectorize` (Impact: 12.7)
  * `vector_sinc1` (Impact: 2.4)
  * `vector_radians_` (Impact: 1.1)
    * *Intent:* #endif /* ULAB_MATH_FUNCTIONS_OUT_KEYWORD */ #endif /* ULAB_NUMPY_HAS_ACOS */ #if ULAB_NUMPY_HAS_ACO...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 22`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 182`, `planned_debt: 1`
* *Architecture:* `api: 73`, `import: 11`
* *Defense:* `safety: 10`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` math.h, runtime.h, binary.h, ulab.h, objarray.h, carray_tools.h, obj.h, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/poly.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.463 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.687 IQR)
- **Top Global Matches:** file_cluster_13: 14.463, file_cluster_11: 14.668, file_cluster_8: 14.732
- **Magnitude:** 300.4 | **LOC:** 219 | **CtrlFlow:** 86.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.0249%), Tech Debt (16.9256%)
**Top Internal Functions/Classes:**
  * `poly_polyfit` (Impact: 27.8)
    * *Intent:* /* * This file is part of the micropython-ulab project, * * https://github.com/v923z/micropython-ula...
  * `poly_polyval` (Impact: 12.9)
    * *Intent:* #endif
  * `poly_eval` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 5`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 227`, `planned_debt: 2`
* *Architecture:* `api: 27`, `import: 8`
* *Defense:* `safety: 11`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` runtime.h, carray_tools.h, ulab.h, objarray.h, poly.h, obj.h, linalg_tools.h, ulab_tools.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/ulab_tools.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.325 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.334 IQR)
- **Top Global Matches:** file_cluster_13: 12.325, file_cluster_8: 12.508, file_cluster_11: 12.515
- **Magnitude:** 278.62 | **LOC:** 332 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.9794%), Tech Debt (99.7847%)
**Top Internal Functions/Classes:**
  * `ndarray_upcast_dtype` (Impact: 25.5)
  * `ulab_tools_restore_dims` (Impact: 24.0)
  * `ndarray_get_float_index` (Impact: 18.7)
  * `ndarray_get_float_value` (Impact: 16.3)
  * `ulab_tools_mp_obj_is_scalar` (Impact: 10.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 62`, `args: 12`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 70`, `dead_code: 1`, `planned_debt: 1`, `orphaned_logic: 10`
* *Architecture:* `api: 47`, `import: 5`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` runtime.h, ulab_tools.h, ndarray.h, ulab.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/random/random.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.954 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 6.377 IQR)
- **Top Global Matches:** file_cluster_13: 14.954, file_cluster_11: 15.093, file_cluster_0: 15.099
- **Magnitude:** 273.26 | **LOC:** 362 | **CtrlFlow:** 88.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.603%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `random_random` (Impact: 25.2)
  * `random_uniform` (Impact: 12.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 5`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 193`, `dead_code: 2`
* *Architecture:* `api: 39`, `import: 5`
* *Defense:* `safety: 8`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` math.h, runtime.h, obj.h, random.h, builtin.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/approx.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.129 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 6.55 IQR)
- **Top Global Matches:** file_cluster_13: 14.129, file_cluster_8: 14.448, file_cluster_11: 14.544
- **Magnitude:** 269.12 | **LOC:** 228 | **CtrlFlow:** 85.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.4345%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `approx_interp` (Impact: 23.4)
    * *Intent:* #if ULAB_NUMPY_HAS_INTERP //| def interp( //| x: ulab.numpy.ndarray,
  * `approx_trapz` (Impact: 14.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 5`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 195`
* *Architecture:* `api: 33`, `import: 10`
* *Defense:* `safety: 7`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` runtime.h, math.h, carray_tools.h, ulab.h, approx.h, obj.h, misc.h, ulab_tools.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/linalg/linalg_tools.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.438 IQR)
- **Local Micro-Species:** `Cluster 0: Defensive Downstream Logic & Immutable State` (Drift: 5.322 IQR)
- **Top Global Matches:** file_cluster_13: 15.438, file_cluster_11: 15.619, file_cluster_8: 15.66
- **Magnitude:** 248.18 | **LOC:** 171 | **CtrlFlow:** 82.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.7241%), Tech Debt (44.8577%)
**Top Internal Functions/Classes:**
  * `linalg_jacobi_rotations` (Impact: 21.2)
  * `linalg_invert_matrix` (Impact: 16.8)
    * *Intent:* /* * This file is part of the micropython-ulab project, * * https://github.com/v923z/micropython-ula...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 6`, `func_start: 2`
* *Risk/State:* `state_mutation: 196`, `orphaned_logic: 2`
* *Architecture:* `api: 12`, `import: 4`
* *Defense:* `safety: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` string.h, math.h, runtime.h, linalg_tools.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `code/ndarray.c` (C) | Magnitude: 2538.6 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 1266, indent_spaces: 1190, pointers: 697, branch: 465
- `code/ndarray.h` (C) | Magnitude: 1106.48 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 923, indent_spaces: 463, pointers: 328, branch: 163

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/2d/numpy/size.py` (PYTHON) | Magnitude: 14.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, debug_prints: 3, safety: 2, scientific: 2
- `code/numpy/numerical.c` (C) | Magnitude: 1889.6 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 1147, indent_spaces: 1002, pointers: 464, branch: 399
- `tests/2d/numpy/linspace.py` (PYTHON) | Magnitude: 14.16 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 4, branch: 2, safety: 2
- `code/numpy/numpy.h` (C) | Magnitude: 14.12 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: import: 2, macros: 2, api: 1, ownership: 1
- `code/scipy/scipy.h` (C) | Magnitude: 14.12 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: import: 2, macros: 2, api: 1, ownership: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `code/ulab.c` (C) | Magnitude: 104.98 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 108, macros: 86, state_mutation: 76, branch: 40
- `code/numpy/compare.h` (C) | Magnitude: 202.56 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 168, indent_spaces: 97, pointers: 39, branch: 32
- `tests/1d/numpy/00smoke.py` (PYTHON) | Magnitude: 11.04 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, scientific: 1, import: 1, debug_prints: 1
- `tests/2d/numpy/00smoke.py` (PYTHON) | Magnitude: 11.04 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, scientific: 1, import: 1, debug_prints: 1
- `tests/3d/numpy/create.py` (PYTHON) | Magnitude: 11.04 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, scientific: 1, import: 1, debug_prints: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `code/ulab.c` -> Churn: **100.0%** | Cog Load: 73.9857% | Debt: 11.9467%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `code/ndarray.c` -> **Zoltán Vörös** (100.0% isolated ownership) | Magnitude: 2538.6
- `code/ndarray.h` -> **Zoltán Vörös** (100.0% isolated ownership) | Magnitude: 1106.48
- `code/numpy/compare.c` -> **Zoltán Vörös** (100.0% isolated ownership) | Magnitude: 868.94
- `code/numpy/compare.h` -> **Zoltán Vörös** (100.0% isolated ownership) | Magnitude: 202.56
- `code/ndarray_properties.c` -> **Zoltán Vörös** (100.0% isolated ownership) | Magnitude: 98.68

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `code/ndarray.h` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `code/ndarray.h` -> **Severity: 4.584** (Embedded: 0.0462 * Error Risk: 99.1388%)
- `code/numpy/numerical.h` -> **Severity: 1.727** (Embedded: 0.0173 * Error Risk: 99.571%)
- `code/ndarray_operators.h` -> **Severity: 1.149** (Embedded: 0.0116 * Error Risk: 99.3732%)
- `code/numpy/compare.h` -> **Severity: 1.145** (Embedded: 0.0116 * Error Risk: 99.0356%)
- `code/numpy/vector.h` -> **Severity: 1.135** (Embedded: 0.0116 * Error Risk: 98.1873%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `code/ndarray.h` -> **Severity: 2782.7** (Blast Radius: 27.827 * Doc Risk: 100.0%)
- `code/numpy/fft/fft_tools.h` -> **Severity: 1505.376** (Blast Radius: 16.373 * Doc Risk: 91.9426%)
- `code/numpy/numerical.h` -> **Severity: 991.953** (Blast Radius: 11.253 * Doc Risk: 88.1501%)
- `code/numpy/compare.h` -> **Severity: 922.0** (Blast Radius: 9.22 * Doc Risk: 100.0%)
- `code/numpy/create.h` -> **Severity: 922.0** (Blast Radius: 9.22 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
