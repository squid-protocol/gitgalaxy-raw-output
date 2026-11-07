# ARCHITECTURAL_BRIEF: rich
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/Textualize/rich.git` |
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
- **Scope:** 436 analyzed artifact(s), 37503 LOC.
- **Load-bearing artifact:** `rich/console.py` -- 110 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `rich/console.py` -- pulls in 52 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `rich/console.py` at magnitude 2260.42 (structural weight, not risk).
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
| Total Artifacts | 553 |
| Analyzed Artifacts (Scanned) | 436 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 117 |
| Total LOC | 37503 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 78.8% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2964 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2361 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 12.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.5656 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 18 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 200 | 36375 | 45.9% |
| JSON | 179 | 834 | 41.1% |
| MARKDOWN | 42 | 0 | 9.6% |
| YAML | 9 | 178 | 2.1% |
| XML | 2 | 75 | 0.5% |
| PLAINTEXT | 2 | 0 | 0.5% |
| MAKEFILE | 1 | 15 | 0.2% |
| BATCH | 1 | 26 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 436 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 57%, Generic / Templated Code Files 13%, Declarative / Non-Code 11%, Large Core Modules (2) 8%, Many-Argument Workhorses Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 214 | 49.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Minified & Vendor Opaque Mass | 178 | 40.8% |
| Static: Literature & Documentation | 44 | 10.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 117*

**Composition by Extension & Reason:**
- `.rst`: 63x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 16x Excluded (Explicitly Denied Extension: '.png')
- `.py`: 1x Excluded (Saturation: Line 94 exceeds 500 chars), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 3611 LOC)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.gif`: 5x Excluded (Explicitly Denied Extension: '.gif')
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2386 LOC)
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 2x Excluded (Unsupported Extension: '.ini')
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ai`: 1x Excluded (Explicitly Denied Extension: '.ai')
- `.bat`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 79.1 | 9.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 83.4 | 26.8 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.9 | 1.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.8 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 94.4 | 10.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 94.7 | 0.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 18.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 16.3 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.6 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 26.6 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 330 | 64 | 1 | `tests/test_text.py` |
| cleanup | 9 | 5 | 0 | `rich/progress.py` |
| guards | 1889 | 143 | 10 | `tests/test_text.py` |
| danger | 504 | 80 | 2 | `rich/console.py` |
| concurrency | 390 | 50 | 2 | `rich/segment.py` |
| connectivity | 1745 | 154 | 8 | `tests/test_console.py` |
| io | 237 | 44 | 1 | `tests/test_win32_console.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 9 | 2 | 0 | `tests/test_console.py` |
| time | 34 | 11 | 0 | `rich/_win32_console.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 17 | 10 | 0 | `tests/test_text.py` |
| events | 17 | 4 | 0 | `tests/test_logging.py` |
| tests | 862 | 60 | 3 | `tests/test_console.py` |
| docs | 921 | 122 | 5 | `rich/console.py` |
| debt | 559 | 115 | 3 | `tests/test_console.py` |
| mutation | 10893 | 193 | 59 | `rich/console.py` |
| dead_code | 660 | 60 | 2 | `tests/test_console.py` |
| credential | 4 | 3 | 0 | `tests/test_text.py` |
| threat | 1 | 1 | 0 | `tests/test_cells.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 171 | 33 | 0 | `tests/test_markup.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/test_win32_console.py` (Hits: 28)
- `tests/test_console.py` (Hits: 24)
- `rich/console.py` (Hits: 21)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **console.py** (`rich/console.py`) — 110 inbound connections
2. **text.py** (`rich/text.py`) — 55 inbound connections
3. **style.py** (`rich/style.py`) — 45 inbound connections
4. **__init__.py** (`rich/__init__.py`) — 37 inbound connections
5. **cells.py** (`rich/cells.py`) — 34 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **console.py** (`rich/console.py`) — 52 outbound dependencies
2. **progress.py** (`rich/progress.py`) — 32 outbound dependencies
3. **syntax.py** (`rich/syntax.py`) — 27 outbound dependencies
4. **live.py** (`rich/live.py`) — 26 outbound dependencies
5. **pretty.py** (`rich/pretty.py`) — 25 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` **(Stateful Encapsulated Methods)** (@ `rich/style.py`) -> Impact: **247.8** | LOC: 75
- `__init__` **(Many-Argument Workhorses)** (@ `rich/console.py`) -> Impact: **225.7** | LOC: 133
- `traverse` **(Many-Argument Workhorses)** (@ `rich/pretty.py`) -> Impact: **184.7** | LOC: 296
- `extract` **(Many-Argument Workhorses)** (@ `rich/traceback.py`) -> Impact: **158.6** | LOC: 192
- `_traverse` **(Many-Argument Workhorses)** (@ `rich/pretty.py`) -> Impact: **156.6** | LOC: 252
  * *Intent:* """Walk the object depth first."""
- `_render` **(Many-Argument Workhorses)** (@ `rich/table.py`) -> Impact: **152.2** | LOC: 181
- `export_svg` **(Many-Argument Workhorses)** (@ `rich/console.py`) -> Impact: **122.8** | LOC: 250
- `print` **(Many-Argument Workhorses)** (@ `rich/console.py`) -> Impact: **91.7** | LOC: 102
- `__rich_console__` **(Many-Argument Workhorses)** (@ `rich/columns.py`) -> Impact: **79.5** | LOC: 110
- `__rich_console__` **(Many-Argument Workhorses)** (@ `rich/markdown.py`) -> Impact: **77.9** | LOC: 118

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `rich` | 76 | 17147.84 | 33.74% | 2.45% |
| `tests` | 57 | 3861.76 | 6.51% | 0.0% |
| `examples` | 37 | 842.48 | 15.58% | 0.0% |
| `rich/_unicode_data` | 23 | 647.56 | 1.93% | 0.0% |
| `__monolith__` | 30 | 241.62 | 0.12% | 3.24% |
| `benchmarks/results/darrenburns-2022-mbp` | 177 | 190.68 | 0.0% | 0.0% |
| `benchmarks` | 3 | 154.7 | 6.02% | 33.29% |
| `.github/workflows` | 6 | 52.06 | 1.26% | 3.04% |
| `.github` | 3 | 26.72 | 0.0% | 0.0% |
| `benchmarks/results` | 1 | 25.3 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `benchmarks/benchmarks.py` -> **99.8703%** Exposure
- `Makefile` -> **97.0688%** Exposure
- `rich/highlighter.py` -> **84.1131%** Exposure
- `rich/align.py` -> **39.1172%** Exposure
- `rich/markdown.py` -> **32.4489%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `rich/_inspect.py` -> **100.0%** Exposure
- `rich/_log_render.py` -> **100.0%** Exposure
- `rich/_loop.py` -> **100.0%** Exposure
- `rich/_ratio.py` -> **100.0%** Exposure
- `rich/_unicode_data/__init__.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/test_console.py` -> **92** Orphaned Functions | **4** Duplicates
- `tests/test_text.py` -> **91** Orphaned Functions | **0** Duplicates
- `tests/test_pretty.py` -> **52** Orphaned Functions | **5** Duplicates
- `tests/test_progress.py` -> **37** Orphaned Functions | **0** Duplicates
- `tests/test_segment.py` -> **31** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `843` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `rich/console.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.457)
- **Top Global Matches:** file_cluster_5: 8.457, file_cluster_4: 9.861, file_cluster_12: 10.165
- **Magnitude:** 2260.42 | **LOC:** 2685 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **110** in-repo importer(s); it depends on **52**; blast radius 98.567; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.4%), Guard Balance (formerly Safety Score) (73.5%)
- **Documentation Coverage:** 46.0784% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 225.7)
  * `export_svg` **(Many-Argument Workhorses)** (Impact: 122.8)
  * `print` **(Many-Argument Workhorses)** (Impact: 91.7)
  * `render_str` **(Many-Argument Workhorses)** (Impact: 50.4)
  * `export_html` **(Many-Argument Workhorses)** (Impact: 50.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 259 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 868
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 322`, `structural_boundaries: 373`, `args: 116`, `func_start: 116`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 350`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 21`, `api: 96`, `concurrency: 4`, `import: 54`
* *Defense:* `safety: 41`, `doc: 118`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 98.567
  * `Choke Point (Betweenness):` 0.035823 | `Ripple Effect (Closeness):` 0.269273
  * `Imports (Out-Degree: 36):` ._emoji_replace, ._export_format, ._fileno, ._log_render, ._windows, .align, .color, .control...
  * `Imported By (In-Degree: 110):` (Excluded from Brief to save tokens)

### `rich/text.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.323)
- **Top Global Matches:** file_cluster_5: 8.323, file_cluster_0: 8.417, file_cluster_12: 8.997
- **Magnitude:** 1352.74 | **LOC:** 1364 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **55** in-repo importer(s); it depends on **21**; blast radius 30.977; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (88.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.7%)
- **Documentation Coverage:** 46.4% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wrap` **(Many-Argument Workhorses)** (Impact: 42.1)
  * `divide` **(Many-Argument Workhorses)** (Impact: 35.1)
    * *Intent:* """Divide text into a number of lines at given offsets. Args: offsets (Iterable[int]): Offsets used ...
  * `split` **(Many-Argument Workhorses)** (Impact: 33.5)
  * `highlight_regex` **(Many-Argument Workhorses)** (Impact: 33.3)
  * `with_indent_guides` **(Many-Argument Workhorses)** (Impact: 31.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 199 instances
* *State Mutation (weighted view):* 631
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 180`, `args: 65`, `func_start: 65`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 233`, `planned_debt: 2`
* *Architecture:* `api: 62`, `import: 22`
* *Defense:* `safety: 16`, `doc: 56`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 30.977
  * `Choke Point (Betweenness):` 0.005652 | `Ripple Effect (Closeness):` 0.200614
  * `Imports (Out-Degree: 15):` ._loop, ._pick, ._wrap, .align, .ansi, .cells, .console, .containers...
  * `Imported By (In-Degree: 55):` (Excluded from Brief to save tokens)

### `rich/progress.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.933)
- **Top Global Matches:** file_cluster_0: 6.933, file_cluster_5: 7.555, file_cluster_12: 8.898
- **Magnitude:** 1160.7 | **LOC:** 1717 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **32**; blast radius 4.372; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (78.5%), Guard Balance (formerly Safety Score) (69.6%)
- **Documentation Coverage:** 57.8947% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update` **(Many-Argument Workhorses)** (Impact: 47.3)
  * `open` **(Many-Argument Workhorses)** (Impact: 40.3)
  * `track` **(Many-Argument Workhorses)** (Impact: 27.7)
  * `reset` **(Many-Argument Workhorses)** (Impact: 22.9)
  * `open` **(Many-Argument Workhorses)** (Impact: 21.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 133 instances
* *State Mutation (weighted view):* 461
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 281`, `args: 97`, `func_start: 96`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 195`
* *Architecture:* `io: 8`, `api: 90`, `concurrency: 1`, `import: 34`
* *Defense:* `safety: 7`, `doc: 80`, `sync_locks: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.372
  * `Choke Point (Betweenness):` 0.0016 | `Ripple Effect (Closeness):` 0.018391
  * `Imports (Out-Degree: 14):` .console, .filesize, .get_console, .highlighter, .jupyter, .live, .panel, .progress_bar...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `rich/table.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.157)
- **Top Global Matches:** file_cluster_6: 8.157, file_cluster_4: 9.961, file_cluster_5: 16.69
- **Magnitude:** 1008.76 | **LOC:** 1016 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **28** in-repo importer(s); it depends on **19**; blast radius 11.888; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.8%), Connectivity (formerly Api Exposure) (51.9%)
- **Documentation Coverage:** 56.8627% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_render` **(Many-Argument Workhorses)** (Impact: 152.2)
  * `_calculate_column_widths` **(Many-Argument Workhorses)** (Impact: 65.2)
  * `_get_cells` **(Many-Argument Workhorses)** (Impact: 52.8)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 40.2)
  * `_collapse_widths` **(Stateful Encapsulated Methods)** (Impact: 37.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 124 instances
* *State Mutation (weighted view):* 423
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 101`, `args: 28`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 175`
* *Architecture:* `api: 24`, `import: 18`
* *Defense:* `safety: 2`, `doc: 43`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.888
  * `Choke Point (Betweenness):` 0.003626 | `Ripple Effect (Closeness):` 0.144281
  * `Imports (Out-Degree: 16):` ._loop, ._pick, ._ratio, ._timer, .align, .box, .console, .errors...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `rich/pretty.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.723)
- **Top Global Matches:** file_cluster_5: 8.723, file_cluster_12: 10.741, file_cluster_4: 11.094
- **Magnitude:** 976.12 | **LOC:** 1017 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **25**; blast radius 8.685; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.5%), Complexity Load (formerly Cognitive Load) (63.5%)
- **Documentation Coverage:** 56.25% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `traverse` **(Many-Argument Workhorses)** (Impact: 184.7)
  * `_traverse` **(Many-Argument Workhorses)** (Impact: 156.6)
    * *Intent:* """Walk the object depth first."""
  * `install` **(Many-Argument Workhorses)** (Impact: 28.0)
  * `_ipy_display_hook` **(Many-Argument Workhorses)** (Impact: 24.4)
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 19.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 104 instances
* *State Mutation (weighted view):* 344
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 155`, `args: 44`, `func_start: 34`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 136`
* *Architecture:* `io: 3`, `api: 25`, `import: 31`
* *Defense:* `safety: 25`, `doc: 24`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.685
  * `Choke Point (Betweenness):` 0.001595 | `Ripple Effect (Closeness):` 0.157356
  * `Imports (Out-Degree: 11):` ._loop, ._pick, .abc, .cells, .console, .get_console, .highlighter, .jupyter...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `rich/style.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.254)
