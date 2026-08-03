# ARCHITECTURAL_BRIEF: pyqtgraph
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/pyqtgraph` |
| **Timestamp** | `2026-08-03T19:40:14.738124+00:00` |
| **Scan Duration** | `1.84s` |
| **Git Branch** | `master` |
| **Git Commit** | `d588dd3ec30915e61c8496a0fe1db21fc25e4da5` |
| **Git Remote** | `https://github.com/pyqtgraph/pyqtgraph.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 400 malicious artifacts.

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
| Total Artifacts | 795 |
| Analyzed Artifacts (Scanned) | 493 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 302 |
| Total LOC | 63030 |
| Volatility Index | 0.008 |
| % Scanned of codebase = | 62.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6818 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.353 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.862 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 29 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 396 | 45067 | 80.3% |
| CSV | 69 | 17664 | 14.0% |
| PLAINTEXT | 11 | 0 | 2.2% |
| XML | 9 | 0 | 1.8% |
| MARKDOWN | 3 | 0 | 0.6% |
| SHELL | 1 | 3 | 0.2% |
| MAKEFILE | 1 | 120 | 0.2% |
| BATCH | 1 | 119 | 0.2% |
| CSS | 1 | 17 | 0.2% |
| C | 1 | 40 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.627`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 284 | 57.6% |
| file_cluster_13 | 172 | 34.9% |
| file_cluster_0 | 14 | 2.8% |
| file_cluster_17 | 5 | 1.0% |
| file_cluster_1 | 2 | 0.4% |
| file_cluster_4 | 1 | 0.2% |
| file_cluster_9 | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 14 | 2.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 302*

**Composition by Extension & Reason:**
- `.rst`: 126x Excluded (Unsupported Extension: '.rst'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 90x Excluded (Explicitly Denied Extension: '.png')
- `.py`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 80 LOC), 1x Excluded (Machine-Generated Source Code Signature: 64 LOC)
- `.ui`: 9x Excluded (Unsupported Extension: '.ui'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dic`: 7x Excluded (Unsupported Extension: '.dic')
- `.ipynb`: 6x Excluded (Unsupported Extension: '.ipynb')
- `.cfg`: 3x Excluded (Unsupported Extension: '.cfg')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.graphml`: 2x Excluded (Unsupported Extension: '.graphml')
- `.svg`: 2x Excluded (Static Asset Blob without Intent: 1227 LOC)
- `.hex`: 2x Excluded (Unsupported Extension: '.hex')
- `.ini`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.ini')
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 79.1 | 14.7 | 7.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.5 | 18.0 | 8.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 11.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 23.8 | 2.3 | 0.0 |
| API Exposure | 0.0 | 13.1 | 3.6 | 3.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 29.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 89.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 18.8 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 93.1 | 4.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 37.8 | 16.7 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 42.8 | 4.5 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 36.2 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pyqtgraph/multiprocess/processes.py` (Hits: 39)
- `pyqtgraph/debug.py` (Hits: 23)
- `tests/image_testing.py` (Hits: 22)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **GLGraphicsItem.py** (`pyqtgraph/opengl/GLGraphicsItem.py`) — 25 inbound connections
2. **GraphicsObject.py** (`pyqtgraph/graphicsItems/GraphicsObject.py`) — 24 inbound connections
3. **Point.py** (`pyqtgraph/Point.py`) — 20 inbound connections
4. **basetypes.py** (`pyqtgraph/parametertree/parameterTypes/basetypes.py`) — 16 inbound connections
5. **Parameter.py** (`pyqtgraph/parametertree/Parameter.py`) — 14 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`pyqtgraph/__init__.py`) — 91 outbound dependencies
2. **__init__.py** (`pyqtgraph/Qt/__init__.py`) — 30 outbound dependencies
3. **debug.py** (`pyqtgraph/debug.py`) — 22 outbound dependencies
4. **PlotItem.py** (`pyqtgraph/graphicsItems/PlotItem/PlotItem.py`) — 22 outbound dependencies
5. **__init__.py** (`pyqtgraph/parametertree/parameterTypes/__init__.py`) — 20 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `setLeftButtonAction` (@ `pyqtgraph/graphicsItems/ViewBox/ViewBox.py`) -> Impact: **4713.1** | LOC: 1389
- `siScale` (@ `pyqtgraph/functions.py`) -> Impact: **1983.1** | LOC: 487
- `debugMsg` (@ `pyqtgraph/multiprocess/remoteproxy.py`) -> Impact: **1716.7** | LOC: 453
  * *Intent:* # corresponding code is in: # processes.py::Process.__init__() if pid is None: connection.send(os.getpid()) pid = connection.recv() RemoteEventHandler...
