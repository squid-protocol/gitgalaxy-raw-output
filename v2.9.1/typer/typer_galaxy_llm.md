# ARCHITECTURAL_BRIEF: typer
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 574 analyzed artifact(s), 16499 LOC.
- **Load-bearing artifact:** `typer-0.24.1/typer/testing.py` -- 169 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `typer-0.24.1/typer/main.py` -- pulls in 29 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `typer-0.24.1/typer/main.py` at magnitude 1081.96 (structural weight, not risk).
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
| Total Artifacts | 579 |
| Analyzed Artifacts (Scanned) | 574 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 16499 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 99.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4194 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5819 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.8757 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 20 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 573 | 16499 | 99.8% |
| MARKDOWN | 1 | 0 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `1.941`
> **Composition Archetype:** `Small Flat Repo (2)` (z +1.94; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 29%, Data / Markup / Trivial 28%, Parameter Forwarders Files 20%, Interface Declarations Files 6%, Compute Cores Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 573 | 99.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.py`: 1x Packed Payload Guard (Impossible Density: 3.33 hits/line)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 89.6 | 6.6 | 3.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.5 | 39.1 | 45.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 24.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.6 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 67.9 | 6.7 | 5.6 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 18.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 32.1 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 74.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 75 | 27 | 0 | `typer-0.24.1/tests/test_others.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 2055 | 208 | 11 | `typer-0.24.1/tests/test_tutorial/test_subcommands/test_tutorial003.py` |
| danger | 664 | 229 | 1 | `typer-0.24.1/typer/main.py` |
| concurrency | 31 | 24 | 0 | `typer-0.24.1/typer/rich_utils.py` |
| connectivity | 1490 | 452 | 6 | `typer-0.24.1/tests/test_others.py` |
| io | 385 | 200 | 1 | `typer-0.24.1/tests/test_completion/test_completion_option_colon.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 486 | 183 | 2 | `typer-0.24.1/tests/test_completion/test_completion_option_colon.py` |
| time | 14 | 12 | 0 | `typer-0.24.1/tests/test_tutorial/test_progressbar/test_tutorial001.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 7 | 3 | 0 | `typer-0.24.1/tests/utils.py` |
| events | 185 | 53 | 0 | `typer-0.24.1/typer/main.py` |
| tests | 1404 | 201 | 10 | `typer-0.24.1/tests/test_rich_markup_mode.py` |
| docs | 286 | 59 | 1 | `typer-0.24.1/typer/params.py` |
| debt | 521 | 263 | 2 | `typer-0.24.1/tests/test_others.py` |
| mutation | 6905 | 455 | 21 | `typer-0.24.1/typer/main.py` |
| dead_code | 1140 | 405 | 5 | `typer-0.24.1/tests/test_others.py` |
| credential | 0 | 0 | 0 | - |
| threat | 53 | 17 | 0 | `typer-0.24.1/typer/main.py` |
| ml_ai | 11 | 3 | 0 | `typer-0.24.1/tests/test_tutorial/test_options/test_password/test_tutorial001.py` |
| ui | 1 | 1 | 0 | `typer-0.24.1/typer/rich_utils.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `typer-0.24.1/tests/test_completion/test_completion_option_colon.py` (Hits: 13)
- `typer-0.24.1/typer/core.py` (Hits: 13)
- `typer-0.24.1/typer/main.py` (Hits: 13)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **testing.py** (`typer-0.24.1/typer/testing.py`) — 169 inbound connections
2. **utils.py** (`typer-0.24.1/tests/utils.py`) — 14 inbound connections
3. **core.py** (`typer-0.24.1/typer/core.py`) — 13 inbound connections
4. **models.py** (`typer-0.24.1/typer/models.py`) — 8 inbound connections
5. **completion.py** (`typer-0.24.1/typer/completion.py`) — 7 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **main.py** (`typer-0.24.1/typer/main.py`) — 29 outbound dependencies
2. **rich_utils.py** (`typer-0.24.1/typer/rich_utils.py`) — 25 outbound dependencies
3. **core.py** (`typer-0.24.1/typer/core.py`) — 20 outbound dependencies
4. **test_others.py** (`typer-0.24.1/tests/test_others.py`) — 16 outbound dependencies
5. **cli.py** (`typer-0.24.1/typer/cli.py`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `get_docs_for_click` **(Many-Argument Workhorses)** (@ `typer-0.24.1/typer/cli.py`) -> Impact: **80.8** | LOC: 82
- `_print_options_panel` **(Many-Argument Workhorses)** (@ `typer-0.24.1/typer/rich_utils.py`) -> Impact: **64.2** | LOC: 109
- `get_help_record` **(Many-Argument Workhorses)** (@ `typer-0.24.1/typer/core.py`) -> Impact: **61.9** | LOC: 94
  * *Intent:* # Duplicate all of Click's logic only to modify a single line, to allow boolean # flags with only names for False values as it's currently supported b...
- `_main` **(Many-Argument Workhorses)** (@ `typer-0.24.1/typer/core.py`) -> Impact: **61.6** | LOC: 92
- `get_click_type` **(Many-Argument Workhorses)** (@ `typer-0.24.1/typer/main.py`) -> Impact: **60.5** | LOC: 101
- `rich_format_help` **(Many-Argument Workhorses)** (@ `typer-0.24.1/typer/rich_utils.py`) -> Impact: **55.0** | LOC: 140
- `_get_parameter_help` **(Many-Argument Workhorses)** (@ `typer-0.24.1/typer/rich_utils.py`) -> Impact: **50.4** | LOC: 87
- `get_click_param` **(Compute Cores)** (@ `typer-0.24.1/typer/main.py`) -> Impact: **46.2** | LOC: 161
- `_get_default_string` **(Many-Argument Workhorses)** (@ `typer-0.24.1/typer/core.py`) -> Impact: **42.6** | LOC: 47
- `__init__` **(Many-Argument Workhorses)** (@ `typer-0.24.1/typer/models.py`) -> Impact: **40.2** | LOC: 125

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `typer-0.24.1/typer` | 15 | 3775.92 | 40.26% | 21.5% |
| `typer-0.24.1/tests` | 20 | 1013.24 | 9.98% | 0.0% |
| `typer-0.24.1/tests/test_completion` | 13 | 352.62 | 3.05% | 0.0% |
| `typer-0.24.1/docs_src/options_autocompletion` | 19 | 279.5 | 15.68% | 58.97% |
| `typer-0.24.1/tests/test_cli` | 18 | 249.04 | 0.34% | 0.0% |
| `typer-0.24.1/tests/test_tutorial/test_commands/test_help` | 9 | 220.48 | 8.7% | 0.0% |
| `typer-0.24.1/tests/test_tutorial/test_subcommands` | 4 | 177.58 | 11.8% | 0.0% |
| `typer-0.24.1/tests/test_tutorial/test_options_autocompletion` | 9 | 162.16 | 0.0% | 0.0% |
| `typer-0.24.1/tests/test_tutorial/test_arguments/test_help` | 9 | 159.56 | 0.0% | 0.0% |
| `typer-0.24.1/tests/test_tutorial/test_subcommands/test_name_help` | 9 | 139.64 | 2.12% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `typer-0.24.1/typer/_completion_classes.py` -> **99.9999%** Exposure
- `typer-0.24.1/docs_src/commands/help/tutorial006_py310.py` -> **99.9972%** Exposure
- `typer-0.24.1/docs_src/commands/callback/tutorial001_py310.py` -> **98.9013%** Exposure
- `typer-0.24.1/docs_src/commands/context/tutorial001_py310.py` -> **98.9013%** Exposure
- `typer-0.24.1/docs_src/commands/context/tutorial002_py310.py` -> **98.9013%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `typer-0.24.1/typer/_completion_classes.py` -> **100.0%** Exposure
- `typer-0.24.1/typer/_completion_shared.py` -> **100.0%** Exposure
- `typer-0.24.1/typer/cli.py` -> **100.0%** Exposure
- `typer-0.24.1/typer/core.py` -> **100.0%** Exposure
- `typer-0.24.1/typer/rich_utils.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `typer-0.24.1/tests/test_others.py` -> **18** Orphaned Functions | **6** Duplicates
- `typer-0.24.1/tests/test_rich_markup_mode.py` -> **9** Orphaned Functions | **7** Duplicates
- `typer-0.24.1/tests/test_tutorial/test_subcommands/test_tutorial003.py` -> **16** Orphaned Functions | **0** Duplicates
- `typer-0.24.1/tests/test_type_conversion.py` -> **14** Orphaned Functions | **2** Duplicates
- `typer-0.24.1/tests/test_suggest_commands.py` -> **5** Orphaned Functions | **9** Duplicates

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
- **Unknown Dependencies:** `1529` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `typer-0.24.1/typer/main.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1081.96 | **LOC:** 2014 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **29**; blast radius 106.494; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (59.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_click_type` **(Many-Argument Workhorses)** (Impact: 60.5)
  * `get_click_param` **(Compute Cores)** (Impact: 46.2)
  * `solve_typer_info_help` **(Defensive Guards)** (Impact: 32.9)
    * *Intent:* # Priority 1: Explicit value was set in app.add_typer() if not isinstance(typer_info.help, DefaultPl...
  * `get_param_callback` **(Generic / Templated Code)** (Impact: 31.9)
  * `get_param_completion` **(Compute Cores)** (Impact: 28.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 154 instances
* *State Mutation (weighted view):* 480
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 182`, `args: 39`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 80`, `high_risk_execution: 2`, `state_mutation: 172`
* *Architecture:* `io: 13`, `api: 37`, `import: 27`
* *Defense:* `safety: 30`, `doc: 77`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 106.494
  * `Choke Point (Betweenness):` 0.004822 | `Ripple Effect (Closeness):` 0.149826
  * `Imports (Out-Degree: 7):` , ._typing, .add, .completion, .core, .delete, .models, .utils...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `typer-0.24.1/typer/core.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 691.78 | **LOC:** 822 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **20**; blast radius 47.136; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.6%), Guard Balance (formerly Safety Score) (96.8%), Complexity Load (formerly Cognitive Load) (89.6%)
- **Documentation Coverage:** 96.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_help_record` **(Many-Argument Workhorses)** (Impact: 61.9)
    * *Intent:* # Duplicate all of Click's logic only to modify a single line, to allow boolean # flags with only na...
  * `_main` **(Many-Argument Workhorses)** (Impact: 61.6)
  * `_get_default_string` **(Many-Argument Workhorses)** (Impact: 42.6)
  * `get_help_record` **(Defensive Guards)** (Impact: 39.1)
    * *Intent:* # Modified version of click.core.Option.get_help_record() # to support Arguments if self.hidden: ret...
  * `_typer_param_setup_autocompletion_compat` **(Stateful Encapsulated Methods)** (Impact: 17.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 86 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 273
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 137`, `args: 34`, `func_start: 34`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 50`, `high_risk_execution: 5`, `state_mutation: 101`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 10`
* *Architecture:* `io: 13`, `api: 19`, `import: 26`
* *Defense:* `safety: 30`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 47.136
  * `Choke Point (Betweenness):` 0.000329 | `Ripple Effect (Closeness):` 0.115184
  * `Imports (Out-Degree: 2):` , ._typing, .completion, .utils, click, click.core, click.formatting, click.shell_completion...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `typer-0.24.1/typer/rich_utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 584.4 | **LOC:** 754 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **25**; blast radius 1.139; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (62.7%)
- **Documentation Coverage:** 70.2703% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_print_options_panel` **(Many-Argument Workhorses)** (Impact: 64.2)
  * `rich_format_help` **(Many-Argument Workhorses)** (Impact: 55.0)
  * `_get_parameter_help` **(Many-Argument Workhorses)** (Impact: 50.4)
  * `_print_commands_panel` **(Many-Argument Workhorses)** (Impact: 30.6)
  * `_get_help_text` **(Stateful Encapsulated Methods)** (Impact: 12.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 308
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 87`, `args: 15`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 142`, `dead_code: 1`
* *Architecture:* `api: 10`, `import: 24`
* *Defense:* `safety: 10`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.139
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.001742
  * `Imports (Out-Degree: 2):` .core, click, collections, collections.abc, gettext, here, inspect, io...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `typer-0.24.1/typer/cli.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 372.18 | **LOC:** 318 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 1.738; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_docs_for_click` **(Many-Argument Workhorses)** (Impact: 80.8)
  * `get_typer_from_module` **(Defensive Guards)** (Impact: 22.1)
    * *Intent:* # Try to get defined app if state.app: obj = getattr(module, state.app, None) if not isinstance(obj,...
  * `docs` **(Many-Argument Workhorses)** (Impact: 21.9)
  * `maybe_update_state` **(Compute Cores)** (Impact: 13.7)
  * `maybe_add_run_to_cli` **(Compute Cores)** (Impact: 9.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 56 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 170
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 57`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 3`, `state_mutation: 58`
* *Architecture:* `io: 4`, `api: 16`, `import: 12`
* *Defense:* `safety: 11`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.738
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.001742
  * `Imports (Out-Degree: 1):` , .core, as, click, importlib.util, pathlib, re, sys...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `typer-0.24.1/typer/models.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 232.74 | **LOC:** 652 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **10**; blast radius 30.951; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (94.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (65.4%)
- **Documentation Coverage:** 87.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 40.2)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 29.9)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 11.2)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 6.6)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 59`, `args: 11`, `func_start: 11`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 86`, `planned_debt: 4`
* *Architecture:* `api: 18`, `import: 9`
* *Defense:* `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.951
  * `Choke Point (Betweenness):` 6.8e-05 | `Ripple Effect (Closeness):` 0.10971
  * `Imports (Out-Degree: 1):` .core, .main, click, click.shell_completion, collections.abc, inspect, io, typer...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `typer-0.24.1/tests/test_rich_markup_mode.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 191.16 | **LOC:** 333 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.939; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.0%), Complexity Load (formerly Cognitive Load) (20.1%), Connectivity (formerly Api Exposure) (9.8%)
