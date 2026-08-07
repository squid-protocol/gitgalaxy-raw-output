# ARCHITECTURAL_BRIEF: pyqtgraph
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/pyqtgraph` |
| **Timestamp** | `2026-08-07T04:01:29.614712+00:00` |
| **Scan Duration** | `1.69s` |
| **Git Branch** | `master` |
| **Git Commit** | `d588dd3ec30915e61c8496a0fe1db21fc25e4da5` |
| **Git Remote** | `https://github.com/pyqtgraph/pyqtgraph.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 400 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.611`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 283 | 57.4% |
| file_cluster_13 | 172 | 34.9% |
| file_cluster_0 | 15 | 3.0% |
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
| Cognitive Load Exposure | 0.0 | 79.1 | 14.0 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.5 | 42.4 | 58.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 11.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 16.2 | 2.3 | 0.0 |
| API Exposure | 0.0 | 13.1 | 3.6 | 3.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 29.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 89.6 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 18.8 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 93.1 | 4.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 28.5 | 15.3 | 0.0 |
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

- `setLeftButtonAction` (@ `pyqtgraph/graphicsItems/ViewBox/ViewBox.py`) -> Impact: **732.8** | LOC: 1389
- `labelString` (@ `pyqtgraph/graphicsItems/AxisItem.py`) -> Impact: **434.4** | LOC: 860
- `rectStr` (@ `pyqtgraph/graphicsItems/ROI.py`) -> Impact: **361.9** | LOC: 933
- `siScale` (@ `pyqtgraph/functions.py`) -> Impact: **350.8** | LOC: 487
- `interpolateArray` (@ `pyqtgraph/functions.py`) -> Impact: **297.4** | LOC: 447
- `debugMsg` (@ `pyqtgraph/multiprocess/remoteproxy.py`) -> Impact: **264.6** | LOC: 453
  * *Intent:* # corresponding code is in: # processes.py::Process.__init__() if pid is None: connection.send(os.getpid()) pid = connection.recv() RemoteEventHandler...
