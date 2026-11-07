# ARCHITECTURAL_BRIEF: python-simplebench
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/JerilynFranz/python-simplebench.git` |
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
- **Scope:** 802 analyzed artifact(s), 147128 LOC.
- **Load-bearing artifact:** `documentation/html/genindex.html` -- 274 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `tests/factories/reporter/reporter_methods.py` -- pulls in 27 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `.env` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 1704 |
| Analyzed Artifacts (Scanned) | 802 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 902 |
| Total LOC | 147128 |
| Volatility Index | 0.012 |
| % Scanned of codebase = | 47.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5628 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5124 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 10.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.7169 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 8 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 293 | 20817 | 36.5% |
| HTML | 268 | 115658 | 33.4% |
| PLAINTEXT | 200 | 1 | 24.9% |
| CSS | 17 | 8288 | 2.1% |
| JAVASCRIPT | 10 | 1177 | 1.2% |
| YAML | 4 | 72 | 0.5% |
| MARKDOWN | 2 | 0 | 0.2% |
| JSON | 2 | 1036 | 0.2% |
| XML | 2 | 0 | 0.2% |
| MAKEFILE | 1 | 21 | 0.1% |
| SHELL | 1 | 4 | 0.1% |
| BATCH | 1 | 52 | 0.1% |
| CSV | 1 | 2 | 0.1% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 801 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 67%, Declarative / Non-Code 10%, Generic / Templated Code Files 9%, Large Core Modules (2) 4%, Many-Argument Workhorses Files 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 600 | 74.8% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 201 | 25.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 902*

**Composition by Extension & Reason:**
- `.html`: 277x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Packed Payload Guard (Impossible Density: 6.53 hits/line), 1x Packed Payload Guard (Impossible Density: 4.61 hits/line)
- `.rst`: 193x Excluded (Unsupported Extension: '.rst')
- `.txt`: 193x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.doctree`: 147x Excluded (Unsupported Extension: '.doctree')
- `.js`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 2 exceeds 500 chars), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.css`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Static Asset Blob without Intent: 1266 LOC), 2x Excluded (Machine-Generated Source Code Signature: 278 LOC)
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 51001 LOC), 1x Excluded (Unsupported Extension: '.code-workspace')
- `.py`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 6x Excluded (Explicitly Denied Extension: '.png')
- `.map`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.yaml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.inv`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.inv')
- `.cfg`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 78.9 | 6.7 | 5.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 88.1 | 45.6 | 50.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.8 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 17.7 | 12.8 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 99.8 | 1.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 23.3 | 11.4 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 48.2 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.7 | 0.5 | 0.5 | 0.5 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 21.7 | 31.6 | 31.6 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 54.6 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 169 | 49 | 0 | `tests/test_stats.py` |
| cleanup | 13 | 8 | 0 | `documentation/html/source/simplebench.reporters.choices.html` |
| guards | 1056 | 186 | 3 | `tests/test_decorators.py` |
| danger | 1160 | 120 | 3 | `src/simplebench/validators/misc.py` |
| concurrency | 39 | 11 | 0 | `tests/timeout/test_timeout.py` |
| connectivity | 14217 | 512 | 46 | `documentation/_static/styles/furo.css` |
| io | 45733 | 302 | 131 | `documentation/html/genindex.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 2 | 1 | 0 | `documentation/_helpers/doctest_utils.py` |
| time | 14 | 4 | 0 | `tests/timeout/test_timeout.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 53 | 12 | 0 | `documentation/html/_static/language_data.js` |
| events | 927 | 300 | 3 | `tests/test_case.py` |
| tests | 454 | 48 | 0 | `tests/test_decorators.py` |
| docs | 6928 | 557 | 16 | `src/simplebench/reporters/reporter/exceptions/reporter.py` |
| debt | 121 | 38 | 0 | `src/simplebench/tasks.py` |
| mutation | 83579 | 536 | 268 | `documentation/html/genindex.html` |
| dead_code | 250 | 65 | 0 | `tests/test_decorators.py` |
| credential | 49 | 7 | 0 | `documentation/html/genindex.html` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 16065 | 279 | 60 | `documentation/html/reports/rich_table_report.html` |
| ui | 8282 | 300 | 22 | `documentation/html/source/simplebench.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `documentation/html/genindex.html` (Hits: 3512)
- `documentation/html/source/simplebench.html` (Hits: 2811)
- `documentation/html/source/simplebench.reporters.graph.matplotlib.html` (Hits: 947)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **genindex.html** (`documentation/html/genindex.html`) — 274 inbound connections
2. **search.html** (`documentation/html/search.html`) — 274 inbound connections
3. **__init__.py** (`src/simplebench/enums/__init__.py`) — 98 inbound connections
4. **__init__.py** (`src/simplebench/exceptions/__init__.py`) — 92 inbound connections
5. **case.py** (`src/simplebench/case.py`) — 42 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **reporter_methods.py** (`tests/factories/reporter/reporter_methods.py`) — 27 outbound dependencies
2. **reporter.py** (`src/simplebench/reporters/reporter/reporter.py`) — 24 outbound dependencies
3. **session.py** (`src/simplebench/session.py`) — 21 outbound dependencies
4. **test_reporter.py** (`tests/reporters/reporter/test_reporter.py`) — 21 outbound dependencies
5. **test_session.py** (`tests/test_session.py`) — 21 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `benchmark` **(Many-Argument Workhorses)** (@ `src/simplebench/decorators.py`) -> Impact: **159.0** | LOC: 294
- `render` **(Many-Argument Workhorses)** (@ `src/simplebench/reporters/rich_table/reporter/reporter.py`) -> Impact: **129.9** | LOC: 138
  * *Intent:* """Prints the benchmark results in a rich table format if available. It creates a :class:`~rich.table.Table` instance containing the benchmark results...
- `dispatch_to_targets` **(Many-Argument Workhorses)** (@ `src/simplebench/reporters/reporter/mixins/_orchestration.py`) -> Impact: **127.6** | LOC: 128
- `render` **(Many-Argument Workhorses)** (@ `src/simplebench/reporters/csv/reporter/reporter.py`) -> Impact: **113.2** | LOC: 117
  * *Intent:* """Renders the benchmark results as tagged CSV data and returns it as a string. :param case: The :class:`~simplebench.case.Case` instance representing...
- `media` **(I/O & Config Routines)** (@ `documentation/html/_static/pygments.css`) -> Impact: **96.7** | LOC: 174
  * *Intent:* .highlight .se { color: #79C0FF } /* Literal.String.Escape */ .highlight .sh { color: #79C0FF } /* Literal.String.Heredoc */ .highlight .si { color: #...
- `__init__` **(Many-Argument Workhorses)** (@ `src/simplebench/case.py`) -> Impact: **91.5** | LOC: 221
- `media` **(Compute Cores)** (@ `documentation/html/_static/pygments.css`) -> Impact: **91.3** | LOC: 87
  * *Intent:* body[data-theme="dark"] .highlight .se { color: #ED9D13 } /* Literal.String.Escape */ body[data-theme="dark"] .highlight .sh { color: #ED9D13 } /* Lit...
- `_validate_render_by_args` **(Many-Argument Workhorses)** (@ `src/simplebench/reporters/reporter/mixins/_orchestration.py`) -> Impact: **83.2** | LOC: 83
- `report` **(Many-Argument Workhorses)** (@ `src/simplebench/reporters/reporter/reporter.py`) -> Impact: **80.0** | LOC: 101
- `validate_sequence_of_type` **(Many-Argument Workhorses)** (@ `src/simplebench/validators/validate_sequence_of_type.py`) -> Impact: **79.8** | LOC: 125

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 5 | 5025.04 | 3.59% | 0.0% |
| `src/simplebench` | 15 | 2488.28 | 26.03% | 2.06% |
| `tests` | 13 | 1251.84 | 6.22% | 0.0% |
| `documentation/html/_static` | 16 | 1211.24 | 25.09% | 8.38% |
| `src/simplebench/validators` | 4 | 722.22 | 13.98% | 0.0% |
| `src/simplebench/reporters/reporter/mixins` | 5 | 687.4 | 24.93% | 2.36% |
| `tests/testspec` | 13 | 616.88 | 10.38% | 0.0% |
| `src/simplebench/reporters/reporter` | 6 | 591.78 | 18.81% | 8.07% |
| `src/simplebench/exceptions` | 12 | 531.92 | 2.28% | 8.33% |
| `tests/factories` | 11 | 502.2 | 3.09% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/simplebench/exceptions/__init__.py` -> **100.0%** Exposure
- `src/simplebench/stats/stats.py` -> **88.4088%** Exposure
- `documentation/html/_static/copybutton_funcs.js` -> **79.35%** Exposure
- `documentation/Makefile` -> **37.7541%** Exposure
- `documentation/html/_downloads/88e7aae14d90ceb1db4850c2e54e5bc2/minimal_parameterized_benchmark.py` -> **37.7541%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `documentation/_helpers/doctest_utils.py` -> **100.0%** Exposure
- `src/simplebench/cli.py` -> **100.0%** Exposure
- `src/simplebench/enums/decorators.py` -> **100.0%** Exposure
- `src/simplebench/exceptions/case.py` -> **100.0%** Exposure
- `src/simplebench/exceptions/decorators.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/test_decorators.py` -> **72** Orphaned Functions | **2** Duplicates
- `tests/test_case.py` -> **9** Orphaned Functions | **6** Duplicates
- `tests/reporters/reporter/test_reporter.py` -> **13** Orphaned Functions | **0** Duplicates
- `tests/test_cache_factory.py` -> **2** Orphaned Functions | **10** Duplicates
- `tests/test_stats.py` -> **11** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1208` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/validators/misc.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.283)
- **Top Global Matches:** file_cluster_5: 8.283, file_cluster_12: 10.375, file_cluster_7: 10.812
- **Magnitude:** 495.64 | **LOC:** 1100 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); it depends on **6**; blast radius 4.925; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.7%), Connectivity (formerly Api Exposure) (51.7%), Mutation Surface (formerly State Flux) (49.6%)
- **Documentation Coverage:** 78.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validate_string` **(Many-Argument Workhorses)** (Impact: 47.2)
  * `validate_dirpath` **(Many-Argument Workhorses)** (Impact: 43.7)
    * *Intent:* """Validate a directory path for use in the filesystem. It validates that: - The directory path is a...
  * `validate_sequence_of_type` **(Many-Argument Workhorses)** (Impact: 32.8)
  * `validate_frozenset_of_type` **(Many-Argument Workhorses)** (Impact: 30.5)
  * `validate_sequence_of_str` **(Many-Argument Workhorses)** (Impact: 27.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 155`, `args: 28`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 17`
* *Architecture:* `io: 1`, `api: 29`, `import: 6`
* *Defense:* `safety: 41`, `doc: 22`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.925
  * `Choke Point (Betweenness):` 0.000476 | `Ripple Effect (Closeness):` 0.087889
  * `Imports (Out-Degree: 3):` pathlib, re, simplebench.exceptions, simplebench.type_proxies.lazy_type_proxy, simplebench.validators.exceptions, typing
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `src/simplebench/case.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.084)
- **Top Global Matches:** file_cluster_5: 9.084, file_cluster_12: 11.561, file_cluster_4: 12.049
- **Magnitude:** 434.82 | **LOC:** 1016 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **42** in-repo importer(s); it depends on **20**; blast radius 5.121; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (94.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.4%)
- **Documentation Coverage:** 13.4328% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 91.5)
  * `run` **(Defensive Guards)** (Impact: 30.4)
    * *Intent:* """Run the benchmark tests. This method will execute the benchmark for each combination of keyword a...
  * `validate_action_signature` **(Many-Argument Workhorses)** (Impact: 28.8)
  * `validate_kwargs_variations` **(Defensive Guards)** (Impact: 16.7)
    * *Intent:* """Validate the kwargs_variations dictionary. Validates that the kwargs_variations is a dictionary w...
  * `validate_variation_cols` **(Defensive Guards)** (Impact: 16.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 130`, `args: 31`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 55`
* *Architecture:* `io: 1`, `api: 31`, `import: 20`
* *Defense:* `safety: 16`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.121
  * `Choke Point (Betweenness):` 0.006819 | `Ripple Effect (Closeness):` 0.074586
  * `Imports (Out-Degree: 15):` .doc_utils, .enums, .exceptions, .protocols, .reporters.protocols, .reporters.reporter.options, .reporters.validators.validators, .results...
  * `Imported By (In-Degree: 42):` (Excluded from Brief to save tokens)

### `documentation/html/_static/searchtools.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.662)
- **Top Global Matches:** file_cluster_4: 7.662, file_cluster_10: 10.246, file_cluster_15: 10.452
- **Magnitude:** 413.62 | **LOC:** 633 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 39.155; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.5%), Guard Balance (formerly Safety Score) (60.2%)
- **Documentation Coverage:** 73.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_performSearch` **(Many-Argument Workhorses)** (Impact: 46.3)
    * *Intent:* /** * execute search (requires search index to be loaded) */
  * `performTermsSearch` **(Defensive Guards)** (Impact: 43.2)
    * *Intent:* /** * search for full-text terms in the index */
  * `objectSearchCallback` **(Defensive Guards)** (Impact: 26.8)
  * `_displayItem` **(Many-Argument Workhorses)** (Impact: 26.7)
  * `_parseQuery` **(Defensive Guards)** (Impact: 10.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 48 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 95`, `args: 57`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 59`, `dead_code: 5`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 2`, `concurrency: 4`
* *Defense:* `safety: 29`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 39.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.170483
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/simplebench/reporters/reporter/mixins/_orchestration.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 23.914)
- **Top Global Matches:** file_cluster_3: 23.914, file_cluster_1: 25.517, file_cluster_8: 45.401
- **Magnitude:** 384.8 | **LOC:** 467 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 0.6; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (58.2%), Complexity Load (formerly Cognitive Load) (49.7%), Connectivity (formerly Api Exposure) (15.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dispatch_to_targets` **(Many-Argument Workhorses)** (Impact: 127.6)
  * `_validate_render_by_args` **(Many-Argument Workhorses)** (Impact: 83.2)
  * `render_by_section` **(Many-Argument Workhorses)** (Impact: 55.7)
  * `render_by_case` **(Many-Argument Workhorses)** (Impact: 52.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 50`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `io: 1`, `api: 3`, `import: 19`
* *Defense:* `safety: 7`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.6
  * `Choke Point (Betweenness):` 0.000297 | `Ripple Effect (Closeness):` 0.033243
  * `Imports (Out-Degree: 17):` __future__, argparse, pathlib, rich.table, rich.text, simplebench.case, simplebench.enums, simplebench.exceptions...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/simplebench/session.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.509)
- **Top Global Matches:** file_cluster_0: 8.509, file_cluster_4: 10.134, file_cluster_5: 10.176
- **Magnitude:** 364.52 | **LOC:** 607 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **27** in-repo importer(s); it depends on **21**; blast radius 3.3; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (88.6%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (61.1%)
- **Documentation Coverage:** 3.3898% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `report` **(Compute Cores)** (Impact: 47.4)
    * *Intent:* """Generate reports for all benchmark cases in the session."""
  * `__init__` **(Many-Argument Workhorses)** (Impact: 31.5)
  * `run` **(Compute Cores)** (Impact: 19.4)
    * *Intent:* """Run all benchmark cases in the session. This method iterates over all :class:`~.case.Case` instan...
  * `parse_args` **(Stateful Encapsulated Methods)** (Impact: 15.8)
    * *Intent:* """Parse the command line arguments using the session's :class:`~argparse.ArgumentParser`. This meth...
  * `cases` **(Stateful Encapsulated Methods)** (Impact: 13.2)
    * *Intent:* """Set the tuple of :class:`~simplebench.Cases` for this session. This replaces all existing Cases i...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 113`, `args: 29`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 45`
