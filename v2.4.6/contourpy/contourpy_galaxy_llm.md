# ARCHITECTURAL_BRIEF: contourpy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/contourpy` |
| **Timestamp** | `2026-08-03T21:20:02.309503+00:00` |
| **Scan Duration** | `0.67s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 75 malicious artifacts.

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
| Total Artifacts | 143 |
| Analyzed Artifacts (Scanned) | 80 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 63 |
| Total LOC | 11047 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 55.9% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5897 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3152 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.8609 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 43 | 5344 | 53.8% |
| CPP | 32 | 5679 | 40.0% |
| MARKDOWN | 3 | 0 | 3.8% |
| JSON | 1 | 24 | 1.2% |
| PLAINTEXT | 1 | 0 | 1.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.245`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 31 | 38.8% |
| file_cluster_13 | 18 | 22.5% |
| file_cluster_16 | 18 | 22.5% |
| file_cluster_0 | 8 | 10.0% |
| file_cluster_4 | 1 | 1.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 5.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 63*

**Composition by Extension & Reason:**
- `.png`: 52x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.build`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.4 | 30.0 | 8.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 22.3 | 2.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 33.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 11.8 | 2.3 | 0.0 |
| API Exposure | 0.0 | 12.4 | 3.3 | 2.5 | 0.0 |
| Concurrency Exposure | 0.0 | 93.4 | 1.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 39.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 17.4 | 0.7 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 96.8 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 48.4 | 46.6 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 34.2 | 14.5 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 17.9 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `contourpy-1.3.3/tests/image_comparison.py` (Hits: 12)
- `contourpy-1.3.3/tests/test_bokeh_renderer.py` (Hits: 2)
- `contourpy-1.3.3/tests/test_renderer.py` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **bench_base.py** (`contourpy-1.3.3/benchmarks/benchmarks/bench_base.py`) — 16 inbound connections
2. **util_bench.py** (`contourpy-1.3.3/benchmarks/benchmarks/util_bench.py`) — 16 inbound connections
3. **image_comparison.py** (`contourpy-1.3.3/tests/image_comparison.py`) — 5 inbound connections
4. **common.h** (`contourpy-1.3.3/src/common.h`) — 5 inbound connections
5. **contour_generator.h** (`contourpy-1.3.3/src/contour_generator.h`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_bokeh_renderer.py** (`contourpy-1.3.3/tests/test_bokeh_renderer.py`) — 17 outbound dependencies
2. **test_filled.py** (`contourpy-1.3.3/tests/test_filled.py`) — 14 outbound dependencies
3. **util_config.py** (`contourpy-1.3.3/tests/util_config.py`) — 13 outbound dependencies
4. **loader.py** (`contourpy-1.3.3/benchmarks/loader.py`) — 12 outbound dependencies
5. **test_lines.py** (`contourpy-1.3.3/tests/test_lines.py`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `get_style` (@ `contourpy-1.3.3/benchmarks/plot_benchmarks.py`) -> Impact: **1530.8** | LOC: 306
  * *Intent:* # Colors from Paul Tol's colorblind friendly light scheme (https://personal.sron.nl/~pault) colors = { "mpl2005": "#eedd88", # light yellow. "mpl2014"...
- `Mpl2014ContourGenerator::follow_interior` (@ `contourpy-1.3.3/src/mpl2014.cpp`) -> Impact: **921.0** | LOC: 149
- `Mpl2014ContourGenerator::single_quad_fil` (@ `contourpy-1.3.3/src/mpl2014.cpp`) -> Impact: **680.2** | LOC: 187
- `__init__` (@ `contourpy-1.3.3/tests/util_config.py`) -> Impact: **677.3** | LOC: 85
- `Mpl2014ContourGenerator::follow_boundary` (@ `contourpy-1.3.3/src/mpl2014.cpp`) -> Impact: **553.7** | LOC: 120
- `data_init` (@ `contourpy-1.3.3/src/mpl2005_original.cpp`) -> Impact: **470.6** | LOC: 178
  * *Intent:* /* Saddle zone array consists of the following bits: * SADDLE_SET whether zone's saddle data has been set. * SADDLE_GT0 whether z of centre of zone is...
- `Mpl2014ContourGenerator::init_cache_grid` (@ `contourpy-1.3.3/src/mpl2014.cpp`) -> Impact: **459.8** | LOC: 96
- `Mpl2014ContourGenerator::lines` (@ `contourpy-1.3.3/src/mpl2014.cpp`) -> Impact: **368.0** | LOC: 86
- `Mpl2014ContourGenerator::move_to_next_bo` (@ `contourpy-1.3.3/src/mpl2014.cpp`) -> Impact: **341.2** | LOC: 105
- `Mpl2014ContourGenerator::get_exit_edge` (@ `contourpy-1.3.3/src/mpl2014.cpp`) -> Impact: **293.5** | LOC: 51

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `get_style` (@ `contourpy-1.3.3/benchmarks/plot_benchmarks.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Colors from Paul Tol's colorblind friendly light scheme (https://personal.sron.nl/~pault) colors = { "mpl2005": "#eedd88", # light yellow. "mpl2014"...
- `__init__` (@ `contourpy-1.3.3/tests/util_config.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `contourpy-1.3.3/tests/util_config.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `contourpy-1.3.3/tests/util_config.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `contourpy-1.3.3/tests/util_config.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # All 4 corners plotted together.
- `driver` (@ `contourpy-1.3.3/tests/test_bokeh_renderer.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Based on Bokeh's tests/support/plugins/selenium.py def chrome() -> WebDriver: from selenium.webdriver.chrome.options import Options from selenium.we...
- `__init__` (@ `contourpy-1.3.3/tests/util_config.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `contourpy-1.3.3/tests/util_config.py`) -> **O(2^N) [Recursive]**
- `clear` (@ `contourpy-1.3.3/src/output_array.h`) -> **O(2^N) [Recursive]**
- `thread_counts` (@ `contourpy-1.3.3/benchmarks/benchmarks/util_bench.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `Mpl2014ContourGenerator::single_quad_fil` (@ `contourpy-1.3.3/src/mpl2014.cpp`) -> DB Complexity: **155**
- `data_init` (@ `contourpy-1.3.3/src/mpl2005_original.cpp`) -> DB Complexity: **121**
  * *Intent:* /* Saddle zone array consists of the following bits: * SADDLE_SET whether zone's saddle data has been set. * SADDLE_GT0 whether z of centre of zone is...
- `PYBIND11_MODULE` (@ `contourpy-1.3.3/src/wrap.cpp`) -> DB Complexity: **97**
- `Mpl2014ContourGenerator::init_cache_grid` (@ `contourpy-1.3.3/src/mpl2014.cpp`) -> DB Complexity: **82**
- `Mpl2014ContourGenerator::follow_interior` (@ `contourpy-1.3.3/src/mpl2014.cpp`) -> DB Complexity: **81**
- `Mpl2014ContourGenerator::lines` (@ `contourpy-1.3.3/src/mpl2014.cpp`) -> DB Complexity: **70**
- `Mpl2014ContourGenerator::follow_boundary` (@ `contourpy-1.3.3/src/mpl2014.cpp`) -> DB Complexity: **67**
- `reorder` (@ `contourpy-1.3.3/src/mpl2005_original.cpp`) -> DB Complexity: **53**
  * *Intent:* /* mark endpoint 0 only if value is 1 there, and this is a
- `Mpl2014ContourGenerator::append_contour_` (@ `contourpy-1.3.3/src/mpl2014.cpp`) -> DB Complexity: **53**
- `Mpl2014ContourGenerator::move_to_next_bo` (@ `contourpy-1.3.3/src/mpl2014.cpp`) -> DB Complexity: **41**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `contourpy-1.3.3/src` | 32 | 14359.78 | 56.72% | 29.34% |
| `contourpy-1.3.3/tests` | 22 | 4983.42 | 7.47% | 0.0% |
| `contourpy-1.3.3/benchmarks` | 4 | 1805.04 | 22.48% | 0.0% |
| `contourpy-1.3.3/benchmarks/benchmarks` | 19 | 201.68 | 11.06% | 84.08% |
| `contourpy-1.3.3` | 3 | 3.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `contourpy-1.3.3/src/converter.cpp` -> **100.0%** Exposure
- `contourpy-1.3.3/src/util.cpp` -> **99.9997%** Exposure
- `contourpy-1.3.3/src/contour_generator.cpp` -> **99.9944%** Exposure
- `contourpy-1.3.3/benchmarks/benchmarks/bench_filled_serial.py` -> **99.9918%** Exposure
- `contourpy-1.3.3/benchmarks/benchmarks/bench_filled_serial_quad_as_tri.py` -> **99.9918%** Exposure
### Highest State Flux (Mutation/Volatility)
- `contourpy-1.3.3/benchmarks/benchmarks/bench_base.py` -> **100.0%** Exposure
- `contourpy-1.3.3/src/base_impl.h` -> **100.0%** Exposure
- `contourpy-1.3.3/src/chunk_local.cpp` -> **100.0%** Exposure
- `contourpy-1.3.3/src/contour_generator.cpp` -> **100.0%** Exposure
- `contourpy-1.3.3/src/contour_generator.h` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `contourpy-1.3.3/src/mpl2014.cpp` -> **46** Orphaned Functions | **8** Duplicates
- `contourpy-1.3.3/tests/test_filled.py` -> **31** Orphaned Functions | **8** Duplicates
- `contourpy-1.3.3/tests/test_lines.py` -> **31** Orphaned Functions | **0** Duplicates
- `contourpy-1.3.3/tests/test_constructor.py` -> **30** Orphaned Functions | **0** Duplicates
- `contourpy-1.3.3/tests/test_array.py` -> **20** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`contourpy-1.3.3/benchmarks/plot_benchmarks.py`** -> AI Confidence: **99.48%**
2. **`contourpy-1.3.3/tests/util_config.py`** -> AI Confidence: **99.35%**
3. **`contourpy-1.3.3/tests/test_typecheck.py`** -> AI Confidence: **99.34%**
4. **`contourpy-1.3.3/src/mpl2014.cpp`** -> AI Confidence: **99.32%**
5. **`contourpy-1.3.3/benchmarks/loader.py`** -> AI Confidence: **99.31%**
6. **`contourpy-1.3.3/tests/test_array.py`** -> AI Confidence: **99.31%**
7. **`contourpy-1.3.3/tests/test_internal.py`** -> AI Confidence: **99.31%**
8. **`contourpy-1.3.3/tests/test_minimal.py`** -> AI Confidence: **99.31%**
9. **`contourpy-1.3.3/tests/test_renderer.py`** -> AI Confidence: **99.31%**
10. **`contourpy-1.3.3/src/fill_type.cpp`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `contourpy-1.3.3/benchmarks/loader.py` -> **100.0%** Exposure
- `contourpy-1.3.3/tests/test_array.py` -> **100.0%** Exposure
- `contourpy-1.3.3/tests/test_dechunk.py` -> **100.0%** Exposure
- `contourpy-1.3.3/tests/test_filled.py` -> **100.0%** Exposure
- `contourpy-1.3.3/tests/test_lines.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `contourpy-1.3.3/benchmarks/loader.py` -> **100.0%** Exposure
- `contourpy-1.3.3/tests/util_config.py` -> **100.0%** Exposure
- `contourpy-1.3.3/src/mpl2005_original.cpp` -> **100.0%** Exposure
- `contourpy-1.3.3/src/mpl2014.cpp` -> **100.0%** Exposure
- `contourpy-1.3.3/src/serial.cpp` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `302` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `contourpy-1.3.3/src/mpl2014.cpp` (CPP) -> Cumulative Risk: **843.28**
- **Archetype:** `file_cluster_8` (Distance: 16.18 IQR)
- **Magnitude:** 7266.42 | **LOC:** 1711 | **CtrlFlow:** 86.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (99.9869%)
- **Heaviest Functions:** `Mpl2014ContourGenerator::follow_interior` (Impact: 921.0), `Mpl2014ContourGenerator::single_quad_fil` (Impact: 680.2), `Mpl2014ContourGenerator::follow_boundary` (Impact: 553.7)

### 2. `contourpy-1.3.3/src/contour_generator.cpp` (CPP) -> Cumulative Risk: **823.63**
- **Archetype:** `file_cluster_8` (Distance: 13.039 IQR)
- **Magnitude:** 128.62 | **LOC:** 80 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9944%), Algorithmic Dos (99.8875%)
- **Heaviest Functions:** `ContourGenerator::check_levels` (Impact: 36.2), `ContourGenerator::check_levels` (Impact: 10.7), `ContourGenerator::multi_filled` (Impact: 6.8)

### 3. `contourpy-1.3.3/src/serial.cpp` (CPP) -> Cumulative Risk: **788.16**
- **Archetype:** `file_cluster_8` (Distance: 13.86 IQR)
- **Magnitude:** 347.18 | **LOC:** 148 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9802%)
- **Heaviest Functions:** `SerialContourGenerator::export_filled` (Impact: 112.0), `SerialContourGenerator::export_lines` (Impact: 99.5), `SerialContourGenerator::march` (Impact: 14.9)