- **Top Global Matches:** file_cluster_5: 8.254, file_cluster_12: 10.297, file_cluster_4: 10.667
- **Magnitude:** 925.36 | **LOC:** 793 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **45** in-repo importer(s); it depends on **10**; blast radius 28.067; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.0%), Connectivity (formerly Api Exposure) (66.1%)
- **Documentation Coverage:** 29.2683% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 247.8)
  * `__str__` **(Compute Cores)** (Impact: 70.1)
    * *Intent:* """Re-generate style definition from attributes."""
  * `_make_ansi_codes` **(Stateful Encapsulated Methods)** (Impact: 28.1)
    * *Intent:* """Generate ANSI codes for this style. Args: color_system (ColorSystem): Color system. Returns: str:...
  * `get_html_style` **(Compute Cores)** (Impact: 24.3)
    * *Intent:* """Get a CSS style rule."""
  * `parse` **(Defensive Guards)** (Impact: 24.0)
    * *Intent:* """Parse a style definition. Args: style_definition (str): A string containing a style. Raises: erro...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 329
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 116`, `args: 41`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 149`
* *Architecture:* `io: 1`, `api: 36`, `import: 10`
* *Defense:* `safety: 9`, `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 28.067
  * `Choke Point (Betweenness):` 0.001322 | `Ripple Effect (Closeness):` 0.195171
  * `Imports (Out-Degree: 4):` .color, .errors, .repr, .terminal_theme, functools, operator, pickle, random...
  * `Imported By (In-Degree: 45):` (Excluded from Brief to save tokens)

### `rich/traceback.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.874)
- **Top Global Matches:** file_cluster_4: 9.874, file_cluster_6: 11.605, file_cluster_5: 12.969
- **Magnitude:** 756.4 | **LOC:** 925 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **25**; blast radius 6.852; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.1%), Complexity Load (formerly Cognitive Load) (56.3%)
- **Documentation Coverage:** 90.2439% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `extract` **(Many-Argument Workhorses)** (Impact: 158.6)
  * `install` **(Many-Argument Workhorses)** (Impact: 60.4)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 58.0)
  * `_render_stack` **(Many-Argument Workhorses)** (Impact: 44.5)
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 31.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *State Mutation (weighted view):* 244
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 112`, `args: 21`, `func_start: 20`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 108`
* *Architecture:* `io: 15`, `api: 21`, `import: 28`
* *Defense:* `safety: 12`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.852
  * `Choke Point (Betweenness):` 0.001568 | `Ripple Effect (Closeness):` 0.153518
  * `Imports (Out-Degree: 13):` ._loop, .columns, .console, .constrain, .highlighter, .panel, .pretty, .scope...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `rich/syntax.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.633)
- **Top Global Matches:** file_cluster_4: 7.633, file_cluster_0: 10.22, file_cluster_12: 10.638
- **Magnitude:** 680.42 | **LOC:** 986 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **27**; blast radius 5.065; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.1%), Complexity Load (formerly Cognitive Load) (42.4%)
- **Documentation Coverage:** 44.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_syntax` **(Many-Argument Workhorses)** (Impact: 76.8)
  * `highlight` **(Many-Argument Workhorses)** (Impact: 46.2)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 17.9)
  * `_apply_stylized_ranges` **(Stateful Encapsulated Methods)** (Impact: 17.2)
    * *Intent:* """ Apply stylized ranges to a text instance, using the given code to determine the right portion to...
  * `guess_lexer` **(Defensive Guards)** (Impact: 16.0)
    * *Intent:* """Guess the alias of the Pygments lexer to use based on a path and an optional string of code. If c...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 100 instances
