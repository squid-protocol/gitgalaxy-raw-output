# ARCHITECTURAL_BRIEF: openpyxl
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
- **Scope:** 183 analyzed artifact(s), 19189 LOC.
- **Load-bearing artifact:** `openpyxl-3.1.5/openpyxl/descriptors/serialisable.py` -- 102 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `openpyxl-3.1.5/openpyxl/workbook/workbook.py` -- pulls in 31 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `openpyxl-3.1.5/openpyxl/pivot/table.py` at magnitude 833.56 (structural weight, not risk).
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
| Total Artifacts | 197 |
| Analyzed Artifacts (Scanned) | 183 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 14 |
| Total LOC | 19189 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 92.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3386 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3454 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 74.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.7789 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 182 | 19189 | 99.5% |
| PLAINTEXT | 1 | 0 | 0.5% |

## 4.1 SOURCE ENCODINGS
All 183 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Parameter Forwarders Files 39%, Large Core Modules (3) 16%, Many-Argument Workhorses Files 14%, Data / Markup / Trivial 11%, Large Core Modules (2) 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 182 | 99.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 14*

**Composition by Extension & Reason:**
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 68 LOC), 1x Excluded (Machine-Generated Source Code Signature: 130 LOC), 1x Excluded (Machine-Generated Source Code Signature: 178 LOC)
- `.rst`: 3x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.8 | 31.3 | 38.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 88.1 | 63.6 | 70.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 20.0 | 2.5 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 38.0 | 39.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 87.0 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 5.8 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 68.6 | 89.1 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 191 | 68 | 3 | `openpyxl-3.1.5/openpyxl/worksheet/_reader.py` |
| cleanup | 15 | 7 | 0 | `openpyxl-3.1.5/openpyxl/worksheet/_writer.py` |
| guards | 520 | 95 | 8 | `openpyxl-3.1.5/openpyxl/worksheet/worksheet.py` |
| danger | 244 | 65 | 4 | `openpyxl-3.1.5/openpyxl/descriptors/base.py` |
| concurrency | 47 | 25 | 1 | `openpyxl-3.1.5/openpyxl/utils/dataframe.py` |
| connectivity | 1270 | 160 | 19 | `openpyxl-3.1.5/openpyxl/worksheet/worksheet.py` |
| io | 22 | 8 | 0 | `openpyxl-3.1.5/openpyxl/reader/excel.py` |
| crypto | 1 | 1 | 0 | `openpyxl-3.1.5/openpyxl/chartsheet/protection.py` |
| ipc | 0 | 0 | 0 | - |
| time | 24 | 8 | 0 | `openpyxl-3.1.5/openpyxl/utils/datetime.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 40 | 17 | 0 | `openpyxl-3.1.5/openpyxl/formula/tokenizer.py` |
| events | 25 | 2 | 0 | `openpyxl-3.1.5/openpyxl/worksheet/_writer.py` |
| tests | 0 | 0 | 0 | - |
| docs | 584 | 113 | 7 | `openpyxl-3.1.5/openpyxl/styles/builtins.py` |
| debt | 21 | 9 | 0 | `openpyxl-3.1.5/openpyxl/drawing/geometry.py` |
| mutation | 16465 | 164 | 162 | `openpyxl-3.1.5/openpyxl/pivot/table.py` |
| dead_code | 12 | 5 | 0 | `openpyxl-3.1.5/openpyxl/packaging/interface.py` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 3 | 2 | 0 | `openpyxl-3.1.5/openpyxl/utils/dataframe.py` |
| ui | 5 | 5 | 0 | `openpyxl-3.1.5/openpyxl/chart/marker.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.3333**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `openpyxl-3.1.5/openpyxl/reader/excel.py` (Hits: 7)
- `openpyxl-3.1.5/openpyxl/worksheet/_writer.py` (Hits: 4)
- `openpyxl-3.1.5/setup.py` (Hits: 4)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **serialisable.py** (`openpyxl-3.1.5/openpyxl/descriptors/serialisable.py`) — 102 inbound connections
2. **__init__.py** (`openpyxl-3.1.5/openpyxl/descriptors/__init__.py`) — 101 inbound connections
3. **base.py** (`openpyxl-3.1.5/openpyxl/descriptors/base.py`) — 101 inbound connections
4. **excel.py** (`openpyxl-3.1.5/openpyxl/descriptors/excel.py`) — 62 inbound connections
5. **sequence.py** (`openpyxl-3.1.5/openpyxl/descriptors/sequence.py`) — 59 inbound connections

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
- `parse_cell` **(Many-Argument Workhorses)** (@ `openpyxl-3.1.5/openpyxl/worksheet/_reader.py`) -> Impact: **37.4** | LOC: 56
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
| `openpyxl-3.1.5/openpyxl/worksheet` | 27 | 4839.4 | 35.95% | 6.02% |
| `openpyxl-3.1.5/openpyxl/drawing` | 16 | 2610.86 | 36.29% | 5.15% |
| `openpyxl-3.1.5/openpyxl/chart` | 31 | 2186.62 | 24.53% | 0.0% |
| `openpyxl-3.1.5/openpyxl/styles` | 16 | 1871.62 | 42.09% | 0.0% |
| `openpyxl-3.1.5/openpyxl/pivot` | 5 | 1708.76 | 31.88% | 15.24% |
| `openpyxl-3.1.5/openpyxl/workbook` | 12 | 1300.42 | 20.26% | 0.0% |
| `openpyxl-3.1.5/openpyxl/descriptors` | 9 | 1059.98 | 51.57% | 4.19% |
| `openpyxl-3.1.5/openpyxl/cell` | 6 | 879.54 | 54.86% | 0.0% |
| `openpyxl-3.1.5/openpyxl/packaging` | 8 | 817.62 | 28.7% | 12.5% |
| `openpyxl-3.1.5/openpyxl/utils` | 11 | 772.48 | 26.18% | 12.17% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `openpyxl-3.1.5/openpyxl/packaging/interface.py` -> **99.9925%** Exposure
- `openpyxl-3.1.5/openpyxl/utils/inference.py` -> **97.0688%** Exposure
- `openpyxl-3.1.5/openpyxl/worksheet/page.py` -> **80.3174%** Exposure
- `openpyxl-3.1.5/openpyxl/pivot/fields.py` -> **76.1878%** Exposure
- `openpyxl-3.1.5/openpyxl/worksheet/filters.py` -> **59.6324%** Exposure
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
- **Unknown Dependencies:** `724` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `openpyxl-3.1.5/openpyxl/pivot/table.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.655)
- **Top Global Matches:** file_cluster_15: 5.655, file_cluster_16: 6.914, file_cluster_2: 7.85
- **Magnitude:** 833.56 | **LOC:** 1262 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 2.281; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.6%), Guard Balance (formerly Safety Score) (76.7%)
- **Documentation Coverage:** 81.6327% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 18.1)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 12.4)
  * `by_priority` **(Compute Cores)** (Impact: 7.9)
    * *Intent:* """ Return a dictionary of format objects keyed by (field id and format property). This can be used ...
  * `_write_rels` **(Stateful Encapsulated Methods)** (Impact: 6.8)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.281
  * `Choke Point (Betweenness):` 0.005804 | `Ripple Effect (Closeness):` 0.190436
  * `Imports (Out-Degree: 10):` .fields, collections, openpyxl.descriptors, openpyxl.descriptors.excel, openpyxl.descriptors.sequence, openpyxl.descriptors.serialisable, openpyxl.packaging.relationship, openpyxl.worksheet.filters...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/worksheet.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.615)
- **Top Global Matches:** file_cluster_12: 6.615, file_cluster_16: 7.809, file_cluster_15: 8.029
- **Magnitude:** 815.74 | **LOC:** 908 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **26**; blast radius 4.904; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.6%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 26.1682% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `append` **(Stateful Encapsulated Methods)** (Impact: 23.1)
    * *Intent:* """Appends a group of values at the bottom of the current sheet. * If it's a list: all values are ad...
  * `__getitem__` **(Defensive Guards)** (Impact: 22.7)
    * *Intent:* """Convenience access by Excel style coordinates The key can be a single cell coordinate 'A1', a ran...
  * `move_range` **(Many-Argument Workhorses)** (Impact: 21.0)
    * *Intent:* """ Move a cell range by the number of rows and/or columns: down if rows > 0 and up if rows < 0 righ...
  * `_move_cells` **(Stateful Encapsulated Methods)** (Impact: 20.9)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.904
  * `Choke Point (Betweenness):` 0.024781 | `Ripple Effect (Closeness):` 0.168451
  * `Imports (Out-Degree: 24):` .cell_range, .datavalidation, .dimensions, .filters, .formula, .merge, .page, .pagebreak...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/pivot/cache.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.07)
- **Top Global Matches:** file_cluster_15: 6.07, file_cluster_16: 7.057, file_cluster_2: 7.736
- **Magnitude:** 604.6 | **LOC:** 966 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 1.994; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.0%), Complexity Load (formerly Cognitive Load) (80.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.2%)
- **Documentation Coverage:** 94.5946% of unit weight undocumented
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.994
  * `Choke Point (Betweenness):` 0.000105 | `Ripple Effect (Closeness):` 0.153075
  * `Imports (Out-Degree: 11):` .fields, .table, openpyxl.descriptors, openpyxl.descriptors.excel, openpyxl.descriptors.nested, openpyxl.descriptors.sequence, openpyxl.descriptors.serialisable, openpyxl.packaging.relationship...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/_reader.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.295)
- **Top Global Matches:** file_cluster_12: 7.295, file_cluster_4: 8.9, file_cluster_15: 9.434
- **Magnitude:** 534.5 | **LOC:** 473 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **30**; blast radius 2.528; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (62.8%)
- **Documentation Coverage:** 85.1852% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_cell` **(Many-Argument Workhorses)** (Impact: 37.4)
  * `parse_row` **(Type Conversions)** (Impact: 16.7)
  * `parse_formula` **(Compute Cores)** (Impact: 13.4)
    * *Intent:* """ possible formulae types: shared, array, datatable """
  * `bind_hyperlinks` **(Defensive Guards)** (Impact: 12.2)
  * `parse` **(I/O & Config Routines)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 323
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 102`, `args: 27`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 157`
* *Architecture:* `api: 26`, `import: 30`
* *Defense:* `safety: 9`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.528
  * `Choke Point (Betweenness):` 0.074902 | `Ripple Effect (Closeness):` 0.192392
  * `Imports (Out-Degree: 28):` .datavalidation, .dimensions, .filters, .formula, .header_footer, .hyperlink, .merge, .page...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/drawing/text.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.503)