- `interpolateArray` (@ `pyqtgraph/functions.py`) -> Impact: **1672.6** | LOC: 447
- `labelString` (@ `pyqtgraph/graphicsItems/AxisItem.py`) -> Impact: **1413.1** | LOC: 860
- `setOpts` (@ `pyqtgraph/widgets/SpinBox.py`) -> Impact: **1355.9** | LOC: 445
- `writeCsv` (@ `pyqtgraph/graphicsItems/PlotItem/PlotItem.py`) -> Impact: **1219.8** | LOC: 390
- `dataBounds` (@ `pyqtgraph/graphicsItems/PlotCurveItem.py`) -> Impact: **1210.1** | LOC: 321
- `addDock` (@ `pyqtgraph/dockarea/DockArea.py`) -> Impact: **1148.8** | LOC: 342
  * *Intent:* """Adds a dock to this area. ============== ================================================================= **Arguments:** dock The new Dock object ...
- `__init__` (@ `pyqtgraph/graphicsItems/ColorBarItem.py`) -> Impact: **1054.4** | LOC: 135

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `mouseMoveEvent` (@ `pyqtgraph/GraphicsScene/GraphicsScene.py`) -> **O(2^N) [Recursive]**
- `mouseReleaseEvent` (@ `pyqtgraph/GraphicsScene/GraphicsScene.py`) -> **O(2^N) [Recursive]**
  * *Intent:* ## set focus on the topmost focusable item under this click
- `setConfigOption` (@ `pyqtgraph/__init__.py`) -> **O(2^N) [Recursive]**
- `parseString` (@ `pyqtgraph/configfile.py`) -> **O(2^N) [Recursive]**
- `_exportPlotDataItem` (@ `pyqtgraph/exporters/CSVExporter.py`) -> **O(2^N) [Recursive]**
- `export` (@ `pyqtgraph/exporters/HDF5Exporter.py`) -> **O(2^N) [Recursive]**
- `export` (@ `pyqtgraph/exporters/ImageExporter.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `pyqtgraph/graphicsItems/ColorBarItem.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `pyqtgraph/graphicsItems/HistogramLUTItem.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `pyqtgraph/graphicsItems/LegendItem.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `assertImageApproved` (@ `tests/image_testing.py`) -> DB Complexity: **79**
- `labelString` (@ `pyqtgraph/graphicsItems/AxisItem.py`) -> DB Complexity: **69**
- `setConfigOption` (@ `pyqtgraph/__init__.py`) -> DB Complexity: **65**
- `rectStr` (@ `pyqtgraph/graphicsItems/ROI.py`) -> DB Complexity: **56**
- `__init__` (@ `pyqtgraph/multiprocess/processes.py`) -> DB Complexity: **50**
- `debugMsg` (@ `pyqtgraph/multiprocess/remoteproxy.py`) -> DB Complexity: **44**
  * *Intent:* # corresponding code is in: # processes.py::Process.__init__() if pid is None: connection.send(os.getpid()) pid = connection.recv() RemoteEventHandler...
- `setLeftButtonAction` (@ `pyqtgraph/graphicsItems/ViewBox/ViewBox.py`) -> DB Complexity: **39**
- `__init__` (@ `pyqtgraph/console/repl_widget.py`) -> DB Complexity: **34**
- `getVersionStrings` (@ `tools/setupHelpers.py`) -> DB Complexity: **33**
- `transmissionCurve` (@ `pyqtgraph/examples/optics/pyoptic.py`) -> DB Complexity: **30**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `pyqtgraph/graphicsItems` | 38 | 22846.22 | 32.61% | 25.04% |
| `pyqtgraph` | 20 | 12916.76 | 20.41% | 27.58% |
| `pyqtgraph/widgets` | 32 | 9243.04 | 31.99% | 27.14% |
| `pyqtgraph/graphicsItems/ViewBox` | 3 | 5762.46 | 24.66% | 17.37% |
| `pyqtgraph/multiprocess` | 5 | 3613.12 | 36.49% | 49.84% |
| `pyqtgraph/examples` | 108 | 3152.58 | 11.07% | 0.0% |
| `pyqtgraph/parametertree/parameterTypes` | 20 | 2731.9 | 14.41% | 33.9% |
| `pyqtgraph/parametertree` | 5 | 2549.58 | 17.47% | 26.55% |
| `pyqtgraph/flowchart` | 4 | 2523.92 | 36.72% | 52.75% |
| `pyqtgraph/dockarea` | 5 | 2516.86 | 34.78% | 59.63% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `benchmarks/arrayToQPath.py` -> **100.0%** Exposure
- `pyqtgraph/PlotData.py` -> **100.0%** Exposure
- `pyqtgraph/Qt/OpenGLHelpers.py` -> **100.0%** Exposure
- `pyqtgraph/dockarea/Container.py` -> **100.0%** Exposure
- `pyqtgraph/flowchart/FlowchartGraphicsView.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `benchmarks/arrayToQPath.py` -> **100.0%** Exposure
- `pyqtgraph/GraphicsScene/mouseEvents.py` -> **100.0%** Exposure
- `pyqtgraph/SignalProxy.py` -> **100.0%** Exposure
- `pyqtgraph/dockarea/Dock.py` -> **100.0%** Exposure
- `pyqtgraph/dockarea/DockDrop.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pyqtgraph/graphicsItems/ROI.py` -> **0** Orphaned Functions | **55** Duplicates
- `pyqtgraph/dockarea/Container.py` -> **0** Orphaned Functions | **22** Duplicates
- `tests/parametertree/test_Parameter.py` -> **22** Orphaned Functions | **0** Duplicates
- `pyqtgraph/widgets/RemoteGraphicsView.py` -> **0** Orphaned Functions | **20** Duplicates
- `pyqtgraph/debug.py` -> **0** Orphaned Functions | **17** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`pyqtgraph/exporters/SVGExporter.py`** -> AI Confidence: **99.34%**
2. **`pyqtgraph/graphicsItems/AxisItem.py`** -> AI Confidence: **99.34%**
3. **`pyqtgraph/GraphicsScene/GraphicsScene.py`** -> AI Confidence: **99.31%**
4. **`pyqtgraph/colormap.py`** -> AI Confidence: **99.31%**
5. **`pyqtgraph/configfile.py`** -> AI Confidence: **99.31%**
6. **`pyqtgraph/console/exception_widget.py`** -> AI Confidence: **99.31%**
7. **`pyqtgraph/debug.py`** -> AI Confidence: **99.31%**
8. **`pyqtgraph/examples/test_examples.py`** -> AI Confidence: **99.31%**
9. **`pyqtgraph/exporters/CSVExporter.py`** -> AI Confidence: **99.31%**
10. **`pyqtgraph/flowchart/Flowchart.py`** -> AI Confidence: **99.31%**
11. **`pyqtgraph/functions.py`** -> AI Confidence: **99.31%**
12. **`pyqtgraph/graphicsItems/ColorBarItem.py`** -> AI Confidence: **99.31%**
13. **`pyqtgraph/graphicsItems/HistogramLUTItem.py`** -> AI Confidence: **99.31%**
14. **`pyqtgraph/graphicsItems/ImageItem.py`** -> AI Confidence: **99.31%**
15. **`pyqtgraph/graphicsItems/InfiniteLine.py`** -> AI Confidence: **99.31%**
16. **`pyqtgraph/graphicsItems/PlotCurveItem.py`** -> AI Confidence: **99.31%**
17. **`pyqtgraph/graphicsItems/PlotDataItem.py`** -> AI Confidence: **99.31%**
18. **`pyqtgraph/graphicsItems/PlotItem/PlotItem.py`** -> AI Confidence: **99.31%**
19. **`pyqtgraph/graphicsItems/ROI.py`** -> AI Confidence: **99.31%**
20. **`pyqtgraph/graphicsItems/ScatterPlotItem.py`** -> AI Confidence: **99.31%**
21. **`pyqtgraph/graphicsItems/ViewBox/ViewBox.py`** -> AI Confidence: **99.31%**
22. **`pyqtgraph/imageview/ImageView.py`** -> AI Confidence: **99.31%**
23. **`pyqtgraph/multiprocess/parallelizer.py`** -> AI Confidence: **99.31%**
24. **`pyqtgraph/multiprocess/processes.py`** -> AI Confidence: **99.31%**
25. **`pyqtgraph/opengl/GLViewWidget.py`** -> AI Confidence: **99.31%**
26. **`pyqtgraph/opengl/items/GLLinePlotItem.py`** -> AI Confidence: **99.31%**
27. **`pyqtgraph/opengl/items/GLMeshItem.py`** -> AI Confidence: **99.31%**
28. **`pyqtgraph/opengl/items/GLScatterPlotItem.py`** -> AI Confidence: **99.31%**
29. **`pyqtgraph/parametertree/interactive.py`** -> AI Confidence: **99.31%**
30. **`pyqtgraph/reload.py`** -> AI Confidence: **99.31%**
31. **`pyqtgraph/widgets/ScatterPlotWidget.py`** -> AI Confidence: **99.31%**
32. **`pyqtgraph/widgets/SpinBox.py`** -> AI Confidence: **99.31%**
33. **`tests/image_testing.py`** -> AI Confidence: **99.31%**
34. **`tools/setupHelpers.py`** -> AI Confidence: **99.31%**
35. **`doc/listmissing.py`** -> AI Confidence: **99.29%**
36. **`pyqtgraph/examples/verlet_chain/relax.c`** -> AI Confidence: **99.29%**
37. **`pyqtgraph/console/repl_widget.py`** -> AI Confidence: **99.24%**
38. **`pyqtgraph/examples/ExampleApp.py`** -> AI Confidence: **99.24%**
39. **`pyqtgraph/graphicsItems/GradientEditorItem.py`** -> AI Confidence: **99.24%**
40. **`pyqtgraph/graphicsItems/LegendItem.py`** -> AI Confidence: **99.24%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `benchmarks/arrayToQPath.py` -> **100.0%** Exposure
- `benchmarks/renderImageItem.py` -> **100.0%** Exposure
- `pyqtgraph/GraphicsScene/GraphicsScene.py` -> **100.0%** Exposure
- `pyqtgraph/GraphicsScene/exportDialog.py` -> **100.0%** Exposure
- `pyqtgraph/GraphicsScene/mouseEvents.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `pyqtgraph/console/Console.py` -> **100.0%** Exposure
- `pyqtgraph/examples/ExampleApp.py` -> **100.0%** Exposure
- `pyqtgraph/examples/hdf5.py` -> **100.0%** Exposure
- `pyqtgraph/examples/test_examples.py` -> **100.0%** Exposure
- `pyqtgraph/multiprocess/bootstrap.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `benchmarks/arrayToQPath.py` -> **100.0%** Exposure
- `benchmarks/renderImageItem.py` -> **100.0%** Exposure
- `pyqtgraph/GraphicsScene/GraphicsScene.py` -> **100.0%** Exposure
- `pyqtgraph/GraphicsScene/exportDialog.py` -> **100.0%** Exposure
- `pyqtgraph/GraphicsScene/mouseEvents.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1104` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `pyqtgraph/multiprocess/parallelizer.py` (PYTHON) -> Cumulative Risk: **930.42**
- **Archetype:** `file_cluster_17` (Distance: 19.854 IQR)
- **Magnitude:** 564.76 | **LOC:** 342 | **CtrlFlow:** 61.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `runParallel` (Impact: 186.3), `__exit__` (Impact: 104.8), `suggestedWorkerCount` (Impact: 61.7)

### 2. `pyqtgraph/debug.py` (PYTHON) -> Cumulative Risk: **899.5**
- **Archetype:** `file_cluster_13` (Distance: 14.117 IQR)
- **Magnitude:** 2114.42 | **LOC:** 1296 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `typeStr` (Impact: 264.3), `printTrace` (Impact: 259.2), `refPathString` (Impact: 236.0)

### 3. `pyqtgraph/exceptionHandling.py` (PYTHON) -> Cumulative Risk: **890.22**
- **Archetype:** `file_cluster_4` (Distance: 12.445 IQR)
- **Magnitude:** 135.56 | **LOC:** 157 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_excepthook` (Impact: 68.6), `implements` (Impact: 10.7), `__init__` (Impact: 2.8)

### 4. `pyqtgraph/multiprocess/processes.py` (PYTHON) -> Cumulative Risk: **883.03**
- **Archetype:** `file_cluster_13` (Distance: 12.536 IQR)
- **Magnitude:** 689.04 | **LOC:** 533 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 422.8), `join` (Impact: 126.4)

### 5. `pyqtgraph/Qt/OpenGLHelpers.py` (PYTHON) -> Cumulative Risk: **851.63**
- **Archetype:** `file_cluster_13` (Distance: 10.924 IQR)
- **Magnitude:** 129.36 | **LOC:** 96 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `getFunctions` (Impact: 62.8), `getFunctions` (Impact: 14.1), `storeProgram` (Impact: 8.2)

### 6. `pyqtgraph/Qt/internals.py` (PYTHON) -> Cumulative Risk: **819.51**
- **Archetype:** `file_cluster_13` (Distance: 11.536 IQR)
- **Magnitude:** 307.72 | **LOC:** 249 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 70.1), `resize` (Impact: 53.5), `instances` (Impact: 31.4)

### 7. `pyqtgraph/widgets/ColorMapButton.py` (PYTHON) -> Cumulative Risk: **803.38**
- **Archetype:** `file_cluster_13` (Distance: 11.205 IQR)
- **Magnitude:** 147.32 | **LOC:** 121 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getImage` (Impact: 35.3), `_setColorMap` (Impact: 17.9), `paintColorMap` (Impact: 17.4)

### 8. `pyqtgraph/dockarea/DockDrop.py` (PYTHON) -> Cumulative Risk: **803.16**
- **Archetype:** `file_cluster_8` (Distance: 12.283 IQR)
- **Magnitude:** 239.68 | **LOC:** 140 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `dragMoveEvent` (Impact: 64.4), `setDropArea` (Impact: 35.9), `dragEnterEvent` (Impact: 14.3)

### 9. `pyqtgraph/multiprocess/remoteproxy.py` (PYTHON) -> Cumulative Risk: **789.49**
- **Archetype:** `file_cluster_13` (Distance: 12.893 IQR)
- **Magnitude:** 2314.22 | **LOC:** 1143 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `debugMsg` (Impact: 1716.7), `unpickleObjectProxy` (Impact: 37.3), `_setProxyOptions` (Impact: 27.4)

### 10. `pyqtgraph/widgets/VerticalLabel.py` (PYTHON) -> Cumulative Risk: **788.01**
- **Archetype:** `file_cluster_17` (Distance: 19.307 IQR)
- **Magnitude:** 121.28 | **LOC:** 83 | **CtrlFlow:** 55.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `paintEvent` (Impact: 45.1), `sizeHint` (Impact: 30.9), `setOrientation` (Impact: 7.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pyqtgraph/graphicsItems/ViewBox/ViewBox.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.534 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.475 IQR)
- **Top Global Matches:** file_cluster_13: 12.534, file_cluster_0: 12.596, file_cluster_8: 12.64
- **Magnitude:** 5424.38 | **LOC:** 1876 | **CtrlFlow:** 65.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (33.1876%), Tech Debt (52.1009%)
**Top Internal Functions/Classes:**
  * `setLeftButtonAction` (Impact: 4713.1 | O(2^N) | DB: 39)
  * `__init__` (Impact: 104.6 | O(2^N) | DB: 22)
    * *Intent:* ## mouse modes
  * `itemChange` (Impact: 70.5 | O(2^N))
  * `itemChange` (Impact: 60.8 | O(2^N))
  * `getState` (Impact: 35.5 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 426`, `structural_boundaries: 221`, `args: 107`, `func_start: 107`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 157`, `dead_code: 11`, `fragile_debt: 2`, `duplicate_logic: 7`
* *Architecture:* `io: 1`, `api: 108`, `import: 13`
* *Defense:* `safety: 33`, `doc: 100`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.332
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` sys, math, ..GraphicsWidget, .ViewBoxMenu, ..ItemGroup, copy, ...Point, numpy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyqtgraph/functions.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.224 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.227 IQR)
- **Top Global Matches:** file_cluster_8: 12.224, file_cluster_13: 12.373, file_cluster_17: 12.458
- **Magnitude:** 5388.34 | **LOC:** 3190 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (12.5779%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `siScale` (Impact: 1983.1 | O(2^N) | DB: 4)
  * `interpolateArray` (Impact: 1672.6 | O(2^N) | DB: 6)
  * `isocurve` (Impact: 325.4 | O(N^6) | DB: 8)
  * `isosurface` (Impact: 158.7 | O(2^N) | DB: 2)
  * `_pseudoScatterExact` (Impact: 151.9 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 482`, `structural_boundaries: 232`, `args: 65`, `func_start: 64`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 70`, `dead_code: 22`
* *Architecture:* `io: 2`, `api: 57`, `import: 15`
* *Defense:* `safety: 57`, `doc: 110`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.353
  * `Choke Point (Betweenness):` 0.000232 | `Ripple Effect (Closeness):` 0.026205
  * `Imports (Out-Degree: 2):` .util.cupy_helper, collections, sys, re, math, .Qt, numpy.linalg, struct...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/ROI.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.138 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.558 IQR)
- **Top Global Matches:** file_cluster_8: 12.138, file_cluster_7: 12.297, file_cluster_13: 12.35
- **Magnitude:** 2940.92 | **LOC:** 2385 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 56
- **Risk Profile:** Cognitive Load (33.8811%), Tech Debt (99.9998%)
**Top Internal Functions/Classes:**
  * `rectStr` (Impact: 992.3 | O(N^5) | DB: 56)
  * `getArrayRegion` (Impact: 241.6 | O(2^N))
  * `mouseDragEvent` (Impact: 148.2 | O(N^6) | DB: 11)
  * `getArrayRegion` (Impact: 74.6 | O(2^N) | DB: 1)
  * `movePoint` (Impact: 56.4 | O(2^N))
    * *Intent:* ## Determine transform that maps ROI bounding box to image coordinates
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 321`, `structural_boundaries: 308`, `args: 151`, `func_start: 150`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 285`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 3`, `duplicate_logic: 55`
* *Architecture:* `io: 1`, `api: 144`, `import: 9`
* *Defense:* `safety: 11`, `doc: 108`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.574
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.004065
  * `Imports (Out-Degree: 4):` sys, math, ..Qt, ..Point, .., numpy.linalg, .GraphicsObject, ..SRTTransform...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/PlotCurveItem.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.511 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.673 IQR)
- **Top Global Matches:** file_cluster_13: 12.511, file_cluster_8: 12.59, file_cluster_0: 12.654
- **Magnitude:** 2379.86 | **LOC:** 1294 | **CtrlFlow:** 68.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (38.2066%), Tech Debt (37.3038%)
**Top Internal Functions/Classes:**
  * `dataBounds` (Impact: 1210.1 | O(2^N) | DB: 17)
  * `paintGL` (Impact: 313.8 | O(N^6) | DB: 1)
    * *Intent:* # note that left/right vertical lines can be omitted here
  * `paint` (Impact: 211.9 | O(N^5) | DB: 1)
  * `arrayToLineSegments` (Impact: 112.1 | O(N^3))
  * `_getFillPathList` (Impact: 50.5 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 113`, `args: 42`, `func_start: 42`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 123`, `dead_code: 12`, `fragile_debt: 2`, `duplicate_logic: 3`
* *Architecture:* `api: 39`, `import: 12`
* *Defense:* `safety: 19`, `doc: 34`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.069
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.01626
  * `Imports (Out-Degree: 1):` ..Qt, math, .., .GraphicsObject, importlib, warnings, numpy
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/PlotItem/PlotItem.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.79 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.72 IQR)
- **Top Global Matches:** file_cluster_13: 11.79, file_cluster_8: 11.948, file_cluster_0: 11.996
- **Magnitude:** 2366.72 | **LOC:** 1646 | **CtrlFlow:** 56.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (27.2777%), Tech Debt (8.4793%)
**Top Internal Functions/Classes:**
  * `writeCsv` (Impact: 1219.8 | O(2^N) | DB: 11)
  * `multiDataPlot` (Impact: 187.3 | O(N^6) | DB: 2)
  * `addItem` (Impact: 136.5 | O(2^N) | DB: 3)
  * `setAxisItems` (Impact: 93.7 | O(N^6) | DB: 1)
  * `addAvgCurve` (Impact: 85.8 | O(N^5) | DB: 2)
    * *Intent:* # Set up new axis
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 177`, `args: 77`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 118`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 87`, `import: 24`
* *Defense:* `safety: 14`, `doc: 76`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.138
  * `Choke Point (Betweenness):` 0.000228 | `Ripple Effect (Closeness):` 0.010163
  * `Imports (Out-Degree: 9):` ...WidgetGroup, ..ViewBox, numpy, weakref, typing, ..LabelItem, ..InfiniteLine, collections.abc...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `pyqtgraph/multiprocess/remoteproxy.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.893 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.736 IQR)
- **Top Global Matches:** file_cluster_13: 12.893, file_cluster_4: 12.947, file_cluster_0: 13.064
- **Magnitude:** 2314.22 | **LOC:** 1143 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 44
- **Risk Profile:** Cognitive Load (45.6147%), Tech Debt (33.3417%)
**Top Internal Functions/Classes:**
  * `debugMsg` (Impact: 1716.7 | O(2^N) | DB: 44)
    * *Intent:* # corresponding code is in: # processes.py::Process.__init__() if pid is None: connection.send(os.ge...
  * `unpickleObjectProxy` (Impact: 37.3 | O(N^4) | DB: 3)
  * `_setProxyOptions` (Impact: 27.4 | O(N^4) | DB: 1)
  * `__getattr__` (Impact: 25.6 | O(N^4) | DB: 1)
  * `__call__` (Impact: 15.4 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 230`, `args: 93`, `func_start: 93`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 74`, `dead_code: 6`, `duplicate_logic: 4`
* *Architecture:* `io: 11`, `api: 36`, `concurrency: 34`, `import: 13`
* *Defense:* `safety: 38`, `doc: 44`, `test: 2`, `sync_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.506
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006098
  * `Imports (Out-Degree: 0):` traceback, sys, new, from, threading, os, a, builtins...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pyqtgraph/debug.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.117 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.962 IQR)
- **Top Global Matches:** file_cluster_13: 14.117, file_cluster_17: 14.155, file_cluster_0: 14.261
- **Magnitude:** 2114.42 | **LOC:** 1296 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (38.6069%), Tech Debt (92.9743%)
**Top Internal Functions/Classes:**
  * `typeStr` (Impact: 264.3 | O(2^N) | DB: 15)
  * `printTrace` (Impact: 259.2 | O(N^5) | DB: 6)
    * *Intent:* # print(" "*indent + prefix + '='*30 + '>>') # print(" "*indent + prefix + '='*30 + '<<') def printT...
  * `refPathString` (Impact: 236.0 | O(N^5) | DB: 6)
  * `collect` (Impact: 177.4 | O(2^N) | DB: 4)
    * *Intent:* #print "deleted:", len(delRefs)
  * `listQThreads` (Impact: 143.8 | O(N^6) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 235`, `args: 82`, `func_start: 80`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 132`, `dead_code: 15`, `duplicate_logic: 17`
* *Architecture:* `io: 23`, `api: 81`, `concurrency: 11`, `import: 23`
* *Defense:* `safety: 70`, `doc: 84`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.225
  * `Choke Point (Betweenness):` 9.5e-05 | `Ripple Effect (Closeness):` 0.021082
  * `Imports (Out-Degree: 1):` types, traceback, re, .Qt, .util.mutex, threading, contextlib, numpy...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/AxisItem.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.419 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.934 IQR)
- **Top Global Matches:** file_cluster_8: 12.419, file_cluster_13: 12.576, file_cluster_7: 12.597
- **Magnitude:** 1950.14 | **LOC:** 1780 | **CtrlFlow:** 69.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 69
- **Risk Profile:** Cognitive Load (46.9941%), Tech Debt (9.3363%)
**Top Internal Functions/Classes:**
  * `labelString` (Impact: 1413.1 | O(N^6) | DB: 69)
  * `setStyle` (Impact: 80.6 | O(N^6) | DB: 2)
  * `resizeEvent` (Impact: 22.0 | O(N^3) | DB: 6)
  * `showLabel` (Impact: 14.4 | O(N^3))
  * `getSIPrefixEnableRanges` (Impact: 14.3 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 120`, `args: 52`, `func_start: 52`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 298`, `fragile_debt: 1`
* *Architecture:* `api: 51`, `import: 9`
* *Defense:* `safety: 9`, `doc: 68`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.293
  * `Choke Point (Betweenness):` 2.7e-05 | `Ripple Effect (Closeness):` 0.012703
  * `Imports (Out-Degree: 2):` math, ..Qt, ..Point, .., .GraphicsWidget, numpy, weakref
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pyqtgraph/Qt/__init__.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.84 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.745 IQR)
- **Top Global Matches:** file_cluster_13: 10.84, file_cluster_8: 11.091, file_cluster_7: 11.635
- **Magnitude:** 1944.29 | **LOC:** 399 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (17.7343%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 92`, `args: 11`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`
* *Architecture:* `io: 10`, `api: 5`, `import: 41`
* *Defense:* `safety: 35`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.332
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` shiboken6, sip, PySide2.QtGui, PySide2.QtWidgets, sys, platform, PyQt5.QtGui, importlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyqtgraph/graphicsItems/ScatterPlotItem.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.912 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.222 IQR)
- **Top Global Matches:** file_cluster_8: 11.912, file_cluster_13: 11.927, file_cluster_7: 12.06
- **Magnitude:** 1910.6 | **LOC:** 1242 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (28.536%), Tech Debt (86.4023%)
**Top Internal Functions/Classes:**
  * `setPointData` (Impact: 414.5 | O(N^6) | DB: 7)
  * `addPoints` (Impact: 336.8 | O(N^6) | DB: 10)
  * `paint` (Impact: 113.5 | O(N^6) | DB: 3)
  * `setSize` (Impact: 106.2 | O(N^4) | DB: 1)
  * `setBrush` (Impact: 92.0 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 144`, `args: 76`, `func_start: 75`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 120`, `dead_code: 3`, `fragile_debt: 1`, `duplicate_logic: 9`
* *Architecture:* `api: 69`, `import: 11`
* *Defense:* `safety: 37`, `doc: 60`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.255
  * `Choke Point (Betweenness):` 2.7e-05 | `Ripple Effect (Closeness):` 0.014935
  * `Imports (Out-Degree: 2):` collections, math, ..Qt, ..Point, .., .GraphicsObject, numpy, itertools...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `pyqtgraph/widgets/SpinBox.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.709 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.136 IQR)
- **Top Global Matches:** file_cluster_13: 12.709, file_cluster_0: 12.875, file_cluster_8: 13.04
- **Magnitude:** 1459.38 | **LOC:** 656 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (14.2612%), Tech Debt (17.4871%)
**Top Internal Functions/Classes:**
  * `setOpts` (Impact: 1355.9 | O(2^N) | DB: 22)
  * `__init__` (Impact: 21.1 | O(2^N) | DB: 10)
    * *Intent:* **Signals:**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 84`, `args: 37`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 40`, `dead_code: 6`, `fragile_debt: 2`
* *Architecture:* `io: 4`, `api: 35`, `import: 9`
* *Defense:* `safety: 14`, `doc: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.347
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002033
  * `Imports (Out-Degree: 1):` re, sys, math, ..Qt, .., decimal, warnings, ..SignalProxy
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/flowchart/Flowchart.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.407 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.893 IQR)
- **Top Global Matches:** file_cluster_13: 12.407, file_cluster_8: 12.621, file_cluster_0: 12.718
- **Magnitude:** 1413.76 | **LOC:** 926 | **CtrlFlow:** 47.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (24.8478%), Tech Debt (37.8992%)
**Top Internal Functions/Classes:**
  * `createNode` (Impact: 289.2 | O(N^6))
  * `setCurrentFile` (Impact: 119.8 | O(N^5) | DB: 23)
  * `restoreState` (Impact: 109.9 | O(2^N) | DB: 1)
  * `nodeOutputChanged` (Impact: 81.1 | O(N^6) | DB: 5)
  * `processOrder` (Impact: 81.0 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 157`, `args: 71`, `func_start: 69`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 104`, `dead_code: 5`, `duplicate_logic: 5`
* *Architecture:* `api: 76`, `import: 16`
* *Defense:* `safety: 39`, `doc: 38`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.332
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` collections, ..Qt, .library, .., ..debug, ..graphicsItems.GraphicsObject, os, .Terminal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyqtgraph/graphicsItems/ColorBarItem.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.408 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.284 IQR)
- **Top Global Matches:** file_cluster_13: 12.408, file_cluster_8: 12.559, file_cluster_7: 12.76
- **Magnitude:** 1367.16 | **LOC:** 369 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (40.4692%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 1054.4 | O(2^N) | DB: 25)
  * `_regionChanging` (Impact: 74.8 | O(N^5) | DB: 1)
  * `setLevels` (Impact: 54.9 | O(N^3) | DB: 2)
  * `_update_items` (Impact: 39.8 | O(N^4))
  * `mouseClickEvent` (Impact: 17.9 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 34`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 89`
* *Architecture:* `api: 9`, `import: 9`
* *Defense:* `safety: 9`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.347
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002033
  * `Imports (Out-Degree: 3):` ..Qt, math, .PlotItem, .., ..widgets.ColorMapMenu, numpy, weakref, .LinearRegionItem
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/ImageItem.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.538 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.862 IQR)
- **Top Global Matches:** file_cluster_13: 12.538, file_cluster_8: 12.754, file_cluster_16: 12.839
- **Magnitude:** 1312.48 | **LOC:** 1227 | **CtrlFlow:** 58.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (38.733%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 172.2 | O(N^5) | DB: 21)
    * *Intent:* * `border`, whose value is directed to :meth:`setBorder` * `colorMap`, whose value is directed to :m...
  * `setImage` (Impact: 138.2 | O(N^4) | DB: 8)
  * `setOpts` (Impact: 81.8 | O(N^4) | DB: 4)
    * *Intent:* ----------
  * `drawAt` (Impact: 68.2 | O(N^5) | DB: 3)
  * `paint` (Impact: 41.1 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 131`, `args: 49`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 236`, `dead_code: 2`
* *Architecture:* `io: 4`, `api: 65`, `import: 15`
* *Defense:* `safety: 10`, `doc: 48`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.347
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002033
  * `Imports (Out-Degree: 3):` pathlib, numpy.typing, ..Qt, ..Point, .., .GraphicsObject, os, ..util.cupy_helper...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/dockarea/DockArea.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.68 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.803 IQR)
- **Top Global Matches:** file_cluster_13: 11.68, file_cluster_8: 11.713, file_cluster_7: 11.963
- **Magnitude:** 1251.28 | **LOC:** 397 | **CtrlFlow:** 55.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (30.6818%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addDock` (Impact: 1148.8 | O(2^N) | DB: 19)
    * *Intent:* """Adds a dock to this area. ============== ========================================================...
  * `__init__` (Impact: 7.5 | O(2^N) | DB: 7)
  * `type` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 61`, `args: 28`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 60`, `dead_code: 1`