- `dataBounds` (@ `pyqtgraph/graphicsItems/PlotCurveItem.py`) -> Impact: **215.1** | LOC: 321
- `setOpts` (@ `pyqtgraph/widgets/SpinBox.py`) -> Impact: **212.8** | LOC: 445
- `addDock` (@ `pyqtgraph/dockarea/DockArea.py`) -> Impact: **205.7** | LOC: 342
  * *Intent:* """Adds a dock to this area. ============== ================================================================= **Arguments:** dock The new Dock object ...
- `writeCsv` (@ `pyqtgraph/graphicsItems/PlotItem/PlotItem.py`) -> Impact: **191.0** | LOC: 390

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `pyqtgraph/graphicsItems` | 38 | 10729.32 | 32.58% | 25.12% |
| `pyqtgraph` | 20 | 4344.86 | 20.38% | 27.73% |
| `pyqtgraph/widgets` | 32 | 3732.54 | 31.69% | 29.39% |
| `pyqtgraph/examples` | 108 | 2302.08 | 8.14% | 0.0% |
| `pyqtgraph/Qt` | 6 | 2234.43 | 28.12% | 45.88% |
| `pyqtgraph/colors/maps` | 71 | 1395.74 | 0.0% | 0.0% |
| `pyqtgraph/graphicsItems/ViewBox` | 3 | 1349.86 | 24.66% | 17.37% |
| `pyqtgraph/parametertree/parameterTypes` | 20 | 1212.2 | 14.84% | 33.9% |
| `pyqtgraph/flowchart` | 4 | 1169.32 | 36.72% | 52.75% |
| `pyqtgraph/opengl` | 5 | 1163.12 | 25.43% | 24.97% |

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
- `pyqtgraph/graphicsItems/ROI.py` -> **0** Orphaned Functions | **78** Duplicates
- `tests/parametertree/test_Parameter.py` -> **22** Orphaned Functions | **14** Duplicates
- `pyqtgraph/dockarea/Container.py` -> **0** Orphaned Functions | **22** Duplicates
- `pyqtgraph/widgets/RemoteGraphicsView.py` -> **0** Orphaned Functions | **20** Duplicates
- `pyqtgraph/debug.py` -> **0** Orphaned Functions | **19** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1104` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `pyqtgraph/widgets/ColorMapButton.py` (PYTHON) -> Cumulative Risk: **655.04**
- **Archetype:** `file_cluster_13` (Distance: 11.205 IQR)
- **Magnitude:** 90.52 | **LOC:** 121 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.8653%), Tech Debt (98.6482%)
- **Heaviest Functions:** `getImage` (Impact: 14.5), `paintColorMap` (Impact: 9.3), `_setColorMap` (Impact: 7.5)

### 2. `pyqtgraph/dockarea/DockDrop.py` (PYTHON) -> Cumulative Risk: **643.38**
- **Archetype:** `file_cluster_8` (Distance: 12.283 IQR)
- **Magnitude:** 163.58 | **LOC:** 140 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9498%), Documentation (99.2413%)
- **Heaviest Functions:** `dragMoveEvent` (Impact: 33.2), `setDropArea` (Impact: 15.2), `dragEnterEvent` (Impact: 7.3)

### 3. `pyqtgraph/Qt/internals.py` (PYTHON) -> Cumulative Risk: **641.5**
- **Archetype:** `file_cluster_13` (Distance: 11.536 IQR)
- **Magnitude:** 164.32 | **LOC:** 249 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9995%), Safety Score (84.939%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Impact: 21.1), `resize` (Impact: 18.9), `get_qpainterpath_element_array` (Impact: 15.2)

### 4. `pyqtgraph/debug.py` (PYTHON) -> Cumulative Risk: **634.45**
- **Archetype:** `file_cluster_13` (Distance: 14.116 IQR)
- **Magnitude:** 845.52 | **LOC:** 1296 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.1314%), Tech Debt (95.9835%), Documentation (88.647%)
- **Heaviest Functions:** `printTrace` (Impact: 91.2), `refPathString` (Impact: 83.6), `typeStr` (Impact: 47.8)

### 5. `pyqtgraph/multiprocess/parallelizer.py` (PYTHON) -> Cumulative Risk: **624.62**
- **Archetype:** `file_cluster_17` (Distance: 19.854 IQR)
- **Magnitude:** 234.06 | **LOC:** 342 | **CtrlFlow:** 61.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Dead Code (85.0286%), Safety Score (81.7146%)
- **Heaviest Functions:** `runParallel` (Impact: 56.4), `suggestedWorkerCount` (Impact: 18.4), `__init__` (Impact: 18.2)

### 6. `pyqtgraph/graphicsItems/ROI.py` (PYTHON) -> Cumulative Risk: **610.7**
- **Archetype:** `file_cluster_8` (Distance: 12.114 IQR)
- **Magnitude:** 1677.22 | **LOC:** 2385 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.7157%)
- **Heaviest Functions:** `rectStr` (Impact: 361.9), `movePoint` (Impact: 159.6), `mouseDragEvent` (Impact: 44.3)

### 7. `pyqtgraph/graphicsItems/GraphicsWidget.py` (PYTHON) -> Cumulative Risk: **609.16**
- **Archetype:** `file_cluster_13` (Distance: 16.967 IQR)
- **Magnitude:** 52.18 | **LOC:** 76 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Tech Debt (88.5488%)
- **Heaviest Functions:** `boundingRect` (Impact: 5.7), `shape` (Impact: 3.8), `__init__` (Impact: 2.5)

### 8. `pyqtgraph/dockarea/Dock.py` (PYTHON) -> Cumulative Risk: **604.33**
- **Archetype:** `file_cluster_8` (Distance: 12.591 IQR)
- **Magnitude:** 315.46 | **LOC:** 372 | **CtrlFlow:** 46.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.2235%), Documentation (95.6311%)
- **Heaviest Functions:** `setOrientation` (Impact: 19.0), `__init__` (Impact: 13.7), `containerChanged` (Impact: 11.2)

### 9. `pyqtgraph/widgets/RawImageWidget.py` (PYTHON) -> Cumulative Risk: **603.61**
- **Archetype:** `file_cluster_13` (Distance: 11.664 IQR)
- **Magnitude:** 175.46 | **LOC:** 267 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9876%), Tech Debt (95.6274%), Verification (80.0%)
- **Heaviest Functions:** `uploadTexture` (Impact: 34.4), `paintEvent` (Impact: 32.0), `checkCudaErrors` (Impact: 9.2)

### 10. `pyqtgraph/graphicsItems/TargetItem.py` (PYTHON) -> Cumulative Risk: **603.43**
- **Archetype:** `file_cluster_13` (Distance: 12.923 IQR)
- **Magnitude:** 314.42 | **LOC:** 468 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.5961%), Safety Score (85.9677%)
- **Heaviest Functions:** `setLabel` (Impact: 18.9), `mouseDragEvent` (Impact: 11.3), `mouseDragEvent` (Impact: 11.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pyqtgraph/Qt/__init__.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.84 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.745 IQR)
- **Top Global Matches:** file_cluster_13: 10.84, file_cluster_8: 11.091, file_cluster_7: 11.635
- **Magnitude:** 1944.29 | **LOC:** 399 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (17.7343%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 92`, `args: 11`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`
* *Architecture:* `io: 10`, `api: 5`, `import: 41`
* *Defense:* `safety: 35`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.332
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Qt, PyQt5.QtCore, importlib, PySide6.QtGui, xml.etree.ElementTree, sys, PyQt6.QtGui, PyQt5.QtGui...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyqtgraph/graphicsItems/ROI.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.114 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.574 IQR)
- **Top Global Matches:** file_cluster_8: 12.114, file_cluster_7: 12.273, file_cluster_13: 12.325
- **Magnitude:** 1677.22 | **LOC:** 2385 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (32.9692%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `rectStr` (Impact: 361.9)
  * `movePoint` (Impact: 159.6)
  * `mouseDragEvent` (Impact: 44.3)
  * `getArrayRegion` (Impact: 32.9)
  * `getArraySlice` (Impact: 22.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 321`, `structural_boundaries: 308`, `args: 151`, `func_start: 150`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 279`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 3`, `duplicate_logic: 78`
* *Architecture:* `io: 1`, `api: 149`, `import: 9`
* *Defense:* `safety: 11`, `doc: 108`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.574
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.004065
  * `Imports (Out-Degree: 4):` .., .GraphicsObject, math, ..SRTTransform, sys, ..Qt, ..Point, numpy.linalg...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyqtgraph/functions.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.225 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.227 IQR)
- **Top Global Matches:** file_cluster_8: 12.225, file_cluster_13: 12.374, file_cluster_17: 12.46
- **Magnitude:** 1396.34 | **LOC:** 3190 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (12.5779%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `siScale` (Impact: 350.8)
  * `interpolateArray` (Impact: 297.4)
  * `isocurve` (Impact: 98.8)
  * `arrayToQPath` (Impact: 63.3)
  * `_pseudoScatterExact` (Impact: 45.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 482`, `structural_boundaries: 232`, `args: 66`, `func_start: 64`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 70`, `dead_code: 22`
* *Architecture:* `io: 2`, `api: 57`, `import: 15`
* *Defense:* `safety: 57`, `doc: 110`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.353
  * `Choke Point (Betweenness):` 0.000232 | `Ripple Effect (Closeness):` 0.026205
  * `Imports (Out-Degree: 2):` math, scipy.ndimage, sys, , warnings, .Qt, .util.cupy_helper, debug...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/ViewBox/ViewBox.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.536 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.476 IQR)
- **Top Global Matches:** file_cluster_13: 12.536, file_cluster_0: 12.598, file_cluster_8: 12.642
- **Magnitude:** 1159.18 | **LOC:** 1876 | **CtrlFlow:** 65.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (33.1876%), Tech Debt (52.1009%)
**Top Internal Functions/Classes:**
  * `setLeftButtonAction` (Impact: 732.8)
  * `__init__` (Impact: 25.0)
    * *Intent:* ## mouse modes
  * `getState` (Impact: 14.7)
  * `itemChange` (Impact: 14.6)
  * `register` (Impact: 12.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 426`, `structural_boundaries: 221`, `args: 108`, `func_start: 107`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 157`, `dead_code: 11`, `fragile_debt: 2`, `duplicate_logic: 7`
* *Architecture:* `io: 1`, `api: 108`, `import: 13`
* *Defense:* `safety: 33`, `doc: 100`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.332
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ..ItemGroup, ..., ...Point, math, sys, .ViewBoxMenu, weakref, ..GraphicsWidget...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyqtgraph/graphicsItems/AxisItem.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.419 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.934 IQR)
- **Top Global Matches:** file_cluster_8: 12.419, file_cluster_13: 12.576, file_cluster_7: 12.597
- **Magnitude:** 871.54 | **LOC:** 1780 | **CtrlFlow:** 69.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (46.9941%), Tech Debt (9.3363%)
**Top Internal Functions/Classes:**
  * `labelString` (Impact: 434.4)
  * `setStyle` (Impact: 24.3)
  * `resizeEvent` (Impact: 11.6)
  * `showLabel` (Impact: 7.4)
  * `getSIPrefixEnableRanges` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 120`, `args: 52`, `func_start: 52`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 298`, `fragile_debt: 1`
* *Architecture:* `api: 51`, `import: 9`
* *Defense:* `safety: 9`, `doc: 68`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.293
  * `Choke Point (Betweenness):` 2.7e-05 | `Ripple Effect (Closeness):` 0.012703
  * `Imports (Out-Degree: 2):` .., math, weakref, .GraphicsWidget, ..Qt, ..Point, numpy
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pyqtgraph/debug.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.116 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.963 IQR)
- **Top Global Matches:** file_cluster_13: 14.116, file_cluster_17: 14.154, file_cluster_0: 14.259
- **Magnitude:** 845.52 | **LOC:** 1296 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.5805%), Tech Debt (95.9835%)
**Top Internal Functions/Classes:**
  * `printTrace` (Impact: 91.2)
    * *Intent:* # print(" "*indent + prefix + '='*30 + '>>') # print(" "*indent + prefix + '='*30 + '<<') def printT...
  * `refPathString` (Impact: 83.6)
  * `typeStr` (Impact: 47.8)
  * `listQThreads` (Impact: 44.2)
  * `collect` (Impact: 38.8)
    * *Intent:* #print "deleted:", len(delRefs)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 235`, `args: 82`, `func_start: 80`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 132`, `dead_code: 15`, `duplicate_logic: 19`
* *Architecture:* `io: 23`, `api: 81`, `concurrency: 11`, `import: 23`
* *Defense:* `safety: 70`, `doc: 84`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.225
  * `Choke Point (Betweenness):` 9.5e-05 | `Ripple Effect (Closeness):` 0.021082
  * `Imports (Out-Degree: 1):` __future__, time, sys, .util.mutex, weakref, pstats, gc, sip...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/ScatterPlotItem.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.912 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.222 IQR)
- **Top Global Matches:** file_cluster_8: 11.912, file_cluster_13: 11.927, file_cluster_7: 12.059
- **Magnitude:** 830.7 | **LOC:** 1242 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.5318%), Tech Debt (86.4023%)
**Top Internal Functions/Classes:**
  * `setPointData` (Impact: 123.8)
  * `addPoints` (Impact: 101.8)
  * `setSize` (Impact: 43.7)
  * `setBrush` (Impact: 38.0)
  * `paint` (Impact: 35.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 144`, `args: 76`, `func_start: 75`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 120`, `dead_code: 3`, `fragile_debt: 1`, `duplicate_logic: 9`
* *Architecture:* `api: 69`, `import: 11`
* *Defense:* `safety: 37`, `doc: 60`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.255
  * `Choke Point (Betweenness):` 2.7e-05 | `Ripple Effect (Closeness):` 0.014935
  * `Imports (Out-Degree: 2):` .., .GraphicsObject, math, itertools, weakref, ..Qt, ..Point, collections...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/PlotCurveItem.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.51 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.673 IQR)
- **Top Global Matches:** file_cluster_13: 12.51, file_cluster_8: 12.589, file_cluster_0: 12.653
- **Magnitude:** 786.76 | **LOC:** 1294 | **CtrlFlow:** 68.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.2066%), Tech Debt (37.3038%)
**Top Internal Functions/Classes:**
  * `dataBounds` (Impact: 215.1)
  * `paintGL` (Impact: 97.3)
    * *Intent:* # note that left/right vertical lines can be omitted here
  * `paint` (Impact: 73.2)
  * `arrayToLineSegments` (Impact: 58.2)
  * `_getFillPathList` (Impact: 21.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 113`, `args: 42`, `func_start: 42`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 123`, `dead_code: 12`, `fragile_debt: 2`, `duplicate_logic: 3`
* *Architecture:* `api: 39`, `import: 12`
* *Defense:* `safety: 19`, `doc: 34`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.069
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.01626
  * `Imports (Out-Degree: 1):` importlib, .., .GraphicsObject, math, warnings, ..Qt, numpy
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/PlotItem/PlotItem.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.789 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.72 IQR)
- **Top Global Matches:** file_cluster_13: 11.789, file_cluster_8: 11.946, file_cluster_0: 11.995
- **Magnitude:** 747.42 | **LOC:** 1646 | **CtrlFlow:** 56.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.3044%), Tech Debt (8.4793%)
**Top Internal Functions/Classes:**
  * `writeCsv` (Impact: 191.0)
  * `multiDataPlot` (Impact: 55.0)
  * `addAvgCurve` (Impact: 30.4)
    * *Intent:* # Set up new axis
  * `addItem` (Impact: 29.1)
  * `setAxisItems` (Impact: 25.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 177`, `args: 77`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 118`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 87`, `import: 24`
* *Defense:* `safety: 14`, `doc: 76`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.138
  * `Choke Point (Betweenness):` 0.000228 | `Ripple Effect (Closeness):` 0.010163
  * `Imports (Out-Degree: 9):` ..LegendItem, ..., ..ViewBox, ...WidgetGroup, weakref, typing, warnings, ...widgets.FileDialog...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/ImageItem.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.536 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.862 IQR)
- **Top Global Matches:** file_cluster_13: 12.536, file_cluster_8: 12.752, file_cluster_16: 12.837
- **Magnitude:** 736.88 | **LOC:** 1227 | **CtrlFlow:** 58.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.733%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 61.4)
    * *Intent:* * `border`, whose value is directed to :meth:`setBorder` * `colorMap`, whose value is directed to :m...
  * `setImage` (Impact: 57.4)
  * `setOpts` (Impact: 33.8)
    * *Intent:* ----------
  * `drawAt` (Impact: 24.1)
  * `paint` (Impact: 17.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 131`, `args: 49`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 236`, `dead_code: 2`
* *Architecture:* `io: 4`, `api: 65`, `import: 15`
* *Defense:* `safety: 10`, `doc: 48`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.347
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002033
  * `Imports (Out-Degree: 3):` ..util.cupy_helper, .., .GraphicsObject, os, pathlib, warnings, ..Qt, numpy.typing...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/PlotDataItem.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.263 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.169 IQR)
- **Top Global Matches:** file_cluster_13: 12.263, file_cluster_0: 12.344, file_cluster_8: 12.44
- **Magnitude:** 612.58 | **LOC:** 1890 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (29.7832%), Tech Debt (23.1102%)
**Top Internal Functions/Classes:**
  * `_getDisplayDataset` (Impact: 110.7)
  * `updateItems` (Impact: 39.1)
  * `dataType` (Impact: 38.4)
  * `viewRangeChanged` (Impact: 21.2)
  * `applyLogMapping` (Impact: 16.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 126`, `args: 52`, `func_start: 52`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 121`, `dead_code: 8`, `duplicate_logic: 4`
* *Architecture:* `api: 77`, `import: 12`
* *Defense:* `safety: 18`, `doc: 72`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.628
  * `Choke Point (Betweenness):` 3.2e-05 | `Ripple Effect (Closeness):` 0.01084
  * `Imports (Out-Degree: 3):` .., .GraphicsObject, bisect, math, .PlotCurveItem, warnings, ..Qt, .ScatterPlotItem...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pyqtgraph/multiprocess/remoteproxy.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.893 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.736 IQR)
- **Top Global Matches:** file_cluster_13: 12.893, file_cluster_4: 12.947, file_cluster_0: 13.064
- **Magnitude:** 594.62 | **LOC:** 1143 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.6147%), Tech Debt (33.3417%)
**Top Internal Functions/Classes:**
  * `debugMsg` (Impact: 264.6)
    * *Intent:* # corresponding code is in: # processes.py::Process.__init__() if pid is None: connection.send(os.ge...
  * `unpickleObjectProxy` (Impact: 15.3)
  * `_setProxyOptions` (Impact: 11.8)
  * `__getattr__` (Impact: 10.6)
  * `__init__` (Impact: 7.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 230`, `args: 93`, `func_start: 93`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 74`, `dead_code: 6`, `duplicate_logic: 4`
* *Architecture:* `io: 11`, `api: 36`, `concurrency: 34`, `import: 13`
* *Defense:* `safety: 38`, `doc: 44`, `test: 2`, `sync_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.506
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006098
  * `Imports (Out-Degree: 0):` Request, from, time, os, threading, ..util, traceback, new...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pyqtgraph/flowchart/Flowchart.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.407 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.893 IQR)
- **Top Global Matches:** file_cluster_13: 12.407, file_cluster_8: 12.621, file_cluster_0: 12.718
- **Magnitude:** 573.46 | **LOC:** 926 | **CtrlFlow:** 47.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.8478%), Tech Debt (37.8992%)
**Top Internal Functions/Classes:**
  * `createNode` (Impact: 87.9)
  * `setCurrentFile` (Impact: 47.1)
  * `nodeOutputChanged` (Impact: 24.8)
  * `processOrder` (Impact: 24.7)
  * `restoreState` (Impact: 19.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 157`, `args: 71`, `func_start: 69`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 104`, `dead_code: 5`, `duplicate_logic: 5`
* *Architecture:* `api: 76`, `import: 16`
* *Defense:* `safety: 39`, `doc: 38`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.332
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .Terminal, ..graphicsItems.GraphicsObject, .Node, .., importlib, .library, os, ..debug...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyqtgraph/flowchart/Terminal.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.98 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.194 IQR)
- **Top Global Matches:** file_cluster_8: 11.98, file_cluster_13: 12.089, file_cluster_7: 12.233
- **Magnitude:** 559.06 | **LOC:** 584 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.036%), Tech Debt (73.0837%)
**Top Internal Functions/Classes:**
  * `connectTo` (Impact: 51.8)
  * `generatePath` (Impact: 43.4)
  * `mouseDragEvent` (Impact: 22.6)
  * `setValue` (Impact: 16.9)
  * `__init__` (Impact: 11.5)
    * *Intent:* """ Construct a new terminal. ============== =======================================================...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 130`, `args: 72`, `func_start: 72`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 127`, `dead_code: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 80`, `import: 5`
