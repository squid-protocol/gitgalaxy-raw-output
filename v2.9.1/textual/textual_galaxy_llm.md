# ARCHITECTURAL_BRIEF: textual
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/Textualize/textual.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 708 analyzed artifact(s), 77975 LOC.
- **Load-bearing artifact:** `src/textual/app.py` -- 376 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/textual/app.py` -- pulls in 89 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/textual/widget.py` at magnitude 3419.6 (structural weight, not risk).
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
| Total Artifacts | 2116 |
| Analyzed Artifacts (Scanned) | 708 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1408 |
| Total LOC | 77975 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 33.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4357 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3594 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 13.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1317 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 56 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 669 | 77440 | 94.5% |
| MARKDOWN | 24 | 0 | 3.4% |
| SCHEME | 7 | 243 | 1.0% |
| YAML | 3 | 32 | 0.4% |
| XML | 2 | 0 | 0.3% |
| MAKEFILE | 1 | 83 | 0.1% |
| PLAINTEXT | 1 | 0 | 0.1% |
| TYPESCRIPT | 1 | 177 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `1.578`
> **Composition Archetype:** `Hub-Coupled App` (z +1.58; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 49%, Large Core Modules (2) 17%, Data / Markup / Trivial 10%, Declarative / Non-Code 5%, Parameter Forwarders Files 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 683 | 96.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 25 | 3.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1408*

**Composition by Extension & Reason:**
- `.svg`: 528x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 314x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Packed Payload Guard (Impossible Density: 3.13 hits/line), 1x Excluded (Machine-Generated Source Code Signature: 1270 LOC)
- `.md`: 297x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 3621 LOC)
- `.tcss`: 146x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 14x Excluded (Unsupported Extension: '.tcss')
- `.png`: 35x Excluded (Explicitly Denied Extension: '.png')
- `.gif`: 26x Excluded (Explicitly Denied Extension: '.gif')
- `.yml`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 116, Signals: 0), 1x Zero-Density Threshold (LOC: 250, Signals: 0)
- `.scm`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 76, Signals: 0), 1x Zero-Density Threshold (LOC: 99, Signals: 0)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mov`: 3x Excluded (Explicitly Denied Extension: '.mov')
- `.lock`: 2x Excluded (Unsupported Extension: '.lock')
- `.monopic`: 2x Excluded (Unsupported Extension: '.monopic')
- `.toml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpeg`: 1x Excluded (Explicitly Denied Extension: '.jpeg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 17.4 | 6.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.7 | 57.8 | 64.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 18.6 | 9.8 | 5.6 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 34.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 29.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 16.7 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 10.2 | 0.7 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 59.7 | 66.7 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 923 | 209 | 3 | `src/textual/css/_styles_builder.py` |
| cleanup | 18 | 8 | 0 | `Makefile` |
| guards | 7634 | 423 | 26 | `tests/snapshot_tests/test_snapshots.py` |
| danger | 1404 | 263 | 5 | `src/textual/app.py` |
| concurrency | 6251 | 472 | 20 | `tests/snapshot_tests/test_snapshots.py` |
| connectivity | 8208 | 645 | 22 | `tests/snapshot_tests/test_snapshots.py` |
| io | 130 | 56 | 0 | `src/textual/app.py` |
| crypto | 1 | 1 | 0 | `src/textual/_doc.py` |
| ipc | 2 | 1 | 0 | `tests/test_pipe.py` |
| time | 4 | 2 | 0 | `examples/merlin.py` |
| serialization | 1 | 1 | 0 | `src/textual/actions.py` |
| regex | 34 | 24 | 0 | `src/textual/_xterm_parser.py` |
| events | 232 | 40 | 0 | `src/textual/message_pump.py` |
| tests | 2699 | 249 | 10 | `tests/snapshot_tests/test_snapshots.py` |
| docs | 6074 | 533 | 17 | `src/textual/app.py` |
| debt | 604 | 130 | 2 | `tests/test_tabbed_content.py` |
| mutation | 29434 | 639 | 95 | `src/textual/widget.py` |
| dead_code | 2682 | 420 | 9 | `tests/snapshot_tests/test_snapshots.py` |
| credential | 0 | 0 | 0 | - |
| threat | 844 | 132 | 2 | `src/textual/widget.py` |
| ml_ai | 14 | 3 | 0 | `tools/gen_easings_tests.ts` |
| ui | 175 | 65 | 0 | `tests/css/test_help_text.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/textual/app.py` (Hits: 16)
- `src/textual/drivers/linux_driver.py` (Hits: 9)
- `src/textual/_import_app.py` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **app.py** (`src/textual/app.py`) — 376 inbound connections
2. **widgets.py** (`src/textual/demo/widgets.py`) — 318 inbound connections
3. **containers.py** (`src/textual/containers.py`) — 102 inbound connections
4. **widget.py** (`src/textual/widget.py`) — 99 inbound connections
5. **geometry.py** (`src/textual/geometry.py`) — 80 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **app.py** (`src/textual/app.py`) — 89 outbound dependencies
2. **widget.py** (`src/textual/widget.py`) — 57 outbound dependencies
3. **__init__.py** (`src/textual/widgets/__init__.py`) — 45 outbound dependencies
4. **dom.py** (`src/textual/dom.py`) — 44 outbound dependencies
5. **screen.py** (`src/textual/screen.py`) — 42 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `render_line` **(Many-Argument Workhorses)** (@ `src/textual/_styles_cache.py`) -> Impact: **270.8** | LOC: 252
- `arrange` **(Many-Argument Workhorses)** (@ `src/textual/layouts/grid.py`) -> Impact: **153.6** | LOC: 328
- `css_lines` **(Compute Cores)** (@ `src/textual/css/styles.py`) -> Impact: **148.2** | LOC: 249
- `_render_line` **(Many-Argument Workhorses)** (@ `src/textual/widgets/_text_area.py`) -> Impact: **134.4** | LOC: 229
  * *Intent:* """Render a single line of the TextArea. Called by Textual. Args: y: Y Coordinate of line relative to the widget region. Returns: A rendered line. """
- `_get_box_model` **(Many-Argument Workhorses)** (@ `src/textual/widget.py`) -> Impact: **114.7** | LOC: 144
- `scroll_to_region` **(Many-Argument Workhorses)** (@ `src/textual/widget.py`) -> Impact: **108.5** | LOC: 108
- `parse` **(Many-Argument Workhorses)** (@ `src/textual/_xterm_parser.py`) -> Impact: **96.2** | LOC: 191
- `resolve` **(Many-Argument Workhorses)** (@ `src/textual/_resolve.py`) -> Impact: **95.0** | LOC: 101
- `resolve_box_models` **(Many-Argument Workhorses)** (@ `src/textual/_resolve.py`) -> Impact: **91.4** | LOC: 130
- `_animate` **(Many-Argument Workhorses)** (@ `src/textual/_animator.py`) -> Impact: **88.6** | LOC: 114

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/textual` | 121 | 27259.44 | 34.55% | 8.89% |
| `tests` | 130 | 15996.94 | 10.31% | 0.0% |
| `src/textual/widgets` | 58 | 13066.12 | 22.54% | 7.59% |
| `src/textual/css` | 20 | 5611.18 | 32.31% | 6.36% |
| `tests/text_area` | 11 | 2996.02 | 12.74% | 0.0% |
| `tests/snapshot_tests` | 4 | 2622.3 | 5.03% | 0.0% |
| `tests/snapshot_tests/snapshot_apps` | 149 | 2060.86 | 6.47% | 0.0% |
| `tests/css` | 15 | 1279.46 | 4.46% | 0.0% |
| `src/textual/document` | 7 | 1161.82 | 35.1% | 13.47% |
| `src/textual/drivers` | 12 | 1144.62 | 32.43% | 14.89% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/textual/_types.py` -> **100.0%** Exposure
- `src/textual/cache.py` -> **100.0%** Exposure
- `src/textual/messages.py` -> **99.6272%** Exposure
- `src/textual/pad.py` -> **97.7023%** Exposure
- `src/textual/widgets/_directory_tree.py` -> **96.614%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/textual/__init__.py` -> **100.0%** Exposure
- `src/textual/_arrange.py` -> **100.0%** Exposure
- `src/textual/_binary_encode.py` -> **100.0%** Exposure
- `src/textual/_callback.py` -> **100.0%** Exposure
- `src/textual/_compat.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/snapshot_tests/test_snapshots.py` -> **360** Orphaned Functions | **24** Duplicates
- `tests/test_geometry.py` -> **87** Orphaned Functions | **0** Duplicates
- `tests/test_tabbed_content.py` -> **43** Orphaned Functions | **43** Duplicates
- `tests/test_data_table.py` -> **83** Orphaned Functions | **0** Duplicates
- `tests/test_reactive.py` -> **53** Orphaned Functions | **22** Duplicates

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
- **Unknown Dependencies:** `3784` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/textual/widget.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 3419.6 | **LOC:** 4955 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 97.6%
- **Blast Radius:** changing it is visible to **99** in-repo importer(s); it depends on **57**; blast radius 20.605; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 40.4762% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_box_model` **(Many-Argument Workhorses)** (Impact: 114.7)
  * `scroll_to_region` **(Many-Argument Workhorses)** (Impact: 108.5)
  * `_scroll_to` **(Many-Argument Workhorses)** (Impact: 74.5)
  * `mount` **(Many-Argument Workhorses)** (Impact: 55.6)
  * `scroll_end` **(Many-Argument Workhorses)** (Impact: 44.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 325 instances
* *Concurrency (weighted view):* 112
* *State Mutation (weighted view):* 1068
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 590`, `structural_boundaries: 725`, `args: 288`, `func_start: 269`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 418`, `planned_debt: 12`, `fragile_debt: 1`
* *Architecture:* `api: 237`, `concurrency: 47`, `import: 63`
* *Defense:* `safety: 94`, `doc: 264`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.605
  * `Choke Point (Betweenness):` 0.033373 | `Ripple Effect (Closeness):` 0.371913
  * `Imports (Out-Degree: 40):` __future__, asyncio, collections, contextlib, fractions, rich.console, rich.measure, rich.repr...
  * `Imported By (In-Degree: 99):` (Excluded from Brief to save tokens)

### `src/textual/app.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 3202.0 | **LOC:** 4986 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 96.4%
- **Blast Radius:** changing it is visible to **376** in-repo importer(s); it depends on **89**; blast radius 74.899; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (89.5%), Guard Balance (formerly Safety Score) (81.9%)
- **Documentation Coverage:** 31.3175% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 82.0)
  * `on_event` **(Stateful Encapsulated Methods)** (Impact: 54.7)
    * *Intent:* # Handle input events that haven't been forwarded # If the event has been forwarded it may have bubb...
  * `_process_messages` **(Many-Argument Workhorses)** (Impact: 52.6)
  * `_log` **(Many-Argument Workhorses)** (Impact: 37.1)
  * `_display` **(Stateful Encapsulated Methods)** (Impact: 35.5)
    * *Intent:* """Display a renderable within a sync. Args: screen: Screen instance renderable: A Rich renderable. ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 66 instances
* *Amplified Cascading Flux:* 242 instances
* *Api Near Db Sink:* 1 instances
* *Concurrency (weighted view):* 488
* *State Mutation (weighted view):* 830
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 490`, `structural_boundaries: 755`, `args: 254`, `func_start: 246`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 346`, `dead_code: 1`, `planned_debt: 6`, `duplicate_logic: 2`
* *Architecture:* `io: 16`, `api: 212`, `concurrency: 158`, `import: 105`
* *Defense:* `safety: 148`, `doc: 312`, `sync_locks: 5`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 74.899
  * `Choke Point (Betweenness):` 0.096841 | `Ripple Effect (Closeness):` 0.500353
  * `Imports (Out-Degree: 51):` __future__, asyncio, base64, concurrent.futures, contextlib, functools, gc, importlib...
  * `Imported By (In-Degree: 376):` (Excluded from Brief to save tokens)

### `tests/snapshot_tests/test_snapshots.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2529.26 | **LOC:** 4874 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 88.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 0.399; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.6%), Complexity Load (formerly Cognitive Load) (15.7%), Connectivity (formerly Api Exposure) (15.4%)
- **Documentation Coverage:** 66.1404% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_click_selection_disabled_when_allow_select_is_false` **(Generic / Templated Code)** (Impact: 12.7)
  * `test_datatable_auto_height_future_updates` **(Generic / Templated Code)** (Impact: 7.7)
    * *Intent:* """https://github.com/Textualize/textual/issues/4928 meant that when height=None, in add_row, future...
  * `test_add_separator` **(Generic / Templated Code)** (Impact: 7.4)
    * *Intent:* """Regression test for https://github.com/Textualize/textual/issues/5431 You should see a button on ...
  * `compose` **(Generic / Templated Code)** (Impact: 7.4)
  * `test_panel_border_title_colors` **(Compute Cores)** (Impact: 6.5)
    * *Intent:* """Regression test for https://github.com/Textualize/textual/issues/5548 You should see four labels ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 38 instances
