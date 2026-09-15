# ARCHITECTURAL_BRIEF: openpyxl
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
| Total Artifacts | 197 |
| Analyzed Artifacts (Scanned) | 191 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6 |
| Total LOC | 19641 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 97.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3674 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3759 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.9311 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 16 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 190 | 19641 | 99.5% |
| PLAINTEXT | 1 | 0 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled App` (z +0.01; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 26%, Parameter Forwarders Files 22%, Many-Argument Workhorses Files 20%, Data / Markup / Trivial 11%, Interface Declarations Files 8%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 190 | 99.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6*

**Composition by Extension & Reason:**
- `.rst`: 3x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.py`: 1x Excluded (Saturation: Line 7 exceeds 500 chars)
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.8 | 30.4 | 36.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.8 | 82.1 | 94.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 19.3 | 2.5 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 37.3 | 38.8 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 87.1 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 7.4 | 0.1 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 88.4 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 69.4 | 93.2 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 191 | 68 | 3 | `openpyxl-3.1.5/openpyxl/worksheet/_reader.py` |
| cleanup | 15 | 7 | 0 | `openpyxl-3.1.5/openpyxl/worksheet/_writer.py` |
| guards | 522 | 97 | 8 | `openpyxl-3.1.5/openpyxl/worksheet/worksheet.py` |
| danger | 244 | 65 | 4 | `openpyxl-3.1.5/openpyxl/descriptors/base.py` |
| concurrency | 47 | 25 | 1 | `openpyxl-3.1.5/openpyxl/utils/dataframe.py` |
| connectivity | 1292 | 168 | 17 | `openpyxl-3.1.5/openpyxl/worksheet/worksheet.py` |
| io | 22 | 8 | 0 | `openpyxl-3.1.5/openpyxl/reader/excel.py` |
| crypto | 1 | 1 | 0 | `openpyxl-3.1.5/openpyxl/chartsheet/protection.py` |
| ipc | 0 | 0 | 0 | - |
| time | 24 | 8 | 0 | `openpyxl-3.1.5/openpyxl/utils/datetime.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 40 | 17 | 0 | `openpyxl-3.1.5/openpyxl/formula/tokenizer.py` |
| events | 25 | 2 | 0 | `openpyxl-3.1.5/openpyxl/worksheet/_writer.py` |
| tests | 0 | 0 | 0 | - |
| docs | 585 | 114 | 7 | `openpyxl-3.1.5/openpyxl/styles/builtins.py` |
| debt | 21 | 9 | 0 | `openpyxl-3.1.5/openpyxl/drawing/geometry.py` |
| mutation | 16889 | 172 | 160 | `openpyxl-3.1.5/openpyxl/pivot/table.py` |
| dead_code | 14 | 7 | 0 | `openpyxl-3.1.5/openpyxl/packaging/interface.py` |
| credential | 0 | 0 | 0 | - |
| threat | 308 | 73 | 5 | `openpyxl-3.1.5/openpyxl/descriptors/serialisable.py` |
| ml_ai | 5 | 3 | 0 | `openpyxl-3.1.5/openpyxl/_constants.py` |
| ui | 5 | 5 | 0 | `openpyxl-3.1.5/openpyxl/chart/marker.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.25**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `openpyxl-3.1.5/openpyxl/reader/excel.py` (Hits: 7)
- `openpyxl-3.1.5/openpyxl/worksheet/_writer.py` (Hits: 4)
- `openpyxl-3.1.5/setup.py` (Hits: 4)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **serialisable.py** (`openpyxl-3.1.5/openpyxl/descriptors/serialisable.py`) — 108 inbound connections
2. **descriptors.py** (`openpyxl-3.1.5/openpyxl/chart/descriptors.py`) — 105 inbound connections
3. **excel.py** (`openpyxl-3.1.5/openpyxl/descriptors/excel.py`) — 66 inbound connections
4. **nested.py** (`openpyxl-3.1.5/openpyxl/descriptors/nested.py`) — 40 inbound connections
5. **constants.py** (`openpyxl-3.1.5/openpyxl/xml/constants.py`) — 39 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **workbook.py** (`openpyxl-3.1.5/openpyxl/workbook/workbook.py`) — 31 outbound dependencies
2. **_reader.py** (`openpyxl-3.1.5/openpyxl/worksheet/_reader.py`) — 30 outbound dependencies
3. **worksheet.py** (`openpyxl-3.1.5/openpyxl/worksheet/worksheet.py`) — 26 outbound dependencies
4. **excel.py** (`openpyxl-3.1.5/openpyxl/reader/excel.py`) — 24 outbound dependencies
5. **plotarea.py** (`openpyxl-3.1.5/openpyxl/chart/plotarea.py`) — 19 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `to_tree` **(Many-Argument Workhorses)** (@ `openpyxl-3.1.5/openpyxl/descriptors/serialisable.py`) -> Impact: **49.6** | LOC: 52
- `translate_range` **(Many-Argument Workhorses)** (@ `openpyxl-3.1.5/openpyxl/formula/translate.py`) -> Impact: **48.6** | LOC: 33
  * *Intent:* """ Translate an A1-style range reference to the destination cell. `rdelta`: the row offset to add to the range `cdelta`: the column offset to add to ...
- `__new__` **(Defensive Guards)** (@ `openpyxl-3.1.5/openpyxl/descriptors/__init__.py`) -> Impact: **39.8** | LOC: 36
- `from_tree` **(Defensive Guards)** (@ `openpyxl-3.1.5/openpyxl/descriptors/serialisable.py`) -> Impact: **39.2** | LOC: 57
  * *Intent:* """ Create object from XML """
- `parse_cell` **(Compute Cores)** (@ `openpyxl-3.1.5/openpyxl/worksheet/_reader.py`) -> Impact: **37.4** | LOC: 56
- `_cells_by_row` **(Many-Argument Workhorses)** (@ `openpyxl-3.1.5/openpyxl/worksheet/_read_only.py`) -> Impact: **36.5** | LOC: 43
  * *Intent:* """ The source worksheet file may have columns or rows missing. Missing cells will be created. """
- `from_ISO8601` **(Compute Cores)** (@ `openpyxl-3.1.5/openpyxl/utils/datetime.py`) -> Impact: **36.1** | LOC: 44
  * *Intent:* """Convert from a timestamp string to a datetime object. According to 18.17.4 in the specification the following ISO 8601 formats are supported. Dates...
