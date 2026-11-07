# ARCHITECTURAL_BRIEF: click
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
- **Scope:** 50 analyzed artifact(s), 13663 LOC.
- **Load-bearing artifact:** `click-8.3.2/src/click/core.py` -- 33 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `click-8.3.2/src/click/core.py` -- pulls in 26 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `click-8.3.2/src/click/core.py` at magnitude 2817.06 (structural weight, not risk).
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
| Total Artifacts | 55 |
| Analyzed Artifacts (Scanned) | 50 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 13663 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 90.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.211 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1666 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 26.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9633 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 48 | 13663 | 96.0% |
| PLAINTEXT | 1 | 0 | 2.0% |
| MARKDOWN | 1 | 0 | 2.0% |

## 4.1 SOURCE ENCODINGS
All 50 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 36%, Large Core Modules (2) 20%, Data / Markup / Trivial 16%, Large Core Modules (3) 14%, Interface Declarations Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 48 | 96.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 4.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 87.9 | 23.8 | 13.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 83.2 | 45.9 | 46.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 59.5 | 3.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 16.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 3.2 | 74.9 | 23.1 | 12.7 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 98.8 | 6.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 33.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 7.3 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 82.6 | 93.5 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 157 | 23 | 11 | `click-8.3.2/src/click/core.py` |
| cleanup | 19 | 7 | 2 | `click-8.3.2/src/click/_termui_impl.py` |
| guards | 1532 | 37 | 85 | `click-8.3.2/tests/test_options.py` |
| danger | 702 | 37 | 29 | `click-8.3.2/src/click/core.py` |
| concurrency | 59 | 14 | 6 | `click-8.3.2/tests/test_stream_lifecycle.py` |
| connectivity | 1323 | 48 | 66 | `click-8.3.2/tests/test_options.py` |
| io | 268 | 20 | 27 | `click-8.3.2/src/click/_compat.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 22 | 4 | 0 | `click-8.3.2/src/click/_termui_impl.py` |
| time | 7 | 3 | 0 | `click-8.3.2/src/click/_termui_impl.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 25 | 4 | 0 | `click-8.3.2/tests/test_options.py` |
| events | 90 | 8 | 6 | `click-8.3.2/src/click/core.py` |
| tests | 666 | 23 | 40 | `click-8.3.2/tests/test_options.py` |
| docs | 391 | 37 | 16 | `click-8.3.2/src/click/core.py` |
| debt | 140 | 20 | 10 | `click-8.3.2/tests/test_options.py` |
| mutation | 5007 | 41 | 211 | `click-8.3.2/src/click/core.py` |
| dead_code | 446 | 25 | 30 | `click-8.3.2/tests/test_options.py` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.97**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `click-8.3.2/src/click/_compat.py` (Hits: 43)
- `click-8.3.2/src/click/_termui_impl.py` (Hits: 33)
- `click-8.3.2/src/click/utils.py` (Hits: 31)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **core.py** (`click-8.3.2/src/click/core.py`) — 33 inbound connections
2. **utils.py** (`click-8.3.2/src/click/utils.py`) — 28 inbound connections
3. **__init__.py** (`click-8.3.2/src/click/__init__.py`) — 24 inbound connections
4. **decorators.py** (`click-8.3.2/src/click/decorators.py`) — 21 inbound connections
5. **types.py** (`click-8.3.2/src/click/types.py`) — 13 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **core.py** (`click-8.3.2/src/click/core.py`) — 26 outbound dependencies
2. **_termui_impl.py** (`click-8.3.2/src/click/_termui_impl.py`) — 25 outbound dependencies
3. **types.py** (`click-8.3.2/src/click/types.py`) — 18 outbound dependencies
4. **test_utils.py** (`click-8.3.2/tests/test_utils.py`) — 18 outbound dependencies
5. **testing.py** (`click-8.3.2/src/click/testing.py`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` **(Many-Argument Workhorses)** (@ `click-8.3.2/src/click/core.py`) -> Impact: **244.9** | LOC: 157
- `__init__` **(Many-Argument Workhorses)** (@ `click-8.3.2/src/click/core.py`) -> Impact: **140.0** | LOC: 169
- `style` **(Many-Argument Workhorses)** (@ `click-8.3.2/src/click/termui.py`) -> Impact: **110.9** | LOC: 127
- `prompt` **(Many-Argument Workhorses)** (@ `click-8.3.2/src/click/termui.py`) -> Impact: **75.2** | LOC: 112
- `get_help_extra` **(Many-Argument Workhorses)** (@ `click-8.3.2/src/click/core.py`) -> Impact: **70.0** | LOC: 83
- `version_option` **(Many-Argument Workhorses)** (@ `click-8.3.2/src/click/decorators.py`) -> Impact: **58.1** | LOC: 104
- `open_stream` **(Many-Argument Workhorses)** (@ `click-8.3.2/src/click/_compat.py`) -> Impact: **57.8** | LOC: 79
- `echo` **(Many-Argument Workhorses)** (@ `click-8.3.2/src/click/utils.py`) -> Impact: **54.0** | LOC: 101
- `__init__` **(Many-Argument Workhorses)** (@ `click-8.3.2/src/click/core.py`) -> Impact: **53.8** | LOC: 70
- `consume_value` **(Many-Argument Workhorses)** (@ `click-8.3.2/src/click/core.py`) -> Impact: **49.1** | LOC: 63

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `click-8.3.2/src/click` | 17 | 8064.9 | 49.05% | 10.84% |
| `click-8.3.2/tests` | 22 | 4427.28 | 13.29% | 0.0% |
| `click-8.3.2/tests/typing` | 9 | 60.88 | 1.82% | 0.0% |
| `click-8.3.2` | 2 | 2.26 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `click-8.3.2/src/click/shell_completion.py` -> **59.4986%** Exposure
- `click-8.3.2/src/click/decorators.py` -> **34.4961%** Exposure
- `click-8.3.2/src/click/types.py` -> **23.8538%** Exposure
- `click-8.3.2/src/click/_winconsole.py` -> **13.7491%** Exposure
- `click-8.3.2/src/click/core.py` -> **13.6666%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `click-8.3.2/src/click/_termui_impl.py` -> **100.0%** Exposure
- `click-8.3.2/src/click/_textwrap.py` -> **100.0%** Exposure
- `click-8.3.2/src/click/core.py` -> **100.0%** Exposure
- `click-8.3.2/src/click/decorators.py` -> **100.0%** Exposure
- `click-8.3.2/src/click/exceptions.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `click-8.3.2/tests/test_options.py` -> **88** Orphaned Functions | **26** Duplicates
- `click-8.3.2/tests/test_basic.py` -> **34** Orphaned Functions | **11** Duplicates
- `click-8.3.2/tests/test_context.py` -> **26** Orphaned Functions | **17** Duplicates
- `click-8.3.2/tests/test_arguments.py` -> **32** Orphaned Functions | **6** Duplicates
- `click-8.3.2/tests/test_commands.py` -> **28** Orphaned Functions | **9** Duplicates

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
- **Unknown Dependencies:** `287` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `click-8.3.2/src/click/core.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.739)
- **Top Global Matches:** file_cluster_5: 8.739, file_cluster_12: 11.767, file_cluster_7: 12.012
- **Magnitude:** 2817.06 | **LOC:** 3438 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **33** in-repo importer(s); it depends on **26**; blast radius 111.39; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (73.7%)
- **Documentation Coverage:** 56.5543% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 244.9)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 140.0)
  * `get_help_extra` **(Many-Argument Workhorses)** (Impact: 70.0)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 53.8)
  * `consume_value` **(Many-Argument Workhorses)** (Impact: 49.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 322 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 1016
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 509`, `structural_boundaries: 489`, `args: 142`, `func_start: 140`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 150`, `high_risk_execution: 5`, `state_mutation: 372`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 12`, `api: 127`, `import: 54`
* *Defense:* `safety: 51`, `doc: 86`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 111.39
  * `Choke Point (Betweenness):` 0.100248 | `Ripple Effect (Closeness):` 0.686122
  * `Imports (Out-Degree: 10):` ._utils, .decorators, .exceptions, .formatting, .globals, .parser, .shell_completion, .termui...
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `click-8.3.2/tests/test_options.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.404)
- **Top Global Matches:** file_cluster_12: 7.404, file_cluster_15: 8.747, file_cluster_13: 9.175
- **Magnitude:** 923.98 | **LOC:** 2504 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 3.585; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.2%), Connectivity (formerly Api Exposure) (13.1%), Complexity Load (formerly Cognitive Load) (9.7%)
- **Documentation Coverage:** 84.7352% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_dual_options_custom_type_sentinel_flag_value` **(Many-Argument Workhorses)** (Impact: 28.8)
    * *Intent:* """Check that an object-based sentinel, used as a flag value, is returned as-is to a custom type tha...
  * `test_bad_defaults_for_multiple` **(Defensive Guards)** (Impact: 16.9)
  * `test_choice_usage_rendering` **(Defensive Guards)** (Impact: 14.2)
    * *Intent:* """BY default ``--help`` prints choice's values in the usage message. But ``show_choices=False`` mak...
  * `test_custom_type_flag_value_dual_options` **(Defensive Guards)** (Impact: 10.9)
  * `test_custom_type_flag_value_standalone_option` **(Defensive Guards)** (Impact: 9.8)
    * *Intent:* """Test how the type and flag_value influence the returned value. Cover cases reported in: https://g...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 248
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 644`, `args: 166`, `func_start: 162`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 174`, `duplicate_logic: 26`, `unreferenced_by_name: 88`
* *Architecture:* `io: 2`, `api: 174`, `import: 13`
* *Defense:* `safety: 225`, `doc: 31`, `test: 129`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.585
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` click, click._utils, click.testing, contextlib, enum, os, pytest, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/src/click/_termui_impl.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.546)
- **Top Global Matches:** file_cluster_5: 8.546, file_cluster_12: 8.909, file_cluster_4: 10.144
- **Magnitude:** 791.16 | **LOC:** 853 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **25**; blast radius 8.934; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.7%), Complexity Load (formerly Cognitive Load) (65.5%)
- **Documentation Coverage:** 90.7692% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `open_url` **(Many-Argument Workhorses)** (Impact: 43.5)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 41.7)
  * `_pipepager` **(Many-Argument Workhorses)** (Impact: 28.7)
  * `pager` **(Defensive Guards)** (Impact: 26.2)
    * *Intent:* """Decide what method to use for paging through text."""
  * `edit` **(Defensive Guards)** (Impact: 21.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Cascading Flux:* 128 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 403
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 176`, `args: 36`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 8`, `state_mutation: 147`, `planned_debt: 1`
* *Architecture:* `io: 33`, `api: 31`, `import: 40`
* *Defense:* `safety: 31`, `doc: 7`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.934
  * `Choke Point (Betweenness):` 0.002268 | `Ripple Effect (Closeness):` 0.309064
  * `Imports (Out-Degree: 3):` ._compat, .exceptions, .utils, __future__, collections.abc, contextlib, gettext, io...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `click-8.3.2/src/click/types.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.744)
- **Top Global Matches:** file_cluster_5: 6.744, file_cluster_12: 9.921, file_cluster_7: 10.451
- **Magnitude:** 731.24 | **LOC:** 1210 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **18**; blast radius 23.292; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.9%), Guard Balance (formerly Safety Score) (70.4%)
- **Documentation Coverage:** 81.6514% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convert` **(Many-Argument Workhorses)** (Impact: 39.4)
  * `convert_type` **(Defensive Guards)** (Impact: 34.1)
    * *Intent:* """Find the most appropriate :class:`ParamType` for the given Python type. If the type isn't provide...
  * `convert` **(Many-Argument Workhorses)** (Impact: 28.3)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 21.3)
  * `shell_complete` **(Many-Argument Workhorses)** (Impact: 19.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 234
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 233`, `args: 66`, `func_start: 66`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 110`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 29`, `api: 59`, `import: 25`
* *Defense:* `safety: 36`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.292
  * `Choke Point (Betweenness):` 0.010282 | `Ripple Effect (Closeness):` 0.451396
  * `Imports (Out-Degree: 5):` ._compat, .core, .exceptions, .shell_completion, .utils, __future__, click.shell_completion, collections.abc...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `click-8.3.2/src/click/termui.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.084)
