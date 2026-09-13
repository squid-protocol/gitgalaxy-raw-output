# ARCHITECTURAL_BRIEF: pyqtgraph
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/pyqtgraph/pyqtgraph.git` |
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
| Total Artifacts | 795 |
| Analyzed Artifacts (Scanned) | 514 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 281 |
| Total LOC | 65541 |
| Volatility Index | 0.008 |
| % Scanned of codebase = | 64.7% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6881 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3573 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.7186 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 31 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 417 | 47494 | 81.1% |
| CSV | 69 | 17734 | 13.4% |
| PLAINTEXT | 11 | 0 | 2.1% |
| XML | 9 | 0 | 1.8% |
| MARKDOWN | 3 | 0 | 0.6% |
| SHELL | 1 | 3 | 0.2% |
| MAKEFILE | 1 | 120 | 0.2% |
| BATCH | 1 | 133 | 0.2% |
| CSS | 1 | 17 | 0.2% |
| C | 1 | 40 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 500 | 97.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 14 | 2.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 281*

**Composition by Extension & Reason:**
- `.rst`: 127x Excluded (Unsupported Extension: '.rst')
- `.png`: 90x Excluded (Explicitly Denied Extension: '.png')
- `.py`: 2x Excluded (Machine-Generated Source Code Signature: 80 LOC), 1x Excluded (Machine-Generated Source Code Signature: 64 LOC), 1x Excluded (Machine-Generated Source Code Signature: 208 LOC)
- `.ui`: 10x Excluded (Unsupported Extension: '.ui')
- `.yml`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dic`: 7x Excluded (Unsupported Extension: '.dic')
- `.ipynb`: 6x Excluded (Unsupported Extension: '.ipynb')
- `.cfg`: 3x Excluded (Unsupported Extension: '.cfg')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.graphml`: 2x Excluded (Unsupported Extension: '.graphml')
- `.svg`: 2x Excluded (Static Asset Blob without Intent: 1227 LOC)
- `.hex`: 2x Excluded (Unsupported Extension: '.hex')
- `.ini`: 2x Excluded (Unsupported Extension: '.ini')
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 86.7 | 28.5 | 29.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 66.3 | 85.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 5.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 17.0 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 20.0 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 37.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 67.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 18.8 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 93.1 | 4.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 55.2 | 71.3 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 903 | 160 | 5 | `pyqtgraph/functions.py` |
| cleanup | 67 | 40 | 0 | `pyqtgraph/multiprocess/processes.py` |
| guards | 2700 | 220 | 18 | `tests/parametertree/test_Parameter.py` |
| danger | 1370 | 280 | 7 | `pyqtgraph/__init__.py` |
| concurrency | 87 | 26 | 0 | `pyqtgraph/multiprocess/processes.py` |
| connectivity | 3895 | 340 | 21 | `pyqtgraph/graphicsItems/ROI.py` |
| io | 398 | 77 | 1 | `pyqtgraph/multiprocess/processes.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 40 | 8 | 0 | `pyqtgraph/multiprocess/processes.py` |
| time | 41 | 20 | 0 | `pyqtgraph/multiprocess/processes.py` |
| serialization | 8 | 6 | 0 | `pyqtgraph/multiprocess/bootstrap.py` |
| regex | 32 | 16 | 0 | `tools/setupHelpers.py` |
| events | 435 | 71 | 2 | `pyqtgraph/graphicsItems/GradientEditorItem.py` |
| tests | 404 | 71 | 2 | `tests/test_makeARGB.py` |
| docs | 1578 | 286 | 8 | `pyqtgraph/functions.py` |
| debt | 365 | 84 | 2 | `pyqtgraph/debug.py` |
| mutation | 26654 | 387 | 128 | `pyqtgraph/functions.py` |
| dead_code | 656 | 194 | 4 | `pyqtgraph/graphicsItems/GradientEditorItem.py` |
| credential | 0 | 0 | 0 | - |
| threat | 216 | 64 | 1 | `pyqtgraph/multiprocess/remoteproxy.py` |
| ml_ai | 225 | 195 | 1 | `pyqtgraph/functions.py` |
| ui | 25 | 15 | 0 | `pyqtgraph/graphicsItems/ImageItem.py` |

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

1. **GLGraphicsItem.py** (`pyqtgraph/opengl/GLGraphicsItem.py`) — 25 inbound connections
2. **GraphicsObject.py** (`pyqtgraph/graphicsItems/GraphicsObject.py`) — 24 inbound connections
3. **Point.py** (`pyqtgraph/Point.py`) — 20 inbound connections
4. **common.py** (`tests/opengl/items/common.py`) — 18 inbound connections
5. **basetypes.py** (`pyqtgraph/parametertree/parameterTypes/basetypes.py`) — 16 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`pyqtgraph/__init__.py`) — 91 outbound dependencies
2. **__init__.py** (`pyqtgraph/Qt/__init__.py`) — 30 outbound dependencies
3. **debug.py** (`pyqtgraph/debug.py`) — 22 outbound dependencies
4. **PlotItem.py** (`pyqtgraph/graphicsItems/PlotItem/PlotItem.py`) — 22 outbound dependencies
5. **__init__.py** (`pyqtgraph/parametertree/parameterTypes/__init__.py`) — 20 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `makeARGB` (@ `pyqtgraph/functions.py`) -> Impact: **195.8** | LOC: 182
  * *Intent:* """ Convert an array of values into an ARGB array suitable for building QImages, OpenGL textures, etc. Returns the ARGB array (unsigned byte) and a bo...
- `movePoint` (@ `pyqtgraph/graphicsItems/ROI.py`) -> Impact: **154.3** | LOC: 175
  * *Intent:* ## called by Handles when they are moved. ## pos is the new position of the handle in scene coords, as requested by the handle. if modifiers is None: ...
- `setRange` (@ `pyqtgraph/graphicsItems/ViewBox/ViewBox.py`) -> Impact: **143.2** | LOC: 149
  * *Intent:* """ Set the visible range of the ViewBox. Must specify at least one of *rect*, *xRange*, or *yRange*. ================== =============================...