* *Architecture:* `api: 27`, `import: 5`
* *Defense:* `safety: 7`, `doc: 12`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.993
  * `Choke Point (Betweenness):` 3.1e-05 | `Ripple Effect (Closeness):` 0.007259
  * `Imports (Out-Degree: 3):` ..Qt, .Dock, .DockDrop, weakref, .Container
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/PlotDataItem.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.264 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.169 IQR)
- **Top Global Matches:** file_cluster_13: 12.264, file_cluster_0: 12.345, file_cluster_8: 12.44
- **Magnitude:** 1251.28 | **LOC:** 1890 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (29.7832%), Tech Debt (23.1102%)
**Top Internal Functions/Classes:**
  * `_getDisplayDataset` (Impact: 361.8 | O(N^6) | DB: 4)
  * `dataType` (Impact: 111.2 | O(N^5))
  * `updateItems` (Impact: 108.4 | O(N^5))
  * `viewRangeChanged` (Impact: 51.4 | O(N^4) | DB: 1)
  * `applyLogMapping` (Impact: 46.3 | O(N^4) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 126`, `args: 52`, `func_start: 52`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 121`, `dead_code: 8`, `duplicate_logic: 4`
* *Architecture:* `api: 77`, `import: 12`
* *Defense:* `safety: 18`, `doc: 72`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.628
  * `Choke Point (Betweenness):` 3.2e-05 | `Ripple Effect (Closeness):` 0.01084
  * `Imports (Out-Degree: 3):` math, ..Qt, .., .GraphicsObject, warnings, numpy, .PlotCurveItem, .ScatterPlotItem...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pyqtgraph/parametertree/Parameter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.076 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.57 IQR)