- **Top Global Matches:** file_cluster_4: 10.084, file_cluster_5: 10.585, file_cluster_12: 11.921
- **Magnitude:** 509.46 | **LOC:** 884 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **16**; blast radius 18.038; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.8%), Complexity Load (formerly Cognitive Load) (61.6%)
- **Documentation Coverage:** 77.2727% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `style` **(Many-Argument Workhorses)** (Impact: 110.9)
  * `prompt` **(Many-Argument Workhorses)** (Impact: 75.2)
  * `confirm` **(Many-Argument Workhorses)** (Impact: 37.5)
  * `_build_prompt` **(Stateful Encapsulated Methods)** (Impact: 16.6)
  * `echo_via_pager` **(Type Conversions)** (Impact: 13.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 119`, `args: 23`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 46`, `fragile_debt: 1`
* *Architecture:* `io: 3`, `api: 20`, `import: 27`
* *Defense:* `safety: 21`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.038
  * `Choke Point (Betweenness):` 0.020755 | `Ripple Effect (Closeness):` 0.423532
  * `Imports (Out-Degree: 6):` ._compat, ._termui_impl, .exceptions, .globals, .types, .utils, __future__, collections.abc...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `click-8.3.2/src/click/parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.072)
- **Top Global Matches:** file_cluster_5: 7.072, file_cluster_12: 9.165, file_cluster_7: 10.646
- **Magnitude:** 484.26 | **LOC:** 533 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **11**; blast radius 20.438; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (61.3%)
- **Documentation Coverage:** 93.1034% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_value_from_state` **(Many-Argument Workhorses)** (Impact: 26.5)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 24.2)
  * `_unpack_args` **(Stateful Encapsulated Methods)** (Impact: 23.7)
  * `_match_short_opt` **(Stateful Encapsulated Methods)** (Impact: 21.9)
  * `process` **(Defensive Guards)** (Impact: 15.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 78 instances
* *State Mutation (weighted view):* 246
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 92`, `args: 21`, `func_start: 21`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 90`, `planned_debt: 3`
* *Architecture:* `api: 7`, `import: 21`
* *Defense:* `safety: 9`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.438
  * `Choke Point (Betweenness):` 0.005789 | `Ripple Effect (Closeness):` 0.408406
  * `Imports (Out-Degree: 4):` ._utils, .core, .exceptions, .shell_completion, __future__, collections, collections.abc, difflib...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `click-8.3.2/src/click/_compat.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.036)
- **Top Global Matches:** file_cluster_5: 8.036, file_cluster_7: 11.058, file_cluster_12: 11.727
- **Magnitude:** 418.8 | **LOC:** 623 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **15**; blast radius 211.879; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (75.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 87.9121% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `open_stream` **(Many-Argument Workhorses)** (Impact: 57.8)
  * `_force_correct_text_stream` **(Many-Argument Workhorses)** (Impact: 24.8)
  * `_make_text_stream` **(Stateful Encapsulated Methods)** (Impact: 8.3)
  * `should_strip_ansi` **(Generic / Templated Code)** (Impact: 7.3)
  * `_find_binary_reader` **(Stateful Encapsulated Methods)** (Impact: 6.5)
    * *Intent:* # We need to figure out if the given stream is already binary. # This can happen because the officia...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 143
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 160`, `args: 52`, `func_start: 49`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 59`, `planned_debt: 1`
* *Architecture:* `io: 43`, `api: 26`, `import: 15`
* *Defense:* `safety: 22`, `doc: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 211.879
  * `Choke Point (Betweenness):` 0.018707 | `Ripple Effect (Closeness):` 0.503982
  * `Imports (Out-Degree: 1):` ._winconsole, __future__, codecs, collections.abc, colorama, errno, io, locale...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `click-8.3.2/src/click/decorators.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.899)
- **Top Global Matches:** file_cluster_5: 6.899, file_cluster_7: 11.164, file_cluster_12: 11.167
- **Magnitude:** 417.78 | **LOC:** 552 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **10**; blast radius 26.069; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (77.5%), Connectivity (formerly Api Exposure) (66.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 81.8182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `version_option` **(Many-Argument Workhorses)** (Impact: 58.1)
  * `command` **(Many-Argument Workhorses)** (Impact: 32.4)
  * `callback` **(Defensive Guards)** (Impact: 17.6)
  * `decorator` **(Defensive Guards)** (Impact: 17.3)
  * `help_option` **(Generic / Templated Code)** (Impact: 9.9)
    * *Intent:* """Pre-configured ``--help`` option which immediately prints the help page and exits the program. :p...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 112`, `args: 33`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 50`, `duplicate_logic: 2`
* *Architecture:* `api: 32`, `import: 15`
* *Defense:* `safety: 11`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.069
  * `Choke Point (Betweenness):` 0.001949 | `Ripple Effect (Closeness):` 0.49719
  * `Imports (Out-Degree: 3):` .core, .globals, .utils, __future__, functools, gettext, importlib.metadata, inspect...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `click-8.3.2/src/click/testing.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 5.895)