### 4. `contourpy-1.3.3/src/threaded.cpp` (CPP) -> Cumulative Risk: **777.26**
- **Archetype:** `file_cluster_4` (Distance: 13.579 IQR)
- **Magnitude:** 567.34 | **LOC:** 317 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (98.1944%)
- **Heaviest Functions:** `ThreadedContourGenerator::export_filled` (Impact: 144.8), `ThreadedContourGenerator::export_lines` (Impact: 119.6), `ThreadedContourGenerator::thread_functio` (Impact: 50.3)

### 5. `contourpy-1.3.3/benchmarks/loader.py` (PYTHON) -> Cumulative Risk: **737.34**
- **Archetype:** `file_cluster_13` (Distance: 10.393 IQR)
- **Magnitude:** 228.04 | **LOC:** 102 | **CtrlFlow:** 47.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9319%)
- **Heaviest Functions:** `get` (Impact: 156.2), `__init__` (Impact: 31.2), `_find_benchmark_by_name` (Impact: 17.6)

### 6. `contourpy-1.3.3/src/wrap.cpp` (CPP) -> Cumulative Risk: **728.15**
- **Archetype:** `file_cluster_8` (Distance: 11.884 IQR)
- **Magnitude:** 300.04 | **LOC:** 420 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9992%), Concurrency (93.441%)
- **Heaviest Functions:** `PYBIND11_MODULE` (Impact: 126.0)

