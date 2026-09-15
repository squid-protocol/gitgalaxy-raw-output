# ARCHITECTURAL_BRIEF: rich
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/Textualize/rich.git` |
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
| Total Artifacts | 553 |
| Analyzed Artifacts (Scanned) | 404 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 149 |
| Total LOC | 25601 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 73.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3024 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2221 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 11.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.5026 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 20 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JSON | 179 | 834 | 44.3% |
| PYTHON | 179 | 24647 | 44.3% |
| MARKDOWN | 39 | 0 | 9.7% |
| XML | 2 | 75 | 0.5% |
| PLAINTEXT | 2 | 0 | 0.5% |
| MAKEFILE | 1 | 15 | 0.2% |
| YAML | 1 | 4 | 0.2% |
| BATCH | 1 | 26 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Typed Library` (z +0.09; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 58%, Generic / Templated Code Files 13%, Interface Declarations Files 8%, Declarative / Non-Code 7%, Defensive Guards Files 4%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 185 | 45.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Minified & Vendor Opaque Mass | 178 | 44.1% |
| Static: Literature & Documentation | 41 | 10.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 149*

**Composition by Extension & Reason:**
- `.rst`: 63x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 2x Excluded (Machine-Generated Source Code Signature: 481 LOC), 1x Excluded (Saturation: Line 94 exceeds 500 chars), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 16x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2386 LOC)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.gif`: 5x Excluded (Explicitly Denied Extension: '.gif')
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 2x Excluded (Unsupported Extension: '.ini')
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ai`: 1x Excluded (Explicitly Denied Extension: '.ai')
- `.bat`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 79.1 | 10.0 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.4 | 30.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.9 | 1.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 94.4 | 11.3 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 94.7 | 0.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 18.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 7.2 | 0.1 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 41.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.1 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 27.6 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 341 | 64 | 1 | `tests/test_text.py` |
| cleanup | 9 | 5 | 0 | `rich/progress.py` |
| guards | 1865 | 119 | 10 | `tests/test_text.py` |
| danger | 504 | 80 | 3 | `rich/console.py` |
| concurrency | 390 | 50 | 2 | `rich/segment.py` |
| connectivity | 1740 | 150 | 9 | `tests/test_console.py` |
| io | 235 | 42 | 1 | `tests/test_win32_console.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 9 | 2 | 0 | `tests/test_console.py` |
| time | 34 | 11 | 0 | `rich/_win32_console.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 17 | 10 | 0 | `tests/test_text.py` |
| events | 13 | 2 | 0 | `tests/test_logging.py` |
| tests | 860 | 59 | 3 | `tests/test_console.py` |
| docs | 913 | 116 | 5 | `rich/console.py` |
| debt | 558 | 114 | 3 | `tests/test_console.py` |
| mutation | 10844 | 170 | 64 | `rich/console.py` |
| dead_code | 666 | 63 | 3 | `tests/test_console.py` |
| credential | 4 | 3 | 0 | `tests/test_text.py` |
| threat | 265 | 51 | 1 | `rich/style.py` |
| ml_ai | 1 | 1 | 0 | `examples/highlighter.py` |
| ui | 171 | 33 | 0 | `tests/test_markup.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/test_win32_console.py` (Hits: 28)
- `tests/test_console.py` (Hits: 24)
- `rich/console.py` (Hits: 21)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **console.py** (`rich/console.py`) — 110 inbound connections
2. **text.py** (`rich/text.py`) — 55 inbound connections
3. **style.py** (`rich/style.py`) — 45 inbound connections
4. **segment.py** (`rich/segment.py`) — 30 inbound connections
5. **measure.py** (`rich/measure.py`) — 26 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **console.py** (`rich/console.py`) — 53 outbound dependencies
2. **progress.py** (`rich/progress.py`) — 31 outbound dependencies
3. **syntax.py** (`rich/syntax.py`) — 27 outbound dependencies
4. **live.py** (`rich/live.py`) — 26 outbound dependencies
5. **pretty.py** (`rich/pretty.py`) — 25 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` **(Many-Argument Workhorses)** (@ `rich/style.py`) -> Impact: **247.8** | LOC: 75
- `__init__` **(Many-Argument Workhorses)** (@ `rich/console.py`) -> Impact: **225.7** | LOC: 133
- `traverse` **(Many-Argument Workhorses)** (@ `rich/pretty.py`) -> Impact: **184.7** | LOC: 296
- `extract` **(Many-Argument Workhorses)** (@ `rich/traceback.py`) -> Impact: **158.6** | LOC: 192
- `_traverse` **(Many-Argument Workhorses)** (@ `rich/pretty.py`) -> Impact: **156.6** | LOC: 252
  * *Intent:* """Walk the object depth first."""
- `_render` **(Many-Argument Workhorses)** (@ `rich/table.py`) -> Impact: **152.2** | LOC: 181
- `export_svg` **(Many-Argument Workhorses)** (@ `rich/console.py`) -> Impact: **122.8** | LOC: 250
- `print` **(Many-Argument Workhorses)** (@ `rich/console.py`) -> Impact: **91.7** | LOC: 102
- `__rich_console__` **(Many-Argument Workhorses)** (@ `rich/columns.py`) -> Impact: **79.5** | LOC: 110
- `__rich_console__` **(Many-Argument Workhorses)** (@ `rich/markdown.py`) -> Impact: **77.9** | LOC: 118

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `rich` | 76 | 17147.84 | 33.74% | 2.63% |
| `tests` | 57 | 3860.16 | 6.51% | 0.0% |
| `examples` | 37 | 842.48 | 15.58% | 0.0% |
| `__monolith__` | 30 | 241.62 | 0.12% | 3.31% |
| `benchmarks/results/darrenburns-2022-mbp` | 177 | 190.68 | 0.0% | 0.0% |
| `benchmarks` | 3 | 154.7 | 6.02% | 33.3% |
| `rich/_unicode_data` | 2 | 77.0 | 22.22% | 0.0% |
| `benchmarks/results` | 1 | 25.3 | 0.0% | 0.0% |
| `questions` | 11 | 11.0 | 0.0% | 0.0% |
| `assets` | 2 | 2.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `benchmarks/benchmarks.py` -> **99.9043%** Exposure
- `Makefile` -> **99.3307%** Exposure
- `rich/highlighter.py` -> **88.9273%** Exposure
- `rich/align.py` -> **44.1118%** Exposure
- `rich/markdown.py` -> **34.4145%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `rich/_inspect.py` -> **100.0%** Exposure
- `rich/_log_render.py` -> **100.0%** Exposure
- `rich/_loop.py` -> **100.0%** Exposure
- `rich/_ratio.py` -> **100.0%** Exposure
- `rich/_unicode_data/__init__.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/test_console.py` -> **92** Orphaned Functions | **4** Duplicates
- `tests/test_text.py` -> **91** Orphaned Functions | **0** Duplicates
- `tests/test_pretty.py` -> **52** Orphaned Functions | **5** Duplicates
- `tests/test_progress.py` -> **37** Orphaned Functions | **0** Duplicates
- `tests/test_segment.py` -> **31** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `812` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `rich/align.py` (PYTHON) -> Cumulative Risk: **665.12**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.08)
- **Magnitude:** 300.46 | **LOC:** 321 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.2056%)
- **Heaviest Functions:** `__rich_console__` (Many-Argument Workhorses, Impact: 70.5), `__init__` (Many-Argument Workhorses, Impact: 25.3), `generate_segments` (Compute Cores, Impact: 17.9)

### 2. `rich/markdown.py` (PYTHON) -> Cumulative Risk: **616.05**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.16)
- **Magnitude:** 625.42 | **LOC:** 794 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (92.2718%), Verification (80.0%)
- **Heaviest Functions:** `__rich_console__` (Many-Argument Workhorses, Impact: 77.9), `__rich_console__` (Many-Argument Workhorses, Impact: 15.2), `__rich_console__` (Compute Cores, Impact: 14.7)

### 3. `benchmarks/benchmarks.py` (PYTHON) -> Cumulative Risk: **603.63**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.41)
- **Magnitude:** 143.18 | **LOC:** 219 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9043%), State Flux (92.2589%), Verification (80.0%)
- **Heaviest Functions:** `time_wrapping_unicode_heavy_warm_cache` (Interface Declarations, Impact: 3.0), `_print_table` (State Mutators, Impact: 2.9), `setup` (Interface Declarations, Impact: 1.9)

### 4. `rich/console.py` (PYTHON) -> Cumulative Risk: **601.68**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +1.33)
- **Magnitude:** 2260.42 | **LOC:** 2685 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (95.5677%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Many-Argument Workhorses, Impact: 225.7), `export_svg` (Many-Argument Workhorses, Impact: 122.8), `print` (Many-Argument Workhorses, Impact: 91.7)

### 5. `rich/containers.py` (PYTHON) -> Cumulative Risk: **592.86**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z -0.44)
- **Magnitude:** 154.46 | **LOC:** 168 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Safety Score (90.9768%)
- **Heaviest Functions:** `justify` (Many-Argument Workhorses, Impact: 46.9), `__rich_measure__` (Generic / Templated Code, Impact: 10.6), `__init__` (Generic / Templated Code, Impact: 5.5)

### 6. `rich/text.py` (PYTHON) -> Cumulative Risk: **589.46**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.39)
- **Magnitude:** 1352.74 | **LOC:** 1364 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.4176%), Api Exposure (88.1599%)
- **Heaviest Functions:** `wrap` (Many-Argument Workhorses, Impact: 42.1), `divide` (Compute Cores, Impact: 35.1), `split` (Many-Argument Workhorses, Impact: 33.5)

### 7. `rich/cells.py` (PYTHON) -> Cumulative Risk: **586.37**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.39)
- **Magnitude:** 280.96 | **LOC:** 353 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (100.0%), Safety Score (98.733%)
- **Heaviest Functions:** `split_graphemes` (Compute Cores, Impact: 29.6), `_cell_len` (Compute Cores, Impact: 21.4), `_split_text` (Many-Argument Workhorses, Impact: 20.1)

### 8. `rich/traceback.py` (PYTHON) -> Cumulative Risk: **585.76**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.41)
- **Magnitude:** 756.4 | **LOC:** 925 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9987%), Safety Score (90.9181%), Documentation (90.2439%)
- **Heaviest Functions:** `extract` (Many-Argument Workhorses, Impact: 158.6), `install` (Many-Argument Workhorses, Impact: 60.4), `__init__` (Many-Argument Workhorses, Impact: 58.0)

### 9. `rich/_log_render.py` (PYTHON) -> Cumulative Risk: **585.09**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +2.40)
- **Magnitude:** 137.42 | **LOC:** 95 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.1661%)
- **Heaviest Functions:** `__call__` (Many-Argument Workhorses, Impact: 69.2), `__init__` (Generic / Templated Code, Impact: 3.6)

### 10. `rich/progress.py` (PYTHON) -> Cumulative Risk: **583.77**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.40)
- **Magnitude:** 1160.7 | **LOC:** 1717 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Safety Score (92.4111%), Verification (80.0%)
- **Heaviest Functions:** `update` (Many-Argument Workhorses, Impact: 47.3), `open` (Many-Argument Workhorses, Impact: 40.3), `track` (Many-Argument Workhorses, Impact: 27.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `rich/console.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2260.42 | **LOC:** 2685 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (47.3033%), Tech Debt (8.6791%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 225.7)
  * `export_svg` **(Many-Argument Workhorses)** (Impact: 122.8)
  * `print` **(Many-Argument Workhorses)** (Impact: 91.7)
  * `render_str` **(Many-Argument Workhorses)** (Impact: 50.4)
  * `export_html` **(Many-Argument Workhorses)** (Impact: 50.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 259 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 868
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 322`, `structural_boundaries: 373`, `args: 116`, `func_start: 116`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 350`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 21`, `api: 96`, `concurrency: 4`, `import: 54`
* *Defense:* `safety: 41`, `doc: 118`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 104.524
  * `Choke Point (Betweenness):` 0.036589 | `Ripple Effect (Closeness):` 0.288239
  * `Imports (Out-Degree: 33):` , ._emoji_replace, ._export_format, ._fileno, ._log_render, ._windows, .align, .color...
  * `Imported By (In-Degree: 110):` (Excluded from Brief to save tokens)

### `rich/text.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1352.74 | **LOC:** 1364 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.3222%), Tech Debt (8.852%)
**Top Internal Functions/Classes:**
  * `wrap` **(Many-Argument Workhorses)** (Impact: 42.1)
  * `divide` **(Compute Cores)** (Impact: 35.1)
    * *Intent:* """Divide text into a number of lines at given offsets. Args: offsets (Iterable[int]): Offsets used ...
  * `split` **(Many-Argument Workhorses)** (Impact: 33.5)
  * `highlight_regex` **(Many-Argument Workhorses)** (Impact: 33.3)
  * `with_indent_guides` **(Many-Argument Workhorses)** (Impact: 31.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 199 instances
* *State Mutation (weighted view):* 631
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 180`, `args: 65`, `func_start: 65`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 233`, `planned_debt: 2`
* *Architecture:* `api: 62`, `import: 22`
* *Defense:* `safety: 16`, `doc: 56`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 44.176
  * `Choke Point (Betweenness):` 0.007027 | `Ripple Effect (Closeness):` 0.215584
  * `Imports (Out-Degree: 15):` ._loop, ._pick, ._wrap, .align, .ansi, .cells, .console, .containers...
  * `Imported By (In-Degree: 55):` (Excluded from Brief to save tokens)

### `rich/progress.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1160.7 | **LOC:** 1717 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (45.4792%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `update` **(Many-Argument Workhorses)** (Impact: 47.3)
  * `open` **(Many-Argument Workhorses)** (Impact: 40.3)
  * `track` **(Many-Argument Workhorses)** (Impact: 27.7)
  * `reset` **(Many-Argument Workhorses)** (Impact: 22.9)
  * `open` **(Many-Argument Workhorses)** (Impact: 21.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 133 instances
* *State Mutation (weighted view):* 461
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 281`, `args: 97`, `func_start: 96`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 195`
* *Architecture:* `io: 8`, `api: 90`, `concurrency: 1`, `import: 34`
* *Defense:* `safety: 7`, `doc: 80`, `sync_locks: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.052
  * `Choke Point (Betweenness):` 0.00159 | `Ripple Effect (Closeness):` 0.019851
  * `Imports (Out-Degree: 11):` , .console, .highlighter, .jupyter, .live, .panel, .progress_bar, .rule...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `rich/table.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1008.76 | **LOC:** 1016 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (47.1189%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_render` **(Many-Argument Workhorses)** (Impact: 152.2)
  * `_calculate_column_widths` **(Many-Argument Workhorses)** (Impact: 65.2)
  * `_get_cells` **(Many-Argument Workhorses)** (Impact: 52.8)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 40.2)
  * `_collapse_widths` **(Many-Argument Workhorses)** (Impact: 37.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 124 instances
* *State Mutation (weighted view):* 423
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 101`, `args: 28`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 175`
* *Architecture:* `api: 24`, `import: 18`
* *Defense:* `safety: 2`, `doc: 43`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.329
  * `Choke Point (Betweenness):` 0.002963 | `Ripple Effect (Closeness):` 0.129137
  * `Imports (Out-Degree: 13):` , ._loop, ._pick, ._ratio, ._timer, .align, .console, .jupyter...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `rich/pretty.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 976.12 | **LOC:** 1017 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (63.4985%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `traverse` **(Many-Argument Workhorses)** (Impact: 184.7)
  * `_traverse` **(Many-Argument Workhorses)** (Impact: 156.6)
    * *Intent:* """Walk the object depth first."""
  * `install` **(Many-Argument Workhorses)** (Impact: 28.0)
  * `_ipy_display_hook` **(Many-Argument Workhorses)** (Impact: 24.4)
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 19.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 104 instances
* *State Mutation (weighted view):* 344
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 155`, `args: 44`, `func_start: 34`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 136`
* *Architecture:* `io: 3`, `api: 25`, `import: 31`
* *Defense:* `safety: 25`, `doc: 24`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.265
  * `Choke Point (Betweenness):` 0.001414 | `Ripple Effect (Closeness):` 0.166681
  * `Imports (Out-Degree: 9):` , ._loop, ._pick, .abc, .cells, .console, .highlighter, .jupyter...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `rich/style.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 925.36 | **LOC:** 793 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.3115%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 247.8)
  * `__str__` **(Compute Cores)** (Impact: 70.1)
    * *Intent:* """Re-generate style definition from attributes."""
  * `_make_ansi_codes` **(Compute Cores)** (Impact: 28.1)
    * *Intent:* """Generate ANSI codes for this style. Args: color_system (ColorSystem): Color system. Returns: str:...
  * `get_html_style` **(Compute Cores)** (Impact: 24.3)
    * *Intent:* """Get a CSS style rule."""
  * `parse` **(Defensive Guards)** (Impact: 24.0)
    * *Intent:* """Parse a style definition. Args: style_definition (str): A string containing a style. Raises: erro...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 329
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 116`, `args: 41`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 149`
* *Architecture:* `io: 1`, `api: 36`, `import: 10`
* *Defense:* `safety: 9`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 36.76
  * `Choke Point (Betweenness):` 0.000902 | `Ripple Effect (Closeness):` 0.210368
  * `Imports (Out-Degree: 2):` , .color, .repr, .terminal_theme, functools, operator, pickle, random...
  * `Imported By (In-Degree: 45):` (Excluded from Brief to save tokens)

### `rich/traceback.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 756.4 | **LOC:** 925 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (56.2705%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `extract` **(Many-Argument Workhorses)** (Impact: 158.6)
  * `install` **(Many-Argument Workhorses)** (Impact: 60.4)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 58.0)
  * `_render_stack` **(Many-Argument Workhorses)** (Impact: 44.5)
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 31.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 244
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 112`, `args: 21`, `func_start: 20`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 108`, `dead_code: 2`
* *Architecture:* `io: 15`, `api: 21`, `import: 28`
* *Defense:* `safety: 12`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.401
  * `Choke Point (Betweenness):` 0.001367 | `Ripple Effect (Closeness):` 0.163546
  * `Imports (Out-Degree: 9):` , ._loop, .columns, .console, .constrain, .highlighter, .panel, .scope...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `rich/syntax.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 680.42 | **LOC:** 986 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.4446%), Tech Debt (14.7705%)
**Top Internal Functions/Classes:**
  * `_get_syntax` **(Many-Argument Workhorses)** (Impact: 76.8)
  * `highlight` **(Many-Argument Workhorses)** (Impact: 46.2)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 17.9)
  * `_apply_stylized_ranges` **(Compute Cores)** (Impact: 17.2)
    * *Intent:* """ Apply stylized ranges to a text instance, using the given code to determine the right portion to...
  * `guess_lexer` **(Defensive Guards)** (Impact: 16.0)
    * *Intent:* """Guess the alias of the Pygments lexer to use based on a path and an optional string of code. If c...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 100 instances
* *State Mutation (weighted view):* 329
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 133`, `args: 31`, `func_start: 31`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 129`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `api: 24`, `import: 28`
* *Defense:* `safety: 20`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.696
  * `Choke Point (Betweenness):` 0.001198 | `Ripple Effect (Closeness):` 0.136932
  * `Imports (Out-Degree: 12):` ._loop, .cells, .color, .console, .jupyter, .measure, .segment, .style...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `rich/segment.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 632.1 | **LOC:** 784 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (43.2876%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `divide` **(Many-Argument Workhorses)** (Impact: 33.4)
  * `adjust_line_length` **(Many-Argument Workhorses)** (Impact: 29.1)
  * `split_and_crop_lines` **(Many-Argument Workhorses)** (Impact: 28.7)
  * `apply_style` **(Many-Argument Workhorses)** (Impact: 26.5)
  * `_split_cells` **(Many-Argument Workhorses)** (Impact: 22.3)
    * *Intent:* """Split a segment in to two at a given cell position. Note that splitting a double-width character,...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 81 instances
