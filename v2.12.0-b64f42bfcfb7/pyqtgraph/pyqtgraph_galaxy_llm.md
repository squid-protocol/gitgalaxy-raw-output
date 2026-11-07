# ARCHITECTURAL_BRIEF: pyqtgraph
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/pyqtgraph/pyqtgraph.git` |
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
- **Scope:** 532 analyzed artifact(s), 66752 LOC.
- **Load-bearing artifact:** `pyqtgraph/Qt/__init__.py` -- 261 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `pyqtgraph/__init__.py` -- pulls in 90 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `pyqtgraph/functions.py` at magnitude 3051.84 (structural weight, not risk).
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
| Total Artifacts | 795 |
| Analyzed Artifacts (Scanned) | 532 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 263 |
| Total LOC | 66752 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 66.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3541 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2097 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 22.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1778 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 12 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 426 | 48207 | 80.1% |
| CSV | 69 | 17734 | 13.0% |
| PLAINTEXT | 12 | 0 | 2.3% |
| XML | 9 | 0 | 1.7% |
| YAML | 7 | 498 | 1.3% |
| MARKDOWN | 4 | 0 | 0.8% |
| SHELL | 1 | 3 | 0.2% |
| MAKEFILE | 1 | 120 | 0.2% |
| BATCH | 1 | 133 | 0.2% |
| CSS | 1 | 17 | 0.2% |
| C | 1 | 40 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 532 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 26%, Parameter Forwarders Files 22%, Large Core Modules (3) 15%, Declarative / Non-Code 10%, Large Core Modules (2) 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 516 | 97.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 16 | 3.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 263*

**Composition by Extension & Reason:**
- `.rst`: 127x Excluded (Unsupported Extension: '.rst')
- `.png`: 90x Excluded (Explicitly Denied Extension: '.png')
- `.ui`: 10x Excluded (Unsupported Extension: '.ui')
- `.dic`: 7x Excluded (Unsupported Extension: '.dic')
- `.ipynb`: 6x Excluded (Unsupported Extension: '.ipynb')
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 524 LOC), 1x Excluded (Saturation: Line 29 exceeds 500 chars), 1x Excluded (Saturation: Line 49 exceeds 500 chars)
- `.cfg`: 3x Excluded (Unsupported Extension: '.cfg')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.graphml`: 2x Excluded (Unsupported Extension: '.graphml')
- `.svg`: 2x Excluded (Static Asset Blob without Intent: 1227 LOC)
- `.hex`: 2x Excluded (Unsupported Extension: '.hex')
- `.ini`: 2x Excluded (Unsupported Extension: '.ini')
- `.css`: 1x Excluded (Saturation: Line 39 exceeds 500 chars)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 86.7 | 28.1 | 27.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 94.9 | 52.4 | 61.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 16.8 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 21.6 | 6.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 37.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.4 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 55.8 | 71.4 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 893 | 161 | 5 | `pyqtgraph/functions.py` |
| cleanup | 67 | 40 | 0 | `pyqtgraph/multiprocess/processes.py` |
| guards | 2711 | 223 | 17 | `tests/parametertree/test_Parameter.py` |
| danger | 1382 | 282 | 6 | `pyqtgraph/__init__.py` |
| concurrency | 89 | 28 | 0 | `pyqtgraph/multiprocess/processes.py` |
| connectivity | 3958 | 350 | 21 | `pyqtgraph/graphicsItems/ROI.py` |
| io | 413 | 80 | 1 | `pyqtgraph/multiprocess/processes.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 40 | 8 | 0 | `pyqtgraph/multiprocess/processes.py` |
| time | 39 | 19 | 0 | `pyqtgraph/multiprocess/processes.py` |
| serialization | 8 | 6 | 0 | `pyqtgraph/multiprocess/bootstrap.py` |
| regex | 32 | 16 | 0 | `tools/setupHelpers.py` |
| events | 440 | 73 | 2 | `pyqtgraph/graphicsItems/GradientEditorItem.py` |
| tests | 423 | 73 | 2 | `tests/test_makeARGB.py` |
| docs | 1601 | 294 | 7 | `pyqtgraph/functions.py` |
| debt | 380 | 86 | 2 | `pyqtgraph/debug.py` |
| mutation | 26879 | 398 | 122 | `pyqtgraph/functions.py` |
| dead_code | 487 | 152 | 3 | `tests/parametertree/test_Parameter.py` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 224 | 194 | 1 | `pyqtgraph/functions.py` |
| ui | 24 | 14 | 0 | `pyqtgraph/graphicsItems/ImageItem.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pyqtgraph/multiprocess/processes.py` (Hits: 42)
- `pyqtgraph/debug.py` (Hits: 22)
- `tests/image_testing.py` (Hits: 22)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`pyqtgraph/Qt/__init__.py`) — 261 inbound connections
2. **__init__.py** (`pyqtgraph/__init__.py`) — 207 inbound connections
3. **AxisItem.py** (`pyqtgraph/graphicsItems/AxisItem.py`) — 103 inbound connections
4. **functions.py** (`pyqtgraph/functions.py`) — 87 inbound connections
5. **PlotItem.py** (`pyqtgraph/graphicsItems/PlotItem/PlotItem.py`) — 73 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`pyqtgraph/__init__.py`) — 90 outbound dependencies
2. **__init__.py** (`pyqtgraph/Qt/__init__.py`) — 31 outbound dependencies
3. **PlotItem.py** (`pyqtgraph/graphicsItems/PlotItem/PlotItem.py`) — 23 outbound dependencies
4. **debug.py** (`pyqtgraph/debug.py`) — 22 outbound dependencies
5. **__init__.py** (`pyqtgraph/parametertree/parameterTypes/__init__.py`) — 20 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `makeARGB` **(Many-Argument Workhorses)** (@ `pyqtgraph/functions.py`) -> Impact: **195.8** | LOC: 182
  * *Intent:* """ Convert an array of values into an ARGB array suitable for building QImages, OpenGL textures, etc. Returns the ARGB array (unsigned byte) and a bo...
- `movePoint` **(Many-Argument Workhorses)** (@ `pyqtgraph/graphicsItems/ROI.py`) -> Impact: **154.3** | LOC: 175
  * *Intent:* ## called by Handles when they are moved. ## pos is the new position of the handle in scene coords, as requested by the handle. if modifiers is None: ...
- `setRange` **(Many-Argument Workhorses)** (@ `pyqtgraph/graphicsItems/ViewBox/ViewBox.py`) -> Impact: **143.2** | LOC: 149
  * *Intent:* """ Set the visible range of the ViewBox. Must specify at least one of *rect*, *xRange*, or *yRange*. ================== =============================...
- `setImage` **(Many-Argument Workhorses)** (@ `pyqtgraph/imageview/ImageView.py`) -> Impact: **141.3** | LOC: 158
- `generateDrawSpecs` **(Many-Argument Workhorses)** (@ `pyqtgraph/graphicsItems/AxisItem.py`) -> Impact: **136.0** | LOC: 295
  * *Intent:* """ Generate the drawing specifications for the axis, ticks, and labels. This method determines all the coordinates and other information needed to dr...
- `try_make_qimage` **(Many-Argument Workhorses)** (@ `pyqtgraph/functions_qimage.py`) -> Impact: **130.2** | LOC: 145
  * *Intent:* """ Internal function to make an QImage from an ndarray without going through the full generality of makeARGB(). Only certain combinations of input ar...
- `correctCoordinates` **(Many-Argument Workhorses)** (@ `pyqtgraph/exporters/SVGExporter.py`) -> Impact: **123.1** | LOC: 136
  * *Intent:* # correct the defs in the linearGradient for d in defs: if d.tagName == "linearGradient": # reset "gradientUnits" attribute to SVG default value d.rem...
- `setup` **(Many-Argument Workhorses)** (@ `benchmarks/renderImageItem.py`) -> Impact: **115.1** | LOC: 82
- `setData` **(Many-Argument Workhorses)** (@ `pyqtgraph/graphicsItems/PlotDataItem.py`) -> Impact: **114.7** | LOC: 173
- `updateViewRange` **(Many-Argument Workhorses)** (@ `pyqtgraph/graphicsItems/ViewBox/ViewBox.py`) -> Impact: **112.5** | LOC: 129
  * *Intent:* # Including a prepareForPaint call is part of the Qt strategy to # defer expensive redraw opertions until requested by a 'sigPrepareForPaint' signal #...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pyqtgraph/graphicsItems` | 39 | 17033.54 | 46.03% | 4.71% |
