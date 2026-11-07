# ARCHITECTURAL_BRIEF: pandas
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/pandas-dev/pandas.git` |
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
- **Scope:** 1914 analyzed artifact(s), 457018 LOC.
- **Load-bearing artifact:** `pandas/__init__.py` -- 1124 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `pandas/core/frame.py` -- pulls in 78 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `pandas/core/frame.py` at magnitude 6455.44 (structural weight, not risk).
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
| Total Artifacts | 2632 |
| Analyzed Artifacts (Scanned) | 1914 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 718 |
| Total LOC | 457018 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 72.7% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.308 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3121 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 14.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.4269 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 37 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 1620 | 445642 | 84.6% |
| HTML | 115 | 6299 | 6.0% |
| XML | 45 | 5 | 2.4% |
| YAML | 44 | 2326 | 2.3% |
| MARKDOWN | 36 | 0 | 1.9% |
| CSV | 25 | 1110 | 1.3% |
| JSON | 9 | 250 | 0.5% |
| C | 7 | 622 | 0.4% |
| PLAINTEXT | 6 | 0 | 0.3% |
| CSS | 4 | 529 | 0.2% |
| SHELL | 3 | 235 | 0.2% |

## 4.1 SOURCE ENCODINGS
> 4 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 1907 |
| cp1252 | cp1252-fallback | 3 |
| utf-16-le | bom | 2 |
| latin-1 | latin-1-fallback | 1 |
| utf-32-le | bom | 1 |

> 1 guessed file(s) read as double-byte text that decodes strictly as shift_jis / gbk: if that is the estate's code page, rescan with `--source-encoding shift_jis` (or the right one of those). E.g. `pandas/tests/io/parser/data/sauron.SHIFT_JIS.csv`.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 23%, Large Core Modules (2) 22%, Large Core Modules (3) 19%, Parameter Forwarders Files 13%, Many-Argument Workhorses Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1865 | 97.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 42 | 2.2% |
| Static: Minified & Vendor Opaque Mass | 7 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 718*

**Composition by Extension & Reason:**
- `.rst`: 219x Excluded (Unsupported Extension: '.rst')
- `.dta`: 111x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 69x Excluded (Explicitly Denied Extension: '.png')
- `.xlsx`: 36x Excluded (Explicitly Denied Extension: '.xlsx')
- `.ods`: 30x Excluded (Explicitly Denied Extension: '.ods')
- `.sas7bdat`: 30x Excluded (Unsupported Extension: '.sas7bdat')
- `.xls`: 26x Excluded (Explicitly Denied Extension: '.xls')
- `.xlsb`: 25x Excluded (Unsupported Extension: '.xlsb')
- `.xlsm`: 25x Excluded (Unsupported Extension: '.xlsm')
- `no_extension`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.csv`: 1x Excluded (Massive Static Asset Blob: 5274 LOC), 1x Excluded (Static Asset Blob without Intent: 1037 LOC), 1x Excluded (Static Asset Blob without Intent: 2070 LOC)
- `.c`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h5`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tpl`: 9x Excluded (Unsupported Extension: '.tpl')
- `.pickle`: 9x Excluded (Unsupported Extension: '.pickle')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 25.8 | 27.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 89.9 | 46.2 | 54.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 5.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 9.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 14.8 | 9.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 65.4 | 0.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 21.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 62.9 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.9 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 6.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 71.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5836 | 745 | 9 | `pandas/tests/frame/test_subclass.py` |
| cleanup | 126 | 34 | 0 | `pandas/tests/io/pytables/test_file_handling.py` |
| guards | 28761 | 1175 | 41 | `pandas/tests/dtypes/test_inference.py` |
| danger | 7060 | 644 | 8 | `pandas/tests/computation/test_eval.py` |
| concurrency | 433 | 119 | 0 | `pandas/io/sql.py` |
| connectivity | 31296 | 1508 | 43 | `pandas/tests/extension/test_arrow.py` |
| io | 1243 | 181 | 0 | `pandas/tests/io/data/html/banklist.html` |
| crypto | 1 | 1 | 0 | `pandas/tests/io/pytables/test_store.py` |
| ipc | 52 | 10 | 0 | `pandas/io/clipboard/__init__.py` |
| time | 1033 | 205 | 1 | `pandas/_libs/tslibs/offsets.pyx` |
| serialization | 15 | 9 | 0 | `pandas/tests/copy_view/test_astype.py` |
| regex | 146 | 57 | 0 | `pandas/tests/strings/test_find_replace.py` |
| events | 52 | 17 | 0 | `pandas/tests/io/data/html/banklist.html` |
| tests | 36314 | 1037 | 53 | `pandas/tests/io/test_sql.py` |
| docs | 6442 | 757 | 7 | `pandas/core/indexes/base.py` |
| debt | 1803 | 459 | 3 | `pandas/_libs/tslibs/offsets.pyx` |
| mutation | 267813 | 1613 | 391 | `pandas/core/frame.py` |
| dead_code | 19706 | 1104 | 28 | `pandas/tests/extension/test_arrow.py` |
| credential | 45 | 9 | 0 | `doc/source/_static/schemas/03_subset_rows.svg` |
| threat | 78 | 13 | 0 | `pandas/io/sas/sas_constants.py` |
| ml_ai | 8151 | 1446 | 9 | `pandas/core/frame.py` |
| ui | 218 | 39 | 0 | `doc/source/whatsnew/whatsnew_0171_html_table.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pandas/tests/io/data/html/banklist.html` (Hits: 154)
- `pandas/tests/io/test_sql.py` (Hits: 102)
- `web/pandas/index.html` (Hits: 68)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`pandas/__init__.py`) — 1124 inbound connections
2. **__init__.py** (`pandas/_testing/__init__.py`) — 805 inbound connections
3. **frame.py** (`pandas/core/frame.py`) — 292 inbound connections
4. **multi.py** (`pandas/core/indexes/multi.py`) — 265 inbound connections
5. **__init__.py** (`pandas/errors/__init__.py`) — 240 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **frame.py** (`pandas/core/frame.py`) — 78 outbound dependencies
2. **generic.py** (`pandas/core/generic.py`) — 60 outbound dependencies
3. **base.py** (`pandas/core/indexes/base.py`) — 56 outbound dependencies
4. **series.py** (`pandas/core/series.py`) — 55 outbound dependencies
5. **array.py** (`pandas/core/arrays/arrow/array.py`) — 49 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `maybe_convert_objects` **(Many-Argument Workhorses)** (@ `pandas/_libs/lib.pyx`) -> Impact: **401.0** | LOC: 384
- `assert_series_equal` **(Many-Argument Workhorses)** (@ `pandas/_testing/asserters.py`) -> Impact: **268.8** | LOC: 285
  * *Intent:* # This could be refactored to use the NDFrame.equals method