### 7. `contourpy-1.3.3/src/mpl2005.cpp` (CPP) -> Cumulative Risk: **708.51**
- **Archetype:** `file_cluster_8` (Distance: 11.347 IQR)
- **Magnitude:** 145.16 | **LOC:** 75 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9944%), Tech Debt (99.9073%), Documentation (97.5588%)
- **Heaviest Functions:** `Mpl2005ContourGenerator::Mpl2005ContourG` (Impact: 114.3), `Mpl2005ContourGenerator` (Impact: 2.2), `Mpl2005ContourGenerator::filled` (Impact: 2.0)

### 8. `contourpy-1.3.3/src/mpl2005_original.cpp` (CPP) -> Cumulative Risk: **686.61**
- **Archetype:** `file_cluster_8` (Distance: 14.763 IQR)
- **Magnitude:** 1981.02 | **LOC:** 1527 | **CtrlFlow:** 92.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (99.8671%)
- **Heaviest Functions:** `data_init` (Impact: 470.6), `reorder` (Impact: 285.8), `cntr_trace` (Impact: 55.9)

### 9. `contourpy-1.3.3/src/output_array.h` (CPP) -> Cumulative Risk: **675.9**
- **Archetype:** `file_cluster_13` (Distance: 13.554 IQR)
- **Magnitude:** 81.14 | **LOC:** 71 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9999%), Tech Debt (99.9689%)
- **Heaviest Functions:** `create_python` (Impact: 3.4), `clear` (Impact: 3.3), `create_cpp` (Impact: 1.9)