* *State Mutation (weighted view):* 329
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 133`, `args: 31`, `func_start: 31`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 129`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `api: 24`, `import: 28`
* *Defense:* `safety: 20`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.065
  * `Choke Point (Betweenness):` 0.00042 | `Ripple Effect (Closeness):` 0.127802
  * `Imports (Out-Degree: 11):` ._loop, .cells, .color, .console, .jupyter, .measure, .segment, .style...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `rich/segment.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.203)
- **Top Global Matches:** file_cluster_5: 8.203, file_cluster_0: 8.627, file_cluster_12: 9.086
- **Magnitude:** 632.1 | **LOC:** 784 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **30** in-repo importer(s); it depends on **13**; blast radius 20.352; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (81.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.1%)
- **Documentation Coverage:** 49.0196% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `divide` **(Many-Argument Workhorses)** (Impact: 33.4)
  * `adjust_line_length` **(Many-Argument Workhorses)** (Impact: 29.1)
  * `split_and_crop_lines` **(Many-Argument Workhorses)** (Impact: 28.7)
  * `apply_style` **(Many-Argument Workhorses)** (Impact: 26.5)
  * `_split_cells` **(Many-Argument Workhorses)** (Impact: 22.3)
    * *Intent:* """Split a segment in to two at a given cell position. Note that splitting a double-width character,...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 81 instances
* *State Mutation (weighted view):* 266
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 95`, `args: 28`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 104`
* *Architecture:* `api: 27`, `import: 13`
* *Defense:* `safety: 3`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 20.352
  * `Choke Point (Betweenness):` 0.001876 | `Ripple Effect (Closeness):` 0.176063
  * `Imports (Out-Degree: 6):` .cells, .console, .repr, .style, enum, functools, itertools, logging...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `rich/markdown.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.66)