* *Api Near Db Sink:* 12 instances
* *Concurrency (weighted view):* 233
* *State Mutation (weighted view):* 335
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 1268`, `args: 572`, `func_start: 571`, `class_start: 136`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 259`, `planned_debt: 2`, `fragile_debt: 4`, `duplicate_logic: 24`, `unreferenced_by_name: 360`
* *Architecture:* `io: 5`, `api: 705`, `concurrency: 143`, `import: 26`
* *Defense:* `safety: 343`, `doc: 266`, `test: 357`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.399
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` __future__, asyncio, pathlib, pytest, rich.panel, rich.text, tests.snapshot_tests.language_snippets, textual...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/textual/widgets/_data_table.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2141.1 | **LOC:** 2865 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 85.7%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **30**; blast radius 0.792; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.1%), Debt Markers (formerly Tech Debt) (84.2%), Connectivity (formerly Api Exposure) (46.8%)
- **Documentation Coverage:** 45.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_render_cell` **(Many-Argument Workhorses)** (Impact: 53.1)
  * `_get_styles_to_render_cell` **(Many-Argument Workhorses)** (Impact: 52.6)
  * `_render_line_in_row` **(Many-Argument Workhorses)** (Impact: 52.3)
  * `_update_dimensions` **(Many-Argument Workhorses)** (Impact: 38.3)
    * *Intent:* """Called to recalculate the virtual (scrollable) size. This recomputes column widths and then check...
  * `add_row` **(Many-Argument Workhorses)** (Impact: 30.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 300 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 1008
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 327`, `structural_boundaries: 322`, `args: 133`, `func_start: 133`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 408`, `planned_debt: 2`, `duplicate_logic: 18`
* *Architecture:* `api: 103`, `concurrency: 2`, `import: 30`
* *Defense:* `safety: 20`, `doc: 176`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.792
  * `Choke Point (Betweenness):` 0.000325 | `Ripple Effect (Closeness):` 0.004438
  * `Imports (Out-Degree: 16):` __future__, dataclasses, functools, itertools, operator, rich.console, rich.padding, rich.protocol...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tests/test_data_table.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1763.54 | **LOC:** 1492 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.399; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (39.4%), Guard Balance (formerly Safety Score) (17.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (14.1%)
- **Documentation Coverage:** 75.419% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_sort_by_function_sum` **(Defensive Guards)** (Impact: 6.8)
    * *Intent:* """Test sorting a `DataTable` using a custom sort function."""
  * `test_datatable_message_emission` **(I/O & Config Routines)** (Impact: 6.2)
  * `test_move_cursor_respects_animate_parameter` **(C Struct Operations)** (Impact: 3.8)
    * *Intent:* """Regression test for https://github.com/Textualize/textual/issues/3840 Make sure that the call to ...
  * `record_data_table_event` **(Generic / Templated Code)** (Impact: 3.7)
  * `on_mount` **(Parameter Forwarders)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 193 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 1183