* *Architecture:* `io: 1`, `api: 30`, `import: 21`
* *Defense:* `safety: 19`, `doc: 39`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.3
  * `Choke Point (Betweenness):` 0.012928 | `Ripple Effect (Closeness):` 0.06658
  * `Imports (Out-Degree: 16):` __future__, argparse, datetime, pathlib, rich.console, rich.progress, simplebench, simplebench.case...
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `src/simplebench/runners.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 14.333)
- **Top Global Matches:** file_cluster_6: 14.333, file_cluster_8: 15.907, file_cluster_4: 19.766
- **Magnitude:** 340.26 | **LOC:** 544 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **19**; blast radius 2.073; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `default_runner` **(Many-Argument Workhorses)** (Impact: 74.0)
  * `calibrate_rounds` **(Many-Argument Workhorses)** (Impact: 71.0)
  * `_run_timed_iteration` **(Many-Argument Workhorses)** (Impact: 27.9)
  * `__init__` **(Generic / Templated Code)** (Impact: 16.0)
  * `run` **(Many-Argument Workhorses)** (Impact: 11.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 59`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 30`, `high_risk_execution: 1`, `state_mutation: 47`, `dead_code: 1`
* *Architecture:* `io: 3`, `api: 6`, `import: 19`
* *Defense:* `safety: 5`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.073
  * `Choke Point (Betweenness):` 0.002399 | `Ripple Effect (Closeness):` 0.056931
  * `Imports (Out-Degree: 14):` .case, .defaults, .enums, .exceptions, .iteration, .results, .session, .tasks...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `src/simplebench/tasks.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.406)