- `lxml_write_cell` **(Many-Argument Workhorses)** (@ `openpyxl-3.1.5/openpyxl/cell/_writer.py`) -> Impact: **35.6** | LOC: 42
- `etree_write_cell` **(Many-Argument Workhorses)** (@ `openpyxl-3.1.5/openpyxl/cell/_writer.py`) -> Impact: **31.2** | LOC: 42
- `__init__` **(Many-Argument Workhorses)** (@ `openpyxl-3.1.5/openpyxl/styles/fonts.py`) -> Impact: **29.6** | LOC: 30

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `openpyxl-3.1.5/openpyxl/worksheet` | 32 | 4964.88 | 30.34% | 5.62% |
| `openpyxl-3.1.5/openpyxl/drawing` | 16 | 2610.86 | 36.29% | 5.62% |
| `openpyxl-3.1.5/openpyxl/chart` | 34 | 2381.28 | 24.47% | 0.0% |
| `openpyxl-3.1.5/openpyxl/styles` | 16 | 1871.62 | 42.09% | 0.0% |
| `openpyxl-3.1.5/openpyxl/pivot` | 5 | 1708.76 | 31.88% | 15.87% |
| `openpyxl-3.1.5/openpyxl/workbook` | 12 | 1300.42 | 20.26% | 0.0% |
| `openpyxl-3.1.5/openpyxl/descriptors` | 9 | 1059.98 | 51.57% | 6.92% |
| `openpyxl-3.1.5/openpyxl/cell` | 6 | 879.54 | 54.86% | 0.0% |
| `openpyxl-3.1.5/openpyxl/packaging` | 8 | 817.62 | 28.7% | 12.5% |
| `openpyxl-3.1.5/openpyxl/utils` | 11 | 772.48 | 26.18% | 14.52% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `openpyxl-3.1.5/openpyxl/packaging/interface.py` -> **99.9972%** Exposure
- `openpyxl-3.1.5/openpyxl/utils/inference.py` -> **98.9013%** Exposure
- `openpyxl-3.1.5/openpyxl/worksheet/page.py` -> **85.7768%** Exposure
- `openpyxl-3.1.5/openpyxl/pivot/fields.py` -> **79.35%** Exposure
- `openpyxl-3.1.5/openpyxl/worksheet/filters.py` -> **63.0574%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `openpyxl-3.1.5/openpyxl/cell/_writer.py` -> **100.0%** Exposure
- `openpyxl-3.1.5/openpyxl/cell/cell.py` -> **100.0%** Exposure
- `openpyxl-3.1.5/openpyxl/cell/rich_text.py` -> **100.0%** Exposure
- `openpyxl-3.1.5/openpyxl/cell/text.py` -> **100.0%** Exposure
- `openpyxl-3.1.5/openpyxl/chart/_3d.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `openpyxl-3.1.5/openpyxl/packaging/interface.py` -> **6** Orphaned Functions | **0** Duplicates
- `openpyxl-3.1.5/openpyxl/drawing/geometry.py` -> **0** Orphaned Functions | **4** Duplicates
- `openpyxl-3.1.5/openpyxl/pivot/fields.py` -> **0** Orphaned Functions | **4** Duplicates
- `openpyxl-3.1.5/openpyxl/worksheet/filters.py` -> **0** Orphaned Functions | **4** Duplicates
- `openpyxl-3.1.5/openpyxl/utils/inference.py` -> **3** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `746` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `openpyxl-3.1.5/openpyxl/descriptors/serialisable.py` (PYTHON) -> Cumulative Risk: **696.37**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.15)
- **Magnitude:** 343.26 | **LOC:** 241 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.4514%), Documentation (92.3077%)
- **Heaviest Functions:** `to_tree` (Many-Argument Workhorses, Impact: 49.6), `from_tree` (Defensive Guards, Impact: 39.2), `__add__` (Compute Cores, Impact: 16.3)

### 2. `openpyxl-3.1.5/openpyxl/worksheet/filters.py` (PYTHON) -> Cumulative Risk: **693.37**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.32)
- **Magnitude:** 360.02 | **LOC:** 487 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.8119%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Many-Argument Workhorses, Impact: 20.1), `to_tree` (Compute Cores, Impact: 7.0), `_guess_operator` (Compute Cores, Impact: 6.4)

### 3. `openpyxl-3.1.5/openpyxl/drawing/text.py` (PYTHON) -> Cumulative Risk: **676.01**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Parameter Forwarders Files` (z +1.55)
- **Magnitude:** 442.22 | **LOC:** 718 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.3999%)
- **Heaviest Functions:** `__init__` (Many-Argument Workhorses, Impact: 10.7), `__init__` (Many-Argument Workhorses, Impact: 8.4), `__init__` (Many-Argument Workhorses, Impact: 7.9)