- **Top Global Matches:** file_cluster_0: 13.076, file_cluster_13: 13.133, file_cluster_11: 13.43
- **Magnitude:** 1247.26 | **LOC:** 879 | **CtrlFlow:** 40.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (28.8489%), Tech Debt (21.886%)
**Top Internal Functions/Classes:**
  * `restoreState` (Impact: 318.2 | O(2^N) | DB: 2)
  * `insertChild` (Impact: 94.1 | O(N^4) | DB: 3)
    * *Intent:* """ return not self.readonly() def setWritable(self, writable=True): """Set whether this Parameter s...
  * `saveState` (Impact: 78.9 | O(2^N) | DB: 1)
  * `remove` (Impact: 61.8 | O(2^N))
  * `setName` (Impact: 48.3 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 158`, `args: 73`, `func_start: 73`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 73`, `dead_code: 5`, `duplicate_logic: 2`
* *Architecture:* `api: 73`, `import: 7`
* *Defense:* `safety: 24`, `doc: 102`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.856
  * `Choke Point (Betweenness):` 8.6e-05 | `Ripple Effect (Closeness):` 0.0371
  * `Imports (Out-Degree: 1):` collections, re, ..Qt, .., .ParameterItem, warnings, weakref
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/InfiniteLine.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.997 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.239 IQR)
- **Top Global Matches:** file_cluster_13: 12.997, file_cluster_8: 13.244, file_cluster_7: 13.373
- **Magnitude:** 1164.38 | **LOC:** 622 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (37.2917%), Tech Debt (99.6118%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 210.4 | O(2^N) | DB: 15)
    * *Intent:* **Signals:**
  * `setPos` (Impact: 140.1 | O(2^N) | DB: 5)
  * `__init__` (Impact: 137.1 | O(2^N) | DB: 7)
  * `setHoverPen` (Impact: 49.8 | O(N^6) | DB: 3)
  * `addMarker` (Impact: 41.9 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 84`, `args: 40`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 184`, `dead_code: 3`, `duplicate_logic: 12`
* *Architecture:* `api: 47`, `import: 9`
* *Defense:* `safety: 5`, `doc: 34`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.347
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002033
  * `Imports (Out-Degree: 3):` .GraphicsItem, ..Qt, math, ..Point, .., .GraphicsObject, .TextItem, .ViewBox...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/GradientEditorItem.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 15.602 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.418 IQR)