- **Top Global Matches:** file_cluster_0: 6.66, file_cluster_12: 9.197, file_cluster_5: 9.332
- **Magnitude:** 625.42 | **LOC:** 794 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **22**; blast radius 1.632; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (72.7%), Guard Balance (formerly Safety Score) (69.3%)
- **Documentation Coverage:** 76.1364% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 77.9)
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 15.2)
  * `__rich_console__` **(Compute Cores)** (Impact: 14.7)
  * `create` **(Defensive Guards)** (Impact: 12.8)
  * `_flatten_tokens` **(Stateful Encapsulated Methods)** (Impact: 10.8)
    * *Intent:* """Flattens the token stream."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 66 instances
* *State Mutation (weighted view):* 265
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 161`, `args: 57`, `func_start: 57`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 133`, `duplicate_logic: 4`
* *Architecture:* `io: 2`, `api: 51`, `import: 23`
* *Defense:* `safety: 15`, `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.632
  * `Choke Point (Betweenness):` 0.000886 | `Ripple Effect (Closeness):` 0.082956
  * `Imports (Out-Degree: 12):` ._loop, ._stack, .box, .console, .containers, .jupyter, .rule, .segment...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tests/test_console.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.753)
- **Top Global Matches:** file_cluster_5: 7.753, file_cluster_12: 9.242, file_cluster_0: 9.429
- **Magnitude:** 564.58 | **LOC:** 1130 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.943; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (45.1%), Complexity Load (formerly Cognitive Load) (32.7%), Connectivity (formerly Api Exposure) (13.3%)
- **Documentation Coverage:** 94.6188% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_size_can_fall_back_to_std_descriptors` **(Generic / Templated Code)** (Impact: 7.0)
  * `test_console_options_update` **(Defensive Guards)** (Impact: 6.1)
  * `test_brokenpipeerror` **(Defensive Guards)** (Impact: 4.8)
    * *Intent:* """Test BrokenPipe works as expected."""
  * `test_tty_compatible` **(Defensive Guards)** (Impact: 4.2)
    * *Intent:* """Check TTY_COMPATIBLE environment var."""
  * `get_terminal_size_mock_impl` **(Generic / Templated Code)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 23 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 351`, `args: 112`, `func_start: 110`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 3`, `state_mutation: 206`, `duplicate_logic: 4`, `unreferenced_by_name: 92`
* *Architecture:* `io: 24`, `api: 110`, `import: 24`
* *Defense:* `safety: 137`, `doc: 8`, `test: 117`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.943
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` datetime, io, os, pytest, rich, rich._null_file, rich.color, rich.console...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_text.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 8.709)
- **Top Global Matches:** file_cluster_11: 8.709, file_cluster_15: 9.185, file_cluster_12: 9.593
- **Magnitude:** 453.32 | **LOC:** 1130 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.943; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (29.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.9%), Complexity Load (formerly Cognitive Load) (20.0%), Connectivity (formerly Api Exposure) (12.9%)
- **Documentation Coverage:** 86.9565% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_highlight_regex` **(Defensive Guards)** (Impact: 4.3)
    * *Intent:* # As a string text = Text("peek-a-boo") count = text.highlight_regex(r"NEVER_MATCH", "red") assert c...
  * `test_divide` **(Defensive Guards)** (Impact: 3.1)
  * `test_indentation_guides` **(I/O & Config Routines)** (Impact: 3.0)
  * `test_highlight_regex_callable` **(Defensive Guards)** (Impact: 2.7)
  * `test_tabs_to_spaces_spans` **(Defensive Guards)** (Impact: 2.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 206
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 354`, `args: 92`, `func_start: 92`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 202`, `unreferenced_by_name: 91`
* *Architecture:* `api: 92`, `import: 8`
* *Defense:* `safety: 235`, `doc: 16`, `test: 100`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.943
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` io, pytest, re, rich.console, rich.measure, rich.style, rich.text, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_pretty.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.411)
- **Top Global Matches:** file_cluster_5: 8.411, file_cluster_12: 9.47, file_cluster_0: 10.072
- **Magnitude:** 396.72 | **LOC:** 760 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.943; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.4%), Complexity Load (formerly Cognitive Load) (30.3%), Connectivity (formerly Api Exposure) (12.5%)
- **Documentation Coverage:** 88.7218% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_attrs_broken_310` **(Annotated & Test Methods)** (Impact: 3.7)
  * `test_pretty_namedtuple` **(I/O & Config Routines)** (Impact: 2.2)
  * `test_reference_cycle_custom_repr` **(Defensive Guards)** (Impact: 2.2)
  * `test_deque` **(Defensive Guards)** (Impact: 2.2)
  * `test_ipy_display_hook__special_repr_raises_exception` **(Encapsulated Accessors)** (Impact: 2.1)
    * *Intent:* """ When an IPython special repr method raises an exception, we treat it as if it doesn't exist and ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 179
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 235`, `args: 77`, `func_start: 77`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 157`, `duplicate_logic: 5`, `unreferenced_by_name: 52`
* *Architecture:* `io: 21`, `api: 85`, `import: 14`
* *Defense:* `safety: 80`, `doc: 11`, `test: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.943
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` array, attr, collections, dataclasses, io, pytest, rich.console, rich.measure...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rich/layout.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.757)
- **Top Global Matches:** file_cluster_0: 6.757, file_cluster_5: 6.897, file_cluster_12: 8.774
- **Magnitude:** 341.52 | **LOC:** 443 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **19**; blast radius 1.192; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.4%), Connectivity (formerly Api Exposure) (57.3%)
- **Documentation Coverage:** 47.0588% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__rich_console__` **(Stateful Encapsulated Methods)** (Impact: 15.1)
  * `split` **(Defensive Guards)** (Impact: 13.2)
  * `render` **(Many-Argument Workhorses)** (Impact: 11.4)
    * *Intent:* """Render the sub_layouts. Args: console (Console): Console instance. options (ConsoleOptions): Cons...
  * `_make_region_map` **(Stateful Encapsulated Methods)** (Impact: 11.0)
    * *Intent:* """Create a dict that maps layout on to Region."""
  * `get` **(Generic / Templated Code)** (Impact: 9.5)
    * *Intent:* """Get a named layout, or None if it doesn't exist. Args: name (str): Name of layout. Returns: Optio...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 95`, `args: 28`, `func_start: 28`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 65`
* *Architecture:* `api: 30`, `concurrency: 1`, `import: 20`
* *Defense:* `safety: 5`, `doc: 24`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.192
  * `Choke Point (Betweenness):` 9e-05 | `Ripple Effect (Closeness):` 0.004598
  * `Imports (Out-Degree: 13):` ._ratio, .align, .console, .highlighter, .panel, .pretty, .region, .repr...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `rich/color.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.474)