| `pyqtgraph` | 20 | 7980.06 | 48.35% | 9.76% |
| `pyqtgraph/examples` | 118 | 5828.72 | 33.67% | 0.0% |
| `pyqtgraph/widgets` | 33 | 5411.46 | 49.44% | 5.31% |
| `pyqtgraph/graphicsItems/ViewBox` | 4 | 2573.48 | 40.24% | 2.38% |
| `pyqtgraph/opengl/items` | 14 | 1999.8 | 36.55% | 6.6% |
| `pyqtgraph/parametertree` | 6 | 1850.4 | 42.07% | 1.67% |
| `pyqtgraph/parametertree/parameterTypes` | 20 | 1796.4 | 35.39% | 0.5% |
| `pyqtgraph/flowchart/library` | 7 | 1738.08 | 51.62% | 5.81% |
| `pyqtgraph/multiprocess` | 5 | 1700.74 | 48.46% | 12.25% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `pyqtgraph/GraphicsScene/mouseEvents.py` -> **100.0%** Exposure
- `pyqtgraph/Qt/OpenGLHelpers.py` -> **99.9998%** Exposure
- `pyqtgraph/PlotData.py` -> **99.999%** Exposure
- `pyqtgraph/widgets/RemoteGraphicsView.py` -> **98.603%** Exposure
- `pyqtgraph/opengl/items/GLGradientLegendItem.py` -> **92.4142%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `benchmarks/renderImageItem.py` -> **100.0%** Exposure
- `pyqtgraph/GraphicsScene/GraphicsScene.py` -> **100.0%** Exposure
- `pyqtgraph/GraphicsScene/exportDialog.py` -> **100.0%** Exposure
- `pyqtgraph/GraphicsScene/mouseEvents.py` -> **100.0%** Exposure
- `pyqtgraph/PlotData.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pyqtgraph/GraphicsScene/mouseEvents.py` -> **0** Orphaned Functions | **30** Duplicates
- `tests/parametertree/test_Parameter.py` -> **23** Orphaned Functions | **5** Duplicates
- `tests/test_functions.py` -> **17** Orphaned Functions | **0** Duplicates
- `tests/graphicsItems/test_DateAxisItem.py` -> **10** Orphaned Functions | **0** Duplicates
- `tests/graphicsItems/test_PlotDataItem.py` -> **10** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1165` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `pyqtgraph/functions.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.841)
- **Top Global Matches:** file_cluster_6: 6.841, file_cluster_4: 6.876, file_cluster_12: 14.562
- **Magnitude:** 3051.84 | **LOC:** 3190 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **87** in-repo importer(s); it depends on **16**; blast radius 31.742; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (90.5%), Guard Balance (formerly Safety Score) (86.2%), Connectivity (formerly Api Exposure) (84.6%)
- **Documentation Coverage:** 13.6752% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `makeARGB` **(Many-Argument Workhorses)** (Impact: 195.8)
    * *Intent:* """ Convert an array of values into an ARGB array suitable for building QImages, OpenGL textures, et...
  * `isocurve` **(Many-Argument Workhorses)** (Impact: 97.2)
    * *Intent:* #for i in range(index.shape[0]): # data x-axis #for j in range(index.shape[1]): # data y-axis #for k...
  * `eq` **(Defensive Guards)** (Impact: 68.7)
    * *Intent:* """The great missing equivalence function: Guaranteed evaluation to a single bool value. This functi...
  * `arrayToQPath` **(Many-Argument Workhorses)** (Impact: 65.9)
    * *Intent:* """ Convert an array of x,y coordinates to QPainterPath as efficiently as possible. The *connect* ar...
  * `_pseudoScatterExact` **(Many-Argument Workhorses)** (Impact: 45.8)
    * *Intent:* """Works by stacking points up one at a time, searching for the lowest position available at each po...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 541 instances
* *State Mutation (weighted view):* 1699
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 467`, `structural_boundaries: 237`, `args: 66`, `func_start: 64`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 617`, `dead_code: 10`
* *Architecture:* `io: 2`, `api: 57`, `import: 15`
* *Defense:* `safety: 51`, `doc: 55`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 31.742
  * `Choke Point (Betweenness):` 0.044131 | `Ripple Effect (Closeness):` 0.351133
  * `Imports (Out-Degree: 9):` .Qt, .debug, .getConfigOption, .reload, .util.cupy_helper, collections, decimal, math...
  * `Imported By (In-Degree: 87):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/ROI.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.004)
- **Top Global Matches:** file_cluster_15: 8.004, file_cluster_12: 8.097, file_cluster_16: 8.404
- **Magnitude:** 2321.62 | **LOC:** 2385 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **9**; blast radius 2.957; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.2%)
- **Documentation Coverage:** 71.2727% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `movePoint` **(Many-Argument Workhorses)** (Impact: 154.3)
    * *Intent:* ## called by Handles when they are moved. ## pos is the new position of the handle in scene coords, ...
  * `mouseDragEvent` **(Many-Argument Workhorses)** (Impact: 42.6)
  * `getArrayRegion` **(Many-Argument Workhorses)** (Impact: 39.0)
    * *Intent:* """ Return the result of :meth:`~pyqtgraph.ROI.getArrayRegion` masked by the elliptical shape of the...
  * `setSize` **(Many-Argument Workhorses)** (Impact: 30.3)
    * *Intent:* """ Set the ROI's size. =============== ============================================================...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 26.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 308 instances
* *State Mutation (weighted view):* 1096
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 316`, `structural_boundaries: 309`, `args: 151`, `func_start: 150`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 480`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 3`, `duplicate_logic: 5`
* *Architecture:* `io: 1`, `api: 141`, `import: 9`
* *Defense:* `safety: 11`, `doc: 54`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.957
  * `Choke Point (Betweenness):` 0.000187 | `Ripple Effect (Closeness):` 0.260099
  * `Imports (Out-Degree: 6):` ..Point, ..Qt, ..SRTTransform, ..functions, .GraphicsObject, .UIGraphicsItem, math, numpy...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/ViewBox/ViewBox.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.717)