### 4. `openpyxl-3.1.5/openpyxl/styles/styleable.py` (PYTHON) -> Cumulative Risk: **658.47**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.19)
- **Magnitude:** 183.28 | **LOC:** 152 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.3087%)
- **Heaviest Functions:** `__set__` (Defensive Guards, Impact: 18.9), `__set__` (Compute Cores, Impact: 8.5), `__get__` (Compute Cores, Impact: 6.4)

### 5. `openpyxl-3.1.5/openpyxl/styles/colors.py` (PYTHON) -> Cumulative Risk: **653.94**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.58)
- **Magnitude:** 148.84 | **LOC:** 173 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.1201%), Documentation (90.4762%)
- **Heaviest Functions:** `__init__` (Many-Argument Workhorses, Impact: 18.8), `__set__` (Compute Cores, Impact: 10.4), `__iter__` (Interface Declarations, Impact: 4.5)

### 6. `openpyxl-3.1.5/openpyxl/workbook/child.py` (PYTHON) -> Cumulative Risk: **653.14**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.14)
- **Magnitude:** 154.86 | **LOC:** 167 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (95.7793%), Documentation (90.0%)
- **Heaviest Functions:** `avoid_duplicate_name` (Compute Cores, Impact: 18.3), `title` (Defensive Guards, Impact: 17.1), `__init__` (Encapsulated Accessors, Impact: 4.2)

### 7. `openpyxl-3.1.5/openpyxl/pivot/table.py` (PYTHON) -> Cumulative Risk: **651.79**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.38)
- **Magnitude:** 833.56 | **LOC:** 1262 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.3109%), Documentation (81.6327%)
- **Heaviest Functions:** `__init__` (Many-Argument Workhorses, Impact: 18.1), `__init__` (Many-Argument Workhorses, Impact: 12.4), `by_priority` (Compute Cores, Impact: 7.9)

### 8. `openpyxl-3.1.5/openpyxl/drawing/geometry.py` (PYTHON) -> Cumulative Risk: **641.64**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Parameter Forwarders Files` (z +1.21)
- **Magnitude:** 296.5 | **LOC:** 585 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Safety Score (92.4038%)
- **Heaviest Functions:** `__init__` (Many-Argument Workhorses, Impact: 4.3), `__init__` (Many-Argument Workhorses, Impact: 3.8), `__init__` (Many-Argument Workhorses, Impact: 3.8)

### 9. `openpyxl-3.1.5/openpyxl/pivot/cache.py` (PYTHON) -> Cumulative Risk: **639.3**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +1.20)
- **Magnitude:** 604.6 | **LOC:** 966 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (96.6139%), Documentation (94.5946%), State Flux (85.0%)
- **Heaviest Functions:** `__init__` (Many-Argument Workhorses, Impact: 8.5), `__init__` (Many-Argument Workhorses, Impact: 7.8), `__init__` (Many-Argument Workhorses, Impact: 6.2)