- `__new__` **(Many-Argument Workhorses)** (@ `pandas/_libs/tslibs/period.pyx`) -> Impact: **242.5** | LOC: 138
- `__new__` **(Many-Argument Workhorses)** (@ `pandas/_libs/tslibs/timestamps.pyx`) -> Impact: **236.9** | LOC: 168
- `to_latex` **(Many-Argument Workhorses)** (@ `pandas/core/generic.py`) -> Impact: **234.9** | LOC: 286
- `maybe_convert_numeric` **(Many-Argument Workhorses)** (@ `pandas/_libs/lib.pyx`) -> Impact: **218.4** | LOC: 253
- `__cinit__` **(Many-Argument Workhorses)** (@ `pandas/_libs/parsers.pyx`) -> Impact: **217.7** | LOC: 218
- `convert_dtypes` **(Many-Argument Workhorses)** (@ `pandas/core/dtypes/cast.py`) -> Impact: **207.2** | LOC: 184
- `json_normalize` **(Many-Argument Workhorses)** (@ `pandas/io/json/_normalize.py`) -> Impact: **194.3** | LOC: 347
- `get_grouper` **(Many-Argument Workhorses)** (@ `pandas/core/groupby/grouper.py`) -> Impact: **191.8** | LOC: 215

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pandas/core` | 22 | 25770.76 | 42.54% | 10.5% |
| `pandas/_libs` | 64 | 19260.9 | 28.04% | 15.66% |
| `pandas/_libs/tslibs` | 47 | 15803.72 | 17.86% | 9.58% |
| `pandas/tests/frame/methods` | 80 | 15743.28 | 29.33% | 0.0% |
| `pandas/core/arrays` | 20 | 14258.26 | 56.23% | 5.98% |
| `pandas/io` | 16 | 13107.94 | 39.72% | 4.94% |
| `pandas/core/indexes` | 14 | 12898.4 | 44.39% | 9.64% |
| `pandas/tests/frame` | 22 | 11019.12 | 29.57% | 0.0% |
| `pandas/tests/groupby` | 24 | 10636.88 | 34.88% | 0.0% |
| `pandas/tests/io` | 19 | 9291.92 | 24.24% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `asv_bench/benchmarks/categoricals.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/frame_methods.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/io/hdf.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/strftime.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/strings.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `asv_bench/benchmarks/algorithms.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/algos/isin.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/array.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/attrs_caching.py` -> **100.0%** Exposure
- `asv_bench/benchmarks/categoricals.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pandas/tests/extension/test_arrow.py` -> **238** Orphaned Functions | **0** Duplicates
- `pandas/tests/frame/test_constructors.py` -> **222** Orphaned Functions | **0** Duplicates
- `pandas/tests/tools/test_to_datetime.py` -> **217** Orphaned Functions | **0** Duplicates
- `pandas/tests/indexing/test_loc.py` -> **215** Orphaned Functions | **0** Duplicates
- `pandas/tests/plotting/frame/test_frame.py` -> **172** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `10853` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `pandas/core/frame.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.992)
- **Top Global Matches:** file_cluster_4: 7.992, file_cluster_5: 10.689, file_cluster_12: 10.809
- **Magnitude:** 6455.44 | **LOC:** 18736 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 14.6%
- **Blast Radius:** changing it is visible to **292** in-repo importer(s); it depends on **78**; blast radius 10.903; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.7%), Connectivity (formerly Api Exposure) (71.7%)
- **Documentation Coverage:** 81.2268% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 153.0)
    * *Intent:* # ---------------------------------------------------------------------- # Constructors
  * `from_records` **(Many-Argument Workhorses)** (Impact: 146.7)
  * `set_index` **(Many-Argument Workhorses)** (Impact: 99.4)
  * `select_dtypes` **(Many-Argument Workhorses)** (Impact: 95.1)
    * *Intent:* """ Return a subset of the DataFrame's columns based on the column dtypes. This method allows for fi...
  * `_align_for_op` **(Many-Argument Workhorses)** (Impact: 90.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 718 instances
* *High Risk Execution (weighted view):* 5
* *State Mutation (weighted view):* 2264
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 955`, `structural_boundaries: 866`, `args: 293`, `func_start: 291`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 87`, `high_risk_execution: 6`, `state_mutation: 828`, `dead_code: 1`, `planned_debt: 12`
* *Architecture:* `io: 2`, `api: 237`, `import: 95`
* *Defense:* `safety: 200`, `doc: 164`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.903
  * `Choke Point (Betweenness):` 0.01913 | `Ripple Effect (Closeness):` 0.314486
  * `Imports (Out-Degree: 69):` __future__, collections, collections.abc, datetime, functools, io, itertools, numpy...
  * `Imported By (In-Degree: 292):` (Excluded from Brief to save tokens)

### `pandas/core/generic.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.61)
- **Top Global Matches:** file_cluster_4: 7.61, file_cluster_12: 11.127, file_cluster_5: 11.433
- **Magnitude:** 5149.68 | **LOC:** 12805 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 19.4%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **60**; blast radius 6.875; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (77.0%), Guard Balance (formerly Safety Score) (69.1%)
- **Documentation Coverage:** 70.0483% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `to_latex` **(Many-Argument Workhorses)** (Impact: 234.9)
  * `replace` **(Many-Argument Workhorses)** (Impact: 185.5)
  * `fillna` **(Many-Argument Workhorses)** (Impact: 127.1)
  * `_where` **(Many-Argument Workhorses)** (Impact: 125.0)
  * `_rename` **(Many-Argument Workhorses)** (Impact: 99.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 549 instances
* *State Mutation (weighted view):* 1711
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 817`, `structural_boundaries: 679`, `args: 227`, `func_start: 222`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 613`, `dead_code: 1`, `planned_debt: 7`, `fragile_debt: 1`
* *Architecture:* `io: 8`, `api: 162`, `import: 69`
* *Defense:* `safety: 117`, `doc: 115`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.875
  * `Choke Point (Betweenness):` 0.007627 | `Ripple Effect (Closeness):` 0.274941
  * `Imports (Out-Degree: 60):` __future__, collections, collections.abc, copy, datetime, functools, json, numpy...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `pandas/io/pytables.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.158)
- **Top Global Matches:** file_cluster_4: 8.158, file_cluster_12: 9.502, file_cluster_5: 9.662
- **Magnitude:** 5048.88 | **LOC:** 5600 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **39**; blast radius 0.801; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.7%), Connectivity (formerly Api Exposure) (70.7%)
- **Documentation Coverage:** 56.5891% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_create_axes` **(Many-Argument Workhorses)** (Impact: 108.2)
  * `read` **(Many-Argument Workhorses)** (Impact: 76.1)
  * `_create_storer` **(Many-Argument Workhorses)** (Impact: 75.9)
  * `_maybe_convert_for_string_atom` **(Many-Argument Workhorses)** (Impact: 72.8)
  * `read_hdf` **(Many-Argument Workhorses)** (Impact: 70.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 712 instances
* *State Mutation (weighted view):* 2284
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 776`, `structural_boundaries: 703`, `args: 245`, `func_start: 239`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 860`, `dead_code: 12`, `planned_debt: 17`, `fragile_debt: 3`, `duplicate_logic: 6`
* *Architecture:* `io: 7`, `api: 200`, `import: 41`
* *Defense:* `safety: 178`, `doc: 146`, `immutability_locks: 6`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.801
  * `Choke Point (Betweenness):` 0.001472 | `Ripple Effect (Closeness):` 0.22534
  * `Imports (Out-Degree: 41):` __future__, collections.abc, contextlib, copy, datetime, itertools, numpy, os...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `pandas/core/indexes/base.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.02)
- **Top Global Matches:** file_cluster_4: 8.02, file_cluster_12: 10.192, file_cluster_5: 10.338
- **Magnitude:** 4925.96 | **LOC:** 8145 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **110** in-repo importer(s); it depends on **56**; blast radius 7.808; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.5%)
- **Documentation Coverage:** 42.8954% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `join` **(Many-Argument Workhorses)** (Impact: 96.2)
  * `_join_level` **(Many-Argument Workhorses)** (Impact: 85.7)
  * `__new__` **(Many-Argument Workhorses)** (Impact: 82.1)
    * *Intent:* # -------------------------------------------------------------------- # Constructors
  * `get_values_for_csv` **(Many-Argument Workhorses)** (Impact: 66.3)
  * `set_names` **(Many-Argument Workhorses)** (Impact: 65.3)
    * *Intent:* """ Set Index or MultiIndex name. Able to set new names partially and by level. Parameters ---------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 605 instances
* *State Mutation (weighted view):* 1910
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 980`, `structural_boundaries: 914`, `args: 235`, `func_start: 235`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 700`, `dead_code: 1`, `planned_debt: 25`, `fragile_debt: 1`
* *Architecture:* `api: 132`, `import: 74`
* *Defense:* `safety: 232`, `doc: 165`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.808
  * `Choke Point (Betweenness):` 0.00551 | `Ripple Effect (Closeness):` 0.304502
  * `Imports (Out-Degree: 55):` __future__, collections, collections.abc, copy, datetime, functools, itertools, numpy...
  * `Imported By (In-Degree: 110):` (Excluded from Brief to save tokens)

### `pandas/_libs/tslibs/offsets.pyx` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.279)
- **Top Global Matches:** file_cluster_4: 8.279, file_cluster_12: 8.854, file_cluster_16: 8.918
- **Magnitude:** 3492.2 | **LOC:** 7801 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 85.9%
- **Blast Radius:** changing it is visible to **29** in-repo importer(s); it depends on **16**; blast radius 1.142; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (93.1%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (78.8%)
- **Documentation Coverage:** 50.6925% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `to_offset` **(Many-Argument Workhorses)** (Impact: 66.8)
    * *Intent:* """ Return DateOffset object from string or datetime.timedelta object. Parameters ---------- freq : ...
  * `_apply` **(Many-Argument Workhorses)** (Impact: 46.4)
    * *Intent:* # used for detecting edge condition nanosecond = getattr(other, "nanosecond", 0) # reset timezone an...
  * `wrapper` **(Compute Cores)** (Impact: 37.3)
    * *Intent:* # Note: normally we would use `@functools.wraps(func)`, but this does # not play nicely with cython ...
  * `_next_opening_time` **(Many-Argument Workhorses)** (Impact: 37.1)
    * *Intent:* """ If self._n and sign have the same sign, return the earliest opening time later than or equal to ...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 36.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 435 instances
* *State Mutation (weighted view):* 1642
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 565`, `structural_boundaries: 680`, `args: 243`, `func_start: 243`, `class_start: 56`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 772`, `dead_code: 2`, `planned_debt: 12`, `fragile_debt: 1`, `duplicate_logic: 24`
* *Architecture:* `api: 103`, `import: 23`
* *Defense:* `safety: 64`, `doc: 150`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.142
  * `Choke Point (Betweenness):` 0.000196 | `Ripple Effect (Closeness):` 0.204204
  * `Imports (Out-Degree: 12):` .timedeltas, .timestamps, dateutil.easter, dateutil.relativedelta, numpy, pandas._libs.properties, pandas._libs.tslibs.ccalendar, pandas.core.dtypes.cast...
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `pandas/core/arrays/arrow/array.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.38)
- **Top Global Matches:** file_cluster_4: 9.38, file_cluster_5: 9.449, file_cluster_12: 10.357
- **Magnitude:** 3201.04 | **LOC:** 3440 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **45** in-repo importer(s); it depends on **49**; blast radius 3.665; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.0%), Complexity Load (formerly Cognitive Load) (74.5%)
- **Documentation Coverage:** 83.1579% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_reduce_pyarrow` **(Many-Argument Workhorses)** (Impact: 112.6)
    * *Intent:* """ Return a pyarrow scalar result of performing the reduction operation. Parameters ---------- name...
  * `_box_pa_array` **(Many-Argument Workhorses)** (Impact: 96.9)
  * `to_numpy` **(Many-Argument Workhorses)** (Impact: 64.5)
  * `__getitem__` **(Many-Argument Workhorses)** (Impact: 60.2)
    * *Intent:* """Select a subset of self. Parameters ---------- item : int, slice, or ndarray * int: The position ...
  * `_evaluate_op_method` **(Many-Argument Workhorses)** (Impact: 55.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 447 instances
* *State Mutation (weighted view):* 1459
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 547`, `structural_boundaries: 693`, `args: 180`, `func_start: 154`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 77`, `state_mutation: 565`, `dead_code: 1`, `planned_debt: 16`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 124`, `import: 60`
* *Defense:* `safety: 103`, `doc: 49`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.665
  * `Choke Point (Betweenness):` 0.002813 | `Ripple Effect (Closeness):` 0.296337
  * `Imports (Out-Degree: 43):` __future__, collections.abc, datetime, functools, numpy, operator, pandas, pandas._config...
  * `Imported By (In-Degree: 45):` (Excluded from Brief to save tokens)

