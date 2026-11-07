# ARCHITECTURAL_BRIEF: matplotlib
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1894 analyzed artifact(s), 217183 LOC.
- **Load-bearing artifact:** `matplotlib-3.10.8/lib/matplotlib/pyplot.py` -- 630 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `matplotlib-3.10.8/lib/matplotlib/pyplot.py` -- pulls in 51 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `matplotlib-3.10.8/lib/matplotlib/axes/_axes.py` at magnitude 6789.34 (structural weight, not risk).
- **How to read this brief:** section 11 ranks artifacts by structural magnitude with a blast-radius line each; section 7 has the full dependency graph. The surface vectors in section 6 describe what is present in a file, not the probability of a defect -- Appendix A has the equations and the validation record behind that distinction.

## 1.5 SYSTEM ROLE & PHILOSOPHY
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
> *(Section 2, the structural-surface lexicon and its equations, is now **Appendix A** at the end of this brief -- the findings come first.)*

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 4376 |
| Analyzed Artifacts (Scanned) | 1894 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2482 |
| Total LOC | 217183 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 43.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5685 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3646 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.6258 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 45 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 985 | 152259 | 52.0% |
| XML | 570 | 0 | 30.1% |
| CPP | 211 | 57112 | 11.1% |
| PLAINTEXT | 50 | 0 | 2.6% |
| YAML | 29 | 2074 | 1.5% |
| HTML | 11 | 217 | 0.6% |
| JSON | 10 | 2504 | 0.5% |
| MARKDOWN | 9 | 0 | 0.5% |
| CSS | 6 | 393 | 0.3% |
| JAVASCRIPT | 3 | 756 | 0.2% |
| SHELL | 2 | 37 | 0.1% |
| CSV | 2 | 77 | 0.1% |
| MAKEFILE | 1 | 31 | 0.1% |
| BATCH | 1 | 55 | 0.1% |
| LUA | 1 | 2 | 0.1% |
| BMS | 1 | 33 | 0.1% |
| OBJECTIVE-C | 1 | 1617 | 0.1% |
| C | 1 | 16 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 1894 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 39%, Declarative / Non-Code 20%, Parameter Forwarders Files 12%, Large Core Modules (3) 11%, Generic / Templated Code Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1835 | 96.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 59 | 3.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2482*

