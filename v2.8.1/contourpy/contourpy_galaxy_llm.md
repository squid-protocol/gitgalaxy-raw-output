# ARCHITECTURAL_BRIEF: contourpy
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
| Total Artifacts | 143 |
| Analyzed Artifacts (Scanned) | 81 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 62 |
| Total LOC | 11681 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 56.6% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6057 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3029 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.6074 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 44 | 5416 | 54.3% |
| CPP | 32 | 6241 | 39.5% |
| MARKDOWN | 3 | 0 | 3.7% |
| JSON | 1 | 24 | 1.2% |
| PLAINTEXT | 1 | 0 | 1.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Typed Library` (z -0.36; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 28%, Declarative / Non-Code 16%, Defensive Guards Files 14%, Data / Markup / Trivial 9%, Many-Argument Workhorses Files 9%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 77 | 95.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 4.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 62*

**Composition by Extension & Reason:**
- `.png`: 52x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.build`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.4 | 21.4 | 7.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.7 | 47.5 | 60.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 31.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 9.7 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 87.5 | 8.8 | 7.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 28.2 | 0.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 21.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 17.4 | 0.8 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 92.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 78.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 514 | 34 | 14 | `contourpy-1.3.3/src/mpl2005_original.cpp` |
| cleanup | 7 | 2 | 0 | `contourpy-1.3.3/tests/test_config.py` |
| guards | 1186 | 52 | 39 | `contourpy-1.3.3/src/mpl2014.cpp` |
| danger | 165 | 24 | 7 | `contourpy-1.3.3/tests/util_config.py` |
| concurrency | 50 | 7 | 0 | `contourpy-1.3.3/src/threaded.cpp` |
| connectivity | 330 | 51 | 8 | `contourpy-1.3.3/tests/test_filled.py` |
| io | 25 | 5 | 0 | `contourpy-1.3.3/tests/image_comparison.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 1 | 1 | 0 | `contourpy-1.3.3/tests/test_codebase.py` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 7 | 4 | 0 | `contourpy-1.3.3/tests/test_renderer.py` |
| events | 0 | 0 | 0 | - |
| tests | 801 | 20 | 24 | `contourpy-1.3.3/tests/test_filled.py` |
| docs | 0 | 0 | 0 | - |
| debt | 66 | 11 | 1 | `contourpy-1.3.3/src/base_impl.h` |
| mutation | 4848 | 63 | 179 | `contourpy-1.3.3/src/base_impl.h` |
| dead_code | 337 | 52 | 9 | `contourpy-1.3.3/src/mpl2014.cpp` |
| credential | 0 | 0 | 0 | - |
| threat | 183 | 28 | 2 | `contourpy-1.3.3/src/base_impl.h` |
| ml_ai | 33 | 17 | 2 | `contourpy-1.3.3/tests/util_config.py` |
| ui | 15 | 1 | 0 | `contourpy-1.3.3/benchmarks/plot_benchmarks.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `contourpy-1.3.3/tests/image_comparison.py` (Hits: 12)
- `contourpy-1.3.3/tests/conftest.py` (Hits: 8)
- `contourpy-1.3.3/tests/test_bokeh_renderer.py` (Hits: 2)

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