- **Top Global Matches:** file_cluster_4: 5.717, file_cluster_12: 9.003, file_cluster_15: 10.12
- **Magnitude:** 2303.68 | **LOC:** 1876 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **59** in-repo importer(s); it depends on **13**; blast radius 10.831; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (68.4%)
- **Documentation Coverage:** 52.6316% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setRange` **(Many-Argument Workhorses)** (Impact: 143.2)
    * *Intent:* """ Set the visible range of the ViewBox. Must specify at least one of *rect*, *xRange*, or *yRange*...
  * `updateViewRange` **(Many-Argument Workhorses)** (Impact: 112.5)
    * *Intent:* # Including a prepareForPaint call is part of the Qt strategy to # defer expensive redraw opertions ...
  * `childrenBounds` **(Many-Argument Workhorses)** (Impact: 108.0)
    * *Intent:* """Return the bounding range of all children. [[xmin, xmax], [ymin, ymax]] Values may be None if the...
  * `enableAutoRange` **(Many-Argument Workhorses)** (Impact: 48.6)
    * *Intent:* """ Enable (or disable) auto-range for *axis*, which may be ViewBox.XAxis, ViewBox.YAxis, or ViewBox...
  * `mouseDragEvent` **(Many-Argument Workhorses)** (Impact: 43.0)
    * *Intent:* ## if axis is specified, event will only affect that axis. ev.accept() ## we accept all buttons pos ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 323 instances
* *State Mutation (weighted view):* 1056
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 415`, `structural_boundaries: 223`, `args: 108`, `func_start: 107`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 410`, `dead_code: 3`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 104`, `import: 13`
* *Defense:* `safety: 27`, `doc: 50`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.831
  * `Choke Point (Betweenness):` 0.008464 | `Ripple Effect (Closeness):` 0.276623
  * `Imports (Out-Degree: 17):` ...Point, ...Qt, ...debug, ...functions, ...getConfigOption, ..GraphicsWidget, ..ItemGroup, .ViewBoxMenu...
  * `Imported By (In-Degree: 59):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/AxisItem.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.442)
- **Top Global Matches:** file_cluster_4: 6.442, file_cluster_12: 9.188, file_cluster_16: 10.6
- **Magnitude:** 1666.14 | **LOC:** 1780 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **103** in-repo importer(s); it depends on **9**; blast radius 12.189; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (47.7%)
- **Documentation Coverage:** 40.8163% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generateDrawSpecs` **(Many-Argument Workhorses)** (Impact: 136.0)
    * *Intent:* """ Generate the drawing specifications for the axis, ticks, and labels. This method determines all ...
  * `tickSpacing` **(Many-Argument Workhorses)** (Impact: 52.3)
    * *Intent:* """ Determine the spacing of ticks on the axis. This method is called whenever the axis needs to be ...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 44.7)
  * `_updateMaxTextSize` **(Stateful Encapsulated Methods)** (Impact: 30.7)
    * *Intent:* ## Informs that the maximum tick size orthogonal to the axis has ## changed; we use this to decide w...
  * `setStyle` **(Many-Argument Workhorses)** (Impact: 29.6)
    * *Intent:* #self.setCacheMode(self.DeviceCoordinateCache) """ Set various style options. Parameters ---------- ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 286 instances
* *State Mutation (weighted view):* 906
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 120`, `args: 52`, `func_start: 52`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 334`, `fragile_debt: 1`
* *Architecture:* `api: 48`, `import: 9`
* *Defense:* `safety: 9`, `doc: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.189
  * `Choke Point (Betweenness):` 0.003769 | `Ripple Effect (Closeness):` 0.292218
  * `Imports (Out-Degree: 12):` ..Point, ..Qt, ..debug, ..functions, ..getConfigOption, .GraphicsWidget, math, numpy...
  * `Imported By (In-Degree: 103):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/PlotCurveItem.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.853)
- **Top Global Matches:** file_cluster_4: 5.853, file_cluster_6: 7.211, file_cluster_16: 13.497
- **Magnitude:** 1484.36 | **LOC:** 1294 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **9**; blast radius 2.455; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.7%)
- **Documentation Coverage:** 71.2329% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `paintGL` **(Many-Argument Workhorses)** (Impact: 97.3)
  * `paint` **(Many-Argument Workhorses)** (Impact: 68.7)
  * `dataBounds` **(Many-Argument Workhorses)** (Impact: 64.0)
    * *Intent:* ## Need this to run as fast as possible. ## check cache first: cache = self._boundsCache[ax] if cach...
  * `updateData` **(Stateful Encapsulated Methods)** (Impact: 64.0)
  * `arrayToLineSegments` **(Many-Argument Workhorses)** (Impact: 58.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 257 instances
* *State Mutation (weighted view):* 840
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 114`, `args: 42`, `func_start: 42`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 326`, `dead_code: 9`, `fragile_debt: 2`
* *Architecture:* `api: 35`, `import: 12`
* *Defense:* `safety: 19`, `doc: 17`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.455
  * `Choke Point (Betweenness):` 0.000879 | `Ripple Effect (Closeness):` 0.254623
  * `Imports (Out-Degree: 12):` ..Qt, ..debug, ..functions, ..getConfigOption, .GraphicsObject, importlib, math, numpy...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/ScatterPlotItem.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.941)
- **Top Global Matches:** file_cluster_12: 6.941, file_cluster_16: 7.557, file_cluster_15: 7.916
- **Magnitude:** 1450.0 | **LOC:** 1242 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **11**; blast radius 7.99; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.3%)
- **Documentation Coverage:** 62.406% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addPoints` **(Many-Argument Workhorses)** (Impact: 80.0)
    * *Intent:* """ Add new points to the scatter plot. Arguments are the same as setData() """
  * `paint` **(Many-Argument Workhorses)** (Impact: 35.3)
  * `dataBounds` **(Many-Argument Workhorses)** (Impact: 35.2)
  * `setPointData` **(Defensive Guards)** (Impact: 27.7)
  * `setSymbol` **(Many-Argument Workhorses)** (Impact: 24.4)
    * *Intent:* """Set the symbol(s) used to draw each spot. If a list or array is provided, then the symbol for eac...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 224 instances
* *State Mutation (weighted view):* 754
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 144`, `args: 76`, `func_start: 75`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 306`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `api: 60`, `import: 11`
* *Defense:* `safety: 35`, `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.99
  * `Choke Point (Betweenness):` 0.006533 | `Ripple Effect (Closeness):` 0.293005
  * `Imports (Out-Degree: 12):` ..Point, ..Qt, ..debug, ..functions, ..getConfigOption, .GraphicsObject, collections, itertools...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `pyqtgraph/debug.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.341)
- **Top Global Matches:** file_cluster_12: 8.341, file_cluster_7: 9.109, file_cluster_5: 10.083
- **Magnitude:** 1404.62 | **LOC:** 1296 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **22**; blast radius 11.075; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.5%), Connectivity (formerly Api Exposure) (84.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 52.7607% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `objectSize` **(Many-Argument Workhorses)** (Impact: 63.4)
    * *Intent:* """Guess how much memory an object is using"""
  * `findRefPath` **(Many-Argument Workhorses)** (Impact: 57.5)
    * *Intent:* """Determine all paths of object references from startObj to endObj"""
  * `searchRefs` **(Compute Cores)** (Impact: 28.8)
    * *Intent:* """Pseudo-interactive function for tracing references backward. **Arguments:** obj: The initial obje...
  * `diff` **(Many-Argument Workhorses)** (Impact: 27.5)
    * *Intent:* #self.newRefs.clear() #self.newRefs.update(refs) """ Compute all differences between the current obj...
  * `refPathString` **(Defensive Guards)** (Impact: 26.6)
    * *Intent:* """Given a list of adjacent objects in a reference path, print the 'natural' path names (ie, attribu...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 213 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 689
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 246`, `args: 82`, `func_start: 80`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 263`, `dead_code: 14`
* *Architecture:* `io: 22`, `api: 72`, `concurrency: 6`, `import: 23`
* *Defense:* `safety: 55`, `doc: 42`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.075
  * `Choke Point (Betweenness):` 0.002422 | `Ripple Effect (Closeness):` 0.273969
  * `Imports (Out-Degree: 3):` .Qt, .util, .util.mutex, PyQt5, __future__, cProfile, contextlib, faulthandler...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/PlotDataItem.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.82)
- **Top Global Matches:** file_cluster_4: 5.82, file_cluster_16: 10.708, file_cluster_12: 10.9
- **Magnitude:** 1310.3 | **LOC:** 1890 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **12**; blast radius 3.375; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (53.6%)
- **Documentation Coverage:** 42.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setData` **(Many-Argument Workhorses)** (Impact: 114.7)
  * `_getDisplayDataset` **(Stateful Encapsulated Methods)** (Impact: 92.8)
    * *Intent:* """ Get data suitable for display as a :class:`PlotDataset`. Warnings -------- This method is not co...
  * `updateItems` **(Many-Argument Workhorses)** (Impact: 39.6)
    * *Intent:* """ Update the displayed curve and scatter plot. This method is called internally to redraw the curv...
  * `dataType` **(Defensive Guards)** (Impact: 25.2)
  * `viewRangeChanged` **(Stateful Encapsulated Methods)** (Impact: 21.2)
    * *Intent:* # def viewTransformChanged(self): # """ view transform (and thus range) has changed, replot if neede...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 215 instances