**Composition by Extension & Reason:**
- `.png`: 1373x Excluded (Explicitly Denied Extension: '.png')
- `.pdf`: 515x Excluded (Explicitly Denied Extension: '.pdf')
- `.rst`: 341x Excluded (Unsupported Extension: '.rst')
- `.afm`: 60x Excluded (Unsupported Extension: '.afm')
- `.ttf`: 39x Excluded (Explicitly Denied Extension: '.ttf')
- `.mplstyle`: 29x Excluded (Unsupported Extension: '.mplstyle')
- `.build`: 27x Excluded (Unsupported Extension: '.build')
- `.svg`: 1x Excluded (Embedded Array/Matrix Payload: 6995 commas in 553 LOC), 1x Excluded (Massive Static Asset Blob: 3172 LOC), 1x Excluded (Static Asset Blob without Intent: 1028 LOC)
- `no_extension`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 814 LOC)
- `.eps`: 11x Excluded (Explicitly Denied Extension: '.eps')
- `.py`: 1x Excluded (Saturation: Line 18 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 374 LOC), 1x Excluded (Embedded Array/Matrix Payload: 12940 commas in 1313 LOC)
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 274, Signals: 0)
- `.ipynb`: 3x Excluded (Unsupported Extension: '.ipynb')
- `.npz`: 3x Excluded (Unsupported Extension: '.npz')
- `.json`: 1x Excluded (Static Asset Blob without Intent: 1412 LOC), 1x Excluded (Static Asset Blob without Intent: 1296 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 16.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.1 | 37.8 | 52.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 8.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 11.1 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 10.3 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 99.8 | 0.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 21.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 76.7 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 36.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2626 | 435 | 3 | `matplotlib-3.10.8/src/_macosx.m` |
| cleanup | 273 | 91 | 0 | `matplotlib-3.10.8/lib/matplotlib/tests/test_figure.py` |
| guards | 14041 | 549 | 18 | `matplotlib-3.10.8/lib/matplotlib/tests/test_axes.py` |
| danger | 3213 | 398 | 3 | `matplotlib-3.10.8/lib/matplotlib/axes/_axes.py` |
| concurrency | 267 | 78 | 0 | `matplotlib-3.10.8/lib/matplotlib/widgets.pyi` |
| connectivity | 13489 | 738 | 18 | `matplotlib-3.10.8/lib/matplotlib/tests/test_axes.py` |
| io | 762 | 166 | 0 | `matplotlib-3.10.8/lib/matplotlib/tests/test_backends_interactive.py` |
| crypto | 5 | 5 | 0 | `matplotlib-3.10.8/lib/matplotlib/__init__.py` |
| ipc | 106 | 28 | 0 | `matplotlib-3.10.8/lib/matplotlib/tests/test_backends_interactive.py` |
| time | 464 | 43 | 0 | `matplotlib-3.10.8/lib/matplotlib/tests/test_dates.py` |
| serialization | 27 | 7 | 0 | `matplotlib-3.10.8/lib/matplotlib/tests/test_pickle.py` |
| regex | 76 | 34 | 0 | `matplotlib-3.10.8/lib/matplotlib/_type1font.py` |
| events | 218 | 64 | 0 | `matplotlib-3.10.8/lib/matplotlib/axes/_base.py` |
| tests | 5201 | 179 | 0 | `matplotlib-3.10.8/lib/matplotlib/tests/test_axes.py` |
| docs | 5397 | 860 | 4 | `matplotlib-3.10.8/lib/matplotlib/patches.py` |
| debt | 1830 | 279 | 2 | `matplotlib-3.10.8/extern/agg24-svn/include/agg_pixfmt_rgba.h` |
| mutation | 102960 | 1179 | 119 | `matplotlib-3.10.8/lib/matplotlib/tests/test_axes.py` |
| dead_code | 4168 | 312 | 3 | `matplotlib-3.10.8/lib/matplotlib/tests/test_axes.py` |
| credential | 8 | 2 | 0 | `matplotlib-3.10.8/doc/_static/quiver_sizes.svg` |
| threat | 9 | 3 | 0 | `matplotlib-3.10.8/lib/matplotlib/tests/test_ft2font.py` |
| ml_ai | 3408 | 905 | 5 | `matplotlib-3.10.8/lib/matplotlib/pyplot.py` |
| ui | 63 | 23 | 0 | `matplotlib-3.10.8/src/_macosx.m` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `matplotlib-3.10.8/lib/matplotlib/tests/test_backends_interactive.py` (Hits: 45)
- `matplotlib-3.10.8/lib/matplotlib/sphinxext/plot_directive.py` (Hits: 32)
- `matplotlib-3.10.8/lib/matplotlib/cbook.py` (Hits: 28)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **pyplot.py** (`matplotlib-3.10.8/lib/matplotlib/pyplot.py`) — 630 inbound connections
2. **__init__.py** (`matplotlib-3.10.8/lib/matplotlib/__init__.py`) — 267 inbound connections
3. **agg_basics.h** (`matplotlib-3.10.8/extern/agg24-svn/include/agg_basics.h`) — 126 inbound connections
4. **cbook.py** (`matplotlib-3.10.8/lib/matplotlib/cbook.py`) — 98 inbound connections
5. **__init__.py** (`matplotlib-3.10.8/lib/matplotlib/_api/__init__.py`) — 92 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **pyplot.py** (`matplotlib-3.10.8/lib/matplotlib/pyplot.py`) — 51 outbound dependencies
2. **test_axes.py** (`matplotlib-3.10.8/lib/matplotlib/tests/test_axes.py`) — 39 outbound dependencies
3. **__init__.py** (`matplotlib-3.10.8/lib/matplotlib/__init__.py`) — 37 outbound dependencies
4. **_axes.py** (`matplotlib-3.10.8/lib/matplotlib/axes/_axes.py`) — 36 outbound dependencies
5. **test_backends_interactive.py** (`matplotlib-3.10.8/lib/matplotlib/tests/test_backends_interactive.py`) — 33 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `hist` **(Many-Argument Workhorses)** (@ `matplotlib-3.10.8/lib/matplotlib/axes/_axes.py`) -> Impact: **474.9** | LOC: 504
  * *Intent:* #### Data analysis
- `platform_specific::put_image` **(Compute Cores)** (@ `matplotlib-3.10.8/extern/agg24-svn/src/platform/X11/agg_platform_support.cpp`) -> Impact: **449.5** | LOC: 221
  * *Intent:* //------------------------------------------------------------------------
- `platform_specific::load_pmap` **(Many-Argument Workhorses)** (@ `matplotlib-3.10.8/extern/agg24-svn/src/platform/win32/agg_platform_support.cpp`) -> Impact: **387.4** | LOC: 267
  * *Intent:* //------------------------------------------------------------------------
- `add` **(Many-Argument Workhorses)** (@ `matplotlib-3.10.8/lib/matplotlib/sankey.py`) -> Impact: **378.1** | LOC: 426
  * *Intent:* # This might be more efficient, but it fails because 'tuple' object # doesn't support item assignment: # path[1] = path[1][-1:0:-1] # path[1][0] = fir...
- `__init__` **(Many-Argument Workhorses)** (@ `matplotlib-3.10.8/lib/matplotlib/legend.py`) -> Impact: **331.8** | LOC: 267
- `bxp` **(Many-Argument Workhorses)** (@ `matplotlib-3.10.8/lib/matplotlib/axes/_axes.py`) -> Impact: **303.0** | LOC: 377
- `errorbar` **(Many-Argument Workhorses)** (@ `matplotlib-3.10.8/lib/matplotlib/axes/_axes.py`) -> Impact: **286.1** | LOC: 376
- `hexbin` **(Many-Argument Workhorses)** (@ `matplotlib-3.10.8/lib/matplotlib/axes/_axes.py`) -> Impact: **268.6** | LOC: 400
- `boxplot` **(Many-Argument Workhorses)** (@ `matplotlib-3.10.8/lib/matplotlib/axes/_axes.py`) -> Impact: **240.0** | LOC: 345
- `markers` **(Compute Cores)** (@ `matplotlib-3.10.8/extern/agg24-svn/include/agg_renderer_markers.h`) -> Impact: **213.4** | LOC: 26
  * *Intent:* //--------------------------------------------------------------------

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `matplotlib-3.10.8/lib/matplotlib` | 132 | 69026.44 | 24.33% | 31.54% |
| `matplotlib-3.10.8/extern/agg24-svn/include` | 127 | 30017.5 | 42.73% | 33.93% |
| `matplotlib-3.10.8/lib/matplotlib/tests` | 94 | 27594.14 | 24.46% | 0.0% |
| `matplotlib-3.10.8/lib/matplotlib/backends` | 39 | 12882.5 | 37.75% | 22.94% |
| `matplotlib-3.10.8/lib/matplotlib/axes` | 8 | 11641.92 | 20.62% | 2.06% |
| `matplotlib-3.10.8/src` | 26 | 6366.92 | 33.11% | 19.8% |
| `matplotlib-3.10.8/lib/mpl_toolkits/mplot3d` | 5 | 5370.3 | 37.36% | 24.53% |
| `matplotlib-3.10.8/lib/matplotlib/tests/baseline_images/test_mathtext` | 391 | 4113.32 | 0.0% | 0.0% |
| `matplotlib-3.10.8/extern/agg24-svn/src` | 28 | 3468.32 | 55.96% | 63.56% |
| `matplotlib-3.10.8/extern/agg24-svn/src/ctrl` | 9 | 2750.42 | 81.31% | 91.8% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `matplotlib-3.10.8/lib/matplotlib/_tri.pyi` -> **100.0%** Exposure
- `matplotlib-3.10.8/lib/matplotlib/animation.pyi` -> **100.0%** Exposure
- `matplotlib-3.10.8/lib/matplotlib/axis.pyi` -> **100.0%** Exposure
- `matplotlib-3.10.8/lib/matplotlib/backend_tools.pyi` -> **100.0%** Exposure
- `matplotlib-3.10.8/lib/matplotlib/cbook.pyi` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `matplotlib-3.10.8/.circleci/fetch_doc_logs.py` -> **100.0%** Exposure
- `matplotlib-3.10.8/ci/schemas/vendor_schemas.py` -> **100.0%** Exposure
- `matplotlib-3.10.8/doc/conf.py` -> **100.0%** Exposure
- `matplotlib-3.10.8/doc/sphinxext/github.py` -> **100.0%** Exposure
- `matplotlib-3.10.8/doc/sphinxext/math_symbol_table.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `matplotlib-3.10.8/lib/matplotlib/tests/test_axes.py` -> **582** Orphaned Functions | **11** Duplicates
- `matplotlib-3.10.8/lib/mpl_toolkits/mplot3d/tests/test_axes3d.py` -> **135** Orphaned Functions | **0** Duplicates
- `matplotlib-3.10.8/lib/matplotlib/tests/test_legend.py` -> **110** Orphaned Functions | **0** Duplicates
- `matplotlib-3.10.8/lib/matplotlib/tests/test_figure.py` -> **100** Orphaned Functions | **0** Duplicates
- `matplotlib-3.10.8/src/tri/_tri.cpp` -> **100** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `12` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5378` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `matplotlib-3.10.8/lib/matplotlib/axes/_axes.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.246)
- **Top Global Matches:** file_cluster_6: 6.246, file_cluster_4: 12.359, file_cluster_8: 13.285
- **Magnitude:** 6789.34 | **LOC:** 8872 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **36**; blast radius 7.228; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.0%), Complexity Load (formerly Cognitive Load) (71.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 62.1302% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hist` **(Many-Argument Workhorses)** (Impact: 474.9)
    * *Intent:* #### Data analysis
  * `bxp` **(Many-Argument Workhorses)** (Impact: 303.0)
  * `errorbar` **(Many-Argument Workhorses)** (Impact: 286.1)
  * `hexbin` **(Many-Argument Workhorses)** (Impact: 268.6)
  * `boxplot` **(Many-Argument Workhorses)** (Impact: 240.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 813 instances
* *State Mutation (weighted view):* 2620
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 927`, `structural_boundaries: 303`, `args: 91`, `func_start: 90`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 994`
* *Architecture:* `api: 77`, `import: 38`
* *Defense:* `safety: 55`, `doc: 73`, `test: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.228
  * `Choke Point (Betweenness):` 0.008874 | `Ripple Effect (Closeness):` 0.198067
  * `Imports (Out-Degree: 25):` builtins, functools, itertools, logging, math, matplotlib, matplotlib.axes._base, matplotlib.axes._secondary_axes...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/lib/matplotlib/tests/test_axes.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 10.577)
- **Top Global Matches:** file_cluster_15: 10.577, file_cluster_12: 10.917, file_cluster_11: 11.055
- **Magnitude:** 5093.8 | **LOC:** 9666 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **39**; blast radius 0.136; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (39.4%), Connectivity (formerly Api Exposure) (13.8%)
- **Documentation Coverage:** 94.2948% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_wrong_use_colorizer` **(Compute Cores)** (Impact: 31.9)
    * *Intent:* # test using the colorizer keyword and norm or cmap np.random.seed(0) rand_x = np.random.random(100)...
  * `test_scatter_c` **(Defensive Guards)** (Impact: 17.1)
  * `test_axis_method_errors` **(Compute Cores)** (Impact: 16.2)
  * `test_plot_format_errors` **(Compute Cores)** (Impact: 14.3)
  * `test_indicate_inset_inverted` **(Defensive Guards)** (Impact: 13.2)
    * *Intent:* """ Test that the inset lines are correctly located with inverted data axes. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 467 instances
* *State Mutation (weighted view):* 2609
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 535`, `structural_boundaries: 1559`, `args: 636`, `func_start: 627`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 1675`, `planned_debt: 2`, `fragile_debt: 7`, `duplicate_logic: 11`, `unreferenced_by_name: 582`
* *Architecture:* `io: 2`, `api: 624`, `import: 46`
* *Defense:* `safety: 598`, `doc: 36`, `test: 841`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` collections, contextlib, cycler, datetime, dateutil.tz, decimal, functools, gc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `matplotlib-3.10.8/lib/matplotlib/axes/_base.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.039)
- **Top Global Matches:** file_cluster_4: 5.039, file_cluster_16: 10.43, file_cluster_12: 10.576
- **Magnitude:** 3736.88 | **LOC:** 4858 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **27**; blast radius 7.652; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 29.7814% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_plot_args` **(Many-Argument Workhorses)** (Impact: 131.9)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 131.8)
  * `autoscale_view` **(Many-Argument Workhorses)** (Impact: 77.9)
    * *Intent:* """ Autoscale the view limits using the data limits. Parameters ---------- tight : bool or None If *...
  * `axis` **(Many-Argument Workhorses)** (Impact: 67.2)
    * *Intent:* """ Convenience method to get or set some axis properties. Call signatures:: xmin, xmax, ymin, ymax ...
  * `__call__` **(Many-Argument Workhorses)** (Impact: 64.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 429 instances
* *State Mutation (weighted view):* 1463
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 665`, `structural_boundaries: 437`, `args: 194`, `func_start: 193`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 605`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 151`, `import: 28`
* *Defense:* `safety: 37`, `doc: 155`, `test: 36`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.652
  * `Choke Point (Betweenness):` 0.001004 | `Ripple Effect (Closeness):` 0.200288
  * `Imports (Out-Degree: 11):` collections.abc, contextlib, functools, inspect, logging, matplotlib, matplotlib.artist, matplotlib.axis...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/lib/matplotlib/widgets.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.789)
- **Top Global Matches:** file_cluster_16: 6.789, file_cluster_15: 7.865, file_cluster_4: 8.323
- **Magnitude:** 3425.18 | **LOC:** 4186 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **18**; blast radius 0.655; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.1%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 31.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_onmove` **(Many-Argument Workhorses)** (Impact: 71.2)
    * *Intent:* """ Motion notify event handler. This can do one of four things: - Translate - Rotate - Re-size - Co...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 64.4)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 49.1)
  * `onmove` **(Compute Cores)** (Impact: 44.9)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 44.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 470 instances