- **Top Global Matches:** file_cluster_0: 8.406, file_cluster_5: 9.031, file_cluster_12: 9.358
- **Magnitude:** 313.8 | **LOC:** 534 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 1.09; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.7%), Connectivity (formerly Api Exposure) (50.8%)
- **Documentation Coverage:** 14.5455% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update` **(Many-Argument Workhorses)** (Impact: 38.1)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 23.0)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 20.6)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 12.3)
    * *Intent:* """Initialize a new RichProgressTasks instance. This instance manages multiple :class:`RichTask` ins...
  * `update` **(Stateful Encapsulated Methods)** (Impact: 10.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 83`, `args: 29`, `func_start: 29`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 24`, `duplicate_logic: 2`
* *Architecture:* `api: 29`, `import: 8`
* *Defense:* `safety: 15`, `doc: 45`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.09
  * `Choke Point (Betweenness):` 2.9e-05 | `Ripple Effect (Closeness):` 0.053445
  * `Imports (Out-Degree: 4):` .enums, .exceptions, .exceptions.tasks, .session, __future__, rich.console, rich.progress, typing
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/simplebench/reporters/reporter/reporter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.685)
- **Top Global Matches:** file_cluster_4: 9.685, file_cluster_5: 10.816, file_cluster_0: 11.591
- **Magnitude:** 313.6 | **LOC:** 647 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **24**; blast radius 1.95; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.1%), Guard Balance (formerly Safety Score) (57.4%)
- **Documentation Coverage:** 6.4516% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `report` **(Many-Argument Workhorses)** (Impact: 80.0)
  * `_validate_subclass_config` **(Defensive Guards)** (Impact: 26.0)
    * *Intent:* """Validate that the subclass has correctly defined its options configuration. This method checks th...
  * `set_default_options` **(Defensive Guards)** (Impact: 18.3)
    * *Intent:* """Set the default options for the reporter. :param options: The options to set as the default, defa...
  * `run_report` **(Many-Argument Workhorses)** (Impact: 14.5)
  * `get_base_unit_for_section` **(Compute Cores)** (Impact: 13.2)
    * *Intent:* """Return the base unit for the specified section. :param section: The section to get the base unit ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 121`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 22`, `planned_debt: 12`
* *Architecture:* `io: 3`, `api: 26`, `import: 25`
* *Defense:* `safety: 10`, `doc: 30`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.95
  * `Choke Point (Betweenness):` 0.007601 | `Ripple Effect (Closeness):` 0.053689
  * `Imports (Out-Degree: 21):` __future__, abc, argparse, pathlib, rich.table, rich.text, simplebench.case, simplebench.defaults...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/simplebench/decorators.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.846)
- **Top Global Matches:** file_cluster_6: 9.846, file_cluster_4: 13.648, file_cluster_8: 16.746
- **Magnitude:** 295.7 | **LOC:** 373 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **10**; blast radius 2.296; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (81.5%), Guard Balance (formerly Safety Score) (68.7%), Connectivity (formerly Api Exposure) (49.7%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `benchmark` **(Many-Argument Workhorses)** (Impact: 159.0)
  * `decorator` **(Compute Cores)** (Impact: 24.3)
    * *Intent:* """The actual decorator that wraps the user's function."""
  * `validate_timer` **(Many-Argument Workhorses)** (Impact: 14.9)
  * `case_action_wrapper` **(Defensive Guards)** (Impact: 11.2)
    * *Intent:* """This wrapper becomes the `action` for the `Case`. It calls the user's decorated function inside `...
  * `get_registered_cases` **(Generic / Templated Code)** (Impact: 1.4)
    * *Intent:* """Retrieve all benchmark cases registered via the `@benchmark` decorator. :return: A list of :class...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 34`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 32`
* *Architecture:* `api: 6`, `import: 10`
* *Defense:* `safety: 6`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.296
  * `Choke Point (Betweenness):` 0.000498 | `Ripple Effect (Closeness):` 0.040637
  * `Imports (Out-Degree: 9):` .case, .doc_utils, .exceptions, .reporters.reporter.options, .runners, .validators, .vcs, __future__...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `documentation/html/_static/language_data.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 7.343)
- **Top Global Matches:** file_cluster_1: 7.343, file_cluster_3: 48.414, file_cluster_8: 70.169
- **Magnitude:** 291.78 | **LOC:** 193 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 39.155; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `stemWord` **(Compute Cores)** (Impact: 68.8)
  * `Stemmer` **(I/O & Config Routines)** (Impact: 52.9)
    * *Intent:* /* Non-minified version is copied as a separate JS file, if available */ /** * Porter Stemmer */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 55 instances
* *State Mutation (weighted view):* 165
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 30`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 55`
* *Architecture:* `api: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 39.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.170483
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/test_decorators.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.471)
- **Top Global Matches:** file_cluster_5: 7.471, file_cluster_7: 10.0, file_cluster_12: 10.372
- **Magnitude:** 278.32 | **LOC:** 708 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.481; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%), Guard Balance (formerly Safety Score) (44.6%), Connectivity (formerly Api Exposure) (13.3%), Complexity Load (formerly Cognitive Load) (5.5%)
- **Documentation Coverage:** 44.1558% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_run_decorated_case` **(Defensive Guards)** (Impact: 9.4)
    * *Intent:* """Test that the action of a decorated case can be run."""
  * `test_decorator_use_field_for_n_valid` **(Defensive Guards)** (Impact: 6.8)
    * *Intent:* """Test that the ``@benchmark`` decorator works correctly with valid use_field_for_n."""
  * `test_benchmark_decorator_registers_case` **(Defensive Guards)** (Impact: 5.5)
    * *Intent:* """Test that the ``@benchmark`` decorator registers a case correctly."""
  * `test_decorator_with_no_parameters` **(Defensive Guards)** (Impact: 3.6)
    * *Intent:* """Test that the ``@benchmark`` decorator works correctly with no optional parameters."""
  * `test_decorator_with_empty_parameters` **(Defensive Guards)** (Impact: 3.5)
    * *Intent:* """Test that the ``@benchmark()`` decorator works correctly with no optional parameters."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 272`, `args: 77`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 21`, `duplicate_logic: 2`, `unreferenced_by_name: 72`