- **Top Global Matches:** file_cluster_5: 5.895, file_cluster_12: 9.434, file_cluster_7: 9.898
- **Magnitude:** 383.5 | **LOC:** 575 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **17**; blast radius 8.325; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (75.7%), Complexity Load (formerly Cognitive Load) (55.6%), Connectivity (formerly Api Exposure) (53.0%)
- **Documentation Coverage:** 83.0508% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isolation` **(Many-Argument Workhorses)** (Impact: 36.7)
  * `invoke` **(Many-Argument Workhorses)** (Impact: 29.6)
  * `make_input_stream` **(Defensive Guards)** (Impact: 11.3)
  * `__init__` **(Generic / Templated Code)** (Impact: 5.4)
  * `isolated_filesystem` **(Defensive Guards)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 186
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 109`, `args: 34`, `func_start: 34`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 88`
* *Architecture:* `io: 27`, `api: 28`, `import: 18`
* *Defense:* `safety: 21`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.325
  * `Choke Point (Betweenness):` 0.008532 | `Ripple Effect (Closeness):` 0.102041
  * `Imports (Out-Degree: 5):` ._compat, .core, .formatting, .termui, .utils, __future__, _typeshed, collections.abc...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `click-8.3.2/src/click/utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.113)
- **Top Global Matches:** file_cluster_5: 7.113, file_cluster_12: 10.065, file_cluster_7: 10.417
- **Magnitude:** 382.56 | **LOC:** 628 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **28** in-repo importer(s); it depends on **14**; blast radius 67.789; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.6%), Connectivity (formerly Api Exposure) (54.5%)
- **Documentation Coverage:** 74.0741% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `echo` **(Many-Argument Workhorses)** (Impact: 54.0)
  * `make_default_short_help` **(Compute Cores)** (Impact: 23.2)
    * *Intent:* """Returns a condensed version of help string."""
  * `_detect_program_name` **(Many-Argument Workhorses)** (Impact: 18.2)
  * `get_app_dir` **(Many-Argument Workhorses)** (Impact: 16.4)
  * `_expand_args` **(Many-Argument Workhorses)** (Impact: 15.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 142
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 126`, `args: 31`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 50`
* *Architecture:* `io: 31`, `api: 19`, `import: 24`
* *Defense:* `safety: 14`, `doc: 16`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 67.789
  * `Choke Point (Betweenness):` 0.021407 | `Ripple Effect (Closeness):` 0.623748
  * `Imports (Out-Degree: 3):` ._compat, .exceptions, .globals, __future__, collections.abc, errno, functools, glob...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `click-8.3.2/tests/test_basic.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.012)
- **Top Global Matches:** file_cluster_12: 7.012, file_cluster_5: 9.333, file_cluster_7: 9.584
- **Magnitude:** 379.5 | **LOC:** 742 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 3.585; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (39.4%), Complexity Load (formerly Cognitive Load) (16.1%), Connectivity (formerly Api Exposure) (13.1%)
- **Documentation Coverage:** 90.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_flag_value_dual_options` **(Many-Argument Workhorses)** (Impact: 12.2)
    * *Intent:* """Check how default is processed when options compete for the same variable name. Covers the regres...
  * `test_uuid_option` **(Defensive Guards)** (Impact: 6.8)
  * `test_string_option` **(Defensive Guards)** (Impact: 6.7)
  * `test_int_option` **(Defensive Guards)** (Impact: 6.7)
  * `test_float_option` **(Defensive Guards)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 248`, `args: 76`, `func_start: 76`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 68`, `fragile_debt: 2`, `duplicate_logic: 11`, `unreferenced_by_name: 34`
* *Architecture:* `io: 9`, `api: 76`, `import: 7`
* *Defense:* `safety: 115`, `doc: 7`, `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.585
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` __future__, click, click._utils, enum, itertools, os, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/tests/test_context.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.632)
- **Top Global Matches:** file_cluster_5: 7.632, file_cluster_12: 7.799, file_cluster_0: 10.043
- **Magnitude:** 359.66 | **LOC:** 783 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 3.585; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.0%), Connectivity (formerly Api Exposure) (12.5%), Complexity Load (formerly Cognitive Load) (12.0%)
- **Documentation Coverage:** 86.014% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_hiding_of_unset_sentinel_in_callbacks` **(Annotated & Test Methods)** (Impact: 6.4)
    * *Intent:* """Fix: https://github.com/pallets/click/issues/3136"""
  * `test_no_state_leaks` **(Defensive Guards)** (Impact: 5.6)
    * *Intent:* """Demonstrate state leaks with a specific case of the generic test above. Use a logger as a real-wo...
  * `test_with_resource_nested_exception` **(Defensive Guards)** (Impact: 5.5)
  * `__exit__` **(Generic / Templated Code)** (Impact: 5.1)
  * `__exit__` **(Generic / Templated Code)** (Impact: 5.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 235`, `args: 77`, `func_start: 77`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 95`, `duplicate_logic: 17`, `unreferenced_by_name: 26`
* *Architecture:* `api: 79`, `import: 12`
* *Defense:* `safety: 81`, `doc: 13`, `test: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.585
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` click, click.core, click.decorators, contextlib, logging, pytest, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/tests/test_termui.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.126)
- **Top Global Matches:** file_cluster_12: 7.126, file_cluster_15: 8.878, file_cluster_13: 9.341
- **Magnitude:** 350.66 | **LOC:** 713 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 3.585; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.3%), Complexity Load (formerly Cognitive Load) (23.4%), Connectivity (formerly Api Exposure) (12.0%)
- **Documentation Coverage:** 97.6378% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_flag_value_prompt` **(Many-Argument Workhorses)** (Impact: 36.4)
  * `test_progressbar_item_show_func` **(Defensive Guards)** (Impact: 9.4)
    * *Intent:* """item_show_func should show the current item being yielded."""
  * `test_progressbar_length_hint` **(Defensive Guards)** (Impact: 8.3)
  * `test_progressbar_update` **(Defensive Guards)** (Impact: 8.0)
  * `test_progressbar_update_with_item_show_func` **(Defensive Guards)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 82
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 188`, `args: 72`, `func_start: 58`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 42`, `unreferenced_by_name: 35`
* *Architecture:* `io: 1`, `api: 54`, `import: 8`
* *Defense:* `safety: 59`, `doc: 4`, `test: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.585
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` click._compat, click._termui_impl, click.exceptions, platform, pytest, tempfile, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/src/click/shell_completion.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.068)
- **Top Global Matches:** file_cluster_5: 6.068, file_cluster_12: 8.563, file_cluster_0: 9.453
- **Magnitude:** 347.92 | **LOC:** 668 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **11**; blast radius 33.52; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.2%), Debt Markers (formerly Tech Debt) (59.5%)
- **Documentation Coverage:** 55.3191% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_resolve_context` **(Many-Argument Workhorses)** (Impact: 23.1)
  * `_resolve_incomplete` **(Many-Argument Workhorses)** (Impact: 22.2)
  * `_is_incomplete_option` **(Stateful Encapsulated Methods)** (Impact: 17.1)
    * *Intent:* """Determine if the given parameter is an option that needs a value. :param args: List of complete a...
  * `_check_version` **(Stateful Encapsulated Methods)** (Impact: 14.6)
  * `shell_complete` **(Many-Argument Workhorses)** (Impact: 11.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 154
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 118`, `args: 27`, `func_start: 27`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 1`, `state_mutation: 68`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 24`, `import: 17`
* *Defense:* `safety: 11`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 33.52
  * `Choke Point (Betweenness):` 0.000638 | `Ripple Effect (Closeness):` 0.408406
  * `Imports (Out-Degree: 2):` .core, .utils, __future__, collections.abc, gettext, os, re, shlex...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `click-8.3.2/tests/test_arguments.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.231)
- **Top Global Matches:** file_cluster_12: 7.231, file_cluster_13: 8.612, file_cluster_15: 8.751
- **Magnitude:** 303.76 | **LOC:** 630 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.585; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (39.8%), Complexity Load (formerly Cognitive Load) (13.8%), Connectivity (formerly Api Exposure) (13.1%)
- **Documentation Coverage:** 95.4887% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_nargs_envvar` **(Defensive Guards)** (Impact: 12.1)
  * `test_required_argument` **(Defensive Guards)** (Impact: 6.7)
    * *Intent:* """Test how a required argument is processing the provided values."""
  * `inout` **(Compute Cores)** (Impact: 5.5)
  * `test_file_args` **(Defensive Guards)** (Impact: 5.3)
  * `test_deprecated_warning` **(Defensive Guards)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 179`, `args: 67`, `func_start: 65`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 40`, `duplicate_logic: 6`, `unreferenced_by_name: 32`
* *Architecture:* `io: 5`, `api: 67`, `import: 5`
* *Defense:* `safety: 69`, `doc: 4`, `test: 48`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.585
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` click, click._utils, pytest, sys, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/tests/test_commands.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.981)
- **Top Global Matches:** file_cluster_12: 6.981, file_cluster_7: 8.811, file_cluster_5: 9.535
- **Magnitude:** 300.36 | **LOC:** 576 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 3.585; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.6%), Connectivity (formerly Api Exposure) (13.2%), Complexity Load (formerly Cognitive Load) (12.7%)
- **Documentation Coverage:** 93.7984% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_iter_params_for_processing` **(Many-Argument Workhorses)** (Impact: 8.9)
  * `test_object_propagation` **(Annotated & Test Methods)** (Impact: 8.0)
  * `test_help_param_priority` **(Defensive Guards)** (Impact: 7.6)
    * *Intent:* """Cover the edge-case in which the eagerness of help option was not respected, because it was inter...
  * `test_custom_parser` **(Defensive Guards)** (Impact: 6.0)
  * `test_invoked_subcommand` **(Defensive Guards)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 167`, `args: 65`, `func_start: 65`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 46`, `fragile_debt: 1`, `duplicate_logic: 9`, `unreferenced_by_name: 28`
* *Architecture:* `api: 66`, `import: 4`
* *Defense:* `safety: 68`, `doc: 4`, `test: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.585
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` click, optparse, pytest, re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/tests/test_stream_lifecycle.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.591)
- **Top Global Matches:** file_cluster_13: 7.591, file_cluster_11: 7.834, file_cluster_10: 8.252
- **Magnitude:** 289.16 | **LOC:** 539 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 3.585; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (41.1%), Complexity Load (formerly Cognitive Load) (23.8%)
- **Documentation Coverage:** 43.299% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_invoke_with_threads_writing_to_streams` **(Annotated & Test Methods)** (Impact: 5.1)
    * *Intent:* """Threads writing to ``click.echo()`` during invocation."""
  * `cli` **(Interface Declarations)** (Impact: 4.7)
  * `test_invoke_with_thread_pool` **(Annotated & Test Methods)** (Impact: 3.7)
    * *Intent:* # --------------------------------------------------------------------------- # Category 4: Multi-th...
  * `cli` **(Callbacks & Closures)** (Impact: 3.2)
  * `test_exception_does_not_corrupt_next_invoke` **(Defensive Guards)** (Impact: 3.2)
    * *Intent:* """A failed invoke must not break subsequent invocations."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 28
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 142`, `args: 51`, `func_start: 47`
* *Risk/State:* `state_mutation: 76`, `duplicate_logic: 2`, `unreferenced_by_name: 27`
* *Architecture:* `io: 12`, `api: 47`, `concurrency: 8`, `import: 13`
* *Defense:* `safety: 69`, `doc: 27`, `test: 34`, `sync_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.585
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` __future__, click, click.testing, concurrent.futures, gc, io, logging, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/tests/test_testing.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.394)
- **Top Global Matches:** file_cluster_13: 7.394, file_cluster_11: 7.42, file_cluster_12: 8.036
- **Magnitude:** 268.08 | **LOC:** 472 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 3.585; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (41.0%), Complexity Load (formerly Cognitive Load) (30.1%), Connectivity (formerly Api Exposure) (13.2%)
- **Documentation Coverage:** 94.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_exit_code_and_output_from_sys_exit` **(Annotated & Test Methods)** (Impact: 4.4)
    * *Intent:* # See issue #362 @click.command() def cli_string(): click.echo("hello world") sys.exit("error") @cli...
  * `test_runner_with_stream` **(Defensive Guards)** (Impact: 4.0)
  * `test_runner` **(Annotated & Test Methods)** (Impact: 3.8)
  * `test_echo_stdin_stream` **(Annotated & Test Methods)** (Impact: 3.8)
  * `test` **(Interface Declarations)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 106
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 171`, `args: 54`, `func_start: 54`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 3`, `state_mutation: 76`, `duplicate_logic: 7`, `unreferenced_by_name: 23`
* *Architecture:* `io: 9`, `api: 57`, `import: 7`
* *Defense:* `safety: 86`, `doc: 3`, `test: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.585
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` click, click.exceptions, click.testing, io, os, pytest, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/src/click/formatting.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 5.931)
- **Top Global Matches:** file_cluster_5: 5.931, file_cluster_12: 8.429, file_cluster_0: 9.212
- **Magnitude:** 247.78 | **LOC:** 302 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **8**; blast radius 17.649; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.2%), Connectivity (formerly Api Exposure) (61.0%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wrap_text` **(Many-Argument Workhorses)** (Impact: 37.8)
  * `write_dl` **(Many-Argument Workhorses)** (Impact: 24.5)
  * `write_usage` **(Many-Argument Workhorses)** (Impact: 10.8)
    * *Intent:* """Writes a usage line into the buffer. :param prog: the program name. :param args: whitespace separ...
  * `__init__` **(Generic / Templated Code)** (Impact: 9.8)
  * `join_options` **(Generic / Templated Code)** (Impact: 6.6)
    * *Intent:* """Given a list of option strings this joins them in the most appropriate way and returns them in th...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 43`, `args: 18`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 37`
* *Architecture:* `api: 17`, `import: 8`
* *Defense:* `safety: 4`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.649
  * `Choke Point (Betweenness):` 0.02055 | `Ripple Effect (Closeness):` 0.423532
  * `Imports (Out-Degree: 3):` ._compat, ._textwrap, .parser, __future__, collections.abc, contextlib, gettext, shutil
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `click-8.3.2/tests/test_utils.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.553)
- **Top Global Matches:** file_cluster_15: 7.553, file_cluster_13: 7.89, file_cluster_11: 7.935
- **Magnitude:** 245.18 | **LOC:** 749 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 3.585; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (36.0%), Complexity Load (formerly Cognitive Load) (12.0%), Connectivity (formerly Api Exposure) (10.2%)
- **Documentation Coverage:** 92.3913% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_echo_via_pager` **(Many-Argument Workhorses)** (Impact: 15.3)
  * `test_prompts` **(Defensive Guards)** (Impact: 9.0)
  * `test_echo_writing_to_standard_error` **(Defensive Guards)** (Impact: 5.5)
  * `test_make_default_short_help` **(Defensive Guards)** (Impact: 4.9)
  * `test_unset_sentinel` **(Defensive Guards)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 12 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 227`, `args: 60`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 50`, `duplicate_logic: 2`, `unreferenced_by_name: 30`
* *Architecture:* `io: 30`, `api: 40`, `import: 19`
* *Defense:* `safety: 97`, `doc: 3`, `test: 57`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.585
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` click._compat, click._termui_impl, click._utils, click.utils, collections, contextlib, decimal, fractions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/src/click/exceptions.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.485)
- **Top Global Matches:** file_cluster_5: 8.485, file_cluster_0: 8.888, file_cluster_4: 9.279
- **Magnitude:** 234.98 | **LOC:** 309 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **8**; blast radius 48.407; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.8%), Connectivity (formerly Api Exposure) (72.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `format_message` **(Compute Cores)** (Impact: 27.4)
  * `show` **(Compute Cores)** (Impact: 11.4)
  * `format_message` **(Generic / Templated Code)** (Impact: 7.6)
  * `__str__` **(Generic / Templated Code)** (Impact: 7.4)
  * `__init__` **(Generic / Templated Code)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 106
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 69`, `args: 20`, `func_start: 20`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 40`
* *Architecture:* `io: 1`, `api: 19`, `import: 12`
* *Defense:* `safety: 1`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 48.407
  * `Choke Point (Betweenness):` 0.017496 | `Ripple Effect (Closeness):` 0.476474
  * `Imports (Out-Degree: 4):` ._compat, .core, .globals, .utils, __future__, collections.abc, gettext, typing
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `click-8.3.2/tests/test_shell_completion.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.859)
- **Top Global Matches:** file_cluster_12: 6.859, file_cluster_5: 8.191, file_cluster_7: 9.494
- **Magnitude:** 175.36 | **LOC:** 562 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 3.585; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (31.7%), Connectivity (formerly Api Exposure) (10.7%), Complexity Load (formerly Cognitive Load) (9.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_words` **(Encapsulated Accessors)** (Impact: 4.1)
  * `test_zsh_full_complete_with_colons` **(Generic / Templated Code)** (Impact: 3.0)
  * `test_nested_group` **(Generic / Templated Code)** (Impact: 2.9)
  * `test_full_complete` **(Defensive Guards)** (Impact: 2.5)
  * `test_files_closed` **(Annotated & Test Methods)** (Impact: 2.4)
    * *Intent:* # Don't make the ResourceWarning give an error
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 206`, `args: 42`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 53`, `unreferenced_by_name: 34`
* *Architecture:* `io: 1`, `api: 40`, `import: 15`
* *Defense:* `safety: 99`, `doc: 3`, `test: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.585
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` click.core, click.shell_completion, click.types, collections.abc, pytest, textwrap, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/tests/test_defaults.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.672)
- **Top Global Matches:** file_cluster_12: 6.672, file_cluster_13: 8.709, file_cluster_15: 9.097
- **Magnitude:** 173.04 | **LOC:** 357 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.585; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.0%), Complexity Load (formerly Cognitive Load) (18.0%), Connectivity (formerly Api Exposure) (10.7%)
- **Documentation Coverage:** 54.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lookup_default` **(Defensive Guards)** (Impact: 8.7)
  * `test_lookup_default_override_respected` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* """A subclass override of ``lookup_default()`` should be called by Click internals, not bypassed by ...
  * `test_default_map_source` **(Defensive Guards)** (Impact: 5.8)
    * *Intent:* """``get_parameter_source()`` reports the correct origin for a parameter value across the resolution...
  * `test_default_map_with_callable_flag_value` **(Defensive Guards)** (Impact: 5.4)
    * *Intent:* """``default_map`` entries should override the auto-aligned callable ``flag_value``, and callable en...
  * `test_lookup_default_returns_hides_sentinel` **(Defensive Guards)** (Impact: 4.5)
    * *Intent:* """``lookup_default()`` should return ``None`` for missing keys, not :attr:`UNSET`. Regression test ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 80`, `args: 26`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 37`, `unreferenced_by_name: 11`
* *Architecture:* `api: 25`, `import: 3`
* *Defense:* `safety: 37`, `doc: 12`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.585
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` click, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/src/click/_winconsole.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.085)
- **Top Global Matches:** file_cluster_5: 6.085, file_cluster_12: 7.988, file_cluster_0: 9.475
- **Magnitude:** 172.82 | **LOC:** 297 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 183.7; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_windows_console_stream` **(Stateful Encapsulated Methods)** (Impact: 15.1)
  * `readinto` **(Compute Cores)** (Impact: 11.8)
  * `write` **(Compute Cores)** (Impact: 6.1)
  * `get_buffer` **(Defensive Guards)** (Impact: 5.7)
  * `_get_error_message` **(Encapsulated Accessors)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 79
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 107`, `args: 20`, `func_start: 20`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 49`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 15`, `import: 28`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 183.7
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.327988
  * `Imports (Out-Degree: 1):` ._compat, __future__, collections.abc, ctypes, ctypes.wintypes, io, msvcrt, sys...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `click-8.3.2/tests/test_formatting.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.098)
- **Top Global Matches:** file_cluster_12: 7.098, file_cluster_7: 8.883, file_cluster_5: 9.657
- **Magnitude:** 165.08 | **LOC:** 369 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 3.585; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (44.5%), Connectivity (formerly Api Exposure) (12.6%), Complexity Load (formerly Cognitive Load) (5.0%)
- **Documentation Coverage:** 71.7949% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_basic_functionality` **(Defensive Guards)** (Impact: 6.5)
  * `test_truncating_docstring` **(Defensive Guards)** (Impact: 5.6)
  * `test_formatting_usage_error_metavar_bad_arg` **(Annotated & Test Methods)** (Impact: 4.9)
  * `test_wrapping_long_options_strings` **(Annotated & Test Methods)** (Impact: 4.5)
  * `test_wrapping_long_command_name` **(Annotated & Test Methods)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 81`, `args: 39`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 22`, `duplicate_logic: 15`, `unreferenced_by_name: 19`
* *Architecture:* `api: 40`, `import: 1`
* *Defense:* `safety: 30`, `doc: 12`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.585
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` click
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `click-8.3.2/tests/test_types.py` (PYTHON) | Magnitude: 125.42 | Delta: **0.134** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 160, structural_boundaries: 87, core_var_decl: 52, design_snake_case: 52

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `click-8.3.2/tests/test_testing.py` (PYTHON) | Magnitude: 268.08 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 313, structural_boundaries: 171, core_var_decl: 92, design_snake_case: 91

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `click-8.3.2/src/click/core.py` -> **Severity: 10.025** (Bridge: 0.1002 * Flux: 100.0%)
- `click-8.3.2/src/click/utils.py` -> **Severity: 2.141** (Bridge: 0.0214 * Flux: 100.0%)
- `click-8.3.2/src/click/termui.py` -> **Severity: 2.075** (Bridge: 0.0208 * Flux: 99.9991%)
- `click-8.3.2/src/click/formatting.py` -> **Severity: 2.055** (Bridge: 0.0205 * Flux: 100.0%)
- `click-8.3.2/src/click/_compat.py` -> **Severity: 1.871** (Bridge: 0.0187 * Flux: 99.9979%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `click-8.3.2/src/click/core.py` -> **Severity: 56.733** (Embedded: 0.6861 * Error Risk: 82.686%)
- `click-8.3.2/src/click/utils.py` -> **Severity: 46.539** (Embedded: 0.6237 * Error Risk: 74.6125%)
- `click-8.3.2/src/click/_compat.py` -> **Severity: 40.319** (Embedded: 0.504 * Error Risk: 80.0%)
- `click-8.3.2/src/click/decorators.py` -> **Severity: 38.513** (Embedded: 0.4972 * Error Risk: 77.4623%)
- `click-8.3.2/src/click/exceptions.py` -> **Severity: 35.643** (Embedded: 0.4765 * Error Risk: 74.8049%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `click-8.3.2/src/click/_compat.py` -> **Severity: 18626.728** (Blast Radius: 211.879 * Doc Risk: 87.9121%)
- `click-8.3.2/src/click/_winconsole.py` -> **Severity: 18370.0** (Blast Radius: 183.7 * Doc Risk: 100.0%)
- `click-8.3.2/src/click/core.py` -> **Severity: 6299.583** (Blast Radius: 111.39 * Doc Risk: 56.5543%)
- `click-8.3.2/src/click/utils.py` -> **Severity: 5021.409** (Blast Radius: 67.789 * Doc Risk: 74.0741%)
- `click-8.3.2/src/click/exceptions.py` -> **Severity: 4840.7** (Blast Radius: 48.407 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 3565 call pairs -- scoped 49.3%, unique 0.0%, ambiguous 11.3%, external 39.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 3565 | 49.3% | 0.0% | 11.3% | 39.5% |

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