- **Top Global Matches:** file_cluster_0: 15.602, file_cluster_13: 15.687, file_cluster_11: 15.743
- **Magnitude:** 1125.84 | **LOC:** 981 | **CtrlFlow:** 46.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (35.4143%), Tech Debt (83.3875%)
**Top Internal Functions/Classes:**
  * `setOrientation` (Impact: 370.4 | O(2^N) | DB: 19)
  * `getColor` (Impact: 92.5 | O(N^4) | DB: 2)
  * `__init__` (Impact: 34.9 | O(2^N) | DB: 9)
  * `__init__` (Impact: 34.0 | O(2^N) | DB: 4)
  * `getGradient` (Impact: 32.2 | O(N^5) | DB: 5)
    * *Intent:* ## public if cm not in ['rgb', 'hsv']: raise Exception("Unknown color mode %s. Options are 'rgb' and...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 123`, `args: 63`, `func_start: 62`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 140`, `dead_code: 23`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `io: 1`, `api: 66`, `import: 10`
* *Defense:* `safety: 3`, `doc: 50`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.072
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.008469
  * `Imports (Out-Degree: 3):` ..Qt, ..widgets.ColorMapMenu, .., .GraphicsWidget, operator, numpy, ..widgets.SpinBox, .GradientPresets...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pyqtgraph/GraphicsScene/GraphicsScene.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.138 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.968 IQR)