* *State Mutation (weighted view):* 266
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 95`, `args: 28`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 104`
* *Architecture:* `api: 27`, `import: 13`
* *Defense:* `safety: 3`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.14
  * `Choke Point (Betweenness):` 0.00286 | `Ripple Effect (Closeness):` 0.189026
  * `Imports (Out-Degree: 6):` .cells, .console, .repr, .style, enum, functools, itertools, logging...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `rich/markdown.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 625.42 | **LOC:** 794 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (46.8124%), Tech Debt (34.4145%)
**Top Internal Functions/Classes:**
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 77.9)
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 15.2)
  * `__rich_console__` **(Compute Cores)** (Impact: 14.7)
  * `create` **(Defensive Guards)** (Impact: 12.8)
  * `_flatten_tokens` **(Compute Cores)** (Impact: 10.8)
    * *Intent:* """Flattens the token stream."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 66 instances
* *State Mutation (weighted view):* 265
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 161`, `args: 57`, `func_start: 57`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 133`, `duplicate_logic: 4`
* *Architecture:* `io: 2`, `api: 51`, `import: 23`
* *Defense:* `safety: 15`, `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.083
  * `Choke Point (Betweenness):` 0.000994 | `Ripple Effect (Closeness):` 0.113911
  * `Imports (Out-Degree: 11):` , ._loop, ._stack, .console, .containers, .jupyter, .rule, .segment...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tests/test_console.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 563.58 | **LOC:** 1130 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.7041%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_size_can_fall_back_to_std_descriptors` **(Generic / Templated Code)** (Impact: 7.0)
  * `test_console_options_update` **(Defensive Guards)** (Impact: 6.1)
  * `test_brokenpipeerror` **(Defensive Guards)** (Impact: 4.8)
    * *Intent:* """Test BrokenPipe works as expected."""
  * `test_tty_compatible` **(Interface Declarations)** (Impact: 4.2)
    * *Intent:* """Check TTY_COMPATIBLE environment var."""
  * `get_terminal_size_mock_impl` **(Generic / Templated Code)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 23 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 351`, `args: 112`, `func_start: 110`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 3`, `state_mutation: 206`, `duplicate_logic: 4`, `unreferenced_by_name: 92`
* *Architecture:* `io: 24`, `api: 109`, `import: 24`
* *Defense:* `safety: 137`, `doc: 8`, `test: 117`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` datetime, io, os, pytest, rich, rich._null_file, rich.color, rich.console...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_text.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 453.32 | **LOC:** 1130 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (20.0478%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_highlight_regex` **(I/O & Config Routines)** (Impact: 4.3)
    * *Intent:* # As a string text = Text("peek-a-boo") count = text.highlight_regex(r"NEVER_MATCH", "red") assert c...
  * `test_divide` **(Defensive Guards)** (Impact: 3.1)
  * `test_indentation_guides` **(I/O & Config Routines)** (Impact: 3.0)
  * `test_highlight_regex_callable` **(Defensive Guards)** (Impact: 2.7)
  * `test_tabs_to_spaces_spans` **(Defensive Guards)** (Impact: 2.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 206
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 354`, `args: 92`, `func_start: 92`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 202`, `unreferenced_by_name: 91`
* *Architecture:* `api: 92`, `import: 8`
* *Defense:* `safety: 235`, `doc: 16`, `test: 100`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` io, pytest, re, rich.console, rich.measure, rich.style, rich.text, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_pretty.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 396.72 | **LOC:** 760 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (30.3487%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_attrs_broken_310` **(Tests & Verification)** (Impact: 3.7)
  * `test_pretty_namedtuple` **(I/O & Config Routines)** (Impact: 2.2)
  * `test_reference_cycle_custom_repr` **(Interface Declarations)** (Impact: 2.2)
  * `test_deque` **(Defensive Guards)** (Impact: 2.2)
  * `test_ipy_display_hook__special_repr_raises_exception` **(Interface Declarations)** (Impact: 2.1)
    * *Intent:* """ When an IPython special repr method raises an exception, we treat it as if it doesn't exist and ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 179
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 235`, `args: 77`, `func_start: 77`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 157`, `duplicate_logic: 5`, `unreferenced_by_name: 52`
* *Architecture:* `io: 21`, `api: 85`, `import: 14`
* *Defense:* `safety: 80`, `doc: 11`, `test: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` array, attr, collections, dataclasses, io, pytest, rich.console, rich.measure...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rich/layout.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 341.52 | **LOC:** 443 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.4803%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 15.1)
  * `split` **(Defensive Guards)** (Impact: 13.2)
  * `render` **(Many-Argument Workhorses)** (Impact: 11.4)
    * *Intent:* """Render the sub_layouts. Args: console (Console): Console instance. options (ConsoleOptions): Cons...
  * `_make_region_map` **(Generic / Templated Code)** (Impact: 11.0)
    * *Intent:* """Create a dict that maps layout on to Region."""
  * `get` **(Generic / Templated Code)** (Impact: 9.5)
    * *Intent:* """Get a named layout, or None if it doesn't exist. Args: name (str): Name of layout. Returns: Optio...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 95`, `args: 28`, `func_start: 28`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 65`
* *Architecture:* `api: 30`, `concurrency: 1`, `import: 20`
* *Defense:* `safety: 5`, `doc: 24`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.387
  * `Choke Point (Betweenness):` 8.7e-05 | `Ripple Effect (Closeness):` 0.004963
  * `Imports (Out-Degree: 12):` ._ratio, .align, .console, .highlighter, .panel, .pretty, .region, .repr...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `rich/color.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 323.56 | **LOC:** 622 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.2942%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `downgrade` **(Defensive Guards)** (Impact: 42.6)
    * *Intent:* """Downgrade a color system to a system with fewer colors."""
  * `get_ansi_codes` **(Defensive Guards)** (Impact: 35.9)
    * *Intent:* """Get the ANSI escape codes for this color."""
  * `parse` **(Compute Cores)** (Impact: 30.2)
    * *Intent:* """Parse a color definition."""
  * `get_truecolor` **(Defensive Guards)** (Impact: 19.5)
  * `from_ansi` **(Generic / Templated Code)** (Impact: 5.9)
    * *Intent:* """Create a Color number from it's 8-bit ansi number. Args: number (int): A number between 0-255 inc...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 124`, `args: 18`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `state_mutation: 54`
* *Architecture:* `io: 1`, `api: 20`, `import: 17`
* *Defense:* `safety: 15`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.618
  * `Choke Point (Betweenness):` 0.002455 | `Ripple Effect (Closeness):` 0.175071
  * `Imports (Out-Degree: 6):` ._palettes, .color_triplet, .console, .repr, .style, .table, .terminal_theme, .text...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `tests/test_progress.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 320.44 | **LOC:** 691 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (32.4369%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_columns` **(I/O & Config Routines)** (Impact: 4.2)
  * `test_using_default_columns` **(I/O & Config Routines)** (Impact: 4.2)
    * *Intent:* # can only check types, as the instances do not '==' each other expected_default_types = [ TextColum...
  * `test_progress_max_refresh` **(I/O & Config Routines)** (Impact: 3.9)
    * *Intent:* """Test max_refresh argument."""
  * `test_track` **(I/O & Config Routines)** (Impact: 3.4)
  * `test_progress_track` **(I/O & Config Routines)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 180
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 189`, `args: 57`, `func_start: 44`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 142`, `unreferenced_by_name: 37`
* *Architecture:* `io: 12`, `api: 44`, `import: 13`
* *Defense:* `safety: 89`, `doc: 2`, `test: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.087
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` .render, io, os, pytest, rich.console, rich.highlighter, rich.progress, rich.progress_bar...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rich/align.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 300.46 | **LOC:** 321 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (74.0716%), Tech Debt (44.1118%)
**Top Internal Functions/Classes:**
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 70.5)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 25.3)
  * `generate_segments` **(Compute Cores)** (Impact: 17.9)
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 17.3)
  * `blank_lines` **(Generic / Templated Code)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 53`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `state_mutation: 52`, `duplicate_logic: 2`
* *Architecture:* `api: 8`, `import: 11`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.0
  * `Choke Point (Betweenness):` 0.001825 | `Ripple Effect (Closeness):` 0.173904
  * `Imports (Out-Degree: 8):` .console, .constrain, .jupyter, .measure, .segment, .style, itertools, rich.align...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `rich/live.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 296.62 | **LOC:** 405 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.446%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `stop` **(Compute Cores)** (Impact: 24.5)
    * *Intent:* """Stop live rendering display."""
  * `__init__` **(Many-Argument Workhorses)** (Impact: 19.3)
  * `refresh` **(Defensive Guards)** (Impact: 17.2)
    * *Intent:* """Update the display of the Live Render."""
  * `start` **(Compute Cores)** (Impact: 12.0)
    * *Intent:* """Start live rendering display. Args: refresh (bool, optional): Also refresh. Defaults to False. ""...
  * `process_renderables` **(Generic / Templated Code)** (Impact: 11.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 97`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 54`, `dead_code: 2`
* *Architecture:* `io: 10`, `api: 13`, `concurrency: 1`, `import: 28`
* *Defense:* `safety: 10`, `doc: 12`, `sync_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.199
  * `Choke Point (Betweenness):` 0.002513 | `Ripple Effect (Closeness):` 0.168839
  * `Imports (Out-Degree: 10):` , .align, .console, .control, .file_proxy, .jupyter, .live, .live_render...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `rich/_inspect.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 284.14 | **LOC:** 273 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (49.8053%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_render` **(Compute Cores)** (Impact: 51.3)
    * *Intent:* """Render object."""
  * `__init__` **(Many-Argument Workhorses)** (Impact: 18.6)
  * `_get_signature` **(Defensive Guards)** (Impact: 18.1)
    * *Intent:* """Get a signature for a callable."""
  * `_make_title` **(Type Conversions)** (Impact: 9.1)
    * *Intent:* """Make a default title."""
  * `_get_formatted_doc` **(Generic / Templated Code)** (Impact: 6.2)
    * *Intent:* """ Extract the docstring of an object, process it and returns it. The processing consists in cleani...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 47 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 58`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 50`
* *Architecture:* `api: 8`, `concurrency: 1`, `import: 11`
* *Defense:* `safety: 8`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.78
  * `Choke Point (Betweenness):` 8e-05 | `Ripple Effect (Closeness):` 0.004963
  * `Imports (Out-Degree: 6):` .console, .control, .highlighter, .jupyter, .panel, .pretty, .table, .text...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `rich/cells.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 280.96 | **LOC:** 353 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.9658%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `split_graphemes` **(Compute Cores)** (Impact: 29.6)
  * `_cell_len` **(Compute Cores)** (Impact: 21.4)
    * *Intent:* """Get the cell length of a string (length as it appears in the terminal). Args: text: String to mea...
  * `_split_text` **(Many-Argument Workhorses)** (Impact: 20.1)
  * `get_character_cell_size` **(Compute Cores)** (Impact: 17.2)
    * *Intent:* """Get the cell size of a character. Args: character (str): A single character. unicode_version: Uni...
  * `chop_cells` **(Many-Argument Workhorses)** (Impact: 13.3)
    * *Intent:* """Split text into lines such that each line fits within the available (cell) width. Args: text: The...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 143
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 49`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 51`
* *Architecture:* `api: 8`, `import: 5`
* *Defense:* `doc: 10`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.562
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.179444
  * `Imports (Out-Degree: 0):` __future__, functools, operator, rich._unicode_data, typing
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `rich/_win32_console.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 269.88 | **LOC:** 662 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.3828%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `write_styled` **(Many-Argument Workhorses)** (Impact: 25.9)
    * *Intent:* """Write styled text to the terminal. Args: text (str): The text to write style (Style): The style o...
  * `move_cursor_to` **(Generic / Templated Code)** (Impact: 5.6)
    * *Intent:* """Set the position of the cursor Args: new_position (WindowsCoordinates): The WindowsCoordinates re...
  * `move_cursor_forward` **(Generic / Templated Code)** (Impact: 4.8)
    * *Intent:* """Move the cursor forward a single cell. Wrap to the next line if required."""
  * `move_cursor_backward` **(Generic / Templated Code)** (Impact: 4.8)
    * *Intent:* """Move the cursor backward a single cell. Wrap to the previous line if required."""
  * `GetConsoleMode` **(Compute Cores)** (Impact: 3.8)
    * *Intent:* """Retrieves the current input mode of a console's input buffer or the current output mode of a cons...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 68`, `args: 29`, `func_start: 29`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 90`
* *Architecture:* `io: 2`, `api: 33`, `import: 9`
* *Defense:* `safety: 3`, `doc: 31`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.392
  * `Choke Point (Betweenness):` 0.00093 | `Ripple Effect (Closeness):` 0.164578
  * `Imports (Out-Degree: 3):` ctypes, rich.color, rich.console, rich.style, sys, time, typing
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `rich/tree.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 265.24 | **LOC:** 258 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.3822%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 72.5)
  * `add` **(Many-Argument Workhorses)** (Impact: 20.0)
  * `make_guide` **(Compute Cores)** (Impact: 16.0)
    * *Intent:* """Make a Segment for a level of the guide lines."""
  * `__rich_measure__` **(Defensive Guards)** (Impact: 9.3)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 39`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 62`
* *Architecture:* `api: 6`, `import: 13`
* *Defense:* `safety: 4`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.717
  * `Choke Point (Betweenness):` 0.000283 | `Ripple Effect (Closeness):` 0.008862
  * `Imports (Out-Degree: 11):` ._loop, .console, .jupyter, .measure, .segment, .style, .styled, rich.console...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `rich/progress_bar.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 255.64 | **LOC:** 224 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.8498%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__rich_console__` **(Compute Cores)** (Impact: 56.1)
  * `_get_pulse_segments` **(Many-Argument Workhorses)** (Impact: 34.0)
  * `_render_pulse` **(Many-Argument Workhorses)** (Impact: 8.2)
  * `update` **(Generic / Templated Code)** (Impact: 6.5)
    * *Intent:* """Update progress with new values. Args: completed (float): Number of steps completed. total (float...
  * `__rich_measure__` **(Generic / Templated Code)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 40`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 51`
* *Architecture:* `api: 7`, `import: 12`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.631
  * `Choke Point (Betweenness):` 9e-05 | `Ripple Effect (Closeness):` 0.012562
  * `Imports (Out-Degree: 7):` .color, .color_triplet, .console, .jupyter, .measure, .segment, .style, functools...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `rich/columns.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 250.9 | **LOC:** 188 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.0337%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 79.5)
  * `iter_renderables` **(Compute Cores)** (Impact: 18.6)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 7.7)
  * `add_renderable` **(Generic / Templated Code)** (Impact: 2.1)
    * *Intent:* """Add a renderable to the columns. Args: renderable (RenderableType): Any renderable object. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 35`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 49`
* *Architecture:* `io: 1`, `api: 5`, `import: 13`
* *Defense:* `safety: 1`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.536
  * `Choke Point (Betweenness):` 0.000285 | `Ripple Effect (Closeness):` 0.118302
  * `Imports (Out-Degree: 6):` .align, .console, .constrain, .jupyter, .measure, .padding, .table, .text...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `rich/panel.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 237.0 | **LOC:** 318 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.4687%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 60.8)
  * `align_text` **(Many-Argument Workhorses)** (Impact: 17.0)
  * `__rich_measure__` **(Many-Argument Workhorses)** (Impact: 11.1)
  * `_title` **(Defensive Guards)** (Impact: 6.4)
  * `_subtitle` **(Defensive Guards)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 49`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 51`
* *Architecture:* `api: 6`, `import: 14`
* *Defense:* `safety: 2`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.536
  * `Choke Point (Betweenness):` 0.00177 | `Ripple Effect (Closeness):` 0.139495
  * `Imports (Out-Degree: 9):` .align, .box, .cells, .console, .jupyter, .measure, .padding, .segment...
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `rich/console.py` -> **Will McGugan** (100.0% isolated ownership) | Magnitude: 2260.42
- `rich/text.py` -> **Will McGugan** (100.0% isolated ownership) | Magnitude: 1352.74
- `rich/table.py` -> **Will McGugan** (100.0% isolated ownership) | Magnitude: 1008.76
- `rich/pretty.py` -> **Joel Ostblom** (100.0% isolated ownership) | Magnitude: 976.12
- `rich/style.py` -> **Will McGugan** (100.0% isolated ownership) | Magnitude: 925.36

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `rich/console.py` -> **Severity: 3.659** (Bridge: 0.0366 * Flux: 100.0%)
- `rich/text.py` -> **Severity: 0.703** (Bridge: 0.007 * Flux: 100.0%)
- `rich/__main__.py` -> **Severity: 0.304** (Bridge: 0.0031 * Flux: 99.6316%)
- `rich/table.py` -> **Severity: 0.296** (Bridge: 0.003 * Flux: 100.0%)
- `rich/segment.py` -> **Severity: 0.286** (Bridge: 0.0029 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `rich/console.py` -> **Severity: 27.546** (Embedded: 0.2882 * Error Risk: 95.5677%)
- `rich/text.py` -> **Severity: 21.217** (Embedded: 0.2156 * Error Risk: 98.4176%)
- `rich/style.py` -> **Severity: 20.514** (Embedded: 0.2104 * Error Risk: 97.5142%)
- `rich/segment.py` -> **Severity: 18.265** (Embedded: 0.189 * Error Risk: 96.6276%)
- `rich/jupyter.py` -> **Severity: 18.007** (Embedded: 0.1812 * Error Risk: 99.4059%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `rich/console.py` -> **Severity: 4816.299** (Blast Radius: 104.524 * Doc Risk: 46.0784%)
- `rich/terminal_theme.py` -> **Severity: 2772.0** (Blast Radius: 27.72 * Doc Risk: 100.0%)
- `rich/text.py` -> **Severity: 2049.766** (Blast Radius: 44.176 * Doc Risk: 46.4%)
- `rich/segment.py` -> **Severity: 1281.372** (Blast Radius: 26.14 * Doc Risk: 49.0196%)
- `rich/palette.py` -> **Severity: 1114.21** (Blast Radius: 17.509 * Doc Risk: 63.6364%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