- `setImage` (@ `pyqtgraph/imageview/ImageView.py`) -> Impact: **141.3** | LOC: 158
- `generateDrawSpecs` (@ `pyqtgraph/graphicsItems/AxisItem.py`) -> Impact: **136.0** | LOC: 295
  * *Intent:* """ Generate the drawing specifications for the axis, ticks, and labels. This method determines all the coordinates and other information needed to dr...
- `try_make_qimage` (@ `pyqtgraph/functions_qimage.py`) -> Impact: **130.2** | LOC: 145
  * *Intent:* """ Internal function to make an QImage from an ndarray without going through the full generality of makeARGB(). Only certain combinations of input ar...
- `correctCoordinates` (@ `pyqtgraph/exporters/SVGExporter.py`) -> Impact: **123.1** | LOC: 136
  * *Intent:* # correct the defs in the linearGradient for d in defs: if d.tagName == "linearGradient": # reset "gradientUnits" attribute to SVG default value d.rem...
- `setup` (@ `benchmarks/renderImageItem.py`) -> Impact: **115.1** | LOC: 82
- `setData` (@ `pyqtgraph/graphicsItems/PlotDataItem.py`) -> Impact: **114.7** | LOC: 173
- `updateViewRange` (@ `pyqtgraph/graphicsItems/ViewBox/ViewBox.py`) -> Impact: **112.5** | LOC: 129
  * *Intent:* # Including a prepareForPaint call is part of the Qt strategy to # defer expensive redraw opertions until requested by a 'sigPrepareForPaint' signal #...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pyqtgraph/graphicsItems` | 39 | 17033.54 | 46.03% | 5.59% |
| `pyqtgraph` | 20 | 7977.06 | 48.35% | 30.13% |
| `pyqtgraph/examples` | 116 | 5736.68 | 34.01% | 0.0% |
| `pyqtgraph/widgets` | 32 | 5324.34 | 49.83% | 5.75% |
| `pyqtgraph/graphicsItems/ViewBox` | 3 | 2540.76 | 46.88% | 3.29% |
| `pyqtgraph/opengl/items` | 14 | 1999.8 | 36.55% | 6.93% |
| `pyqtgraph/parametertree/parameterTypes` | 20 | 1796.4 | 35.39% | 0.65% |
| `pyqtgraph/multiprocess` | 5 | 1700.74 | 48.46% | 17.0% |
| `pyqtgraph/parametertree` | 5 | 1692.68 | 34.75% | 2.63% |
| `pyqtgraph/flowchart` | 5 | 1655.32 | 42.1% | 16.87% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `pyqtgraph/GraphicsScene/mouseEvents.py` -> **100.0%** Exposure
- `pyqtgraph/Qt/OpenGLHelpers.py` -> **99.9999%** Exposure
- `pyqtgraph/PlotData.py` -> **99.9996%** Exposure
- `pyqtgraph/exceptionHandling.py` -> **99.9983%** Exposure
- `pyqtgraph/flowchart/library/Display.py` -> **99.2255%** Exposure
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
- **Unknown Dependencies:** `1175` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `pyqtgraph/multiprocess/processes.py` (PYTHON) -> Cumulative Risk: **731.51**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 488.16 | **LOC:** 533 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9946%), Safety Score (98.3548%)
- **Heaviest Functions:** `__init__` (Impact: 73.0), `__init__` (Impact: 38.7), `startQtEventLoop` (Impact: 15.6)

### 2. `pyqtgraph/multiprocess/parallelizer.py` (PYTHON) -> Cumulative Risk: **712.59**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 272.76 | **LOC:** 342 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.8223%), Dead Code (85.0286%)
- **Heaviest Functions:** `runParallel` (Impact: 41.2), `__init__` (Impact: 19.0), `__exit__` (Impact: 13.0)

### 3. `pyqtgraph/widgets/RemoteGraphicsView.py` (PYTHON) -> Cumulative Risk: **699.05**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 310.34 | **LOC:** 324 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.8816%), Safety Score (94.5638%)
- **Heaviest Functions:** `__init__` (Impact: 15.6), `get_state` (Impact: 12.8), `renderView` (Impact: 11.8)

### 4. `pyqtgraph/multiprocess/remoteproxy.py` (PYTHON) -> Cumulative Risk: **697.98**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 879.72 | **LOC:** 1143 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (97.0071%), Safety Score (96.1233%)
- **Heaviest Functions:** `handleRequest` (Impact: 78.7), `send` (Impact: 51.3), `callObj` (Impact: 23.6)