- `Mpl2014ContourGenerator::single_quad_filled` **(Many-Argument Workhorses)** (@ `contourpy-1.3.3/src/mpl2014.cpp`) -> Impact: **277.7** | LOC: 187
- `Mpl2014ContourGenerator::follow_interior` **(Many-Argument Workhorses)** (@ `contourpy-1.3.3/src/mpl2014.cpp`) -> Impact: **268.4** | LOC: 149
- `Mpl2014ContourGenerator::follow_boundary` **(Many-Argument Workhorses)** (@ `contourpy-1.3.3/src/mpl2014.cpp`) -> Impact: **188.6** | LOC: 120
- `by_name_and_type` **(Many-Argument Workhorses)** (@ `contourpy-1.3.3/benchmarks/plot_benchmarks.py`) -> Impact: **185.1** | LOC: 125
- `zone_crosser` **(Many-Argument Workhorses)** (@ `contourpy-1.3.3/src/mpl2005_original.cpp`) -> Impact: **138.3** | LOC: 206
  * *Intent:* /* ------------------------------------------------------------------------ */ /* zone_crosser assumes you are sitting at a cut edge about to cross * ...
- `comparison_two_benchmarks` **(Many-Argument Workhorses)** (@ `contourpy-1.3.3/benchmarks/plot_benchmarks.py`) -> Impact: **114.2** | LOC: 128
- `curve_tracer` **(Many-Argument Workhorses)** (@ `contourpy-1.3.3/src/mpl2005_original.cpp`) -> Impact: **113.2** | LOC: 186
  * *Intent:* /* ------------------------------------------------------------------------ */ /* curve_tracer finds the next starting point, then traces the curve, *...
- `edge_walker` **(Compute Cores)** (@ `contourpy-1.3.3/src/mpl2005_original.cpp`) -> Impact: **103.4** | LOC: 162
  * *Intent:* /* edge_walker assumes that the current edge is being drawn CCW * around the current zone. Since only boundary edges are drawn * and we always walk ar...
- `reorder` **(Many-Argument Workhorses)** (@ `contourpy-1.3.3/src/mpl2005_original.cpp`) -> Impact: **99.2** | LOC: 117
- `__init__` **(Many-Argument Workhorses)** (@ `contourpy-1.3.3/tests/util_config.py`) -> Impact: **98.2** | LOC: 85

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `contourpy-1.3.3/src` | 32 | 6496.72 | 23.57% | 30.16% |
| `contourpy-1.3.3/tests` | 23 | 4530.96 | 27.12% | 0.0% |
| `contourpy-1.3.3/benchmarks` | 4 | 764.14 | 46.17% | 0.0% |
| `contourpy-1.3.3/benchmarks/benchmarks` | 19 | 259.58 | 4.32% | 77.82% |
| `contourpy-1.3.3` | 3 | 3.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `contourpy-1.3.3/src/mpl2005.cpp` -> **99.9835%** Exposure
- `contourpy-1.3.3/src/chunk_local.cpp` -> **98.9013%** Exposure
- `contourpy-1.3.3/src/util.cpp` -> **98.9013%** Exposure
- `contourpy-1.3.3/benchmarks/benchmarks/bench_filled_mpl20xx.py` -> **92.4142%** Exposure
- `contourpy-1.3.3/benchmarks/benchmarks/bench_filled_mpl20xx_render.py` -> **92.4142%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `contourpy-1.3.3/benchmarks/loader.py` -> **100.0%** Exposure
- `contourpy-1.3.3/benchmarks/plot_benchmarks.py` -> **100.0%** Exposure
- `contourpy-1.3.3/src/base_impl.h` -> **100.0%** Exposure
- `contourpy-1.3.3/src/contour_generator.cpp` -> **100.0%** Exposure
- `contourpy-1.3.3/src/mpl2005_original.cpp` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `contourpy-1.3.3/src/mpl2014.cpp` -> **53** Orphaned Functions | **0** Duplicates
- `contourpy-1.3.3/tests/test_filled.py` -> **31** Orphaned Functions | **0** Duplicates
- `contourpy-1.3.3/tests/test_lines.py` -> **31** Orphaned Functions | **0** Duplicates
- `contourpy-1.3.3/tests/test_constructor.py` -> **30** Orphaned Functions | **0** Duplicates
- `contourpy-1.3.3/tests/test_array.py` -> **20** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `311` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `contourpy-1.3.3/src/mpl2014.cpp` (CPP) -> Cumulative Risk: **713.59**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.39)
- **Magnitude:** 2340.02 | **LOC:** 1711 | **CtrlFlow:** 60.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (99.3724%)
- **Heaviest Functions:** `Mpl2014ContourGenerator::single_quad_filled` (Many-Argument Workhorses, Impact: 277.7), `Mpl2014ContourGenerator::follow_interior` (Many-Argument Workhorses, Impact: 268.4), `Mpl2014ContourGenerator::follow_boundary` (Many-Argument Workhorses, Impact: 188.6)

### 2. `contourpy-1.3.3/src/threaded.cpp` (CPP) -> Cumulative Risk: **648.15**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.04)
- **Magnitude:** 221.04 | **LOC:** 317 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9937%), Cognitive Load (88.0353%)
- **Heaviest Functions:** `ThreadedContourGenerator::export_filled` (Many-Argument Workhorses, Impact: 45.2), `ThreadedContourGenerator::export_lines` (Many-Argument Workhorses, Impact: 37.3), `ThreadedContourGenerator::thread_function` (Compute Cores, Impact: 18.3)

### 3. `contourpy-1.3.3/src/mpl2005_original.cpp` (CPP) -> Cumulative Risk: **645.38**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +0.44)
- **Magnitude:** 1702.86 | **LOC:** 1527 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.6483%)
- **Heaviest Functions:** `zone_crosser` (Many-Argument Workhorses, Impact: 138.3), `curve_tracer` (Many-Argument Workhorses, Impact: 113.2), `edge_walker` (Compute Cores, Impact: 103.4)

### 4. `contourpy-1.3.3/src/serial.cpp` (CPP) -> Cumulative Risk: **621.28**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +0.20)
- **Magnitude:** 101.08 | **LOC:** 148 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.3094%), Tech Debt (80.9593%)
- **Heaviest Functions:** `SerialContourGenerator::export_filled` (Defensive Guards, Impact: 34.1), `SerialContourGenerator::export_lines` (Defensive Guards, Impact: 30.2), `SerialContourGenerator::march` (Compute Cores, Impact: 6.7)

### 5. `contourpy-1.3.3/src/contour_generator.cpp` (CPP) -> Cumulative Risk: **619.81**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +2.79)
- **Magnitude:** 67.22 | **LOC:** 80 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.0873%)
- **Heaviest Functions:** `ContourGenerator::check_levels` (Compute Cores, Impact: 15.5), `ContourGenerator::check_levels` (Compute Cores, Impact: 7.3), `ContourGenerator::multi_filled` (Interface Declarations, Impact: 3.7)

### 6. `contourpy-1.3.3/benchmarks/loader.py` (PYTHON) -> Cumulative Risk: **594.06**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.79)
- **Magnitude:** 149.24 | **LOC:** 102 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.4384%), Cognitive Load (87.0167%)
- **Heaviest Functions:** `get` (Many-Argument Workhorses, Impact: 44.2), `__init__` (Compute Cores, Impact: 13.0), `_find_benchmark_by_name` (Generic / Templated Code, Impact: 5.4)

### 7. `contourpy-1.3.3/benchmarks/plot_benchmarks.py` (PYTHON) -> Cumulative Risk: **590.55**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.90)
- **Magnitude:** 598.38 | **LOC:** 340 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.7366%), Cognitive Load (97.6832%)
- **Heaviest Functions:** `by_name_and_type` (Many-Argument Workhorses, Impact: 185.1), `comparison_two_benchmarks` (Many-Argument Workhorses, Impact: 114.2), `main` (I/O & Config Routines, Impact: 9.9)

### 8. `contourpy-1.3.3/src/chunk_local.cpp` (CPP) -> Cumulative Risk: **583.03**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +1.68)
- **Magnitude:** 30.06 | **LOC:** 60 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9955%), Tech Debt (98.9013%)
- **Heaviest Functions:** `operator<<` (Compute Cores, Impact: 10.1), `ChunkLocal::clear` (I/O & Config Routines, Impact: 1.8), `ChunkLocal::ChunkLocal` (I/O & Config Routines, Impact: 1.2)

### 9. `contourpy-1.3.3/src/util.cpp` (CPP) -> Cumulative Risk: **556.54**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.74)
- **Magnitude:** 12.66 | **LOC:** 31 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.9013%), State Flux (91.6827%)
- **Heaviest Functions:** `Util::ensure_nan_loaded` (I/O & Config Routines, Impact: 2.4), `Util::is_nan` (Interface Declarations, Impact: 1.6), `Util::get_max_threads` (Interface Declarations, Impact: 1.2)

### 10. `contourpy-1.3.3/src/base_impl.h` (CPP) -> Cumulative Risk: **539.56**
- **Archetype:** `file_cluster_7` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +0.01)
- **Magnitude:** 1451.44 | **LOC:** 2525 | **CtrlFlow:** 49.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.5951%)
- **Heaviest Functions:** `_return_list_count` (Compute Cores, Impact: 37.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `contourpy-1.3.3/src/mpl2014.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2340.02 | **LOC:** 1711 | **CtrlFlow:** 60.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.3724%), Tech Debt (85.9487%)
**Top Internal Functions/Classes:**
  * `Mpl2014ContourGenerator::single_quad_filled` **(Many-Argument Workhorses)** (Impact: 277.7)
  * `Mpl2014ContourGenerator::follow_interior` **(Many-Argument Workhorses)** (Impact: 268.4)
  * `Mpl2014ContourGenerator::follow_boundary` **(Many-Argument Workhorses)** (Impact: 188.6)
  * `Mpl2014ContourGenerator::init_cache_grid` **(Compute Cores)** (Impact: 96.7)
  * `Mpl2014ContourGenerator::lines` **(Compute Cores)** (Impact: 89.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 219 instances
* *State Mutation (weighted view):* 660
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 755`, `structural_boundaries: 117`, `args: 57`, `func_start: 57`
* *Risk/State:* `state_mutation: 222`, `dead_code: 1`, `unreferenced_by_name: 53`
* *Architecture:* `import: 3`
* *Defense:* `safety: 88`, `immutability_locks: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` algorithm, mpl2014.h, mpl_kind_code.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/src/mpl2005_original.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1702.86 | **LOC:** 1527 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.9029%), Tech Debt (18.4893%)
**Top Internal Functions/Classes:**
  * `zone_crosser` **(Many-Argument Workhorses)** (Impact: 138.3)
    * *Intent:* /* ------------------------------------------------------------------------ */ /* zone_crosser assum...
  * `curve_tracer` **(Many-Argument Workhorses)** (Impact: 113.2)
    * *Intent:* /* ------------------------------------------------------------------------ */ /* curve_tracer finds...
  * `edge_walker` **(Compute Cores)** (Impact: 103.4)
    * *Intent:* /* edge_walker assumes that the current edge is being drawn CCW * around the current zone. Since onl...
  * `reorder` **(Many-Argument Workhorses)** (Impact: 99.2)
  * `data_init` **(Compute Cores)** (Impact: 93.1)
    * *Intent:* /* ------------------------------------------------------------------------ */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 323 instances