- **Top Global Matches:** file_cluster_6: 8.474, file_cluster_4: 11.805, file_cluster_8: 16.288
- **Magnitude:** 323.56 | **LOC:** 622 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **14**; blast radius 14.705; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (72.9%), Guard Balance (formerly Safety Score) (59.6%)
- **Documentation Coverage:** 29.4118% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `downgrade` **(Defensive Guards)** (Impact: 42.6)
    * *Intent:* """Downgrade a color system to a system with fewer colors."""
  * `get_ansi_codes` **(Defensive Guards)** (Impact: 35.9)
    * *Intent:* """Get the ANSI escape codes for this color."""
  * `parse` **(Type Conversions)** (Impact: 30.2)
    * *Intent:* """Parse a color definition."""
  * `get_truecolor` **(Defensive Guards)** (Impact: 19.5)
  * `from_ansi` **(Generic / Templated Code)** (Impact: 5.9)
    * *Intent:* """Create a Color number from it's 8-bit ansi number. Args: number (int): A number between 0-255 inc...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 124`, `args: 18`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `state_mutation: 54`
* *Architecture:* `io: 1`, `api: 20`, `import: 17`
* *Defense:* `safety: 15`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.705
  * `Choke Point (Betweenness):` 0.002577 | `Ripple Effect (Closeness):` 0.16402
  * `Imports (Out-Degree: 8):` ._palettes, .color_triplet, .console, .repr, .style, .table, .terminal_theme, .text...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `tests/test_progress.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.794)
- **Top Global Matches:** file_cluster_5: 7.794, file_cluster_12: 7.944, file_cluster_7: 9.989
- **Magnitude:** 320.44 | **LOC:** 691 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.943; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.1%), Complexity Load (formerly Cognitive Load) (32.4%), Connectivity (formerly Api Exposure) (11.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (8.2%)
- **Documentation Coverage:** 97.7011% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_columns` **(I/O & Config Routines)** (Impact: 4.2)
  * `test_using_default_columns` **(Defensive Guards)** (Impact: 4.2)
    * *Intent:* # can only check types, as the instances do not '==' each other expected_default_types = [ TextColum...
  * `test_progress_max_refresh` **(I/O & Config Routines)** (Impact: 3.9)
    * *Intent:* """Test max_refresh argument."""
  * `test_track` **(I/O & Config Routines)** (Impact: 3.4)
  * `test_progress_track` **(I/O & Config Routines)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 180
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 189`, `args: 57`, `func_start: 44`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 142`, `unreferenced_by_name: 37`
* *Architecture:* `io: 12`, `api: 44`, `import: 13`
* *Defense:* `safety: 89`, `doc: 2`, `test: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.943
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` .render, io, os, pytest, rich.console, rich.highlighter, rich.progress, rich.progress_bar...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rich/align.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.949)
- **Top Global Matches:** file_cluster_6: 8.949, file_cluster_4: 10.405, file_cluster_0: 15.735
- **Magnitude:** 300.46 | **LOC:** 321 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **11**; blast radius 8.75; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.1%), Guard Balance (formerly Safety Score) (72.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 70.5)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 25.3)
  * `generate_segments` **(I/O & Config Routines)** (Impact: 17.9)
  * `__rich_console__` **(Compute Cores)** (Impact: 17.3)
  * `blank_lines` **(Generic / Templated Code)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 53`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `state_mutation: 52`, `duplicate_logic: 2`
* *Architecture:* `api: 8`, `import: 11`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.75
  * `Choke Point (Betweenness):` 0.000886 | `Ripple Effect (Closeness):` 0.162958
  * `Imports (Out-Degree: 8):` .console, .constrain, .jupyter, .measure, .segment, .style, itertools, rich.console...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `rich/live.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.273)
- **Top Global Matches:** file_cluster_5: 9.273, file_cluster_4: 9.963, file_cluster_12: 10.672
- **Magnitude:** 296.62 | **LOC:** 405 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **26**; blast radius 5.583; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.1%), Complexity Load (formerly Cognitive Load) (45.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `stop` **(Stateful Encapsulated Methods)** (Impact: 24.5)
    * *Intent:* """Stop live rendering display."""
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 19.3)
  * `refresh` **(Defensive Guards)** (Impact: 17.2)
    * *Intent:* """Update the display of the Live Render."""
  * `start` **(Stateful Encapsulated Methods)** (Impact: 12.0)
    * *Intent:* """Start live rendering display. Args: refresh (bool, optional): Also refresh. Defaults to False. ""...
  * `process_renderables` **(Generic / Templated Code)** (Impact: 11.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 97`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 54`
* *Architecture:* `io: 10`, `api: 13`, `concurrency: 1`, `import: 28`
* *Defense:* `safety: 10`, `doc: 12`, `sync_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.583
  * `Choke Point (Betweenness):` 0.00248 | `Ripple Effect (Closeness):` 0.158346
  * `Imports (Out-Degree: 13):` .align, .console, .control, .file_proxy, .get_console, .jupyter, .live, .live_render...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `rich/_inspect.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 10.406)