### 10. `openpyxl-3.1.5/openpyxl/worksheet/_reader.py` (PYTHON) -> Cumulative Risk: **636.17**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.14)
- **Magnitude:** 534.5 | **LOC:** 473 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.4592%), Documentation (85.1852%)
- **Heaviest Functions:** `parse_cell` (Compute Cores, Impact: 37.4), `parse_row` (Defensive Guards, Impact: 16.7), `parse_formula` (Compute Cores, Impact: 13.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `openpyxl-3.1.5/openpyxl/pivot/table.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 833.56 | **LOC:** 1262 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.6374%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 18.1)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 12.4)
  * `by_priority` **(Compute Cores)** (Impact: 7.9)
    * *Intent:* """ Return a dictionary of format objects keyed by (field id and format property). This can be used ...
  * `_write_rels` **(Many-Argument Workhorses)** (Impact: 6.8)
    * *Intent:* """ Write the relevant child objects and add links """
  * `__init__` **(Many-Argument Workhorses)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 630
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 107`, `args: 38`, `func_start: 38`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 600`
* *Architecture:* `api: 35`, `import: 10`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.958
  * `Choke Point (Betweenness):` 0.000124 | `Ripple Effect (Closeness):` 0.007018
  * `Imports (Out-Degree: 9):` .fields, collections, openpyxl.descriptors, openpyxl.descriptors.excel, openpyxl.descriptors.sequence, openpyxl.descriptors.serialisable, openpyxl.packaging.relationship, openpyxl.worksheet.filters...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/worksheet.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 815.74 | **LOC:** 908 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.8262%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `append` **(Defensive Guards)** (Impact: 23.1)
    * *Intent:* """Appends a group of values at the bottom of the current sheet. * If it's a list: all values are ad...
  * `__getitem__` **(Compute Cores)** (Impact: 22.7)
    * *Intent:* """Convenience access by Excel style coordinates The key can be a single cell coordinate 'A1', a ran...
  * `move_range` **(Many-Argument Workhorses)** (Impact: 21.0)
    * *Intent:* """ Move a cell range by the number of rows and/or columns: down if rows > 0 and up if rows < 0 righ...
  * `_move_cells` **(Many-Argument Workhorses)** (Impact: 20.9)
    * *Intent:* """ Move either rows or columns around by the offset """
  * `iter_rows` **(Many-Argument Workhorses)** (Impact: 20.4)
    * *Intent:* """ Produces cells from the worksheet, by row. Specify the iteration range using indices of rows and...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 101 instances
* *State Mutation (weighted view):* 382
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 161`, `args: 60`, `func_start: 60`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 180`
* *Architecture:* `api: 48`, `import: 26`
* *Defense:* `safety: 13`, `doc: 46`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.283
  * `Choke Point (Betweenness):` 0.025853 | `Ripple Effect (Closeness):` 0.052074
  * `Imports (Out-Degree: 14):` .cell_range, .datavalidation, .dimensions, .filters, .formula, .merge, .page, .pagebreak...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/pivot/cache.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 604.6 | **LOC:** 966 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.7471%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 8.5)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 7.8)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 6.2)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 5.7)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 446
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 89`, `args: 33`, `func_start: 33`, `class_start: 27`
* *Risk/State:* `state_mutation: 442`
* *Architecture:* `api: 31`, `import: 10`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.007
  * `Choke Point (Betweenness):` 7.2e-05 | `Ripple Effect (Closeness):` 0.005263
  * `Imports (Out-Degree: 9):` .fields, .table, openpyxl.descriptors, openpyxl.descriptors.excel, openpyxl.descriptors.nested, openpyxl.descriptors.sequence, openpyxl.descriptors.serialisable, openpyxl.packaging.relationship...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/_reader.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 534.5 | **LOC:** 473 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.6915%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_cell` **(Compute Cores)** (Impact: 37.4)
  * `parse_row` **(Defensive Guards)** (Impact: 16.7)
  * `parse_formula` **(Compute Cores)** (Impact: 13.4)
    * *Intent:* """ possible formulae types: shared, array, datatable """
  * `bind_hyperlinks` **(Defensive Guards)** (Impact: 12.2)
  * `parse` **(Compute Cores)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 323
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 102`, `args: 27`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 157`
* *Architecture:* `api: 26`, `import: 30`
* *Defense:* `safety: 9`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.388
  * `Choke Point (Betweenness):` 0.001881 | `Ripple Effect (Closeness):` 0.014035
  * `Imports (Out-Degree: 20):` .datavalidation, .dimensions, .filters, .formula, .header_footer, .hyperlink, .merge, .page...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/drawing/text.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 442.22 | **LOC:** 718 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.7023%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 10.7)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 8.4)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 7.9)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 6.0)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 339
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 69`, `args: 19`, `func_start: 19`, `class_start: 19`
* *Risk/State:* `state_mutation: 325`
* *Architecture:* `api: 19`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.603
  * `Choke Point (Betweenness):` 0.000401 | `Ripple Effect (Closeness):` 0.047595
  * `Imports (Out-Degree: 8):` .colors, .effect, .fill, .geometry, openpyxl.descriptors, openpyxl.descriptors.excel, openpyxl.descriptors.nested, openpyxl.descriptors.serialisable...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/formula/tokenizer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 418.6 | **LOC:** 447 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.5676%), Tech Debt (10.8337%)
