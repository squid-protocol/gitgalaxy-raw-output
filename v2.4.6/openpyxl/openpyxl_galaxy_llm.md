# ARCHITECTURAL_BRIEF: openpyxl
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/openpyxl` |
| **Timestamp** | `2026-08-03T21:22:40.716552+00:00` |
| **Scan Duration** | `0.68s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 189 malicious artifacts.

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
| Total Artifacts | 197 |
| Analyzed Artifacts (Scanned) | 190 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7 |
| Total LOC | 19587 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 96.4% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3744 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3769 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.537 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 16 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 189 | 19587 | 99.5% |
| PLAINTEXT | 1 | 0 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.746`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 92 | 48.4% |
| file_cluster_8 | 90 | 47.4% |
| file_cluster_0 | 4 | 2.1% |
| file_cluster_7 | 2 | 1.1% |
| file_cluster_17 | 1 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7*

**Composition by Extension & Reason:**
- `.rst`: 3x Excluded (Unsupported Extension: '.rst')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 7 exceeds 500 chars)
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 98.8 | 20.9 | 17.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 14.2 | 12.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 51.3 | 82.4 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 36.7 | 2.8 | 80.0 |
| API Exposure | 0.0 | 14.0 | 3.3 | 2.9 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 73.2 | 98.7 | 0.0 |
| Commented Logic Exposure | 0.0 | 7.4 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 89.3 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 2.4 | 100.0 | 83.6 | 99.8 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 76.2 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 65.6 | 100.0 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `openpyxl-3.1.5/openpyxl/reader/excel.py` (Hits: 7)
- `openpyxl-3.1.5/setup.py` (Hits: 5)
- `openpyxl-3.1.5/openpyxl/worksheet/_writer.py` (Hits: 4)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **serialisable.py** (`openpyxl-3.1.5/openpyxl/descriptors/serialisable.py`) — 107 inbound connections
2. **descriptors.py** (`openpyxl-3.1.5/openpyxl/chart/descriptors.py`) — 104 inbound connections
3. **excel.py** (`openpyxl-3.1.5/openpyxl/descriptors/excel.py`) — 65 inbound connections
4. **nested.py** (`openpyxl-3.1.5/openpyxl/descriptors/nested.py`) — 39 inbound connections
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

- `to_tree` (@ `openpyxl-3.1.5/openpyxl/descriptors/serialisable.py`) -> Impact: **331.3** | LOC: 52
- `_parse_operator` (@ `openpyxl-3.1.5/openpyxl/formula/tokenizer.py`) -> Impact: **302.0** | LOC: 220
- `translate_range` (@ `openpyxl-3.1.5/openpyxl/formula/translate.py`) -> Impact: **283.0** | LOC: 26
- `__new__` (@ `openpyxl-3.1.5/openpyxl/descriptors/__init__.py`) -> Impact: **267.9** | LOC: 36
- `from_tree` (@ `openpyxl-3.1.5/openpyxl/descriptors/serialisable.py`) -> Impact: **221.0** | LOC: 56
- `lxml_write_cell` (@ `openpyxl-3.1.5/openpyxl/cell/_writer.py`) -> Impact: **158.6** | LOC: 42
- `__init__` (@ `openpyxl-3.1.5/openpyxl/worksheet/dimensions.py`) -> Impact: **154.2** | LOC: 32
- `_cells_by_row` (@ `openpyxl-3.1.5/openpyxl/worksheet/_read_only.py`) -> Impact: **131.7** | LOC: 41
- `read_worksheets` (@ `openpyxl-3.1.5/openpyxl/reader/excel.py`) -> Impact: **118.8** | LOC: 73
- `__init__` (@ `openpyxl-3.1.5/openpyxl/worksheet/dimensions.py`) -> Impact: **116.8** | LOC: 28

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `from_tree` (@ `openpyxl-3.1.5/openpyxl/chart/axis.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """ Special case value axes with no gridlines """
- `__new__` (@ `openpyxl-3.1.5/openpyxl/descriptors/__init__.py`) -> **O(2^N) [Recursive]**
- `to_tree` (@ `openpyxl-3.1.5/openpyxl/descriptors/serialisable.py`) -> **O(2^N) [Recursive]**
- `__setattr__` (@ `openpyxl-3.1.5/openpyxl/styles/proxy.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `openpyxl-3.1.5/openpyxl/worksheet/dimensions.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `openpyxl-3.1.5/openpyxl/worksheet/dimensions.py`) -> **O(2^N) [Recursive]**
- `from_tree` (@ `openpyxl-3.1.5/openpyxl/chart/plotarea.py`) -> **O(2^N) [Recursive]**
- `to_tree` (@ `openpyxl-3.1.5/openpyxl/chart/plotarea.py`) -> **O(2^N) [Recursive]**
- `deprecated` (@ `openpyxl-3.1.5/openpyxl/compat/__init__.py`) -> **O(2^N) [Recursive]**
- `__set__` (@ `openpyxl-3.1.5/openpyxl/descriptors/base.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `__init__` (@ `openpyxl-3.1.5/openpyxl/pivot/table.py`) -> DB Complexity: **87**
- `__init__` (@ `openpyxl-3.1.5/openpyxl/pivot/table.py`) -> DB Complexity: **50**
- `__init__` (@ `openpyxl-3.1.5/openpyxl/drawing/text.py`) -> DB Complexity: **40**
- `_setup` (@ `openpyxl-3.1.5/openpyxl/worksheet/worksheet.py`) -> DB Complexity: **32**
- `__init__` (@ `openpyxl-3.1.5/openpyxl/drawing/fill.py`) -> DB Complexity: **31**
- `__init__` (@ `openpyxl-3.1.5/openpyxl/drawing/colors.py`) -> DB Complexity: **30**
- `__init__` (@ `openpyxl-3.1.5/openpyxl/drawing/colors.py`) -> DB Complexity: **29**
- `__set__` (@ `openpyxl-3.1.5/openpyxl/chart/data_source.py`) -> DB Complexity: **28**
- `__init__` (@ `openpyxl-3.1.5/openpyxl/drawing/text.py`) -> DB Complexity: **28**
- `__init__` (@ `openpyxl-3.1.5/openpyxl/pivot/cache.py`) -> DB Complexity: **28**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `openpyxl-3.1.5/openpyxl/worksheet` | 32 | 5660.82 | 21.46% | 71.52% |
| `openpyxl-3.1.5/openpyxl/drawing` | 16 | 2393.16 | 25.61% | 74.69% |
| `openpyxl-3.1.5/openpyxl/descriptors` | 9 | 2319.55 | 29.45% | 44.44% |
| `openpyxl-3.1.5/openpyxl/chart` | 33 | 2122.58 | 17.54% | 55.39% |
| `openpyxl-3.1.5/openpyxl/styles` | 16 | 1852.76 | 27.07% | 49.4% |
| `openpyxl-3.1.5/openpyxl/workbook` | 12 | 1561.84 | 16.84% | 70.39% |
| `openpyxl-3.1.5/openpyxl/pivot` | 5 | 1296.26 | 21.32% | 79.52% |
| `openpyxl-3.1.5/openpyxl/cell` | 6 | 1146.14 | 41.68% | 65.76% |
| `openpyxl-3.1.5/openpyxl/packaging` | 8 | 947.82 | 19.05% | 49.72% |
| `openpyxl-3.1.5/openpyxl/formula` | 3 | 840.48 | 23.73% | 3.61% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `openpyxl-3.1.5/openpyxl/compat/singleton.py` -> **100.0%** Exposure
- `openpyxl-3.1.5/openpyxl/descriptors/base.py` -> **100.0%** Exposure
- `openpyxl-3.1.5/openpyxl/descriptors/nested.py` -> **100.0%** Exposure
- `openpyxl-3.1.5/openpyxl/descriptors/sequence.py` -> **100.0%** Exposure
- `openpyxl-3.1.5/openpyxl/styles/colors.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `openpyxl-3.1.5/openpyxl/chartsheet/chartsheet.py` -> **100.0%** Exposure
- `openpyxl-3.1.5/openpyxl/chartsheet/protection.py` -> **100.0%** Exposure
- `openpyxl-3.1.5/openpyxl/descriptors/__init__.py` -> **100.0%** Exposure
- `openpyxl-3.1.5/openpyxl/descriptors/slots.py` -> **100.0%** Exposure
- `openpyxl-3.1.5/openpyxl/drawing/drawing.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `openpyxl-3.1.5/openpyxl/pivot/table.py` -> **0** Orphaned Functions | **31** Duplicates
- `openpyxl-3.1.5/openpyxl/pivot/cache.py` -> **0** Orphaned Functions | **29** Duplicates
- `openpyxl-3.1.5/openpyxl/drawing/geometry.py` -> **0** Orphaned Functions | **26** Duplicates
- `openpyxl-3.1.5/openpyxl/descriptors/base.py` -> **0** Orphaned Functions | **22** Duplicates
- `openpyxl-3.1.5/openpyxl/drawing/effect.py` -> **0** Orphaned Functions | **19** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`openpyxl-3.1.5/openpyxl/cell/_writer.py`** -> AI Confidence: **99.31%**
2. **`openpyxl-3.1.5/openpyxl/descriptors/serialisable.py`** -> AI Confidence: **99.31%**
3. **`openpyxl-3.1.5/openpyxl/reader/excel.py`** -> AI Confidence: **99.24%**
4. **`openpyxl-3.1.5/openpyxl/worksheet/_reader.py`** -> AI Confidence: **99.24%**
5. **`openpyxl-3.1.5/openpyxl/worksheet/_writer.py`** -> AI Confidence: **99.24%**
6. **`openpyxl-3.1.5/openpyxl/worksheet/worksheet.py`** -> AI Confidence: **99.24%**
7. **`openpyxl-3.1.5/openpyxl/writer/excel.py`** -> AI Confidence: **99.24%**
8. **`openpyxl-3.1.5/openpyxl/chart/_chart.py`** -> AI Confidence: **99.18%**
9. **`openpyxl-3.1.5/openpyxl/chart/plotarea.py`** -> AI Confidence: **99.18%**
10. **`openpyxl-3.1.5/openpyxl/workbook/workbook.py`** -> AI Confidence: **99.18%**
11. **`openpyxl-3.1.5/openpyxl/worksheet/datavalidation.py`** -> AI Confidence: **99.18%**
12. **`openpyxl-3.1.5/openpyxl/worksheet/dimensions.py`** -> AI Confidence: **99.18%**
13. **`openpyxl-3.1.5/openpyxl/worksheet/table.py`** -> AI Confidence: **99.18%**
14. **`openpyxl-3.1.5/openpyxl/xml/functions.py`** -> AI Confidence: **99.18%**
15. **`openpyxl-3.1.5/openpyxl/cell/cell.py`** -> AI Confidence: **99.16%**
16. **`openpyxl-3.1.5/openpyxl/drawing/spreadsheet_drawing.py`** -> AI Confidence: **99.16%**
17. **`openpyxl-3.1.5/openpyxl/reader/workbook.py`** -> AI Confidence: **99.16%**
18. **`openpyxl-3.1.5/openpyxl/styles/fonts.py`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `openpyxl-3.1.5/openpyxl/cell/cell.py` -> **100.0%** Exposure
- `openpyxl-3.1.5/openpyxl/cell/read_only.py` -> **100.0%** Exposure
- `openpyxl-3.1.5/openpyxl/cell/rich_text.py` -> **100.0%** Exposure
- `openpyxl-3.1.5/openpyxl/cell/text.py` -> **100.0%** Exposure
- `openpyxl-3.1.5/openpyxl/chart/_3d.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `openpyxl-3.1.5/openpyxl/pivot/cache.py` -> **0.0325%** Exposure
### Algorithmic DoS Exposure
- `openpyxl-3.1.5/openpyxl/cell/cell.py` -> **100.0%** Exposure
- `openpyxl-3.1.5/openpyxl/cell/read_only.py` -> **100.0%** Exposure
- `openpyxl-3.1.5/openpyxl/cell/rich_text.py` -> **100.0%** Exposure
- `openpyxl-3.1.5/openpyxl/cell/text.py` -> **100.0%** Exposure
- `openpyxl-3.1.5/openpyxl/chart/_3d.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `742` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `openpyxl-3.1.5/openpyxl/descriptors/__init__.py` (PYTHON) -> Cumulative Risk: **910.28**
- **Archetype:** `file_cluster_13` (Distance: 13.483 IQR)
- **Magnitude:** 326.6 | **LOC:** 59 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `__new__` (Impact: 267.9), `__new__` (Impact: 33.8)

### 2. `openpyxl-3.1.5/openpyxl/drawing/drawing.py` (PYTHON) -> Cumulative Risk: **853.39**
- **Archetype:** `file_cluster_13` (Distance: 12.078 IQR)
- **Magnitude:** 134.44 | **LOC:** 93 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `set_dimension` (Impact: 30.6), `anchor` (Impact: 21.7), `width` (Impact: 10.6)

### 3. `openpyxl-3.1.5/openpyxl/cell/read_only.py` (PYTHON) -> Cumulative Risk: **826.57**
- **Archetype:** `file_cluster_0` (Distance: 10.029 IQR)
- **Magnitude:** 130.1 | **LOC:** 137 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9999%)
- **Heaviest Functions:** `value` (Impact: 14.1), `number_format` (Impact: 13.3), `__eq__` (Impact: 13.2)

### 4. `openpyxl-3.1.5/openpyxl/worksheet/protection.py` (PYTHON) -> Cumulative Risk: **812.25**
- **Archetype:** `file_cluster_13` (Distance: 11.503 IQR)
- **Magnitude:** 106.36 | **LOC:** 121 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 25.4), `set_password` (Impact: 8.3), `set_password` (Impact: 6.2)

### 5. `openpyxl-3.1.5/openpyxl/pivot/table.py` (PYTHON) -> Cumulative Risk: **804.75**
- **Archetype:** `file_cluster_8` (Distance: 10.571 IQR)
- **Magnitude:** 634.96 | **LOC:** 1262 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.978%)
- **Heaviest Functions:** `by_priority` (Impact: 31.0), `__init__` (Impact: 30.0), `__init__` (Impact: 13.1)

### 6. `openpyxl-3.1.5/openpyxl/drawing/picture.py` (PYTHON) -> Cumulative Risk: **803.6**
- **Archetype:** `file_cluster_8` (Distance: 10.47 IQR)
- **Magnitude:** 108.94 | **LOC:** 145 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9982%)
- **Heaviest Functions:** `__init__` (Impact: 31.0), `__init__` (Impact: 17.3), `__init__` (Impact: 10.9)

### 7. `openpyxl-3.1.5/openpyxl/styles/styleable.py` (PYTHON) -> Cumulative Risk: **801.78**
- **Archetype:** `file_cluster_13` (Distance: 11.769 IQR)
- **Magnitude:** 176.38 | **LOC:** 152 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `__set__` (Impact: 54.9), `__set__` (Impact: 16.5), `__get__` (Impact: 12.4)

### 8. `openpyxl-3.1.5/openpyxl/drawing/text.py` (PYTHON) -> Cumulative Risk: **801.64**
- **Archetype:** `file_cluster_8` (Distance: 9.781 IQR)
- **Magnitude:** 351.02 | **LOC:** 718 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9624%)
- **Heaviest Functions:** `__init__` (Impact: 20.7), `__init__` (Impact: 16.8), `__init__` (Impact: 16.1)

### 9. `openpyxl-3.1.5/openpyxl/chart/reference.py` (PYTHON) -> Cumulative Risk: **796.52**
- **Archetype:** `file_cluster_13` (Distance: 11.363 IQR)
- **Magnitude:** 131.7 | **LOC:** 125 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 29.4), `__str__` (Impact: 18.6), `pop` (Impact: 10.8)

### 10. `openpyxl-3.1.5/openpyxl/packaging/workbook.py` (PYTHON) -> Cumulative Risk: **795.95**
- **Archetype:** `file_cluster_13` (Distance: 10.286 IQR)
- **Magnitude:** 103.32 | **LOC:** 186 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9776%)
- **Heaviest Functions:** `__init__` (Impact: 16.3), `active` (Impact: 13.2), `__init__` (Impact: 7.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `openpyxl-3.1.5/openpyxl/worksheet/worksheet.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.234 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.989 IQR)
- **Top Global Matches:** file_cluster_13: 12.234, file_cluster_0: 12.423, file_cluster_7: 12.582
- **Magnitude:** 1095.64 | **LOC:** 908 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (26.0306%), Tech Debt (83.5449%)
**Top Internal Functions/Classes:**
  * `__getitem__` (Impact: 74.3 | O(N^6))
  * `append` (Impact: 74.3 | O(N^6) | DB: 1)
    * *Intent:* """ Add a data-validation object to the sheet. The data-validation object defines the type of data-v...
  * `freeze_panes` (Impact: 56.2 | O(N^6) | DB: 2)
  * `_cells_by_col` (Impact: 56.1 | O(N^6))
  * `_move_cells` (Impact: 50.2 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 160`, `args: 60`, `func_start: 60`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 79`, `duplicate_logic: 8`
* *Architecture:* `api: 68`, `import: 26`
* *Defense:* `safety: 13`, `doc: 126`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.327
  * `Choke Point (Betweenness):` 0.026511 | `Ripple Effect (Closeness):` 0.05235
  * `Imports (Out-Degree: 14):` .table, openpyxl.compat, .merge, .formula, .scenario, openpyxl.cell, openpyxl.formula.translate, .print_settings...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/descriptors/serialisable.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.871 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.507 IQR)
- **Top Global Matches:** file_cluster_13: 11.871, file_cluster_8: 12.019, file_cluster_12: 12.135
- **Magnitude:** 737.76 | **LOC:** 241 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (69.5115%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `to_tree` (Impact: 331.3 | O(2^N) | DB: 2)
  * `from_tree` (Impact: 221.0 | O(2^N) | DB: 2)
  * `__iter__` (Impact: 42.1 | O(N^5))
  * `__add__` (Impact: 39.7 | O(N^4))
  * `__eq__` (Impact: 22.1 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 48`, `args: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 21`
* *Architecture:* `api: 11`, `import: 8`
* *Defense:* `safety: 30`, `doc: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 76.703
  * `Choke Point (Betweenness):` 0.012934 | `Ripple Effect (Closeness):` 0.582605
  * `Imports (Out-Degree: 3):` keyword, , .namespace, copy, openpyxl.compat, openpyxl.xml.functions, .sequence
  * `Imported By (In-Degree: 107):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/pivot/table.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.571 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.156 IQR)
- **Top Global Matches:** file_cluster_8: 10.571, file_cluster_7: 11.079, file_cluster_13: 11.148
- **Magnitude:** 634.96 | **LOC:** 1262 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 87
- **Risk Profile:** Cognitive Load (53.5043%), Tech Debt (99.3162%)
**Top Internal Functions/Classes:**
  * `by_priority` (Impact: 31.0 | O(N^6))
    * *Intent:* """ Return a dictionary of format objects keyed by (field id and format property). This can be used ...
  * `__init__` (Impact: 30.0 | O(N^4) | DB: 87)
  * `__init__` (Impact: 13.1 | O(N^4) | DB: 17)
  * `_write_rels` (Impact: 12.8 | O(N^3) | DB: 2)
  * `__init__` (Impact: 11.3 | O(N^4) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 107`, `args: 38`, `func_start: 38`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 279`, `duplicate_logic: 31`
* *Architecture:* `api: 37`, `import: 10`
* *Defense:* `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.972
  * `Choke Point (Betweenness):` 0.000125 | `Ripple Effect (Closeness):` 0.007055
  * `Imports (Out-Degree: 9):` openpyxl.descriptors.serialisable, collections, openpyxl.packaging.relationship, .fields, openpyxl.descriptors.excel, openpyxl.xml.functions, openpyxl.worksheet.filters, openpyxl.descriptors...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/descriptors/base.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.554 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.168 IQR)
- **Top Global Matches:** file_cluster_8: 11.554, file_cluster_13: 11.615, file_cluster_7: 11.798
- **Magnitude:** 614.16 | **LOC:** 273 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (16.0756%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__set__` (Impact: 90.5 | O(2^N))
  * `__set__` (Impact: 72.5 | O(2^N))
  * `__set__` (Impact: 50.4 | O(2^N))
  * `__set__` (Impact: 50.4 | O(2^N))
  * `__set__` (Impact: 40.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 64`, `args: 26`, `func_start: 26`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 9`, `duplicate_logic: 22`
* *Architecture:* `api: 23`, `import: 5`
* *Defense:* `safety: 12`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 30.32
  * `Choke Point (Betweenness):` 0.003537 | `Ripple Effect (Closeness):` 0.279171
  * `Imports (Out-Degree: 2):` openpyxl, .namespace, datetime, re, openpyxl.utils.datetime
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/dimensions.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.265 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.011 IQR)
- **Top Global Matches:** file_cluster_13: 11.265, file_cluster_8: 11.381, file_cluster_7: 11.555
- **Magnitude:** 530.48 | **LOC:** 307 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (36.8804%), Tech Debt (99.8425%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 154.2 | O(2^N) | DB: 3)
  * `__init__` (Impact: 116.8 | O(2^N) | DB: 5)
  * `group` (Impact: 52.4 | O(N^5))
  * `to_tree` (Impact: 44.3 | O(2^N) | DB: 2)
  * `__init__` (Impact: 15.3 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 54`, `args: 19`, `func_start: 19`, `class_start: 6`
* *Risk/State:* `state_mutation: 53`, `duplicate_logic: 8`
* *Architecture:* `api: 21`, `import: 9`
* *Defense:* `safety: 3`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.523
  * `Choke Point (Betweenness):` 0.008033 | `Ripple Effect (Closeness):` 0.048375
  * `Imports (Out-Degree: 6):` openpyxl.descriptors.serialisable, openpyxl.styles.styleable, openpyxl.utils.bound_dictionary, openpyxl.compat, copy, openpyxl.utils, openpyxl.descriptors, openpyxl.utils.units...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/_writer.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.317 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.992 IQR)
- **Top Global Matches:** file_cluster_13: 11.317, file_cluster_8: 11.909, file_cluster_1: 11.913
- **Magnitude:** 502.58 | **LOC:** 391 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (17.4444%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `write_tables` (Impact: 49.6 | O(N^6) | DB: 2)
    * *Intent:* """ Comments & VBA controls use VML and require an additional element that is no longer in the speci...
  * `get_stream` (Impact: 49.2 | O(N^6))
  * `write_row` (Impact: 47.9 | O(N^5) | DB: 2)
  * `write_formatting` (Impact: 26.4 | O(N^5))
  * `rows` (Impact: 21.4 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 79`, `args: 34`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 39`, `dead_code: 1`
* *Architecture:* `io: 4`, `api: 37`, `import: 17`
* *Defense:* `safety: 6`, `doc: 20`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.971
  * `Choke Point (Betweenness):` 0.000394 | `Ripple Effect (Closeness):` 0.007055
  * `Imports (Out-Degree: 10):` .table, io, .related, openpyxl.comments.comment_sheet, .hyperlink, collections, openpyxl.packaging.relationship, openpyxl.styles.differential...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/workbook/workbook.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.926 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.658 IQR)
- **Top Global Matches:** file_cluster_13: 12.926, file_cluster_0: 13.175, file_cluster_11: 13.545
- **Magnitude:** 474.46 | **LOC:** 439 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (38.2242%), Tech Debt (84.9907%)
**Top Internal Functions/Classes:**
  * `active` (Impact: 42.5 | O(2^N) | DB: 2)
  * `copy_worksheet` (Impact: 28.3 | O(2^N))
  * `_duplicate_name` (Impact: 26.5 | O(N^5))
  * `mime_type` (Impact: 21.1 | O(N^3))
  * `epoch` (Impact: 21.0 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 132`, `args: 36`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 75`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 47`, `import: 32`
* *Defense:* `safety: 9`, `doc: 68`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.846
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` openpyxl.styles.colors, openpyxl.chartsheet, openpyxl.styles.borders, .child, openpyxl.compat, openpyxl.utils.indexed_list, openpyxl.writer.excel, openpyxl.styles.fonts...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `openpyxl-3.1.5/openpyxl/pivot/cache.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.729 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.451 IQR)
- **Top Global Matches:** file_cluster_8: 9.729, file_cluster_7: 10.362, file_cluster_13: 10.398
- **Magnitude:** 471.9 | **LOC:** 966 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (48.1049%), Tech Debt (99.8887%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 15.1 | O(N^4) | DB: 25)
  * `__init__` (Impact: 14.7 | O(N^4) | DB: 28)
  * `__init__` (Impact: 13.0 | O(N^4) | DB: 17)
  * `__init__` (Impact: 10.6 | O(N^4) | DB: 11)
  * `__init__` (Impact: 9.2 | O(N^4) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 89`, `args: 33`, `func_start: 33`, `class_start: 27`
* *Risk/State:* `state_mutation: 190`, `duplicate_logic: 29`
* *Architecture:* `api: 31`, `import: 10`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.02
  * `Choke Point (Betweenness):` 7.2e-05 | `Ripple Effect (Closeness):` 0.005291
  * `Imports (Out-Degree: 9):` .table, openpyxl.descriptors.serialisable, .fields, openpyxl.packaging.relationship, openpyxl.descriptors.excel, openpyxl.xml.functions, openpyxl.descriptors, openpyxl.descriptors.nested...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/cell_range.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.259 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.062 IQR)
- **Top Global Matches:** file_cluster_13: 12.259, file_cluster_0: 12.409, file_cluster_7: 12.469
- **Magnitude:** 460.26 | **LOC:** 513 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (22.5915%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 43.4 | O(N^4) | DB: 5)
  * `add` (Impact: 28.2 | O(2^N))
  * `shift` (Impact: 24.6 | O(2^N))
  * `__ne__` (Impact: 18.0 | O(N^3))
  * `isdisjoint` (Impact: 17.9 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 101`, `args: 45`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `state_mutation: 30`, `duplicate_logic: 18`
* *Architecture:* `api: 31`, `import: 8`
* *Defense:* `safety: 10`, `doc: 101`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.866
  * `Choke Point (Betweenness):` 0.000556 | `Ripple Effect (Closeness):` 0.063142
  * `Imports (Out-Degree: 3):` openpyxl.descriptors.serialisable, itertools, copy, operator, openpyxl.utils, openpyxl.descriptors, openpyxl.descriptors.sequence
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/formula/translate.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.719 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.938 IQR)
- **Top Global Matches:** file_cluster_13: 10.719, file_cluster_8: 10.821, file_cluster_0: 10.856
- **Magnitude:** 425.26 | **LOC:** 167 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (31.895%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `translate_range` (Impact: 283.0 | O(2^N))
  * `translate_formula` (Impact: 63.9 | O(N^6) | DB: 2)
  * `translate_col` (Impact: 21.3 | O(N^5))
  * `translate_row` (Impact: 17.8 | O(N^4))
  * `strip_ws_name` (Impact: 11.0 | O(N^3))
    * *Intent:* """ if row_str.startswith('$'): return row_str else: new_row = int(row_str) + rdelta if new_row <= 0...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 32`, `args: 7`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `api: 10`, `import: 3`
* *Defense:* `safety: 2`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.262
  * `Choke Point (Betweenness):` 0.000872 | `Ripple Effect (Closeness):` 0.044602
  * `Imports (Out-Degree: 1):` openpyxl.utils, .tokenizer, re
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/formula/tokenizer.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.554 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.004 IQR)
- **Top Global Matches:** file_cluster_8: 12.554, file_cluster_17: 12.722, file_cluster_7: 12.744
- **Magnitude:** 404.7 | **LOC:** 447 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (34.2882%), Tech Debt (10.8337%)
**Top Internal Functions/Classes:**
  * `_parse_operator` (Impact: 302.0 | O(N^6) | DB: 15)
  * `make_separator` (Impact: 8.1 | O(N^2))
    * *Intent:* # Literal operands: # # Literal operands are always of type 'OPERAND' and can be of subtype # 'TEXT'...
  * `_parse_whitespace` (Impact: 5.5 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 74`, `args: 20`, `func_start: 20`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 72`, `planned_debt: 1`
* *Architecture:* `api: 12`, `import: 1`
* *Defense:* `safety: 17`, `doc: 42`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.039197
  * `Imports (Out-Degree: 0):` re
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/drawing/spreadsheet_drawing.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.06 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.621 IQR)
- **Top Global Matches:** file_cluster_13: 11.06, file_cluster_8: 11.189, file_cluster_7: 11.548
- **Magnitude:** 394.74 | **LOC:** 383 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (29.0625%), Tech Debt (97.7506%)
**Top Internal Functions/Classes:**
  * `_write` (Impact: 63.9 | O(N^5) | DB: 5)
  * `_blip_rels` (Impact: 42.3 | O(N^5) | DB: 1)
  * `__init__` (Impact: 37.4 | O(2^N) | DB: 3)
  * `__init__` (Impact: 34.1 | O(2^N) | DB: 2)
  * `__init__` (Impact: 34.1 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 70`, `args: 17`, `func_start: 17`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 70`, `duplicate_logic: 7`
* *Architecture:* `api: 13`, `import: 17`
* *Defense:* `safety: 7`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.902
  * `Choke Point (Betweenness):` 0.016159 | `Ripple Effect (Closeness):` 0.037793
  * `Imports (Out-Degree: 14):` .relation, openpyxl.descriptors.serialisable, .fill, openpyxl.packaging.relationship, .connector, openpyxl.drawing.image, openpyxl.descriptors.excel, openpyxl.utils...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/reader/excel.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.438 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.228 IQR)
- **Top Global Matches:** file_cluster_13: 10.438, file_cluster_8: 10.701, file_cluster_7: 11.017
- **Magnitude:** 378.12 | **LOC:** 350 | **CtrlFlow:** 39.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (9.5786%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `read_worksheets` (Impact: 118.8 | O(N^6) | DB: 4)
  * `_validate_archive` (Impact: 61.9 | O(N^6) | DB: 9)
  * `read` (Impact: 36.0 | O(2^N))
  * `read_chartsheet` (Impact: 26.0 | O(N^4) | DB: 3)
  * `read_workbook` (Impact: 18.4 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 73`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 22`
* *Architecture:* `io: 7`, `api: 13`, `import: 24`
* *Defense:* `safety: 8`, `doc: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.369
  * `Choke Point (Betweenness):` 0.003096 | `Ripple Effect (Closeness):` 0.005291
  * `Imports (Out-Degree: 16):` .drawings, openpyxl.comments.comment_sheet, openpyxl.chartsheet, openpyxl.xml.functions, openpyxl.packaging.manifest, openpyxl.xml.constants, openpyxl.cell, .strings...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/drawing/text.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.781 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.303 IQR)
- **Top Global Matches:** file_cluster_8: 9.781, file_cluster_13: 10.408, file_cluster_7: 10.492
- **Magnitude:** 351.02 | **LOC:** 718 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (50.6296%), Tech Debt (99.5596%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 20.7 | O(N^4) | DB: 40)
  * `__init__` (Impact: 16.8 | O(N^4) | DB: 28)
  * `__init__` (Impact: 16.1 | O(N^4) | DB: 25)
  * `__init__` (Impact: 14.8 | O(N^4) | DB: 5)
  * `__init__` (Impact: 10.5 | O(N^4) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 69`, `args: 19`, `func_start: 19`, `class_start: 19`
* *Risk/State:* `state_mutation: 154`, `duplicate_logic: 19`
* *Architecture:* `api: 19`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.685
  * `Choke Point (Betweenness):` 0.000405 | `Ripple Effect (Closeness):` 0.047847
  * `Imports (Out-Degree: 8):` openpyxl.descriptors.serialisable, .fill, openpyxl.descriptors.excel, .colors, openpyxl.descriptors, openpyxl.descriptors.nested, .effect, .geometry...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/filters.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.89 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.875 IQR)
- **Top Global Matches:** file_cluster_8: 10.89, file_cluster_13: 11.163, file_cluster_7: 11.218
- **Magnitude:** 347.02 | **LOC:** 487 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (28.5258%), Tech Debt (99.9951%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 49.8 | O(N^4) | DB: 9)
  * `to_tree` (Impact: 20.4 | O(2^N))
  * `_guess_operator` (Impact: 18.0 | O(N^4) | DB: 1)
  * `_get_subtype` (Impact: 17.8 | O(N^4) | DB: 1)
  * `convert` (Impact: 11.0 | O(N^3) | DB: 1)
    * *Intent:* """Convert to more specific filter"""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 72`, `args: 28`, `func_start: 28`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 82`, `duplicate_logic: 17`
* *Architecture:* `api: 25`, `import: 6`
* *Defense:* `safety: 2`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.635
  * `Choke Point (Betweenness):` 0.000275 | `Ripple Effect (Closeness):` 0.049672
  * `Imports (Out-Degree: 4):` openpyxl.descriptors.serialisable, openpyxl.descriptors.excel, openpyxl.utils, openpyxl.descriptors, openpyxl.descriptors.sequence, re
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/print_settings.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.281 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.942 IQR)
- **Top Global Matches:** file_cluster_13: 12.281, file_cluster_8: 12.447, file_cluster_0: 12.597
- **Magnitude:** 332.62 | **LOC:** 185 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (38.8993%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `from_string` (Impact: 44.2 | O(N^4))
  * `__init__` (Impact: 39.5 | O(N^4) | DB: 2)
  * `__init__` (Impact: 39.5 | O(N^4) | DB: 2)
  * `__eq__` (Impact: 26.5 | O(N^5) | DB: 2)
  * `__eq__` (Impact: 26.5 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 52`, `args: 17`, `func_start: 17`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 40`, `duplicate_logic: 17`
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `safety: 7`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.02
  * `Choke Point (Betweenness):` 6.4e-05 | `Ripple Effect (Closeness):` 0.005291
  * `Imports (Out-Degree: 3):` .cell_range, openpyxl.utils, openpyxl.descriptors, openpyxl.utils.cell, re
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/table.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.893 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.821 IQR)
- **Top Global Matches:** file_cluster_8: 10.893, file_cluster_13: 10.963, file_cluster_7: 11.256
- **Magnitude:** 330.78 | **LOC:** 386 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (30.5732%), Tech Debt (94.115%)
**Top Internal Functions/Classes:**
  * `get` (Impact: 40.3 | O(2^N))
  * `__init__` (Impact: 28.8 | O(N^4) | DB: 26)
  * `__iter__` (Impact: 26.2 | O(2^N))
  * `__set__` (Impact: 24.2 | O(2^N))
  * `_initialise_columns` (Impact: 14.4 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 57`, `args: 20`, `func_start: 20`, `class_start: 8`
* *Risk/State:* `state_mutation: 74`, `duplicate_logic: 6`
* *Architecture:* `api: 21`, `import: 10`
* *Defense:* `safety: 1`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.972
  * `Choke Point (Betweenness):` 0.000153 | `Ripple Effect (Closeness):` 0.007055
  * `Imports (Out-Degree: 9):` openpyxl.descriptors.serialisable, .related, .filters, openpyxl.descriptors.excel, openpyxl.xml.functions, openpyxl.utils, openpyxl.descriptors, openpyxl.utils.escape...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/descriptors/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.483 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.084 IQR)
- **Top Global Matches:** file_cluster_13: 13.483, file_cluster_8: 13.676, file_cluster_11: 13.798
- **Magnitude:** 326.6 | **LOC:** 59 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (98.8393%), Tech Debt (99.994%)
**Top Internal Functions/Classes:**
  * `__new__` (Impact: 267.9 | O(2^N) | DB: 7)
  * `__new__` (Impact: 33.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 16`, `args: 2`, `func_start: 2`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 21`, `duplicate_logic: 2`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.846
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .sequence, .base
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `openpyxl-3.1.5/openpyxl/packaging/custom.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.338 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.649 IQR)
- **Top Global Matches:** file_cluster_13: 11.338, file_cluster_8: 11.524, file_cluster_0: 11.715
- **Magnitude:** 323.24 | **LOC:** 290 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (30.9861%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `from_tree` (Impact: 44.6 | O(2^N) | DB: 1)
  * `to_tree` (Impact: 44.1 | O(2^N) | DB: 1)
  * `__init__` (Impact: 27.4 | O(N^4) | DB: 5)
  * `type` (Impact: 22.1 | O(N^4))
  * `append` (Impact: 21.0 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 67`, `args: 19`, `func_start: 19`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 35`, `duplicate_logic: 11`
* *Architecture:* `api: 19`, `import: 8`
* *Defense:* `safety: 4`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.035
  * `Choke Point (Betweenness):` 0.000112 | `Ripple Effect (Closeness):` 0.011905
  * `Imports (Out-Degree: 6):` openpyxl.descriptors.serialisable, openpyxl.descriptors, warnings, openpyxl.descriptors.nested, openpyxl.descriptors.sequence, openpyxl.xml.constants, .core
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/_read_only.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.873 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.098 IQR)
- **Top Global Matches:** file_cluster_13: 10.873, file_cluster_0: 11.058, file_cluster_7: 11.283
- **Magnitude:** 317.56 | **LOC:** 191 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (36.8534%), Tech Debt (30.8939%)
**Top Internal Functions/Classes:**
  * `_cells_by_row` (Impact: 131.7 | O(N^6))
  * `_get_row` (Impact: 59.9 | O(N^5))
  * `calculate_dimension` (Impact: 35.0 | O(2^N))
  * `_get_cell` (Impact: 15.3 | O(N^4))
  * `_calculate_dimension` (Impact: 13.6 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 39`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 18`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 12`, `import: 5`
* *Defense:* `doc: 14`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.035
  * `Choke Point (Betweenness):` 0.000605 | `Ripple Effect (Closeness):` 0.011905
  * `Imports (Out-Degree: 4):` .worksheet, openpyxl.cell.read_only, openpyxl.utils, ._reader, openpyxl.workbook.defined_name
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/cell/rich_text.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.826 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.007 IQR)
- **Top Global Matches:** file_cluster_13: 11.826, file_cluster_8: 12.035, file_cluster_0: 12.089
- **Magnitude:** 317.36 | **LOC:** 203 | **CtrlFlow:** 38.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (32.0216%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `_opt` (Impact: 53.2 | O(N^5) | DB: 2)
  * `from_tree` (Impact: 52.7 | O(2^N) | DB: 2)
  * `__init__` (Impact: 43.9 | O(2^N))
  * `to_tree` (Impact: 35.5 | O(2^N) | DB: 3)
  * `__iadd__` (Impact: 10.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 50`, `args: 19`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 31`, `duplicate_logic: 8`
* *Architecture:* `api: 11`, `import: 5`
* *Defense:* `safety: 5`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.996
  * `Choke Point (Betweenness):` 0.001248 | `Ripple Effect (Closeness):` 0.040336
  * `Imports (Out-Degree: 3):` openpyxl.cell.text, openpyxl.compat, openpyxl.xml.functions, copy, openpyxl.descriptors
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/styles/named_styles.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.524 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.644 IQR)
- **Top Global Matches:** file_cluster_13: 11.524, file_cluster_8: 11.802, file_cluster_7: 11.94
- **Magnitude:** 297.7 | **LOC:** 283 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (29.1285%), Tech Debt (96.5555%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 53.1 | O(N^4) | DB: 11)
  * `__getitem__` (Impact: 43.8 | O(2^N))
  * `__setattr__` (Impact: 24.3 | O(2^N))
  * `remove_duplicates` (Impact: 18.3 | O(N^4) | DB: 1)
  * `__init__` (Impact: 14.2 | O(2^N))
    * *Intent:* """ Named styles are editable and can be applied to multiple objects As only the index is stored in ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 53`, `args: 17`, `func_start: 17`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 47`, `duplicate_logic: 4`
* *Architecture:* `api: 17`, `import: 11`
* *Defense:* `safety: 4`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.953
  * `Choke Point (Betweenness):` 0.002994 | `Ripple Effect (Closeness):` 0.045211
  * `Imports (Out-Degree: 8):` .fills, openpyxl.descriptors.serialisable, .alignment, openpyxl.descriptors.excel, .borders, openpyxl.compat, .cell_style, openpyxl.descriptors...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/cell/cell.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.716 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.902 IQR)
- **Top Global Matches:** file_cluster_13: 12.716, file_cluster_0: 12.854, file_cluster_8: 13.116
- **Magnitude:** 296.9 | **LOC:** 333 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (47.2753%), Tech Debt (94.7081%)
**Top Internal Functions/Classes:**
  * `check_error` (Impact: 110.1 | O(N^4) | DB: 12)
  * `__init__` (Impact: 21.9 | O(2^N) | DB: 7)
  * `get_time_format` (Impact: 17.8 | O(N^3))
  * `get_type` (Impact: 16.2 | O(N^2))
  * `check_string` (Impact: 14.6 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 70`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `state_mutation: 57`, `duplicate_logic: 4`
* *Architecture:* `api: 25`, `import: 11`
* *Defense:* `safety: 11`, `doc: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.275
  * `Choke Point (Betweenness):` 0.003038 | `Ripple Effect (Closeness):` 0.039737
  * `Imports (Out-Degree: 6):` openpyxl.styles.styleable, openpyxl.worksheet.hyperlink, openpyxl.worksheet.formula, openpyxl.compat, copy, openpyxl.utils, openpyxl.styles, openpyxl.cell.rich_text...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/drawing/geometry.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.218 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.355 IQR)
- **Top Global Matches:** file_cluster_8: 9.218, file_cluster_7: 9.923, file_cluster_13: 9.938
- **Magnitude:** 294.5 | **LOC:** 585 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (99.9993%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 9.7 | O(N^4) | DB: 9)
  * `__init__` (Impact: 8.7 | O(N^4) | DB: 7)
  * `__init__` (Impact: 8.7 | O(N^4) | DB: 7)
  * `__init__` (Impact: 8.2 | O(N^4) | DB: 6)
  * `__init__` (Impact: 7.7 | O(N^4) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 69`, `args: 26`, `func_start: 26`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 86`, `duplicate_logic: 26`
* *Architecture:* `api: 27`, `import: 7`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.109
  * `Choke Point (Betweenness):` 0.001749 | `Ripple Effect (Closeness):` 0.108972
  * `Imports (Out-Degree: 6):` openpyxl.styles.colors, openpyxl.descriptors.serialisable, openpyxl.descriptors.excel, openpyxl.descriptors, .line, openpyxl.xml.constants
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/cell/_writer.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.652 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.232 IQR)
- **Top Global Matches:** file_cluster_13: 10.652, file_cluster_8: 10.71, file_cluster_7: 11.227
- **Magnitude:** 293.52 | **LOC:** 137 | **CtrlFlow:** 68.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (36.0587%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `lxml_write_cell` (Impact: 158.6 | O(N^6))
  * `etree_write_cell` (Impact: 60.2 | O(N^3) | DB: 3)
  * `_set_attributes` (Impact: 58.7 | O(N^5) | DB: 1)
    * *Intent:* """ Set coordinate and datatype """
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 20`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 12`
* *Architecture:* `api: 2`, `import: 7`
* *Defense:* `safety: 9`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.013
  * `Choke Point (Betweenness):` 0.000113 | `Ripple Effect (Closeness):` 0.007937
  * `Imports (Out-Degree: 4):` openpyxl.worksheet.formula, openpyxl.compat, openpyxl.xml.functions, openpyxl.cell.rich_text, datetime, openpyxl, openpyxl.utils.datetime
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `openpyxl-3.1.5/openpyxl/descriptors/container.py` (PYTHON) | Magnitude: 54.52 | Delta: **0.148 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 12, api: 6, args: 5
- `openpyxl-3.1.5/openpyxl/comments/comments.py` (PYTHON) | Magnitude: 67.46 | Delta: **0.153 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 15, state_mutation: 13, api: 12
- `openpyxl-3.1.5/openpyxl/cell/read_only.py` (PYTHON) | Magnitude: 130.1 | Delta: **0.233 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 52, encapsulation: 43, api: 22
- `openpyxl-3.1.5/openpyxl/workbook/child.py` (PYTHON) | Magnitude: 270.36 | Delta: **0.304 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 92, structural_boundaries: 38, api: 21, args: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `openpyxl-3.1.5/openpyxl/chartsheet/properties.py` (PYTHON) | Magnitude: 11.92 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 8, state_mutation: 3, import: 3
- `openpyxl-3.1.5/openpyxl/chart/print_settings.py` (PYTHON) | Magnitude: 22.92 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 12, state_mutation: 9, import: 4
- `openpyxl-3.1.5/openpyxl/chart/radar_chart.py` (PYTHON) | Magnitude: 19.78 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 19, import: 8, state_mutation: 6
- `openpyxl-3.1.5/openpyxl/worksheet/formula.py` (PYTHON) | Magnitude: 51.42 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 33, state_mutation: 10, structural_boundaries: 8, branch: 4
- `openpyxl-3.1.5/openpyxl/worksheet/picture.py` (PYTHON) | Magnitude: 12.56 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, class_start: 1, api: 1, import: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `openpyxl-3.1.5/openpyxl/descriptors/slots.py` (PYTHON) | Magnitude: 74.98 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, state_mutation: 6, branch: 5, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `openpyxl-3.1.5/openpyxl/writer/theme.py` (PYTHON) | Magnitude: 3.96 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 2, api: 2, args: 1
- `openpyxl-3.1.5/openpyxl/utils/exceptions.py` (PYTHON) | Magnitude: 20.64 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 16, structural_boundaries: 7, class_start: 7, api: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `openpyxl-3.1.5/openpyxl/compat/__init__.py` (PYTHON) | Magnitude: 110.38 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 20, branch: 9, import: 5
- `openpyxl-3.1.5/openpyxl/chart/descriptors.py` (PYTHON) | Magnitude: 19.6 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 10, doc: 4, class_start: 3
- `openpyxl-3.1.5/openpyxl/utils/inference.py` (PYTHON) | Magnitude: 39.08 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, branch: 17, structural_boundaries: 11, doc: 10
- `openpyxl-3.1.5/openpyxl/chart/chartspace.py` (PYTHON) | Magnitude: 98.52 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 138, state_mutation: 46, structural_boundaries: 40, import: 15
- `openpyxl-3.1.5/openpyxl/comments/author.py` (PYTHON) | Magnitude: 7.76 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 6, api: 2, import: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `openpyxl-3.1.5/openpyxl/chart/_chart.py` -> **Severity: 3.043** (Bridge: 0.0305 * Flux: 99.8563%)
- `openpyxl-3.1.5/openpyxl/worksheet/worksheet.py` -> **Severity: 2.607** (Bridge: 0.0265 * Flux: 98.3343%)
- `openpyxl-3.1.5/openpyxl/chart/reference.py` -> **Severity: 2.208** (Bridge: 0.0221 * Flux: 99.9992%)
- `openpyxl-3.1.5/openpyxl/drawing/spreadsheet_drawing.py` -> **Severity: 1.615** (Bridge: 0.0162 * Flux: 99.9434%)
- `openpyxl-3.1.5/openpyxl/descriptors/serialisable.py` -> **Severity: 1.178** (Bridge: 0.0129 * Flux: 91.1068%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `openpyxl-3.1.5/openpyxl/descriptors/nested.py` -> **Severity: 31.232** (Embedded: 0.3904 * Error Risk: 80.0%)
- `openpyxl-3.1.5/openpyxl/utils/indexed_list.py` -> **Severity: 19.719** (Embedded: 0.2613 * Error Risk: 75.4545%)
- `openpyxl-3.1.5/openpyxl/chart/data_source.py` -> **Severity: 4.692** (Embedded: 0.3227 * Error Risk: 14.5387%)
- `openpyxl-3.1.5/openpyxl/chart/shapes.py` -> **Severity: 3.622** (Embedded: 0.1076 * Error Risk: 33.6569%)
- `openpyxl-3.1.5/openpyxl/chart/marker.py` -> **Severity: 2.688** (Embedded: 0.0532 * Error Risk: 50.5479%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `openpyxl-3.1.5/openpyxl/descriptors/serialisable.py` -> **Severity: 7670.269** (Blast Radius: 76.703 * Doc Risk: 99.9996%)
- `openpyxl-3.1.5/openpyxl/chart/descriptors.py` -> **Severity: 6548.674** (Blast Radius: 65.487 * Doc Risk: 99.9996%)
- `openpyxl-3.1.5/openpyxl/descriptors/nested.py` -> **Severity: 4981.5** (Blast Radius: 49.815 * Doc Risk: 100.0%)
- `openpyxl-3.1.5/openpyxl/xml/functions.py` -> **Severity: 3485.364** (Blast Radius: 74.028 * Doc Risk: 47.0817%)
- `openpyxl-3.1.5/openpyxl/descriptors/excel.py` -> **Severity: 3305.633** (Blast Radius: 33.677 * Doc Risk: 98.157%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