* *Architecture:* `api: 78`, `import: 7`
* *Defense:* `safety: 74`, `doc: 45`, `test: 71`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` __future__, pytest, simplebench.decorators, simplebench.defaults, simplebench.enums, simplebench.exceptions, simplebench.session
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_case.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 5.336)
- **Top Global Matches:** file_cluster_5: 5.336, file_cluster_12: 7.581, file_cluster_7: 8.218
- **Magnitude:** 266.98 | **LOC:** 1140 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.481; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%), Guard Balance (formerly Safety Score) (56.3%), Connectivity (formerly Api Exposure) (11.2%), Complexity Load (formerly Cognitive Load) (3.3%)
- **Documentation Coverage:** 43.4343% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_run` **(Defensive Guards)** (Impact: 13.4)
    * *Intent:* """Test the run method of the Case class. :param capsys: The pytest capsys fixture. :param testspec:...
  * `benchcase_with_size_and_factor` **(Generic / Templated Code)** (Impact: 7.6)
    * *Intent:* """A simple benchmark case function. :param _bench: The benchmark runner. :param kwargs: The keyword...
  * `postrun_benchmark_case` **(I/O & Config Routines)** (Impact: 6.1)
    * *Intent:* """Create and runs a benchmark Case, returning the Case instance. :return: The Case instance after r...
  * `broken_benchcase_missing_bench` **(Generic / Templated Code)** (Impact: 5.1)
    * *Intent:* """A broken benchmark case function that is missing the required 'bench' parameter. :param kwargs: T...
  * `broken_callback_extra_param` **(Generic / Templated Code)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 147`, `args: 57`, `func_start: 49`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 16`, `duplicate_logic: 6`, `unreferenced_by_name: 9`