**Top Internal Functions/Classes:**
  * `_parse_string` **(Compute Cores)** (Impact: 22.6)
    * *Intent:* """ Parse a "-delimited string or '-delimited link. The offset must be pointing to either a single q...
  * `_parse_operator` **(Compute Cores)** (Impact: 20.2)
    * *Intent:* """ Consume the characters constituting an operator. Returns the number of characters consumed. (Doe...
  * `_parse` **(Compute Cores)** (Impact: 17.5)
    * *Intent:* """Populate self.items with the tokens from the formula."""
  * `make_subexp` **(Defensive Guards)** (Impact: 17.0)
    * *Intent:* """ Create a subexpression token. `value`: The value of the token `func`: If True, force the token t...
  * `_parse_separator` **(Defensive Guards)** (Impact: 9.7)
    * *Intent:* """ Consumes a ; or , character. Returns the number of characters consumed. (Does not update self.of...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 70 instances
* *State Mutation (weighted view):* 238
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 74`, `args: 20`, `func_start: 20`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 98`, `planned_debt: 1`
* *Architecture:* `api: 12`, `import: 1`
* *Defense:* `safety: 17`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.03899
  * `Imports (Out-Degree: 0):` re
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/drawing/spreadsheet_drawing.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 371.74 | **LOC:** 383 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.6072%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_write` **(Defensive Guards)** (Impact: 18.6)
    * *Intent:* """ create required structure and the serialise """
  * `_blip_rels` **(Compute Cores)** (Impact: 12.2)
    * *Intent:* """ Get relationship information for each blip and bind anchor to it Images that are not part of the...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 8.0)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 7.3)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 258
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 70`, `args: 17`, `func_start: 17`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 146`
* *Architecture:* `api: 13`, `import: 17`
* *Defense:* `safety: 7`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.876
  * `Choke Point (Betweenness):` 0.016247 | `Ripple Effect (Closeness):` 0.037594
  * `Imports (Out-Degree: 14):` .connector, .fill, .geometry, .graphic, .picture, .relation, .xdr, openpyxl.chart._chart...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/filters.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 360.02 | **LOC:** 487 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.7996%), Tech Debt (63.0574%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 20.1)
  * `to_tree` **(Compute Cores)** (Impact: 7.0)
  * `_guess_operator` **(Compute Cores)** (Impact: 6.4)
  * `convert` **(Type Conversions)** (Impact: 4.8)
    * *Intent:* """Convert to more specific filter"""
  * `_get_subtype` **(Defensive Guards)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 230
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 72`, `args: 28`, `func_start: 28`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 166`, `duplicate_logic: 4`
* *Architecture:* `api: 22`, `import: 6`
* *Defense:* `safety: 2`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.616
  * `Choke Point (Betweenness):` 0.00027 | `Ripple Effect (Closeness):` 0.04941
  * `Imports (Out-Degree: 4):` openpyxl.descriptors, openpyxl.descriptors.excel, openpyxl.descriptors.sequence, openpyxl.descriptors.serialisable, openpyxl.utils, re
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/descriptors/serialisable.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 343.26 | **LOC:** 241 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.8598%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `to_tree` **(Many-Argument Workhorses)** (Impact: 49.6)
  * `from_tree` **(Defensive Guards)** (Impact: 39.2)
    * *Intent:* """ Create object from XML """
  * `__add__` **(Compute Cores)** (Impact: 16.3)
  * `__iter__` **(Compute Cores)** (Impact: 11.9)
  * `__eq__` **(Type Conversions)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 59 instances
* *State Mutation (weighted view):* 185
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 48`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 67`
* *Architecture:* `api: 11`, `import: 8`
* *Defense:* `safety: 13`, `doc: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 76.719
  * `Choke Point (Betweenness):` 0.012895 | `Ripple Effect (Closeness):` 0.584563
  * `Imports (Out-Degree: 3):` , .namespace, .sequence, copy, keyword, openpyxl.compat, openpyxl.xml.functions
  * `Imported By (In-Degree: 108):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/_writer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 334.58 | **LOC:** 391 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.5814%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `write_row` **(Many-Argument Workhorses)** (Impact: 14.3)
  * `write_tables` **(Defensive Guards)** (Impact: 11.0)
  * `get_stream` **(Defensive Guards)** (Impact: 7.8)
  * `write_formatting` **(Compute Cores)** (Impact: 7.5)
  * `write_hyperlinks` **(Compute Cores)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 84`, `args: 34`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 62`, `dead_code: 1`
* *Architecture:* `io: 4`, `api: 35`, `import: 17`
* *Defense:* `safety: 5`, `doc: 10`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.957
  * `Choke Point (Betweenness):` 0.00039 | `Ripple Effect (Closeness):` 0.007018
  * `Imports (Out-Degree: 10):` .dimensions, .hyperlink, .merge, .related, .table, atexit, collections, io...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/workbook/workbook.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 325.14 | **LOC:** 439 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.3845%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `active` **(Defensive Guards)** (Impact: 11.3)
    * *Intent:* """Set the active sheet"""
  * `_add_sheet` **(Defensive Guards)** (Impact: 10.7)
    * *Intent:* """Add an worksheet (at an optional index)."""
  * `_duplicate_name` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* """ Check for duplicate name in defined name list and table list of each worksheet. Names are not ca...
  * `mime_type` **(Compute Cores)** (Impact: 9.0)
    * *Intent:* """ The mime type is determined by whether a workbook is a template or not and whether it contains m...
  * `create_sheet` **(Many-Argument Workhorses)** (Impact: 8.9)
    * *Intent:* """Create a worksheet (at an optional index). :param title: optional title of the sheet :type title:...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 132`, `args: 36`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 71`, `dead_code: 1`
* *Architecture:* `api: 35`, `import: 32`
* *Defense:* `safety: 9`, `doc: 27`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.833
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` .child, .defined_name, .properties, .protection, .views, copy, openpyxl.chartsheet, openpyxl.compat...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `openpyxl-3.1.5/openpyxl/worksheet/cell_range.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 325.06 | **LOC:** 513 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.4776%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 18.0)
  * `__ne__` **(Defensive Guards)** (Impact: 7.9)
    * *Intent:* """ Test whether the ranges are not equal. :type other: openpyxl.worksheet.cell_range.CellRange :par...
  * `isdisjoint` **(Compute Cores)** (Impact: 7.8)
    * *Intent:* """ Return ``True`` if this range has no cell in common with *other*. Ranges are disjoint if and onl...
  * `_check_title` **(Defensive Guards)** (Impact: 7.5)
    * *Intent:* """ Check whether comparisons between ranges are possible. Cannot compare ranges from different work...
  * `add` **(Defensive Guards)** (Impact: 7.5)
    * *Intent:* """ Add a cell coordinate or CellRange """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 102`, `args: 45`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `state_mutation: 50`
* *Architecture:* `api: 27`, `import: 8`
* *Defense:* `safety: 9`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.832
  * `Choke Point (Betweenness):` 0.000549 | `Ripple Effect (Closeness):` 0.06281
  * `Imports (Out-Degree: 3):` copy, itertools, openpyxl.descriptors, openpyxl.descriptors.sequence, openpyxl.descriptors.serialisable, openpyxl.utils, operator
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/reader/excel.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 323.82 | **LOC:** 350 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.6122%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `read_worksheets` **(Compute Cores)** (Impact: 29.1)
  * `_validate_archive` **(Compute Cores)** (Impact: 12.9)
    * *Intent:* """ Does a first check whether filename is a string or a file-like object. If it is a string represe...
  * `read_chartsheet` **(Many-Argument Workhorses)** (Impact: 9.0)
  * `_find_workbook_part` **(Compute Cores)** (Impact: 7.8)
  * `read_workbook` **(Compute Cores)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 60 instances
* *State Mutation (weighted view):* 213
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 77`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 93`
* *Architecture:* `io: 7`, `api: 12`, `import: 24`
* *Defense:* `safety: 8`, `doc: 5`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.353
  * `Choke Point (Betweenness):` 0.003091 | `Ripple Effect (Closeness):` 0.005263
  * `Imports (Out-Degree: 16):` ..tests, .drawings, .strings, .workbook, io, openpyxl.cell, openpyxl.chartsheet, openpyxl.comments.comment_sheet...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/styles/stylesheet.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 296.92 | **LOC:** 275 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.4484%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 20.0)
  * `_normalise_numbers` **(Compute Cores)** (Impact: 12.6)
    * *Intent:* """ Rebase custom numFmtIds with a floor of 164 when reading stylesheet And index datetime formats "...
  * `apply_stylesheet` **(Many-Argument Workhorses)** (Impact: 12.5)
    * *Intent:* """ Add styles to workbook if present """
  * `_expand_named_style` **(Compute Cores)** (Impact: 11.8)
    * *Intent:* """ Expand a named style reference element to a named style object by binding the relevant objects f...
  * `write_stylesheet` **(Compute Cores)** (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 204
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 57`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 92`
* *Architecture:* `api: 7`, `import: 19`
* *Defense:* `safety: 2`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.082
  * `Choke Point (Betweenness):` 0.000824 | `Ripple Effect (Closeness):` 0.014035
  * `Imports (Out-Degree: 14):` .borders, .builtins, .cell_style, .colors, .differential, .fills, .fonts, .named_styles...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/drawing/geometry.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 296.5 | **LOC:** 585 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (45.2071%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 4.3)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 3.8)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 3.8)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 3.5)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 69`, `args: 26`, `func_start: 26`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 191`, `duplicate_logic: 4`
* *Architecture:* `api: 27`, `import: 7`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.021
  * `Choke Point (Betweenness):` 0.00173 | `Ripple Effect (Closeness):` 0.108399
  * `Imports (Out-Degree: 6):` .line, openpyxl.descriptors, openpyxl.descriptors.excel, openpyxl.descriptors.serialisable, openpyxl.styles.colors, openpyxl.xml.constants
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/table.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 285.08 | **LOC:** 386 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.6699%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 13.6)
  * `get` **(Compute Cores)** (Impact: 8.3)
  * `_initialise_columns` **(Compute Cores)** (Impact: 6.3)
    * *Intent:* """ Create a list of table columns from a cell range Always set a ref if we have headers (the defaul...
  * `__set__` **(Compute Cores)** (Impact: 6.2)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 5.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 180
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 57`, `args: 20`, `func_start: 20`, `class_start: 8`
* *Risk/State:* `state_mutation: 140`
* *Architecture:* `api: 22`, `import: 10`
* *Defense:* `safety: 1`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.958
  * `Choke Point (Betweenness):` 0.000152 | `Ripple Effect (Closeness):` 0.007018
  * `Imports (Out-Degree: 9):` .filters, .related, openpyxl.descriptors, openpyxl.descriptors.excel, openpyxl.descriptors.sequence, openpyxl.descriptors.serialisable, openpyxl.utils, openpyxl.utils.escape...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/dimensions.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 281.38 | **LOC:** 307 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.3777%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 23.4)
  * `group` **(Many-Argument Workhorses)** (Impact: 18.4)
    * *Intent:* """allow grouping a range of consecutive rows or columns together :param start: first row or column ...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 17.4)
  * `to_tree` **(Compute Cores)** (Impact: 8.1)
  * `__iter__` **(Compute Cores)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 54`, `args: 19`, `func_start: 19`, `class_start: 6`
* *Risk/State:* `state_mutation: 87`
* *Architecture:* `api: 19`, `import: 9`
* *Defense:* `safety: 2`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.505
  * `Choke Point (Betweenness):` 0.007957 | `Ripple Effect (Closeness):` 0.04812
  * `Imports (Out-Degree: 6):` copy, openpyxl.compat, openpyxl.descriptors, openpyxl.descriptors.serialisable, openpyxl.styles.styleable, openpyxl.utils, openpyxl.utils.bound_dictionary, openpyxl.utils.units...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/cell/cell.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 274.7 | **LOC:** 333 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.591%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_bind_value` **(Defensive Guards)** (Impact: 20.5)
    * *Intent:* """Given a value, infer the correct data type"""
  * `hyperlink` **(Defensive Guards)** (Impact: 11.1)
    * *Intent:* """Set value and display for hyperlinks in a cell. Automatically sets the `value` of the cell with l...
  * `get_type` **(Defensive Guards)** (Impact: 11.0)
  * `comment` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* """ Assign a comment to a cell """
  * `get_time_format` **(Compute Cores)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 70`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `state_mutation: 68`
* *Architecture:* `api: 21`, `import: 11`
* *Defense:* `safety: 11`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.259
  * `Choke Point (Betweenness):` 0.002975 | `Ripple Effect (Closeness):` 0.039528
  * `Imports (Out-Degree: 6):` copy, datetime, openpyxl.cell.rich_text, openpyxl.compat, openpyxl.styles, openpyxl.styles.styleable, openpyxl.utils, openpyxl.utils.exceptions...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/chart/axis.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 268.74 | **LOC:** 402 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.51%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 10.3)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 4.4)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 4.1)
  * `from_tree` **(Parameter Forwarders)** (Impact: 3.9)
    * *Intent:* """ Special case value axes with no gridlines """
  * `__init__` **(Many-Argument Workhorses)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 213
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 40`, `args: 10`, `func_start: 10`, `class_start: 9`
* *Risk/State:* `state_mutation: 191`
* *Architecture:* `api: 9`, `import: 10`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.033
  * `Choke Point (Betweenness):` 0.001091 | `Ripple Effect (Closeness):` 0.045687
  * `Imports (Out-Degree: 8):` .descriptors, .layout, .shapes, .text, .title, openpyxl.descriptors, openpyxl.descriptors.excel, openpyxl.descriptors.nested...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/header_footer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 260.16 | **LOC:** 271 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.1659%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 25.9)
  * `from_str` **(Compute Cores)** (Impact: 10.9)
    * *Intent:* """ Convert from miniformat to object """
  * `__str__` **(Compute Cores)** (Impact: 9.9)
    * *Intent:* """ Pack parts into a single string """
  * `__init__` **(Many-Argument Workhorses)** (Impact: 9.4)
  * `from_tree` **(Compute Cores)** (Impact: 7.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 164
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 37`, `args: 13`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 76`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 2`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.531
  * `Choke Point (Betweenness):` 0.001303 | `Ripple Effect (Closeness):` 0.046093
  * `Imports (Out-Degree: 4):` openpyxl.descriptors, openpyxl.descriptors.serialisable, openpyxl.utils.escape, openpyxl.xml.functions, re, warnings
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/drawing/fill.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 255.88 | **LOC:** 426 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.6145%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 8.9)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 7.0)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 3.5)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 3.5)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 196
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 41`, `args: 11`, `func_start: 11`, `class_start: 11`
* *Risk/State:* `state_mutation: 186`
* *Architecture:* `api: 11`, `import: 9`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.2
  * `Choke Point (Betweenness):` 0.001162 | `Ripple Effect (Closeness):` 0.110266
  * `Imports (Out-Degree: 7):` .colors, .effect, openpyxl.descriptors, openpyxl.descriptors.excel, openpyxl.descriptors.nested, openpyxl.descriptors.sequence, openpyxl.descriptors.serialisable, openpyxl.xml.constants
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/drawing/colors.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 254.24 | **LOC:** 436 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.2483%), Tech Debt (10.8891%)
**Top Internal Functions/Classes:**
  * `__set__` **(Defensive Guards)** (Impact: 10.3)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 8.8)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 8.6)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 5.3)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 196
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 31`, `args: 7`, `func_start: 7`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 188`, `planned_debt: 2`
* *Architecture:* `api: 9`, `import: 7`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.861
  * `Choke Point (Betweenness):` 0.000414 | `Ripple Effect (Closeness):` 0.075521
  * `Imports (Out-Degree: 6):` openpyxl.descriptors, openpyxl.descriptors.excel, openpyxl.descriptors.nested, openpyxl.descriptors.serialisable, openpyxl.styles.colors, openpyxl.xml.constants
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/writer/excel.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 252.26 | **LOC:** 296 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.4638%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_write_worksheets` **(Compute Cores)** (Impact: 17.9)
  * `_write_comment` **(Compute Cores)** (Impact: 8.0)
  * `write_data` **(Compute Cores)** (Impact: 7.8)
  * `_merge_vba` **(Compute Cores)** (Impact: 7.8)
    * *Intent:* """ If workbook contains macros then extract associated files from cache of old file and add to arch...
  * `write_worksheet` **(Compute Cores)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 47`, `args: 13`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 79`
* *Architecture:* `api: 7`, `import: 15`
* *Defense:* `doc: 7`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.896
  * `Choke Point (Betweenness):` 0.001184 | `Ripple Effect (Closeness):` 0.005263
  * `Imports (Out-Degree: 13):` .theme, datetime, openpyxl.comments.comment_sheet, openpyxl.drawing.spreadsheet_drawing, openpyxl.packaging.extended, openpyxl.packaging.manifest, openpyxl.packaging.relationship, openpyxl.styles.stylesheet...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/utils/cell.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 250.62 | **LOC:** 241 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.9227%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `range_boundaries` **(Compute Cores)** (Impact: 24.7)
    * *Intent:* """ Convert a range string into a tuple of boundaries: (min_col, min_row, max_col, max_row) Cell coo...
  * `absolute_coordinate` **(Compute Cores)** (Impact: 12.1)
    * *Intent:* """Convert a coordinate to an absolute coordinate string (B12 -> $B$12)"""
  * `coordinate_from_string` **(Compute Cores)** (Impact: 10.5)
    * *Intent:* """Convert a coordinate string like 'B12' to a tuple ('B', 12)"""
  * `get_column_letter` **(Compute Cores)** (Impact: 8.6)
    * *Intent:* """ Convert decimal column position to its ASCII (base 26) form. Because column indices are 1-based,...
  * `get_column_interval` **(Defensive Guards)** (Impact: 7.5)
    * *Intent:* """ Given the start and end columns, return all the columns in the series. The start and end columns...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 32`, `args: 11`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 50`