* *State Mutation (weighted view):* 1576
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 597`, `structural_boundaries: 395`, `args: 217`, `func_start: 207`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 636`, `fragile_debt: 1`, `duplicate_logic: 13`
* *Architecture:* `api: 122`, `import: 11`
* *Defense:* `safety: 10`, `doc: 158`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.655
  * `Choke Point (Betweenness):` 7.2e-05 | `Ripple Effect (Closeness):` 0.004752
  * `Imports (Out-Degree: 15):` ._api, ._docstring, .backend_tools, .cbook, .collections, .colors, .lines, .patches...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/lib/mpl_toolkits/mplot3d/axes3d.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.643)
- **Top Global Matches:** file_cluster_4: 5.643, file_cluster_12: 10.498, file_cluster_6: 10.626
- **Magnitude:** 3424.92 | **LOC:** 4163 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **21**; blast radius 1.546; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.1%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 50.7246% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `errorbar` **(Many-Argument Workhorses)** (Impact: 203.6)
  * `plot_surface` **(Many-Argument Workhorses)** (Impact: 126.0)
  * `plot_wireframe` **(Many-Argument Workhorses)** (Impact: 109.3)
    * *Intent:* """ Plot a 3D wireframe. .. note:: The *rcount* and *ccount* kwargs, which both default to 50, deter...
  * `voxels` **(Many-Argument Workhorses)** (Impact: 94.7)
  * `fill_between` **(Many-Argument Workhorses)** (Impact: 66.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 468 instances
* *State Mutation (weighted view):* 1645
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 418`, `structural_boundaries: 264`, `args: 118`, `func_start: 117`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 709`, `planned_debt: 3`, `fragile_debt: 6`
* *Architecture:* `api: 91`, `import: 24`
* *Defense:* `safety: 14`, `doc: 87`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.546
  * `Choke Point (Betweenness):` 0.000884 | `Ripple Effect (Closeness):` 0.106067
  * `Imports (Out-Degree: 15):` .art3d, .axis3d, .proj3d, collections, itertools, math, matplotlib, matplotlib.artist...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/lib/matplotlib/patches.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.884)
- **Top Global Matches:** file_cluster_16: 6.884, file_cluster_15: 7.361, file_cluster_12: 8.406
- **Magnitude:** 3090.72 | **LOC:** 4761 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **29** in-repo importer(s); it depends on **23**; blast radius 1.619; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.4%)
- **Documentation Coverage:** 34.7319% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_xy` **(Many-Argument Workhorses)** (Impact: 63.4)
    * *Intent:* """Calculate the pixel position of given point."""
  * `transmute` **(Many-Argument Workhorses)** (Impact: 51.2)
    * *Intent:* # docstring inherited if self._beginarrow_head or self._endarrow_head: head_length = self.head_lengt...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 48.2)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 38.7)
  * `draw` **(Many-Argument Workhorses)** (Impact: 33.0)
    * *Intent:* """ Draw the arc to the given *renderer*. Notes ----- Ellipses are normally drawn using an approxima...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 375 instances
* *State Mutation (weighted view):* 1497
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 320`, `structural_boundaries: 511`, `args: 256`, `func_start: 255`, `class_start: 56`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 747`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 37`
* *Architecture:* `io: 1`, `api: 211`, `import: 16`
* *Defense:* `safety: 21`, `doc: 233`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.619
  * `Choke Point (Betweenness):` 0.000797 | `Ripple Effect (Closeness):` 0.150024
  * `Imports (Out-Degree: 16):` ._api, ._docstring, ._enums, .artist, .bezier, .cbook, .colors, .hatch...
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/lib/matplotlib/colors.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.54)
- **Top Global Matches:** file_cluster_4: 7.54, file_cluster_16: 8.068, file_cluster_12: 8.229
- **Magnitude:** 2792.9 | **LOC:** 3716 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **14**; blast radius 0.889; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.9%), Connectivity (formerly Api Exposure) (60.8%)
- **Documentation Coverage:** 48.5816% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_to_rgba_no_colorcycle` **(Defensive Guards)** (Impact: 96.4)
    * *Intent:* """ Convert *c* to an RGBA color, with no support for color-cycle syntax. If *alpha* is given, force...
  * `to_rgba_array` **(Defensive Guards)** (Impact: 88.4)
    * *Intent:* """ Convert *c* to a (n, 4) array of RGBA colors. Parameters ---------- c : Matplotlib color or arra...
  * `_make_norm_from_scale` **(Many-Argument Workhorses)** (Impact: 64.1)
  * `__call__` **(Many-Argument Workhorses)** (Impact: 49.5)
  * `__call__` **(Many-Argument Workhorses)** (Impact: 37.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 361 instances
* *State Mutation (weighted view):* 1295
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 451`, `structural_boundaries: 380`, `args: 164`, `func_start: 161`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 573`, `dead_code: 2`, `duplicate_logic: 13`
* *Architecture:* `api: 116`, `import: 16`
* *Defense:* `safety: 51`, `doc: 112`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.889
  * `Choke Point (Betweenness):` 0.000277 | `Ripple Effect (Closeness):` 0.117141
  * `Imports (Out-Degree: 4):` ._color_data, PIL, PIL.PngImagePlugin, base64, collections.abc, functools, importlib, inspect...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/lib/matplotlib/ticker.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.97)