### `pandas/io/stata.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.014)
- **Top Global Matches:** file_cluster_4: 9.014, file_cluster_5: 9.027, file_cluster_12: 9.195
- **Magnitude:** 3119.36 | **LOC:** 3939 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **28**; blast radius 0.52; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (49.8%)
- **Documentation Coverage:** 59.4771% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read` **(Many-Argument Workhorses)** (Impact: 141.7)
  * `_cast_to_stata_types` **(Compute Cores)** (Impact: 64.3)
    * *Intent:* """ Checks the dtypes of the columns of a pandas DataFrame for compatibility with the data types and...
  * `_datetime_to_stata_elapsed_vec` **(Many-Argument Workhorses)** (Impact: 47.3)
    * *Intent:* """ Convert from datetime to SIF. https://www.stata.com/help.cgi?datetime Parameters ---------- date...
  * `_read_old_header` **(Stateful Encapsulated Methods)** (Impact: 46.1)
  * `_do_convert_categoricals` **(Many-Argument Workhorses)** (Impact: 38.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 517 instances
* *State Mutation (weighted view):* 1682
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 526`, `structural_boundaries: 391`, `args: 132`, `func_start: 130`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 648`, `dead_code: 1`, `planned_debt: 9`, `fragile_debt: 2`
* *Architecture:* `io: 9`, `api: 30`, `import: 29`
* *Defense:* `safety: 43`, `doc: 72`, `immutability_locks: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.52
  * `Choke Point (Betweenness):` 0.000167 | `Ripple Effect (Closeness):` 0.250427
  * `Imports (Out-Degree: 18):` __future__, collections, collections.abc, datetime, io, numpy, os, pandas...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pandas/core/indexes/multi.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.949)