- **Top Global Matches:** file_cluster_15: 5.503, file_cluster_2: 7.149, file_cluster_11: 7.653
- **Magnitude:** 442.22 | **LOC:** 718 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 2.893; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.893
  * `Choke Point (Betweenness):` 0.000724 | `Ripple Effect (Closeness):` 0.129893
  * `Imports (Out-Degree: 11):` .colors, .effect, .fill, .geometry, openpyxl.descriptors, openpyxl.descriptors.excel, openpyxl.descriptors.nested, openpyxl.descriptors.serialisable...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/formula/tokenizer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.602)
- **Top Global Matches:** file_cluster_12: 6.602, file_cluster_15: 8.108, file_cluster_16: 8.423
- **Magnitude:** 418.6 | **LOC:** 447 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 4.515; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.4%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 13.7931% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_parse_string` **(Stateful Encapsulated Methods)** (Impact: 22.6)
    * *Intent:* """ Parse a "-delimited string or '-delimited link. The offset must be pointing to either a single q...
  * `_parse_operator` **(Stateful Encapsulated Methods)** (Impact: 20.2)
    * *Intent:* """ Consume the characters constituting an operator. Returns the number of characters consumed. (Doe...
  * `_parse` **(Stateful Encapsulated Methods)** (Impact: 17.5)
    * *Intent:* """Populate self.items with the tokens from the formula."""
  * `make_subexp` **(Defensive Guards)** (Impact: 17.0)
    * *Intent:* """ Create a subexpression token. `value`: The value of the token `func`: If True, force the token t...
  * `_parse_separator` **(Stateful Encapsulated Methods)** (Impact: 9.7)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.515
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.143707
  * `Imports (Out-Degree: 0):` re
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/drawing/spreadsheet_drawing.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.251)
- **Top Global Matches:** file_cluster_12: 6.251, file_cluster_16: 7.986, file_cluster_15: 8.777
- **Magnitude:** 371.74 | **LOC:** 383 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **17**; blast radius 4.498; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (54.6%)
- **Documentation Coverage:** 62.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_write` **(Stateful Encapsulated Methods)** (Impact: 18.6)
    * *Intent:* """ create required structure and the serialise """
  * `_blip_rels` **(Stateful Encapsulated Methods)** (Impact: 12.2)
    * *Intent:* """ Get relationship information for each blip and bind anchor to it Images that are not part of the...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 8.0)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 7.3)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 258
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 70`, `args: 17`, `func_start: 17`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 146`
* *Architecture:* `api: 13`, `import: 17`
* *Defense:* `safety: 7`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.498
  * `Choke Point (Betweenness):` 0.113647 | `Ripple Effect (Closeness):` 0.199569
  * `Imports (Out-Degree: 20):` .connector, .fill, .geometry, .graphic, .picture, .relation, .xdr, openpyxl.chart._chart...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/filters.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.399)
- **Top Global Matches:** file_cluster_15: 5.399, file_cluster_16: 6.061, file_cluster_12: 7.513
- **Magnitude:** 360.02 | **LOC:** 487 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **6**; blast radius 2.448; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.6%), Complexity Load (formerly Cognitive Load) (70.8%)
- **Documentation Coverage:** 77.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 20.1)
  * `to_tree` **(Compute Cores)** (Impact: 7.0)
  * `_guess_operator` **(Stateful Encapsulated Methods)** (Impact: 6.4)
  * `convert` **(Type Conversions)** (Impact: 4.8)
    * *Intent:* """Convert to more specific filter"""
  * `_get_subtype` **(Stateful Encapsulated Methods)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 230
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 72`, `args: 28`, `func_start: 28`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 166`, `duplicate_logic: 4`
* *Architecture:* `api: 22`, `import: 6`
* *Defense:* `safety: 2`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.448
  * `Choke Point (Betweenness):` 0.000532 | `Ripple Effect (Closeness):` 0.167948
  * `Imports (Out-Degree: 7):` openpyxl.descriptors, openpyxl.descriptors.excel, openpyxl.descriptors.sequence, openpyxl.descriptors.serialisable, openpyxl.utils, re
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/descriptors/serialisable.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.346)
- **Top Global Matches:** file_cluster_6: 7.346, file_cluster_8: 12.593, file_cluster_4: 13.822
- **Magnitude:** 343.26 | **LOC:** 241 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **102** in-repo importer(s); it depends on **8**; blast radius 40.306; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (87.1%), Complexity Load (formerly Cognitive Load) (86.9%), Guard Balance (formerly Safety Score) (84.5%)
- **Documentation Coverage:** 92.3077% of unit weight undocumented
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 40.306
  * `Choke Point (Betweenness):` 0.015346 | `Ripple Effect (Closeness):` 0.535034
  * `Imports (Out-Degree: 6):` .Descriptor, .MetaSerialisable, .namespace, .sequence, copy, keyword, openpyxl.compat, openpyxl.xml.functions
  * `Imported By (In-Degree: 102):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/_writer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.697)
- **Top Global Matches:** file_cluster_12: 5.697, file_cluster_15: 8.28, file_cluster_7: 8.709
- **Magnitude:** 334.58 | **LOC:** 391 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **17**; blast radius 2.269; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.0%), Connectivity (formerly Api Exposure) (69.2%)
- **Documentation Coverage:** 69.5652% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 62`
* *Architecture:* `io: 4`, `api: 35`, `import: 17`
* *Defense:* `safety: 5`, `doc: 10`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.269
  * `Choke Point (Betweenness):` 0.008092 | `Ripple Effect (Closeness):` 0.131105
  * `Imports (Out-Degree: 12):` .dimensions, .hyperlink, .merge, .related, .table, atexit, collections, io...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/workbook/workbook.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.768)
- **Top Global Matches:** file_cluster_12: 7.768, file_cluster_15: 10.029, file_cluster_5: 10.086
- **Magnitude:** 325.14 | **LOC:** 439 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **31**; blast radius 8.955; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 34.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `active` **(Stateful Encapsulated Methods)** (Impact: 11.3)
    * *Intent:* """Set the active sheet"""
  * `_add_sheet` **(Stateful Encapsulated Methods)** (Impact: 10.7)
    * *Intent:* """Add an worksheet (at an optional index)."""
  * `_duplicate_name` **(Stateful Encapsulated Methods)** (Impact: 9.3)
    * *Intent:* """ Check for duplicate name in defined name list and table list of each worksheet. Names are not ca...
  * `mime_type` **(Compute Cores)** (Impact: 9.0)
    * *Intent:* """ The mime type is determined by whether a workbook is a template or not and whether it contains m...
  * `create_sheet` **(Compute Cores)** (Impact: 8.9)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.955
  * `Choke Point (Betweenness):` 0.094343 | `Ripple Effect (Closeness):` 0.191736
  * `Imports (Out-Degree: 32):` .child, .defined_name, .properties, .protection, .views, copy, openpyxl.chartsheet, openpyxl.compat...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/cell_range.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.696)
- **Top Global Matches:** file_cluster_15: 5.696, file_cluster_16: 7.54, file_cluster_13: 8.099
- **Magnitude:** 325.06 | **LOC:** 513 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **7**; blast radius 3.591; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (70.4%), Guard Balance (formerly Safety Score) (67.6%)
- **Documentation Coverage:** 32.3944% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 18.0)
  * `__ne__` **(Defensive Guards)** (Impact: 7.9)
    * *Intent:* """ Test whether the ranges are not equal. :type other: openpyxl.worksheet.cell_range.CellRange :par...
  * `isdisjoint` **(Compute Cores)** (Impact: 7.8)
    * *Intent:* """ Return ``True`` if this range has no cell in common with *other*. Ranges are disjoint if and onl...
  * `_check_title` **(Stateful Encapsulated Methods)** (Impact: 7.5)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.591
  * `Choke Point (Betweenness):` 0.000668 | `Ripple Effect (Closeness):` 0.170496
  * `Imports (Out-Degree: 6):` copy, itertools, openpyxl.descriptors, openpyxl.descriptors.sequence, openpyxl.descriptors.serialisable, openpyxl.utils, operator
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/reader/excel.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.566)
- **Top Global Matches:** file_cluster_4: 6.566, file_cluster_12: 10.145, file_cluster_15: 10.622
- **Magnitude:** 323.82 | **LOC:** 350 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **24**; blast radius 7.674; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (52.6%)
- **Documentation Coverage:** 95.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_worksheets` **(Compute Cores)** (Impact: 29.1)
  * `_validate_archive` **(Stateful Encapsulated Methods)** (Impact: 12.9)
    * *Intent:* """ Does a first check whether filename is a string or a file-like object. If it is a string represe...
  * `read_chartsheet` **(Many-Argument Workhorses)** (Impact: 9.0)
  * `_find_workbook_part` **(Stateful Encapsulated Methods)** (Impact: 7.8)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.674
  * `Choke Point (Betweenness):` 0.490856 | `Ripple Effect (Closeness):` 0.246939
  * `Imports (Out-Degree: 22):` ..tests, .drawings, .strings, .workbook, io, openpyxl.cell, openpyxl.chartsheet, openpyxl.comments.comment_sheet...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/styles/stylesheet.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.594)