- **Top Global Matches:** file_cluster_13: 13.138, file_cluster_0: 13.282, file_cluster_17: 13.308
- **Magnitude:** 1077.92 | **LOC:** 545 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (38.288%), Tech Debt (14.8715%)
**Top Internal Functions/Classes:**
  * `mouseMoveEvent` (Impact: 208.0 | O(2^N) | DB: 2)
  * `mouseReleaseEvent` (Impact: 159.2 | O(2^N) | DB: 6)
    * *Intent:* ## set focus on the topmost focusable item under this click
  * `sendDragEvent` (Impact: 143.3 | O(N^6) | DB: 3)
  * `sendClickEvent` (Impact: 98.7 | O(N^6))
  * `sendHoverEvents` (Impact: 98.6 | O(N^5) | DB: 2)
    * *Intent:* ## keep track of which buttons are involved in dragging
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 70`, `args: 22`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 76`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 25`, `import: 9`
* *Defense:* `safety: 27`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.332
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ..Qt, ..Point, .., .mouseEvents, warnings, time, , weakref
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyqtgraph/exporters/SVGExporter.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.888 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.687 IQR)
- **Top Global Matches:** file_cluster_8: 10.888, file_cluster_13: 10.99, file_cluster_17: 11.066
- **Magnitude:** 1071.36 | **LOC:** 538 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (26.4749%), Tech Debt (9.826%)
**Top Internal Functions/Classes:**
  * `correctCoordinates` (Impact: 541.9 | O(N^6) | DB: 7)
    * *Intent:* ## Get top-level group for this item g1 = doc.getElementsByTagName('g')[0] defs = doc.getElementsByT...
  * `generateSvg` (Impact: 363.5 | O(2^N) | DB: 3)
  * `__init__` (Impact: 54.2 | O(2^N) | DB: 1)
  * `export` (Impact: 51.4 | O(N^4) | DB: 3)
  * `widthChanged` (Impact: 2.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 51`, `args: 12`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 33`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 12`, `import: 9`