- **Top Global Matches:** file_cluster_4: 7.949, file_cluster_5: 10.947, file_cluster_12: 11.007
- **Magnitude:** 3113.4 | **LOC:** 4847 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 23.1%
- **Blast Radius:** changing it is visible to **265** in-repo importer(s); it depends on **35**; blast radius 6.252; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.9%)
- **Documentation Coverage:** 45.8128% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_loc_level` **(Many-Argument Workhorses)** (Impact: 97.4)
    * *Intent:* """ get_loc_level but with `level` known to be positional, not name-based. """
  * `_get_level_indexer` **(Many-Argument Workhorses)** (Impact: 74.9)
  * `_reorder_indexer` **(Many-Argument Workhorses)** (Impact: 60.4)
    * *Intent:* # --------------------------------------------------------------------
  * `get_locs` **(Many-Argument Workhorses)** (Impact: 57.1)
    * *Intent:* """ Get location for a sequence of labels. This method returns the integer positions in the index th...
  * `_verify_integrity` **(Many-Argument Workhorses)** (Impact: 53.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 442 instances
* *State Mutation (weighted view):* 1416
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 552`, `structural_boundaries: 445`, `args: 118`, `func_start: 118`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 532`, `dead_code: 2`, `planned_debt: 6`, `fragile_debt: 4`
* *Architecture:* `api: 85`, `import: 38`
* *Defense:* `safety: 103`, `doc: 86`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.252
  * `Choke Point (Betweenness):` 0.004528 | `Ripple Effect (Closeness):` 0.267069
  * `Imports (Out-Degree: 33):` __future__, collections.abc, copy, functools, itertools, numpy, pandas, pandas._config...
  * `Imported By (In-Degree: 265):` (Excluded from Brief to save tokens)

### `pandas/tests/extension/test_arrow.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.652)
- **Top Global Matches:** file_cluster_15: 7.652, file_cluster_11: 8.753, file_cluster_12: 9.056
- **Magnitude:** 3109.48 | **LOC:** 3952 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 18.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (64.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.0%), Complexity Load (formerly Cognitive Load) (44.1%), Connectivity (formerly Api Exposure) (12.8%)
- **Documentation Coverage:** 97.7186% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_cast_pointwise_result` **(Many-Argument Workhorses)** (Impact: 90.3)
    * *Intent:* # TODO: use EA._cast_pointwise_result, same with other test files that # override this # BaseOpsUtil...
  * `test_quantile` **(Many-Argument Workhorses)** (Impact: 57.2)
  * `_get_expected_reduction_dtype` **(Many-Argument Workhorses)** (Impact: 46.6)
  * `_supports_reduction` **(Stateful Encapsulated Methods)** (Impact: 40.1)
  * `_get_arith_xfail_marker` **(Many-Argument Workhorses)** (Impact: 36.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 311 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1530
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 399`, `structural_boundaries: 556`, `args: 255`, `func_start: 251`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 3`, `state_mutation: 908`, `planned_debt: 12`, `fragile_debt: 1`, `unreferenced_by_name: 238`
* *Architecture:* `io: 1`, `api: 244`, `import: 24`
* *Defense:* `safety: 118`, `doc: 8`, `test: 417`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` __future__, datetime, decimal, io, numpy, operator, pandas, pandas._libs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/tests/io/test_sql.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.675)
- **Top Global Matches:** file_cluster_15: 6.675, file_cluster_12: 7.943, file_cluster_11: 8.374
- **Magnitude:** 2919.0 | **LOC:** 4399 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (56.4%), Complexity Load (formerly Cognitive Load) (28.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.8%), Connectivity (formerly Api Exposure) (12.8%)
- **Documentation Coverage:** 99.0868% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `func` **(Many-Argument Workhorses)** (Impact: 19.9)
  * `test_api_timedelta` **(Compute Cores)** (Impact: 17.8)
    * *Intent:* # see #6921 conn_name = conn conn = request.getfixturevalue(conn) if sql.has_table("test_timedelta",...
  * `get_all_views` **(Defensive Guards)** (Impact: 16.7)
  * `get_all_tables` **(Defensive Guards)** (Impact: 16.7)
  * `test_read_sql_dtype_backend_table` **(Many-Argument Workhorses)** (Impact: 16.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 347 instances
* *Api Near Db Sink:* 12 instances
* *State Mutation (weighted view):* 1494
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 1015`, `args: 220`, `func_start: 215`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 800`, `planned_debt: 7`, `fragile_debt: 2`, `unreferenced_by_name: 145`
* *Architecture:* `io: 102`, `api: 217`, `import: 82`
* *Defense:* `safety: 306`, `doc: 21`, `test: 485`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` __future__, adbc_driver_manager, adbc_driver_postgresql, adbc_driver_sqlite, contextlib, csv, datetime, decimal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/_libs/lib.pyx` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.946)
- **Top Global Matches:** file_cluster_4: 6.946, file_cluster_12: 9.432, file_cluster_15: 9.506
- **Magnitude:** 2622.88 | **LOC:** 3326 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (77.5%), Guard Balance (formerly Safety Score) (73.9%)
- **Documentation Coverage:** 59.1463% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `maybe_convert_objects` **(Many-Argument Workhorses)** (Impact: 401.0)
  * `maybe_convert_numeric` **(Many-Argument Workhorses)** (Impact: 218.4)
  * `infer_dtype` **(Many-Argument Workhorses)** (Impact: 117.4)
    * *Intent:* """ Return a string label of the type of the elements in a list-like input. This method inspects the...
  * `generate_bins_dt64` **(Many-Argument Workhorses)** (Impact: 43.2)
    * *Intent:* # ------------------------------------------------------------------------------ # Groupby-related f...
  * `array_equivalent_object` **(Many-Argument Workhorses)** (Impact: 37.8)
    * *Intent:* """ Perform an element by element comparison on N-d object arrays taking into account nan positions....
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 342 instances
* *State Mutation (weighted view):* 1069
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 581`, `structural_boundaries: 427`, `args: 112`, `func_start: 112`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 385`, `planned_debt: 8`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 47`, `import: 27`
* *Defense:* `safety: 53`, `doc: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` collections, decimal, enum, numpy, pandas, pandas._config, pandas._libs.interval, pandas._libs.missing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/tests/frame/test_constructors.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.663)
- **Top Global Matches:** file_cluster_15: 7.663, file_cluster_12: 7.808, file_cluster_16: 9.489
- **Magnitude:** 2614.84 | **LOC:** 3382 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (62.5%), Complexity Load (formerly Cognitive Load) (42.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.3%), Connectivity (formerly Api Exposure) (13.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_dict_nocopy` **(Defensive Guards)** (Impact: 46.6)
  * `test_constructor_data_aware_dtype_naive` **(Compute Cores)** (Impact: 19.6)
    * *Intent:* # GH#25843, GH#41555, GH#33401 tz = tz_aware_fixture ts = Timestamp("2019", tz=tz) if pydt: ts = ts....
  * `test_constructor_error_msgs` **(Compute Cores)** (Impact: 18.5)
  * `test_constructor_mixed_dtypes` **(Defensive Guards)** (Impact: 17.1)
  * `constructor` **(Callbacks & Closures)** (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 267 instances
* *State Mutation (weighted view):* 1417
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 630`, `args: 252`, `func_start: 232`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 883`, `planned_debt: 8`, `fragile_debt: 4`, `unreferenced_by_name: 222`
* *Architecture:* `api: 238`, `import: 22`
* *Defense:* `safety: 234`, `test: 348`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` array, collections, collections.abc, dataclasses, datetime, functools, numpy, numpy.dtypes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/_libs/groupby.pyx` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.009)
- **Top Global Matches:** file_cluster_8: 6.009, file_cluster_6: 16.437, file_cluster_3: 20.594
- **Magnitude:** 2499.5 | **LOC:** 2347 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.6%), Complexity Load (formerly Cognitive Load) (63.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `group_sum` **(Many-Argument Workhorses)** (Impact: 129.1)
  * `group_quantile` **(Many-Argument Workhorses)** (Impact: 103.9)
  * `group_var` **(Many-Argument Workhorses)** (Impact: 98.6)
  * `group_mean` **(Many-Argument Workhorses)** (Impact: 95.6)
  * `group_cummin_max` **(Many-Argument Workhorses)** (Impact: 81.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 345 instances
* *State Mutation (weighted view):* 1052
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 400`, `structural_boundaries: 112`, `args: 31`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 362`
* *Architecture:* `api: 22`, `import: 2`
* *Defense:* `safety: 11`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` numpy, pandas._libs.algos
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/core/series.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 9.372)
- **Top Global Matches:** file_cluster_0: 9.372, file_cluster_12: 9.563, file_cluster_5: 9.855
- **Magnitude:** 2452.5 | **LOC:** 9949 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 25.6%
- **Blast Radius:** changing it is visible to **186** in-repo importer(s); it depends on **55**; blast radius 7.672; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.6%), Connectivity (formerly Api Exposure) (71.5%)
- **Documentation Coverage:** 59.587% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 155.7)
    * *Intent:* # ---------------------------------------------------------------------- # Constructors
  * `reset_index` **(Many-Argument Workhorses)** (Impact: 44.5)
  * `sort_values` **(Many-Argument Workhorses)** (Impact: 42.6)
  * `_flex_method` **(Many-Argument Workhorses)** (Impact: 36.3)
  * `case_when` **(Many-Argument Workhorses)** (Impact: 33.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 232 instances
* *State Mutation (weighted view):* 776
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 288`, `structural_boundaries: 533`, `args: 180`, `func_start: 179`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 312`, `planned_debt: 6`
* *Architecture:* `io: 3`, `api: 158`, `import: 59`
* *Defense:* `safety: 78`, `doc: 127`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.672
  * `Choke Point (Betweenness):` 0.007506 | `Ripple Effect (Closeness):` 0.295047
  * `Imports (Out-Degree: 53):` __future__, collections.abc, functools, numpy, operator, pandas._libs, pandas._libs.internals, pandas._libs.lib...
  * `Imported By (In-Degree: 186):` (Excluded from Brief to save tokens)

### `pandas/tests/indexing/test_loc.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.545)
- **Top Global Matches:** file_cluster_15: 6.545, file_cluster_10: 8.431, file_cluster_11: 8.499
- **Magnitude:** 2438.22 | **LOC:** 3601 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (66.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (45.8%), Complexity Load (formerly Cognitive Load) (41.2%), Connectivity (formerly Api Exposure) (13.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_loc_iloc_getitem_leading_ellipses` **(Compute Cores)** (Impact: 25.1)
  * `test_loc_getitem_listlike_of_datetimelike_keys` **(Compute Cores)** (Impact: 19.3)
    * *Intent:* # GH#11497 idx = date_range("2011-01-01", "2011-01-02", freq="D", name="idx") if to_period: idx = id...
  * `test_loc_setitem_with_expansion_nonunique_index` **(Many-Argument Workhorses)** (Impact: 18.5)
    * *Intent:* # GH#40096 if not len(index): pytest.skip("Not relevant for empty Index") index = index.repeat(2) # ...
  * `test_loc_iloc_getitem_ellipses_only_one_ellipsis` **(Compute Cores)** (Impact: 16.9)
    * *Intent:* # GH37750 key = 0 if (indexer is tm.iloc or len(obj) == 0) else obj.index[0] with pytest.raises(Inde...
  * `test_loc_setitem_str_to_small_float_conversion_type` **(Type Conversions)** (Impact: 15.0)
    * *Intent:* # GH#20388 col_data = [str(np.random.default_rng(2).random() * 1e-12) for _ in range(5)] result = Da...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 202 instances
* *State Mutation (weighted view):* 1409
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 427`, `args: 261`, `func_start: 220`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1005`, `dead_code: 2`, `planned_debt: 5`, `fragile_debt: 1`, `unreferenced_by_name: 215`
* *Architecture:* `api: 232`, `import: 17`
* *Defense:* `safety: 72`, `doc: 2`, `test: 361`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` collections, contextlib, datetime, dateutil.tz, numpy, pandas, pandas._libs, pandas._testing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/core/reshape/merge.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.156)
- **Top Global Matches:** file_cluster_6: 7.156, file_cluster_4: 12.83, file_cluster_8: 13.961
- **Magnitude:** 2435.58 | **LOC:** 3139 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **34**; blast radius 1.21; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.7%), Complexity Load (formerly Cognitive Load) (65.4%)
- **Documentation Coverage:** 87.8788% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_maybe_coerce_merge_keys` **(Many-Argument Workhorses)** (Impact: 118.5)
    * *Intent:* # we have valid merges but we may have to further # coerce these if they are originally incompatible...
  * `_maybe_add_join_keys` **(Many-Argument Workhorses)** (Impact: 108.7)
  * `_factorize_keys` **(Many-Argument Workhorses)** (Impact: 95.3)
  * `_validate_left_right_on` **(Many-Argument Workhorses)** (Impact: 86.0)
  * `_validate_left_right_on` **(Many-Argument Workhorses)** (Impact: 76.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 369 instances
* *State Mutation (weighted view):* 1163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 527`, `structural_boundaries: 250`, `args: 59`, `func_start: 54`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 425`, `planned_debt: 12`, `fragile_debt: 1`
* *Architecture:* `api: 11`, `import: 37`
* *Defense:* `safety: 79`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.21
  * `Choke Point (Betweenness):` 0.000213 | `Ripple Effect (Closeness):` 0.257596
  * `Imports (Out-Degree: 33):` __future__, collections.abc, datetime, functools, numpy, pandas, pandas._libs, pandas._libs.lib...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `pandas/core/groupby/groupby.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.297)