* *Defense:* `safety: 8`, `doc: 22`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.709
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.002033
  * `Imports (Out-Degree: 2):` ..graphicsItems.GraphicsObject, .., weakref, ..Qt, ..Point
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/InfiniteLine.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.996 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.239 IQR)
- **Top Global Matches:** file_cluster_13: 12.996, file_cluster_8: 13.244, file_cluster_7: 13.372
- **Magnitude:** 541.58 | **LOC:** 622 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.2917%), Tech Debt (99.6118%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 42.3)
    * *Intent:* **Signals:**
  * `setPos` (Impact: 29.3)
  * `__init__` (Impact: 23.9)
  * `addMarker` (Impact: 21.8)
  * `setHoverPen` (Impact: 14.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 84`, `args: 40`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 184`, `dead_code: 3`, `duplicate_logic: 12`
* *Architecture:* `api: 47`, `import: 9`
* *Defense:* `safety: 5`, `doc: 34`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.347
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002033
  * `Imports (Out-Degree: 3):` .GraphicsItem, .., .GraphicsObject, math, .ViewBox, ..Qt, ..Point, .TextItem...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/parametertree/Parameter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.076 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.57 IQR)
- **Top Global Matches:** file_cluster_0: 13.076, file_cluster_13: 13.133, file_cluster_11: 13.43
- **Magnitude:** 527.26 | **LOC:** 879 | **CtrlFlow:** 40.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.8489%), Tech Debt (21.886%)
**Top Internal Functions/Classes:**
  * `restoreState` (Impact: 48.3)
  * `insertChild` (Impact: 38.9)
    * *Intent:* """ return not self.readonly() def setWritable(self, writable=True): """Set whether this Parameter s...
  * `setName` (Impact: 19.8)
  * `saveState` (Impact: 16.6)
  * `setOpts` (Impact: 16.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 158`, `args: 73`, `func_start: 73`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 73`, `dead_code: 5`, `duplicate_logic: 2`
* *Architecture:* `api: 73`, `import: 7`
* *Defense:* `safety: 24`, `doc: 102`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.856
  * `Choke Point (Betweenness):` 8.6e-05 | `Ripple Effect (Closeness):` 0.0371
  * `Imports (Out-Degree: 1):` .., warnings, weakref, .ParameterItem, ..Qt, collections, re
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/GradientEditorItem.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 15.607 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.419 IQR)
- **Top Global Matches:** file_cluster_0: 15.607, file_cluster_13: 15.692, file_cluster_11: 15.748
- **Magnitude:** 522.04 | **LOC:** 981 | **CtrlFlow:** 46.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.3945%), Tech Debt (83.3875%)
**Top Internal Functions/Classes:**
  * `setOrientation` (Impact: 76.0)
  * `getColor` (Impact: 38.5)
  * `getGradient` (Impact: 11.4)
    * *Intent:* ## public if cm not in ['rgb', 'hsv']: raise Exception("Unknown color mode %s. Options are 'rgb' and...
  * `mouseDragEvent` (Impact: 11.3)
  * `isLookupTrivial` (Impact: 11.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 123`, `args: 65`, `func_start: 62`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 140`, `dead_code: 23`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `io: 1`, `api: 66`, `import: 10`
* *Defense:* `safety: 3`, `doc: 50`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.072
  * `Choke Point (Betweenness):` 4.3e-05 | `Ripple Effect (Closeness):` 0.008469
  * `Imports (Out-Degree: 3):` ..widgets.ColorMapMenu, ..widgets.SpinBox, .GradientPresets, ..colormap, .., weakref, .GraphicsWidget, ..Qt...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/PColorMeshItem.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.876 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.732 IQR)