* *State Mutation (weighted view):* 288
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 550`, `args: 91`, `func_start: 91`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 262`, `unreferenced_by_name: 83`
* *Architecture:* `api: 92`, `concurrency: 218`, `import: 12`
* *Defense:* `safety: 245`, `doc: 23`, `test: 104`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.399
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` __future__, pytest, rich.panel, rich.text, textual._wait, textual.actions, textual.app, textual.coordinate...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/textual/widgets/_text_area.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1739.72 | **LOC:** 2656 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **36**; blast radius 0.73; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.3%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (51.2%)
- **Documentation Coverage:** 21.8107% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_render_line` **(Many-Argument Workhorses)** (Impact: 134.4)
    * *Intent:* """Render a single line of the TextArea. Called by Textual. Args: y: Y Coordinate of line relative t...
  * `_set_document` **(Stateful Encapsulated Methods)** (Impact: 39.2)
    * *Intent:* """Construct and return an appropriate document. Args: text: The text of the document. language: The...
  * `render_line` **(Compute Cores)** (Impact: 32.6)
    * *Intent:* """Render a single line of the TextArea. Called by Textual. Args: y: Y Coordinate of line relative t...
  * `find_matching_bracket` **(Many-Argument Workhorses)** (Impact: 32.5)
  * `_redo_batch` **(Stateful Encapsulated Methods)** (Impact: 21.5)
    * *Intent:* """Redo a batch of Edits in order. The sequence must be chronologically ordered by edit time. Edits ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 226 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 750
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 283`, `structural_boundaries: 320`, `args: 133`, `func_start: 133`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 298`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 116`, `concurrency: 8`, `import: 37`
* *Defense:* `safety: 17`, `doc: 164`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.73
  * `Choke Point (Betweenness):` 0.001033 | `Ripple Effect (Closeness):` 0.012681
  * `Imports (Out-Degree: 22):` __future__, collections, dataclasses, functools, pathlib, re, rich.console, rich.segment...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/textual/content.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1696.24 | **LOC:** 1834 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 94.1%
- **Blast Radius:** changing it is visible to **32** in-repo importer(s); it depends on **25**; blast radius 7.125; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.8%)
- **Documentation Coverage:** 42.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_wrap_and_format` **(Many-Argument Workhorses)** (Impact: 63.5)
  * `render` **(Many-Argument Workhorses)** (Impact: 44.7)
  * `split` **(Many-Argument Workhorses)** (Impact: 38.2)
  * `to_strip` **(Many-Argument Workhorses)** (Impact: 34.6)
  * `join` **(Many-Argument Workhorses)** (Impact: 32.4)
    * *Intent:* """Join an iterable of content or strings. This works much like the join method on `str` objects. Se...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 235 instances
* *State Mutation (weighted view):* 746
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 310`, `structural_boundaries: 269`, `args: 75`, `func_start: 75`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 276`, `planned_debt: 3`
* *Architecture:* `api: 68`, `import: 27`
* *Defense:* `safety: 37`, `doc: 66`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.125
  * `Choke Point (Betweenness):` 0.00704 | `Ripple Effect (Closeness):` 0.348706
  * `Imports (Out-Degree: 12):` __future__, functools, operator, re, rich._wrap, rich.cells, rich.console, rich.repr...
  * `Imported By (In-Degree: 32):` (Excluded from Brief to save tokens)

### `src/textual/screen.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1618.38 | **LOC:** 2234 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 97.1%
- **Blast Radius:** changing it is visible to **44** in-repo importer(s); it depends on **42**; blast radius 11.564; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (94.5%), Guard Balance (formerly Safety Score) (91.4%), Concurrency Surface (formerly Concurrency) (89.0%)
- **Documentation Coverage:** 29.5858% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_forward_event` **(Stateful Encapsulated Methods)** (Impact: 73.6)
  * `_refresh_layout` **(Many-Argument Workhorses)** (Impact: 46.0)
    * *Intent:* """Refresh the layout (can change size and positions of widgets)."""
  * `_move_focus` **(Many-Argument Workhorses)** (Impact: 39.4)
  * `_check_auto_scroll` **(Many-Argument Workhorses)** (Impact: 32.1)
  * `_handle_mouse_move` **(Stateful Encapsulated Methods)** (Impact: 28.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 185 instances
* *Concurrency (weighted view):* 71
* *State Mutation (weighted view):* 603
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 330`, `structural_boundaries: 311`, `args: 98`, `func_start: 98`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 233`, `planned_debt: 1`
* *Architecture:* `api: 75`, `concurrency: 21`, `import: 44`
* *Defense:* `safety: 56`, `doc: 124`, `sync_locks: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.564
  * `Choke Point (Betweenness):` 0.0136 | `Ripple Effect (Closeness):` 0.350125
  * `Imports (Out-Degree: 32):` __future__, asyncio, functools, operator, rich.console, rich.repr, rich.style, textual...
  * `Imported By (In-Degree: 44):` (Excluded from Brief to save tokens)

### `src/textual/css/_styles_builder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1349.08 | **LOC:** 1317 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **22**; blast radius 0.973; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.3%)
- **Documentation Coverage:** 92.517% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_hatch` **(Many-Argument Workhorses)** (Impact: 39.7)
  * `process_transition` **(Many-Argument Workhorses)** (Impact: 31.1)
  * `process_color` **(Many-Argument Workhorses)** (Impact: 28.1)
    * *Intent:* """Processes a simple color declaration."""
  * `_parse_border` **(Stateful Encapsulated Methods)** (Impact: 21.9)
  * `process_keyline` **(Many-Argument Workhorses)** (Impact: 19.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 170 instances
* *State Mutation (weighted view):* 596
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 163`, `args: 79`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 256`
* *Architecture:* `api: 67`, `import: 22`
* *Defense:* `safety: 40`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.973
  * `Choke Point (Betweenness):` 0.003248 | `Ripple Effect (Closeness):` 0.206381
  * `Imports (Out-Degree: 19):` __future__, rich.repr, textual._border, textual._cells, textual._duration, textual._easing, textual.color, textual.css._error_tools...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/textual/widgets/_markdown.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1316.72 | **LOC:** 1669 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **29**; blast radius 1.267; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.6%), Connectivity (formerly Api Exposure) (57.8%)
- **Documentation Coverage:** 43.3962% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_parse_markdown` **(Many-Argument Workhorses)** (Impact: 58.1)
    * *Intent:* """Create a stream of MarkdownBlock widgets from markdown. Args: tokens: List of tokens. Yields: Wid...
  * `_token_to_content` **(Many-Argument Workhorses)** (Impact: 31.9)
    * *Intent:* """Convert an inline token to Textual Content. Args: token: A markdown token. Returns: Content insta...
  * `append` **(Stateful Encapsulated Methods)** (Impact: 29.3)
    * *Intent:* """Append to markdown. Args: markdown: A fragment of markdown to be appended. Returns: An optionally...
  * `update` **(Stateful Encapsulated Methods)** (Impact: 24.2)
    * *Intent:* """Update the document with new Markdown. Args: markdown: A string containing Markdown. Returns: An ...
  * `await_append` **(Defensive Guards)** (Impact: 15.2)
    * *Intent:* """Append new markdown widgets."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 48 instances