- **Top Global Matches:** file_cluster_4: 7.297, file_cluster_12: 8.978, file_cluster_16: 10.053
- **Magnitude:** 2432.76 | **LOC:** 6037 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 23.5%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **44**; blast radius 0.624; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (54.1%)
- **Documentation Coverage:** 68.984% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `quantile` **(Many-Argument Workhorses)** (Impact: 91.4)
  * `_value_counts` **(Many-Argument Workhorses)** (Impact: 67.0)
  * `shift` **(Many-Argument Workhorses)** (Impact: 51.2)
  * `apply` **(Many-Argument Workhorses)** (Impact: 45.0)
    * *Intent:* # ----------------------------------------------------------------- # apply/agg/transform """ Apply ...
  * `_concat_objects` **(Many-Argument Workhorses)** (Impact: 38.9)
    * *Intent:* # ----------------------------------------------------------------- # Dispatch/Wrapping
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 320 instances
* *State Mutation (weighted view):* 1040
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 328`, `structural_boundaries: 402`, `args: 116`, `func_start: 102`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 400`, `dead_code: 3`, `planned_debt: 10`
* *Architecture:* `io: 1`, `api: 76`, `import: 56`
* *Defense:* `safety: 65`, `doc: 65`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.624
  * `Choke Point (Betweenness):` 0.000931 | `Ripple Effect (Closeness):` 0.202981
  * `Imports (Out-Degree: 48):` __future__, collections.abc, datetime, functools, numpy, pandas._libs, pandas._libs.algos, pandas._libs.groupby...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `pandas/plotting/_matplotlib/core.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.598)
- **Top Global Matches:** file_cluster_4: 7.598, file_cluster_12: 11.092, file_cluster_5: 11.137
- **Magnitude:** 2427.52 | **LOC:** 2222 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **33**; blast radius 0.188; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.2%), Complexity Load (formerly Cognitive Load) (73.5%)
- **Documentation Coverage:** 85.3846% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 160.0)
  * `_validate_color_args` **(Stateful Encapsulated Methods)** (Impact: 50.0)
  * `_parse_errorbars` **(Many-Argument Workhorses)** (Impact: 49.4)
    * *Intent:* # TODO: tighter typing for first return?
  * `_make_plot` **(Many-Argument Workhorses)** (Impact: 40.2)
  * `_adorn_subplots` **(Many-Argument Workhorses)** (Impact: 37.9)
    * *Intent:* """Common post process unrelated to data"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 345 instances
* *State Mutation (weighted view):* 1103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 449`, `structural_boundaries: 320`, `args: 106`, `func_start: 106`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 413`, `planned_debt: 26`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 27`, `import: 34`
* *Defense:* `safety: 57`, `doc: 19`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.188
  * `Choke Point (Betweenness):` 0.000678 | `Ripple Effect (Closeness):` 0.139757
  * `Imports (Out-Degree: 25):` __future__, abc, collections.abc, matplotlib, matplotlib.artist, matplotlib.axes, matplotlib.axis, matplotlib.figure...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pandas/_libs/window/aggregations.pyx` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.022)
- **Top Global Matches:** file_cluster_6: 6.022, file_cluster_8: 12.099, file_cluster_4: 12.916
- **Magnitude:** 2415.06 | **LOC:** 2119 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (61.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `roll_rank` **(Many-Argument Workhorses)** (Impact: 98.7)
  * `ewmcov` **(Many-Argument Workhorses)** (Impact: 97.7)
  * `roll_quantile` **(Many-Argument Workhorses)** (Impact: 93.2)
  * `ewm` **(Many-Argument Workhorses)** (Impact: 90.2)
    * *Intent:* # ---------------------------------------------------------------------- # Exponentially weighted mo...
  * `_roll_min_max` **(Many-Argument Workhorses)** (Impact: 81.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 414 instances
* *State Mutation (weighted view):* 1271
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 365`, `structural_boundaries: 95`, `args: 41`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 443`, `fragile_debt: 1`
* *Architecture:* `api: 19`, `import: 3`
* *Defense:* `safety: 4`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cython, numpy, pandas._libs.algos
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/tests/groupby/test_groupby.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.492)
- **Top Global Matches:** file_cluster_15: 8.492, file_cluster_12: 8.844, file_cluster_11: 9.433
- **Magnitude:** 2329.54 | **LOC:** 3020 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 28.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (70.2%), Complexity Load (formerly Cognitive Load) (43.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.4%), Connectivity (formerly Api Exposure) (12.5%)
- **Documentation Coverage:** 99.4382% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_empty_groupby` **(Many-Argument Workhorses)** (Impact: 116.4)
    * *Intent:* # GH8093 & GH26411 override_dtype = None if isinstance(values, BooleanArray) and op in ["sum", "prod...
  * `test_omit_nuisance_agg` **(Many-Argument Workhorses)** (Impact: 26.1)
    * *Intent:* # GH 38774, GH 38815 grouped = df.groupby("A") no_drop_nuisance = ("var", "std", "sem", "mean", "pro...
  * `test_len_categorical` **(Compute Cores)** (Impact: 23.0)
    * *Intent:* # GH#57595 df = DataFrame( { "a": Categorical([1, 1, 2, np.nan], categories=[1, 2, 3]), "b": Categor...
  * `test_groups_sort_dropna` **(Compute Cores)** (Impact: 18.7)
    * *Intent:* # GH#56966, GH#56851 df = DataFrame([[2.0, 1.0], [np.nan, 4.0], [0.0, 3.0]]) keys = [(2.0, 1.0), (np...
  * `test_indices_concatenation_order` **(I/O & Config Routines)** (Impact: 13.7)
    * *Intent:* # GH 2808 def f1(x): y = x[(x.b % 2) == 1] ** 2 if y.empty: multiindex = MultiIndex(levels=[[]] * 2,...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 283 instances
