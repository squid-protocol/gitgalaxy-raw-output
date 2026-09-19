# ARCHITECTURAL_BRIEF: python-simplebench
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/JerilynFranz/python-simplebench.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 723 analyzed artifact(s), 103451 LOC.
- **Load-bearing artifact:** `documentation/html/genindex.html` -- 274 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/simplebench/reporters/reporter/reporter.py` -- pulls in 27 dependencies, the widest assembly point in the scan.
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
| Analyzed Artifacts (Scanned) | 723 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 981 |
| Total LOC | 103451 |
| Volatility Index | 0.012 |
| % Scanned of codebase = | 42.4% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4964 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5305 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8667 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 27 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 291 | 20636 | 40.2% |
| PLAINTEXT | 200 | 1 | 27.7% |
| HTML | 193 | 72197 | 26.7% |
| CSS | 17 | 8288 | 2.4% |
| JAVASCRIPT | 10 | 1177 | 1.4% |
| MARKDOWN | 2 | 0 | 0.3% |
| YAML | 2 | 37 | 0.3% |
| JSON | 2 | 1036 | 0.3% |
| XML | 2 | 0 | 0.3% |
| MAKEFILE | 1 | 21 | 0.1% |
| SHELL | 1 | 4 | 0.1% |
| BATCH | 1 | 52 | 0.1% |
| CSV | 1 | 2 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `4.858`
> **Composition Archetype:** `Hub-Coupled App` (z +4.86; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 64%, Declarative / Non-Code 11%, Generic / Templated Code Files 10%, Large Core Modules (2) 5%, Many-Argument Workhorses Files 4%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 521 | 72.1% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 201 | 27.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 981*

**Composition by Extension & Reason:**
- `.html`: 277x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Packed Payload Guard (Impossible Density: 3.25 hits/line), 3x Packed Payload Guard (Impossible Density: 3.89 hits/line)
- `.rst`: 193x Excluded (Unsupported Extension: '.rst')
- `.txt`: 193x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.doctree`: 147x Excluded (Unsupported Extension: '.doctree')
- `.js`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 2 exceeds 500 chars), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.css`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 258 LOC), 1x Excluded (Machine-Generated Source Code Signature: 320 LOC)
- `.svg`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Static Asset Blob without Intent: 1266 LOC), 2x Excluded (Machine-Generated Source Code Signature: 278 LOC)
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 51001 LOC exceeds safe regex boundaries), 1x Excluded (Unsupported Extension: '.code-workspace')
- `.png`: 6x Excluded (Explicitly Denied Extension: '.png')
- `.map`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.yaml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.inv`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.inv')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 78.9 | 7.0 | 5.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.8 | 50.6 | 49.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 2.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.4 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 18.5 | 13.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 99.8 | 1.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 25.2 | 11.7 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 48.2 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.7 | 0.5 | 0.1 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 19.2 | 31.6 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 48.4 | 33.3 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 159 | 47 | 0 | `tests/test_stats.py` |
| cleanup | 6 | 5 | 0 | `src/simplebench/reporters/graph/scatterplot/reporter/reporter.py` |
| guards | 1020 | 169 | 3 | `tests/test_decorators.py` |
| danger | 1131 | 118 | 4 | `src/simplebench/validators/misc.py` |
| concurrency | 37 | 9 | 0 | `tests/timeout/test_timeout.py` |
| connectivity | 10379 | 435 | 43 | `documentation/_static/styles/furo.css` |
| io | 27965 | 226 | 99 | `documentation/html/genindex.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 2 | 1 | 0 | `documentation/_helpers/doctest_utils.py` |
| time | 14 | 4 | 0 | `tests/timeout/test_timeout.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 53 | 12 | 0 | `documentation/html/_static/language_data.js` |
| events | 719 | 225 | 3 | `tests/test_case.py` |
| tests | 454 | 48 | 0 | `tests/test_decorators.py` |
| docs | 5713 | 478 | 16 | `src/simplebench/reporters/reporter/exceptions/reporter.py` |
| debt | 101 | 31 | 0 | `src/simplebench/tasks.py` |
| mutation | 53278 | 459 | 204 | `documentation/html/genindex.html` |
| dead_code | 257 | 71 | 0 | `tests/test_decorators.py` |
| credential | 49 | 7 | 0 | `documentation/html/genindex.html` |
| threat | 2484 | 236 | 11 | `documentation/html/genindex.html` |
| ml_ai | 11604 | 205 | 60 | `documentation/html/reports/rich_table_report.html` |
| ui | 3803 | 225 | 12 | `documentation/html/source/simplebench.html` |

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
3. **argparse.py** (`tests/factories/argparse.py`) — 24 inbound connections
4. **simplebench.html** (`documentation/html/source/simplebench.html`) — 20 inbound connections
5. **simplebench.reporters.reporter.options.html** (`documentation/html/source/simplebench.reporters.reporter.options.html`) — 19 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **reporter.py** (`src/simplebench/reporters/reporter/reporter.py`) — 27 outbound dependencies
2. **session.py** (`src/simplebench/session.py`) — 22 outbound dependencies
3. **case.py** (`src/simplebench/case.py`) — 21 outbound dependencies
4. **reporter.py** (`src/simplebench/reporters/json/reporter/reporter.py`) — 21 outbound dependencies
5. **_orchestration.py** (`src/simplebench/reporters/reporter/mixins/_orchestration.py`) — 21 outbound dependencies

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
| `src/simplebench` | 15 | 2488.28 | 26.03% | 2.31% |
| `tests` | 13 | 1251.84 | 6.22% | 0.0% |
| `documentation/html/_static` | 16 | 1229.24 | 25.33% | 14.42% |
| `src/simplebench/validators` | 4 | 722.22 | 13.98% | 0.0% |
| `src/simplebench/reporters/reporter/mixins` | 5 | 687.4 | 24.93% | 3.59% |
| `tests/testspec` | 13 | 616.88 | 10.38% | 0.0% |
| `src/simplebench/reporters/reporter` | 6 | 591.78 | 18.81% | 9.21% |
| `src/simplebench/exceptions` | 12 | 531.92 | 2.28% | 8.33% |
| `tests/factories` | 11 | 502.2 | 3.09% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/simplebench/exceptions/__init__.py` -> **100.0%** Exposure
- `documentation/html/_static/copybutton_funcs.js` -> **94.2049%** Exposure
- `src/simplebench/stats/stats.py` -> **89.8692%** Exposure
- `documentation/Makefile` -> **73.1059%** Exposure
- `documentation/html/_static/doctools.js` -> **71.9174%** Exposure
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
- **Unknown Dependencies:** `1246` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/validators/misc.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 495.64 | **LOC:** 1100 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.499; role: Pure Consumer (Orchestrator)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` pathlib, re, simplebench.exceptions, simplebench.type_proxies.lazy_type_proxy, simplebench.validators.exceptions, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/case.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 434.82 | **LOC:** 1016 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (94.6%), Guard Balance (formerly Safety Score) (87.7%), Test Surface (formerly Verification) (80.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .doc_utils, .enums, .exceptions, .protocols, .reporters.protocols, .reporters.reporter.options, .reporters.validators.validators, .results...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `documentation/html/_static/searchtools.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 419.82 | **LOC:** 633 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 62.83; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.9%), Complexity Load (formerly Cognitive Load) (73.5%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_performSearch` **(Many-Argument Workhorses)** (Impact: 46.3)
    * *Intent:* /** * execute search (requires search index to be loaded) */
  * `performTermsSearch` **(Defensive Guards)** (Impact: 43.2)
    * *Intent:* /** * search for full-text terms in the index */
  * `objectSearchCallback` **(Defensive Guards)** (Impact: 27.2)
  * `_displayItem` **(Many-Argument Workhorses)** (Impact: 26.8)
  * `_orderResultsByScoreThenName` **(Defensive Guards)** (Impact: 11.5)
    * *Intent:* // Helper function used by query() to order search results. // Each input is an array of [docname, t...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 48 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 95`, `args: 57`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 59`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 4`, `concurrency: 4`
* *Defense:* `safety: 29`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 62.83
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.237943
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/simplebench/reporters/reporter/mixins/_orchestration.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 384.8 | **LOC:** 467 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **21**; blast radius 0.605; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (74.6%), Complexity Load (formerly Cognitive Load) (49.7%), Connectivity (formerly Api Exposure) (15.4%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.605
  * `Choke Point (Betweenness):` 1.5e-05 | `Ripple Effect (Closeness):` 0.001244
  * `Imports (Out-Degree: 15):` __future__, argparse, pathlib, rich.table, rich.text, runtime, simplebench.case, simplebench.enums...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/simplebench/session.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 364.52 | **LOC:** 607 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (88.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.3%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` __future__, argparse, datetime, mybenchmark.runners, pathlib, rich.console, rich.progress, simplebench...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/runners.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 340.26 | **LOC:** 544 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.9%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%)
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
* *Risk/State:* `safety_bypasses: 30`, `high_risk_execution: 1`, `state_mutation: 47`, `dead_code: 2`
* *Architecture:* `io: 3`, `api: 6`, `import: 19`
* *Defense:* `safety: 5`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .case, .defaults, .enums, .exceptions, .iteration, .results, .session, .tasks...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/tasks.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 313.8 | **LOC:** 534 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.2%), Connectivity (formerly Api Exposure) (50.8%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .enums, .exceptions, .exceptions.tasks, .session, __future__, rich.console, rich.progress, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/reporters/reporter/reporter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 313.6 | **LOC:** 647 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.6%), Guard Balance (formerly Safety Score) (72.4%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` __future__, abc, argparse, issues, of, pathlib, rich.table, rich.text...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `documentation/html/_static/language_data.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 296.78 | **LOC:** 193 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 62.83; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.5%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `stemWord` **(Compute Cores)** (Impact: 68.8)
  * `Stemmer` **(I/O & Config Routines)** (Impact: 57.9)
    * *Intent:* /* Non-minified version is copied as a separate JS file, if available */ /** * Porter Stemmer */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 55 instances
* *State Mutation (weighted view):* 165
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 30`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 55`
* *Architecture:* `api: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 62.83
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.237943
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/simplebench/decorators.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 295.7 | **LOC:** 373 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (81.5%), Test Surface (formerly Verification) (80.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .case, .doc_utils, .exceptions, .reporters.reporter.options, .runners, .validators, .vcs, __future__...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_decorators.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 278.32 | **LOC:** 708 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%), Guard Balance (formerly Safety Score) (35.5%), Connectivity (formerly Api Exposure) (13.3%), Complexity Load (formerly Cognitive Load) (5.5%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` __future__, pytest, simplebench.decorators, simplebench.defaults, simplebench.enums, simplebench.exceptions, simplebench.session
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_case.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 266.98 | **LOC:** 1140 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (68.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%), Connectivity (formerly Api Exposure) (11.2%), Complexity Load (formerly Cognitive Load) (3.3%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` .kwargs, .testspec, __future__, argparse, functools, inspect, pytest, rich.console...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/stats/stats.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 262.52 | **LOC:** 614 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.7%), Debt Markers (formerly Tech Debt) (89.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.1%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ..exceptions, ..si_units, ..validators, .exceptions.stats, __future__, math, statistics, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/reporters/graph/matplotlib/reporter/options/options.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 235.0 | **LOC:** 638 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.2%), Connectivity (formerly Api Exposure) (80.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ...enums.style, ...theme, .exceptions, simplebench.exceptions, simplebench.reporters.graph.enums.image_type, simplebench.reporters.graph.options, simplebench.validators, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/reporters/reporter/mixins/test_prioritization.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 231.66 | **LOC:** 663 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (79.3%), Complexity Load (formerly Cognitive Load) (13.6%), Connectivity (formerly Api Exposure) (8.5%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` ....factories, ....testspec, dataclasses, pytest, simplebench.case, simplebench.enums, simplebench.exceptions, simplebench.reporters.choice.choice...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/reporters/csv/reporter/reporter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 223.08 | **LOC:** 213 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` .config, .exceptions, .options, __future__, csv, io, simplebench.case, simplebench.defaults...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/reporters/choice/choice_conf.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 216.46 | **LOC:** 485 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (52.8%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` collections.abc, simplebench.enums, simplebench.exceptions, simplebench.reporters.choice.exceptions, simplebench.reporters.protocols, simplebench.reporters.reporter.options, simplebench.validators, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/reporters/rich_table/reporter/reporter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 198.32 | **LOC:** 226 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` .config, .exceptions, .options, __future__, rich.table, simplebench.case, simplebench.defaults, simplebench.enums...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/factories/reporter/base.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 194.84 | **LOC:** 751 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (80.2%), Guard Balance (formerly Safety Score) (71.3%), Complexity Load (formerly Cognitive Load) (15.2%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` ...cache_factory, ...kwargs, .._primitives, .._utils, ..argparse, ..case, ..path, ..reporter_callback...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/results.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 186.8 | **LOC:** 670 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.6%), Connectivity (formerly Api Exposure) (53.9%), Mutation Surface (formerly State Flux) (36.9%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .defaults, .enums, .iteration, .stats, .validators, __future__, copy, simplebench.exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/cli.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 185.96 | **LOC:** 235 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (81.5%), Test Surface (formerly Verification) (80.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .case, .decorators, .doc_utils, .enums, .exceptions, .session, __future__, argparse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_stats.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 184.46 | **LOC:** 1109 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (45.7%), Connectivity (formerly Api Exposure) (8.1%), Complexity Load (formerly Cognitive Load) (5.6%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .testspec, enum, pytest, simplebench.enums, simplebench.exceptions, simplebench.iteration, simplebench.stats, simplebench.stats.exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/factories/_primitives.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 182.46 | **LOC:** 821 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **8**; blast radius 1.886; role: Transceiver (Middle-Tier)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.886
  * `Choke Point (Betweenness):` 9e-05 | `Ripple Effect (Closeness):` 0.02054
  * `Imports (Out-Degree: 3):` ..cache_factory, .path, __future__, pathlib, rich.table, rich.text, simplebench.enums, typing
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `tests/reporters/validators/test_validate_report_renderer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 181.28 | **LOC:** 588 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.0%), Connectivity (formerly Api Exposure) (10.3%), Complexity Load (formerly Cognitive Load) (2.4%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` ...factories, ...testspec, argparse, pathlib, pytest, rich.table, rich.text, simplebench.case...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/simplebench/cli.py` -> Churn: **81.55%** | Cog Load: 55.7463% | Debt: 0.0%
- `src/simplebench/exceptions/__init__.py` -> Churn: **73.25%** | Cog Load: 27.4085% | Debt: 100.0%
- `documentation/tutorials/parameterized/minimal_parameterized_benchmark.py` -> Churn: **63.09%** | Cog Load: 3.0704% | Debt: 62.2459%

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

- `src/simplebench/reporters/choices/_base.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.9973%)
- `src/simplebench/reporters/reporter/mixins/_argparse.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.0611%)
- `src/simplebench/reporters/reporter/mixins/_orchestration.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.9302%)
- `src/simplebench/reporters/reporter/mixins/_targets.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `src/simplebench/stats/exceptions/memory_usage.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 91.6827%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `documentation/html/_static/language_data.js` -> **Severity: 23.746** (Embedded: 0.2379 * Error Risk: 99.7975%)
- `documentation/html/_static/searchtools.js` -> **Severity: 18.767** (Embedded: 0.2379 * Error Risk: 78.8705%)
- `tests/cache_factory.py` -> **Severity: 2.282** (Embedded: 0.0238 * Error Risk: 96.0283%)
- `tests/factories/argparse.py` -> **Severity: 2.158** (Embedded: 0.0315 * Error Risk: 68.5924%)
- `tests/factories/path.py` -> **Severity: 0.859** (Embedded: 0.0148 * Error Risk: 58.0716%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `documentation/html/_static/searchtools.js` -> **Severity: 4712.25** (Blast Radius: 62.83 * Doc Risk: 75.0%)
- `documentation/html/_static/language_data.js` -> **Severity: 3141.5** (Blast Radius: 62.83 * Doc Risk: 50.0%)
- `tests/cache_factory.py` -> **Severity: 322.21** (Blast Radius: 4.603 * Doc Risk: 70.0%)
- `tests/factories/argparse.py` -> **Severity: 101.92** (Blast Radius: 2.548 * Doc Risk: 40.0%)
- `tests/kwargs/reporters/reporter/reporter_config_kwargs.py` -> **Severity: 92.3** (Blast Radius: 0.923 * Doc Risk: 100.0%)

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