- **Documentation Coverage:** 56.25% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_markup_mode_newline_mixed` **(Defensive Guards)** (Impact: 15.4)
  * `test_markup_mode_newline_pr815` **(Defensive Guards)** (Impact: 11.8)
  * `test_markup_mode_bullets_double_newline` **(Defensive Guards)** (Impact: 11.8)
  * `test_markup_mode_newline_issue447` **(Defensive Guards)** (Impact: 11.7)
  * `test_markup_mode_bullets_single_newline` **(Defensive Guards)** (Impact: 11.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 22 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 58`, `args: 16`, `func_start: 16`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 40`, `duplicate_logic: 7`, `unreferenced_by_name: 9`
* *Architecture:* `io: 1`, `api: 16`, `import: 7`
* *Defense:* `safety: 34`, `doc: 7`, `test: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` os, pytest, subprocess, sys, typer, typer.completion, typer.testing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/typer/_completion_classes.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 183.12 | **LOC:** 200 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 9.264; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (98.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `complete` **(Compute Cores)** (Impact: 10.7)
  * `get_completion_args` **(Generic / Templated Code)** (Impact: 6.2)
  * `get_completion_args` **(Generic / Templated Code)** (Impact: 6.2)
  * `complete` **(Generic / Templated Code)** (Impact: 6.1)
  * `format_completion` **(Generic / Templated Code)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 60`, `args: 18`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 38`, `dead_code: 5`, `planned_debt: 3`, `duplicate_logic: 6`
* *Architecture:* `io: 7`, `api: 21`, `import: 11`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.264
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.083545
  * `Imports (Out-Degree: 1):` , ._completion_shared, click, click.parser, click.shell_completion, importlib.util, os, re...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `typer-0.24.1/tests/test_others.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 179.22 | **LOC:** 340 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.939; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (33.8%), Complexity Load (formerly Cognitive Load) (17.2%), Connectivity (formerly Api Exposure) (12.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `names_callback` **(Generic / Templated Code)** (Impact: 6.2)
  * `test_callback_4_list_none` **(Annotated & Test Methods)** (Impact: 6.1)
  * `main` **(Generic / Templated Code)** (Impact: 4.6)
  * `test_too_many_parsers` **(Type Conversions)** (Impact: 4.1)
  * `test_forward_references` **(Annotated & Test Methods)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 140`, `args: 39`, `func_start: 39`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 5`, `state_mutation: 36`, `duplicate_logic: 6`, `unreferenced_by_name: 18`
* *Architecture:* `io: 6`, `api: 41`, `import: 17`
* *Defense:* `safety: 43`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` .utils, click, os, pathlib, pytest, subprocess, sys, typer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/typer/_completion_shared.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 165.82 | **LOC:** 253 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **7**; blast radius 18.575; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.8%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 92.3077% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `install` **(Many-Argument Workhorses)** (Impact: 21.8)
  * `install_powershell` **(Defensive Guards)** (Impact: 14.1)
  * `install_zsh` **(Many-Argument Workhorses)** (Impact: 9.3)
    * *Intent:* # Setup Zsh and load ~/.zfunc zshrc_path = Path.home() / ".zshrc" zshrc_path.parent.mkdir(parents=Tr...
  * `install_bash` **(Many-Argument Workhorses)** (Impact: 9.2)
    * *Intent:* # Ref: https://github.com/scop/bash-completion#faq # It seems bash-completion is the official comple...
  * `get_completion_script` **(Generic / Templated Code)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 24 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 32`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 44`, `planned_debt: 2`
* *Architecture:* `io: 3`, `api: 7`, `import: 7`
* *Defense:* `safety: 7`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.575
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.087814
  * `Imports (Out-Degree: 0):` click, enum, os, pathlib, re, shellingham, subprocess
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `typer-0.24.1/typer/utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 135.3 | **LOC:** 198 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 1.339; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.9%), Debt Markers (formerly Tech Debt) (80.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_params_from_function` **(Compute Cores)** (Impact: 25.2)
  * `__str__` **(Generic / Templated Code)** (Impact: 7.6)
  * `parse_boolean_env_var` **(Generic / Templated Code)** (Impact: 7.4)
  * `_split_annotation_from_typer_annotations` **(Stateful Encapsulated Methods)** (Impact: 6.2)
  * `_param_type_to_user_string` **(Encapsulated Accessors)** (Impact: 4.7)
    * *Intent:* # Render a `ParameterInfo` subclass for use in error messages. # User code doesn't call `*Info` dire...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 58`, `args: 12`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 28`, `duplicate_logic: 2`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.339
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.001742
  * `Imports (Out-Degree: 2):` ._typing, .models, collections.abc, copy, inspect, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `typer-0.24.1/tests/test_type_conversion.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 122.4 | **LOC:** 171 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.939; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.9%), Complexity Load (formerly Cognitive Load) (28.2%), Connectivity (formerly Api Exposure) (11.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `opt` **(Compute Cores)** (Impact: 4.5)
  * `opt` **(Compute Cores)** (Impact: 4.5)
  * `opt` **(Generic / Templated Code)** (Impact: 4.5)
  * `test_optional` **(Defensive Guards)** (Impact: 3.9)
  * `test_union_type_optional` **(Defensive Guards)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 55`, `args: 17`, `func_start: 17`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 26`, `duplicate_logic: 2`, `unreferenced_by_name: 14`
* *Architecture:* `io: 1`, `api: 19`, `import: 7`
* *Defense:* `safety: 28`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` click, enum, pathlib, pytest, typer, typer.testing, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_rich_utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 116.18 | **LOC:** 225 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.939; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (28.3%), Complexity Load (formerly Cognitive Load) (25.3%), Connectivity (formerly Api Exposure) (10.5%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_help_table_alignment_with_styled_text` **(Defensive Guards)** (Impact: 10.2)
  * `test_rich_markup_import_regression` **(Annotated & Test Methods)** (Impact: 3.8)
    * *Intent:* # Remove rich.markup if it was imported by other tests if "rich" in sys.modules: rich_module = sys.m...
  * `test_metavar_highlighter` **(Type Conversions)** (Impact: 2.8)
    * *Intent:* """ Test that the MetavarHighlighter works correctly. cf PR 1508 """
  * `main` **(Parameter Forwarders)** (Impact: 2.6)
  * `test_rich_utils_click_rewrapp` **(Annotated & Test Methods)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 71`, `args: 16`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 38`, `unreferenced_by_name: 8`
* *Architecture:* `io: 2`, `api: 16`, `import: 8`
* *Defense:* `safety: 42`, `doc: 6`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` pytest, sys, tests.utils, typer, typer.completion, typer.rich_utils, typer.testing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/typer/params.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 113.26 | **LOC:** 1832 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 8.865; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (31.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Option` **(Many-Argument Workhorses)** (Impact: 31.2)
    * *Intent:* # Parameter default: Annotated[ Any | None, Doc( """
  * `Argument` **(Many-Argument Workhorses)** (Impact: 26.0)
    * *Intent:* # Parameter default: Annotated[ Any | None, Doc( """
  * `Option` **(Many-Argument Workhorses)** (Impact: 9.7)
    * *Intent:* # Overload for Option created with custom type 'parser' # Parameter default: Any | None = ..., *para...
  * `Option` **(Many-Argument Workhorses)** (Impact: 9.7)
    * *Intent:* # Overload for Option created with custom type 'click_type' # Parameter default: Any | None = ..., *...
  * `Argument` **(Many-Argument Workhorses)** (Impact: 8.5)
    * *Intent:* # Overload for Argument created with custom type 'parser' # Parameter default: Any | None = ..., *, ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 30`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 38`, `planned_debt: 9`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `doc: 81`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.082675
  * `Imports (Out-Degree: 1):` .models, annotated_doc, click, click.shell_completion, collections.abc, datetime, enum, pathlib...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `typer-0.24.1/typer/completion.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 102.88 | **LOC:** 147 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **11**; blast radius 35.44; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `shell_complete` **(Many-Argument Workhorses)** (Impact: 14.3)
    * *Intent:* # Re-implement Click's shell_complete to add error message with: # Invalid completion instruction # ...
  * `show_callback` **(Defensive Guards)** (Impact: 12.9)
  * `install_callback` **(Defensive Guards)** (Impact: 10.5)
  * `_install_completion_placeholder_function` **(Stateful Encapsulated Methods)** (Impact: 7.8)
    * *Intent:* # Create a fake command function to extract the completion parameters
  * `_install_completion_no_auto_placeholder_function` **(Stateful Encapsulated Methods)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 36`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 2`, `state_mutation: 14`
* *Architecture:* `io: 4`, `api: 4`, `import: 12`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 35.44
  * `Choke Point (Betweenness):` 0.001645 | `Ripple Effect (Closeness):` 0.11055
  * `Imports (Out-Degree: 4):` ._completion_classes, ._completion_shared, .models, .params, .utils, click, click.shell_completion, collections.abc...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `typer-0.24.1/tests/test_tutorial/test_subcommands/test_tutorial003.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 83.82 | **LOC:** 179 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.939; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (21.8%), Connectivity (formerly Api Exposure) (11.3%), Guard Balance (formerly Safety Score) (1.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_scripts` **(Type Conversions)** (Impact: 3.8)
  * `test_help` **(Defensive Guards)** (Impact: 1.8)
  * `test_help_items` **(Defensive Guards)** (Impact: 1.8)
  * `test_items_create` **(Defensive Guards)** (Impact: 1.8)
  * `test_items_sell` **(Defensive Guards)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 98`, `args: 18`, `func_start: 18`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 24`, `unreferenced_by_name: 16`
* *Architecture:* `io: 1`, `api: 18`, `import: 9`
* *Defense:* `safety: 62`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` docs_src.subcommands, docs_src.subcommands.tutorial003_py310, os, pytest, subprocess, sys, typer.testing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_ambiguous_params.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 72.6 | **LOC:** 233 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.939; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (27.7%), Connectivity (formerly Api Exposure) (11.3%), Dead Code Surface (formerly Dead Code) (6.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_forbid_default_factory_and_default_value_in_annotated` **(Annotated & Test Methods)** (Impact: 2.6)
  * `test_forbid_default_and_default_factory_with_default_param` **(Annotated & Test Methods)** (Impact: 2.6)
  * `test_forbid_annotated_param_and_default_param` **(Annotated & Test Methods)** (Impact: 2.4)
  * `test_allow_default_factory_with_default_param` **(Annotated & Test Methods)** (Impact: 2.1)
  * `test_forbid_default_value_in_annotated_argument` **(Annotated & Test Methods)** (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 58`, `args: 21`, `func_start: 21`
* *Risk/State:* `state_mutation: 13`, `dead_code: 1`, `duplicate_logic: 3`, `unreferenced_by_name: 10`
* *Architecture:* `api: 21`, `import: 5`
* *Defense:* `safety: 14`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pytest, typer, typer.testing, typer.utils, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_completion/test_completion_install.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 68.46 | **LOC:** 174 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.939; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (64.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (16.9%), Connectivity (formerly Api Exposure) (6.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_completion_install_zsh` **(I/O & Config Routines)** (Impact: 4.9)
  * `test_completion_install_bash` **(Defensive Guards)** (Impact: 3.9)
  * `test_completion_install_powershell` **(Defensive Guards)** (Impact: 3.5)
  * `test_completion_install_fish` **(I/O & Config Routines)** (Impact: 2.4)
  * `test_completion_install_no_shell` **(Interface Declarations)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 9 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 41`, `args: 5`, `func_start: 5`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 26`, `unreferenced_by_name: 5`
* *Architecture:* `io: 5`, `api: 5`, `import: 9`
* *Defense:* `safety: 19`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ..utils, docs_src.typer_app, os, pathlib, shellingham, subprocess, sys, typer.testing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_annotated.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 61.14 | **LOC:** 98 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.939; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (38.5%), Guard Balance (formerly Safety Score) (26.2%), Connectivity (formerly Api Exposure) (11.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cmd` **(Compute Cores)** (Impact: 4.5)
  * `test_annotated_option_with_argname_doesnt_mutate_multiple_calls` **(Defensive Guards)** (Impact: 3.9)
  * `test_annotated_custom_path` **(Annotated & Test Methods)** (Impact: 2.9)
  * `test_annotated_argument_with_default_factory` **(Annotated & Test Methods)** (Impact: 1.9)
  * `test_annotated_argument_with_default` **(Annotated & Test Methods)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 40`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`, `unreferenced_by_name: 6`
* *Architecture:* `io: 2`, `api: 12`, `import: 5`
* *Defense:* `safety: 19`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pathlib, sys, typer, typer.testing, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_completion/test_completion_complete.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 59.44 | **LOC:** 188 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.939; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (41.5%), Connectivity (formerly Api Exposure) (9.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_completion_complete_subcommand_fish` **(Defensive Guards)** (Impact: 2.3)
  * `test_completion_complete_subcommand_bash` **(Defensive Guards)** (Impact: 2.2)
  * `test_completion_complete_subcommand_zsh` **(Defensive Guards)** (Impact: 2.2)
  * `test_completion_complete_subcommand_powershell` **(Defensive Guards)** (Impact: 2.2)
  * `test_completion_complete_subcommand_pwsh` **(Defensive Guards)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 10 instances
* *High Risk Execution (weighted view):* 0
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 42`, `args: 11`, `func_start: 11`
* *Risk/State:* `high_risk_execution: 10`, `state_mutation: 22`, `unreferenced_by_name: 11`
* *Architecture:* `io: 11`, `api: 11`, `import: 8`
* *Defense:* `safety: 10`, `doc: 2`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` importlib, os, pathlib, pytest, subprocess, sys, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_tutorial/test_commands/test_help/test_tutorial001.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 53.76 | **LOC:** 122 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.939; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (28.5%), Connectivity (formerly Api Exposure) (11.0%), Guard Balance (formerly Safety Score) (0.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_help_delete_all` **(Defensive Guards)** (Impact: 3.3)
  * `test_help` **(Defensive Guards)** (Impact: 2.0)
  * `test_help_delete` **(Defensive Guards)** (Impact: 1.8)
  * `test_script` **(Defensive Guards)** (Impact: 1.8)
  * `test_help_create` **(Defensive Guards)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *High Risk Execution (weighted view):* 0
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 73`, `args: 13`, `func_start: 13`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 15`, `unreferenced_by_name: 13`
* *Architecture:* `io: 1`, `api: 13`, `import: 7`
* *Defense:* `safety: 47`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` importlib, pytest, subprocess, sys, typer.testing, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_completion/test_completion_option_colon.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 52.46 | **LOC:** 220 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.939; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (11.1%), Connectivity (formerly Api Exposure) (9.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_completion_colon_bash_all` **(Defensive Guards)** (Impact: 1.8)
  * `test_completion_colon_bash_partial` **(Defensive Guards)** (Impact: 1.8)
  * `test_completion_colon_bash_single` **(Defensive Guards)** (Impact: 1.8)
  * `test_completion_colon_powershell_all` **(Defensive Guards)** (Impact: 1.8)
  * `test_completion_colon_powershell_partial` **(Defensive Guards)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 13 instances
* *High Risk Execution (weighted view):* 0
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 57`, `args: 13`, `func_start: 13`
* *Risk/State:* `high_risk_execution: 13`, `state_mutation: 13`, `planned_debt: 1`, `unreferenced_by_name: 13`
* *Architecture:* `io: 13`, `api: 13`, `import: 4`
* *Defense:* `safety: 38`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , os, subprocess, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_tutorial/test_subcommands/test_tutorial001.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 50.52 | **LOC:** 100 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.939; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (25.4%), Connectivity (formerly Api Exposure) (10.8%), Guard Balance (formerly Safety Score) (4.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_scripts` **(Type Conversions)** (Impact: 3.5)
  * `test_help` **(Defensive Guards)** (Impact: 1.8)
  * `test_help_items` **(Defensive Guards)** (Impact: 1.8)
  * `test_help_users` **(Defensive Guards)** (Impact: 1.8)
  * `mod` **(Type Conversions)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 54`, `args: 11`, `func_start: 11`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 12`, `unreferenced_by_name: 9`
* *Architecture:* `io: 1`, `api: 11`, `import: 8`
* *Defense:* `safety: 28`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` docs_src.subcommands, docs_src.subcommands.tutorial001_py310, os, pytest, subprocess, sys, typer.testing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_suggest_commands.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 49.62 | **LOC:** 99 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.939; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (15.8%), Connectivity (formerly Api Exposure) (12.0%), Complexity Load (formerly Cognitive Load) (7.9%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_typo_suggestion_multiple_matches` **(Annotated & Test Methods)** (Impact: 2.9)
    * *Intent:* """Test that multiple suggestions are shown when there are multiple close matches"""
  * `test_typo_suggestion_exact_match_works` **(Annotated & Test Methods)** (Impact: 2.0)
    * *Intent:* """Test that exact matches still work normally"""
  * `test_typo_suggestion_enabled` **(Annotated & Test Methods)** (Impact: 1.8)
    * *Intent:* """Test that typo suggestions work when enabled"""
  * `test_typo_suggestion_no_matches` **(Annotated & Test Methods)** (Impact: 1.8)
    * *Intent:* """Test that no suggestions are shown when there are no close matches"""
  * `test_typo_suggestion_disabled` **(Annotated & Test Methods)** (Impact: 1.8)
    * *Intent:* """Test that typo suggestions can be explicitly disabled"""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 35`, `args: 15`, `func_start: 15`
* *Risk/State:* `state_mutation: 12`, `duplicate_logic: 9`, `unreferenced_by_name: 5`
* *Architecture:* `api: 15`, `import: 2`
* *Defense:* `safety: 17`, `doc: 5`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` typer, typer.testing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_completion/test_completion.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 49.58 | **LOC:** 167 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.939; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (36.6%), Complexity Load (formerly Cognitive Load) (9.7%), Connectivity (formerly Api Exposure) (9.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_install_completion` **(Defensive Guards)** (Impact: 3.0)
  * `test_completion_source_bash` **(I/O & Config Routines)** (Impact: 1.7)
  * `test_completion_source_powershell` **(I/O & Config Routines)** (Impact: 1.7)
  * `test_completion_source_pwsh` **(I/O & Config Routines)** (Impact: 1.7)
  * `test_show_completion` **(I/O & Config Routines)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 10 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 34`, `args: 10`, `func_start: 10`
* *Risk/State:* `high_risk_execution: 10`, `state_mutation: 13`, `fragile_debt: 1`, `unreferenced_by_name: 10`
* *Architecture:* `io: 11`, `api: 10`, `import: 6`
* *Defense:* `safety: 14`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ..utils, docs_src.typer_app, os, pathlib, subprocess, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_tutorial/test_parameter_types/test_number/test_tutorial001.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 48.12 | **LOC:** 92 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.939; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (45.4%), Connectivity (formerly Api Exposure) (10.2%), Guard Balance (formerly Safety Score) (3.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_invalid_score` **(Defensive Guards)** (Impact: 3.8)
  * `test_invalid_id` **(Defensive Guards)** (Impact: 3.1)
  * `test_invalid_age` **(Defensive Guards)** (Impact: 3.1)
  * `test_help_no_rich` **(Defensive Guards)** (Impact: 2.1)
  * `test_help` **(Defensive Guards)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 47`, `args: 9`, `func_start: 9`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 11`, `unreferenced_by_name: 9`
* *Architecture:* `io: 1`, `api: 9`, `import: 9`
* *Defense:* `safety: 27`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` importlib, pytest, subprocess, sys, typer, typer.core, typer.testing, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `typer-0.24.1/typer/main.py` -> **Severity: 0.482** (Bridge: 0.0048 * Flux: 99.9997%)
- `typer-0.24.1/typer/completion.py` -> **Severity: 0.164** (Bridge: 0.0016 * Flux: 99.9995%)
- `typer-0.24.1/typer/testing.py` -> **Severity: 0.089** (Bridge: 0.0053 * Flux: 16.7982%)
- `typer-0.24.1/typer/core.py` -> **Severity: 0.033** (Bridge: 0.0003 * Flux: 100.0%)
- `typer-0.24.1/typer/models.py` -> **Severity: 0.007** (Bridge: 0.0001 * Flux: 99.9331%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `typer-0.24.1/typer/testing.py` -> **Severity: 22.63** (Embedded: 0.2945 * Error Risk: 76.8525%)
- `typer-0.24.1/typer/main.py` -> **Severity: 14.342** (Embedded: 0.1498 * Error Risk: 95.7223%)
- `typer-0.24.1/typer/core.py` -> **Severity: 11.151** (Embedded: 0.1152 * Error Risk: 96.8091%)
- `typer-0.24.1/typer/_typing.py` -> **Severity: 10.822** (Embedded: 0.1099 * Error Risk: 98.4974%)
- `typer-0.24.1/typer/completion.py` -> **Severity: 10.606** (Embedded: 0.1105 * Error Risk: 95.941%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `typer-0.24.1/typer/testing.py` -> **Severity: 12415.4** (Blast Radius: 124.154 * Doc Risk: 100.0%)
- `typer-0.24.1/typer/main.py` -> **Severity: 10649.4** (Blast Radius: 106.494 * Doc Risk: 100.0%)
- `typer-0.24.1/typer/core.py` -> **Severity: 4525.056** (Blast Radius: 47.136 * Doc Risk: 96.0%)
- `typer-0.24.1/typer/completion.py` -> **Severity: 3544.0** (Blast Radius: 35.44 * Doc Risk: 100.0%)
- `typer-0.24.1/typer/_typing.py` -> **Severity: 2873.249** (Blast Radius: 34.479 * Doc Risk: 83.3333%)

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
