# ARCHITECTURAL_BRIEF: abap2xlsx
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/abap2xlsx/abap2xlsx.git` |
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
| Total Artifacts | 407 |
| Analyzed Artifacts (Scanned) | 393 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 14 |
| Total LOC | 34438 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 96.6% |
| Dominant Lang | ABAP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| XML | 277 | 0 | 70.5% |
| ABAP | 105 | 34094 | 26.7% |
| JSON | 4 | 335 | 1.0% |
| MARKDOWN | 3 | 0 | 0.8% |
| PLAINTEXT | 2 | 1 | 0.5% |
| YAML | 1 | 1 | 0.3% |
| JAVASCRIPT | 1 | 7 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Mainframe / COBOL & Config` (z +1.39; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 74%, I/O & Config Routines Files 9%, Large Core Modules 5%, Declarative / Non-Code 4%, Interface Declarations Files 4%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 388 | 98.7% |
| Unknown | 1 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 1.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 14*

**Composition by Extension & Reason:**
- `.md`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 92.8 | 6.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.5 | 15.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.7 | 1.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.5 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 5.4 | 0.2 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 53.3 | 0.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 16.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 43.0 | 0.6 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 26.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.5 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 22.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3688 | 79 | 11 | `src/zcl_excel_worksheet.clas.abap` |
| cleanup | 284 | 37 | 0 | `src/zcl_excel_reader_2007.clas.abap` |
| guards | 1889 | 93 | 9 | `src/zcl_excel_reader_2007.clas.abap` |
| danger | 167 | 25 | 0 | `src/zcl_excel_worksheet.clas.abap` |
| concurrency | 2 | 1 | 0 | `test/run.mjs` |
| connectivity | 90 | 81 | 1 | `src/not_cloud/zexcel_template_get_types.prog.abap` |
| io | 140 | 25 | 0 | `src/not_cloud/zcl_excel_converter_alv.clas.abap` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 0 | 0 | 0 | - |
| tests | 441 | 11 | 0 | `src/zcl_excel_common.clas.testclasses.abap` |
| docs | 9 | 3 | 0 | `src/zcl_excel_common.clas.abap` |
| debt | 30 | 8 | 0 | `src/not_cloud/zcl_excel_ole.clas.abap` |
| mutation | 14675 | 90 | 41 | `src/zcl_excel_writer_2007.clas.abap` |
| dead_code | 193 | 20 | 0 | `src/zcl_excel_style_changer.clas.abap` |
| credential | 2 | 1 | 0 | `src/zcl_excel_writer_2007.clas.abap` |
| threat | 79 | 8 | 0 | `src/zcl_excel_worksheet.clas.abap` |
| ml_ai | 304 | 10 | 0 | `src/zcl_excel_worksheet.clas.testclasses.abap` |
| ui | 17 | 4 | 0 | `src/not_cloud/zexcel_template_get_types.prog.abap` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/not_cloud/zcl_excel_converter_alv.clas.abap` (Hits: 37)
- `src/zcl_excel_reader_2007.clas.abap` (Hits: 16)
- `src/not_cloud/zcl_excel_converter.clas.abap` (Hits: 12)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 1 inbound connections
2. **README.md** (`README.md`) — 0 inbound connections
3. **SECURITY.md** (`SECURITY.md`) — 0 inbound connections
4. **_config.yml** (`_config.yml`) — 0 inbound connections
5. **abap_transpile.json** (`abap_transpile.json`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **run.mjs** (`test/run.mjs`) — 3 outbound dependencies
2. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 2 outbound dependencies
3. **README.md** (`README.md`) — 1 outbound dependencies
4. **zcl_excel_reader_huge_file.clas.abap** (`src/zcl_excel_reader_huge_file.clas.abap`) — 1 outbound dependencies
5. **SECURITY.md** (`SECURITY.md`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `bind_alv_ole2` **(Many-Argument Workhorses)** (@ `src/not_cloud/zcl_excel_ole.clas.abap`) -> Impact: **926.4** | LOC: 1981
- `change_cell_style` **(Many-Argument Workhorses)** (@ `src/zcl_excel_worksheet.clas.abap`) -> Impact: **638.0** | LOC: 378
- `create_ax` **(Many-Argument Workhorses)** (@ `src/zcl_excel_graph_bars.clas.abap`) -> Impact: **249.1** | LOC: 146
- `create_ax` **(Many-Argument Workhorses)** (@ `src/zcl_excel_graph_line.clas.abap`) -> Impact: **249.1** | LOC: 146
- `load_worksheet` **(Many-Argument Workhorses)** (@ `src/zcl_excel_reader_2007.clas.abap`) -> Impact: **241.9** | LOC: 857
- `set_cell` **(Many-Argument Workhorses)** (@ `src/zcl_excel_worksheet.clas.abap`) -> Impact: **227.3** | LOC: 306
- `create_xl_styles` **(Compute Cores)** (@ `src/zcl_excel_writer_2007.clas.abap`) -> Impact: **162.9** | LOC: 912
- `bind_table` **(Many-Argument Workhorses)** (@ `src/zcl_excel_worksheet.clas.abap`) -> Impact: **150.9** | LOC: 299
- `convert_to_table` **(Many-Argument Workhorses)** (@ `src/zcl_excel_worksheet.clas.abap`) -> Impact: **150.0** | LOC: 285
- `shift_formula` **(Many-Argument Workhorses)** (@ `src/zcl_excel_common.clas.abap`) -> Impact: **143.8** | LOC: 372

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 335 | 20876.26 | 6.59% | 0.86% |
| `__monolith__` | 10 | 5081.22 | 0.0% | 0.0% |
| `src/not_cloud` | 44 | 4344.88 | 10.44% | 2.24% |
| `test` | 4 | 39.12 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/zcl_excel_style_changer.clas.abap` -> **99.7405%** Exposure
- `src/not_cloud/zcl_excel_ole.clas.locals_imp.abap` -> **98.6851%** Exposure
- `src/zcl_excel_reader_huge_file.clas.locals_imp.abap` -> **88.0797%** Exposure
- `src/zcl_excel_worksheet.clas.testclasses.abap` -> **20.0431%** Exposure
- `src/zcl_excel.clas.abap` -> **13.6026%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/not_cloud/zcl_excel_converter_alv.clas.abap` -> **100.0%** Exposure
- `src/not_cloud/zcl_excel_converter_result_wd.clas.abap` -> **100.0%** Exposure
- `src/not_cloud/zcl_excel_ole.clas.abap` -> **100.0%** Exposure
- `src/not_cloud/zexcel_template_get_types.prog.abap` -> **100.0%** Exposure
- `src/zcl_excel_autofilter.clas.abap` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/zcl_excel_style_changer.clas.abap` -> **95** Orphaned Functions | **0** Duplicates
- `src/zcl_excel_worksheet.clas.abap` -> **12** Orphaned Functions | **0** Duplicates
- `src/zcl_excel_worksheet.clas.testclasses.abap` -> **0** Orphaned Functions | **6** Duplicates
- `src/not_cloud/zcl_excel_ole.clas.locals_imp.abap` -> **5** Orphaned Functions | **0** Duplicates
- `src/zcl_excel.clas.abap` -> **3** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `2` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/zcl_excel_style_changer.clas.abap` (ABAP) -> Cumulative Risk: **668.39**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +0.83)
- **Magnitude:** 1212.64 | **LOC:** 1673 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.7405%)
- **Heaviest Functions:** `zif_excel_style_changer~apply` (Compute Cores, Impact: 109.2), `move_supplied_borders` (Many-Argument Workhorses, Impact: 14.4), `zif_excel_style_changer~set_complete_borders` (I/O & Config Routines, Impact: 12.6)

### 2. `src/zcl_excel_reader_2007.clas.abap` (ABAP) -> Cumulative Risk: **645.78**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +0.08)
- **Magnitude:** 2436.66 | **LOC:** 4488 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `load_worksheet` (Many-Argument Workhorses, Impact: 241.9), `load_workbook` (Many-Argument Workhorses, Impact: 99.3), `load_styles` (Many-Argument Workhorses, Impact: 63.1)

### 3. `src/zcl_excel_common.clas.abap` (ABAP) -> Cumulative Risk: **611.05**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +0.77)
- **Magnitude:** 1036.92 | **LOC:** 1753 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (93.7176%)
- **Heaviest Functions:** `shift_formula` (Many-Argument Workhorses, Impact: 143.8), `convert_range2column_a_row` (Many-Argument Workhorses, Impact: 46.6), `convert_column2int` (Many-Argument Workhorses, Impact: 31.2)

### 4. `src/zcl_excel_worksheet.clas.abap` (ABAP) -> Cumulative Risk: **601.79**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.22)
- **Magnitude:** 3438.98 | **LOC:** 4870 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9974%), Safety Score (84.3466%)
- **Heaviest Functions:** `change_cell_style` (Many-Argument Workhorses, Impact: 638.0), `set_cell` (Many-Argument Workhorses, Impact: 227.3), `bind_table` (Many-Argument Workhorses, Impact: 150.9)

### 5. `src/not_cloud/zcl_excel_ole.clas.abap` (ABAP) -> Cumulative Risk: **590.52**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +2.54)
- **Magnitude:** 1680.64 | **LOC:** 2092 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (95.4592%)
- **Heaviest Functions:** `bind_alv_ole2` (Many-Argument Workhorses, Impact: 926.4), `close_document` (I/O & Config Routines, Impact: 7.2), `error_doi` (I/O & Config Routines, Impact: 2.7)

### 6. `src/not_cloud/zcl_excel_converter.clas.abap` (ABAP) -> Cumulative Risk: **583.55**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +1.87)
- **Magnitude:** 1202.74 | **LOC:** 1818 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Safety Score (91.2299%)
- **Heaviest Functions:** `loop_subtotal` (Many-Argument Workhorses, Impact: 120.9), `convert` (Many-Argument Workhorses, Impact: 47.6), `loop_normal` (Many-Argument Workhorses, Impact: 29.6)

### 7. `src/zcl_excel_writer_2007.clas.locals_imp.abap` (ABAP) -> Cumulative Risk: **572.22**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +1.31)
- **Magnitude:** 721.22 | **LOC:** 1834 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9805%), Verification (80.0%)
- **Heaviest Functions:** `add_conditional_formatting` (I/O & Config Routines, Impact: 65.3), `add_sheet_views` (I/O & Config Routines, Impact: 35.0), `add_cols` (I/O & Config Routines, Impact: 28.4)

### 8. `src/zcl_excel_graph_line.clas.abap` (ABAP) -> Cumulative Risk: **571.51**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.61)
- **Magnitude:** 438.74 | **LOC:** 282 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.8922%)
- **Heaviest Functions:** `create_ax` (Many-Argument Workhorses, Impact: 249.1), `set_show_cat_name` (Interface Declarations, Impact: 1.6), `set_show_legend_key` (Interface Declarations, Impact: 1.6)

### 9. `src/zcl_excel_graph_bars.clas.abap` (ABAP) -> Cumulative Risk: **571.38**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.60)
- **Magnitude:** 438.78 | **LOC:** 284 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.8336%)
- **Heaviest Functions:** `create_ax` (Many-Argument Workhorses, Impact: 249.1), `set_show_cat_name` (Interface Declarations, Impact: 1.6), `set_show_legend_key` (Interface Declarations, Impact: 1.6)

### 10. `src/zcl_excel_writer_csv.clas.abap` (ABAP) -> Cumulative Risk: **569.67**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +2.13)
- **Magnitude:** 209.86 | **LOC:** 378 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9998%), Cognitive Load (90.7944%)
- **Heaviest Functions:** `create_csv` (Compute Cores, Impact: 77.2), `create` (I/O & Config Routines, Impact: 2.0), `set_active_sheet_index` (I/O & Config Routines, Impact: 1.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_worksheet.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 3438.98 | **LOC:** 4870 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (83.9611%), Tech Debt (10.2059%)
**Top Internal Functions/Classes:**
  * `change_cell_style` **(Many-Argument Workhorses)** (Impact: 638.0)
  * `set_cell` **(Many-Argument Workhorses)** (Impact: 227.3)
  * `bind_table` **(Many-Argument Workhorses)** (Impact: 150.9)
  * `convert_to_table` **(Many-Argument Workhorses)** (Impact: 150.0)
  * `get_table` **(Many-Argument Workhorses)** (Impact: 68.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 15 instances
* *Amplified Cascading Flux:* 368 instances
* *Memory Alloc (weighted view):* 33
* *State Mutation (weighted view):* 1228
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 540`, `structural_boundaries: 279`, `args: 121`, `func_start: 111`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 492`, `dead_code: 17`, `unreferenced_by_name: 12`
* *Architecture:* `io: 12`, `api: 1`
* *Defense:* `safety: 118`, `doc: 4`, `immutability_locks: 17`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_reader_2007.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2436.66 | **LOC:** 4488 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (62.5603%), Tech Debt (9.2028%)
**Top Internal Functions/Classes:**
  * `load_worksheet` **(Many-Argument Workhorses)** (Impact: 241.9)
  * `load_workbook` **(Many-Argument Workhorses)** (Impact: 99.3)
  * `load_styles` **(Many-Argument Workhorses)** (Impact: 63.1)
  * `load_drawing_anchor` **(Many-Argument Workhorses)** (Impact: 54.6)
  * `load_style_fills` **(Many-Argument Workhorses)** (Impact: 46.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 53 instances
* *Amplified Cascading Flux:* 393 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 1326
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 383`, `structural_boundaries: 177`, `args: 54`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 540`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 16`, `api: 1`
* *Defense:* `safety: 198`, `immutability_locks: 9`, `cleanup: 49`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_writer_2007.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2189.54 | **LOC:** 6552 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.2925%), Tech Debt (7.7609%)
**Top Internal Functions/Classes:**
  * `create_xl_styles` **(Compute Cores)** (Impact: 162.9)
  * `create_xl_charts` **(Many-Argument Workhorses)** (Impact: 114.4)
  * `create_xl_sheet_sheet_data` **(Many-Argument Workhorses)** (Impact: 106.8)
  * `create_dxf_style` **(Many-Argument Workhorses)** (Impact: 40.6)
  * `create_xl_table` **(Many-Argument Workhorses)** (Impact: 39.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 18 instances
* *Amplified Cascading Flux:* 291 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 1130
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 357`, `structural_boundaries: 163`, `args: 65`, `func_start: 44`, `class_start: 2`
* *Risk/State:* `state_mutation: 548`, `dead_code: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 1`
* *Defense:* `safety: 88`, `immutability_locks: 32`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/not_cloud/zcl_excel_ole.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1680.64 | **LOC:** 2092 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (62.4954%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bind_alv_ole2` **(Many-Argument Workhorses)** (Impact: 926.4)
  * `close_document` **(I/O & Config Routines)** (Impact: 7.2)
  * `error_doi` **(I/O & Config Routines)** (Impact: 2.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 44 instances
* *Amplified Cascading Flux:* 209 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 714
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 163`, `args: 2`, `func_start: 3`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 296`, `dead_code: 26`
* *Architecture:* `io: 9`, `api: 1`
* *Defense:* `safety: 15`, `doc: 1`, `cleanup: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_style_changer.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1212.64 | **LOC:** 1673 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.0804%), Tech Debt (99.7405%)
**Top Internal Functions/Classes:**
  * `zif_excel_style_changer~apply` **(Compute Cores)** (Impact: 109.2)
  * `move_supplied_borders` **(Many-Argument Workhorses)** (Impact: 14.4)
  * `zif_excel_style_changer~set_complete_borders` **(I/O & Config Routines)** (Impact: 12.6)
  * `zif_excel_style_changer~set_complete_font` **(I/O & Config Routines)** (Impact: 10.1)
  * `clear_initial_colorxfields` **(Compute Cores)** (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 19 instances
* *Amplified Cascading Flux:* 198 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 886
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 108`, `args: 6`, `func_start: 98`, `class_start: 2`
* *Risk/State:* `state_mutation: 490`, `unreferenced_by_name: 95`
* *Architecture:* `api: 1`
* *Defense:* `safety: 10`, `immutability_locks: 1`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/not_cloud/zcl_excel_converter.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 1202.74 | **LOC:** 1818 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (69.7618%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `loop_subtotal` **(Many-Argument Workhorses)** (Impact: 120.9)
  * `convert` **(Many-Argument Workhorses)** (Impact: 47.6)
  * `loop_normal` **(Many-Argument Workhorses)** (Impact: 29.6)
  * `execute_converter` **(Many-Argument Workhorses)** (Impact: 29.5)
  * `get_color_style` **(Many-Argument Workhorses)** (Impact: 27.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 22 instances
* *Amplified Cascading Flux:* 183 instances
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 627
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 110`, `args: 45`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 261`, `dead_code: 2`
* *Architecture:* `io: 12`, `api: 2`
* *Defense:* `safety: 41`, `immutability_locks: 5`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_common.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1036.92 | **LOC:** 1753 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (83.8185%), Tech Debt (9.7857%)
**Top Internal Functions/Classes:**
  * `shift_formula` **(Many-Argument Workhorses)** (Impact: 143.8)
  * `convert_range2column_a_row` **(Many-Argument Workhorses)** (Impact: 46.6)
  * `convert_column2int` **(Many-Argument Workhorses)** (Impact: 31.2)
  * `recursive_struct_to_class` **(Many-Argument Workhorses)** (Impact: 25.1)
  * `get_fieldcatalog` **(Many-Argument Workhorses)** (Impact: 19.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 18 instances
* *Amplified Cascading Flux:* 171 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 563
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 95`, `args: 62`, `func_start: 32`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 221`, `dead_code: 7`, `fragile_debt: 2`
* *Architecture:* `io: 4`, `api: 1`
* *Defense:* `safety: 30`, `doc: 4`, `immutability_locks: 9`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_writer_2007.clas.locals_imp.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 721.22 | **LOC:** 1834 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (40.4487%), Tech Debt (7.933%)
**Top Internal Functions/Classes:**
  * `add_conditional_formatting` **(I/O & Config Routines)** (Impact: 65.3)
  * `add_sheet_views` **(I/O & Config Routines)** (Impact: 35.0)
  * `add_cols` **(I/O & Config Routines)** (Impact: 28.4)
  * `add_data_validations` **(I/O & Config Routines)** (Impact: 24.6)
  * `add_page_setup` **(I/O & Config Routines)** (Impact: 24.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 10 instances
* *Amplified Cascading Flux:* 100 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 424
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 55`, `args: 1`, `func_start: 23`, `class_start: 4`
* *Risk/State:* `state_mutation: 224`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* `safety: 45`, `immutability_locks: 2`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_drawing.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 594.0 | **LOC:** 1137 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.2208%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `load_chart_attributes` **(Compute Cores)** (Impact: 111.2)
  * `set_position2` **(Many-Argument Workhorses)** (Impact: 15.3)
  * `get_media` **(I/O & Config Routines)** (Impact: 10.1)
  * `set_media` **(Many-Argument Workhorses)** (Impact: 9.6)
  * `set_position` **(Many-Argument Workhorses)** (Impact: 8.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 81 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 369
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 86`, `args: 26`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `state_mutation: 207`, `dead_code: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 38`, `immutability_locks: 17`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/not_cloud/zcl_excel_converter_alv.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 523.14 | **LOC:** 601 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.9565%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `update_catalog` **(Many-Argument Workhorses)** (Impact: 64.5)
  * `get_color` **(Many-Argument Workhorses)** (Impact: 33.9)
  * `get_filter` **(Many-Argument Workhorses)** (Impact: 23.9)
  * `apply_sort` **(Many-Argument Workhorses)** (Impact: 10.3)
  * `class_constructor` **(I/O & Config Routines)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 12 instances
* *Amplified Cascading Flux:* 62 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 377
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 24`, `args: 7`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 253`
* *Architecture:* `io: 37`, `api: 1`
* *Defense:* `safety: 13`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_worksheet.clas.testclasses.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 498.02 | **LOC:** 1828 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (41.055%), Tech Debt (20.0431%)
**Top Internal Functions/Classes:**
  * `assert` **(Many-Argument Workhorses)** (Impact: 13.2)
  * `delete_merge3` **(I/O & Config Routines)** (Impact: 9.1)
  * `delete_merge4` **(I/O & Config Routines)** (Impact: 9.1)
  * `assert` **(Many-Argument Workhorses)** (Impact: 8.8)
  * `assert` **(Many-Argument Workhorses)** (Impact: 8.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 19 instances
* *Memory Alloc (weighted view):* 15
* *State Mutation (weighted view):* 286
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 208`, `args: 8`, `func_start: 74`, `class_start: 30`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 248`, `duplicate_logic: 6`
* *Architecture:* `io: 8`
* *Defense:* `safety: 81`, `test: 142`, `immutability_locks: 1`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_writer_huge_file.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 494.26 | **LOC:** 817 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.0313%), Tech Debt (9.8875%)
**Top Internal Functions/Classes:**
  * `create_xl_sheet` **(I/O & Config Routines)** (Impact: 104.0)
  * `create_xl_sharedstrings` **(I/O & Config Routines)** (Impact: 7.8)
  * `get_cells` **(I/O & Config Routines)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 110 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 367
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 19`, `args: 1`, `func_start: 3`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 147`, `fragile_debt: 1`
* *Architecture:* `io: 3`, `api: 1`
* *Defense:* `safety: 15`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_graph_bars.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 438.78 | **LOC:** 284 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.7274%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create_ax` **(Many-Argument Workhorses)** (Impact: 249.1)
  * `set_show_cat_name` **(Interface Declarations)** (Impact: 1.6)
  * `set_show_legend_key` **(Interface Declarations)** (Impact: 1.6)
  * `set_show_percent` **(Interface Declarations)** (Impact: 1.6)
  * `set_show_ser_name` **(Interface Declarations)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 174
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 25`, `args: 7`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `state_mutation: 62`
* *Architecture:* `api: 1`
* *Defense:* `safety: 1`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_graph_line.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 438.74 | **LOC:** 282 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.7946%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create_ax` **(Many-Argument Workhorses)** (Impact: 249.1)
  * `set_show_cat_name` **(Interface Declarations)** (Impact: 1.6)
  * `set_show_legend_key` **(Interface Declarations)** (Impact: 1.6)
  * `set_show_percent` **(Interface Declarations)** (Impact: 1.6)
  * `set_show_ser_name` **(Interface Declarations)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 174
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 25`, `args: 7`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `state_mutation: 62`
* *Architecture:* `api: 1`
* *Defense:* `safety: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_fill_template.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 356.78 | **LOC:** 650 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.5023%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fill_range` **(Many-Argument Workhorses)** (Impact: 73.9)
  * `find_var` **(I/O & Config Routines)** (Impact: 20.3)
  * `validate_range` **(Compute Cores)** (Impact: 12.1)
  * `fill_sheet` **(Many-Argument Workhorses)** (Impact: 10.7)
  * `discard_overlapped` **(I/O & Config Routines)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 61 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 210
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 32`, `args: 6`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 88`
* *Architecture:* `api: 1`
* *Defense:* `safety: 9`, `immutability_locks: 5`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_common.clas.testclasses.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 293.5 | **LOC:** 1856 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.7589%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `macro_calculate_cell_distance` **(Many-Argument Workhorses)** (Impact: 4.3)
  * `macro_shift_formula` **(Many-Argument Workhorses)** (Impact: 4.0)
  * `simple` **(I/O & Config Routines)** (Impact: 3.4)
  * `describe_structure` **(I/O & Config Routines)** (Impact: 2.8)
  * `excel_string_to_date` **(I/O & Config Routines)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 9 instances
* *Memory Alloc (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 163`, `args: 3`, `func_start: 89`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 109`
* *Architecture:* None
* *Defense:* `safety: 60`, `test: 199`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 284.18 | **LOC:** 701 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (55.7269%), Tech Debt (13.6026%)
**Top Internal Functions/Classes:**
  * `get_style_index_in_styles` **(Compute Cores)** (Impact: 13.3)
  * `add_new_drawing` **(Many-Argument Workhorses)** (Impact: 10.8)
  * `get_drawings_iterator` **(Compute Cores)** (Impact: 9.2)
  * `fill_template` **(Many-Argument Workhorses)** (Impact: 7.0)
  * `delete_worksheet` **(Many-Argument Workhorses)** (Impact: 6.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 33 instances
* *Memory Alloc (weighted view):* 14
* *State Mutation (weighted view):* 130
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 78`, `args: 45`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `state_mutation: 64`, `unreferenced_by_name: 3`
* *Architecture:* `io: 4`, `api: 1`
* *Defense:* `safety: 6`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_theme_font_scheme.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 279.6 | **LOC:** 505 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.9192%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `build_xml` **(Defensive Guards)** (Impact: 44.5)
  * `modify_lec_fonts` **(Many-Argument Workhorses)** (Impact: 33.1)
  * `load` **(Compute Cores)** (Impact: 29.9)
  * `modify_font` **(Many-Argument Workhorses)** (Impact: 17.2)
  * `modify_cs_font` **(Many-Argument Workhorses)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 39 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 42`, `args: 8`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `state_mutation: 53`
* *Architecture:* `io: 4`, `api: 1`
* *Defense:* `safety: 39`, `immutability_locks: 13`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_theme_color_scheme.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 260.66 | **LOC:** 448 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.906%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `build_xml` **(Defensive Guards)** (Impact: 66.1)
  * `set_color` **(Many-Argument Workhorses)** (Impact: 49.1)
  * `load` **(Compute Cores)** (Impact: 24.6)
  * `get_color` **(Defensive Guards)** (Impact: 11.3)
  * `set_name` **(I/O & Config Routines)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 12 instances
* *Amplified Cascading Flux:* 26 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 37`, `args: 6`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `state_mutation: 41`
* *Architecture:* `api: 1`
* *Defense:* `safety: 37`, `immutability_locks: 18`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_sheet_setup.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 254.24 | **LOC:** 479 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.7572%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_header_footer_string` **(Many-Argument Workhorses)** (Impact: 71.7)
  * `set_page_margins` **(Many-Argument Workhorses)** (Impact: 32.2)
  * `process_header_footer` **(Many-Argument Workhorses)** (Impact: 20.6)
  * `set_header_footer` **(Many-Argument Workhorses)** (Impact: 6.0)
  * `get_header_footer` **(Many-Argument Workhorses)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 33 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 44`, `args: 6`, `func_start: 6`, `class_start: 2`
* *Risk/State:* `state_mutation: 44`
* *Architecture:* `api: 1`
* *Defense:* `safety: 31`, `immutability_locks: 81`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_autofilter.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 210.56 | **LOC:** 431 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.0853%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `is_row_hidden` **(Compute Cores)** (Impact: 14.2)
  * `is_row_hidden_single_values` **(Many-Argument Workhorses)** (Impact: 13.1)
  * `is_row_hidden_text_pattern` **(Many-Argument Workhorses)** (Impact: 10.5)
  * `validate_area` **(I/O & Config Routines)** (Impact: 9.9)
  * `set_text_filter` **(Many-Argument Workhorses)** (Impact: 8.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 35 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 42`, `args: 17`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `state_mutation: 53`
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* `safety: 1`, `immutability_locks: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_writer_csv.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 209.86 | **LOC:** 378 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.7944%), Tech Debt (11.3216%)
**Top Internal Functions/Classes:**
  * `create_csv` **(Compute Cores)** (Impact: 77.2)
  * `create` **(I/O & Config Routines)** (Impact: 2.0)
  * `set_active_sheet_index` **(I/O & Config Routines)** (Impact: 1.6)
  * `set_active_sheet_index_by_name` **(I/O & Config Routines)** (Impact: 1.6)
  * `set_delimiter` **(Interface Declarations)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 32 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 23`, `args: 10`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 46`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `api: 1`
* *Defense:* `safety: 10`, `immutability_locks: 1`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/not_cloud/zexcel_template_get_types.prog.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 209.78 | **LOC:** 385 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.1974%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_type_r` **(Compute Cores)** (Impact: 45.5)
  * `get_types` **(I/O & Config Routines)** (Impact: 11.8)
  * `get_file_path` **(Compute Cores)** (Impact: 8.7)
    * *Intent:* *&---------------------------------------------------------------------* *& Form Get_file_path *&---...
  * `load_smw0` **(I/O & Config Routines)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 39 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 13`, `args: 3`, `func_start: 4`
* *Risk/State:* `state_mutation: 51`
* *Architecture:* `io: 2`, `api: 4`
* *Defense:* `safety: 5`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/zcl_excel_style_fill.clas.abap` (ABAP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 195.26 | **LOC:** 187 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.2808%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `build_gradient` **(I/O & Config Routines)** (Impact: 19.6)
  * `check_filltype_is_gradient` **(I/O & Config Routines)** (Impact: 5.1)
  * `get_structure` **(I/O & Config Routines)** (Impact: 1.9)
  * `constructor` **(I/O & Config Routines)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 49 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 11`, `args: 2`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `state_mutation: 65`
* *Architecture:* `api: 1`
* *Defense:* `safety: 1`, `immutability_locks: 34`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/zcl_excel_reader_2007.clas.abap` -> Churn: **100.0%** | Cog Load: 62.5603% | Debt: 9.2028%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/zcl_excel_worksheet.clas.abap` -> **Lars Hvam** (100.0% isolated ownership) | Magnitude: 3438.98
- `src/zcl_excel_reader_2007.clas.abap` -> **Bernd** (100.0% isolated ownership) | Magnitude: 2436.66
- `src/zcl_excel_writer_2007.clas.abap` -> **Lars Hvam** (100.0% isolated ownership) | Magnitude: 2189.54
- `src/not_cloud/zcl_excel_ole.clas.abap` -> **Lars Hvam** (100.0% isolated ownership) | Magnitude: 1680.64
- `src/not_cloud/zcl_excel_converter.clas.abap` -> **Lars Hvam** (100.0% isolated ownership) | Magnitude: 1202.74

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/not_cloud/zcl_excel_converter.clas.abap` -> **Severity: 253.9** (Blast Radius: 2.539 * Doc Risk: 100.0%)
- `src/not_cloud/zcl_excel_converter_alv.clas.abap` -> **Severity: 253.9** (Blast Radius: 2.539 * Doc Risk: 100.0%)
- `src/not_cloud/zcl_excel_converter_alv_grid.clas.abap` -> **Severity: 253.9** (Blast Radius: 2.539 * Doc Risk: 100.0%)
- `src/not_cloud/zcl_excel_converter_result.clas.abap` -> **Severity: 253.9** (Blast Radius: 2.539 * Doc Risk: 100.0%)
- `src/not_cloud/zcl_excel_converter_result_ex.clas.abap` -> **Severity: 253.9** (Blast Radius: 2.539 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