* *Amplified Cascading Flux:* 103 instances
* *Concurrency (weighted view):* 306
* *State Mutation (weighted view):* 411
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 280`, `args: 93`, `func_start: 93`, `class_start: 36`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 205`, `duplicate_logic: 3`
* *Architecture:* `io: 1`, `api: 102`, `concurrency: 66`, `import: 29`
* *Defense:* `safety: 30`, `doc: 123`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.267
  * `Choke Point (Betweenness):` 0.000744 | `Ripple Effect (Closeness):` 0.008322
  * `Imports (Out-Degree: 17):` __future__, asyncio, contextlib, functools, markdown_it, markdown_it.token, pathlib, re...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/textual/dom.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1221.96 | **LOC:** 1917 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 92.9%
- **Blast Radius:** changing it is visible to **30** in-repo importer(s); it depends on **44**; blast radius 34.231; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.8%), Connectivity (formerly Api Exposure) (82.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 34.9138% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `query_one` **(Many-Argument Workhorses)** (Impact: 45.6)
  * `query_exactly_one` **(Many-Argument Workhorses)** (Impact: 39.3)
  * `query_ancestor` **(Defensive Guards)** (Impact: 21.9)
  * `data_bind` **(Many-Argument Workhorses)** (Impact: 20.4)
  * `rich_style` **(Compute Cores)** (Impact: 18.8)
    * *Intent:* """Get a Rich Style object for this DOMNode. Returns: A Rich style. """
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 144 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 448
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 368`, `args: 112`, `func_start: 112`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 160`, `dead_code: 1`, `planned_debt: 5`
* *Architecture:* `api: 110`, `concurrency: 3`, `import: 56`
* *Defense:* `safety: 49`, `doc: 106`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.231
  * `Choke Point (Betweenness):` 0.017102 | `Ripple Effect (Closeness):` 0.35041
  * `Imports (Out-Degree: 28):` __future__, _typeshed, functools, inspect, re, rich.columns, rich.console, rich.highlighter...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `src/textual/widgets/_tree.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1153.0 | **LOC:** 1601 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **19**; blast radius 5.302; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (51.5%)
- **Documentation Coverage:** 29.8969% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_render_line` **(Many-Argument Workhorses)** (Impact: 79.8)
  * `add` **(Many-Argument Workhorses)** (Impact: 51.9)
  * `add_json` **(Many-Argument Workhorses)** (Impact: 20.2)
    * *Intent:* """Adds JSON data to a node. Args: json_data: An object decoded from JSON. node: Node to add data to...
  * `watch_cursor_line` **(Stateful Encapsulated Methods)** (Impact: 19.4)
  * `_build` **(Stateful Encapsulated Methods)** (Impact: 19.3)
    * *Intent:* """Builds the tree by traversing nodes, and creating tree lines."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 123 instances
* *Concurrency (weighted view):* 20
* *State Mutation (weighted view):* 449
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 235`, `args: 111`, `func_start: 111`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 203`, `duplicate_logic: 8`
* *Architecture:* `api: 93`, `concurrency: 5`, `import: 19`
* *Defense:* `safety: 31`, `doc: 114`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.302
  * `Choke Point (Betweenness):` 0.002551 | `Ripple Effect (Closeness):` 0.189896
  * `Imports (Out-Degree: 11):` __future__, dataclasses, rich.highlighter, rich.repr, rich.style, rich.text, textual, textual._immutable_sequence_view...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `tests/test_widget.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 897.08 | **LOC:** 769 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.399; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (40.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.9%), Guard Balance (formerly Safety Score) (28.7%)
- **Documentation Coverage:** 85.034% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_compose_order` **(Generic / Templated Code)** (Impact: 7.1)
  * `test_sort_children_no_key` **(Defensive Guards)** (Impact: 5.8)
    * *Intent:* """Test sorting with no key."""
  * `test_sort_children` **(Defensive Guards)** (Impact: 5.7)
    * *Intent:* """Test the sort_children method."""
  * `test_of_type` **(Defensive Guards)** (Impact: 4.2)
  * `compose` **(Type Conversions)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 80 instances
* *Amplified Cascading Flux:* 10 instances
* *Api Near Db Sink:* 3 instances
* *Concurrency (weighted view):* 497
* *State Mutation (weighted view):* 146
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 334`, `args: 75`, `func_start: 75`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 126`, `duplicate_logic: 2`, `unreferenced_by_name: 47`
* *Architecture:* `api: 98`, `concurrency: 97`, `import: 20`
* *Defense:* `safety: 98`, `doc: 11`, `test: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.399
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` operator, pytest, textual, textual._node_list, textual.app, textual.containers, textual.content, textual.css.errors...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_reactive.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 890.78 | **LOC:** 843 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.399; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (46.6%), Complexity Load (formerly Cognitive Load) (27.7%), Connectivity (formerly Api Exposure) (13.9%)
- **Documentation Coverage:** 73.913% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_public_and_private_validate_order` **(Stateful Encapsulated Methods)** (Impact: 4.0)
    * *Intent:* """The private validate should be called first."""
  * `validate_value` **(Generic / Templated Code)** (Impact: 3.7)
  * `_validate_value` **(Encapsulated Accessors)** (Impact: 3.7)
  * `test_watch_compute` **(Defensive Guards)** (Impact: 3.5)
    * *Intent:* """Check that watching a computed attribute works."""
  * `test_reactive_inheritance` **(Defensive Guards)** (Impact: 3.1)
    * *Intent:* """Check that inheritance works as expected for reactives."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 63 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 388
* *State Mutation (weighted view):* 174
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 322`, `args: 99`, `func_start: 98`, `class_start: 45`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 162`, `duplicate_logic: 22`, `unreferenced_by_name: 53`
* *Architecture:* `api: 131`, `concurrency: 73`, `import: 8`
* *Defense:* `safety: 95`, `doc: 24`, `test: 38`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.399
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` __future__, asyncio, pytest, textual.app, textual.message, textual.message_pump, textual.reactive, textual.widget
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_tabbed_content.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 878.38 | **LOC:** 917 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.399; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (43.7%), Connectivity (formerly Api Exposure) (14.5%), Guard Balance (formerly Safety Score) (11.0%)
- **Documentation Coverage:** 90.8163% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_tabbed_content_switch_via_ui` **(Defensive Guards)** (Impact: 3.9)
    * *Intent:* """Check tab navigation via the user interface."""
  * `test_tabbed_content_add_before_pane` **(Defensive Guards)** (Impact: 3.2)
  * `test_tabbed_content_add_after_pane` **(Defensive Guards)** (Impact: 3.2)
  * `test_tabbed_content_switch_via_code` **(Defensive Guards)** (Impact: 3.0)
    * *Intent:* """Check tab navigation via code."""
  * `test_tabbed_content_add_before_id` **(Defensive Guards)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 65 instances
* *Concurrency (weighted view):* 475
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 515`, `args: 98`, `func_start: 98`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 70`, `duplicate_logic: 43`, `unreferenced_by_name: 43`
* *Architecture:* `api: 138`, `concurrency: 150`, `import: 6`
* *Defense:* `safety: 143`, `doc: 9`, `test: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.399
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, pytest, textual.app, textual.reactive, textual.widgets, textual.widgets._tabbed_content
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/textual/widgets/_input.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 842.02 | **LOC:** 1124 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **24**; blast radius 1.238; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.0%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (66.0%)
- **Documentation Coverage:** 21.374% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 59.4)
  * `render_line` **(Many-Argument Workhorses)** (Impact: 27.4)
  * `replace` **(Many-Argument Workhorses)** (Impact: 24.2)
    * *Intent:* """Replace the text between the start and end locations with the given text. Args: text: Text to rep...
  * `_watch_value` **(Stateful Encapsulated Methods)** (Impact: 15.0)
    * *Intent:* """Update the virtual size and suggestion when the value changes."""
  * `action_cursor_right` **(Compute Cores)** (Impact: 14.8)
    * *Intent:* """Accept an auto-completion or move the cursor one position to the right. Args: select: If `True`, ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 102 instances