* *State Mutation (weighted view):* 1400
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 367`, `args: 214`, `func_start: 169`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 834`, `planned_debt: 3`, `duplicate_logic: 2`, `unreferenced_by_name: 146`
* *Architecture:* `io: 1`, `api: 161`, `import: 13`
* *Defense:* `safety: 106`, `doc: 1`, `test: 233`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` datetime, decimal, numpy, pandas, pandas._testing, pandas.core.arrays, pandas.core.common, pandas.errors...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/core/internals/managers.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.853)
- **Top Global Matches:** file_cluster_5: 7.853, file_cluster_12: 8.94, file_cluster_0: 9.545
- **Magnitude:** 2265.6 | **LOC:** 2557 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **30**; blast radius 1.508; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (55.9%)
- **Documentation Coverage:** 61.5721% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_slice_take_blocks_ax0` **(Many-Argument Workhorses)** (Impact: 86.3)
  * `iset` **(Many-Argument Workhorses)** (Impact: 71.1)
  * `reindex_indexer` **(Many-Argument Workhorses)** (Impact: 46.3)
  * `as_array` **(Many-Argument Workhorses)** (Impact: 46.2)
  * `setitem` **(Many-Argument Workhorses)** (Impact: 38.8)
    * *Intent:* """ Set values with indexer. For SingleBlockManager, this backs s[indexer] = value """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 348 instances
* *State Mutation (weighted view):* 1117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 326`, `structural_boundaries: 382`, `args: 132`, `func_start: 130`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 421`, `dead_code: 1`, `planned_debt: 25`, `fragile_debt: 2`
* *Architecture:* `api: 100`, `import: 30`
* *Defense:* `safety: 44`, `doc: 70`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.508
  * `Choke Point (Betweenness):` 0.000948 | `Ripple Effect (Closeness):` 0.230708
  * `Imports (Out-Degree: 34):` __future__, collections.abc, itertools, numpy, pandas._config.config, pandas._libs, pandas._libs.internals, pandas._libs.tslibs...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `pandas/_libs/parsers.pyx` (PYTHON | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.908)
- **Top Global Matches:** file_cluster_6: 5.908, file_cluster_4: 7.801, file_cluster_12: 15.945
- **Magnitude:** 2103.22 | **LOC:** 2183 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.5%), Complexity Load (formerly Cognitive Load) (69.6%)
- **Documentation Coverage:** 89.8305% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__cinit__` **(Many-Argument Workhorses)** (Impact: 217.7)
  * `_try_double_nogil` **(Many-Argument Workhorses)** (Impact: 108.2)
  * `_convert_with_dtype` **(Many-Argument Workhorses)** (Impact: 108.0)
  * `_get_header` **(Many-Argument Workhorses)** (Impact: 107.5)
    * *Intent:* # header is now a list of lists, so field_count should use header[0] # # modifies: # self.parser att...
  * `_convert_tokens` **(Many-Argument Workhorses)** (Impact: 70.8)
    * *Intent:* # -> tuple["ArrayLike", int]:
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 273 instances
* *State Mutation (weighted view):* 876
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 372`, `structural_boundaries: 177`, `args: 51`, `func_start: 50`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 330`, `planned_debt: 5`
* *Architecture:* `api: 9`, `import: 15`
* *Defense:* `safety: 46`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` collections, csv, numpy, pandas, pandas._config, pandas._libs, pandas.core.arrays, pandas.core.arrays.boolean...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/core/indexing.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.205)
- **Top Global Matches:** file_cluster_4: 7.205, file_cluster_6: 11.469, file_cluster_12: 11.628
- **Magnitude:** 2059.0 | **LOC:** 3434 | **CtrlFlow:** 38.4% | **Authorship Centralization:** 16.7%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **27**; blast radius 0.827; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.3%)
- **Documentation Coverage:** 44.3396% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_align_series` **(Many-Argument Workhorses)** (Impact: 96.5)
  * `_setitem_with_indexer_split_path` **(Many-Argument Workhorses)** (Impact: 80.4)
    * *Intent:* """ Setitem column-wise. """
  * `_convert_to_indexer` **(Defensive Guards)** (Impact: 58.0)
    * *Intent:* """ Convert indexing key into something we can use to do actual fancy indexing on an ndarray. Exampl...
  * `_align_frame` **(Defensive Guards)** (Impact: 48.4)
  * `_setitem_with_indexer_missing` **(Many-Argument Workhorses)** (Impact: 44.4)
    * *Intent:* """ Insert new row(s) or column(s) into the Series or DataFrame. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 257 instances
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 480`, `structural_boundaries: 340`, `args: 85`, `func_start: 85`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 289`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 4`
* *Architecture:* `io: 3`, `api: 17`, `import: 30`
* *Defense:* `safety: 129`, `doc: 53`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.827
  * `Choke Point (Betweenness):` 0.00058 | `Ripple Effect (Closeness):` 0.25825
  * `Imports (Out-Degree: 28):` __future__, collections.abc, contextlib, numpy, pandas, pandas._libs.indexing, pandas._libs.lib, pandas._typing...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `pandas/tests/arithmetic/test_timedelta64.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.856)
- **Top Global Matches:** file_cluster_15: 5.856, file_cluster_16: 7.98, file_cluster_13: 8.572
- **Magnitude:** 2009.56 | **LOC:** 2332 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 87.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (75.3%), Complexity Load (formerly Cognitive Load) (30.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.9%), Connectivity (formerly Api Exposure) (11.6%)
- **Documentation Coverage:** 98.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_td64arr_div_numeric_array` **(Many-Argument Workhorses)** (Impact: 29.4)
  * `test_subtraction_ops_with_tz` **(Many-Argument Workhorses)** (Impact: 28.4)
    * *Intent:* # check that dt/dti subtraction ops with tz are validated dti = pd.date_range("20130101", periods=3)...
  * `test_td64arr_add_sub_datetimelike_scalar` **(Many-Argument Workhorses)** (Impact: 24.5)
    * *Intent:* # ------------------------------------------------------------- # Binary operations td64 arraylike a...
  * `test_td64arr_mod_tdscalar` **(Many-Argument Workhorses)** (Impact: 19.6)
    * *Intent:* # ------------------------------------------------------------------ # mod, divmod # TODO: operation...
  * `test_timedelta_ops_with_missing_values` **(Compute Cores)** (Impact: 14.5)
    * *Intent:* # TODO: moved from tests.indexes.timedeltas.test_arithmetic; needs # parametrization+de-duplication ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 259 instances