### 10. `contourpy-1.3.3/src/converter.cpp` (CPP) -> Cumulative Risk: **636.64**
- **Archetype:** `file_cluster_8` (Distance: 14.118 IQR)
- **Magnitude:** 156.92 | **LOC:** 156 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9508%)
- **Heaviest Functions:** `Converter::convert_codes_check_closed` (Impact: 16.0), `Converter::convert_codes_check_closed_si` (Impact: 6.9), `Converter::convert_offsets` (Impact: 6.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `contourpy-1.3.3/src/mpl2014.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 16.18 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.078 IQR)
- **Top Global Matches:** file_cluster_8: 16.18, file_cluster_11: 16.195, file_cluster_17: 16.332
- **Magnitude:** 7266.42 | **LOC:** 1711 | **CtrlFlow:** 86.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 155
- **Risk Profile:** Cognitive Load (99.3786%), Tech Debt (94.5761%)
**Top Internal Functions/Classes:**
  * `Mpl2014ContourGenerator::follow_interior` (Impact: 921.0 | O(N^6) | DB: 81)
  * `Mpl2014ContourGenerator::single_quad_fil` (Impact: 680.2 | O(N^4) | DB: 155)
  * `Mpl2014ContourGenerator::follow_boundary` (Impact: 553.7 | O(N^5) | DB: 67)
  * `Mpl2014ContourGenerator::init_cache_grid` (Impact: 459.8 | O(N^6) | DB: 82)
  * `Mpl2014ContourGenerator::lines` (Impact: 368.0 | O(N^6) | DB: 70)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 755`, `structural_boundaries: 117`, `args: 72`, `func_start: 57`
* *Risk/State:* `state_mutation: 2655`, `dead_code: 1`, `duplicate_logic: 8`, `orphaned_logic: 46`
* *Architecture:* `import: 3`
* *Defense:* `safety: 88`, `immutability_locks: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mpl_kind_code.h, mpl2014.h, algorithm
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/src/base_impl.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.055 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 3.765 IQR)
- **Top Global Matches:** file_cluster_8: 15.055, file_cluster_11: 15.169, file_cluster_13: 15.342
- **Magnitude:** 2721.24 | **LOC:** 2525 | **CtrlFlow:** 81.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (79.5782%), Tech Debt (11.5717%)
**Top Internal Functions/Classes:**
  * `_return_list_count` (Impact: 64.5 | O(N^4) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1011`, `structural_boundaries: 227`, `args: 172`, `func_start: 1`
* *Risk/State:* `state_mutation: 2616`, `fragile_debt: 6`
* *Architecture:* `import: 4`
* *Defense:* `safety: 79`, `sync_locks: 4`, `immutability_locks: 55`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.719
  * `Choke Point (Betweenness):` 0.001839 | `Ripple Effect (Closeness):` 0.037975
  * `Imports (Out-Degree: 3):` util.h, base.h, iostream, converter.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `contourpy-1.3.3/src/mpl2005_original.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.763 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.532 IQR)
- **Top Global Matches:** file_cluster_8: 14.763, file_cluster_11: 15.024, file_cluster_13: 15.05
- **Magnitude:** 1981.02 | **LOC:** 1527 | **CtrlFlow:** 92.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 121
- **Risk Profile:** Cognitive Load (86.937%), Tech Debt (30.2383%)
**Top Internal Functions/Classes:**
  * `data_init` (Impact: 470.6 | O(N^6) | DB: 121)
    * *Intent:* /* Saddle zone array consists of the following bits: * SADDLE_SET whether zone's saddle data has bee...
  * `reorder` (Impact: 285.8 | O(N^5) | DB: 53)
    * *Intent:* /* mark endpoint 0 only if value is 1 there, and this is a
  * `cntr_trace` (Impact: 55.9 | O(N^3) | DB: 26)
  * `mask_zones` (Impact: 46.3 | O(N^4) | DB: 17)
  * `cntr_init` (Impact: 30.1 | O(N^2) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 197`, `structural_boundaries: 15`, `args: 9`, `func_start: 9`
* *Risk/State:* `state_mutation: 1040`, `dead_code: 2`, `fragile_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `import: 2`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mpl_kind_code.h, mpl2005_original.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/benchmarks/plot_benchmarks.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.707 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.192 IQR)
- **Top Global Matches:** file_cluster_8: 8.707, file_cluster_13: 9.031, file_cluster_2: 9.103
- **Magnitude:** 1560.48 | **LOC:** 340 | **CtrlFlow:** 78.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (27.7972%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_style` (Impact: 1530.8 | O(2^N) | DB: 1)
    * *Intent:* # Colors from Paul Tol's colorblind friendly light scheme (https://personal.sron.nl/~pault) colors =...
  * `get_corner_mask_label` (Impact: 11.3 | O(N^2))
  * `capital_letters_to_newlines` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 35`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 3`
* *Architecture:* `api: 8`, `import: 10`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` matplotlib.pyplot, asv.util, matplotlib.patches, numpy, contourpy, typing, matplotlib.axes, __future__...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/util_config.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.481 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.776 IQR)
- **Top Global Matches:** file_cluster_8: 10.481, file_cluster_13: 10.6, file_cluster_16: 10.781
- **Magnitude:** 1273.6 | **LOC:** 602 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (26.9083%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 677.3 | O(2^N) | DB: 2)
  * `__init__` (Impact: 283.4 | O(2^N) | DB: 2)
  * `_decode_config` (Impact: 56.0 | O(N^4))
  * `__init__` (Impact: 49.1 | O(2^N) | DB: 2)
  * `_decode_config` (Impact: 36.0 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 67`, `args: 21`, `func_start: 21`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 51`, `dead_code: 1`, `duplicate_logic: 13`
* *Architecture:* `api: 15`, `import: 13`
* *Defense:* `safety: 8`, `test: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.564
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012658
  * `Imports (Out-Degree: 0):` matplotlib.pyplot, io, enum, matplotlib.figure, contourpy, contourpy._contourpy, typing, matplotlib.axes...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `contourpy-1.3.3/tests/test_typecheck.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.05 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.404 IQR)
- **Top Global Matches:** file_cluster_8: 9.05, file_cluster_16: 9.77, file_cluster_7: 9.849
- **Magnitude:** 855.62 | **LOC:** 389 | **CtrlFlow:** 78.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (13.7144%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_check_filled_ChunkCombinedOffsetOff` (Impact: 158.1 | O(N^5))
    * *Intent:* # Valid filled, does not raise. points = np.array([[1.1, 2.2], [3.3, 4.4], [5.5, 6.6], [7.7, 8.8]], ...
  * `test_check_filled_ChunkCombinedCodeOffse` (Impact: 157.9 | O(N^5))
    * *Intent:* # Valid filled, does not raise. points = np.array([[1.1, 2.2], [3.3, 4.4], [5.5, 6.6], [7.7, 8.8]], ...
  * `test_check_filled_ChunkCombinedCode` (Impact: 61.3 | O(N^2))
    * *Intent:* # Valid filled, does not raise. points = np.array([[1.1, 2.2], [3.3, 4.4], [5.5, 6.6]], dtype=point_...
  * `test_check_filled_ChunkCombinedOffset` (Impact: 61.3 | O(N^2))
    * *Intent:* # Valid filled, does not raise. points = np.array([[1.1, 2.2], [3.3, 4.4], [5.5, 6.6], [7.7, 8.8]], ...
  * `test_check_lines_ChunkCombinedCode` (Impact: 61.3 | O(N^2))
    * *Intent:* # Valid lines, does not raise. points = np.array([[1.1, 2.2], [3.3, 4.4], [5.5, 6.6], [7.7, 8.8]], d...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 64`, `args: 14`, `func_start: 14`
* *Risk/State:* `orphaned_logic: 14`
* *Architecture:* `api: 14`, `import: 6`
* *Defense:* `test: 120`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` contourpy.typecheck, contourpy, pytest, __future__, numpy, contourpy.types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/src/threaded.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.579 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.909 IQR)
- **Top Global Matches:** file_cluster_4: 13.579, file_cluster_8: 13.675, file_cluster_13: 13.773
- **Magnitude:** 567.34 | **LOC:** 317 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (92.3994%), Tech Debt (66.0283%)
**Top Internal Functions/Classes:**
  * `ThreadedContourGenerator::export_filled` (Impact: 144.8 | O(N^6) | DB: 34)
  * `ThreadedContourGenerator::export_lines` (Impact: 119.6 | O(N^6) | DB: 27)
  * `ThreadedContourGenerator::thread_functio` (Impact: 50.3 | O(N^4) | DB: 8)
  * `ThreadedContourGenerator::ThreadedContou` (Impact: 13.1 | O(N^6) | DB: 4)
  * `ThreadedContourGenerator::march` (Impact: 11.8 | O(N^3) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 27`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 191`, `orphaned_logic: 7`
* *Architecture:* `concurrency: 24`, `import: 5`
* *Defense:* `safety: 17`, `sync_locks: 16`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` threaded.h, util.h, thread, base_impl.h, converter.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_filled.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.398 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.067 IQR)
- **Top Global Matches:** file_cluster_0: 11.398, file_cluster_8: 11.554, file_cluster_13: 11.564
- **Magnitude:** 513.94 | **LOC:** 1045 | **CtrlFlow:** 33.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.2725%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_multi_filled_invalid_levels` (Impact: 53.6 | O(N^3))
  * `test_filled_random_chunk` (Impact: 34.0 | O(N^3))
  * `test_filled_random_big` (Impact: 24.8 | O(N^2))
  * `test_filled_nan_levels` (Impact: 24.6 | O(N^2))
  * `test_filled_z_nonfinite` (Impact: 22.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 252`, `args: 41`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 15`, `duplicate_logic: 8`, `orphaned_logic: 31`
* *Architecture:* `api: 41`, `import: 52`
* *Defense:* `safety: 124`, `test: 234`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .image_comparison, numpy.testing, functools, , numpy, contourpy, contourpy._contourpy, typing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_array.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.079 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.702 IQR)
- **Top Global Matches:** file_cluster_8: 10.079, file_cluster_16: 10.718, file_cluster_13: 10.806
- **Magnitude:** 407.18 | **LOC:** 575 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0793%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_insert_nan_at_offsets` (Impact: 68.1 | O(N^4))
  * `test_codes_from_offsets_and_points` (Impact: 55.1 | O(N^3))
  * `test_split_points_at_nan` (Impact: 49.9 | O(N^6))
  * `test_split_codes_by_offsets` (Impact: 24.8 | O(N^2))
  * `test_codes_from_offsets` (Impact: 24.4 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 88`, `args: 20`, `func_start: 20`
* *Risk/State:* `orphaned_logic: 20`
* *Architecture:* `api: 20`, `import: 7`
* *Defense:* `safety: 41`, `test: 99`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` contourpy.array, numpy.testing, , pytest, __future__, numpy, contourpy.types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/src/serial.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.86 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 3.607 IQR)
- **Top Global Matches:** file_cluster_8: 13.86, file_cluster_13: 13.913, file_cluster_11: 14.133
- **Magnitude:** 347.18 | **LOC:** 148 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (83.8772%), Tech Debt (80.9593%)
**Top Internal Functions/Classes:**
  * `SerialContourGenerator::export_filled` (Impact: 112.0 | O(N^6) | DB: 17)
  * `SerialContourGenerator::export_lines` (Impact: 99.5 | O(N^6) | DB: 15)
  * `SerialContourGenerator::march` (Impact: 14.9 | O(N^3) | DB: 6)
  * `SerialContourGenerator::SerialContourGen` (Impact: 12.5 | O(N^6) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 14`, `args: 9`, `func_start: 4`
* *Risk/State:* `state_mutation: 106`, `orphaned_logic: 4`
* *Architecture:* `import: 3`
* *Defense:* `safety: 12`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` serial.h, converter.h, base_impl.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_lines.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.455 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.34 IQR)
- **Top Global Matches:** file_cluster_0: 11.455, file_cluster_13: 11.649, file_cluster_8: 11.677
- **Magnitude:** 321.88 | **LOC:** 878 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.3735%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_e_to_w` (Impact: 21.8 | O(N^2))
  * `test_lines_random_chunk` (Impact: 21.6 | O(N^3))
  * `test_multi_lines_levels_type` (Impact: 19.5 | O(N^2))
  * `test_lines_random_big` (Impact: 18.8 | O(N^2))
  * `test_level_outside` (Impact: 17.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 249`, `args: 35`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 15`, `orphaned_logic: 31`
* *Architecture:* `api: 35`, `import: 49`
* *Defense:* `safety: 125`, `test: 235`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .image_comparison, numpy.testing, , contourpy, contourpy._contourpy, pytest, typing, contourpy.util.mpl_renderer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_renderer.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 9.262 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.602 IQR)
- **Top Global Matches:** file_cluster_0: 9.262, file_cluster_13: 9.315, file_cluster_8: 9.401
- **Magnitude:** 302.86 | **LOC:** 230 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (7.7453%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_renderer_lines` (Impact: 108.5 | O(N^4))
  * `test_renderer_filled` (Impact: 108.4 | O(N^4))
  * `test_debug_renderer_lines` (Impact: 29.3 | O(N^3))
  * `test_debug_renderer_filled` (Impact: 19.3 | O(N^2))
  * `test_save_svg` (Impact: 16.5 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 52`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `orphaned_logic: 6`
* *Architecture:* `io: 2`, `api: 6`, `import: 19`
* *Defense:* `safety: 8`, `test: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .image_comparison, _pytest._py.path, PIL, contourpy, pytest, typing, contourpy.util.mpl_renderer, __future__...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/src/wrap.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.884 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.552 IQR)
- **Top Global Matches:** file_cluster_8: 11.884, file_cluster_13: 12.193, file_cluster_11: 12.418
- **Magnitude:** 300.04 | **LOC:** 420 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 97
- **Risk Profile:** Cognitive Load (63.1187%), Tech Debt (61.8945%)
**Top Internal Functions/Classes:**
  * `PYBIND11_MODULE` (Impact: 126.0 | O(N^5) | DB: 97)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 66`, `args: 44`, `func_start: 1`
* *Risk/State:* `state_mutation: 160`, `planned_debt: 1`, `fragile_debt: 4`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 6`, `import: 10`
* *Defense:* `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` z_interp.h, mpl2005.h, threaded.h, mpl2014.h, util.h, serial.h, base_impl.h, fill_type.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_dechunk.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.161 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.208 IQR)
- **Top Global Matches:** file_cluster_0: 11.161, file_cluster_8: 11.262, file_cluster_13: 11.355
- **Magnitude:** 283.7 | **LOC:** 226 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (6.3191%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_dechunk_filled` (Impact: 107.8 | O(N^6))
  * `test_dechunk_lines` (Impact: 93.3 | O(N^6) | DB: 1)
  * `test_dechunk_lines_empty` (Impact: 18.9 | O(N^2))
  * `test_dechunk_multi_filled` (Impact: 15.9 | O(N^2))
  * `test_dechunk_multi_lines` (Impact: 15.9 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 58`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 6`, `import: 8`
* *Defense:* `safety: 39`, `test: 56`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` numpy.testing, , contourpy, contourpy._contourpy, pytest, typing, __future__, numpy
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/benchmarks/loader.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.393 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.143 IQR)
- **Top Global Matches:** file_cluster_13: 10.393, file_cluster_0: 10.942, file_cluster_8: 10.949
- **Magnitude:** 228.04 | **LOC:** 102 | **CtrlFlow:** 47.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (51.8285%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get` (Impact: 156.2 | O(N^6))
  * `__init__` (Impact: 31.2 | O(N^4) | DB: 4)
  * `_find_benchmark_by_name` (Impact: 17.6 | O(N^4))
  * `commit` (Impact: 2.7 | O(N^2))
  * `machine` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 34`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 10`
* *Architecture:* `api: 6`, `import: 12`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.715
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012658
  * `Imports (Out-Degree: 0):` copy, asv.results, datetime, asv.benchmark, contourpy, typing, asv_runner.statistics, asv.config...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `contourpy-1.3.3/tests/test_minimal.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.883 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.871 IQR)