- **Top Global Matches:** file_cluster_16: 6.97, file_cluster_15: 7.508, file_cluster_4: 7.688
- **Magnitude:** 2733.8 | **LOC:** 2991 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **8**; blast radius 3.707; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.9%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (74.2%)
- **Documentation Coverage:** 51.0638% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tick_values` **(Many-Argument Workhorses)** (Impact: 75.8)
    * *Intent:* # dummy axis has no axes attribute if hasattr(self.axis, "axes") and self.axis.axes.name == "polar":...
  * `tick_values` **(Many-Argument Workhorses)** (Impact: 71.8)
  * `tick_values` **(Many-Argument Workhorses)** (Impact: 40.2)
  * `__call__` **(Many-Argument Workhorses)** (Impact: 33.8)
    * *Intent:* # docstring inherited if x == 0: # Symlog return r'$\mathdefault{0}$' sign_string = '-' if x < 0 els...
  * `_raw_ticks` **(Many-Argument Workhorses)** (Impact: 33.4)
    * *Intent:* """ Generate a list of tick locations including the range *vmin* to *vmax*. In some applications, on...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 405 instances
* *State Mutation (weighted view):* 1298
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 467`, `structural_boundaries: 372`, `args: 162`, `func_start: 161`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 488`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 13`
* *Architecture:* `api: 124`, `import: 11`
* *Defense:* `safety: 11`, `doc: 118`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.707
  * `Choke Point (Betweenness):` 8e-05 | `Ripple Effect (Closeness):` 0.189151
  * `Imports (Out-Degree: 4):` itertools, locale, logging, math, matplotlib, numbers, numpy, string
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/lib/matplotlib/backends/backend_pdf.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.478)
- **Top Global Matches:** file_cluster_4: 7.478, file_cluster_12: 7.577, file_cluster_15: 9.468
- **Magnitude:** 2703.58 | **LOC:** 2807 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **31**; blast radius 0.26; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.2%)
- **Documentation Coverage:** 63.9831% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `embedTTF` **(Many-Argument Workhorses)** (Impact: 97.8)
    * *Intent:* """Embed the TTF font from the named file into the document."""
  * `draw_path_collection` **(Many-Argument Workhorses)** (Impact: 65.4)
  * `draw_text` **(Many-Argument Workhorses)** (Impact: 61.7)
    * *Intent:* # docstring inherited # TODO: combine consecutive texts into one BT/ET delimited section self.check_...
  * `draw_tex` **(Many-Argument Workhorses)** (Impact: 55.1)
    * *Intent:* # docstring inherited texmanager = self.get_texmanager() fontsize = prop.get_size_in_points() dvifil...
  * `embedTTFType42` **(Many-Argument Workhorses)** (Impact: 35.2)
    * *Intent:* """The Type 42-specific part of embedding a Truetype font"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 396 instances
* *State Mutation (weighted view):* 1386
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 358`, `structural_boundaries: 345`, `args: 130`, `func_start: 129`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 594`, `planned_debt: 16`, `fragile_debt: 2`
* *Architecture:* `io: 6`, `api: 105`, `import: 34`
* *Defense:* `safety: 39`, `doc: 57`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.26
  * `Choke Point (Betweenness):` 3.1e-05 | `Ripple Effect (Closeness):` 0.00264
  * `Imports (Out-Degree: 13):` ._backend_pdf_ps, PIL, codecs, datetime, encodings, enum, functools, io...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/lib/matplotlib/_mathtext.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.46)
- **Top Global Matches:** file_cluster_5: 8.46, file_cluster_12: 9.455, file_cluster_4: 9.509
- **Magnitude:** 2598.72 | **LOC:** 2856 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **20**; blast radius 0.236; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.6%), Complexity Load (formerly Cognitive Load) (58.5%), Connectivity (formerly Api Exposure) (55.0%)
- **Documentation Coverage:** 87.7828% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `subsuper` **(Many-Argument Workhorses)** (Impact: 97.7)
  * `ship` **(Defensive Guards)** (Impact: 80.0)
    * *Intent:* """ Ship out *box* at offset *xy*, converting it to an `Output`. Since boxes can be inside of boxes ...
  * `symbol` **(Many-Argument Workhorses)** (Impact: 51.5)
  * `_get_glyph` **(Many-Argument Workhorses)** (Impact: 50.1)
  * `_map_virtual_font` **(Many-Argument Workhorses)** (Impact: 42.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 382 instances
* *State Mutation (weighted view):* 1359
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 324`, `structural_boundaries: 335`, `args: 134`, `func_start: 133`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 595`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 124`, `import: 22`
* *Defense:* `safety: 70`, `doc: 65`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.236
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.001584
  * `Imports (Out-Degree: 5):` ._mathtext_data, .cbook, .font_manager, .ft2font, __future__, abc, collections.abc, copy...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/lib/matplotlib/figure.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.143)
- **Top Global Matches:** file_cluster_4: 6.143, file_cluster_12: 9.015, file_cluster_16: 10.403
- **Magnitude:** 2344.24 | **LOC:** 3727 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **34** in-repo importer(s); it depends on **25**; blast radius 1.784; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.0%), Connectivity (formerly Api Exposure) (66.2%)
- **Documentation Coverage:** 33.9207% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `subplot_mosaic` **(Many-Argument Workhorses)** (Impact: 144.7)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 88.8)
  * `colorbar` **(Many-Argument Workhorses)** (Impact: 64.1)
  * `ginput` **(Many-Argument Workhorses)** (Impact: 61.3)
  * `get_tightbbox` **(Many-Argument Workhorses)** (Impact: 45.6)
    * *Intent:* """ Return a (tight) bounding box of the figure *in inches*. Note that `.FigureBase` differs from al...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 252 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 863
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 373`, `structural_boundaries: 300`, `args: 127`, `func_start: 125`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 359`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 100`, `concurrency: 2`, `import: 27`
* *Defense:* `safety: 40`, `doc: 96`, `test: 23`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.784
  * `Choke Point (Betweenness):` 0.002176 | `Ripple Effect (Closeness):` 0.120873
  * `Imports (Out-Degree: 18):` contextlib, functools, inspect, itertools, logging, matplotlib, matplotlib._api, matplotlib._pylab_helpers...
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/lib/matplotlib/backend_bases.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.33)
- **Top Global Matches:** file_cluster_12: 7.33, file_cluster_16: 7.797, file_cluster_15: 8.355
- **Magnitude:** 2322.54 | **LOC:** 3586 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **28** in-repo importer(s); it depends on **31**; blast radius 2.762; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.9%), Connectivity (formerly Api Exposure) (65.3%)
- **Documentation Coverage:** 24.0331% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `print_figure` **(Many-Argument Workhorses)** (Impact: 93.9)
  * `key_press_handler` **(Many-Argument Workhorses)** (Impact: 81.0)
    * *Intent:* """ Implement the default Matplotlib key bindings for the canvas and toolbar described at :ref:`key-...
  * `_iter_collection` **(Many-Argument Workhorses)** (Impact: 76.0)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 44.6)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 32.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 242 instances
* *State Mutation (weighted view):* 885
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 351`, `structural_boundaries: 418`, `args: 201`, `func_start: 192`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 401`, `dead_code: 1`, `planned_debt: 10`, `fragile_debt: 2`
* *Architecture:* `io: 18`, `api: 170`, `import: 36`
* *Defense:* `safety: 48`, `doc: 166`, `test: 3`, `sync_locks: 6`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.762
  * `Choke Point (Betweenness):` 0.001242 | `Ripple Effect (Closeness):` 0.154568
  * `Imports (Out-Degree: 9):` .backends.registry, IPython, IPython.core, collections, contextlib, enum, functools, importlib...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/lib/matplotlib/axis.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.182)
- **Top Global Matches:** file_cluster_4: 7.182, file_cluster_12: 7.479, file_cluster_16: 7.527
- **Magnitude:** 2292.56 | **LOC:** 2820 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **16**; blast radius 0.415; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.1%), Connectivity (formerly Api Exposure) (56.0%)
- **Documentation Coverage:** 40.5316% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 121.5)
  * `set_ticklabels` **(Many-Argument Workhorses)** (Impact: 55.3)
  * `_set_lim` **(Many-Argument Workhorses)** (Impact: 47.8)
    * *Intent:* # this is mainly in support of custom object plotting. For # example, if someone passes in a datetim...
  * `get_tightbbox` **(Many-Argument Workhorses)** (Impact: 38.5)
    * *Intent:* """ Return a bounding box that encloses the axis. It only accounts tick labels, axis label, and offs...
  * `set_tick_params` **(Many-Argument Workhorses)** (Impact: 31.3)
    * *Intent:* """ Set appearance parameters for ticks, ticklabels, and gridlines. For documentation of keyword arg...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 301 instances
* *State Mutation (weighted view):* 1002
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 355`, `structural_boundaries: 349`, `args: 172`, `func_start: 172`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 400`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 127`, `import: 17`
* *Defense:* `safety: 32`, `doc: 115`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.415
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.133401
  * `Imports (Out-Degree: 8):` datetime, dateutil.tz, functools, logging, matplotlib, matplotlib.artist, matplotlib.colors, matplotlib.lines...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/extern/agg24-svn/include/agg_renderer_markers.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.391)
- **Top Global Matches:** file_cluster_6: 7.391, file_cluster_8: 12.229, file_cluster_4: 14.079
- **Magnitude:** 2202.2 | **LOC:** 707 | **CtrlFlow:** 71.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.136; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `markers` **(Compute Cores)** (Impact: 213.4)
    * *Intent:* //--------------------------------------------------------------------
  * `markers` **(Compute Cores)** (Impact: 199.7)
    * *Intent:* //--------------------------------------------------------------------
  * `markers` **(Compute Cores)** (Impact: 193.0)
    * *Intent:* //--------------------------------------------------------------------
  * `markers` **(Compute Cores)** (Impact: 185.0)
    * *Intent:* //--------------------------------------------------------------------
  * `marker` **(Compute Cores)** (Impact: 86.2)
    * *Intent:* //--------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 359 instances
* *State Mutation (weighted view):* 1077
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 423`, `structural_boundaries: 46`, `args: 97`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `state_mutation: 359`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` agg_basics.h, agg_renderer_primitives.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `matplotlib-3.10.8/lib/matplotlib/pyplot.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.458)
- **Top Global Matches:** file_cluster_5: 7.458, file_cluster_12: 9.139, file_cluster_0: 9.898
- **Magnitude:** 1956.56 | **LOC:** 4645 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **630** in-repo importer(s); it depends on **51**; blast radius 61.725; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (99.6%), Guard Balance (formerly Safety Score) (62.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 68.1199% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `figure` **(Many-Argument Workhorses)** (Impact: 104.9)
    * *Intent:* ## Figures ## # autoincrement if None, else integer from 1-N num: int | str | Figure | SubFigure | N...
  * `switch_backend` **(Compute Cores)** (Impact: 38.7)
    * *Intent:* """ Set the pyplot backend. Switching to an interactive backend is possible only if no event loop fo...
  * `subplot` **(Many-Argument Workhorses)** (Impact: 38.4)
    * *Intent:* ## More ways of creating Axes ## """ Add an Axes to the current figure or retrieve an existing Axes....
  * `_add_pyplot_note` **(Many-Argument Workhorses)** (Impact: 32.3)
    * *Intent:* """ Add a note to the docstring of *func* that it is a pyplot wrapper. The note is added to the "Not...
  * `rgrids` **(Many-Argument Workhorses)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 148 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 487
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `structural_boundaries: 496`, `args: 183`, `func_start: 182`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 191`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 6`, `api: 174`, `concurrency: 6`, `import: 81`
* *Defense:* `safety: 21`, `doc: 67`, `sync_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 61.725
  * `Choke Point (Betweenness):` 0.01616 | `Ripple Effect (Closeness):` 0.296006
  * `Imports (Out-Degree: 17):` .ticker, IPython, IPython.core.pylabtools, PIL.Image, __future__, collections.abc, contextlib, cycler...
  * `Imported By (In-Degree: 630):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/lib/matplotlib/collections.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.261)
- **Top Global Matches:** file_cluster_16: 6.261, file_cluster_15: 7.211, file_cluster_12: 7.616
- **Magnitude:** 1930.44 | **LOC:** 2574 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **20**; blast radius 0.648; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.1%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 42.5532% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `legend_elements` **(Many-Argument Workhorses)** (Impact: 67.8)
  * `draw` **(Many-Argument Workhorses)** (Impact: 46.0)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 37.1)
  * `set_verts` **(Stateful Encapsulated Methods)** (Impact: 22.1)
    * *Intent:* """ Set the vertices of the polygons. Parameters ---------- verts : list of array-like The sequence ...
  * `get_datalim` **(Many-Argument Workhorses)** (Impact: 20.7)
    * *Intent:* # Calculate the data limits and return them as a `.Bbox`. # # This operation depends on the transfor...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 275 instances