* *State Mutation (weighted view):* 1263
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 287`, `args: 92`, `func_start: 88`, `class_start: 7`
* *Risk/State:* `state_mutation: 745`, `planned_debt: 13`, `fragile_debt: 1`, `unreferenced_by_name: 85`
* *Architecture:* `api: 94`, `import: 12`
* *Defense:* `safety: 62`, `doc: 1`, `test: 188`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` datetime, numpy, pandas, pandas._libs.tslibs, pandas._testing, pandas.compat, pandas.core.arrays, pandas.errors...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pandas/tests/io/test_stata.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.608)
- **Top Global Matches:** file_cluster_15: 6.608, file_cluster_12: 7.702, file_cluster_16: 8.726
- **Magnitude:** 2006.78 | **LOC:** 2629 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (70.5%), Complexity Load (formerly Cognitive Load) (27.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (23.7%), Connectivity (formerly Api Exposure) (12.0%)
- **Documentation Coverage:** 99.5671% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_compression` **(Many-Argument Workhorses)** (Impact: 36.8)
  * `test_big_dates` **(Many-Argument Workhorses)** (Impact: 19.6)
  * `test_categorical_order` **(Many-Argument Workhorses)** (Impact: 13.7)
    * *Intent:* # Directly construct using expected codes # Format is is_cat, col_name, labels (in order), underlyin...
  * `test_stata_compression` **(Many-Argument Workhorses)** (Impact: 13.4)
  * `test_write_variable_label_errors` **(Many-Argument Workhorses)** (Impact: 11.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 257 instances
* *State Mutation (weighted view):* 1254
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 350`, `args: 118`, `func_start: 116`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 740`, `planned_debt: 2`, `fragile_debt: 3`, `unreferenced_by_name: 111`
* *Architecture:* `io: 15`, `api: 116`, `import: 21`
* *Defense:* `safety: 60`, `doc: 4`, `test: 219`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` bz2, datetime, gzip, io, itertools, numpy, os, pandas...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `scripts/validate_rst_title_capitalization.py` (PYTHON) | Magnitude: 70.38 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 179, structural_boundaries: 17, core_var_decl: 17, design_snake_case: 15
- `pandas/core/arrays/masked.py` (PYTHON) | Magnitude: 1639.86 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1141, core_var_decl: 381, design_snake_case: 364, structural_boundaries: 348
- `generate_version.py` (PYTHON) | Magnitude: 36.56 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 44, core_var_decl: 19, design_snake_case: 19, structural_boundaries: 12
- `pandas/_libs/hashtable.pyx` (PYTHON) | Magnitude: 63.66 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 27, core_var_decl: 14, state_mutation: 13
- `pandas/io/excel/_pyxlsb.py` (PYTHON) | Magnitude: 89.9 | Delta: **0.154** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 37, branch: 17, core_var_decl: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `pandas/tests/arithmetic/conftest.py` (PYTHON) | Magnitude: 34.9 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 22, test: 13, core_var_decl: 13
- `web/pandas/_templates/layout.html` (HTML) | Magnitude: 15.38 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 106, core_var_decl: 53, design_snake_case: 51, ssr_boundaries: 35
- `pandas/tests/series/methods/test_sort_index.py` (PYTHON) | Magnitude: 231.48 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 235, state_mutation: 108, core_var_decl: 108, design_snake_case: 108
- `pandas/tests/series/methods/test_case_when.py` (PYTHON) | Magnitude: 74.6 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 67, core_var_decl: 29, design_snake_case: 29, structural_boundaries: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `pandas/tests/series/methods/test_dtypes.py` (PYTHON) | Magnitude: 4.0 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 3, safety: 2, api: 2
- `pandas/tests/arrays/boolean/test_reduction.py` (PYTHON) | Magnitude: 78.58 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 15, branch: 13, core_var_decl: 12
- `pandas/tests/series/methods/test_reindex.py` (PYTHON) | Magnitude: 294.06 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 282, core_var_decl: 161, design_snake_case: 154, state_mutation: 141
- `pandas/tests/indexes/categorical/test_map.py` (PYTHON) | Magnitude: 53.7 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 97, core_var_decl: 36, design_snake_case: 36, state_mutation: 31
- `pandas/tests/extension/test_categorical.py` (PYTHON) | Magnitude: 124.04 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 88, structural_boundaries: 57, test: 32, core_var_decl: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `pandas/core/interchange/column.py` (PYTHON) | Magnitude: 290.64 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 274, structural_boundaries: 84, state_mutation: 61, core_var_decl: 61
- `scripts/tests/test_validate_docstrings.py` (PYTHON) | Magnitude: 115.38 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 321, core_var_decl: 62, design_snake_case: 62, structural_boundaries: 52
- `pandas/tests/test_errors.py` (PYTHON) | Magnitude: 64.06 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 93, structural_boundaries: 34, core_var_decl: 19, design_snake_case: 19
- `pandas/tests/groupby/methods/test_describe.py` (PYTHON) | Magnitude: 152.82 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 207, core_var_decl: 83, design_snake_case: 83, state_mutation: 66
- `pandas/tests/indexes/datetimes/test_formats.py` (PYTHON) | Magnitude: 128.08 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 218, core_var_decl: 84, design_snake_case: 84, state_mutation: 75

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `pandas/tests/io/parser/common/test_decimal.py` (PYTHON) | Magnitude: 29.78 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 37, core_var_decl: 13, design_snake_case: 13, structural_boundaries: 12
- `pandas/tests/interchange/test_utils.py` (PYTHON) | Magnitude: 29.02 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 11, test: 6, state_mutation: 5
- `pandas/tests/groupby/test_index_as_string.py` (PYTHON) | Magnitude: 50.76 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 52, state_mutation: 12, core_var_decl: 12, design_snake_case: 12
- `pandas/tests/indexes/datetimes/test_freq_attr.py` (PYTHON) | Magnitude: 28.68 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 18, state_mutation: 10, test: 9
- `pandas/tests/indexes/period/test_scalar_compat.py` (PYTHON) | Magnitude: 17.74 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 10, state_mutation: 8, core_var_decl: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `pandas/tests/frame/methods/test_swaplevel.py` (PYTHON) | Magnitude: 22.48 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 25, core_var_decl: 14, design_snake_case: 14, state_mutation: 13
- `pandas/tests/copy_view/test_methods.py` (PYTHON) | Magnitude: 858.06 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 996, state_mutation: 417, core_var_decl: 369, design_snake_case: 368
- `pandas/tests/series/methods/test_rename_axis.py` (PYTHON) | Magnitude: 38.96 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 14, core_var_decl: 14, design_snake_case: 14
- `pandas/core/_numba/extensions.py` (PYTHON) | Magnitude: 344.02 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 283, structural_boundaries: 158, state_mutation: 83, core_var_decl: 61
- `pandas/tests/indexes/timedeltas/methods/test_repeat.py` (PYTHON) | Magnitude: 18.0 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 10, state_mutation: 4, core_var_decl: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `pandas/util/_doctools.py` (PYTHON) | Magnitude: 234.88 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 131, core_var_decl: 61, design_snake_case: 60, state_mutation: 53
- `pandas/io/excel/_xlrd.py` (PYTHON) | Magnitude: 117.52 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 42, core_var_decl: 19, branch: 17
- `pandas/core/indexes/interval.py` (PYTHON) | Magnitude: 740.24 | Delta: **0.13** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 525, structural_boundaries: 175, core_var_decl: 160, branch: 142
- `pandas/tests/test_expressions.py` (PYTHON) | Magnitude: 311.8 | Delta: **0.13** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 336, core_var_decl: 105, design_snake_case: 105, structural_boundaries: 99

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `pandas/api/typing/__init__.py` (PYTHON) | Magnitude: 18.04 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 22, scientific: 11, import: 11
- `pandas/io/api.py` (PYTHON) | Magnitude: 18.2 | Delta: **0.186** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 32, scientific: 16, import: 16
- `pandas/core/arrays/__init__.py` (PYTHON) | Magnitude: 17.84 | Delta: **0.211** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 30, indent_spaces: 23, scientific: 15, import: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `pandas/tests/arrays/categorical/test_warnings.py` (PYTHON) | Magnitude: 6.62 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 8, test: 3, import: 3
- `pandas/core/api.py` (PYTHON) | Magnitude: 19.64 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 94, structural_boundaries: 52, scientific: 26, import: 26
- `pandas/tests/arrays/boolean/test_repr.py` (PYTHON) | Magnitude: 6.68 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 6, state_mutation: 4, core_var_decl: 4
- `pandas/tests/indexes/timedeltas/methods/test_factorize.py` (PYTHON) | Magnitude: 12.92 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 13, core_var_decl: 9, design_snake_case: 9
- `pandas/tests/frame/methods/test_iterrows.py` (PYTHON) | Magnitude: 6.76 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, branch: 1, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `pandas/io/stata.py` (PYTHON) | Magnitude: 3119.36 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 2166, state_mutation: 648, core_var_decl: 559, branch: 526
- `pandas/core/computation/align.py` (PYTHON) | Magnitude: 211.24 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 112, structural_boundaries: 68, branch: 48, core_var_decl: 40
- `pandas/core/groupby/generic.py` (PYTHON) | Magnitude: 1420.0 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 998, core_var_decl: 418, design_snake_case: 393, structural_boundaries: 259
- `pandas/core/arrays/arrow/array.py` (PYTHON) | Magnitude: 3201.04 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 2151, core_var_decl: 726, structural_boundaries: 693, design_snake_case: 689
- `pandas/core/arrays/string_arrow.py` (PYTHON) | Magnitude: 633.38 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 399, structural_boundaries: 156, branch: 148, core_var_decl: 130

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `scripts/validate_exception_location.py` (PYTHON) | Magnitude: 73.86 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 24, state_mutation: 17, core_var_decl: 17
- `pandas/io/formats/string.py` (PYTHON) | Magnitude: 290.88 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 146, state_mutation: 70, core_var_decl: 58, design_snake_case: 56
- `pandas/tests/indexing/common.py` (PYTHON) | Magnitude: 39.72 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 10, branch: 7, core_var_decl: 6
- `pandas/core/base.py` (PYTHON) | Magnitude: 479.44 | Delta: **0.133** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 380, structural_boundaries: 158, core_var_decl: 94, design_snake_case: 83
- `pandas/core/internals/ops.py` (PYTHON) | Magnitude: 108.78 | Delta: **0.155** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 32, state_mutation: 20, core_var_decl: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `pandas/_config/display.py` (PYTHON) | Magnitude: 31.24 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 13, core_var_decl: 8, state_mutation: 7
- `pandas/tests/arrays/categorical/test_subclass.py` (PYTHON) | Magnitude: 16.4 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 13, safety: 6, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `pandas/core/window/online.py` (PYTHON) | Magnitude: 140.34 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 70, state_mutation: 23, structural_boundaries: 18, branch: 14

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `pandas/_libs/tslibs/offsets.pyx` -> Churn: **93.14%** | Cog Load: 47.5726% | Debt: 78.8108%
- `pandas/core/frame.py` -> Churn: **79.67%** | Cog Load: 61.832% | Debt: 8.4633%
- `pandas/core/generic.py` -> Churn: **76.97%** | Cog Load: 66.3773% | Debt: 8.5275%
- `pandas/_libs/tslibs/period.pyx` -> Churn: **61.61%** | Cog Load: 66.1363% | Debt: 8.3409%
- `pandas/_libs/tslibs/timedeltas.pyx` -> Churn: **60.39%** | Cog Load: 68.9339% | Debt: 12.6818%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `pandas/_libs/tslibs/offsets.pyx` -> **Tuhin Sharma** (85.9% isolated ownership) | Magnitude: 3492.2
- `pandas/_libs/window/aggregations.pyx` -> **Álvaro Kothe** (100.0% isolated ownership) | Magnitude: 2415.06
- `pandas/tests/arithmetic/test_timedelta64.py` -> **jbrockmendel** (87.5% isolated ownership) | Magnitude: 2009.56
- `pandas/tests/arithmetic/test_datetime64.py` -> **jbrockmendel** (100.0% isolated ownership) | Magnitude: 1782.62
- `pandas/tests/frame/test_stack_unstack.py` -> **Álvaro Kothe** (100.0% isolated ownership) | Magnitude: 1726.86

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pandas/core/frame.py` -> **Severity: 1.913** (Bridge: 0.0191 * Flux: 100.0%)
- `pandas/_testing/__init__.py` -> **Severity: 1.235** (Bridge: 0.0123 * Flux: 99.999%)
- `pandas/__init__.py` -> **Severity: 1.008** (Bridge: 0.0386 * Flux: 26.0859%)
- `pandas/_typing.py` -> **Severity: 0.996** (Bridge: 0.024 * Flux: 41.5116%)
- `pandas/core/dtypes/dtypes.py` -> **Severity: 0.931** (Bridge: 0.0093 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pandas/__init__.py` -> **Severity: 30.707** (Embedded: 0.58 * Error Risk: 52.944%)
- `pandas/core/col.py` -> **Severity: 27.045** (Embedded: 0.3326 * Error Risk: 81.3159%)
- `pandas/_testing/__init__.py` -> **Severity: 26.761** (Embedded: 0.4214 * Error Risk: 63.4997%)
- `pandas/core/dtypes/dtypes.py` -> **Severity: 25.018** (Embedded: 0.375 * Error Risk: 66.7083%)
- `pandas/io/json/_normalize.py` -> **Severity: 24.976** (Embedded: 0.3236 * Error Risk: 77.184%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pandas/_typing.py` -> **Severity: 6781.6** (Blast Radius: 67.816 * Doc Risk: 100.0%)
- `pandas/_config/__init__.py` -> **Severity: 1491.0** (Blast Radius: 14.91 * Doc Risk: 100.0%)
- `pandas/util/_decorators.py` -> **Severity: 1440.24** (Blast Radius: 18.003 * Doc Risk: 80.0%)
- `pandas/util/version/__init__.py` -> **Severity: 1346.1** (Blast Radius: 13.461 * Doc Risk: 100.0%)
- `pandas/_testing/__init__.py` -> **Severity: 1108.975** (Blast Radius: 21.625 * Doc Risk: 51.2821%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 61 literal sites + 1 sites through wrappers = 62
- **`memory_alloc`:** 15 literal sites + 1 sites through wrappers = 16
- **`panics_and_aborts`:** 3622 literal sites + 5 sites through wrappers = 3627

- `freq_to_dtype_code` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `pandas/_libs/tslibs/period.pyx`
- `_get_unicode_name` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `pandas/io/sql.py`
- `get_writer` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `pandas/io/excel/_util.py`
- `skiplist_destroy` (function, memory_alloc, primitive): 1 call sites in 1 files -- `pandas/_libs/include/pandas/skiplist.h`
- `write_legacy_pickles` (function, debug_prints, primitive): 1 call sites in 1 files -- `pandas/tests/io/generate_legacy_storage_files.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 133937 call pairs -- scoped 21.3%, unique 0.0%, ambiguous 37.7%, external 41.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 133902 | 21.3% | 0.0% | 37.7% | 41.0% |
| c | 24 | 66.7% | 0.0% | 0.0% | 33.3% |
| shell | 8 | 0.0% | 0.0% | 0.0% | 100.0% |
| html | 3 | 0.0% | 0.0% | 0.0% | 100.0% |

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