* *Architecture:* `api: 50`, `import: 18`
* *Defense:* `safety: 9`, `doc: 50`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` .kwargs, .testspec, argparse, functools, inspect, pytest, rich.console, simplebench.case...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/stats/stats.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.863)
- **Top Global Matches:** file_cluster_0: 7.863, file_cluster_5: 8.085, file_cluster_12: 9.433
- **Magnitude:** 262.52 | **LOC:** 614 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 0.824; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.7%), Debt Markers (formerly Tech Debt) (88.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.5%)
- **Documentation Coverage:** 4.7619% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__eq__` **(Compute Cores)** (Impact: 26.9)
    * *Intent:* """Compare two Stats objects for equality. Equality is based on stats statistics and not on object i...
  * `__eq__` **(Compute Cores)** (Impact: 26.7)
    * *Intent:* """Compare this StatsSummary to another Stats or StatsSummary object. Equality is based on stats sta...
  * `from_dict` **(Many-Argument Workhorses)** (Impact: 12.6)
    * *Intent:* """Construct a Stats object from a dictionary. Example: .. code-block:: python stats_dict = { "unit"...
  * `from_dict` **(Many-Argument Workhorses)** (Impact: 9.3)
    * *Intent:* """Construct a StatsSummary object from a dictionary. Example: .. code-block:: python stats_summary_...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 102`, `args: 35`, `func_start: 35`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 27`, `duplicate_logic: 6`
* *Architecture:* `api: 30`, `import: 8`
* *Defense:* `safety: 5`, `doc: 36`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.824
  * `Choke Point (Betweenness):` 0.000396 | `Ripple Effect (Closeness):` 0.041208
  * `Imports (Out-Degree: 5):` ..exceptions, ..si_units, ..validators, .exceptions.stats, __future__, math, statistics, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/simplebench/reporters/graph/matplotlib/reporter/options/options.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.213)
- **Top Global Matches:** file_cluster_0: 6.213, file_cluster_13: 9.717, file_cluster_15: 10.334
- **Magnitude:** 235.0 | **LOC:** 638 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 0.979; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.2%), Connectivity (formerly Api Exposure) (80.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.5%)
- **Documentation Coverage:** 3.0303% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 46.1)
  * `set_default_theme` **(Defensive Guards)** (Impact: 7.9)
    * *Intent:* """Set the default theme for all MatPlotLib graphs. This static method allows setting a global defau...
  * `set_default_style` **(Defensive Guards)** (Impact: 7.8)
    * *Intent:* """Set the default style/theme for all MatPlotLib graphs. This static method allows setting a global...
  * `set_default_y_starts_at_zero` **(Defensive Guards)** (Impact: 7.6)
    * *Intent:* """Set the default value for whether Y-axis starts at zero for all MatPlotLib graphs Setting this to...
  * `set_default_x_labels_rotation` **(Defensive Guards)** (Impact: 7.6)
    * *Intent:* """Set the default rotation angle in degrees for X-axis labels for all MatPlotLib graphs. Setting th...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 82`, `args: 33`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 34`, `import: 8`
* *Defense:* `safety: 4`, `doc: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.979
  * `Choke Point (Betweenness):` 0.000314 | `Ripple Effect (Closeness):` 0.024956
  * `Imports (Out-Degree: 8):` ...enums.style, ...theme, .exceptions, simplebench.exceptions, simplebench.reporters.graph.enums.image_type, simplebench.reporters.graph.options, simplebench.validators, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/reporters/reporter/mixins/test_prioritization.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.759)
- **Top Global Matches:** file_cluster_4: 8.759, file_cluster_0: 10.221, file_cluster_5: 10.549
- **Magnitude:** 231.66 | **LOC:** 663 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.481; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.6%), Complexity Load (formerly Cognitive Load) (13.6%), Connectivity (formerly Api Exposure) (8.5%)
- **Documentation Coverage:** 7.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_prioritized_options_testspecs` **(Compute Cores)** (Impact: 41.0)
    * *Intent:* """Get test specifications for get_prioritized_options method. Because the default reporter options ...
  * `get_prioritized_file_append_and_unique_testspecs` **(I/O & Config Routines)** (Impact: 12.1)
    * *Intent:* """Get test specifications for get_prioritized_file_append and get_prioritized_file_unique methods. ...
  * `get_prioritized_options_helper` **(Many-Argument Workhorses)** (Impact: 10.0)
  * `prioritize_options_testspec` **(Compute Cores)** (Impact: 5.4)
    * *Intent:* """Create a TestSpec for a prioritization test case. :param testcase: The test case to create a Test...
  * `get_prioritized_file_suffix_testspecs` **(I/O & Config Routines)** (Impact: 3.9)
    * *Intent:* """Get test specifications for get_prioritized_file_suffix method. :return: A list of TestSpec insta...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 89`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 90`, `unreferenced_by_name: 7`