- **Top Global Matches:** file_cluster_16: 7.594, file_cluster_12: 7.741, file_cluster_15: 8.649
- **Magnitude:** 296.92 | **LOC:** 275 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **18**; blast radius 2.273; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (51.4%)
- **Documentation Coverage:** 62.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 20.0)
  * `_normalise_numbers` **(Stateful Encapsulated Methods)** (Impact: 12.6)
    * *Intent:* """ Rebase custom numFmtIds with a floor of 164 when reading stylesheet And index datetime formats "...
  * `apply_stylesheet` **(Many-Argument Workhorses)** (Impact: 12.5)
    * *Intent:* """ Add styles to workbook if present """
  * `_expand_named_style` **(Stateful Encapsulated Methods)** (Impact: 11.8)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.273
  * `Choke Point (Betweenness):` 0.017151 | `Ripple Effect (Closeness):` 0.192063
  * `Imports (Out-Degree: 18):` .borders, .builtins, .cell_style, .colors, .differential, .fills, .fonts, .named_styles...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/drawing/geometry.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.119)
- **Top Global Matches:** file_cluster_15: 5.119, file_cluster_2: 6.409, file_cluster_11: 7.036
- **Magnitude:** 296.5 | **LOC:** 585 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **6**; blast radius 5.405; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.0%), Guard Balance (formerly Safety Score) (69.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.405
  * `Choke Point (Betweenness):` 0.009063 | `Ripple Effect (Closeness):` 0.184494
  * `Imports (Out-Degree: 7):` .line, openpyxl.descriptors, openpyxl.descriptors.excel, openpyxl.descriptors.serialisable, openpyxl.styles.colors, openpyxl.xml.constants
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/table.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.323)
- **Top Global Matches:** file_cluster_15: 5.323, file_cluster_16: 6.784, file_cluster_11: 8.009
- **Magnitude:** 285.08 | **LOC:** 386 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **10**; blast radius 2.533; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.6%), Connectivity (formerly Api Exposure) (67.0%)
- **Documentation Coverage:** 82.3529% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 13.6)
  * `get` **(Compute Cores)** (Impact: 8.3)
  * `_initialise_columns` **(Stateful Encapsulated Methods)** (Impact: 6.3)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.533
  * `Choke Point (Betweenness):` 0.009482 | `Ripple Effect (Closeness):` 0.200997
  * `Imports (Out-Degree: 12):` .filters, .related, openpyxl.descriptors, openpyxl.descriptors.excel, openpyxl.descriptors.sequence, openpyxl.descriptors.serialisable, openpyxl.utils, openpyxl.utils.escape...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/dimensions.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.186)
- **Top Global Matches:** file_cluster_15: 5.186, file_cluster_16: 7.786, file_cluster_13: 7.897
- **Magnitude:** 281.38 | **LOC:** 307 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 2.308; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.8%), Connectivity (formerly Api Exposure) (69.1%)
- **Documentation Coverage:** 65.7143% of unit weight undocumented
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.308
  * `Choke Point (Betweenness):` 0.008878 | `Ripple Effect (Closeness):` 0.165718
  * `Imports (Out-Degree: 11):` copy, openpyxl.compat, openpyxl.descriptors, openpyxl.descriptors.serialisable, openpyxl.styles.styleable, openpyxl.utils, openpyxl.utils.bound_dictionary, openpyxl.utils.units...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/cell/cell.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.177)
- **Top Global Matches:** file_cluster_15: 6.177, file_cluster_16: 7.457, file_cluster_13: 8.103
- **Magnitude:** 274.7 | **LOC:** 333 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **11**; blast radius 3.996; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 37.2093% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_bind_value` **(Stateful Encapsulated Methods)** (Impact: 20.5)
    * *Intent:* """Given a value, infer the correct data type"""
  * `hyperlink` **(Stateful Encapsulated Methods)** (Impact: 11.1)
    * *Intent:* """Set value and display for hyperlinks in a cell. Automatically sets the `value` of the cell with l...
  * `get_type` **(Defensive Guards)** (Impact: 11.0)
  * `comment` **(Stateful Encapsulated Methods)** (Impact: 9.3)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.996
  * `Choke Point (Betweenness):` 0.014553 | `Ripple Effect (Closeness):` 0.169213
  * `Imports (Out-Degree: 11):` copy, datetime, openpyxl.cell.rich_text, openpyxl.compat, openpyxl.styles, openpyxl.styles.styleable, openpyxl.utils, openpyxl.utils.exceptions...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/chart/axis.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.361)