* *Concurrency (weighted view):* 22
* *State Mutation (weighted view):* 341
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 172`, `args: 70`, `func_start: 70`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 137`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 66`, `concurrency: 7`, `import: 25`
* *Defense:* `safety: 6`, `doc: 88`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.238
  * `Choke Point (Betweenness):` 0.001823 | `Ripple Effect (Closeness):` 0.175634
  * `Imports (Out-Degree: 14):` __future__, dataclasses, re, rich.cells, rich.console, rich.highlighter, rich.text, textual...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/textual/strip.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 820.44 | **LOC:** 818 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **15**; blast radius 4.558; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.3%)
- **Documentation Coverage:** 36.5854% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `align` **(Many-Argument Workhorses)** (Impact: 66.9)
  * `crop` **(Many-Argument Workhorses)** (Impact: 36.9)
    * *Intent:* """Crop a strip between two cell positions. Args: start: The start cell position (inclusive). end: T...
  * `join` **(Compute Cores)** (Impact: 25.4)
    * *Intent:* """Join a number of strips into one. Args: strips: An iterable of Strips. Returns: A new combined st...
  * `text_align` **(Many-Argument Workhorses)** (Impact: 21.6)
  * `adjust_cell_length` **(Many-Argument Workhorses)** (Impact: 20.7)
    * *Intent:* """Adjust the cell length, possibly truncating or extending. Args: cell_length: New desired cell len...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 118 instances
* *State Mutation (weighted view):* 369
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 135`, `args: 42`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 133`
* *Architecture:* `api: 42`, `import: 15`
* *Defense:* `safety: 5`, `doc: 31`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.558
  * `Choke Point (Betweenness):` 0.001082 | `Ripple Effect (Closeness):` 0.271485
  * `Imports (Out-Degree: 6):` __future__, functools, rich.cells, rich.color, rich.console, rich.measure, rich.repr, rich.segment...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/textual/css/_style_properties.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 787.54 | **LOC:** 1259 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **24**; blast radius 0.896; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (82.6%), Guard Balance (formerly Safety Score) (76.5%), Complexity Load (formerly Cognitive Load) (45.9%)
- **Documentation Coverage:** 81.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__set__` **(Many-Argument Workhorses)** (Impact: 32.9)
  * `__set__` **(Many-Argument Workhorses)** (Impact: 30.7)
    * *Intent:* """Set the string property and ensure it is in the set of allowed values. Args: obj: The `Styles` ob...
  * `__set__` **(Many-Argument Workhorses)** (Impact: 28.6)
  * `__set__` **(Many-Argument Workhorses)** (Impact: 26.1)
    * *Intent:* """Set the style using a style flag string. Args: obj: The ``Styles`` object. style_flags: The style...
  * `__set__` **(Many-Argument Workhorses)** (Impact: 24.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 64 instances
* *State Mutation (weighted view):* 236
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 220`, `args: 73`, `func_start: 73`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 108`, `duplicate_logic: 12`
* *Architecture:* `api: 32`, `import: 26`
* *Defense:* `safety: 46`, `doc: 56`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.896
  * `Choke Point (Betweenness):` 0.00282 | `Ripple Effect (Closeness):` 0.208987
  * `Imports (Out-Degree: 18):` __future__, operator, rich.errors, rich.repr, rich.style, textual._border, textual._cells, textual.canvas...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/textual/css/styles.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 775.22 | **LOC:** 1529 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **23**; blast radius 8.761; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.6%), Connectivity (formerly Api Exposure) (77.0%)