### 5. `pyqtgraph/Qt/internals.py` (PYTHON) -> Cumulative Risk: **688.28**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 230.52 | **LOC:** 249 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.319%)
- **Heaviest Functions:** `__init__` (Impact: 19.4), `resize` (Impact: 18.9), `get_qpainterpath_element_array` (Impact: 15.2)

### 6. `pyqtgraph/flowchart/library/Display.py` (PYTHON) -> Cumulative Risk: **668.46**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 282.68 | **LOC:** 311 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.2255%), Safety Score (96.0157%)
- **Heaviest Functions:** `process` (Impact: 29.6), `updateKeys` (Impact: 23.8), `process` (Impact: 21.1)

### 7. `pyqtgraph/widgets/ColorMapMenu.py` (PYTHON) -> Cumulative Risk: **661.82**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 337.54 | **LOC:** 302 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.4039%), Documentation (97.2222%)
- **Heaviest Functions:** `__init__` (Impact: 32.8), `buildCetSubMenu` (Impact: 22.6), `buildUserSubMenu` (Impact: 12.7)

### 8. `pyqtgraph/widgets/ColorMapWidget.py` (PYTHON) -> Cumulative Risk: **660.73**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 254.6 | **LOC:** 275 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.109%), Documentation (81.25%)
- **Heaviest Functions:** `map` (Impact: 24.2), `addNew` (Impact: 16.9), `__init__` (Impact: 9.2)

### 9. `pyqtgraph/graphicsItems/PlotCurveItem.py` (PYTHON) -> Cumulative Risk: **660.04**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1484.36 | **LOC:** 1294 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.6896%), Verification (80.0%)
- **Heaviest Functions:** `paintGL` (Impact: 97.3), `paint` (Impact: 68.7), `dataBounds` (Impact: 64.0)