- **Top Global Matches:** file_cluster_15: 5.361, file_cluster_2: 6.869, file_cluster_11: 7.419
- **Magnitude:** 268.74 | **LOC:** 402 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **10**; blast radius 3.16; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (77.0%), Complexity Load (formerly Cognitive Load) (76.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 81.8182% of unit weight undocumented
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.16
  * `Choke Point (Betweenness):` 0.00241 | `Ripple Effect (Closeness):` 0.120168
  * `Imports (Out-Degree: 11):` .descriptors, .layout, .shapes, .text, .title, openpyxl.descriptors, openpyxl.descriptors.excel, openpyxl.descriptors.nested...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/worksheet/header_footer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.378)
- **Top Global Matches:** file_cluster_12: 6.378, file_cluster_15: 6.936, file_cluster_16: 8.113
- **Magnitude:** 264.16 | **LOC:** 271 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **6**; blast radius 5.067; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.6%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 25.9)
  * `from_str` **(Compute Cores)** (Impact: 10.9)
    * *Intent:* """ Convert from miniformat to object """
  * `__str__` **(Compute Cores)** (Impact: 9.9)
    * *Intent:* """ Pack parts into a single string """
  * `__init__` **(Compute Cores)** (Impact: 9.4)
  * `from_tree` **(Compute Cores)** (Impact: 7.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 166
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 37`, `args: 13`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 76`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 2`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.067
  * `Choke Point (Betweenness):` 0.005303 | `Ripple Effect (Closeness):` 0.168958
  * `Imports (Out-Degree: 5):` openpyxl.descriptors, openpyxl.descriptors.serialisable, openpyxl.utils.escape, openpyxl.xml.functions, re, warnings
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/drawing/fill.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.52)
- **Top Global Matches:** file_cluster_15: 5.52, file_cluster_2: 7.0, file_cluster_11: 7.571
- **Magnitude:** 255.88 | **LOC:** 426 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **8**; blast radius 3.494; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (77.6%), Guard Balance (formerly Safety Score) (74.3%), Connectivity (formerly Api Exposure) (57.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.494
  * `Choke Point (Betweenness):` 0.004212 | `Ripple Effect (Closeness):` 0.185714
  * `Imports (Out-Degree: 9):` .colors, .effect, openpyxl.descriptors, openpyxl.descriptors.excel, openpyxl.descriptors.nested, openpyxl.descriptors.sequence, openpyxl.descriptors.serialisable, openpyxl.xml.constants
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/drawing/colors.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.91)
- **Top Global Matches:** file_cluster_15: 5.91, file_cluster_2: 7.42, file_cluster_16: 7.879
- **Magnitude:** 254.24 | **LOC:** 436 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **6**; blast radius 3.932; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (77.2%), Guard Balance (formerly Safety Score) (72.7%), Connectivity (formerly Api Exposure) (51.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.932
  * `Choke Point (Betweenness):` 0.000623 | `Ripple Effect (Closeness):` 0.159146
  * `Imports (Out-Degree: 7):` openpyxl.descriptors, openpyxl.descriptors.excel, openpyxl.descriptors.nested, openpyxl.descriptors.serialisable, openpyxl.styles.colors, openpyxl.xml.constants
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/writer/excel.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.285)
- **Top Global Matches:** file_cluster_12: 6.285, file_cluster_16: 8.648, file_cluster_7: 8.669
- **Magnitude:** 252.26 | **LOC:** 296 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 2.068; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.4%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_write_worksheets` **(Stateful Encapsulated Methods)** (Impact: 17.9)
  * `_write_comment` **(Stateful Encapsulated Methods)** (Impact: 8.0)
  * `write_data` **(Compute Cores)** (Impact: 7.8)
  * `_merge_vba` **(Stateful Encapsulated Methods)** (Impact: 7.8)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.068
  * `Choke Point (Betweenness):` 0.020298 | `Ripple Effect (Closeness):` 0.154975
  * `Imports (Out-Degree: 12):` .theme, datetime, openpyxl.comments.comment_sheet, openpyxl.drawing.spreadsheet_drawing, openpyxl.packaging.extended, openpyxl.packaging.manifest, openpyxl.packaging.relationship, openpyxl.styles.stylesheet...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/utils/cell.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.727)