* *Defense:* `safety: 25`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.52
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.002033
  * `Imports (Out-Degree: 2):` re, ..Qt, .Exporter, .., ..parametertree, contextlib, numpy, xml.dom.minidom
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/flowchart/Terminal.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.98 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.194 IQR)
- **Top Global Matches:** file_cluster_8: 11.98, file_cluster_13: 12.089, file_cluster_7: 12.233
- **Magnitude:** 1059.66 | **LOC:** 584 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (48.036%), Tech Debt (73.0837%)
**Top Internal Functions/Classes:**
  * `connectTo` (Impact: 147.8 | O(N^5) | DB: 1)
  * `generatePath` (Impact: 103.4 | O(N^4) | DB: 6)
  * `mouseDragEvent` (Impact: 74.5 | O(N^6) | DB: 3)
  * `disconnected` (Impact: 43.8 | O(2^N) | DB: 1)
  * `setValue` (Impact: 40.9 | O(N^4) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 130`, `args: 72`, `func_start: 72`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 127`, `dead_code: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 80`, `import: 5`
* *Defense:* `safety: 8`, `doc: 22`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.709
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.002033
  * `Imports (Out-Degree: 2):` ..Qt, ..Point, .., ..graphicsItems.GraphicsObject, weakref
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/widgets/TableWidget.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.707 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.539 IQR)
- **Top Global Matches:** file_cluster_0: 12.707, file_cluster_13: 12.876, file_cluster_8: 12.973
- **Magnitude:** 973.2 | **LOC:** 477 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (34.6735%), Tech Debt (33.254%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 426.4 | O(2^N) | DB: 19)
    * *Intent:* """ def __init__(self, *args, **kwds): """
  * `serialize` (Impact: 74.7 | O(N^6) | DB: 7)
  * `__init__` (Impact: 37.1 | O(2^N) | DB: 6)
    * *Intent:* """Copy all data to clipboard."""
  * `iteratorFn` (Impact: 32.0 | O(N^3))
  * `setSortMode` (Impact: 30.4 | O(2^N))
    * *Intent:* # for numpy.void, which can be iterated but mysteriously # has no __iter__ (??) for x in data: yield...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 70`, `args: 38`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 101`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 38`, `import: 2`
* *Defense:* `safety: 19`, `doc: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.347
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002033
  * `Imports (Out-Degree: 0):` ..Qt, numpy
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/HistogramLUTItem.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.001 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.78 IQR)
- **Top Global Matches:** file_cluster_13: 12.001, file_cluster_8: 12.288, file_cluster_0: 12.303
- **Magnitude:** 938.48 | **LOC:** 486 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (33.5776%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 319.8 | O(2^N) | DB: 19)
  * `imageChanged` (Impact: 93.2 | O(N^6) | DB: 1)
    * *Intent:* """Enable auto-scaling on the histogram plot."""
  * `getLookupTable` (Impact: 67.7 | O(2^N) | DB: 1)
  * `paint` (Impact: 62.2 | O(N^4) | DB: 4)
    * *Intent:* # gradient position to axis orientation ax = {'left': 'right', 'right': 'left', 'top': 'bottom', 'bo...
  * `setLevels` (Impact: 56.7 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 59`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 101`, `dead_code: 2`
* *Architecture:* `api: 24`, `import: 12`
* *Defense:* `safety: 1`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.492
  * `Choke Point (Betweenness):` 3.7e-05 | `Ripple Effect (Closeness):` 0.004065
  * `Imports (Out-Degree: 6):` ..Qt, .AxisItem, ..Point, .., .GraphicsWidget, .ViewBox, .GradientEditorItem, numpy...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/PColorMeshItem.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.876 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.732 IQR)
- **Top Global Matches:** file_cluster_13: 11.876, file_cluster_8: 11.896, file_cluster_7: 12.18
- **Magnitude:** 884.14 | **LOC:** 787 | **CtrlFlow:** 60.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (38.4731%), Tech Debt (31.2827%)
**Top Internal Functions/Classes:**
  * `paintGL` (Impact: 98.1 | O(N^4) | DB: 1)
  * `paint` (Impact: 88.9 | O(N^5) | DB: 2)
  * `setup` (Impact: 72.6 | O(N^4) | DB: 3)
  * `_prepareData` (Impact: 72.4 | O(N^4) | DB: 14)
  * `__init__` (Impact: 61.9 | O(2^N) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 76`, `args: 29`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `state_mutation: 138`, `dead_code: 2`, `duplicate_logic: 3`