* *Architecture:* `api: 15`, `import: 12`
* *Defense:* `safety: 3`, `doc: 22`, `test: 14`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` ....factories, ....testspec, dataclasses, pytest, simplebench.case, simplebench.enums, simplebench.exceptions, simplebench.reporters.choice.choice...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/reporters/csv/reporter/reporter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 11.39)
- **Top Global Matches:** file_cluster_3: 11.39, file_cluster_8: 22.482, file_cluster_6: 34.605
- **Magnitude:** 223.08 | **LOC:** 213 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 0.673; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.7%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render` **(Many-Argument Workhorses)** (Impact: 113.2)
    * *Intent:* """Renders the benchmark results as tagged CSV data and returns it as a string. :param case: The :cl...
  * `__init__` **(Compute Cores)** (Impact: 4.5)
    * *Intent:* """Initialize the :class:`~.CSVReporter`. .. note:: The exception documentation below refers to vali...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 43`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 34`
* *Architecture:* `api: 3`, `import: 18`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.673
  * `Choke Point (Betweenness):` 0.000372 | `Ripple Effect (Closeness):` 0.001856
  * `Imports (Out-Degree: 18):` .config, .exceptions, .options, __future__, csv, io, simplebench.case, simplebench.defaults...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/simplebench/reporters/choice/choice_conf.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.71)
- **Top Global Matches:** file_cluster_5: 8.71, file_cluster_4: 9.839, file_cluster_12: 10.036
- **Magnitude:** 216.46 | **LOC:** 485 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **8**; blast radius 3.046; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.5%), Connectivity (formerly Api Exposure) (52.8%)
- **Documentation Coverage:** 5.8824% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 74.8)
  * `__eq__` **(Compute Cores)** (Impact: 27.2)
    * *Intent:* """Check equality between two :class:`~.ChoiceConf` instances. :param other: The other :class:`~.Cho...
  * `__hash__` **(Generic / Templated Code)** (Impact: 2.5)
    * *Intent:* """Compute a hash value for the :class:`~.ChoiceConf` instance. :return: The computed hash value. :r...
  * `flags` **(Generic / Templated Code)** (Impact: 2.3)
    * *Intent:* """Flags associated with the choice. These are used for command-line selection. They must be unique ...
  * `output_format` **(Generic / Templated Code)** (Impact: 2.0)
    * *Intent:* """Output format for the choice. This is the output format that the associated :class:`~simplebench....
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 51`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 23`, `planned_debt: 1`
* *Architecture:* `api: 18`, `import: 8`
* *Defense:* `safety: 1`, `doc: 33`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.046
  * `Choke Point (Betweenness):` 0.00147 | `Ripple Effect (Closeness):` 0.057069
  * `Imports (Out-Degree: 8):` collections.abc, simplebench.enums, simplebench.exceptions, simplebench.reporters.choice.exceptions, simplebench.reporters.protocols, simplebench.reporters.reporter.options, simplebench.validators, typing
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `src/simplebench/reporters/rich_table/reporter/reporter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.793)
- **Top Global Matches:** file_cluster_3: 9.793, file_cluster_8: 21.726, file_cluster_6: 34.125
- **Magnitude:** 198.32 | **LOC:** 226 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 0.733; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.4%), Complexity Load (formerly Cognitive Load) (65.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render` **(Many-Argument Workhorses)** (Impact: 129.9)
    * *Intent:* """Prints the benchmark results in a rich table format if available. It creates a :class:`~rich.tabl...
  * `__init__` **(Compute Cores)** (Impact: 4.8)
    * *Intent:* """Initialize the RichTableReporter. .. note:: The exception documentation below refers to validatio...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 38`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 20`
* *Architecture:* `api: 3`, `import: 16`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.733
  * `Choke Point (Betweenness):` 0.000394 | `Ripple Effect (Closeness):` 0.00165
  * `Imports (Out-Degree: 16):` .config, .exceptions, .options, __future__, rich.table, simplebench.case, simplebench.defaults, simplebench.enums...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/factories/reporter/base.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.814)
- **Top Global Matches:** file_cluster_5: 7.814, file_cluster_0: 9.271, file_cluster_12: 10.187
- **Magnitude:** 194.84 | **LOC:** 751 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **20**; blast radius 1.055; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (80.2%), Guard Balance (formerly Safety Score) (56.6%), Complexity Load (formerly Cognitive Load) (15.2%)
- **Documentation Coverage:** 37.037% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `choice_factory` **(Many-Argument Workhorses)** (Impact: 26.6)
  * `choices_factory` **(Defensive Guards)** (Impact: 15.2)
  * `choice_conf_factory` **(Many-Argument Workhorses)** (Impact: 11.9)
  * `reporter_factory` **(Defensive Guards)** (Impact: 11.8)
  * `choices_conf_factory` **(Defensive Guards)** (Impact: 9.5)
    * *Intent:* """Factory function to return a cached ChoicesConf instance for testing. :param choices: A tuple of ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 90`, `args: 27`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 15`
* *Architecture:* `api: 28`, `import: 20`
* *Defense:* `safety: 9`, `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.055
  * `Choke Point (Betweenness):` 0.001053 | `Ripple Effect (Closeness):` 0.015594
  * `Imports (Out-Degree: 23):` ...cache_factory, ...kwargs, .._primitives, .._utils, ..argparse, ..case, ..path, ..reporter_callback...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/simplebench/results.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 5.448)
- **Top Global Matches:** file_cluster_5: 5.448, file_cluster_12: 9.101, file_cluster_0: 10.143
- **Magnitude:** 186.8 | **LOC:** 670 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **10**; blast radius 2.164; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (53.9%), Guard Balance (formerly Safety Score) (53.8%), Mutation Surface (formerly State Flux) (36.9%)
- **Documentation Coverage:** 3.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `results_section` **(Defensive Guards)** (Impact: 17.0)
    * *Intent:* """Returns the requested section of the benchmark results. Args: section (Section): The section of t...
  * `_validate_variation_cols` **(Stateful Encapsulated Methods)** (Impact: 14.1)
    * *Intent:* """Validate the variation_cols dictionary. Args: value (dict[str, str]): The variation_cols dictiona...
  * `_validate_variation_marks` **(Stateful Encapsulated Methods)** (Impact: 12.5)
    * *Intent:* """Validate the variation_marks dictionary. Performs shallow copy of the dictionary to help mitigate...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 11.5)
  * `_validate_iterations` **(Stateful Encapsulated Methods)** (Impact: 8.0)
    * *Intent:* """Validate the iterations Sequence. Args: value (Sequence[Iteration]): The iterations Sequence to v...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 130`, `args: 33`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 9`
* *Architecture:* `api: 24`, `import: 10`
* *Defense:* `safety: 13`, `doc: 35`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.164
  * `Choke Point (Betweenness):` 0.002426 | `Ripple Effect (Closeness):` 0.064514
  * `Imports (Out-Degree: 11):` .defaults, .enums, .iteration, .stats, .validators, __future__, copy, simplebench.exceptions...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `src/simplebench/cli.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 16.097)