- **Top Global Matches:** file_cluster_4: 6.727, file_cluster_6: 10.638, file_cluster_15: 11.634
- **Magnitude:** 250.62 | **LOC:** 241 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **5**; blast radius 13.977; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.4%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.977
  * `Choke Point (Betweenness):` 0.00113 | `Ripple Effect (Closeness):` 0.205836
  * `Imports (Out-Degree: 1):` .exceptions, functools, itertools, re, string
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `openpyxl-3.1.5/openpyxl/descriptors/base.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.054)
- **Top Global Matches:** file_cluster_12: 6.054, file_cluster_15: 8.468, file_cluster_7: 8.818
- **Magnitude:** 244.36 | **LOC:** 273 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **101** in-repo importer(s); it depends on **5**; blast radius 69.784; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (69.3%), Guard Balance (formerly Safety Score) (68.6%)
- **Documentation Coverage:** 97.0588% of unit weight undocumented
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 69.784
  * `Choke Point (Betweenness):` 0.436466 | `Ripple Effect (Closeness):` 0.561786
  * `Imports (Out-Degree: 3):` .namespace, datetime, openpyxl, openpyxl.utils.datetime, re
  * `Imported By (In-Degree: 101):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `openpyxl-3.1.5/setup.py` (PYTHON) | Magnitude: 25.0 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 52, core_var_decl: 32, design_snake_case: 30, state_mutation: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `openpyxl-3.1.5/openpyxl/chart/trendline.py` (PYTHON) | Magnitude: 53.16 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 71, core_var_decl: 43, state_mutation: 41, design_camel_case: 23