- **Documentation Coverage:** 41.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `css_lines` **(Compute Cores)** (Impact: 148.2)
  * `__textual_animation__` **(Many-Argument Workhorses)** (Impact: 25.5)
  * `_get_border_css_lines` **(Many-Argument Workhorses)** (Impact: 22.6)
  * `refresh` **(Many-Argument Workhorses)** (Impact: 18.0)
  * `extract_rules` **(Many-Argument Workhorses)** (Impact: 15.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 235
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 188`, `args: 74`, `func_start: 74`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 149`
* *Architecture:* `api: 68`, `import: 24`
* *Defense:* `safety: 11`, `doc: 105`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.761
  * `Choke Point (Betweenness):` 0.009463 | `Ripple Effect (Closeness):` 0.286297
  * `Imports (Out-Degree: 15):` __future__, dataclasses, functools, operator, rich.repr, rich.style, textual._animator, textual._types...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/textual/message_pump.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 762.28 | **LOC:** 921 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **26**; blast radius 13.554; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 31.5789% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_dispatch_methods` **(Many-Argument Workhorses)** (Impact: 46.9)
  * `__new__` **(Many-Argument Workhorses)** (Impact: 28.8)
  * `_on_message` **(Stateful Encapsulated Methods)** (Impact: 18.8)
    * *Intent:* """Called to process a message. Args: message: A Message object. """
  * `_process_messages_loop` **(Stateful Encapsulated Methods)** (Impact: 18.6)
    * *Intent:* """Process messages until the queue is closed."""
  * `_close_messages` **(Stateful Encapsulated Methods)** (Impact: 16.6)
    * *Intent:* """Close message queue, and optionally wait for queue to finish processing."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 28 instances
* *Amplified Cascading Flux:* 58 instances
* *Concurrency (weighted view):* 196
* *State Mutation (weighted view):* 193
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 237`, `args: 54`, `func_start: 54`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 77`
* *Architecture:* `api: 36`, `concurrency: 56`, `import: 31`
* *Defense:* `safety: 52`, `doc: 48`, `sync_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.554
  * `Choke Point (Betweenness):` 0.00473 | `Ripple Effect (Closeness):` 0.278694
  * `Imports (Out-Degree: 16):` __future__, asyncio, contextlib, functools, textual, textual._callback, textual._compat, textual._context...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/textual/_styles_cache.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 640.94 | **LOC:** 514 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **25**; blast radius 0.894; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.4%), Complexity Load (formerly Cognitive Load) (65.4%), Connectivity (formerly Api Exposure) (37.6%)