* *State Mutation (weighted view):* 691
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 131`, `args: 52`, `func_start: 52`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 261`, `dead_code: 7`
* *Architecture:* `api: 53`, `import: 12`
* *Defense:* `safety: 18`, `doc: 35`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.375
  * `Choke Point (Betweenness):` 0.001245 | `Ripple Effect (Closeness):` 0.257331
  * `Imports (Out-Degree: 12):` ..Qt, ..debug, ..functions, ..getConfigOption, .GraphicsObject, .PlotCurveItem, .ScatterPlotItem, bisect...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/PlotItem/PlotItem.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.976)
- **Top Global Matches:** file_cluster_12: 6.976, file_cluster_4: 7.735, file_cluster_5: 8.887
- **Magnitude:** 1184.02 | **LOC:** 1646 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **73** in-repo importer(s); it depends on **23**; blast radius 12.506; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.2%), Guard Balance (formerly Safety Score) (75.2%)
- **Documentation Coverage:** 51.634% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `multiDataPlot` **(Many-Argument Workhorses)** (Impact: 52.4)
    * *Intent:* """ Allow plotting multiple curves on the same plot in one call. Parameters ---------- x, y : array_...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 52.3)
  * `showAxes` **(Many-Argument Workhorses)** (Impact: 47.3)
    * *Intent:* """ Convenience method for quickly configuring axis settings. Parameters ---------- selection : bool...
  * `setDownsampling` **(Many-Argument Workhorses)** (Impact: 34.1)
    * *Intent:* """ Set the downsampling mode for the PlotItem. Downsampling reduces the number of samples drawn to ...
  * `addItem` **(Many-Argument Workhorses)** (Impact: 30.6)
    * *Intent:* """ Add a :class:`~pyqtgraph.GraphicsItem` to the :class:`~pyqtgraph.ViewBox`. If the item has plot ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 133 instances
* *State Mutation (weighted view):* 448
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 179`, `args: 77`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 182`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 75`, `import: 24`
* *Defense:* `safety: 13`, `doc: 38`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.506
  * `Choke Point (Betweenness):` 0.01696 | `Ripple Effect (Closeness):` 0.250233
  * `Imports (Out-Degree: 20):` ...Qt, ...WidgetGroup, ...exporters, ...functions, ...icons, ...widgets.FileDialog, ..AxisItem, ..ButtonItem...
  * `Imported By (In-Degree: 73):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/ImageItem.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.947)