* *Architecture:* `api: 11`, `import: 5`
* *Defense:* `safety: 4`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.622
  * `Choke Point (Betweenness):` 0.000585 | `Ripple Effect (Closeness):` 0.051982
  * `Imports (Out-Degree: 1):` .exceptions, functools, itertools, re, string
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/descriptors/base.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 244.36 | **LOC:** 273 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.2519%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__set__` **(Compute Cores)** (Impact: 18.6)
  * `__set__` **(Defensive Guards)** (Impact: 12.4)
  * `__set__` **(Compute Cores)** (Impact: 10.3)
  * `__set__` **(Compute Cores)** (Impact: 10.3)
  * `__set__` **(Compute Cores)** (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 64`, `args: 26`, `func_start: 26`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 32`
* *Architecture:* `api: 23`, `import: 5`
* *Defense:* `safety: 10`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 30.391
  * `Choke Point (Betweenness):` 0.003559 | `Ripple Effect (Closeness):` 0.280147
  * `Imports (Out-Degree: 2):` .namespace, datetime, openpyxl, openpyxl.utils.datetime, re
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `openpyxl-3.1.5/openpyxl/chart/_chart.py` -> **Severity: 3.053** (Bridge: 0.0305 * Flux: 100.0%)
- `openpyxl-3.1.5/openpyxl/worksheet/worksheet.py` -> **Severity: 2.585** (Bridge: 0.0259 * Flux: 100.0%)
- `openpyxl-3.1.5/openpyxl/chart/reference.py` -> **Severity: 2.184** (Bridge: 0.0218 * Flux: 100.0%)
- `openpyxl-3.1.5/openpyxl/drawing/spreadsheet_drawing.py` -> **Severity: 1.625** (Bridge: 0.0162 * Flux: 100.0%)
- `openpyxl-3.1.5/openpyxl/descriptors/serialisable.py` -> **Severity: 1.29** (Bridge: 0.0129 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `openpyxl-3.1.5/openpyxl/descriptors/serialisable.py` -> **Severity: 58.136** (Embedded: 0.5846 * Error Risk: 99.4514%)
- `openpyxl-3.1.5/openpyxl/chart/descriptors.py` -> **Severity: 45.599** (Embedded: 0.5659 * Error Risk: 80.5786%)
- `openpyxl-3.1.5/openpyxl/descriptors/nested.py` -> **Severity: 38.6** (Embedded: 0.3925 * Error Risk: 98.3374%)
- `openpyxl-3.1.5/openpyxl/xml/constants.py` -> **Severity: 37.453** (Embedded: 0.3805 * Error Risk: 98.4382%)
- `openpyxl-3.1.5/openpyxl/descriptors/excel.py` -> **Severity: 36.697** (Embedded: 0.384 * Error Risk: 95.5568%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `openpyxl-3.1.5/openpyxl/xml/functions.py` -> **Severity: 7409.1** (Blast Radius: 74.091 * Doc Risk: 100.0%)
- `openpyxl-3.1.5/openpyxl/descriptors/serialisable.py` -> **Severity: 7081.754** (Blast Radius: 76.719 * Doc Risk: 92.3077%)
- `openpyxl-3.1.5/openpyxl/chart/descriptors.py` -> **Severity: 6539.1** (Blast Radius: 65.391 * Doc Risk: 100.0%)
- `openpyxl-3.1.5/openpyxl/descriptors/nested.py` -> **Severity: 5007.2** (Blast Radius: 50.072 * Doc Risk: 100.0%)
- `openpyxl-3.1.5/openpyxl/chart/data_source.py` -> **Severity: 3198.2** (Blast Radius: 31.982 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