- **Documentation Coverage:** 45.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render_line` **(Many-Argument Workhorses)** (Impact: 270.8)
  * `render` **(Many-Argument Workhorses)** (Impact: 66.5)
  * `render_widget` **(Many-Argument Workhorses)** (Impact: 25.1)
    * *Intent:* """Render the content for a widget. Args: widget: A widget. region: A region of the widget to render...
  * `line_post` **(Generic / Templated Code)** (Impact: 7.6)
    * *Intent:* """Apply effects to segments inside the border."""
  * `set_dirty` **(Generic / Templated Code)** (Impact: 7.3)
    * *Intent:* """Add a dirty regions."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 70 instances
* *State Mutation (weighted view):* 228
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 71`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 88`
* *Architecture:* `api: 12`, `import: 25`
* *Defense:* `safety: 2`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.894
  * `Choke Point (Betweenness):` 0.005557 | `Ripple Effect (Closeness):` 0.251493
  * `Imports (Out-Degree: 16):` __future__, functools, rich.repr, rich.segment, rich.style, rich.terminal_theme, textual, textual._ansi_theme...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/text_area/test_edit_via_bindings.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 639.4 | **LOC:** 566 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.399; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (32.0%), Connectivity (formerly Api Exposure) (10.6%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_cut` **(Defensive Guards)** (Impact: 2.8)
  * `test_tab_with_spaces_goes_to_tab_stop` **(Defensive Guards)** (Impact: 2.6)
  * `test_deletion_with_non_empty_selection` **(Defensive Guards)** (Impact: 2.6)
    * *Intent:* """When there's a selection, pressing backspace or delete should delete everything that is selected ...
  * `test_delete_word_left` **(Defensive Guards)** (Impact: 2.5)
  * `test_delete_word_left_with_tabs` **(Defensive Guards)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 78 instances
* *Concurrency (weighted view):* 468
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 164`, `args: 27`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `state_mutation: 82`, `fragile_debt: 1`, `unreferenced_by_name: 27`
* *Architecture:* `api: 28`, `concurrency: 78`, `import: 5`
* *Defense:* `safety: 49`, `doc: 12`, `test: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.399
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` pytest, textual.app, textual.events, textual.widgets, textual.widgets.text_area
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/textual/command.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 637.72 | **LOC:** 1277 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **32**; blast radius 8.155; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.1%)
- **Documentation Coverage:** 25.7732% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_search_for` **(Many-Argument Workhorses)** (Impact: 28.5)
  * `_gather_commands` **(Stateful Encapsulated Methods)** (Impact: 26.7)
    * *Intent:* """Gather up all of the commands that match the search value. Args: search_value: The value to searc...
  * `_select_or_command` **(Stateful Encapsulated Methods)** (Impact: 15.5)
  * `_provider_classes` **(Stateful Encapsulated Methods)** (Impact: 14.6)
    * *Intent:* """The currently available command providers. This is a combination of the command providers defined...
  * `__init__` **(Generic / Templated Code)** (Impact: 12.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 49 instances
* *Concurrency (weighted view):* 103
* *State Mutation (weighted view):* 177
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 202`, `args: 63`, `func_start: 63`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 79`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 46`, `concurrency: 33`, `import: 34`
* *Defense:* `safety: 29`, `doc: 102`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.155
  * `Choke Point (Betweenness):` 0.00899 | `Ripple Effect (Closeness):` 0.310464
  * `Imports (Out-Degree: 17):` __future__, abc, asyncio, dataclasses, functools, inspect, operator, rich.align...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `src/textual/geometry.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 624.98 | **LOC:** 1488 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **80** in-repo importer(s); it depends on **9**; blast radius 31.466; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (95.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.4%)
- **Documentation Coverage:** 16.9492% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `intersection` **(Compute Cores)** (Impact: 30.6)
    * *Intent:* """Get the overlapping portion of the two regions. Args: region: A region that overlaps this region....
  * `constrain` **(Many-Argument Workhorses)** (Impact: 28.3)
  * `get_scroll_to_visible` **(Many-Argument Workhorses)** (Impact: 20.5)
  * `selection_bounds` **(Many-Argument Workhorses)** (Impact: 19.6)
    * *Intent:* """Get a shape that would be constructed by a user selecting text between two points. The shape woul...
  * `clamp` **(Many-Argument Workhorses)** (Impact: 15.6)
    * *Intent:* """Restrict a value to a given range. If `value` is less than the minimum, return the minimum. If `v...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 238`, `args: 96`, `func_start: 96`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 36`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 86`, `import: 9`