* *State Mutation (weighted view):* 974
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 283`, `args: 139`, `func_start: 139`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 424`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `api: 111`, `import: 10`
* *Defense:* `safety: 20`, `doc: 102`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.648
  * `Choke Point (Betweenness):` 0.000585 | `Ripple Effect (Closeness):` 0.142825
  * `Imports (Out-Degree: 16):` ._api, ._docstring, ._enums, ._path, .artist, .cbook, .colorizer, .colors...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/lib/matplotlib/transforms.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.43)
- **Top Global Matches:** file_cluster_15: 6.43, file_cluster_16: 6.479, file_cluster_12: 8.219
- **Magnitude:** 1869.14 | **LOC:** 2997 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **60** in-repo importer(s); it depends on **10**; blast radius 8.658; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (86.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.9%)
- **Documentation Coverage:** 44.2623% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nonsingular` **(Many-Argument Workhorses)** (Impact: 29.7)
    * *Intent:* """ Modify the endpoints of a range as needed to avoid singularities. Parameters ---------- vmin, vm...
  * `transform_non_affine` **(Defensive Guards)** (Impact: 22.1)
    * *Intent:* # docstring inherited if self._x.is_affine and self._y.is_affine: return values x = self._x y = self...
  * `__sub__` **(Compute Cores)** (Impact: 19.8)
    * *Intent:* """ Compose *self* with the inverse of *other*, cancelling identical terms if any:: # In general: A ...
  * `transform_angles` **(Many-Argument Workhorses)** (Impact: 17.1)
    * *Intent:* """ Transform a set of angles anchored at specific locations. Parameters ---------- angles : (N,) ar...
  * `shrunk_to_aspect` **(Many-Argument Workhorses)** (Impact: 16.8)
    * *Intent:* """ Return a copy of the `Bbox`, shrunk so that it is as large as it can be while having the desired...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 175 instances
* *State Mutation (weighted view):* 698
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 258`, `structural_boundaries: 485`, `args: 245`, `func_start: 229`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 348`, `duplicate_logic: 14`
* *Architecture:* `api: 213`, `import: 10`
* *Defense:* `safety: 23`, `doc: 158`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.658
  * `Choke Point (Betweenness):` 0.000356 | `Ripple Effect (Closeness):` 0.164663
  * `Imports (Out-Degree: 5):` .path, functools, itertools, math, matplotlib, matplotlib._path, numpy, numpy.linalg...
  * `Imported By (In-Degree: 60):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/lib/matplotlib/cbook.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.655)