- **Top Global Matches:** file_cluster_5: 10.406, file_cluster_4: 11.747, file_cluster_12: 12.56
- **Magnitude:** 284.14 | **LOC:** 273 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 5.796; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.2%), Concurrency Surface (formerly Concurrency) (55.3%), Complexity Load (formerly Cognitive Load) (49.8%)
- **Documentation Coverage:** 21.6216% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_render` **(Compute Cores)** (Impact: 51.3)
    * *Intent:* """Render object."""
  * `__init__` **(Many-Argument Workhorses)** (Impact: 18.6)
  * `_get_signature` **(Stateful Encapsulated Methods)** (Impact: 18.1)
    * *Intent:* """Get a signature for a callable."""
  * `_make_title` **(Stateful Encapsulated Methods)** (Impact: 9.1)
    * *Intent:* """Make a default title."""
  * `_get_formatted_doc` **(Stateful Encapsulated Methods)** (Impact: 6.2)
    * *Intent:* """ Extract the docstring of an object, process it and returns it. The processing consists in cleani...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 47 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 58`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 50`
* *Architecture:* `api: 8`, `concurrency: 1`, `import: 11`
* *Defense:* `safety: 8`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.796
  * `Choke Point (Betweenness):` 0.000602 | `Ripple Effect (Closeness):` 0.103823
  * `Imports (Out-Degree: 8):` .console, .control, .highlighter, .jupyter, .panel, .pretty, .table, .text...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `rich/cells.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.256)