* *State Mutation (weighted view):* 987
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 331`, `structural_boundaries: 32`, `args: 18`, `func_start: 13`
* *Risk/State:* `state_mutation: 341`, `dead_code: 11`, `fragile_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `import: 2`
* *Defense:* `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mpl2005_original.h, mpl_kind_code.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/src/base_impl.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 1451.44 | **LOC:** 2525 | **CtrlFlow:** 49.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.3352%), Tech Debt (11.3191%)
**Top Internal Functions/Classes:**
  * `_return_list_count` **(Compute Cores)** (Impact: 37.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 453 instances
* *State Mutation (weighted view):* 1371
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1065`, `structural_boundaries: 235`, `args: 102`, `func_start: 1`
* *Risk/State:* `state_mutation: 465`, `fragile_debt: 6`
* *Architecture:* `import: 4`
* *Defense:* `safety: 82`, `sync_locks: 4`, `immutability_locks: 55`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.292
  * `Choke Point (Betweenness):` 0.001793 | `Ripple Effect (Closeness):` 0.0375
  * `Imports (Out-Degree: 3):` base.h, converter.h, iostream, util.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `contourpy-1.3.3/tests/test_filled.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 796.54 | **LOC:** 1045 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.8238%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_return_by_fill_type_chunk` **(Defensive Guards)** (Impact: 77.4)
  * `test_return_by_fill_type` **(Defensive Guards)** (Impact: 48.6)
  * `test_filled_random_chunk` **(Many-Argument Workhorses)** (Impact: 18.0)
  * `test_multi_filled_invalid_levels` **(Compute Cores)** (Impact: 17.2)
  * `test_filled_random_big` **(Defensive Guards)** (Impact: 16.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 98 instances
* *State Mutation (weighted view):* 384
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 264`, `args: 41`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 188`, `unreferenced_by_name: 31`
* *Architecture:* `api: 41`, `import: 52`
* *Defense:* `safety: 124`, `test: 128`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` , .image_comparison, __future__, contourpy, contourpy._contourpy, contourpy.util.data, contourpy.util.mpl_renderer, functools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/util_config.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 773.1 | **LOC:** 602 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.3234%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 98.2)
  * `_next_quad` **(Many-Argument Workhorses)** (Impact: 89.5)
  * `_quad_lines` **(Many-Argument Workhorses)** (Impact: 81.0)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 41.9)
  * `_decode_config` **(Compute Cores)** (Impact: 23.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 324
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 71`, `args: 21`, `func_start: 21`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 136`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 13`, `import: 13`
* *Defense:* `safety: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.179
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0125
  * `Imports (Out-Degree: 0):` __future__, abc, collections.abc, contourpy, contourpy._contourpy, enum, io, matplotlib...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `contourpy-1.3.3/benchmarks/plot_benchmarks.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 598.38 | **LOC:** 340 | **CtrlFlow:** 48.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.6832%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `by_name_and_type` **(Many-Argument Workhorses)** (Impact: 185.1)
  * `comparison_two_benchmarks` **(Many-Argument Workhorses)** (Impact: 114.2)
  * `main` **(I/O & Config Routines)** (Impact: 9.9)
  * `get_corner_mask_label` **(Generic / Templated Code)** (Impact: 4.5)
  * `in_bar_label` **(Generic / Templated Code)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 261
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 35`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 95`
* *Architecture:* `api: 8`, `import: 10`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, asv.util, contourpy, loader, matplotlib.axes, matplotlib.patches, matplotlib.pyplot, numpy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_lines.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 561.88 | **LOC:** 878 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.5786%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_return_by_line_type_chunk` **(Many-Argument Workhorses)** (Impact: 51.0)
  * `test_return_by_line_type` **(Defensive Guards)** (Impact: 27.0)
  * `test_multi_lines_levels_type` **(Many-Argument Workhorses)** (Impact: 13.5)
  * `test_e_to_w` **(Defensive Guards)** (Impact: 12.9)
  * `test_lines_random_big` **(Defensive Guards)** (Impact: 12.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 268
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 251`, `args: 35`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 146`, `unreferenced_by_name: 31`
* *Architecture:* `api: 35`, `import: 49`
* *Defense:* `safety: 125`, `test: 122`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` , .image_comparison, __future__, contourpy, contourpy._contourpy, contourpy.util.data, contourpy.util.mpl_renderer, numpy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_renderer.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 264.36 | **LOC:** 230 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.5457%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_renderer_lines` **(Many-Argument Workhorses)** (Impact: 44.8)
  * `test_renderer_filled` **(Many-Argument Workhorses)** (Impact: 44.7)
  * `test_debug_renderer_lines` **(Many-Argument Workhorses)** (Impact: 15.3)
  * `test_debug_renderer_filled` **(Many-Argument Workhorses)** (Impact: 13.3)
  * `test_save_svg` **(Defensive Guards)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 54`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 45`, `unreferenced_by_name: 6`
* *Architecture:* `io: 2`, `api: 6`, `import: 19`
* *Defense:* `safety: 8`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .image_comparison, PIL, __future__, _pytest._py.path, contourpy, contourpy.util.data, contourpy.util.mpl_renderer, numpy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_constructor.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 246.06 | **LOC:** 420 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.4812%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_chunk_size_2d` **(Defensive Guards)** (Impact: 12.3)
  * `test_thread_count` **(Defensive Guards)** (Impact: 8.9)
  * `test_chunk_size_and_count` **(Tests & Verification)** (Impact: 7.6)
  * `test_chunk_size_negative` **(Generic / Templated Code)** (Impact: 7.4)
  * `test_chunk_size_1d` **(Defensive Guards)** (Impact: 7.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 118`, `args: 32`, `func_start: 32`
* *Risk/State:* `state_mutation: 47`, `unreferenced_by_name: 30`
* *Architecture:* `api: 32`, `import: 9`
* *Defense:* `safety: 43`, `test: 98`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , __future__, contourpy, contourpy._contourpy, math, numpy, numpy.typing, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_dechunk.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 222.5 | **LOC:** 226 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.3334%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_dechunk_filled` **(Defensive Guards)** (Impact: 32.8)
  * `test_dechunk_lines` **(Defensive Guards)** (Impact: 28.4)
  * `test_dechunk_lines_empty` **(Defensive Guards)** (Impact: 12.8)
  * `test_dechunk_multi_filled` **(Defensive Guards)** (Impact: 10.9)
  * `test_dechunk_multi_lines` **(Defensive Guards)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 58`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 39`, `unreferenced_by_name: 6`
* *Architecture:* `api: 6`, `import: 8`
* *Defense:* `safety: 39`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , __future__, contourpy, contourpy._contourpy, numpy, numpy.testing, pytest, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/src/threaded.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 221.04 | **LOC:** 317 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0353%), Tech Debt (56.0358%)
**Top Internal Functions/Classes:**
  * `ThreadedContourGenerator::export_filled` **(Many-Argument Workhorses)** (Impact: 45.2)
  * `ThreadedContourGenerator::export_lines` **(Many-Argument Workhorses)** (Impact: 37.3)
  * `ThreadedContourGenerator::thread_function` **(Compute Cores)** (Impact: 18.3)
  * `ThreadedContourGenerator::limit_n_threads` **(Type Conversions)** (Impact: 5.6)
  * `ThreadedContourGenerator::march` **(Compute Cores)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 23 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 27`, `args: 8`, `func_start: 7`
* *Risk/State:* `state_mutation: 29`, `unreferenced_by_name: 6`
* *Architecture:* `concurrency: 4`, `import: 5`
* *Defense:* `safety: 17`, `sync_locks: 16`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` base_impl.h, converter.h, thread, threaded.h, util.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_array.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 205.98 | **LOC:** 575 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.5379%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_codes_from_offsets_and_points` **(Tests & Verification)** (Impact: 11.2)
  * `test_insert_nan_at_offsets` **(Tests & Verification)** (Impact: 11.2)
  * `test_split_codes_by_offsets` **(Tests & Verification)** (Impact: 6.4)
  * `test_split_points_at_nan` **(Defensive Guards)** (Impact: 6.4)
  * `test_split_points_by_offsets` **(Tests & Verification)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 87
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 131`, `args: 20`, `func_start: 20`
* *Risk/State:* `state_mutation: 85`, `unreferenced_by_name: 20`
* *Architecture:* `api: 20`, `import: 7`
* *Defense:* `safety: 41`, `test: 64`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , __future__, contourpy.array, contourpy.types, numpy, numpy.testing, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_typecheck.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 195.62 | **LOC:** 389 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.8614%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_check_filled_ChunkCombinedOffsetOffset` **(Tests & Verification)** (Impact: 18.2)
    * *Intent:* # Valid filled, does not raise. points = np.array([[1.1, 2.2], [3.3, 4.4], [5.5, 6.6], [7.7, 8.8]], ...
  * `test_check_filled_ChunkCombinedCodeOffset` **(Tests & Verification)** (Impact: 18.1)
    * *Intent:* # Valid filled, does not raise. points = np.array([[1.1, 2.2], [3.3, 4.4], [5.5, 6.6], [7.7, 8.8]], ...
  * `test_check_filled_ChunkCombinedCode` **(Tests & Verification)** (Impact: 13.6)
    * *Intent:* # Valid filled, does not raise. points = np.array([[1.1, 2.2], [3.3, 4.4], [5.5, 6.6]], dtype=point_...
  * `test_check_filled_ChunkCombinedOffset` **(Tests & Verification)** (Impact: 13.6)
    * *Intent:* # Valid filled, does not raise. points = np.array([[1.1, 2.2], [3.3, 4.4], [5.5, 6.6], [7.7, 8.8]], ...
  * `test_check_lines_ChunkCombinedCode` **(Tests & Verification)** (Impact: 13.6)
    * *Intent:* # Valid lines, does not raise. points = np.array([[1.1, 2.2], [3.3, 4.4], [5.5, 6.6], [7.7, 8.8]], d...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 178`, `args: 14`, `func_start: 14`
* *Risk/State:* `state_mutation: 22`, `unreferenced_by_name: 14`
* *Architecture:* `api: 14`, `import: 6`
* *Defense:* `test: 120`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, contourpy, contourpy.typecheck, contourpy.types, numpy, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_minimal.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 180.54 | **LOC:** 181 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.6197%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_minimal_filled` **(Many-Argument Workhorses)** (Impact: 44.1)
  * `test_minimal_lines` **(Many-Argument Workhorses)** (Impact: 39.2)
  * `z` **(Interface Declarations)** (Impact: 1.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 24`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 33`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 7`
* *Defense:* `safety: 7`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , __future__, contourpy, contourpy._contourpy, numpy, pytest, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_internal.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 175.6 | **LOC:** 209 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.4094%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_xyz_ndim` **(Compute Cores)** (Impact: 14.9)
  * `test_xyz_shape` **(Generic / Templated Code)** (Impact: 9.3)
  * `default_kwargs` **(Compute Cores)** (Impact: 8.1)
  * `test_chunk_size_not_negative` **(Generic / Templated Code)** (Impact: 7.6)
  * `test_xy_at_least_2x2` **(Generic / Templated Code)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 63`, `args: 12`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 36`, `unreferenced_by_name: 9`
* *Architecture:* `io: 1`, `api: 12`, `import: 7`
* *Defense:* `safety: 2`, `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, contourpy._contourpy, io, pytest, sys, typing, wurlitzer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_bokeh_renderer.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 167.34 | **LOC:** 197 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.3859%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_renderer_lines_bokeh` **(Many-Argument Workhorses)** (Impact: 31.1)
  * `test_renderer_filled_bokeh` **(Many-Argument Workhorses)** (Impact: 31.0)
  * `test_save_svg` **(Defensive Guards)** (Impact: 7.7)
  * `driver` **(Generic / Templated Code)** (Impact: 5.3)
    * *Intent:* # Based on Bokeh's tests/support/plugins/selenium.py def chrome() -> WebDriver: from selenium.webdri...
  * `chrome` **(Interface Declarations)** (Impact: 3.7)
    * *Intent:* # Based on Bokeh's tests/support/plugins/selenium.py
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 55`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 28`, `unreferenced_by_name: 5`
* *Architecture:* `io: 2`, `api: 7`, `import: 18`
* *Defense:* `safety: 7`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .image_comparison, PIL, __future__, _pytest._py.path, _pytest.logging, collections.abc, contourpy, contourpy.util.data...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/benchmarks/loader.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 149.24 | **LOC:** 102 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.0167%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get` **(Many-Argument Workhorses)** (Impact: 44.2)
  * `__init__` **(Compute Cores)** (Impact: 13.0)
  * `_find_benchmark_by_name` **(Generic / Templated Code)** (Impact: 5.4)
  * `commit` **(Generic / Templated Code)** (Impact: 1.5)
  * `machine` **(Generic / Templated Code)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 35`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 27`
* *Architecture:* `api: 5`, `import: 12`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0125
  * `Imports (Out-Degree: 0):` __future__, asv.benchmark, asv.benchmarks, asv.config, asv.results, asv_runner.statistics, contourpy, copy...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `contourpy-1.3.3/tests/test_convert.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 124.9 | **LOC:** 180 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.5362%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_convert_filled` **(Many-Argument Workhorses)** (Impact: 23.8)
  * `test_convert_multi_filled` **(Defensive Guards)** (Impact: 17.1)
  * `test_convert_lines` **(Many-Argument Workhorses)** (Impact: 13.6)
  * `test_convert_multi_lines` **(Defensive Guards)** (Impact: 7.9)
  * `z` **(Interface Declarations)** (Impact: 1.8)
    * *Intent:* # Care needed with test data as although arbitrary z produces identical results for lines # regardle...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 31`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 22`, `dead_code: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `safety: 12`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , __future__, contourpy, contourpy._contourpy, numpy, pytest, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_z_interp.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 109.78 | **LOC:** 107 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.5075%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_z_interp_log` **(Many-Argument Workhorses)** (Impact: 13.8)
  * `test_z_interp_log_saddle` **(Defensive Guards)** (Impact: 9.5)
  * `test_z_interp_negative` **(Tests & Verification)** (Impact: 6.3)
  * `xyz_log` **(Interface Declarations)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 27`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 29`, `unreferenced_by_name: 3`
* *Architecture:* `api: 4`, `import: 8`
* *Defense:* `safety: 6`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, collections.abc, contourpy, contourpy._contourpy, numpy, numpy.testing, pytest, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/test_config.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 104.24 | **LOC:** 112 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.2945%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_config_lines` **(Generic / Templated Code)** (Impact: 7.5)
  * `test_config_filled` **(Generic / Templated Code)** (Impact: 5.6)
  * `test_config_filled_quad_as_tri` **(Generic / Templated Code)** (Impact: 5.6)
  * `test_config_filled_corner` **(Generic / Templated Code)** (Impact: 5.6)
  * `test_config_lines_quad_as_tri` **(Generic / Templated Code)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 42`, `args: 7`, `func_start: 7`
* *Risk/State:* `state_mutation: 19`, `unreferenced_by_name: 6`
* *Architecture:* `api: 7`, `import: 19`
* *Defense:* `test: 33`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` , .image_comparison, .util_config, __future__, gc, platform, pytest, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/src/serial.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 101.08 | **LOC:** 148 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.5412%), Tech Debt (80.9593%)
**Top Internal Functions/Classes:**
  * `SerialContourGenerator::export_filled` **(Defensive Guards)** (Impact: 34.1)
  * `SerialContourGenerator::export_lines` **(Defensive Guards)** (Impact: 30.2)
  * `SerialContourGenerator::march` **(Compute Cores)** (Impact: 6.7)
  * `SerialContourGenerator::SerialContourGenerator` **(Many-Argument Workhorses)** (Impact: 3.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 14`, `args: 9`, `func_start: 4`
* *Risk/State:* `state_mutation: 8`, `unreferenced_by_name: 4`
* *Architecture:* `import: 3`
* *Defense:* `safety: 12`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` base_impl.h, converter.h, serial.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/src/converter.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 98.12 | **LOC:** 156 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.2831%), Tech Debt (20.506%)
**Top Internal Functions/Classes:**
  * `Converter::convert_codes_check_closed` **(Defensive Guards)** (Impact: 13.2)
  * `Converter::convert_offsets` **(Defensive Guards)** (Impact: 9.8)
  * `Converter::convert_codes_check_closed_single` **(Defensive Guards)** (Impact: 8.9)
  * `Converter::convert_codes` **(Defensive Guards)** (Impact: 8.0)
  * `Converter::convert_codes_check_closed` **(Defensive Guards)** (Impact: 5.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 16`, `args: 11`, `func_start: 11`
* *Risk/State:* `state_mutation: 11`, `unreferenced_by_name: 1`
* *Architecture:* `import: 3`
* *Defense:* `safety: 27`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` converter.h, limits, mpl_kind_code.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/tests/image_comparison.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 87.54 | **LOC:** 90 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.796%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `compare_images` **(Many-Argument Workhorses)** (Impact: 28.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 19`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `io: 12`, `api: 1`, `import: 8`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.466
  * `Choke Point (Betweenness):` 0.000791 | `Ripple Effect (Closeness):` 0.0625
  * `Imports (Out-Degree: 1):` .conftest, PIL, __future__, io, numpy, os, shutil, typing
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `contourpy-1.3.3/tests/test_static.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 85.52 | **LOC:** 121 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.1507%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_default_fill_type` **(Defensive Guards)** (Impact: 4.7)
  * `test_default_line_type` **(Defensive Guards)** (Impact: 4.7)
  * `test_has_lines_and_filled` **(Defensive Guards)** (Impact: 3.1)
  * `test_supports_fill_type` **(Defensive Guards)** (Impact: 1.9)
  * `test_supports_line_type` **(Defensive Guards)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 42`, `args: 10`, `func_start: 10`
* *Risk/State:* `state_mutation: 31`, `unreferenced_by_name: 9`
* *Architecture:* `api: 10`, `import: 4`
* *Defense:* `safety: 33`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , __future__, contourpy, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `contourpy-1.3.3/src/wrap.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 80.04 | **LOC:** 420 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.8374%), Tech Debt (61.8945%)
**Top Internal Functions/Classes:**
  * `PYBIND11_MODULE` **(Many-Argument Workhorses)** (Impact: 70.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 66`, `args: 44`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`, `planned_debt: 1`, `fragile_debt: 4`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 1`, `import: 10`
* *Defense:* `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.143
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` base_impl.h, contour_generator.h, fill_type.h, line_type.h, mpl2005.h, mpl2014.h, serial.h, threaded.h...
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

- `contourpy-1.3.3/src/base_impl.h` -> **Severity: 0.179** (Bridge: 0.0018 * Flux: 100.0%)
- `contourpy-1.3.3/src/output_array.h` -> **Severity: 0.032** (Bridge: 0.0003 * Flux: 99.8921%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `contourpy-1.3.3/benchmarks/benchmarks/bench_base.py` -> **Severity: 18.689** (Embedded: 0.2 * Error Risk: 93.445%)
- `contourpy-1.3.3/benchmarks/benchmarks/util_bench.py` -> **Severity: 11.279** (Embedded: 0.2 * Error Risk: 56.3934%)
- `contourpy-1.3.3/tests/image_comparison.py` -> **Severity: 6.123** (Embedded: 0.0625 * Error Risk: 97.9728%)
- `contourpy-1.3.3/tests/conftest.py` -> **Severity: 3.639** (Embedded: 0.0409 * Error Risk: 88.9629%)
- `contourpy-1.3.3/src/base_impl.h` -> **Severity: 3.622** (Embedded: 0.0375 * Error Risk: 96.5951%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `contourpy-1.3.3/benchmarks/benchmarks/bench_base.py` -> **Severity: 5571.7** (Blast Radius: 55.717 * Doc Risk: 100.0%)
- `contourpy-1.3.3/benchmarks/benchmarks/util_bench.py` -> **Severity: 5571.7** (Blast Radius: 55.717 * Doc Risk: 100.0%)
- `contourpy-1.3.3/tests/conftest.py` -> **Severity: 3643.7** (Blast Radius: 36.437 * Doc Risk: 100.0%)
- `contourpy-1.3.3/tests/image_comparison.py` -> **Severity: 3446.6** (Blast Radius: 34.466 * Doc Risk: 100.0%)
- `contourpy-1.3.3/src/base.h` -> **Severity: 2652.8** (Blast Radius: 26.528 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