### 10. `pyqtgraph/graphicsItems/PColorMeshItem.py` (PYTHON) -> Cumulative Risk: **659.02**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 762.74 | **LOC:** 787 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.5807%), Churn (89.82%)
- **Heaviest Functions:** `paintGL` (Impact: 43.5), `_prepareData` (Impact: 31.0), `setup` (Impact: 31.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pyqtgraph/functions.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3051.84 | **LOC:** 3190 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (51.191%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `makeARGB` (Impact: 195.8)
    * *Intent:* """ Convert an array of values into an ARGB array suitable for building QImages, OpenGL textures, et...
  * `isocurve` (Impact: 97.2)
    * *Intent:* #for i in range(index.shape[0]): # data x-axis #for j in range(index.shape[1]): # data y-axis #for k...
  * `eq` (Impact: 68.7)
    * *Intent:* """The great missing equivalence function: Guaranteed evaluation to a single bool value. This functi...
  * `arrayToQPath` (Impact: 65.9)
    * *Intent:* """ Convert an array of x,y coordinates to QPainterPath as efficiently as possible. The *connect* ar...
  * `_pseudoScatterExact` (Impact: 45.8)
    * *Intent:* """Works by stacking points up one at a time, searching for the lowest position available at each po...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 541 instances
* *State Mutation (weighted view):* 1699
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 467`, `structural_boundaries: 237`, `args: 66`, `func_start: 64`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 617`, `dead_code: 22`
* *Architecture:* `io: 2`, `api: 57`, `import: 15`
* *Defense:* `safety: 51`, `doc: 55`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.725
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.011696
  * `Imports (Out-Degree: 2):` , .Qt, .util.cupy_helper, collections, debug, decimal, math, numpy...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/ROI.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2321.62 | **LOC:** 2385 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.5442%), Tech Debt (37.0369%)
**Top Internal Functions/Classes:**
  * `movePoint` (Impact: 154.3)
    * *Intent:* ## called by Handles when they are moved. ## pos is the new position of the handle in scene coords, ...
  * `mouseDragEvent` (Impact: 42.6)
  * `getArrayRegion` (Impact: 39.0)
    * *Intent:* """ Return the result of :meth:`~pyqtgraph.ROI.getArrayRegion` masked by the elliptical shape of the...
  * `setSize` (Impact: 30.3)
    * *Intent:* """ Set the ROI's size. =============== ============================================================...
  * `__init__` (Impact: 26.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 308 instances
* *State Mutation (weighted view):* 1096
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 316`, `structural_boundaries: 309`, `args: 151`, `func_start: 150`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 480`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 3`, `duplicate_logic: 5`
* *Architecture:* `io: 1`, `api: 141`, `import: 9`
* *Defense:* `safety: 11`, `doc: 54`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.513
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003899
  * `Imports (Out-Degree: 4):` .., ..Point, ..Qt, ..SRTTransform, .GraphicsObject, .UIGraphicsItem, math, numpy...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/ViewBox/ViewBox.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2303.68 | **LOC:** 1876 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (56.5885%), Tech Debt (9.86%)
**Top Internal Functions/Classes:**
  * `setRange` (Impact: 143.2)
    * *Intent:* """ Set the visible range of the ViewBox. Must specify at least one of *rect*, *xRange*, or *yRange*...
  * `updateViewRange` (Impact: 112.5)
    * *Intent:* # Including a prepareForPaint call is part of the Qt strategy to # defer expensive redraw opertions ...
  * `childrenBounds` (Impact: 108.0)
    * *Intent:* """Return the bounding range of all children. [[xmin, xmax], [ymin, ymax]] Values may be None if the...
  * `enableAutoRange` (Impact: 48.6)
    * *Intent:* """ Enable (or disable) auto-range for *axis*, which may be ViewBox.XAxis, ViewBox.YAxis, or ViewBox...
  * `mouseDragEvent` (Impact: 43.0)
    * *Intent:* ## if axis is specified, event will only affect that axis. ev.accept() ## we accept all buttons pos ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 323 instances
* *State Mutation (weighted view):* 1056
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 415`, `structural_boundaries: 223`, `args: 108`, `func_start: 107`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 410`, `dead_code: 11`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 104`, `import: 13`
* *Defense:* `safety: 27`, `doc: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.28
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ..., ...Point, ...Qt, ..GraphicsWidget, ..ItemGroup, .ViewBoxMenu, copy, math...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyqtgraph/graphicsItems/AxisItem.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1666.14 | **LOC:** 1780 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (47.7359%), Tech Debt (9.3363%)
**Top Internal Functions/Classes:**
  * `generateDrawSpecs` (Impact: 136.0)
    * *Intent:* """ Generate the drawing specifications for the axis, ticks, and labels. This method determines all ...
  * `tickSpacing` (Impact: 52.3)
    * *Intent:* """ Determine the spacing of ticks on the axis. This method is called whenever the axis needs to be ...
  * `__init__` (Impact: 44.7)
  * `_updateMaxTextSize` (Impact: 30.7)
    * *Intent:* ## Informs that the maximum tick size orthogonal to the axis has ## changed; we use this to decide w...
  * `setStyle` (Impact: 29.6)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.162
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.013104
  * `Imports (Out-Degree: 2):` .., ..Point, ..Qt, .GraphicsWidget, math, numpy, weakref
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/PlotCurveItem.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1484.36 | **LOC:** 1294 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (74.6599%), Tech Debt (11.1073%)
**Top Internal Functions/Classes:**
  * `paintGL` (Impact: 97.3)
  * `paint` (Impact: 68.7)
  * `dataBounds` (Impact: 64.0)
    * *Intent:* ## Need this to run as fast as possible. ## check cache first: cache = self._boundsCache[ax] if cach...
  * `updateData` (Impact: 64.0)
  * `arrayToLineSegments` (Impact: 58.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 257 instances
* *State Mutation (weighted view):* 840
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 114`, `args: 42`, `func_start: 42`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 326`, `dead_code: 12`, `fragile_debt: 2`
* *Architecture:* `api: 35`, `import: 12`
* *Defense:* `safety: 19`, `doc: 17`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.958
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.016472
  * `Imports (Out-Degree: 1):` .., ..Qt, .GraphicsObject, importlib, math, numpy, warnings
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/ScatterPlotItem.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1450.0 | **LOC:** 1242 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.2924%), Tech Debt (9.4207%)
**Top Internal Functions/Classes:**
  * `addPoints` (Impact: 80.0)
    * *Intent:* """ Add new points to the scatter plot. Arguments are the same as setData() """
  * `paint` (Impact: 35.3)
  * `dataBounds` (Impact: 35.2)
  * `setPointData` (Impact: 27.7)
  * `setSymbol` (Impact: 24.4)
    * *Intent:* """Set the symbol(s) used to draw each spot. If a list or array is provided, then the symbol for eac...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 224 instances
* *State Mutation (weighted view):* 754
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 144`, `args: 76`, `func_start: 75`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 306`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* `api: 60`, `import: 11`
* *Defense:* `safety: 35`, `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.65
  * `Choke Point (Betweenness):` 2e-05 | `Ripple Effect (Closeness):` 0.016244
  * `Imports (Out-Degree: 2):` .., ..Point, ..Qt, .GraphicsObject, collections, itertools, math, numpy...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `pyqtgraph/debug.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1404.62 | **LOC:** 1296 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.1837%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `objectSize` (Impact: 63.4)
    * *Intent:* """Guess how much memory an object is using"""
  * `findRefPath` (Impact: 57.5)
    * *Intent:* """Determine all paths of object references from startObj to endObj"""
  * `searchRefs` (Impact: 28.8)
    * *Intent:* """Pseudo-interactive function for tracing references backward. **Arguments:** obj: The initial obje...
  * `diff` (Impact: 27.5)
    * *Intent:* #self.newRefs.clear() #self.newRefs.update(refs) """ Compute all differences between the current obj...
  * `refPathString` (Impact: 26.6)
    * *Intent:* """Given a list of adjacent objects in a reference path, print the 'natural' path names (ie, attribu...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 213 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 689
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 246`, `args: 82`, `func_start: 80`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 263`, `dead_code: 15`
* *Architecture:* `io: 22`, `api: 72`, `concurrency: 6`, `import: 23`
* *Defense:* `safety: 55`, `doc: 42`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.254
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012183
  * `Imports (Out-Degree: 1):` .Qt, .util, .util.mutex, PyQt5, __future__, cProfile, contextlib, faulthandler...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/PlotDataItem.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1310.3 | **LOC:** 1890 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (53.5502%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setData` (Impact: 114.7)
  * `_getDisplayDataset` (Impact: 92.8)
    * *Intent:* """ Get data suitable for display as a :class:`PlotDataset`. Warnings -------- This method is not co...
  * `updateItems` (Impact: 39.6)
    * *Intent:* """ Update the displayed curve and scatter plot. This method is called internally to redraw the curv...
  * `dataType` (Impact: 25.2)
  * `viewRangeChanged` (Impact: 21.2)
    * *Intent:* # def viewTransformChanged(self): # """ view transform (and thus range) has changed, replot if neede...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 215 instances
* *State Mutation (weighted view):* 691
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 223`, `structural_boundaries: 131`, `args: 52`, `func_start: 52`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 261`, `dead_code: 8`
* *Architecture:* `api: 53`, `import: 12`
* *Defense:* `safety: 18`, `doc: 35`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.565
  * `Choke Point (Betweenness):` 6.5e-05 | `Ripple Effect (Closeness):` 0.011278
  * `Imports (Out-Degree: 3):` .., ..Qt, .GraphicsObject, .PlotCurveItem, .ScatterPlotItem, bisect, math, numpy...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/PlotItem/PlotItem.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1184.02 | **LOC:** 1646 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.6496%), Tech Debt (8.4793%)
**Top Internal Functions/Classes:**
  * `multiDataPlot` (Impact: 52.4)
    * *Intent:* """ Allow plotting multiple curves on the same plot in one call. Parameters ---------- x, y : array_...
  * `__init__` (Impact: 52.3)
  * `showAxes` (Impact: 47.3)
    * *Intent:* """ Convenience method for quickly configuring axis settings. Parameters ---------- selection : bool...
  * `setDownsampling` (Impact: 34.1)
    * *Intent:* """ Set the downsampling mode for the PlotItem. Downsampling reduces the number of samples drawn to ...
  * `addItem` (Impact: 30.6)
    * *Intent:* """ Add a :class:`~pyqtgraph.GraphicsItem` to the :class:`~pyqtgraph.ViewBox`. If the item has plot ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 133 instances
* *State Mutation (weighted view):* 448
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 179`, `args: 77`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 182`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 75`, `import: 24`
* *Defense:* `safety: 13`, `doc: 38`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.307
  * `Choke Point (Betweenness):` 0.000273 | `Ripple Effect (Closeness):` 0.011696
  * `Imports (Out-Degree: 9):` , ..., ...Qt, ...WidgetGroup, ...exporters, ...widgets.FileDialog, ..AxisItem, ..ButtonItem...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/ImageItem.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1071.28 | **LOC:** 1227 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.728%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getHistogram` (Impact: 64.0)
  * `setImage` (Impact: 59.7)
  * `render` (Impact: 51.2)
    * *Intent:* # Convert data to QImage for display. self._unrenderable = True if self.image is None or self.image....
  * `setOpts` (Impact: 36.5)
    * *Intent:* """ Set display and processing options for this ImageItem. :class:`~pyqtgraph.ImageItem` and :meth:`...
  * `drawAt` (Impact: 24.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 160 instances
* *State Mutation (weighted view):* 534
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 132`, `args: 49`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 214`, `dead_code: 2`
* *Architecture:* `io: 4`, `api: 47`, `import: 15`
* *Defense:* `safety: 10`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001949
  * `Imports (Out-Degree: 3):` .., ..Point, ..Qt, ..util.cupy_helper, .GraphicsObject, collections.abc, numpy, numpy.typing...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/flowchart/Flowchart.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 897.16 | **LOC:** 926 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.3176%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `process` (Impact: 36.6)
    * *Intent:* """ Process data through the flowchart, returning the output. Keyword arguments must be the names of...
  * `nodeOutputChanged` (Impact: 21.4)
    * *Intent:* """Triggered when a node's output values have changed. (NOT called during process()) Propagates new ...
  * `processOrder` (Impact: 19.2)
    * *Intent:* """Return the order of operations required to process this chart. The order returned should look lik...
  * `hoverOver` (Impact: 18.4)
    * *Intent:* #print "FlowchartWidget.hoverOver called." term = None for item in items: if item is self.hoverItem:...
  * `selectionChanged` (Impact: 16.8)
    * *Intent:* #print "FlowchartWidget.selectionChanged called." items = self._scene.selectedItems() #print " scene...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 129 instances
* *State Mutation (weighted view):* 444
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 158`, `args: 71`, `func_start: 69`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 186`, `dead_code: 5`
* *Architecture:* `io: 1`, `api: 70`, `import: 16`
* *Defense:* `safety: 30`, `doc: 19`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.28
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` , .., ..Qt, ..debug, ..graphicsItems.GraphicsObject, .Node, .Terminal, .library...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyqtgraph/multiprocess/remoteproxy.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 879.72 | **LOC:** 1143 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.8366%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleRequest` (Impact: 78.7)
    * *Intent:* """Handle a single request from the remote process. Blocks until a request is available."""
  * `send` (Impact: 51.3)
    * *Intent:* """Send a request or return packet to the remote process. Generally it is not necessary to call this...
  * `callObj` (Impact: 23.6)
  * `getResult` (Impact: 21.0)
    * *Intent:* ## raises NoResultError if the result is not available yet #print self.results.keys(), os.getpid() w...
  * `result` (Impact: 19.6)
    * *Intent:* """ Return the result for this request. If block is True, wait until the result has arrived or *time...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 89 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 49
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 309
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 243`, `args: 93`, `func_start: 93`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 2`, `state_mutation: 131`, `dead_code: 6`
* *Architecture:* `io: 13`, `api: 85`, `concurrency: 9`, `import: 13`
* *Defense:* `safety: 29`, `doc: 22`, `sync_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.332
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005848
  * `Imports (Out-Degree: 0):` ..util, Request, a, builtins, from, new, numpy, os...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pyqtgraph/imageview/ImageView.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 866.14 | **LOC:** 946 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (46.873%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setImage` (Impact: 141.3)
  * `__init__` (Impact: 51.7)
  * `normalize` (Impact: 28.3)
    * *Intent:* """ Process *image* using the normalization options configured in the control panel. This can be rep...
  * `roiChanged` (Impact: 27.1)
    * *Intent:* # Extract image data from ROI if self.image is None: return image = self.getProcessedImage() # getAr...
  * `keyPressEvent` (Impact: 15.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 107 instances
* *State Mutation (weighted view):* 357
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 114`, `args: 40`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 143`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 40`, `import: 19`
* *Defense:* `safety: 8`, `doc: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.28
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` , .., ..Qt, ..SignalProxy, ..graphicsItems.GradientEditorItem, ..graphicsItems.ImageItem, ..graphicsItems.InfiniteLine, ..graphicsItems.LinearRegionItem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyqtgraph/colormap.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 861.46 | **LOC:** 847 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.154%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `map` (Impact: 37.2)
    * *Intent:* """ map(data, mode=ColorMap.BYTE) Returns an array of colors corresponding to a single value or an a...
  * `_getFromFile` (Impact: 30.7)
  * `getSubset` (Impact: 21.4)
    * *Intent:* """ Returns a new ColorMap object that extracts the subset specified by 'start' and 'length' to the ...
  * `getFromMatplotlib` (Impact: 20.6)
    * *Intent:* """ Generates a ColorMap object from a Matplotlib definition. Same as ``colormap.get(name, source='m...
  * `getStops` (Impact: 20.5)
    * *Intent:* """ Returns a tuple (stops, colors) containing a list of all stops (ranging 0.0 to 1.0) and a list o...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 155 instances
* *State Mutation (weighted view):* 499
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 108`, `args: 30`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 189`, `dead_code: 3`
* *Architecture:* `io: 1`, `api: 31`, `import: 9`
* *Defense:* `safety: 27`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001949
  * `Imports (Out-Degree: 0):` .Qt, .functions, collections.abc, colorcet, matplotlib.pyplot, numpy, os
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/GradientEditorItem.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 785.44 | **LOC:** 981 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.5139%), Tech Debt (11.4766%)
**Top Internal Functions/Classes:**
  * `getColor` (Impact: 38.9)
    * *Intent:* """ Return a color for a given value. ============== ===============================================...
  * `mouseClickEvent` (Impact: 14.4)
    * *Intent:* #return #pos = self.mapToScene(ev.pos()) #if ev.button() == QtCore.Qt.MouseButton.LeftButton and sel...
  * `setOrientation` (Impact: 12.2)
    * *Intent:* ## public """Set the orientation of the TickSliderItem. ============== =============================...
  * `mouseDragEvent` (Impact: 11.3)
  * `getLookupTable` (Impact: 11.2)
    * *Intent:* """ Return an RGB(A) lookup table (ndarray). ============== ========================================...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 106 instances
* *State Mutation (weighted view):* 375
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 123`, `args: 65`, `func_start: 62`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 163`, `dead_code: 23`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 60`, `import: 10`
* *Defense:* `safety: 2`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.953
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008122
  * `Imports (Out-Degree: 3):` .., ..Qt, ..colormap, ..widgets.ColorMapMenu, ..widgets.SpinBox, .GradientPresets, .GraphicsWidget, numpy...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/PColorMeshItem.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 762.74 | **LOC:** 787 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (57.8788%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `paintGL` (Impact: 43.5)
  * `_prepareData` (Impact: 31.0)
    * *Intent:* """ Check the shape of the data. Return a set of 2d array x, y, z ready to be used to draw the pictu...
  * `setup` (Impact: 31.0)
  * `paint` (Impact: 26.2)
  * `_drawPicture` (Impact: 21.7)
    * *Intent:* # on entry, the following members are all valid: x, y, z, levels # this function does not alter any ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 135 instances
* *State Mutation (weighted view):* 450
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 76`, `args: 29`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `state_mutation: 180`, `dead_code: 2`
* *Architecture:* `api: 27`, `import: 11`
* *Defense:* `safety: 4`, `doc: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001949
  * `Imports (Out-Degree: 1):` .., ..Qt, .GraphicsObject, enum, importlib, numpy
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/examples/relativity/relativity.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 740.34 | **LOC:** 763 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.7949%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `hypIntersect` (Impact: 24.4)
    * *Intent:* ## given a reference clock (seen from inertial frame) has rx, rt, and rv, ## and another clock start...
  * `runReference` (Impact: 21.9)
  * `getCurve` (Impact: 19.6)
  * `stepTo` (Impact: 15.4)
  * `runInertial` (Impact: 13.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 114 instances
* *State Mutation (weighted view):* 440
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 122`, `args: 44`, `func_start: 44`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 212`, `dead_code: 9`
* *Architecture:* `io: 9`, `api: 44`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.457
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003899
  * `Imports (Out-Degree: 1):` collections, numpy, os, pyqtgraph, pyqtgraph.Qt, pyqtgraph.console, pyqtgraph.parametertree, sys...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyqtgraph/parametertree/Parameter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 703.46 | **LOC:** 879 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (46.31%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `restoreState` (Impact: 43.4)
    * *Intent:* """ Restore the state of this parameter and its children from a structure generated using saveState(...
  * `insertChild` (Impact: 29.0)
    * *Intent:* """ Insert a new child at pos. If pos is a Parameter, then insert at the position of that Parameter....
  * `setName` (Impact: 18.0)
    * *Intent:* """Attempt to change the name of this parameter; return the actual name. (The parameter may reject t...
  * `setOpts` (Impact: 16.9)
    * *Intent:* """ Set any arbitrary options on this parameter. The exact behavior of this function will depend on ...
  * `saveState` (Impact: 16.8)
    * *Intent:* """ Return a structure representing the entire state of the parameter tree. The tree state may be re...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 282
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 161`, `args: 73`, `func_start: 73`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 118`, `dead_code: 5`
* *Architecture:* `api: 62`, `import: 7`
* *Defense:* `safety: 16`, `doc: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.475
  * `Choke Point (Betweenness):` 3.9e-05 | `Ripple Effect (Closeness):` 0.036604
  * `Imports (Out-Degree: 1):` .., ..Qt, .ParameterItem, collections, re, warnings, weakref
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `pyqtgraph/graphicsItems/InfiniteLine.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 702.18 | **LOC:** 622 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.9073%), Tech Debt (25.9453%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 47.2)
  * `setPos` (Impact: 29.3)
  * `__init__` (Impact: 23.9)
  * `addMarker` (Impact: 22.3)
    * *Intent:* """Add a marker to be displayed on the line. ============= =========================================...
  * `setHoverPen` (Impact: 15.0)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001949
  * `Imports (Out-Degree: 3):` .., ..Point, ..Qt, .GraphicsItem, .GraphicsObject, .TextItem, .ViewBox, math...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/flowchart/Terminal.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 640.66 | **LOC:** 584 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.1195%), Tech Debt (22.1238%)
**Top Internal Functions/Classes:**
  * `recolor` (Impact: 24.9)
  * `connectTo` (Impact: 23.4)
  * `mouseDragEvent` (Impact: 20.9)
  * `setValue` (Impact: 16.9)
    * *Intent:* """If this is a single-value terminal, val should be a single value. If this is a multi-value termin...
  * `__init__` (Impact: 12.3)
    * *Intent:* """ Construct a new terminal. ============== =======================================================...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 213
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 130`, `args: 72`, `func_start: 72`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 101`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 73`, `import: 5`
* *Defense:* `safety: 6`, `doc: 11`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.643
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001949
  * `Imports (Out-Degree: 2):` .., ..Point, ..Qt, ..graphicsItems.GraphicsObject, weakref
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/opengl/GLViewWidget.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 622.56 | **LOC:** 569 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (46.3784%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setCameraPosition` (Impact: 49.4)
  * `drawItemTree` (Impact: 25.6)
  * `pan` (Impact: 22.8)
    * *Intent:* """ Moves the center (look-at) position while holding the camera in place. ============== ==========...
  * `mouseMoveEvent` (Impact: 18.2)
  * `evalKeyState` (Impact: 15.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 84 instances
* *State Mutation (weighted view):* 311
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 83`, `args: 39`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 143`
* *Architecture:* `api: 37`, `import: 11`
* *Defense:* `safety: 13`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.28
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., ..Qt, OpenGL, importlib, math, numpy, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyqtgraph/examples/ExampleApp.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 614.86 | **LOC:** 606 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.0724%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `match_multiline` (Impact: 49.0)
    * *Intent:* """Do highlighting of multi-line strings. =========== ==============================================...
  * `keyPressEvent` (Impact: 17.0)
  * `highlightBlock` (Impact: 15.0)
    * *Intent:* """Apply syntax highlighting to the given block of text. """
  * `populateTree` (Impact: 14.9)
  * `getMatchingTitles` (Impact: 14.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 86 instances
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 344
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 75`, `args: 27`, `func_start: 27`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 3`, `state_mutation: 172`
* *Architecture:* `io: 13`, `api: 29`, `import: 14`
* *Defense:* `safety: 10`, `doc: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.546
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005848
  * `Imports (Out-Degree: 1):` argparse, collections, exampleLoaderTemplate_generic, functools, keyword, os, pkgutil, pyqtgraph...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pyqtgraph/parametertree/interactive.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 587.26 | **LOC:** 635 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.9693%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `interact` (Impact: 82.7)
  * `createFunctionParameter` (Impact: 23.0)
    * *Intent:* """ Constructs a dict ready for insertion into a group parameter based on the provided information i...
  * `functionToParameterDict` (Impact: 22.2)
    * *Intent:* """ Converts a function into a list of child parameter dicts """
  * `resolveAndHookupParameterChild` (Impact: 11.8)
  * `_nameToTitle` (Impact: 11.2)
    * *Intent:* """ Converts a function name to a title based on ``self.titleFormat``. Parameters ---------- name: s...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 289
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 90`, `args: 32`, `func_start: 32`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 115`, `dead_code: 1`
* *Architecture:* `api: 21`, `import: 7`
* *Defense:* `safety: 10`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001949
  * `Imports (Out-Degree: 0):` , .., .parameterTypes, contextlib, functools, inspect, pydoc
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/examples/optics/pyoptic.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 577.0 | **LOC:** 562 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (58.5129%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `intersectRay` (Impact: 27.0)
    * *Intent:* ## return the point of intersection and the angle of incidence #print "intersect ray" h = self.h2 r ...
  * `__init__` (Impact: 14.7)
    * *Intent:* """ Arguments for each surface are: x1,x2 - position of center of _physical surface_ r1,r2 - radius ...
  * `transmissionCurve` (Impact: 11.1)
  * `__init__` (Impact: 9.9)
  * `propagateRay` (Impact: 7.5)
    * *Intent:* """Refract, reflect, absorb, and/or scatter ray. This function may create and return new rays"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 337
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 97`, `args: 48`, `func_start: 48`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 149`, `dead_code: 1`, `fragile_debt: 3`, `duplicate_logic: 5`
* *Architecture:* `io: 3`, `api: 48`, `import: 8`
* *Defense:* `safety: 4`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.369
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001949
  * `Imports (Out-Degree: 0):` csv, gzip, math, numpy, os, pyqtgraph, pyqtgraph.Qt
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyqtgraph/opengl/MeshData.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 573.26 | **LOC:** 515 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.1298%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 24.3)
    * *Intent:* """ ============== ===================================================== **Arguments:** vertexes (Nv...
  * `setVertexes` (Impact: 16.7)
    * *Intent:* """ Set the array (Nv, 3) of vertex coordinates. If indexed=='faces', then the data must have shape ...
  * `vertexes` (Impact: 14.6)
    * *Intent:* """Return an array (N,3) of the positions of vertexes in the mesh. By default, each unique vertex ap...
  * `vertexNormals` (Impact: 13.5)
    * *Intent:* """ Return an array of normal vectors. By default, the array will be (N, 3) with one entry per uniqu...
  * `save` (Impact: 12.3)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.245
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007797
  * `Imports (Out-Degree: 0):` ..Qt, numpy, pickle
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `pyqtgraph/Qt/__init__.py` -> Churn: **93.08%** | Cog Load: 79.9177% | Debt: 0.0%
- `pyqtgraph/graphicsItems/PColorMeshItem.py` -> Churn: **89.82%** | Cog Load: 57.8788% | Debt: 0.0%
- `pyqtgraph/functions.py` -> Churn: **84.27%** | Cog Load: 51.191% | Debt: 0.0%
- `pyqtgraph/graphicsItems/PlotCurveItem.py` -> Churn: **74.83%** | Cog Load: 74.6599% | Debt: 11.1073%
- `pyqtgraph/Qt/OpenGLHelpers.py` -> Churn: **61.58%** | Cog Load: 81.1581% | Debt: 99.9999%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `pyqtgraph/graphicsItems/ViewBox/ViewBox.py` -> **Moritz Heinemann** (100.0% isolated ownership) | Magnitude: 2303.68
- `pyqtgraph/graphicsItems/PlotCurveItem.py` -> **KIU Shueng Chuan** (100.0% isolated ownership) | Magnitude: 1484.36
- `pyqtgraph/debug.py` -> **Luke Campagnola** (100.0% isolated ownership) | Magnitude: 1404.62
- `pyqtgraph/graphicsItems/PlotDataItem.py` -> **Ogi Moore** (100.0% isolated ownership) | Magnitude: 1310.3
- `pyqtgraph/graphicsItems/PColorMeshItem.py` -> **KIU Shueng Chuan** (100.0% isolated ownership) | Magnitude: 762.74

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pyqtgraph/graphicsItems/PlotItem/PlotItem.py` -> **Severity: 0.027** (Bridge: 0.0003 * Flux: 100.0%)
- `pyqtgraph/parametertree/parameterTypes/basetypes.py` -> **Severity: 0.024** (Bridge: 0.0002 * Flux: 99.9971%)
- `pyqtgraph/parametertree/parameterTypes/list.py` -> **Severity: 0.012** (Bridge: 0.0001 * Flux: 100.0%)
- `pyqtgraph/console/Console.py` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 100.0%)
- `pyqtgraph/graphicsItems/PlotDataItem.py` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pyqtgraph/opengl/GLGraphicsItem.py` -> **Severity: 4.734** (Embedded: 0.0506 * Error Risk: 93.4946%)
- `pyqtgraph/graphicsItems/GraphicsObject.py` -> **Severity: 4.047** (Embedded: 0.0565 * Error Risk: 71.6205%)
- `pyqtgraph/parametertree/Parameter.py` -> **Severity: 3.565** (Embedded: 0.0366 * Error Risk: 97.4059%)
- `pyqtgraph/parametertree/ParameterItem.py` -> **Severity: 2.693** (Embedded: 0.0303 * Error Risk: 88.7448%)
- `pyqtgraph/Point.py` -> **Severity: 2.649** (Embedded: 0.0456 * Error Risk: 58.0645%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pyqtgraph/graphicsItems/GraphicsObject.py` -> **Severity: 2916.7** (Blast Radius: 29.167 * Doc Risk: 100.0%)
- `pyqtgraph/examples/parametertree.py` -> **Severity: 1483.8** (Blast Radius: 14.838 * Doc Risk: 100.0%)
- `pyqtgraph/parametertree/parameterTypes/basetypes.py` -> **Severity: 1478.815** (Blast Radius: 23.042 * Doc Risk: 64.1791%)
- `pyqtgraph/Point.py` -> **Severity: 1422.72** (Blast Radius: 17.784 * Doc Risk: 80.0%)
- `pyqtgraph/parametertree/ParameterItem.py` -> **Severity: 1419.008** (Blast Radius: 22.172 * Doc Risk: 64.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