- **Top Global Matches:** file_cluster_9: 8.256, file_cluster_0: 10.163, file_cluster_12: 10.626
- **Magnitude:** 280.96 | **LOC:** 353 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **34** in-repo importer(s); it depends on **5**; blast radius 47.093; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (80.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 31.25% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `split_graphemes` **(Many-Argument Workhorses)** (Impact: 29.6)
  * `_cell_len` **(Stateful Encapsulated Methods)** (Impact: 21.4)
    * *Intent:* """Get the cell length of a string (length as it appears in the terminal). Args: text: String to mea...
  * `_split_text` **(Stateful Encapsulated Methods)** (Impact: 20.1)
  * `get_character_cell_size` **(Compute Cores)** (Impact: 17.2)
    * *Intent:* """Get the cell size of a character. Args: character (str): A single character. unicode_version: Uni...
  * `chop_cells` **(Generic / Templated Code)** (Impact: 13.3)
    * *Intent:* """Split text into lines such that each line fits within the available (cell) width. Args: text: The...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 143
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 49`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 51`
* *Architecture:* `api: 8`, `import: 5`
* *Defense:* `doc: 10`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 47.093
  * `Choke Point (Betweenness):` 0.001812 | `Ripple Effect (Closeness):` 0.204769
  * `Imports (Out-Degree: 1):` __future__, functools, operator, rich._unicode_data, typing
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `rich/_win32_console.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.446)
- **Top Global Matches:** file_cluster_5: 7.446, file_cluster_12: 8.328, file_cluster_0: 8.812
- **Magnitude:** 269.88 | **LOC:** 662 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **7**; blast radius 6.602; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (66.9%), Connectivity (formerly Api Exposure) (48.7%), Complexity Load (formerly Cognitive Load) (41.4%)
- **Documentation Coverage:** 28.0702% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write_styled` **(Many-Argument Workhorses)** (Impact: 25.9)
    * *Intent:* """Write styled text to the terminal. Args: text (str): The text to write style (Style): The style o...
  * `move_cursor_to` **(Generic / Templated Code)** (Impact: 5.6)
    * *Intent:* """Set the position of the cursor Args: new_position (WindowsCoordinates): The WindowsCoordinates re...
  * `move_cursor_forward` **(Generic / Templated Code)** (Impact: 4.8)
    * *Intent:* """Move the cursor forward a single cell. Wrap to the next line if required."""
  * `move_cursor_backward` **(Generic / Templated Code)** (Impact: 4.8)
    * *Intent:* """Move the cursor backward a single cell. Wrap to the previous line if required."""
  * `GetConsoleMode` **(Type Conversions)** (Impact: 3.8)
    * *Intent:* """Retrieves the current input mode of a console's input buffer or the current output mode of a cons...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 68`, `args: 29`, `func_start: 29`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 90`
* *Architecture:* `io: 2`, `api: 33`, `import: 9`
* *Defense:* `safety: 3`, `doc: 31`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.602
  * `Choke Point (Betweenness):` 0.000589 | `Ripple Effect (Closeness):` 0.15446
  * `Imports (Out-Degree: 3):` ctypes, rich.color, rich.console, rich.style, sys, time, typing
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `rich/tree.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.74)
- **Top Global Matches:** file_cluster_6: 7.74, file_cluster_8: 12.438, file_cluster_4: 14.368
- **Magnitude:** 265.24 | **LOC:** 258 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **13**; blast radius 1.443; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.0%), Complexity Load (formerly Cognitive Load) (52.4%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 72.5)
  * `add` **(Many-Argument Workhorses)** (Impact: 20.0)
  * `make_guide` **(Compute Cores)** (Impact: 16.0)
    * *Intent:* """Make a Segment for a level of the guide lines."""
  * `__rich_measure__` **(Defensive Guards)** (Impact: 9.3)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 39`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 62`
* *Architecture:* `api: 6`, `import: 13`
* *Defense:* `safety: 4`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.443
  * `Choke Point (Betweenness):` 0.000229 | `Ripple Effect (Closeness):` 0.00821
  * `Imports (Out-Degree: 11):` ._loop, .console, .jupyter, .measure, .segment, .style, .styled, rich.console...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `rich/progress_bar.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.205)
- **Top Global Matches:** file_cluster_4: 9.205, file_cluster_6: 9.341, file_cluster_0: 14.5
- **Magnitude:** 255.64 | **LOC:** 224 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 1.342; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (53.8%)
- **Documentation Coverage:** 71.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 56.1)
  * `_get_pulse_segments` **(Many-Argument Workhorses)** (Impact: 34.0)
  * `_render_pulse` **(Stateful Encapsulated Methods)** (Impact: 8.2)
  * `update` **(Generic / Templated Code)** (Impact: 6.5)
    * *Intent:* """Update progress with new values. Args: completed (float): Number of steps completed. total (float...
  * `__rich_measure__` **(Generic / Templated Code)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 40`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 51`
* *Architecture:* `api: 7`, `import: 12`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.342
  * `Choke Point (Betweenness):` 7.2e-05 | `Ripple Effect (Closeness):` 0.011638
  * `Imports (Out-Degree: 7):` .color, .color_triplet, .console, .jupyter, .measure, .segment, .style, functools...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `rich/columns.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.171)
- **Top Global Matches:** file_cluster_8: 9.171, file_cluster_6: 10.958, file_cluster_4: 18.769
- **Magnitude:** 250.9 | **LOC:** 188 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **13**; blast radius 3.188; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (64.0%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 79.5)
  * `iter_renderables` **(Compute Cores)** (Impact: 18.6)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 7.7)
  * `add_renderable` **(Generic / Templated Code)** (Impact: 2.1)
    * *Intent:* """Add a renderable to the columns. Args: renderable (RenderableType): Any renderable object. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 35`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 49`
* *Architecture:* `io: 1`, `api: 5`, `import: 13`
* *Defense:* `safety: 1`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.188
  * `Choke Point (Betweenness):` 0.000387 | `Ripple Effect (Closeness):` 0.11341
  * `Imports (Out-Degree: 8):` .align, .console, .constrain, .jupyter, .measure, .padding, .table, .text...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `rich/panel.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.91)
- **Top Global Matches:** file_cluster_6: 7.91, file_cluster_4: 9.586, file_cluster_0: 16.283
- **Magnitude:** 237.0 | **LOC:** 318 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); it depends on **11**; blast radius 8.477; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.7%), Complexity Load (formerly Cognitive Load) (61.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__rich_console__` **(Many-Argument Workhorses)** (Impact: 60.8)
  * `align_text` **(Many-Argument Workhorses)** (Impact: 17.0)
  * `__rich_measure__` **(Many-Argument Workhorses)** (Impact: 11.1)
  * `_title` **(Stateful Encapsulated Methods)** (Impact: 6.4)
  * `_subtitle` **(Stateful Encapsulated Methods)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 49`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 51`