- **Top Global Matches:** file_cluster_8: 8.883, file_cluster_13: 9.288, file_cluster_16: 9.327
- **Magnitude:** 205.24 | **LOC:** 181 | **CtrlFlow:** 60.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.2891%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_minimal_filled` (Impact: 104.2 | O(N^4))
  * `test_minimal_lines` (Impact: 93.2 | O(N^4))
  * `z` (Impact: 2.9 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 24`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 12`, `orphaned_logic: 2`
* *Architecture:* `api: 2`, `import: 7`
* *Defense:* `safety: 7`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , contourpy, contourpy._contourpy, pytest, typing, __future__, numpy
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_constructor.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.152 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.668 IQR)
- **Top Global Matches:** file_cluster_0: 11.152, file_cluster_16: 11.286, file_cluster_8: 11.347
- **Magnitude:** 197.96 | **LOC:** 420 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.4281%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_chunk_size_negative` (Impact: 21.4 | O(N^2))
  * `test_chunk_size_and_count` (Impact: 21.3 | O(N^2))
  * `test_xy_1d` (Impact: 15.6 | O(N^2))
  * `test_xy_ndim_more_than_2` (Impact: 15.2 | O(N^2))
  * `test_z_interp_not_supported` (Impact: 9.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 93`, `args: 32`, `func_start: 32`
* *Risk/State:* `orphaned_logic: 30`
* *Architecture:* `api: 32`, `import: 9`
* *Defense:* `safety: 43`, `test: 140`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` numpy.typing, , math, contourpy, contourpy._contourpy, pytest, typing, __future__...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_internal.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.857 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.448 IQR)
- **Top Global Matches:** file_cluster_16: 9.857, file_cluster_0: 9.898, file_cluster_13: 9.97
- **Magnitude:** 196.0 | **LOC:** 209 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (10.9201%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_xyz_ndim` (Impact: 37.4 | O(N^2))
  * `test_xyz_shape` (Impact: 21.4 | O(N^2))
  * `default_kwargs` (Impact: 21.1 | O(N^3) | DB: 1)
  * `test_xy_at_least_2x2` (Impact: 18.4 | O(N^2))
  * `test_chunk_size_not_negative` (Impact: 16.3 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 42`, `args: 12`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 9`, `orphaned_logic: 9`
* *Architecture:* `io: 1`, `api: 12`, `import: 7`
* *Defense:* `safety: 2`, `test: 42`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, io, pytest, typing, wurlitzer, __future__, contourpy._contourpy
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/src/converter.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.118 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.371 IQR)
- **Top Global Matches:** file_cluster_8: 14.118, file_cluster_13: 14.205, file_cluster_17: 14.344
- **Magnitude:** 156.92 | **LOC:** 156 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (72.6532%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Converter::convert_codes_check_closed` (Impact: 16.0 | O(N^5) | DB: 11)
  * `Converter::convert_codes_check_closed_si` (Impact: 6.9 | O(N^2) | DB: 7)
  * `Converter::convert_offsets` (Impact: 6.8 | O(N^2) | DB: 4)
  * `Converter::convert_codes` (Impact: 5.2 | O(N^2) | DB: 6)
  * `Converter::check_max_offset` (Impact: 3.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 16`, `func_start: 11`
* *Risk/State:* `state_mutation: 105`, `duplicate_logic: 10`, `orphaned_logic: 1`
* *Architecture:* `import: 3`
* *Defense:* `safety: 27`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mpl_kind_code.h, converter.h, limits
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/src/mpl2005.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.347 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.219 IQR)
- **Top Global Matches:** file_cluster_8: 11.347, file_cluster_13: 11.806, file_cluster_7: 11.965
- **Magnitude:** 145.16 | **LOC:** 75 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (94.5939%), Tech Debt (99.9073%)
**Top Internal Functions/Classes:**
  * `Mpl2005ContourGenerator::Mpl2005ContourG` (Impact: 114.3 | O(N^4) | DB: 7)
  * `Mpl2005ContourGenerator` (Impact: 2.2 | O(2^N))
  * `Mpl2005ContourGenerator::filled` (Impact: 2.0 | O(N^1) | DB: 1)
  * `Mpl2005ContourGenerator::lines` (Impact: 2.0 | O(N^1) | DB: 1)
  * `Mpl2005ContourGenerator::get_chunk_count` (Impact: 1.3 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 7`, `args: 3`, `func_start: 6`
* *Risk/State:* `state_mutation: 21`, `orphaned_logic: 5`
* *Architecture:* `import: 1`
* *Defense:* `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` mpl2005.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/src/contour_generator.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.039 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.333 IQR)
- **Top Global Matches:** file_cluster_8: 13.039, file_cluster_13: 13.145, file_cluster_11: 13.475
- **Magnitude:** 128.62 | **LOC:** 80 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (90.2868%), Tech Debt (99.9944%)
**Top Internal Functions/Classes:**
  * `ContourGenerator::check_levels` (Impact: 36.2 | O(N^4) | DB: 10)
  * `ContourGenerator::check_levels` (Impact: 10.7 | O(N^2))
  * `ContourGenerator::multi_filled` (Impact: 6.8 | O(N^2) | DB: 8)
  * `ContourGenerator::multi_lines` (Impact: 6.7 | O(N^2) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 15`, `args: 6`, `func_start: 4`
* *Risk/State:* `state_mutation: 67`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `import: 2`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` util.h, contour_generator.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/src/mpl2014.h` (CPP | Tier 0 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.86 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.214 IQR)
- **Top Global Matches:** file_cluster_13: 15.86, file_cluster_17: 15.994, file_cluster_0: 16.014
- **Magnitude:** 83.36 | **LOC:** 514 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 31`, `args: 20`, `class_start: 4`
* *Risk/State:* `state_mutation: 64`, `dead_code: 6`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `immutability_locks: 51`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.194
  * `Choke Point (Betweenness):` 0.000325 | `Ripple Effect (Closeness):` 0.025316
  * `Imports (Out-Degree: 1):` iostream, list, vector, contour_generator.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `contourpy-1.3.3/src/output_array.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 98.79%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.554 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.067 IQR)
- **Top Global Matches:** file_cluster_13: 13.554, file_cluster_8: 13.643, file_cluster_11: 13.874
- **Magnitude:** 81.14 | **LOC:** 71 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (77.0906%), Tech Debt (99.9689%)
**Top Internal Functions/Classes:**
  * `create_python` (Impact: 3.4 | O(N^2) | DB: 5)
  * `clear` (Impact: 3.3 | O(2^N) | DB: 3)
  * `create_cpp` (Impact: 1.9 | O(N^2) | DB: 3)
  * `create_python` (Impact: 1.9 | O(N^2) | DB: 3)
  * `OutputArray` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 8`, `args: 4`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 66`, `duplicate_logic: 2`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 3`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.386
  * `Choke Point (Betweenness):` 0.000325 | `Ripple Effect (Closeness):` 0.039435
  * `Imports (Out-Degree: 1):` vector, common.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `contourpy-1.3.3/tests/test_chunk.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.572 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.767 IQR)
- **Top Global Matches:** file_cluster_0: 10.572, file_cluster_16: 10.643, file_cluster_8: 10.713
- **Magnitude:** 79.86 | **LOC:** 99 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.9824%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_calc_chunk_sizes_invalid` (Impact: 42.5 | O(N^2))
  * `test_two_factors_invalid` (Impact: 9.2 | O(N^2))
  * `test_chunk_count_2d` (Impact: 3.6 | O(N^2))
  * `test_chunk_count_1d` (Impact: 3.5 | O(N^2))
  * `test_total_chunk_count` (Impact: 3.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 21`, `args: 8`, `func_start: 8`
* *Risk/State:* `orphaned_logic: 8`
* *Architecture:* `api: 8`, `import: 3`
* *Defense:* `safety: 8`, `test: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.413
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` contourpy.chunk, pytest, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/src/contour_generator.h` (CPP | Tier 0 | 🚨 AI THREAT: 98.75%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.415 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.549 IQR)
- **Top Global Matches:** file_cluster_13: 14.415, file_cluster_8: 14.472, file_cluster_11: 14.803
- **Magnitude:** 73.46 | **LOC:** 37 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (74.0657%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 9`, `args: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 57`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.706
  * `Choke Point (Betweenness):` 0.001136 | `Ripple Effect (Closeness):` 0.086799
  * `Imports (Out-Degree: 1):` common.h
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `contourpy-1.3.3/tests/test_renderer.py` (PYTHON) | Magnitude: 302.86 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 138, branch: 56, structural_boundaries: 52, test: 41
- `contourpy-1.3.3/tests/test_chunk.py` (PYTHON) | Magnitude: 79.86 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 51, test: 32, structural_boundaries: 21, branch: 17
- `contourpy-1.3.3/tests/test_dechunk.py` (PYTHON) | Magnitude: 283.7 | Delta: **0.101 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 151, structural_boundaries: 58, test: 56, branch: 44
- `contourpy-1.3.3/tests/test_constructor.py` (PYTHON) | Magnitude: 197.96 | Delta: **0.134 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 253, test: 140, structural_boundaries: 93, generics: 65
- `contourpy-1.3.3/tests/test_filled.py` (PYTHON) | Magnitude: 513.94 | Delta: **0.156 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 682, structural_boundaries: 252, test: 234, branch: 125

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `contourpy-1.3.3/src/line_type.h` (CPP) | Magnitude: 23.32 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 8, indent_spaces: 5, structural_boundaries: 3, import: 2
- `contourpy-1.3.3/tests/test_build_config.py` (PYTHON) | Magnitude: 19.68 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 10, test: 6, generics: 4
- `contourpy-1.3.3/src/z_interp.h` (CPP) | Magnitude: 20.26 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 5, structural_boundaries: 3, import: 2, macros: 2
- `contourpy-1.3.3/src/contour_generator.h` (CPP) | Magnitude: 73.46 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 57, indent_spaces: 12, args: 10, structural_boundaries: 9
- `contourpy-1.3.3/src/base.h` (CPP) | Magnitude: 51.9 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 116, immutability_locks: 66, state_mutation: 46, structural_boundaries: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `contourpy-1.3.3/benchmarks/benchmarks/bench_filled_threaded.py` (PYTHON) | Magnitude: 6.9 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 11, generics: 10, import: 4
- `contourpy-1.3.3/benchmarks/benchmarks/bench_lines_threaded.py` (PYTHON) | Magnitude: 6.9 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 11, generics: 10, import: 4
- `contourpy-1.3.3/tests/test_internal.py` (PYTHON) | Magnitude: 196.0 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 129, branch: 49, structural_boundaries: 42, test: 42
- `contourpy-1.3.3/benchmarks/benchmarks/bench_lines_mpl20xx_render.py` (PYTHON) | Magnitude: 6.76 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 15, generics: 8, import: 6
- `contourpy-1.3.3/benchmarks/benchmarks/bench_filled_mpl20xx_render.py` (PYTHON) | Magnitude: 6.74 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 15, generics: 8, import: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `contourpy-1.3.3/src/threaded.cpp` (CPP) | Magnitude: 567.34 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 210, state_mutation: 191, branch: 54, structural_boundaries: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `contourpy-1.3.3/tests/test_codebase.py` (PYTHON) | Magnitude: 27.62 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 18, test: 10, safety: 8
- `contourpy-1.3.3/src/fill_type.h` (CPP) | Magnitude: 24.34 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 9, indent_spaces: 6, structural_boundaries: 3, import: 2
- `contourpy-1.3.3/src/mpl2014.cpp` (CPP) | Magnitude: 7266.42 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 2655, indent_spaces: 1014, branch: 755, structural_boundaries: 117
- `contourpy-1.3.3/src/mpl2005.h` (CPP) | Magnitude: 20.44 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, immutability_locks: 6, state_mutation: 4, structural_boundaries: 3
- `contourpy-1.3.3/src/serial.cpp` (CPP) | Magnitude: 347.18 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 106, indent_spaces: 98, branch: 35, structural_boundaries: 14

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `contourpy-1.3.3/src/base.h` -> **Severity: 0.537** (Bridge: 0.0065 * Flux: 82.8047%)
- `contourpy-1.3.3/src/base_impl.h` -> **Severity: 0.184** (Bridge: 0.0018 * Flux: 100.0%)
- `contourpy-1.3.3/src/chunk_local.h` -> **Severity: 0.13** (Bridge: 0.0015 * Flux: 88.7736%)
- `contourpy-1.3.3/src/contour_generator.h` -> **Severity: 0.114** (Bridge: 0.0011 * Flux: 100.0%)
- `contourpy-1.3.3/src/serial.h` -> **Severity: 0.087** (Bridge: 0.0009 * Flux: 99.9866%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `contourpy-1.3.3/benchmarks/benchmarks/bench_base.py` -> **Severity: 16.203** (Embedded: 0.2025 * Error Risk: 80.0%)
- `contourpy-1.3.3/src/contour_generator.h` -> **Severity: 8.645** (Embedded: 0.0868 * Error Risk: 99.5977%)
- `contourpy-1.3.3/src/base_impl.h` -> **Severity: 3.744** (Embedded: 0.038 * Error Risk: 98.5943%)
- `contourpy-1.3.3/src/output_array.h` -> **Severity: 3.618** (Embedded: 0.0394 * Error Risk: 91.7461%)
- `contourpy-1.3.3/src/threaded.h` -> **Severity: 2.293** (Embedded: 0.0253 * Error Risk: 90.5641%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `contourpy-1.3.3/benchmarks/benchmarks/util_bench.py` -> **Severity: 5782.5** (Blast Radius: 57.825 * Doc Risk: 100.0%)
- `contourpy-1.3.3/benchmarks/benchmarks/bench_base.py` -> **Severity: 5782.494** (Blast Radius: 57.825 * Doc Risk: 99.9999%)
- `contourpy-1.3.3/src/common.h` -> **Severity: 3482.019** (Blast Radius: 100.662 * Doc Risk: 34.5912%)
- `contourpy-1.3.3/src/contour_generator.h` -> **Severity: 2378.422** (Blast Radius: 30.706 * Doc Risk: 77.4579%)
- `contourpy-1.3.3/src/util.h` -> **Severity: 1959.754** (Blast Radius: 22.391 * Doc Risk: 87.5242%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