* *Architecture:* `api: 34`, `import: 11`
* *Defense:* `safety: 5`, `doc: 20`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.347
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002033
  * `Imports (Out-Degree: 1):` ..Qt, .., .GraphicsObject, enum, importlib, numpy
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `pyqtgraph/widgets/ColorMapMenu.py` (PYTHON) | Magnitude: 393.94 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 201, branch: 58, structural_boundaries: 38, args: 20
- `pyqtgraph/WidgetGroup.py` (PYTHON) | Magnitude: 453.38 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 200, branch: 59, structural_boundaries: 55, args: 26
- `pyqtgraph/GraphicsScene/exportDialog.py` (PYTHON) | Magnitude: 234.24 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 114, structural_boundaries: 31, state_mutation: 25, branch: 23
- `pyqtgraph/widgets/ColorButton.py` (PYTHON) | Magnitude: 119.84 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 22, api: 13, state_mutation: 13
- `pyqtgraph/dockarea/Container.py` (PYTHON) | Magnitude: 439.7 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 195, structural_boundaries: 60, branch: 43, args: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `pyqtgraph/ThreadsafeTimer.py` (PYTHON) | Magnitude: 57.26 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 7, events: 6, api: 5
- `tests/test_signalproxy.py` (PYTHON) | Magnitude: 70.84 | Delta: **0.152 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 81, structural_boundaries: 41, test: 34, events: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `pyqtgraph/parametertree/parameterTypes/basetypes.py` (PYTHON) | Magnitude: 694.92 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 259, structural_boundaries: 76, branch: 55, api: 41
- `pyqtgraph/widgets/LayoutWidget.py` (PYTHON) | Magnitude: 99.14 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 39, doc: 18, structural_boundaries: 16, api: 12
- `pyqtgraph/widgets/FeedbackButton.py` (PYTHON) | Magnitude: 232.74 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 94, state_mutation: 26, branch: 23, structural_boundaries: 16
- `pyqtgraph/examples/relativity/relativity.py` (PYTHON) | Magnitude: 738.44 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 509, structural_boundaries: 122, state_mutation: 95, branch: 78
- `pyqtgraph/graphicsItems/NonUniformImage.py` (PYTHON) | Magnitude: 232.94 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 104, state_mutation: 33, structural_boundaries: 27, branch: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `pyqtgraph/widgets/VerticalLabel.py` (PYTHON) | Magnitude: 121.28 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 50, state_mutation: 23, branch: 16, structural_boundaries: 13
- `pyqtgraph/examples/SpinBox.py` (PYTHON) | Magnitude: 8.28 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, branch: 13, structural_boundaries: 7, dead_code: 7
- `pyqtgraph/widgets/ProgressDialog.py` (PYTHON) | Magnitude: 450.26 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 153, state_mutation: 52, encapsulation: 50, structural_boundaries: 47
- `pyqtgraph/examples/BoxplotItem.py` (PYTHON) | Magnitude: 3.5 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, branch: 4, doc: 2, comprehensions: 2
- `pyqtgraph/multiprocess/parallelizer.py` (PYTHON) | Magnitude: 564.76 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 158, state_mutation: 69, branch: 63, structural_boundaries: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `pyqtgraph/exceptionHandling.py` (PYTHON) | Magnitude: 135.56 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 25, branch: 14, io: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `pyqtgraph/dockarea/Dock.py` (PYTHON) | Magnitude: 575.16 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 232, state_mutation: 112, structural_boundaries: 55, branch: 48
- `pyqtgraph/examples/GraphicsScene.py` (PYTHON) | Magnitude: 31.34 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 11, api: 7, args: 5
- `pyqtgraph/graphicsItems/LinearRegionItem.py` (PYTHON) | Magnitude: 468.74 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 210, state_mutation: 91, branch: 52, structural_boundaries: 47
- `pyqtgraph/widgets/FileDialog.py` (PYTHON) | Magnitude: 16.26 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 4, encapsulation: 3, api: 2
- `tests/parametertree/test_Parameter.py` (PYTHON) | Magnitude: 203.62 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 368, structural_boundaries: 230, test: 130, safety: 107

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `pyqtgraph/graphicsItems/__init__.py` (PYTHON) | Magnitude: 10.52 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 6

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `pyqtgraph/Qt/OpenGLHelpers.py` -> Churn: **61.58%** | Cog Load: 60.5532% | Debt: 100.0%
- `pyqtgraph/widgets/ColorMapButton.py` -> Churn: **60.86%** | Cog Load: 49.0742% | Debt: 98.6482%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `pyqtgraph/graphicsItems/ROI.py` -> **KIU Shueng Chuan** (100.0% isolated ownership) | Magnitude: 2940.92
- `pyqtgraph/graphicsItems/PlotCurveItem.py` -> **KIU Shueng Chuan** (100.0% isolated ownership) | Magnitude: 2379.86
- `pyqtgraph/debug.py` -> **Luke Campagnola** (100.0% isolated ownership) | Magnitude: 2114.42
- `pyqtgraph/Qt/__init__.py` -> **KIU Shueng Chuan** (83.3% isolated ownership) | Magnitude: 1944.29
- `pyqtgraph/widgets/SpinBox.py` -> **oyvindlr** (100.0% isolated ownership) | Magnitude: 1459.38

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pyqtgraph/parametertree/parameterTypes/basetypes.py` -> **Severity: 0.026** (Bridge: 0.0003 * Flux: 93.9258%)
- `pyqtgraph/graphicsItems/PlotItem/PlotItem.py` -> **Severity: 0.022** (Bridge: 0.0002 * Flux: 96.8759%)
- `pyqtgraph/SignalProxy.py` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 100.0%)
- `pyqtgraph/debug.py` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 98.1314%)
- `pyqtgraph/functions.py` -> **Severity: 0.008** (Bridge: 0.0002 * Flux: 32.9879%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pyqtgraph/graphicsItems/GraphicsObject.py` -> **Severity: 3.064** (Embedded: 0.0569 * Error Risk: 53.8095%)
- `pyqtgraph/parametertree/ParameterItem.py` -> **Severity: 1.735** (Embedded: 0.0309 * Error Risk: 56.1194%)
- `pyqtgraph/debug.py` -> **Severity: 1.318** (Embedded: 0.0211 * Error Risk: 62.5059%)
- `pyqtgraph/opengl/GLGraphicsItem.py` -> **Severity: 0.809** (Embedded: 0.0511 * Error Risk: 15.827%)
- `pyqtgraph/exporters/Exporter.py` -> **Severity: 0.759** (Embedded: 0.0122 * Error Risk: 62.2581%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pyqtgraph/opengl/GLGraphicsItem.py` -> **Severity: 2965.197** (Blast Radius: 29.652 * Doc Risk: 99.9999%)
- `pyqtgraph/graphicsItems/GraphicsObject.py` -> **Severity: 2895.5** (Blast Radius: 28.955 * Doc Risk: 100.0%)
- `pyqtgraph/parametertree/parameterTypes/basetypes.py` -> **Severity: 2396.9** (Blast Radius: 23.969 * Doc Risk: 100.0%)
- `pyqtgraph/parametertree/ParameterItem.py` -> **Severity: 2282.5** (Blast Radius: 22.825 * Doc Risk: 100.0%)
- `pyqtgraph/Point.py` -> **Severity: 1807.489** (Blast Radius: 18.075 * Doc Risk: 99.9994%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