- **Top Global Matches:** file_cluster_12: 7.655, file_cluster_4: 8.64, file_cluster_16: 10.239
- **Magnitude:** 1732.62 | **LOC:** 2420 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **98** in-repo importer(s); it depends on **24**; blast radius 17.795; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.8%), Connectivity (formerly Api Exposure) (53.6%)
- **Documentation Coverage:** 32.8502% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `boxplot_stats` **(Many-Argument Workhorses)** (Impact: 63.8)
  * `delete_masked_points` **(Defensive Guards)** (Impact: 36.3)
    * *Intent:* """ Find all masked and/or non-finite points in a set of arguments, and return the arguments with on...
  * `print_cycles` **(Many-Argument Workhorses)** (Impact: 35.4)
    * *Intent:* """ Print loops of cyclic references in the given *objects*. It is often useful to pass in ``gc.garb...
  * `_reshape_2D` **(Many-Argument Workhorses)** (Impact: 32.3)
    * *Intent:* """ Use Fortran ordering to convert ndarrays and lists of iterables to lists of 1D arrays. Lists of ...
  * `to_filehandle` **(Many-Argument Workhorses)** (Impact: 24.9)
    * *Intent:* """ Convert a path to an open file handle or pass-through a file-like object. Consider using `open_f...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 223 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 754
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 315`, `structural_boundaries: 353`, `args: 120`, `func_start: 119`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 34`, `high_risk_execution: 1`, `state_mutation: 308`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 28`, `api: 81`, `import: 26`
* *Defense:* `safety: 104`, `doc: 85`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.795
  * `Choke Point (Betweenness):` 0.000422 | `Ripple Effect (Closeness):` 0.24298
  * `Imports (Out-Degree: 3):` bz2, collections, collections.abc, contextlib, functools, gc, gi.repository, gzip...
  * `Imported By (In-Degree: 98):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/extern/agg24-svn/include/agg_blur.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.107)
- **Top Global Matches:** file_cluster_4: 7.107, file_cluster_0: 9.3, file_cluster_15: 9.426
- **Magnitude:** 1704.06 | **LOC:** 1504 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.136; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `stack_blur_rgba32` **(Many-Argument Workhorses)** (Impact: 60.4)
    * *Intent:* //=======================================================stack_blur_rgba32
  * `stack_blur_rgb24` **(Many-Argument Workhorses)** (Impact: 58.5)
    * *Intent:* //========================================================stack_blur_rgb24
  * `stack_blur_gray8` **(Many-Argument Workhorses)** (Impact: 54.0)
    * *Intent:* //========================================================stack_blur_gray8
  * `blur_x` **(Many-Argument Workhorses)** (Impact: 28.6)
    * *Intent:* //--------------------------------------------------------------------
  * `blur` **(Compute Cores)** (Impact: 26.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 360 instances
* *State Mutation (weighted view):* 1315
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 210`, `args: 36`, `func_start: 49`, `class_start: 10`
* *Risk/State:* `state_mutation: 595`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `immutability_locks: 49`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` agg_array.h, agg_pixfmt_base.h, agg_pixfmt_transposer.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `matplotlib-3.10.8/extern/agg24-svn/include/agg_renderer_outline_aa.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.506)
- **Top Global Matches:** file_cluster_15: 6.506, file_cluster_11: 7.361, file_cluster_16: 8.071
- **Magnitude:** 1688.34 | **LOC:** 1838 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 0.273; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.5%), Complexity Load (formerly Cognitive Load) (74.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `line_interpolator_aa3` **(Many-Argument Workhorses)** (Impact: 69.8)
    * *Intent:* //---------------------------------------------------------------------
  * `line_interpolator_aa1` **(Many-Argument Workhorses)** (Impact: 59.8)
    * *Intent:* //---------------------------------------------------------------------
  * `line3` **(Many-Argument Workhorses)** (Impact: 32.1)
    * *Intent:* //-------------------------------------------------------------------------
  * `pie_hline` **(Many-Argument Workhorses)** (Impact: 27.1)
    * *Intent:* //-------------------------------------------------------------------------
  * `line1` **(Many-Argument Workhorses)** (Impact: 20.1)
    * *Intent:* //-------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 312 instances
* *State Mutation (weighted view):* 1019
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 168`, `args: 41`, `func_start: 115`, `class_start: 12`
* *Risk/State:* `state_mutation: 395`, `duplicate_logic: 18`
* *Architecture:* `api: 23`, `import: 8`
* *Defense:* `immutability_locks: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.273
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.000528
  * `Imports (Out-Degree: 9):` agg_array.h, agg_clip_liang_barsky.h, agg_dda_line.h, agg_ellipse_bresenham.h, agg_gamma_functions.h, agg_line_aa_basics.h, agg_math.h, agg_renderer_base.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/src/tri/_tri.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.211)
- **Top Global Matches:** file_cluster_4: 6.211, file_cluster_15: 10.433, file_cluster_6: 11.737
- **Magnitude:** 1657.58 | **LOC:** 2072 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.46; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.4%), Complexity Load (formerly Cognitive Load) (93.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TrapezoidMapTriFinder::add_edge_to_tree` **(Compute Cores)** (Impact: 85.7)
  * `TrapezoidMapTriFinder::Node::search` **(Compute Cores)** (Impact: 59.1)
  * `TriContourGenerator::follow_boundary` **(Many-Argument Workhorses)** (Impact: 57.0)
  * `Triangulation::Triangulation` **(Many-Argument Workhorses)** (Impact: 47.3)
  * `TriContourGenerator::follow_interior` **(Many-Argument Workhorses)** (Impact: 36.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 192 instances
* *State Mutation (weighted view):* 603
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 474`, `structural_boundaries: 160`, `args: 102`, `func_start: 116`
* *Risk/State:* `state_mutation: 219`, `unreferenced_by_name: 100`
* *Architecture:* `import: 5`
* *Defense:* `safety: 88`, `immutability_locks: 155`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.46
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000704
  * `Imports (Out-Degree: 3):` mplutils.h, _tri.h, algorithm, random, set
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/lib/matplotlib/image.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.21)
- **Top Global Matches:** file_cluster_4: 5.21, file_cluster_12: 9.95, file_cluster_16: 10.012
- **Magnitude:** 1594.22 | **LOC:** 1787 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **18**; blast radius 0.586; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.1%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (60.7%)
- **Documentation Coverage:** 42.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_make_image` **(Many-Argument Workhorses)** (Impact: 175.9)
  * `imsave` **(Many-Argument Workhorses)** (Impact: 109.4)
  * `_draw_list_compositing_images` **(Many-Argument Workhorses)** (Impact: 40.3)
  * `make_image` **(Many-Argument Workhorses)** (Impact: 35.0)
    * *Intent:* # docstring inherited if self._A is None: raise RuntimeError('You must first set the image array') i...
  * `_resample` **(Many-Argument Workhorses)** (Impact: 34.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 212 instances
* *State Mutation (weighted view):* 710
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 259`, `structural_boundaries: 194`, `args: 71`, `func_start: 71`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 286`, `planned_debt: 3`, `duplicate_logic: 7`
* *Architecture:* `io: 6`, `api: 60`, `import: 21`
* *Defense:* `safety: 17`, `doc: 55`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.586
  * `Choke Point (Betweenness):` 0.000589 | `Ripple Effect (Closeness):` 0.14559
  * `Imports (Out-Degree: 10):` PIL.Image, PIL.PngImagePlugin, logging, math, matplotlib, matplotlib._image, matplotlib.artist, matplotlib.backend_bases...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/lib/matplotlib/contour.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.034)
- **Top Global Matches:** file_cluster_4: 6.034, file_cluster_6: 10.37, file_cluster_9: 11.261
- **Magnitude:** 1557.22 | **LOC:** 1703 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 0.197; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.8%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 41.0714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 188.5)
  * `clabel` **(Many-Argument Workhorses)** (Impact: 66.4)
  * `_check_xyz` **(Many-Argument Workhorses)** (Impact: 56.0)
    * *Intent:* """ Check that the shapes of the input arrays match; if x and y are 1D, convert them to 2D using mes...
  * `_split_path_and_get_label_rotation` **(Many-Argument Workhorses)** (Impact: 37.8)
    * *Intent:* """ Prepare for insertion of a label at index *idx* of *path*. Parameters ---------- path : Path The...
  * `_contour_labeler_event_handler` **(Stateful Encapsulated Methods)** (Impact: 34.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 230 instances
* *State Mutation (weighted view):* 747
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 128`, `args: 40`, `func_start: 36`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 287`, `dead_code: 1`
* *Architecture:* `api: 21`, `import: 21`
* *Defense:* `safety: 14`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.197
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.089426
  * `Imports (Out-Degree: 10):` contextlib, contourpy, functools, math, matplotlib, matplotlib.backend_bases, matplotlib.cbook, matplotlib.cm...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `matplotlib-3.10.8/lib/matplotlib/colorbar.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.07)