- **Top Global Matches:** file_cluster_4: 5.947, file_cluster_16: 10.924, file_cluster_6: 11.22
- **Magnitude:** 1071.28 | **LOC:** 1227 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **15**; blast radius 2.998; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (46.7%)
- **Documentation Coverage:** 56.383% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getHistogram` **(Many-Argument Workhorses)** (Impact: 64.0)
  * `setImage` **(Stateful Encapsulated Methods)** (Impact: 59.7)
  * `render` **(Stateful Encapsulated Methods)** (Impact: 51.2)
    * *Intent:* # Convert data to QImage for display. self._unrenderable = True if self.image is None or self.image....
  * `setOpts` **(Many-Argument Workhorses)** (Impact: 36.5)
    * *Intent:* """ Set display and processing options for this ImageItem. :class:`~pyqtgraph.ImageItem` and :meth:`...
  * `drawAt` **(Many-Argument Workhorses)** (Impact: 24.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 160 instances
* *State Mutation (weighted view):* 534
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 132`, `args: 49`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 214`, `dead_code: 1`
* *Architecture:* `io: 4`, `api: 47`, `import: 15`
* *Defense:* `safety: 10`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.998
  * `Choke Point (Betweenness):` 0.003353 | `Ripple Effect (Closeness):` 0.257028
  * `Imports (Out-Degree: 14):` ..Point, ..Qt, ..colormap, ..debug, ..functions, ..functions_qimage, ..getConfigOption, ..util.cupy_helper...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `pyqtgraph/flowchart/Flowchart.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.658)
- **Top Global Matches:** file_cluster_12: 6.658, file_cluster_7: 8.133, file_cluster_5: 9.138
- **Magnitude:** 897.16 | **LOC:** 926 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **17**; blast radius 1.913; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (65.4%)
- **Documentation Coverage:** 74.8148% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process` **(Many-Argument Workhorses)** (Impact: 36.6)
    * *Intent:* """ Process data through the flowchart, returning the output. Keyword arguments must be the names of...
  * `nodeOutputChanged` **(Many-Argument Workhorses)** (Impact: 21.4)
    * *Intent:* """Triggered when a node's output values have changed. (NOT called during process()) Propagates new ...
  * `processOrder` **(Defensive Guards)** (Impact: 19.2)
    * *Intent:* """Return the order of operations required to process this chart. The order returned should look lik...
  * `hoverOver` **(Defensive Guards)** (Impact: 18.4)
    * *Intent:* #print "FlowchartWidget.hoverOver called." term = None for item in items: if item is self.hoverItem:...
  * `selectionChanged` **(Defensive Guards)** (Impact: 16.8)
    * *Intent:* #print "FlowchartWidget.selectionChanged called." items = self._scene.selectedItems() #print " scene...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 129 instances
* *State Mutation (weighted view):* 444
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 158`, `args: 71`, `func_start: 69`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 186`, `dead_code: 4`
* *Architecture:* `io: 1`, `api: 70`, `import: 16`
* *Defense:* `safety: 30`, `doc: 19`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.913
  * `Choke Point (Betweenness):` 0.002043 | `Ripple Effect (Closeness):` 0.011078
  * `Imports (Out-Degree: 26):` ..DataTreeWidget, ..FileDialog, ..Qt, ..configfile, ..debug, ..dockarea, ..functions, ..graphicsItems.GraphicsObject...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pyqtgraph/multiprocess/remoteproxy.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.507)
- **Top Global Matches:** file_cluster_12: 7.507, file_cluster_7: 9.47, file_cluster_5: 10.041
- **Magnitude:** 879.72 | **LOC:** 1143 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **11**; blast radius 1.756; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (97.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.2%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleRequest` **(Defensive Guards)** (Impact: 78.7)
    * *Intent:* """Handle a single request from the remote process. Blocks until a request is available."""
  * `send` **(Many-Argument Workhorses)** (Impact: 51.3)
    * *Intent:* """Send a request or return packet to the remote process. Generally it is not necessary to call this...
  * `callObj` **(Many-Argument Workhorses)** (Impact: 23.6)
  * `getResult` **(Defensive Guards)** (Impact: 21.0)
    * *Intent:* ## raises NoResultError if the result is not available yet #print self.results.keys(), os.getpid() w...
  * `result` **(Stateful Encapsulated Methods)** (Impact: 19.6)
    * *Intent:* """ Return the result for this request. If block is True, wait until the result has arrived or *time...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 89 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 49
* *State Mutation (weighted view):* 309
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 243`, `args: 93`, `func_start: 93`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 2`, `state_mutation: 131`, `dead_code: 4`
* *Architecture:* `io: 13`, `api: 85`, `concurrency: 9`, `import: 13`
* *Defense:* `safety: 29`, `doc: 22`, `sync_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.756
  * `Choke Point (Betweenness):` 3.2e-05 | `Ripple Effect (Closeness):` 0.183571
  * `Imports (Out-Degree: 1):` ..util, builtins, numpy, os, pickle, sys, threading, time...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `pyqtgraph/imageview/ImageView.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.096)
- **Top Global Matches:** file_cluster_4: 6.096, file_cluster_12: 8.389, file_cluster_15: 8.679
- **Magnitude:** 866.14 | **LOC:** 946 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **18**; blast radius 4.518; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.3%), Connectivity (formerly Api Exposure) (56.1%)
- **Documentation Coverage:** 51.2195% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setImage` **(Many-Argument Workhorses)** (Impact: 141.3)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 51.7)
  * `normalize` **(Compute Cores)** (Impact: 28.3)
    * *Intent:* """ Process *image* using the normalization options configured in the control panel. This can be rep...
  * `roiChanged` **(Compute Cores)** (Impact: 27.1)
    * *Intent:* # Extract image data from ROI if self.image is None: return image = self.getProcessedImage() # getAr...
  * `keyPressEvent` **(Compute Cores)** (Impact: 15.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 107 instances
* *State Mutation (weighted view):* 357
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 114`, `args: 40`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 143`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 40`, `import: 19`
* *Defense:* `safety: 8`, `doc: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.518
  * `Choke Point (Betweenness):` 0.00274 | `Ripple Effect (Closeness):` 0.254029
  * `Imports (Out-Degree: 22):` ..Qt, ..SignalProxy, ..debug, ..functions, ..getConfigOption, ..graphicsItems.GradientEditorItem, ..graphicsItems.ImageItem, ..graphicsItems.InfiniteLine...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `pyqtgraph/colormap.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.991)
- **Top Global Matches:** file_cluster_4: 6.991, file_cluster_12: 9.506, file_cluster_9: 11.27
- **Magnitude:** 861.46 | **LOC:** 847 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **25** in-repo importer(s); it depends on **7**; blast radius 4.22; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.3%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.4%)
- **Documentation Coverage:** 8.4746% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `map` **(Many-Argument Workhorses)** (Impact: 37.2)
    * *Intent:* """ map(data, mode=ColorMap.BYTE) Returns an array of colors corresponding to a single value or an a...
  * `_getFromFile` **(Stateful Encapsulated Methods)** (Impact: 30.7)
  * `getSubset` **(Many-Argument Workhorses)** (Impact: 21.4)
    * *Intent:* """ Returns a new ColorMap object that extracts the subset specified by 'start' and 'length' to the ...
  * `getFromMatplotlib` **(Defensive Guards)** (Impact: 20.6)
    * *Intent:* """ Generates a ColorMap object from a Matplotlib definition. Same as ``colormap.get(name, source='m...
  * `getStops` **(Compute Cores)** (Impact: 20.5)
    * *Intent:* """ Returns a tuple (stops, colors) containing a list of all stops (ranging 0.0 to 1.0) and a list o...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 155 instances
* *State Mutation (weighted view):* 499
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 108`, `args: 30`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 189`, `dead_code: 2`
* *Architecture:* `io: 1`, `api: 31`, `import: 9`
* *Defense:* `safety: 27`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.22
  * `Choke Point (Betweenness):` 0.001405 | `Ripple Effect (Closeness):` 0.269101
  * `Imports (Out-Degree: 2):` .Qt, .functions, collections.abc, colorcet, matplotlib.pyplot, numpy, os
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/GradientEditorItem.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.771)
- **Top Global Matches:** file_cluster_12: 6.771, file_cluster_15: 7.496, file_cluster_16: 8.47
- **Magnitude:** 785.44 | **LOC:** 981 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **10**; blast radius 1.943; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.7%), Connectivity (formerly Api Exposure) (73.9%)
- **Documentation Coverage:** 74.5763% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getColor` **(Many-Argument Workhorses)** (Impact: 38.9)
    * *Intent:* """ Return a color for a given value. ============== ===============================================...
  * `mouseClickEvent` **(Compute Cores)** (Impact: 14.4)
    * *Intent:* #return #pos = self.mapToScene(ev.pos()) #if ev.button() == QtCore.Qt.MouseButton.LeftButton and sel...
  * `setOrientation` **(Many-Argument Workhorses)** (Impact: 12.2)
    * *Intent:* ## public """Set the orientation of the TickSliderItem. ============== =============================...
  * `mouseDragEvent` **(Compute Cores)** (Impact: 11.3)
  * `getLookupTable` **(Many-Argument Workhorses)** (Impact: 11.2)
    * *Intent:* """ Return an RGB(A) lookup table (ndarray). ============== ========================================...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 106 instances
* *State Mutation (weighted view):* 375
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 123`, `args: 65`, `func_start: 62`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 163`, `dead_code: 18`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 60`, `import: 10`
* *Defense:* `safety: 2`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.943
  * `Choke Point (Betweenness):` 0.000724 | `Ripple Effect (Closeness):` 0.254325
  * `Imports (Out-Degree: 7):` ..Qt, ..colormap, ..functions, ..widgets.ColorMapMenu, ..widgets.SpinBox, .GradientPresets, .GraphicsWidget, numpy...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/PColorMeshItem.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.167)
- **Top Global Matches:** file_cluster_4: 5.167, file_cluster_6: 8.212, file_cluster_15: 12.116
- **Magnitude:** 762.74 | **LOC:** 787 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 1.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (83.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 84.3137% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `paintGL` **(Many-Argument Workhorses)** (Impact: 43.5)
  * `_prepareData` **(Stateful Encapsulated Methods)** (Impact: 31.0)
    * *Intent:* """ Check the shape of the data. Return a set of 2d array x, y, z ready to be used to draw the pictu...
  * `setup` **(Many-Argument Workhorses)** (Impact: 31.0)
  * `paint` **(Many-Argument Workhorses)** (Impact: 26.2)
  * `_drawPicture` **(Compute Cores)** (Impact: 21.7)
    * *Intent:* # on entry, the following members are all valid: x, y, z, levels # this function does not alter any ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 135 instances
* *State Mutation (weighted view):* 450
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 76`, `args: 29`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `state_mutation: 180`, `dead_code: 1`
* *Architecture:* `api: 27`, `import: 11`
* *Defense:* `safety: 4`, `doc: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.027
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.249087
  * `Imports (Out-Degree: 5):` ..Qt, ..colormap, ..functions, .GraphicsObject, enum, importlib, numpy
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/examples/relativity/relativity.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.989)
- **Top Global Matches:** file_cluster_12: 5.989, file_cluster_15: 6.995, file_cluster_16: 8.229
- **Magnitude:** 740.34 | **LOC:** 763 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 1.33; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (84.7%), Complexity Load (formerly Cognitive Load) (67.8%), Connectivity (formerly Api Exposure) (66.9%), Dead Code Surface (formerly Dead Code) (3.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hypIntersect` **(Many-Argument Workhorses)** (Impact: 24.4)
    * *Intent:* ## given a reference clock (seen from inertial frame) has rx, rt, and rv, ## and another clock start...
  * `runReference` **(Many-Argument Workhorses)** (Impact: 21.9)
  * `getCurve` **(Compute Cores)** (Impact: 19.6)
  * `stepTo` **(Compute Cores)** (Impact: 15.4)
  * `runInertial` **(Compute Cores)** (Impact: 13.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 114 instances
* *State Mutation (weighted view):* 440
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 122`, `args: 44`, `func_start: 44`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 212`, `dead_code: 6`
* *Architecture:* `io: 9`, `api: 44`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.33
  * `Choke Point (Betweenness):` 0.00069 | `Ripple Effect (Closeness):` 0.003766
  * `Imports (Out-Degree: 13):` collections, numpy, os, pyqtgraph, pyqtgraph.Qt, pyqtgraph.parametertree, sys, time
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyqtgraph/parametertree/Parameter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.067)
- **Top Global Matches:** file_cluster_12: 6.067, file_cluster_7: 8.836, file_cluster_15: 9.164
- **Magnitude:** 703.46 | **LOC:** 879 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **36** in-repo importer(s); it depends on **7**; blast radius 7.282; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.7%), Connectivity (formerly Api Exposure) (73.6%)
- **Documentation Coverage:** 25.5639% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `restoreState` **(Many-Argument Workhorses)** (Impact: 43.4)
    * *Intent:* """ Restore the state of this parameter and its children from a structure generated using saveState(...
  * `insertChild` **(Many-Argument Workhorses)** (Impact: 29.0)
    * *Intent:* """ Insert a new child at pos. If pos is a Parameter, then insert at the position of that Parameter....
  * `setName` **(Compute Cores)** (Impact: 18.0)
    * *Intent:* """Attempt to change the name of this parameter; return the actual name. (The parameter may reject t...
  * `setOpts` **(Compute Cores)** (Impact: 16.9)
    * *Intent:* """ Set any arbitrary options on this parameter. The exact behavior of this function will depend on ...
  * `saveState` **(Compute Cores)** (Impact: 16.8)
    * *Intent:* """ Return a structure representing the entire state of the parameter tree. The tree state may be re...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 282
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 161`, `args: 73`, `func_start: 73`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 118`, `dead_code: 3`
* *Architecture:* `api: 62`, `import: 7`
* *Defense:* `safety: 16`, `doc: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.282
  * `Choke Point (Betweenness):` 0.004745 | `Ripple Effect (Closeness):` 0.206745
  * `Imports (Out-Degree: 3):` ..Qt, ..functions, .ParameterItem, collections, re, warnings, weakref
  * `Imported By (In-Degree: 36):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/InfiniteLine.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.959)
- **Top Global Matches:** file_cluster_16: 6.959, file_cluster_15: 7.043, file_cluster_12: 7.297
- **Magnitude:** 702.18 | **LOC:** 622 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **9**; blast radius 2.402; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (46.9%)
- **Documentation Coverage:** 63.1579% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 47.2)
  * `setPos` **(Defensive Guards)** (Impact: 29.3)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 23.9)
  * `addMarker` **(Many-Argument Workhorses)** (Impact: 22.3)
    * *Intent:* """Add a marker to be displayed on the line. ============= =========================================...
  * `setHoverPen` **(Defensive Guards)** (Impact: 15.0)
    * *Intent:* """Set the pen for drawing the line while the mouse hovers over it. Allowable arguments are any that...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 108 instances
* *State Mutation (weighted view):* 357
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 84`, `args: 40`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 141`, `dead_code: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 39`, `import: 9`
* *Defense:* `safety: 5`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.402
  * `Choke Point (Betweenness):` 0.000357 | `Ripple Effect (Closeness):` 0.25522
  * `Imports (Out-Degree: 8):` ..Point, ..Qt, ..functions, .GraphicsItem, .GraphicsObject, .TextItem, .ViewBox, math...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `pyqtgraph/flowchart/Terminal.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.695)
- **Top Global Matches:** file_cluster_12: 5.695, file_cluster_15: 6.481, file_cluster_16: 7.52
- **Magnitude:** 640.66 | **LOC:** 584 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.684; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.8%), Connectivity (formerly Api Exposure) (60.4%)
- **Documentation Coverage:** 85.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `recolor` **(Compute Cores)** (Impact: 24.9)
  * `connectTo` **(Many-Argument Workhorses)** (Impact: 23.4)
  * `mouseDragEvent` **(Defensive Guards)** (Impact: 20.9)
  * `setValue` **(Stateful Encapsulated Methods)** (Impact: 16.9)
    * *Intent:* """If this is a single-value terminal, val should be a single value. If this is a multi-value termin...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 12.3)
    * *Intent:* """ Construct a new terminal. ============== =======================================================...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 213
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 130`, `args: 72`, `func_start: 72`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 101`, `duplicate_logic: 2`
* *Architecture:* `api: 73`, `import: 5`
* *Defense:* `safety: 6`, `doc: 11`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.684
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.008138
  * `Imports (Out-Degree: 4):` ..Point, ..Qt, ..functions, ..graphicsItems.GraphicsObject, weakref
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/opengl/GLViewWidget.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.157)
- **Top Global Matches:** file_cluster_12: 6.157, file_cluster_4: 8.888, file_cluster_15: 8.914
- **Magnitude:** 622.56 | **LOC:** 569 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **10**; blast radius 1.863; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (60.4%)
- **Documentation Coverage:** 63.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setCameraPosition` **(Many-Argument Workhorses)** (Impact: 49.4)
  * `drawItemTree` **(Defensive Guards)** (Impact: 25.6)
  * `pan` **(Many-Argument Workhorses)** (Impact: 22.8)
    * *Intent:* """ Moves the center (look-at) position while holding the camera in place. ============== ==========...
  * `mouseMoveEvent` **(Defensive Guards)** (Impact: 18.2)
  * `evalKeyState` **(Compute Cores)** (Impact: 15.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 84 instances
* *State Mutation (weighted view):* 311
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 83`, `args: 39`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 143`
* *Architecture:* `api: 37`, `import: 11`
* *Defense:* `safety: 13`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.863
  * `Choke Point (Betweenness):` 0.005544 | `Ripple Effect (Closeness):` 0.035154
  * `Imports (Out-Degree: 7):` ..Qt, ..Vector, ..debug, ..functions, ..getConfigOption, OpenGL, importlib, math...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `pyqtgraph/examples/ExampleApp.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.153)