- `openpyxl-3.1.5/openpyxl/cell/rich_text.py` (PYTHON) | Magnitude: 176.56 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 115, structural_boundaries: 50, state_mutation: 34, branch: 31
- `openpyxl-3.1.5/openpyxl/chart/bar_chart.py` (PYTHON) | Magnitude: 73.82 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 98, state_mutation: 59, core_var_decl: 55, structural_boundaries: 31
- `openpyxl-3.1.5/openpyxl/chart/error_bar.py` (PYTHON) | Magnitude: 30.32 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 42, core_var_decl: 24, state_mutation: 23, structural_boundaries: 14
- `openpyxl-3.1.5/openpyxl/chart/plotarea.py` (PYTHON) | Magnitude: 125.88 | Delta: **0.144** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 108, state_mutation: 60, core_var_decl: 58, structural_boundaries: 48

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `openpyxl-3.1.5/openpyxl/comments/comments.py` (PYTHON) | Magnitude: 52.16 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 15, state_mutation: 12, api: 10
- `openpyxl-3.1.5/openpyxl/styles/stylesheet.py` (PYTHON) | Magnitude: 296.92 | Delta: **0.147** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 177, state_mutation: 92, structural_boundaries: 57, core_var_decl: 55

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `openpyxl-3.1.5/openpyxl/chart/__init__.py` (PYTHON) | Magnitude: 15.32 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 23, import: 11, indent_spaces: 4
- `openpyxl-3.1.5/openpyxl/styles/__init__.py` (PYTHON) | Magnitude: 14.16 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 16, import: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `openpyxl-3.1.5/openpyxl/chart/reader.py` (PYTHON) | Magnitude: 29.48 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 18, state_mutation: 16, core_var_decl: 3, design_snake_case: 3
- `openpyxl-3.1.5/openpyxl/packaging/extended.py` (PYTHON) | Magnitude: 77.92 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 95, state_mutation: 60, core_var_decl: 60, design_pascal_case: 54

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `openpyxl-3.1.5/openpyxl/__init__.py` -> **Severity: 52.754** (Bridge: 0.549 * Flux: 96.0834%)
- `openpyxl-3.1.5/openpyxl/reader/excel.py` -> **Severity: 49.086** (Bridge: 0.4909 * Flux: 100.0%)
- `openpyxl-3.1.5/openpyxl/descriptors/base.py` -> **Severity: 43.647** (Bridge: 0.4365 * Flux: 100.0%)
- `openpyxl-3.1.5/openpyxl/drawing/spreadsheet_drawing.py` -> **Severity: 11.365** (Bridge: 0.1136 * Flux: 100.0%)
- `openpyxl-3.1.5/openpyxl/xml/functions.py` -> **Severity: 10.108** (Bridge: 0.1011 * Flux: 99.9763%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `openpyxl-3.1.5/openpyxl/descriptors/serialisable.py` -> **Severity: 45.189** (Embedded: 0.535 * Error Risk: 84.4609%)
- `openpyxl-3.1.5/openpyxl/descriptors/__init__.py` -> **Severity: 43.575** (Embedded: 0.5402 * Error Risk: 80.6679%)
- `openpyxl-3.1.5/openpyxl/descriptors/base.py` -> **Severity: 38.545** (Embedded: 0.5618 * Error Risk: 68.6116%)
- `openpyxl-3.1.5/openpyxl/descriptors/sequence.py` -> **Severity: 34.04** (Embedded: 0.4476 * Error Risk: 76.0433%)
- `openpyxl-3.1.5/openpyxl/xml/constants.py` -> **Severity: 30.958** (Embedded: 0.3929 * Error Risk: 78.7985%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `openpyxl-3.1.5/openpyxl/descriptors/base.py` -> **Severity: 6773.151** (Blast Radius: 69.784 * Doc Risk: 97.0588%)
- `openpyxl-3.1.5/openpyxl/descriptors/__init__.py` -> **Severity: 5422.0** (Blast Radius: 54.22 * Doc Risk: 100.0%)
- `openpyxl-3.1.5/openpyxl/descriptors/sequence.py` -> **Severity: 3901.52** (Blast Radius: 48.769 * Doc Risk: 80.0%)
- `openpyxl-3.1.5/openpyxl/descriptors/serialisable.py` -> **Severity: 3720.554** (Blast Radius: 40.306 * Doc Risk: 92.3077%)
- `openpyxl-3.1.5/openpyxl/xml/functions.py` -> **Severity: 2810.8** (Blast Radius: 28.108 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2980 call pairs -- scoped 46.6%, unique 0.0%, ambiguous 13.7%, external 39.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 2980 | 46.6% | 0.0% | 13.7% | 39.7% |

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