* *Architecture:* `api: 6`, `import: 14`
* *Defense:* `safety: 2`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.477
  * `Choke Point (Betweenness):` 0.001349 | `Ripple Effect (Closeness):` 0.134277
  * `Imports (Out-Degree: 10):` .align, .box, .cells, .console, .jupyter, .measure, .padding, .segment...
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `rich/box.py` (PYTHON) | Magnitude: 160.68 | Delta: **0.112** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 307, core_var_decl: 57, state_mutation: 38, structural_boundaries: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/test_color_triplet.py` (PYTHON) | Magnitude: 6.5 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 11, safety: 6, indent_spaces: 6, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/test_inspect.py` (PYTHON) | Magnitude: 169.38 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 321, structural_boundaries: 124, core_var_decl: 105, design_snake_case: 104

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tests/test_palette.py` (PYTHON) | Magnitude: 3.32 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 7, safety: 3, indent_spaces: 3, import: 2
- `tests/test_filesize.py` (PYTHON) | Magnitude: 6.12 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 16, indent_spaces: 13, safety: 12, core_var_decl: 6
- `tests/test_box.py` (PYTHON) | Magnitude: 29.34 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 39, core_var_decl: 26, design_snake_case: 26
- `tests/test_constrain.py` (PYTHON) | Magnitude: 4.62 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 7, import: 3, core_var_decl: 3
- `examples/listdir.py` (PYTHON) | Magnitude: 23.96 | Delta: **0.15** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 10, branch: 6, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/test_highlighter.py` (PYTHON) | Magnitude: 46.4 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 421, structural_boundaries: 22, state_mutation: 19, core_var_decl: 19
- `tests/test_jupyter.py` (PYTHON) | Magnitude: 14.64 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 12, core_var_decl: 9, design_snake_case: 9
- `tests/test_stack.py` (PYTHON) | Magnitude: 4.56 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 6, safety: 3, state_mutation: 2
- `tests/test_pick.py` (PYTHON) | Magnitude: 2.84 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 13, safety: 10, indent_spaces: 10, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `rich/progress_bar.py` (PYTHON) | Magnitude: 255.64 | Delta: **0.136** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 148, state_mutation: 51, core_var_decl: 49, branch: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `rich/_windows.py` (PYTHON) | Magnitude: 47.16 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 16, core_var_decl: 16, design_snake_case: 16
- `rich/text.py` (PYTHON) | Magnitude: 1352.74 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 865, core_var_decl: 264, design_snake_case: 244, state_mutation: 233
- `tests/test_progress.py` (PYTHON) | Magnitude: 320.44 | Delta: **0.15** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 519, core_var_decl: 232, design_snake_case: 232, structural_boundaries: 189

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `rich/screen.py` (PYTHON) | Magnitude: 44.38 | Delta: **0.139** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 16, state_mutation: 9, branch: 8

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `rich/console.py` -> **Will McGugan** (100.0% isolated ownership) | Magnitude: 2260.42
- `rich/text.py` -> **Will McGugan** (100.0% isolated ownership) | Magnitude: 1352.74
- `rich/table.py` -> **Will McGugan** (100.0% isolated ownership) | Magnitude: 1008.76
- `rich/pretty.py` -> **Joel Ostblom** (100.0% isolated ownership) | Magnitude: 976.12
- `rich/traceback.py` -> **daniel.jaekel** (100.0% isolated ownership) | Magnitude: 756.4

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `rich/console.py` -> **Severity: 3.582** (Bridge: 0.0358 * Flux: 100.0%)
- `rich/text.py` -> **Severity: 0.565** (Bridge: 0.0057 * Flux: 100.0%)
- `rich/__init__.py` -> **Severity: 0.416** (Bridge: 0.0042 * Flux: 99.9982%)
- `rich/table.py` -> **Severity: 0.363** (Bridge: 0.0036 * Flux: 100.0%)
- `rich/color.py` -> **Severity: 0.258** (Bridge: 0.0026 * Flux: 99.9791%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `rich/console.py` -> **Severity: 19.786** (Embedded: 0.2693 * Error Risk: 73.4778%)
- `rich/cells.py` -> **Severity: 16.47** (Embedded: 0.2048 * Error Risk: 80.4311%)
- `rich/text.py` -> **Severity: 15.99** (Embedded: 0.2006 * Error Risk: 79.7054%)
- `rich/style.py` -> **Severity: 15.032** (Embedded: 0.1952 * Error Risk: 77.0215%)
- `rich/jupyter.py` -> **Severity: 14.101** (Embedded: 0.169 * Error Risk: 83.4488%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `rich/console.py` -> **Severity: 4541.81** (Blast Radius: 98.567 * Doc Risk: 46.0784%)
- `rich/cells.py` -> **Severity: 1471.656** (Blast Radius: 47.093 * Doc Risk: 31.25%)
- `rich/text.py` -> **Severity: 1437.333** (Blast Radius: 30.977 * Doc Risk: 46.4%)
- `rich/terminal_theme.py` -> **Severity: 1360.9** (Blast Radius: 13.609 * Doc Risk: 100.0%)
- `rich/__init__.py` -> **Severity: 1079.25** (Blast Radius: 21.585 * Doc Risk: 50.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 522 literal sites + 11 sites through wrappers = 533

- `render` (function, debug_prints, primitive): 8 call sites in 1 files -- `tests/test_markdown.py`
- `bar` (function, debug_prints, primitive): 1 call sites in 1 files -- `rich/traceback.py`
- `render` (function, debug_prints, primitive): 1 call sites in 1 files -- `tests/test_card.py`
- `render` (function, debug_prints, primitive): 1 call sites in 1 files -- `tests/test_panel.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 5867 call pairs -- scoped 57.0%, unique 0.0%, ambiguous 7.3%, external 35.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 5867 | 57.0% | 0.0% | 7.3% | 35.7% |

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