- **Top Global Matches:** file_cluster_4: 6.07, file_cluster_16: 8.097, file_cluster_12: 8.539
- **Magnitude:** 1536.18 | **LOC:** 1564 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.136; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (50.5%)
- **Documentation Coverage:** 46.3158% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 144.3)
  * `make_axes` **(Many-Argument Workhorses)** (Impact: 56.0)
  * `_do_extends` **(Many-Argument Workhorses)** (Impact: 49.7)
    * *Intent:* """ Add the extend tri/rectangles on the outside of the Axes. ax is unused, but required due to the ...
  * `add_lines` **(Many-Argument Workhorses)** (Impact: 27.9)
    * *Intent:* """ Draw lines on the colorbar. The lines are appended to the list :attr:`lines`. Parameters -------...
  * `make_axes_gridspec` **(Many-Argument Workhorses)** (Impact: 27.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 259 instances
* *State Mutation (weighted view):* 849
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 123`, `args: 61`, `func_start: 58`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 331`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 30`, `import: 10`
* *Defense:* `safety: 35`, `doc: 40`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` logging, matplotlib, matplotlib.artist, matplotlib.patches, matplotlib.path, matplotlib.spines, matplotlib.transforms, numpy
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `matplotlib-3.10.8/extern/agg24-svn/src/platform/X11/agg_platform_support.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.463)
- **Top Global Matches:** file_cluster_6: 7.463, file_cluster_8: 12.85, file_cluster_4: 13.468
- **Magnitude:** 1509.86 | **LOC:** 1602 | **CtrlFlow:** 51.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.136; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `platform_specific::put_image` **(Compute Cores)** (Impact: 449.5)
    * *Intent:* //------------------------------------------------------------------------
  * `platform_support::load_img` **(Many-Argument Workhorses)** (Impact: 168.7)
    * *Intent:* //------------------------------------------------------------------------
  * `platform_support::save_img` **(Many-Argument Workhorses)** (Impact: 130.8)
    * *Intent:* //------------------------------------------------------------------------
  * `platform_support::init` **(Many-Argument Workhorses)** (Impact: 110.8)
    * *Intent:* //------------------------------------------------------------------------
  * `platform_support::run` **(I/O & Config Routines)** (Impact: 95.0)
    * *Intent:* //------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 106 instances
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 395
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 645`, `structural_boundaries: 50`, `args: 19`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 183`, `dead_code: 19`, `unreferenced_by_name: 30`
* *Architecture:* `io: 6`, `api: 1`, `import: 15`
* *Defense:* `immutability_locks: 14`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` Xatom.h, Xlib.h, Xutil.h, keysym.h, agg_basics.h, agg_pixfmt_gray.h, agg_pixfmt_rgb.h, agg_pixfmt_rgba.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_gradient_lut.h` (CPP) | Magnitude: 100.0 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 160, structural_boundaries: 43, state_mutation: 25, func_start: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `matplotlib-3.10.8/lib/matplotlib/tests/test_backend_template.py` (PYTHON) | Magnitude: 22.54 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 23, core_var_decl: 9, state_mutation: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_span_interpolator_trans.h` (CPP) | Magnitude: 27.62 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 49, state_mutation: 12, pointers: 12, core_var_decl: 12
- `matplotlib-3.10.8/lib/matplotlib/tests/test_text.py` (PYTHON) | Magnitude: 507.08 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 707, core_var_decl: 379, design_snake_case: 378, structural_boundaries: 214
- `matplotlib-3.10.8/lib/matplotlib/tests/test_backend_pdf.py` (PYTHON) | Magnitude: 201.68 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 261, structural_boundaries: 122, core_var_decl: 121, design_snake_case: 119
- `matplotlib-3.10.8/galleries/examples/axes_grid1/demo_axes_divider.py` (PYTHON) | Magnitude: 36.74 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 48, core_var_decl: 26, design_snake_case: 26, state_mutation: 18
- `matplotlib-3.10.8/lib/matplotlib/tests/test_legend.py` (PYTHON) | Magnitude: 773.14 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 916, core_var_decl: 509, design_snake_case: 507, structural_boundaries: 299

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `matplotlib-3.10.8/lib/matplotlib/tests/test_type1font.py` (PYTHON) | Magnitude: 98.94 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 117, structural_boundaries: 72, safety: 40, state_mutation: 28
- `matplotlib-3.10.8/lib/mpl_toolkits/mplot3d/axis3d.py` (PYTHON) | Magnitude: 657.1 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 474, core_var_decl: 184, design_snake_case: 182, state_mutation: 174
- `matplotlib-3.10.8/galleries/examples/shapes_and_collections/collections.py` (PYTHON) | Magnitude: 61.2 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 34, design_snake_case: 34, state_mutation: 27, indent_spaces: 7
- `matplotlib-3.10.8/lib/matplotlib/tests/test_backend_pgf.py` (PYTHON) | Magnitude: 134.16 | Delta: **0.14** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 223, structural_boundaries: 77, core_var_decl: 76, design_snake_case: 75
- `matplotlib-3.10.8/lib/mpl_toolkits/axes_grid1/anchored_artists.py` (PYTHON) | Magnitude: 185.34 | Delta: **0.158** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 103, core_var_decl: 51, design_snake_case: 47, state_mutation: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `matplotlib-3.10.8/lib/matplotlib/pylab.py` (PYTHON) | Magnitude: 22.54 | Delta: **0.112** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 26, import: 20, scientific: 12, state_mutation: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_span_solid.h` (CPP) | Magnitude: 19.02 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 9, func_start: 4, state_mutation: 3
- `matplotlib-3.10.8/lib/mpl_toolkits/axes_grid1/mpl_axes.py` (PYTHON) | Magnitude: 155.62 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 95, structural_boundaries: 34, branch: 28, state_mutation: 20
- `matplotlib-3.10.8/lib/matplotlib/tests/test_scale.py` (PYTHON) | Magnitude: 131.78 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 184, structural_boundaries: 89, core_var_decl: 83, design_snake_case: 83
- `matplotlib-3.10.8/extern/agg24-svn/include/ctrl/agg_slider_ctrl.h` (CPP) | Magnitude: 41.2 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 25, args: 20, state_mutation: 13
- `matplotlib-3.10.8/lib/matplotlib/tests/test_agg.py` (PYTHON) | Magnitude: 183.0 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 199, core_var_decl: 94, design_snake_case: 91, structural_boundaries: 87

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `matplotlib-3.10.8/lib/matplotlib/tri/_trirefine.py` (PYTHON) | Magnitude: 161.26 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 117, state_mutation: 57, core_var_decl: 56, design_snake_case: 56
- `matplotlib-3.10.8/lib/matplotlib/backends/backend_gtk4agg.py` (PYTHON) | Magnitude: 17.8 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 13, state_mutation: 6, core_var_decl: 6
- `matplotlib-3.10.8/lib/matplotlib/testing/_markers.py` (PYTHON) | Magnitude: 11.54 | Delta: **0.089** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 12, core_var_decl: 11, design_snake_case: 11
- `matplotlib-3.10.8/doc/sphinxext/missing_references.py` (PYTHON) | Magnitude: 150.66 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 87, core_var_decl: 35, design_snake_case: 35, state_mutation: 34
- `matplotlib-3.10.8/lib/matplotlib/projections/geo.py` (PYTHON) | Magnitude: 327.18 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 313, structural_boundaries: 136, state_mutation: 104, core_var_decl: 90

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `matplotlib-3.10.8/.github/workflows/conflictcheck.yml` (YAML) | Magnitude: 16.38 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 15, args: 3, branch: 2, structural_boundaries: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `matplotlib-3.10.8/.github/workflows/labeler.yml` (YAML) | Magnitude: 15.28 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 2, args: 1, class_start: 1
- `matplotlib-3.10.8/galleries/examples/color/colormap_reference.py` (PYTHON) | Magnitude: 12.86 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 35, core_var_decl: 10, design_snake_case: 10, structural_boundaries: 5
- `matplotlib-3.10.8/.github/workflows/stale-tidy.yml` (YAML) | Magnitude: 15.46 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 19, args: 11, structural_boundaries: 2, events: 2
- `matplotlib-3.10.8/lib/matplotlib/tests/test_textpath.py` (PYTHON) | Magnitude: 3.34 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 4, safety: 3, import: 2
- `matplotlib-3.10.8/lib/matplotlib/tri/__init__.py` (PYTHON) | Magnitude: 16.34 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 16, import: 8, indent_spaces: 8, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `matplotlib-3.10.8/lib/matplotlib/backends/backend_pdf.py` (PYTHON) | Magnitude: 2703.58 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1826, state_mutation: 594, core_var_decl: 514, design_snake_case: 461

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `matplotlib-3.10.8/lib/matplotlib/tests/test_preprocess_data.py` (PYTHON) | Magnitude: 105.22 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 157, structural_boundaries: 98, core_var_decl: 67, design_snake_case: 67
- `matplotlib-3.10.8/galleries/examples/specialty_plots/sankey_rankine.py` (PYTHON) | Magnitude: 24.38 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 50, core_var_decl: 46, design_snake_case: 45, structural_boundaries: 5
- `matplotlib-3.10.8/galleries/examples/subplots_axes_and_figures/axes_demo.py` (PYTHON) | Magnitude: 22.44 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: core_var_decl: 9, design_snake_case: 9, state_mutation: 7, design_short_vars: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `matplotlib-3.10.8/lib/matplotlib/backends/backend_qtagg.py` (PYTHON) | Magnitude: 49.38 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 18, state_mutation: 14, core_var_decl: 14

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `matplotlib-3.10.8/lib/matplotlib/pyplot.py` -> **Severity: 1.609** (Bridge: 0.0162 * Flux: 99.5966%)
- `matplotlib-3.10.8/lib/matplotlib/axes/_axes.py` -> **Severity: 0.887** (Bridge: 0.0089 * Flux: 100.0%)
- `matplotlib-3.10.8/lib/matplotlib/__init__.py` -> **Severity: 0.262** (Bridge: 0.0026 * Flux: 100.0%)
- `matplotlib-3.10.8/lib/matplotlib/figure.py` -> **Severity: 0.218** (Bridge: 0.0022 * Flux: 100.0%)
- `matplotlib-3.10.8/lib/mpl_toolkits/axisartist/axislines.py` -> **Severity: 0.175** (Bridge: 0.0018 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `matplotlib-3.10.8/lib/matplotlib/__init__.py` -> **Severity: 18.738** (Embedded: 0.2735 * Error Risk: 68.5054%)
- `matplotlib-3.10.8/lib/matplotlib/pyplot.py` -> **Severity: 18.475** (Embedded: 0.296 * Error Risk: 62.4133%)
- `matplotlib-3.10.8/lib/matplotlib/cbook.py` -> **Severity: 18.415** (Embedded: 0.243 * Error Risk: 75.7872%)
- `matplotlib-3.10.8/lib/matplotlib/_api/deprecation.py` -> **Severity: 17.638** (Embedded: 0.235 * Error Risk: 75.0395%)
- `matplotlib-3.10.8/lib/matplotlib/_api/__init__.py` -> **Severity: 17.066** (Embedded: 0.2454 * Error Risk: 69.5497%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `matplotlib-3.10.8/lib/matplotlib/_api/deprecation.py` -> **Severity: 12767.425** (Blast Radius: 185.708 * Doc Risk: 68.75%)
- `matplotlib-3.10.8/lib/matplotlib/_api/__init__.py` -> **Severity: 7719.478** (Blast Radius: 201.564 * Doc Risk: 38.2979%)
- `matplotlib-3.10.8/lib/matplotlib/pyplot.py` -> **Severity: 4204.701** (Blast Radius: 61.725 * Doc Risk: 68.1199%)
- `matplotlib-3.10.8/extern/agg24-svn/include/agg_basics.h` -> **Severity: 1852.4** (Blast Radius: 18.524 * Doc Risk: 100.0%)
- `matplotlib-3.10.8/lib/matplotlib/__init__.py` -> **Severity: 1584.412** (Blast Radius: 48.625 * Doc Risk: 32.5843%)

- **Mainframe skeleton completeness:** n/a (no channel has facts) (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: none.

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 356 literal sites + 4 sites through wrappers = 360
- **`memory_alloc`:** 90 literal sites + 5 sites through wrappers = 95
- **`panics_and_aborts`:** 1256 literal sites + 4 sites through wrappers = 1260

- `Error` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `matplotlib-3.10.8/lib/matplotlib/_mathtext.py`
- `lazy_init` (function, memory_alloc, primitive): 4 call sites in 1 files -- `matplotlib-3.10.8/src/_macosx.m`
- `copy_file` (function, debug_prints, primitive): 2 call sites in 1 files -- `matplotlib-3.10.8/tools/triage_tests.py`
- `set_os2` (function, debug_prints, primitive): 2 call sites in 1 files -- `matplotlib-3.10.8/tools/subset.py`
- `AGGApplication` (function, memory_alloc, primitive): 1 call sites in 1 files -- `matplotlib-3.10.8/extern/agg24-svn/src/platform/BeOS/agg_platform_support.cpp`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 57219 call pairs -- scoped 23.5%, unique 0.3%, ambiguous 33.4%, external 42.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 49683 | 22.0% | 0.0% | 33.7% | 44.3% |
| cpp | 6955 | 35.5% | 2.1% | 34.2% | 28.2% |
| objective-c | 423 | 17.0% | 0.5% | 1.9% | 80.6% |
| javascript | 130 | 7.7% | 0.0% | 0.0% | 92.3% |
| html | 17 | 0.0% | 0.0% | 0.0% | 100.0% |
| lua | 6 | 0.0% | 0.0% | 0.0% | 100.0% |
| shell | 5 | 0.0% | 0.0% | 0.0% | 100.0% |

## APPENDIX A. STRUCTURAL SURFACE LEXICON (EQUATIONS & CONTEXT)
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

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with high Structural Magnitude combined with a wide Blast Radius, severe Z-Scores (Architectural Drift), or extreme spikes in individual surface vectors (like Mutation Surface or Complexity Load). Do NOT sum the surface vectors together or treat any total of them as a score -- they are independently scaled meters in different units (#3112). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