- **Top Global Matches:** file_cluster_13: 11.876, file_cluster_8: 11.896, file_cluster_7: 12.18
- **Magnitude:** 472.14 | **LOC:** 787 | **CtrlFlow:** 60.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.4731%), Tech Debt (31.2827%)
**Top Internal Functions/Classes:**
  * `paintGL` (Impact: 43.5)
  * `setup` (Impact: 31.0)
  * `_prepareData` (Impact: 30.9)
  * `paint` (Impact: 30.7)
  * `_drawPicture` (Impact: 25.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 76`, `args: 29`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `state_mutation: 138`, `dead_code: 2`, `duplicate_logic: 3`
* *Architecture:* `api: 34`, `import: 11`
* *Defense:* `safety: 5`, `doc: 20`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.347
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002033
  * `Imports (Out-Degree: 1):` .., importlib, .GraphicsObject, enum, ..Qt, numpy
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/colormap.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.303 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.652 IQR)
- **Top Global Matches:** file_cluster_13: 12.303, file_cluster_8: 12.412, file_cluster_17: 12.575
- **Magnitude:** 455.86 | **LOC:** 847 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.2518%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_getFromFile` (Impact: 76.9)
  * `map` (Impact: 35.9)
    * *Intent:* # alternative code may be more efficient, but fails to handle lists of QColor. # self.color = np.app...
  * `makeMonochrome` (Impact: 21.1)
  * `getSubset` (Impact: 20.7)
  * `getStops` (Impact: 20.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 105`, `args: 30`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 67`, `dead_code: 3`
* *Architecture:* `io: 1`, `api: 41`, `import: 9`
* *Defense:* `safety: 27`, `doc: 56`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.615
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002033
  * `Imports (Out-Degree: 1):` os, matplotlib.pyplot, colorcet, .Qt, .functions, collections.abc, numpy
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/examples/relativity/relativity.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.358 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.82 IQR)
- **Top Global Matches:** file_cluster_13: 12.358, file_cluster_0: 12.365, file_cluster_8: 12.443
- **Magnitude:** 406.34 | **LOC:** 763 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.5859%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `hypIntersect` (Impact: 24.4)
    * *Intent:* ## given a reference clock (seen from inertial frame) has rx, rt, and rv, ## and another clock start...
  * `runReference` (Impact: 21.9)
  * `getCurve` (Impact: 19.6)
  * `stepTo` (Impact: 15.4)
  * `runInertial` (Impact: 13.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 122`, `args: 44`, `func_start: 44`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 95`, `dead_code: 9`, `duplicate_logic: 15`
* *Architecture:* `io: 10`, `api: 45`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.596
  * `Choke Point (Betweenness):` 4.1e-05 | `Ripple Effect (Closeness):` 0.004065
  * `Imports (Out-Degree: 1):` time, os, pyqtgraph.parametertree, pyqtgraph.console, sys, pyqtgraph, pyqtgraph.Qt, collections...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyqtgraph/opengl/GLViewWidget.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.738 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.626 IQR)
- **Top Global Matches:** file_cluster_8: 11.738, file_cluster_13: 11.755, file_cluster_7: 12.003
- **Magnitude:** 405.66 | **LOC:** 569 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (20.5012%), Tech Debt (24.9645%)
**Top Internal Functions/Classes:**
  * `initializeGL` (Impact: 54.6)
  * `setCameraPosition` (Impact: 49.4)
    * *Intent:* # The GLGraphicsItem(s) making use of QPainter end # rebind it before each GLGraphicsItem. if self.d...
  * `pan` (Impact: 21.8)
  * `evalKeyState` (Impact: 18.3)
  * `mouseMoveEvent` (Impact: 18.2)
    * *Intent:* # apply translation self.opts['center'] += scale_factor * (xv*-dx + yv*dy + zv*dz) else: # use defau...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 83`, `args: 39`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 78`, `duplicate_logic: 2`
* *Architecture:* `api: 52`, `import: 11`
* *Defense:* `safety: 14`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.332
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` OpenGL, importlib, .., math, warnings, ..Qt, numpy
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyqtgraph/opengl/MeshData.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.422 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.993 IQR)
- **Top Global Matches:** file_cluster_13: 13.422, file_cluster_0: 13.485, file_cluster_8: 13.627
- **Magnitude:** 399.86 | **LOC:** 515 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.3339%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 23.6)
  * `setVertexes` (Impact: 16.5)
  * `save` (Impact: 14.9)
    * *Intent:* #def _setUnindexedFaces(self, faces, vertexes, vertexColors=None, faceColors=None): #self._vertexes ...
  * `vertexes` (Impact: 14.5)
  * `vertexNormals` (Impact: 13.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 61`, `args: 27`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 132`, `dead_code: 4`
* *Architecture:* `api: 35`, `import: 4`
* *Defense:* `safety: 5`, `doc: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.415
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00813
  * `Imports (Out-Degree: 0):` pickle, ..Qt, numpy
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pyqtgraph/widgets/TableWidget.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.708 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.539 IQR)
- **Top Global Matches:** file_cluster_0: 12.708, file_cluster_13: 12.877, file_cluster_8: 12.974
- **Magnitude:** 384.8 | **LOC:** 477 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.6735%), Tech Debt (33.254%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 66.4)
    * *Intent:* """ def __init__(self, *args, **kwds): """
  * `serialize` (Impact: 22.7)
  * `iteratorFn` (Impact: 16.4)
  * `format` (Impact: 10.9)
  * `defersort` (Impact: 10.7)
    * *Intent:* # may be called recursively; only the first call needs to block sorting setSorting = False if self._...
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
- **Global Archetype:** `file_cluster_13` (Drift: 12.005 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.782 IQR)
- **Top Global Matches:** file_cluster_13: 12.005, file_cluster_8: 12.293, file_cluster_0: 12.308
- **Magnitude:** 362.48 | **LOC:** 486 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.5776%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 49.9)
  * `imageChanged` (Impact: 28.2)
    * *Intent:* """Enable auto-scaling on the histogram plot."""
  * `paint` (Impact: 26.2)
    * *Intent:* # gradient position to axis orientation ax = {'left': 'right', 'right': 'left', 'top': 'bottom', 'bo...
  * `setLevels` (Impact: 23.1)
  * `_showRegions` (Impact: 14.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 59`, `args: 22`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 101`, `dead_code: 2`
* *Architecture:* `api: 24`, `import: 12`
* *Defense:* `safety: 1`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.492
  * `Choke Point (Betweenness):` 3.7e-05 | `Ripple Effect (Closeness):` 0.004065
  * `Imports (Out-Degree: 6):` .LinearRegionItem, .., .GradientEditorItem, .AxisItem, .PlotCurveItem, weakref, .ViewBox, .GraphicsWidget...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyqtgraph/GraphicsScene/GraphicsScene.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.144 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.97 IQR)