- **Top Global Matches:** file_cluster_4: 7.153, file_cluster_12: 7.349, file_cluster_15: 7.88
- **Magnitude:** 614.86 | **LOC:** 606 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **14**; blast radius 1.86; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (82.7%), Connectivity (formerly Api Exposure) (67.8%), Complexity Load (formerly Cognitive Load) (57.1%)
- **Documentation Coverage:** 73.0769% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `match_multiline` **(Many-Argument Workhorses)** (Impact: 49.0)
    * *Intent:* """Do highlighting of multi-line strings. =========== ==============================================...
  * `keyPressEvent` **(Compute Cores)** (Impact: 17.0)
  * `highlightBlock` **(Compute Cores)** (Impact: 15.0)
    * *Intent:* """Apply syntax highlighting to the given block of text. """
  * `populateTree` **(Defensive Guards)** (Impact: 14.9)
  * `getMatchingTitles` **(Defensive Guards)** (Impact: 14.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 86 instances
* *State Mutation (weighted view):* 344
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 75`, `args: 27`, `func_start: 27`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 3`, `state_mutation: 172`
* *Architecture:* `io: 13`, `api: 29`, `import: 14`
* *Defense:* `safety: 10`, `doc: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.86
  * `Choke Point (Betweenness):` 0.001155 | `Ripple Effect (Closeness):` 0.006026
  * `Imports (Out-Degree: 15):` argparse, collections, exampleLoaderTemplate_generic, functools, keyword, os, pkgutil, pyqtgraph...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pyqtgraph/parametertree/interactive.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.891)
- **Top Global Matches:** file_cluster_12: 6.891, file_cluster_4: 8.933, file_cluster_16: 9.583
- **Magnitude:** 587.26 | **LOC:** 635 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **7**; blast radius 1.472; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (41.0%)
- **Documentation Coverage:** 42.1053% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `interact` **(Many-Argument Workhorses)** (Impact: 82.7)
  * `createFunctionParameter` **(Many-Argument Workhorses)** (Impact: 23.0)
    * *Intent:* """ Constructs a dict ready for insertion into a group parameter based on the provided information i...
  * `functionToParameterDict` **(Many-Argument Workhorses)** (Impact: 22.2)
    * *Intent:* """ Converts a function into a list of child parameter dicts """
  * `resolveAndHookupParameterChild` **(Compute Cores)** (Impact: 11.8)
  * `_nameToTitle` **(Stateful Encapsulated Methods)** (Impact: 11.2)
    * *Intent:* """ Converts a function name to a title based on ``self.titleFormat``. Parameters ---------- name: s...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 289
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 90`, `args: 32`, `func_start: 32`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 115`
* *Architecture:* `api: 21`, `import: 7`
* *Defense:* `safety: 10`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.472
  * `Choke Point (Betweenness):` 0.000699 | `Ripple Effect (Closeness):` 0.148097
  * `Imports (Out-Degree: 4):` ..functions, .Parameter, .parameterTypes, contextlib, functools, inspect, pydoc
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `pyqtgraph/examples/optics/pyoptic.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.415)
- **Top Global Matches:** file_cluster_12: 5.415, file_cluster_15: 8.161, file_cluster_7: 8.342
- **Magnitude:** 577.0 | **LOC:** 562 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 1.153; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (84.7%), Connectivity (formerly Api Exposure) (67.2%), Complexity Load (formerly Cognitive Load) (58.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (30.8%)
- **Documentation Coverage:** 83.908% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `intersectRay` **(Compute Cores)** (Impact: 27.0)
    * *Intent:* ## return the point of intersection and the angle of incidence #print "intersect ray" h = self.h2 r ...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 14.7)
    * *Intent:* """ Arguments for each surface are: x1,x2 - position of center of _physical surface_ r1,r2 - radius ...
  * `transmissionCurve` **(Type Conversions)** (Impact: 11.1)
  * `__init__` **(Compute Cores)** (Impact: 9.9)
  * `propagateRay` **(Many-Argument Workhorses)** (Impact: 7.5)
    * *Intent:* """Refract, reflect, absorb, and/or scatter ray. This function may create and return new rays"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 337
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 97`, `args: 48`, `func_start: 48`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 149`, `fragile_debt: 3`, `duplicate_logic: 5`
* *Architecture:* `io: 3`, `api: 48`, `import: 8`
* *Defense:* `safety: 4`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.153
  * `Choke Point (Betweenness):` 0.000558 | `Ripple Effect (Closeness):` 0.001883
  * `Imports (Out-Degree: 7):` csv, gzip, math, numpy, os, pyqtgraph, pyqtgraph.Qt
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/opengl/MeshData.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.645)
- **Top Global Matches:** file_cluster_16: 6.645, file_cluster_12: 7.021, file_cluster_15: 7.506
- **Magnitude:** 573.26 | **LOC:** 515 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **3**; blast radius 1.993; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (40.1%)
- **Documentation Coverage:** 15.0943% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 24.3)
    * *Intent:* """ ============== ===================================================== **Arguments:** vertexes (Nv...
  * `setVertexes` **(Stateful Encapsulated Methods)** (Impact: 16.7)
    * *Intent:* """ Set the array (Nv, 3) of vertex coordinates. If indexed=='faces', then the data must have shape ...
  * `vertexes` **(Stateful Encapsulated Methods)** (Impact: 14.6)
    * *Intent:* """Return an array (N,3) of the positions of vertexes in the mesh. By default, each unique vertex ap...
  * `vertexNormals` **(Stateful Encapsulated Methods)** (Impact: 13.5)
    * *Intent:* """ Return an array of normal vectors. By default, the array will be (N, 3) with one entry per uniqu...
  * `save` **(Compute Cores)** (Impact: 12.3)
    * *Intent:* """Serialize this mesh to a string appropriate for disk storage"""
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 89 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 326
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 61`, `args: 27`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 148`, `dead_code: 4`
* *Architecture:* `api: 25`, `import: 4`
* *Defense:* `safety: 4`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.993
  * `Choke Point (Betweenness):` 2.4e-05 | `Ripple Effect (Closeness):` 0.032905
  * `Imports (Out-Degree: 1):` ..Qt, numpy, pickle
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/dockarea/test_dockarea.py` (PYTHON) | Magnitude: 93.92 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 191, structural_boundaries: 64, safety: 47, core_var_decl: 45
- `pyqtgraph/examples/scrollingPlots.py` (PYTHON) | Magnitude: 105.96 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 41, indent_spaces: 41, core_var_decl: 30, design_snake_case: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `pyqtgraph/WidgetGroup.py` (PYTHON) | Magnitude: 266.18 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 200, branch: 58, structural_boundaries: 57, state_mutation: 38
- `pyqtgraph/exporters/Exporter.py` (PYTHON) | Magnitude: 160.66 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 86, structural_boundaries: 31, state_mutation: 30, branch: 26
- `tests/test_functions.py` (PYTHON) | Magnitude: 288.08 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 390, structural_boundaries: 101, state_mutation: 91, core_var_decl: 91

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tests/graphicsItems/test_ScatterPlotItem.py` (PYTHON) | Magnitude: 30.14 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 67, structural_boundaries: 19, core_var_decl: 15, state_mutation: 14
- `tests/graphicsItems/test_ArrowItem.py` (PYTHON) | Magnitude: 5.34 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 4, state_mutation: 3, core_var_decl: 3
- `pyqtgraph/graphicsItems/LinearRegionItem.py` (PYTHON) | Magnitude: 315.84 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 210, state_mutation: 60, branch: 52, structural_boundaries: 47
- `pyqtgraph/examples/ColorBarItem.py` (PYTHON) | Magnitude: 28.72 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 54, core_var_decl: 34, design_snake_case: 29, state_mutation: 19
- `pyqtgraph/graphicsItems/PlotItem/plotConfigTemplate_generic.py` (PYTHON) | Magnitude: 58.6 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 168, state_mutation: 38, structural_boundaries: 6, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `pyqtgraph/Qt/__init__.py` (PYTHON) | Magnitude: 214.66 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 211, structural_boundaries: 94, state_mutation: 82, core_var_decl: 69
- `pyqtgraph/graphicsItems/InfiniteLine.py` (PYTHON) | Magnitude: 702.18 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 367, state_mutation: 141, branch: 100, structural_boundaries: 84
- `pyqtgraph/graphicsItems/GraphicsWidget.py` (PYTHON) | Magnitude: 62.28 | Delta: **0.153** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 22, state_mutation: 15, encapsulation: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `pyqtgraph/parametertree/parameterTypes/__init__.py` (PYTHON) | Magnitude: 15.88 | Delta: **0.143** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 40, import: 20, core_var_decl: 19, design_snake_case: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/graphicsItems/test_TextItem.py` (PYTHON) | Magnitude: 8.22 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 6, state_mutation: 5, core_var_decl: 5
- `tests/graphicsItems/ViewBox/test_ViewBox.py` (PYTHON) | Magnitude: 42.74 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 60, state_mutation: 27, core_var_decl: 27, design_snake_case: 26
- `tests/widgets/test_busycursor.py` (PYTHON) | Magnitude: 3.58 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 6, safety: 3, args: 1
- `tests/widgets/test_graphics_view.py` (PYTHON) | Magnitude: 14.86 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 38, safety: 34, state_mutation: 8
- `tests/widgets/test_combobox.py` (PYTHON) | Magnitude: 9.08 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 12, safety: 9, state_mutation: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `tools/setupHelpers.py` (PYTHON) | Magnitude: 0.17 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 132, core_var_decl: 38, state_mutation: 37, structural_boundaries: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `pyqtgraph/functions.py` (PYTHON) | Magnitude: 3051.84 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 1692, state_mutation: 617, core_var_decl: 572, design_snake_case: 486

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `pyqtgraph/examples/verlet_chain/relax.py` (PYTHON) | Magnitude: 65.98 | Delta: **0.147** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 32, state_mutation: 13, core_var_decl: 13, design_snake_case: 11

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `pyqtgraph/Qt/__init__.py` -> Churn: **100.0%** | Cog Load: 79.9177% | Debt: 0.0%
- `pyqtgraph/functions.py` -> Churn: **90.54%** | Cog Load: 51.191% | Debt: 0.0%
- `pyqtgraph/graphicsItems/PColorMeshItem.py` -> Churn: **83.12%** | Cog Load: 57.8788% | Debt: 0.0%
- `pyqtgraph/graphicsItems/PlotCurveItem.py` -> Churn: **68.16%** | Cog Load: 74.6599% | Debt: 10.5283%
- `pyqtgraph/widgets/ColorMapButton.py` -> Churn: **65.39%** | Cog Load: 73.8278% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `pyqtgraph/graphicsItems/AxisItem.py` -> **oyvindlr** (100.0% isolated ownership) | Magnitude: 1666.14
- `pyqtgraph/graphicsItems/PlotCurveItem.py` -> **KIU Shueng Chuan** (100.0% isolated ownership) | Magnitude: 1484.36
- `pyqtgraph/graphicsItems/PlotDataItem.py` -> **Ogi Moore** (100.0% isolated ownership) | Magnitude: 1310.3
- `pyqtgraph/imageview/ImageView.py` -> **KIU Shueng Chuan** (100.0% isolated ownership) | Magnitude: 866.14
- `pyqtgraph/graphicsItems/PColorMeshItem.py` -> **KIU Shueng Chuan** (100.0% isolated ownership) | Magnitude: 762.74

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pyqtgraph/__init__.py` -> **Severity: 14.061** (Bridge: 0.1406 * Flux: 100.0%)
- `pyqtgraph/functions.py` -> **Severity: 4.413** (Bridge: 0.0441 * Flux: 100.0%)
- `pyqtgraph/graphicsItems/PlotItem/PlotItem.py` -> **Severity: 1.696** (Bridge: 0.017 * Flux: 100.0%)
- `pyqtgraph/widgets/ColorMapWidget.py` -> **Severity: 0.987** (Bridge: 0.0099 * Flux: 100.0%)
- `pyqtgraph/widgets/DataFilterWidget.py` -> **Severity: 0.987** (Bridge: 0.0099 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pyqtgraph/Qt/__init__.py` -> **Severity: 39.905** (Embedded: 0.5512 * Error Risk: 72.3958%)
- `pyqtgraph/__init__.py` -> **Severity: 37.22** (Embedded: 0.4062 * Error Risk: 91.6392%)
- `pyqtgraph/functions.py` -> **Severity: 30.274** (Embedded: 0.3511 * Error Risk: 86.218%)
- `pyqtgraph/Qt/internals.py` -> **Severity: 27.965** (Embedded: 0.3353 * Error Risk: 83.3971%)
- `pyqtgraph/graphicsItems/AxisItem.py` -> **Severity: 25.919** (Embedded: 0.2922 * Error Risk: 88.6985%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pyqtgraph/Qt/__init__.py` -> **Severity: 11949.47** (Blast Radius: 141.9 * Doc Risk: 84.2105%)
- `pyqtgraph/Qt/internals.py` -> **Severity: 3341.4** (Blast Radius: 33.414 * Doc Risk: 100.0%)
- `pyqtgraph/__init__.py` -> **Severity: 1883.629** (Blast Radius: 40.812 * Doc Risk: 46.1538%)
- `pyqtgraph/Point.py` -> **Severity: 1252.4** (Blast Radius: 15.655 * Doc Risk: 80.0%)
- `pyqtgraph/graphicsItems/GraphicsObject.py` -> **Severity: 907.7** (Blast Radius: 9.077 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 268 literal sites + 12 sites through wrappers = 280
- **`panics_and_aborts`:** 431 literal sites + 3 sites through wrappers = 434

- `p` (function, debug_prints, primitive): 12 call sites in 1 files -- `tests/test_stability.py`
- `raiseException` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `pyqtgraph/examples/console_exception_inspection.py`
- `some_func2` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `pyqtgraph/examples/DataTreeWidget.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 18591 call pairs -- scoped 28.0%, unique 0.0%, ambiguous 19.4%, external 52.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 18590 | 28.0% | 0.0% | 19.4% | 52.6% |
| c | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