* *Defense:* `safety: 18`, `doc: 103`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 31.466
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.394649
  * `Imports (Out-Degree: 0):` __future__, functools, operator, os, rich.repr, textual.geometry, textual_speedups, typing...
  * `Imported By (In-Degree: 80):` (Excluded from Brief to save tokens)

### `tests/test_screens.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 620.74 | **LOC:** 626 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.399; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (35.6%), Guard Balance (formerly Safety Score) (25.7%), Connectivity (formerly Api Exposure) (13.8%)
- **Documentation Coverage:** 76.3441% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_screens` **(Defensive Guards)** (Impact: 5.5)
  * `test_worker_cancellation` **(Annotated & Test Methods)** (Impact: 3.9)
    * *Intent:* """Regression test for https://github.com/Textualize/textual/issues/4884 The MRE below was pushing a...
  * `test_auto_focus_on_screen_if_app_auto_focus_is_none` **(Defensive Guards)** (Impact: 3.1)
    * *Intent:* """Setting app.AUTO_FOCUS = `None` means it is not taken into consideration."""
  * `test_auto_focus_on_screen_if_app_auto_focus_is_disabled` **(Defensive Guards)** (Impact: 3.1)
    * *Intent:* """Setting app.AUTO_FOCUS = `None` means it is not taken into consideration."""
  * `test_mouse_move_event_bubbles_to_screen_from_widget` **(Interface Declarations)** (Impact: 2.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 55 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 349
* *State Mutation (weighted view):* 85
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 267`, `args: 47`, `func_start: 47`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 83`, `duplicate_logic: 15`, `unreferenced_by_name: 22`
* *Architecture:* `io: 2`, `api: 84`, `concurrency: 74`, `import: 17`
* *Defense:* `safety: 86`, `doc: 12`, `test: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.399
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` __future__, asyncio, pytest, sys, textual, textual.app, textual.containers, textual.events...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/textual/widget.py` -> **Will McGugan** (97.6% isolated ownership) | Magnitude: 3419.6
- `src/textual/app.py` -> **Will McGugan** (96.4% isolated ownership) | Magnitude: 3202.0
- `tests/snapshot_tests/test_snapshots.py` -> **Will McGugan** (88.9% isolated ownership) | Magnitude: 2529.26
- `src/textual/widgets/_data_table.py` -> **Will McGugan** (85.7% isolated ownership) | Magnitude: 2141.1
- `tests/test_data_table.py` -> **Will McGugan** (100.0% isolated ownership) | Magnitude: 1763.54

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/textual/app.py` -> **Severity: 9.684** (Bridge: 0.0968 * Flux: 99.9963%)
- `src/textual/widget.py` -> **Severity: 3.337** (Bridge: 0.0334 * Flux: 99.9995%)
- `src/textual/dom.py` -> **Severity: 1.71** (Bridge: 0.0171 * Flux: 100.0%)
- `src/textual/screen.py` -> **Severity: 1.36** (Bridge: 0.0136 * Flux: 100.0%)
- `src/textual/css/styles.py` -> **Severity: 0.946** (Bridge: 0.0095 * Flux: 99.9225%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/textual/app.py` -> **Severity: 40.993** (Embedded: 0.5004 * Error Risk: 81.929%)
- `src/textual/content.py` -> **Severity: 33.95** (Embedded: 0.3487 * Error Risk: 97.3611%)
- `src/textual/demo/widgets.py` -> **Severity: 33.726** (Embedded: 0.4126 * Error Risk: 81.7467%)
- `src/textual/reactive.py` -> **Severity: 33.398** (Embedded: 0.3604 * Error Risk: 92.6725%)
- `src/textual/_types.py` -> **Severity: 33.355** (Embedded: 0.3473 * Error Risk: 96.0402%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/textual/demo/widgets.py` -> **Severity: 3500.053** (Blast Radius: 43.334 * Doc Risk: 80.7692%)
- `src/textual/app.py` -> **Severity: 2345.649** (Blast Radius: 74.899 * Doc Risk: 31.3175%)
- `src/textual/_types.py` -> **Severity: 1421.1** (Blast Radius: 14.211 * Doc Risk: 100.0%)
- `src/textual/dom.py` -> **Severity: 1195.134** (Blast Radius: 34.231 * Doc Risk: 34.9138%)
- `src/textual/containers.py` -> **Severity: 1166.9** (Blast Radius: 11.669 * Doc Risk: 100.0%)

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