- **Top Global Matches:** file_cluster_13: 13.144, file_cluster_0: 13.288, file_cluster_17: 13.314
- **Magnitude:** 353.22 | **LOC:** 545 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.288%), Tech Debt (14.8715%)
**Top Internal Functions/Classes:**
  * `sendDragEvent` (Impact: 42.6)
  * `sendHoverEvents` (Impact: 34.6)
    * *Intent:* ## keep track of which buttons are involved in dragging
  * `mouseMoveEvent` (Impact: 31.3)
  * `sendClickEvent` (Impact: 29.5)
  * `addParentContextMenus` (Impact: 28.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 70`, `args: 23`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 76`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 25`, `import: 9`
* *Defense:* `safety: 27`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.332
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .., time, .mouseEvents, , warnings, weakref, ..Qt, ..Point
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `pyqtgraph/widgets/ColorMapMenu.py` (PYTHON) | Magnitude: 190.44 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 201, branch: 58, structural_boundaries: 38, args: 20
- `pyqtgraph/WidgetGroup.py` (PYTHON) | Magnitude: 167.38 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 200, branch: 59, structural_boundaries: 55, args: 26
- `pyqtgraph/GraphicsScene/exportDialog.py` (PYTHON) | Magnitude: 111.84 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 114, structural_boundaries: 31, state_mutation: 25, branch: 23
- `tests/parametertree/test_Parameter.py` (PYTHON) | Magnitude: 198.42 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 368, structural_boundaries: 230, test: 130, safety: 107
- `pyqtgraph/widgets/ColorButton.py` (PYTHON) | Magnitude: 64.74 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 22, api: 13, state_mutation: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `pyqtgraph/ThreadsafeTimer.py` (PYTHON) | Magnitude: 21.66 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 7, events: 6, api: 5
- `tests/test_signalproxy.py` (PYTHON) | Magnitude: 35.34 | Delta: **0.152 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 81, structural_boundaries: 41, test: 34, events: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `pyqtgraph/parametertree/parameterTypes/basetypes.py` (PYTHON) | Magnitude: 265.22 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 259, structural_boundaries: 76, branch: 55, api: 41
- `pyqtgraph/widgets/LayoutWidget.py` (PYTHON) | Magnitude: 49.54 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 39, doc: 18, structural_boundaries: 16, api: 12
- `pyqtgraph/widgets/FeedbackButton.py` (PYTHON) | Magnitude: 117.64 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 94, state_mutation: 26, branch: 23, structural_boundaries: 16
- `pyqtgraph/examples/relativity/relativity.py` (PYTHON) | Magnitude: 406.34 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 509, structural_boundaries: 122, state_mutation: 95, branch: 78
- `pyqtgraph/graphicsItems/NonUniformImage.py` (PYTHON) | Magnitude: 116.14 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 104, state_mutation: 33, structural_boundaries: 27, branch: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `pyqtgraph/widgets/VerticalLabel.py` (PYTHON) | Magnitude: 69.18 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 50, state_mutation: 23, branch: 16, structural_boundaries: 13
- `pyqtgraph/examples/SpinBox.py` (PYTHON) | Magnitude: 8.28 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, branch: 13, structural_boundaries: 7, dead_code: 7
- `pyqtgraph/widgets/ProgressDialog.py` (PYTHON) | Magnitude: 199.86 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 153, state_mutation: 52, encapsulation: 50, structural_boundaries: 47
- `pyqtgraph/examples/BoxplotItem.py` (PYTHON) | Magnitude: 3.5 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, branch: 4, doc: 2, comprehensions: 2
- `pyqtgraph/multiprocess/parallelizer.py` (PYTHON) | Magnitude: 234.06 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 158, state_mutation: 69, branch: 63, structural_boundaries: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `pyqtgraph/exceptionHandling.py` (PYTHON) | Magnitude: 83.06 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 25, branch: 14, io: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `pyqtgraph/dockarea/Dock.py` (PYTHON) | Magnitude: 315.46 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 232, state_mutation: 112, structural_boundaries: 55, branch: 48
- `pyqtgraph/examples/GraphicsScene.py` (PYTHON) | Magnitude: 20.74 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 11, api: 7, args: 5
- `pyqtgraph/graphicsItems/LinearRegionItem.py` (PYTHON) | Magnitude: 263.64 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 210, state_mutation: 91, branch: 52, structural_boundaries: 47
- `pyqtgraph/widgets/FileDialog.py` (PYTHON) | Magnitude: 5.86 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 4, encapsulation: 3, api: 2
- `pyqtgraph/opengl/items/GLBoxItem.py` (PYTHON) | Magnitude: 43.86 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 21, state_mutation: 11, api: 7

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

- `pyqtgraph/Qt/__init__.py` -> **KIU Shueng Chuan** (83.3% isolated ownership) | Magnitude: 1944.29
- `pyqtgraph/graphicsItems/ROI.py` -> **KIU Shueng Chuan** (100.0% isolated ownership) | Magnitude: 1677.22
- `pyqtgraph/debug.py` -> **Luke Campagnola** (100.0% isolated ownership) | Magnitude: 845.52
- `pyqtgraph/graphicsItems/PlotCurveItem.py` -> **KIU Shueng Chuan** (100.0% isolated ownership) | Magnitude: 786.76
- `pyqtgraph/graphicsItems/ImageItem.py` -> **KIU Shueng Chuan** (100.0% isolated ownership) | Magnitude: 736.88

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

- `pyqtgraph/opengl/GLGraphicsItem.py` -> **Severity: 3.627** (Embedded: 0.0511 * Error Risk: 70.9845%)
- `pyqtgraph/graphicsItems/GraphicsObject.py` -> **Severity: 3.314** (Embedded: 0.0569 * Error Risk: 58.1937%)
- `pyqtgraph/parametertree/Parameter.py` -> **Severity: 2.194** (Embedded: 0.0371 * Error Risk: 59.1459%)
- `pyqtgraph/parametertree/ParameterItem.py` -> **Severity: 1.961** (Embedded: 0.0309 * Error Risk: 63.4437%)
- `pyqtgraph/parametertree/parameterTypes/basetypes.py` -> **Severity: 1.801** (Embedded: 0.0329 * Error Risk: 54.6872%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pyqtgraph/opengl/GLGraphicsItem.py` -> **Severity: 2956.551** (Blast Radius: 29.652 * Doc Risk: 99.7083%)
- `pyqtgraph/graphicsItems/GraphicsObject.py` -> **Severity: 2895.5** (Blast Radius: 28.955 * Doc Risk: 100.0%)
- `pyqtgraph/parametertree/ParameterItem.py` -> **Severity: 2256.902** (Blast Radius: 22.825 * Doc Risk: 98.8785%)
- `pyqtgraph/parametertree/parameterTypes/basetypes.py` -> **Severity: 2096.12** (Blast Radius: 23.969 * Doc Risk: 87.4513%)
- `pyqtgraph/Point.py` -> **Severity: 1724.42** (Blast Radius: 18.075 * Doc Risk: 95.4036%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