- **Top Global Matches:** file_cluster_3: 16.097, file_cluster_1: 34.061, file_cluster_8: 36.979
- **Magnitude:** 185.96 | **LOC:** 235 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **12**; blast radius 2.297; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (81.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.8%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 59.7)
  * `_configure_session_from_args` **(Many-Argument Workhorses)** (Impact: 36.4)
  * `_create_parser` **(Stateful Encapsulated Methods)** (Impact: 5.0)
    * *Intent:* """Create the ArgumentParser instance for the SimpleBench CLI. :return: An ArgumentParser instance c...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 24 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 36`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 33`
* *Architecture:* `io: 4`, `api: 1`, `import: 12`
* *Defense:* `safety: 9`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.297
  * `Choke Point (Betweenness):` 0.000621 | `Ripple Effect (Closeness):` 0.040428
  * `Imports (Out-Degree: 6):` .case, .decorators, .doc_utils, .enums, .exceptions, .session, __future__, argparse...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `tests/test_stats.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.695)
- **Top Global Matches:** file_cluster_0: 6.695, file_cluster_15: 7.854, file_cluster_12: 7.975
- **Magnitude:** 184.46 | **LOC:** 1109 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.481; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (48.4%), Connectivity (formerly Api Exposure) (8.1%), Complexity Load (formerly Cognitive Load) (5.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_stats_initalization` **(Defensive Guards)** (Impact: 24.0)
    * *Intent:* """Test that data is correctly initialized in stats classes. :param section: Section to test. :type ...
  * `test_computed_stats_values` **(Defensive Guards)** (Impact: 17.7)
    * *Intent:* """Test that computed stats properties return correct values. :param stats_data: Sequence of stats d...
  * `test_as_dict` **(Defensive Guards)** (Impact: 9.1)
    * *Intent:* """Test that as_dict returns correct values. :param stats_data: Sequence of stats data. :type stats_...
  * `test_computed_stats_read_only` **(Generic / Templated Code)** (Impact: 6.8)
    * *Intent:* """Test that computed stats properties exist and are read-only. :param stats_instances: List of stat...
  * `test_stats_init` **(Generic / Templated Code)** (Impact: 4.1)
    * *Intent:* """Test that the stats module is initialized correctly for shared aspects of init. :param stats_clas...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 140`, `args: 18`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 26`, `unreferenced_by_name: 11`
* *Architecture:* `api: 16`, `import: 10`
* *Defense:* `safety: 30`, `doc: 18`, `test: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` .testspec, enum, pytest, simplebench.enums, simplebench.exceptions, simplebench.iteration, simplebench.stats, simplebench.stats.exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/factories/_primitives.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.128)
- **Top Global Matches:** file_cluster_0: 7.128, file_cluster_13: 11.384, file_cluster_5: 12.13
- **Magnitude:** 182.46 | **LOC:** 821 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **8**; blast radius 1.419; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (85.4%), Complexity Load (formerly Cognitive Load) (1.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `description_factory` **(Generic / Templated Code)** (Impact: 3.3)
    * *Intent:* """Return a description string for testing purposes. :param cache_id: An optional identifier to dist...
  * `output_path_factory` **(Generic / Templated Code)** (Impact: 2.2)
    * *Intent:* """Return a default output Path instance for testing purposes. This path points to a directory insid...
  * `rounds_factory` **(Generic / Templated Code)** (Impact: 2.1)
    * *Intent:* """Return a default number of rounds for testing purposes. This is for use in configuring benchmark ...
  * `variation_cols_factory` **(Generic / Templated Code)** (Impact: 2.1)
    * *Intent:* """Return a dictionary of variation columns for testing purposes. This is for use in configuring ben...
  * `kwargs_variations_factory` **(Generic / Templated Code)** (Impact: 2.1)
    * *Intent:* """Return a set of kwargs variations for testing purposes. This is for use in configuring benchmark ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 148`, `args: 67`, `func_start: 67`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 67`, `import: 8`
* *Defense:* `doc: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.419
  * `Choke Point (Betweenness):` 4.8e-05 | `Ripple Effect (Closeness):` 0.020906
  * `Imports (Out-Degree: 3):` ..cache_factory, .path, __future__, pathlib, rich.table, rich.text, simplebench.enums, typing
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `tests/reporters/validators/test_validate_report_renderer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.188)
- **Top Global Matches:** file_cluster_5: 7.188, file_cluster_0: 7.543, file_cluster_12: 8.168
- **Magnitude:** 181.28 | **LOC:** 588 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.481; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.1%), Connectivity (formerly Api Exposure) (10.3%), Complexity Load (formerly Cognitive Load) (2.4%)
- **Documentation Coverage:** 95.9184% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_report` **(Many-Argument Workhorses)** (Impact: 13.8)
  * `invalid_render_with_extra_return_type` **(Many-Argument Workhorses)** (Impact: 7.6)
  * `invalid_render_case_wrong_type` **(Generic / Templated Code)** (Impact: 7.4)
  * `invalid_render_case_missing_type_hint` **(Generic / Templated Code)** (Impact: 7.4)
  * `invalid_render_extra_parameter` **(Many-Argument Workhorses)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 129`, `args: 25`, `func_start: 25`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 10`, `unreferenced_by_name: 3`
* *Architecture:* `io: 1`, `api: 26`, `import: 19`
* *Defense:* `doc: 29`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.481
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` ...factories, ...testspec, argparse, pathlib, pytest, rich.table, rich.text, simplebench.case...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/kwargs/reporters/reporter/methods/dispatch_to_targets_method_kwargs.py` (PYTHON) | Magnitude: 11.68 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 28, indent_spaces: 15, import: 13, core_var_decl: 10
- `tests/test_cache_factory.py` (PYTHON) | Magnitude: 128.46 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 55, core_var_decl: 42, design_snake_case: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/simplebench/reporters/json/reporter/config.py` (PYTHON) | Magnitude: 28.44 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 49, core_var_decl: 28, design_snake_case: 17, structural_boundaries: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/simplebench/reporters/csv/reporter/options/fields.py` (PYTHON) | Magnitude: 28.32 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 14, state_mutation: 12, indent_spaces: 12, core_var_decl: 12
- `src/simplebench/reporters/rich_table/reporter/options/fields.py` (PYTHON) | Magnitude: 28.32 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 14, state_mutation: 12, indent_spaces: 12, core_var_decl: 12
- `src/simplebench/exceptions/iteration.py` (PYTHON) | Magnitude: 29.38 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 15, indent_spaces: 15, state_mutation: 14, core_var_decl: 14
- `src/simplebench/reporters/rich_table/reporter/exceptions.py` (PYTHON) | Magnitude: 27.38 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 15, doc: 14, state_mutation: 12, core_var_decl: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `tests/testspec/context.py` (PYTHON) | Magnitude: 27.94 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 15, branch: 11, structural_boundaries: 8, panics_and_aborts: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `examples/example_scatterplot.py` (PYTHON) | Magnitude: 2.8 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 5, core_var_decl: 3, design_snake_case: 3, structural_boundaries: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/testspec/__init__.py` (PYTHON) | Magnitude: 18.52 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 22, indent_spaces: 12, import: 11, state_mutation: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/simplebench/enums/__init__.py` (PYTHON) | Magnitude: 17.36 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 16, import: 8, indent_spaces: 8, api: 1
- `documentation/html/genindex.html` (HTML) | Magnitude: 0.18 | Delta: **0.147** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 3557, io: 3512, structural_boundaries: 2578, core_var_decl: 1923

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `tests/kwargs/reporters/choice_conf_kwargs.py` (PYTHON) | Magnitude: 9.0 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 14, core_var_decl: 14, design_pascal_case: 14
- `src/simplebench/enums/section.py` (PYTHON) | Magnitude: 11.04 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 9, doc: 8, indent_spaces: 7, state_mutation: 5
- `tests/factories/results.py` (PYTHON) | Magnitude: 23.12 | Delta: **0.128** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 102, core_var_decl: 66, design_snake_case: 66, structural_boundaries: 26

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/simplebench/cli.py` -> Churn: **81.55%** | Cog Load: 55.7463% | Debt: 0.0%
- `src/simplebench/exceptions/__init__.py` -> Churn: **73.25%** | Cog Load: 27.4085% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/simplebench/case.py` -> **Jerilyn** (100.0% isolated ownership) | Magnitude: 434.82
- `src/simplebench/session.py` -> **Jerilyn** (100.0% isolated ownership) | Magnitude: 364.52
- `src/simplebench/runners.py` -> **Jerilyn** (100.0% isolated ownership) | Magnitude: 340.26
- `src/simplebench/decorators.py` -> **Jerilyn** (100.0% isolated ownership) | Magnitude: 295.7
- `tests/test_decorators.py` -> **Jerilyn** (100.0% isolated ownership) | Magnitude: 278.32

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/simplebench/session.py` -> **Severity: 1.293** (Bridge: 0.0129 * Flux: 99.9938%)
- `src/simplebench/reporters/reporter/reporter.py` -> **Severity: 0.755** (Bridge: 0.0076 * Flux: 99.3842%)
- `src/simplebench/case.py` -> **Severity: 0.682** (Bridge: 0.0068 * Flux: 99.9834%)
- `src/simplebench/exceptions/__init__.py` -> **Severity: 0.323** (Bridge: 0.0032 * Flux: 99.9589%)
- `src/simplebench/__init__.py` -> **Severity: 0.274** (Bridge: 0.0088 * Flux: 31.0026%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `documentation/html/_static/language_data.js` -> **Severity: 15.012** (Embedded: 0.1705 * Error Risk: 88.0556%)
- `documentation/html/_static/searchtools.js` -> **Severity: 10.26** (Embedded: 0.1705 * Error Risk: 60.1811%)
- `src/simplebench/exceptions/__init__.py` -> **Severity: 9.153** (Embedded: 0.1496 * Error Risk: 61.2003%)
- `src/simplebench/enums/__init__.py` -> **Severity: 8.308** (Embedded: 0.1643 * Error Risk: 50.5714%)
- `src/simplebench/exceptions/case.py` -> **Severity: 7.214** (Embedded: 0.0955 * Error Risk: 75.5286%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `documentation/html/_static/searchtools.js` -> **Severity: 2871.365** (Blast Radius: 39.155 * Doc Risk: 73.3333%)
- `documentation/html/_static/language_data.js` -> **Severity: 1957.75** (Blast Radius: 39.155 * Doc Risk: 50.0%)
- `src/simplebench/validators/misc.py` -> **Severity: 386.964** (Blast Radius: 4.925 * Doc Risk: 78.5714%)
- `tests/cache_factory.py` -> **Severity: 252.98** (Blast Radius: 3.614 * Doc Risk: 70.0%)
- `src/simplebench/validators/validate_iterable_of_type.py` -> **Severity: 250.1** (Blast Radius: 2.501 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 3329 call pairs -- scoped 48.1%, unique 0.0%, ambiguous 4.5%, external 47.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 3046 | 52.0% | 0.0% | 4.8% | 43.2% |
| javascript | 279 | 6.5% | 0.0% | 0.7% | 92.8% |
| shell | 4 | 0.0% | 0.0% | 0.0% | 100.0% |

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
