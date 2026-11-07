# ARCHITECTURAL_BRIEF: jedi
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/davidhalter/jedi.git` |
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
- **Scope:** 336 analyzed artifact(s), 27745 LOC.
- **Load-bearing artifact:** `jedi/__init__.py` -- 75 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `test/test_inference/test_imports.py` -- pulls in 40 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `jedi/inference/syntax_tree.py` at magnitude 1168.28 (structural weight, not risk).
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
| Total Artifacts | 387 |
| Analyzed Artifacts (Scanned) | 336 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 51 |
| Total LOC | 27745 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 86.8% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3536 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1546 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 19.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.816 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 27 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 325 | 27635 | 96.7% |
| PLAINTEXT | 4 | 0 | 1.2% |
| YAML | 2 | 63 | 0.6% |
| MARKDOWN | 2 | 0 | 0.6% |
| SHELL | 2 | 34 | 0.6% |
| C | 1 | 13 | 0.3% |

## 4.1 SOURCE ENCODINGS
All 336 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 37%, Parameter Forwarders Files 18%, Large Core Modules (2) 16%, Large Core Modules (3) 12%, Declarative / Non-Code 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 330 | 98.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 1.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 51*

**Composition by Extension & Reason:**
- `.rst`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable)
- `.py`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 4x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cfg`: 2x Excluded (Unsupported Extension: '.cfg')
- `.egg-link`: 2x Excluded (Unsupported Extension: '.egg-link')
- `.pth`: 2x Excluded (Unsupported Extension: '.pth')
- `.zip`: 2x Excluded (Explicitly Denied Extension: '.zip')
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')
- `.so`: 1x Excluded (Explicitly Denied Extension: '.so')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.2 | 19.7 | 5.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 88.4 | 46.6 | 51.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 12.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 16.4 | 7.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 24.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 20.9 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.8 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 58.2 | 82.1 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 584 | 114 | 5 | `test/completion/arrays.py` |
| cleanup | 2 | 2 | 0 | `jedi/inference/compiled/subprocess/__init__.py` |
| guards | 2539 | 155 | 23 | `test/test_api/test_classes.py` |
| danger | 762 | 158 | 8 | `test/test_api/test_interpreter.py` |
| concurrency | 455 | 81 | 5 | `test/completion/generators.py` |
| connectivity | 2889 | 224 | 23 | `test/test_api/test_interpreter.py` |
| io | 458 | 83 | 5 | `jedi/api/environment.py` |
| crypto | 2 | 2 | 0 | `jedi/api/environment.py` |
| ipc | 30 | 9 | 0 | `jedi/inference/compiled/subprocess/__init__.py` |
| time | 37 | 16 | 0 | `test/completion/precedence.py` |
| serialization | 1 | 1 | 0 | `jedi/_compatibility.py` |
| regex | 45 | 21 | 0 | `jedi/inference/docstrings.py` |
| events | 42 | 8 | 0 | `jedi/plugins/stdlib.py` |
| tests | 849 | 74 | 6 | `test/test_api/test_interpreter.py` |
| docs | 772 | 161 | 6 | `test/test_inference/test_signature.py` |
| debt | 324 | 92 | 3 | `test/refactor/extract_function.py` |
| mutation | 10986 | 247 | 110 | `jedi/inference/syntax_tree.py` |
| dead_code | 665 | 107 | 6 | `test/test_api/test_interpreter.py` |
| credential | 0 | 0 | 0 | - |
| threat | 4 | 3 | 0 | `test/completion/on_import.py` |
| ml_ai | 4 | 3 | 0 | `test/test_api/test_completion.py` |
| ui | 2 | 1 | 0 | `jedi/__init__.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `jedi/api/environment.py` (Hits: 39)
- `test/test_inference/test_imports.py` (Hits: 22)
- `test/run.py` (Hits: 19)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`jedi/__init__.py`) — 75 inbound connections
2. **base_value.py** (`jedi/inference/base_value.py`) — 51 inbound connections
3. **__init__.py** (`jedi/api/__init__.py`) — 43 inbound connections
4. **__init__.py** (`jedi/inference/__init__.py`) — 33 inbound connections
5. **names.py** (`jedi/inference/names.py`) — 28 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_imports.py** (`test/test_inference/test_imports.py`) — 40 outbound dependencies
2. **imports.py** (`test/completion/imports.py`) — 30 outbound dependencies
3. **__init__.py** (`jedi/api/__init__.py`) — 27 outbound dependencies
4. **klass.py** (`jedi/inference/value/klass.py`) — 24 outbound dependencies
5. **on_import.py** (`test/completion/on_import.py`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_infer_comparison_part` **(Many-Argument Workhorses)** (@ `jedi/inference/syntax_tree.py`) -> Impact: **112.3** | LOC: 91
- `process_params` **(Many-Argument Workhorses)** (@ `jedi/inference/star_args.py`) -> Impact: **83.5** | LOC: 112
- `test_infer_and_goto` **(Many-Argument Workhorses)** (@ `test/test_inference/test_gradual/test_stubs.py`) -> Impact: **81.9** | LOC: 47
- `extract_function` **(Many-Argument Workhorses)** (@ `jedi/api/refactoring/extract.py`) -> Impact: **78.3** | LOC: 85
- `search_in_module` **(Many-Argument Workhorses)** (@ `jedi/api/completion.py`) -> Impact: **71.6** | LOC: 40
- `_complete_python` **(Many-Argument Workhorses)** (@ `jedi/api/completion.py`) -> Impact: **71.2** | LOC: 142
  * *Intent:* """ Analyzes the current context of a completion and decides what to return. Technically this works by generating a parser stack and analysing the cur...
- `_check_for_exception_catch` **(Many-Argument Workhorses)** (@ `jedi/inference/analysis.py`) -> Impact: **69.2** | LOC: 88
  * *Intent:* """ Checks if a jedi object (e.g. `Statement`) sits inside a try/catch and doesn't count as an error (if equal to `exception`). Also checks `hasattr` ...
- `get_executed_param_names_and_issues` **(Many-Argument Workhorses)** (@ `jedi/inference/param.py`) -> Impact: **67.5** | LOC: 173
  * *Intent:* """ Return a tuple of: - a list of `ExecutedParamName`s corresponding to the arguments of the function execution `function_value`, containing the infe...
- `tree_name_to_values` **(Many-Argument Workhorses)** (@ `jedi/inference/syntax_tree.py`) -> Impact: **65.0** | LOC: 101
- `_try_to_load_stub` **(Many-Argument Workhorses)** (@ `jedi/inference/gradual/typeshed.py`) -> Impact: **60.8** | LOC: 90

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `jedi/inference` | 25 | 7205.0 | 59.37% | 14.38% |
| `test/completion` | 54 | 3887.8 | 13.83% | 0.0% |
| `jedi/api` | 14 | 3824.7 | 37.3% | 5.89% |
| `test/test_api` | 22 | 2521.78 | 15.25% | 0.0% |
| `jedi/inference/value` | 9 | 2490.36 | 45.31% | 25.51% |
| `jedi/inference/gradual` | 10 | 2020.56 | 55.79% | 26.55% |
| `test/test_inference` | 19 | 1454.18 | 12.22% | 0.0% |
| `jedi/plugins` | 6 | 1431.14 | 47.68% | 30.44% |
| `jedi/inference/compiled` | 5 | 1339.78 | 69.3% | 20.06% |
| `test` | 11 | 1175.06 | 17.36% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `conftest.py` -> **99.9996%** Exposure
- `jedi/inference/context.py` -> **99.9987%** Exposure
- `jedi/inference/gradual/base.py` -> **99.9527%** Exposure
- `jedi/file_io.py` -> **99.7464%** Exposure
- `jedi/inference/value/instance.py` -> **99.1205%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `jedi/api/__init__.py` -> **100.0%** Exposure
- `jedi/api/classes.py` -> **100.0%** Exposure
- `jedi/api/completion.py` -> **100.0%** Exposure
- `jedi/api/environment.py` -> **100.0%** Exposure
- `jedi/api/file_name.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/test_api/test_interpreter.py` -> **56** Orphaned Functions | **2** Duplicates
- `test/test_api/test_call_signatures.py` -> **42** Orphaned Functions | **0** Duplicates
- `test/test_inference/test_imports.py` -> **37** Orphaned Functions | **2** Duplicates
- `test/test_api/test_classes.py` -> **37** Orphaned Functions | **0** Duplicates
- `test/test_inference/test_docstring.py` -> **33** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `1304` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `jedi/inference/syntax_tree.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.73)
- **Top Global Matches:** file_cluster_8: 7.73, file_cluster_6: 9.27, file_cluster_4: 17.738
- **Magnitude:** 1168.28 | **LOC:** 906 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **18**; blast radius 10.379; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (99.7%), Guard Balance (formerly Safety Score) (81.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 68.2927% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_infer_comparison_part` **(Many-Argument Workhorses)** (Impact: 112.3)
  * `tree_name_to_values` **(Many-Argument Workhorses)** (Impact: 65.0)
  * `infer_atom` **(Defensive Guards)** (Impact: 52.6)
    * *Intent:* """ Basically to process ``atom`` nodes. The parser sometimes doesn't generate the node (because it ...
  * `infer_node` **(Compute Cores)** (Impact: 52.0)
  * `_infer_node` **(Compute Cores)** (Impact: 48.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 177 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 540
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 256`, `structural_boundaries: 234`, `args: 28`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 186`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `api: 14`, `concurrency: 1`, `import: 25`
* *Defense:* `safety: 26`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.379
  * `Choke Point (Betweenness):` 0.0054 | `Ripple Effect (Closeness):` 0.15958
  * `Imports (Out-Degree: 22):` copy, itertools, jedi, jedi.inference, jedi.inference.base_value, jedi.inference.cache, jedi.inference.compiled.access, jedi.inference.context...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `jedi/api/completion.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.264)
- **Top Global Matches:** file_cluster_6: 7.264, file_cluster_4: 8.999, file_cluster_12: 15.865
- **Magnitude:** 875.3 | **LOC:** 697 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **21**; blast radius 4.719; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.5%)
- **Documentation Coverage:** 81.8182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `search_in_module` **(Many-Argument Workhorses)** (Impact: 71.6)
  * `_complete_python` **(Many-Argument Workhorses)** (Impact: 71.2)
    * *Intent:* """ Analyzes the current context of a completion and decides what to return. Technically this works ...
  * `_extract_string_while_in_string` **(Compute Cores)** (Impact: 50.8)
  * `filter_names` **(Many-Argument Workhorses)** (Impact: 35.4)
  * `_complete_in_string` **(Stateful Encapsulated Methods)** (Impact: 31.6)
    * *Intent:* """ To make it possible for people to have completions in doctests or generally in "Python" code in ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 112 instances
* *State Mutation (weighted view):* 361
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 163`, `args: 31`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 137`, `planned_debt: 1`
* *Architecture:* `api: 14`, `import: 24`
* *Defense:* `safety: 8`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.719
  * `Choke Point (Betweenness):` 0.005473 | `Ripple Effect (Closeness):` 0.139386
  * `Imports (Out-Degree: 19):` inspect, jedi, jedi.api, jedi.api.file_name, jedi.api.strings, jedi.inference, jedi.inference.base_value, jedi.inference.context...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `jedi/plugins/stdlib.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.505)
- **Top Global Matches:** file_cluster_16: 6.505, file_cluster_15: 6.682, file_cluster_12: 7.274
- **Magnitude:** 747.2 | **LOC:** 917 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 1.291; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (64.4%), Guard Balance (formerly Safety Score) (64.4%)
- **Documentation Coverage:** 95.4198% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `builtins_isinstance` **(Many-Argument Workhorses)** (Impact: 31.0)
  * `collections_namedtuple` **(Many-Argument Workhorses)** (Impact: 26.8)
    * *Intent:* """ Implementation of the namedtuple function. This has to be done by processing the namedtuple clas...
  * `_dataclass_transform` **(Many-Argument Workhorses)** (Impact: 23.1)
    * *Intent:* """ Decorator entry points for dataclass_transform. 1. dataclass-like decorator instantiation from a...
  * `wrapper` **(Defensive Guards)** (Impact: 18.8)
  * `argument_clinic` **(Many-Argument Workhorses)** (Impact: 17.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *Api Near Db Sink:* 3 instances
* *State Mutation (weighted view):* 226
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 224`, `args: 77`, `func_start: 73`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 92`, `dead_code: 1`, `planned_debt: 6`, `fragile_debt: 1`, `unreferenced_by_name: 7`
* *Architecture:* `io: 7`, `api: 60`, `import: 19`
* *Defense:* `safety: 22`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` jedi, jedi.inference, jedi.inference.arguments, jedi.inference.base_value, jedi.inference.filters, jedi.inference.helpers, jedi.inference.lazy_value, jedi.inference.names...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jedi/inference/names.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.962)
- **Top Global Matches:** file_cluster_15: 6.962, file_cluster_12: 7.177, file_cluster_16: 7.496
- **Magnitude:** 686.48 | **LOC:** 674 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **28** in-repo importer(s); it depends on **19**; blast radius 16.452; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (93.7%), Complexity Load (formerly Cognitive Load) (87.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 95.6522% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `goto` **(Compute Cores)** (Impact: 45.9)
  * `get_kind` **(Compute Cores)** (Impact: 18.3)
  * `assignment_indexes` **(Compute Cores)** (Impact: 14.7)
    * *Intent:* """ Returns an array of tuple(int, node) of the indexes that are used in tuple assignments. For exam...
  * `get_qualified_names` **(Compute Cores)** (Impact: 14.6)
  * `py__doc__` **(Compute Cores)** (Impact: 12.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 87 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 289
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 276`, `args: 77`, `func_start: 77`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 115`, `planned_debt: 1`
* *Architecture:* `api: 75`, `concurrency: 1`, `import: 25`
* *Defense:* `safety: 1`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.452
  * `Choke Point (Betweenness):` 0.00643 | `Ripple Effect (Closeness):` 0.151548
  * `Imports (Out-Degree: 18):` abc, inspect, jedi.cache, jedi.inference, jedi.inference.base_value, jedi.inference.cache, jedi.inference.dynamic_params, jedi.inference.gradual.annotation...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `jedi/api/helpers.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.415)
- **Top Global Matches:** file_cluster_4: 5.415, file_cluster_6: 9.084, file_cluster_16: 12.268
- **Magnitude:** 660.34 | **LOC:** 523 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **14**; blast radius 4.623; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.2%), Complexity Load (formerly Cognitive Load) (74.7%)
- **Documentation Coverage:** 87.2727% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_iter_arguments` **(Compute Cores)** (Impact: 56.9)
  * `calculate_index` **(Compute Cores)** (Impact: 51.0)
  * `get_signature_details` **(Compute Cores)** (Impact: 33.8)
  * `_get_code_for_stack` **(Stateful Encapsulated Methods)** (Impact: 27.9)
    * *Intent:* # It might happen that we're on whitespace or on a comment. This means # that we would not get the r...
  * `wrapper` **(Many-Argument Workhorses)** (Impact: 25.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 73 instances
* *State Mutation (weighted view):* 230
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 157`, `args: 32`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 84`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 26`, `import: 14`
* *Defense:* `safety: 5`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.623
  * `Choke Point (Betweenness):` 0.000798 | `Ripple Effect (Closeness):` 0.135213
  * `Imports (Out-Degree: 7):` collections, functools, inspect, itertools, jedi.cache, jedi.inference.base_value, jedi.inference.compiled, jedi.inference.helpers...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `jedi/api/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.48)
- **Top Global Matches:** file_cluster_16: 7.48, file_cluster_15: 7.669, file_cluster_9: 7.95
- **Magnitude:** 638.78 | **LOC:** 799 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **43** in-repo importer(s); it depends on **27**; blast radius 28.53; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.7%)
- **Documentation Coverage:** 37.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 28.8)
  * `help` **(Compute Cores)** (Impact: 28.1)
    * *Intent:* """ Used to display a help window to users. Uses :meth:`.Script.goto` and returns additional definit...
  * `goto` **(Many-Argument Workhorses)** (Impact: 28.0)
  * `infer` **(Many-Argument Workhorses)** (Impact: 24.2)
    * *Intent:* """ Return the definitions of under the cursor. It is basically a wrapper around Jedi's type inferen...
  * `get_context` **(Many-Argument Workhorses)** (Impact: 23.9)
    * *Intent:* """ Returns the scope context under the cursor. This basically means the function, class or module w...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 92 instances
* *State Mutation (weighted view):* 291
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 146`, `args: 30`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 107`, `planned_debt: 5`
* *Architecture:* `io: 3`, `api: 22`, `import: 33`
* *Defense:* `safety: 6`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.53
  * `Choke Point (Betweenness):` 0.028289 | `Ripple Effect (Closeness):` 0.186617
  * `Imports (Out-Degree: 25):` jedi, jedi.api, jedi.api.completion, jedi.api.environment, jedi.api.errors, jedi.api.helpers, jedi.api.keywords, jedi.api.project...
  * `Imported By (In-Degree: 43):` (Excluded from Brief to save tokens)

### `test/test_api/test_interpreter.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.998)
- **Top Global Matches:** file_cluster_5: 6.998, file_cluster_12: 7.488, file_cluster_7: 9.081
- **Magnitude:** 600.5 | **LOC:** 862 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 1.291; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.8%), Complexity Load (formerly Cognitive Load) (42.4%), Concurrency Surface (formerly Concurrency) (22.6%), Connectivity (formerly Api Exposure) (13.3%)
- **Documentation Coverage:** 93.8144% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_dict_completion` **(Defensive Guards)** (Impact: 16.9)
  * `test__getattr__completions` **(Compute Cores)** (Impact: 15.4)
  * `test_dir_magic_method` **(Defensive Guards)** (Impact: 12.7)
  * `_assert_interpreter_complete` **(Stateful Encapsulated Methods)** (Impact: 10.2)
  * `test_custom__getitem__` **(Compute Cores)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 52 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 224
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 282`, `args: 94`, `func_start: 89`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 1`, `state_mutation: 120`, `planned_debt: 2`, `duplicate_logic: 2`, `unreferenced_by_name: 56`
* *Architecture:* `io: 10`, `api: 98`, `concurrency: 1`, `import: 20`
* *Defense:* `safety: 67`, `doc: 7`, `test: 69`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.291
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` collections, datetime, functools, importlib, jedi, jedi.inference.compiled, jedi.settings, keyword...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jedi/inference/imports.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.943)
- **Top Global Matches:** file_cluster_4: 6.943, file_cluster_12: 8.97, file_cluster_9: 9.044
- **Magnitude:** 564.38 | **LOC:** 592 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **18**; blast radius 8.682; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.7%)
- **Documentation Coverage:** 70.5882% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `completion_names` **(Many-Argument Workhorses)** (Impact: 36.4)
    * *Intent:* """ :param only_modules: Indicates wheter it's possible to import a definition that is not defined i...
  * `import_module` **(Many-Argument Workhorses)** (Impact: 34.3)
    * *Intent:* """ This method is very similar to importlib's `_gcd_import`. """
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 32.8)
    * *Intent:* """ An implementation similar to ``__import__``. Use `follow` to actually follow the imports. *level...
  * `import_module_by_names` **(Many-Argument Workhorses)** (Impact: 25.9)
  * `load_module_from_path` **(Many-Argument Workhorses)** (Impact: 20.1)
    * *Intent:* """ This should pretty much only be used for get_modules_containing_name. It's here to ensure that a...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 81 instances
* *State Mutation (weighted view):* 257
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 120`, `args: 22`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 95`
* *Architecture:* `io: 8`, `api: 14`, `import: 23`
* *Defense:* `safety: 11`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.682
  * `Choke Point (Betweenness):` 0.004001 | `Ripple Effect (Closeness):` 0.163628
  * `Imports (Out-Degree: 18):` beyond, jedi, jedi.file_io, jedi.inference, jedi.inference.base_value, jedi.inference.cache, jedi.inference.compiled.subprocess.functions, jedi.inference.gradual.conversion...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `test/run.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.624)
- **Top Global Matches:** file_cluster_12: 7.624, file_cluster_4: 8.066, file_cluster_15: 9.673
- **Magnitude:** 561.9 | **LOC:** 545 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **22**; blast radius 1.621; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (82.7%), Connectivity (formerly Api Exposure) (52.2%), Complexity Load (formerly Cognitive Load) (36.6%), Dead Code Surface (formerly Dead Code) (5.5%)
- **Documentation Coverage:** 95.9184% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `collect_file_tests` **(Many-Argument Workhorses)** (Impact: 42.5)
  * `collect_dir_tests` **(Defensive Guards)** (Impact: 29.3)
  * `run_inference` **(Many-Argument Workhorses)** (Impact: 25.9)
  * `run_get_references` **(Many-Argument Workhorses)** (Impact: 23.4)
  * `definition` **(Type Conversions)** (Impact: 17.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 85 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 282
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 102`, `args: 27`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 2`, `state_mutation: 112`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 19`, `api: 24`, `import: 25`
* *Defense:* `safety: 12`, `doc: 4`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.621
  * `Choke Point (Betweenness):` 0.000681 | `Ripple Effect (Closeness):` 0.00597
  * `Imports (Out-Degree: 9):` _pytest.outcomes, ast, docopt, functools, io, jedi, jedi.api.classes, jedi.api.completion...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `jedi/inference/value/iterable.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.771)
- **Top Global Matches:** file_cluster_12: 6.771, file_cluster_16: 7.18, file_cluster_15: 7.555
- **Magnitude:** 546.92 | **LOC:** 648 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **12**; blast radius 6.228; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (78.3%), Complexity Load (formerly Cognitive Load) (69.0%)
- **Documentation Coverage:** 87.1795% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_tree_entries` **(Compute Cores)** (Impact: 27.7)
  * `unpack_tuple_to_dict` **(Many-Argument Workhorses)** (Impact: 25.8)
    * *Intent:* """ Unpacking tuple assignments in for statements and expr_stmts. """
  * `comprehension_from_atom` **(Many-Argument Workhorses)** (Impact: 17.7)
  * `_nested` **(Stateful Encapsulated Methods)** (Impact: 11.4)
  * `py__iter__` **(Compute Cores)** (Impact: 9.3)
    * *Intent:* """ While values returns the possible values for any array field, this function returns the value fo...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 186
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 238`, `args: 76`, `func_start: 76`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 90`, `planned_debt: 3`, `duplicate_logic: 4`
* *Architecture:* `api: 57`, `import: 14`
* *Defense:* `safety: 12`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.228
  * `Choke Point (Betweenness):` 0.002278 | `Ripple Effect (Closeness):` 0.159018
  * `Imports (Out-Degree: 13):` jedi.inference, jedi.inference.base_value, jedi.inference.cache, jedi.inference.context, jedi.inference.filters, jedi.inference.gradual.base, jedi.inference.gradual.generics, jedi.inference.helpers...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `jedi/inference/value/instance.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.656)
- **Top Global Matches:** file_cluster_15: 5.656, file_cluster_16: 5.875, file_cluster_11: 7.593
- **Magnitude:** 543.02 | **LOC:** 609 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **16**; blast radius 6.946; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.1%), Complexity Load (formerly Cognitive Load) (82.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 96.5035% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_filters` **(Defensive Guards)** (Impact: 17.1)
  * `py__simple_getitem__` **(Compute Cores)** (Impact: 16.7)
  * `_filter_self_names` **(Stateful Encapsulated Methods)** (Impact: 14.4)
  * `py__get__` **(Compute Cores)** (Impact: 12.9)
    * *Intent:* """ obj may be None. """
  * `get_key_values` **(Compute Cores)** (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 217`, `args: 80`, `func_start: 80`, `class_start: 18`
* *Risk/State:* `state_mutation: 67`, `planned_debt: 2`, `duplicate_logic: 8`
* *Architecture:* `api: 73`, `import: 18`
* *Defense:* `safety: 4`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.946
  * `Choke Point (Betweenness):` 0.000658 | `Ripple Effect (Closeness):` 0.135213
  * `Imports (Out-Degree: 15):` abc, jedi, jedi.inference, jedi.inference.arguments, jedi.inference.base_value, jedi.inference.cache, jedi.inference.compiled.value, jedi.inference.filters...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `jedi/inference/compiled/value.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.546)
- **Top Global Matches:** file_cluster_15: 6.546, file_cluster_12: 6.83, file_cluster_16: 7.097
- **Magnitude:** 531.32 | **LOC:** 627 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **20**; blast radius 10.245; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (71.6%)
- **Documentation Coverage:** 97.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get` **(Stateful Encapsulated Methods)** (Impact: 28.2)
    * *Intent:* """ To remove quite a few access calls we introduced the callback here. """
  * `_parse_function_doc` **(Compute Cores)** (Impact: 22.7)
    * *Intent:* """ Takes a function and returns the params and return value as a tuple. This is nothing more than a...
  * `execute_annotation` **(Compute Cores)** (Impact: 10.9)
  * `get_param_names` **(Defensive Guards)** (Impact: 10.7)
  * `py__call__` **(Defensive Guards)** (Impact: 9.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 167
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 229`, `args: 82`, `func_start: 78`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 75`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 65`, `import: 21`
* *Defense:* `safety: 17`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.245
  * `Choke Point (Betweenness):` 0.003073 | `Ripple Effect (Closeness):` 0.140689
  * `Imports (Out-Degree: 17):` functools, inspect, jedi, jedi.cache, jedi.inference, jedi.inference.base_value, jedi.inference.cache, jedi.inference.compiled...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `jedi/api/refactoring/extract.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.919)
- **Top Global Matches:** file_cluster_4: 6.919, file_cluster_6: 8.978, file_cluster_16: 12.708
- **Magnitude:** 528.84 | **LOC:** 387 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 2.261; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.4%)
- **Documentation Coverage:** 72.7273% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `extract_function` **(Many-Argument Workhorses)** (Impact: 78.3)
  * `_find_nodes` **(Many-Argument Workhorses)** (Impact: 36.6)
    * *Intent:* """ Looks up a module and tries to find the appropriate amount of nodes that are in there. """
  * `_remove_unwanted_expression_nodes` **(Stateful Encapsulated Methods)** (Impact: 27.7)
    * *Intent:* """ This function makes it so for `1 * 2 + 3` you can extract `2 + 3`, even though it is not part of...
  * `_replace` **(Many-Argument Workhorses)** (Impact: 25.4)
  * `_find_inputs_and_outputs` **(Stateful Encapsulated Methods)** (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 78 instances
* *State Mutation (weighted view):* 243
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 87`, `args: 19`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 87`
* *Architecture:* `api: 2`, `import: 7`
* *Defense:* `safety: 5`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.261
  * `Choke Point (Betweenness):` 0.001611 | `Ripple Effect (Closeness):` 0.124411
  * `Imports (Out-Degree: 6):` jedi, jedi.api.exceptions, jedi.api.refactoring, jedi.common, jedi.parser_utils, parso, textwrap
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `jedi/inference/value/klass.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.417)
- **Top Global Matches:** file_cluster_12: 7.417, file_cluster_16: 8.09, file_cluster_15: 8.111
- **Magnitude:** 499.2 | **LOC:** 695 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **24**; blast radius 8.49; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.9%), Connectivity (formerly Api Exposure) (60.6%)
- **Documentation Coverage:** 84.7059% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_filters` **(Many-Argument Workhorses)** (Impact: 26.1)
  * `_get_dataclass_transform_signatures` **(Stateful Encapsulated Methods)** (Impact: 22.5)
    * *Intent:* """ Returns: A non-empty list if the class has dataclass semantics else an empty list. The dataclass...
  * `get_metaclasses` **(Compute Cores)** (Impact: 17.8)
  * `get_dataclass_param_names` **(Compute Cores)** (Impact: 13.1)
    * *Intent:* """ ``cls`` is a :class:`ClassMixin`. The type is only documented as mypy would complain that some f...
  * `is_typeddict` **(Defensive Guards)** (Impact: 12.7)
    * *Intent:* # TODO Do a proper mro resolution. Currently we are just listing # classes. However, it's a complica...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 166
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 201`, `args: 48`, `func_start: 47`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 62`, `planned_debt: 5`
* *Architecture:* `api: 43`, `import: 29`
* *Defense:* `safety: 15`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.49
  * `Choke Point (Betweenness):` 0.004955 | `Ripple Effect (Closeness):` 0.15958
  * `Imports (Out-Degree: 23):` __future__, inspect, jedi, jedi.inference, jedi.inference.arguments, jedi.inference.base_value, jedi.inference.cache, jedi.inference.compiled...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `jedi/inference/context.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.829)
- **Top Global Matches:** file_cluster_15: 6.829, file_cluster_16: 8.044, file_cluster_4: 8.125
- **Magnitude:** 493.86 | **LOC:** 499 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **14**; blast radius 6.567; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Connectivity (formerly Api Exposure) (99.7%), Mutation Surface (formerly State Flux) (85.0%), Complexity Load (formerly Cognitive Load) (84.4%)
- **Documentation Coverage:** 96.748% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `py__getattribute__` **(Many-Argument Workhorses)** (Impact: 54.0)
  * `create_context` **(Compute Cores)** (Impact: 29.6)
  * `_check_for_additional_knowledge` **(Stateful Encapsulated Methods)** (Impact: 21.1)
  * `_get_global_filters_for_name` **(Stateful Encapsulated Methods)** (Impact: 16.9)
    * *Intent:* # For functions and classes the defaults don't belong to the # function and get inferred in the valu...
  * `parent_scope` **(Compute Cores)** (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 197`, `args: 65`, `func_start: 65`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 57`, `planned_debt: 1`, `duplicate_logic: 12`
* *Architecture:* `io: 1`, `api: 68`, `import: 18`
* *Defense:* `safety: 12`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.567
  * `Choke Point (Betweenness):` 0.002179 | `Ripple Effect (Closeness):` 0.137268
  * `Imports (Out-Degree: 11):` abc, contextlib, jedi, jedi.inference, jedi.inference.base_value, jedi.inference.filters, jedi.inference.finder, jedi.inference.names...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `jedi/api/classes.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.699)
- **Top Global Matches:** file_cluster_15: 6.699, file_cluster_16: 6.876, file_cluster_12: 7.155
- **Magnitude:** 491.7 | **LOC:** 894 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **14**; blast radius 2.084; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.7%)
- **Documentation Coverage:** 27.8351% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `infer` **(Many-Argument Workhorses)** (Impact: 17.7)
    * *Intent:* """ Like :meth:`.Script.infer`, it can be useful to understand which type the current name has. Retu...
  * `docstring` **(Many-Argument Workhorses)** (Impact: 16.1)
  * `goto` **(Many-Argument Workhorses)** (Impact: 16.1)
  * `type` **(Compute Cores)** (Impact: 14.8)
    * *Intent:* """ The type of the definition. Here is an example of the value of this attribute. Let's consider th...
  * `_get_signatures` **(Stateful Encapsulated Methods)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 169
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 200`, `args: 63`, `func_start: 58`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 65`, `planned_debt: 3`
* *Architecture:* `io: 8`, `api: 45`, `import: 15`
* *Defense:* `safety: 10`, `doc: 44`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.084
  * `Choke Point (Betweenness):` 0.000479 | `Ripple Effect (Closeness):` 0.096498
  * `Imports (Out-Degree: 12):` jedi, jedi.api, jedi.api.helpers, jedi.api.keywords, jedi.cache, jedi.inference.base_value, jedi.inference.compiled.mixed, jedi.inference.gradual.conversion...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `jedi/inference/value/function.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.43)
- **Top Global Matches:** file_cluster_15: 6.43, file_cluster_16: 6.738, file_cluster_12: 7.277
- **Magnitude:** 491.32 | **LOC:** 460 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **16**; blast radius 8.333; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Complexity Load (formerly Cognitive Load) (92.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.6744% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_yield_lazy_values` **(Compute Cores)** (Impact: 33.4)
    * *Intent:* # TODO: if is_async, wrap yield statements in Awaitable/async_generator_asend for_parents = [(y, y.s...
  * `_find_overload_functions` **(Stateful Encapsulated Methods)** (Impact: 28.0)
  * `get_return_values` **(Compute Cores)** (Impact: 24.5)
  * `infer` **(Compute Cores)** (Impact: 15.8)
    * *Intent:* """ Created to be used by inheritance. """
  * `from_context` **(Many-Argument Workhorses)** (Impact: 15.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 185
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 172`, `args: 46`, `func_start: 46`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 73`, `planned_debt: 3`
* *Architecture:* `api: 48`, `import: 20`
* *Defense:* `safety: 4`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.333
  * `Choke Point (Betweenness):` 0.002421 | `Ripple Effect (Closeness):` 0.137687
  * `Imports (Out-Degree: 18):` jedi, jedi.inference, jedi.inference.base_value, jedi.inference.cache, jedi.inference.context, jedi.inference.filters, jedi.inference.gradual.annotation, jedi.inference.gradual.base...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `jedi/inference/base_value.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.086)
- **Top Global Matches:** file_cluster_12: 6.086, file_cluster_15: 6.543, file_cluster_16: 7.477
- **Magnitude:** 474.6 | **LOC:** 559 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **51** in-repo importer(s); it depends on **17**; blast radius 34.909; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.4%)
- **Documentation Coverage:** 94.1176% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `py__getattribute__` **(Many-Argument Workhorses)** (Impact: 25.5)
  * `get_type_hint` **(Compute Cores)** (Impact: 14.8)
  * `_getitem` **(Stateful Encapsulated Methods)** (Impact: 11.2)
    * *Intent:* # The actual getitem call. result = NO_VALUES unused_values = set() for index_value in index_values:...
  * `iterate` **(Compute Cores)** (Impact: 10.3)
  * `_get_value_filters` **(Stateful Encapsulated Methods)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *Api Near Db Sink:* 3 instances
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 244`, `args: 90`, `func_start: 90`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 43`, `planned_debt: 4`
* *Architecture:* `api: 79`, `import: 21`
* *Defense:* `safety: 13`, `doc: 8`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 34.909
  * `Choke Point (Betweenness):` 0.008916 | `Ripple Effect (Closeness):` 0.205278
  * `Imports (Out-Degree: 14):` functools, itertools, jedi, jedi.cache, jedi.inference, jedi.inference.arguments, jedi.inference.cache, jedi.inference.compiled...
  * `Imported By (In-Degree: 51):` (Excluded from Brief to save tokens)

### `jedi/inference/gradual/annotation.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.201)
- **Top Global Matches:** file_cluster_12: 6.201, file_cluster_15: 8.859, file_cluster_16: 9.109
- **Magnitude:** 451.46 | **LOC:** 475 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **12**; blast radius 6.109; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.7%), Complexity Load (formerly Cognitive Load) (55.5%)
- **Documentation Coverage:** 71.0526% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_find_type_from_comment_hint` **(Stateful Encapsulated Methods)** (Impact: 28.0)
  * `_infer_param` **(Stateful Encapsulated Methods)** (Impact: 26.6)
    * *Intent:* """ Infers the type of a function parameter, using type annotations. """
  * `infer_return_types` **(Compute Cores)** (Impact: 22.8)
    * *Intent:* """ Infers the type of a function's return value, according to type annotations. """
  * `infer_return_for_callable` **(Defensive Guards)** (Impact: 12.7)
  * `infer_type_vars_for_execution` **(Many-Argument Workhorses)** (Impact: 11.8)
    * *Intent:* """ Some functions use type vars that are not defined by the class, but rather only defined in the f...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 65 instances
* *State Mutation (weighted view):* 203
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 115`, `args: 24`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 73`, `planned_debt: 1`
* *Architecture:* `api: 15`, `import: 13`
* *Defense:* `safety: 15`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.109
  * `Choke Point (Betweenness):` 0.001462 | `Ripple Effect (Closeness):` 0.137687
  * `Imports (Out-Degree: 13):` inspect, jedi, jedi.inference.base_value, jedi.inference.cache, jedi.inference.compiled, jedi.inference.gradual.base, jedi.inference.gradual.generics, jedi.inference.gradual.type_var...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `jedi/inference/compiled/access.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.273)
- **Top Global Matches:** file_cluster_12: 6.273, file_cluster_5: 7.669, file_cluster_7: 8.922
- **Magnitude:** 423.6 | **LOC:** 563 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **12**; blast radius 3.432; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.3%), Connectivity (formerly Api Exposure) (69.4%), Guard Balance (formerly Safety Score) (58.3%)
- **Documentation Coverage:** 96.124% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getattr_paths` **(Defensive Guards)** (Impact: 20.2)
  * `is_allowed_getattr` **(Defensive Guards)** (Impact: 15.6)
    * *Intent:* # TODO this API is ugly. try: attr, is_get_descriptor = getattr_static(self._obj, name) except Attri...
  * `py__getitem__all_values` **(Defensive Guards)** (Impact: 12.3)
  * `get_annotation_name_and_args` **(Compute Cores)** (Impact: 10.7)
    * *Intent:* """ Returns Tuple[Optional[str], Tuple[AccessPath, ...]] """
  * `get_api_type` **(Compute Cores)** (Impact: 10.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 192`, `args: 53`, `func_start: 53`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 59`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 46`, `import: 16`
* *Defense:* `safety: 49`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.432
  * `Choke Point (Betweenness):` 0.00219 | `Ripple Effect (Closeness):` 0.122057
  * `Imports (Out-Degree: 2):` builtins, collections, inspect, jedi.inference.compiled.getattr_static, operator, pathlib, re, sys...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `jedi/api/project.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.435)
- **Top Global Matches:** file_cluster_12: 6.435, file_cluster_5: 8.745, file_cluster_7: 9.072
- **Magnitude:** 372.52 | **LOC:** 449 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **13**; blast radius 21.183; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.7%), Complexity Load (formerly Cognitive Load) (40.4%)
- **Documentation Coverage:** 43.2432% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_search_func` **(Many-Argument Workhorses)** (Impact: 35.4)
    * *Intent:* # Using a Script is they easiest way to get an empty module context. from jedi import Script s = Scr...
  * `_get_sys_path` **(Many-Argument Workhorses)** (Impact: 29.1)
    * *Intent:* """ Keep this method private for all users of jedi. However internally this one is used like a publi...
  * `get_default_project` **(Defensive Guards)** (Impact: 22.3)
    * *Intent:* """ If a project is not defined by the user, Jedi tries to define a project by itself as well as pos...
  * `wrapper` **(Compute Cores)** (Impact: 12.8)
  * `_try_to_skip_duplicates` **(Stateful Encapsulated Methods)** (Impact: 10.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 180
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 98`, `args: 23`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 68`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 13`, `import: 14`
* *Defense:* `safety: 14`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.183
  * `Choke Point (Betweenness):` 0.00799 | `Ripple Effect (Closeness):` 0.175724
  * `Imports (Out-Degree: 12):` itertools, jedi, jedi.api.completion, jedi.api.environment, jedi.api.exceptions, jedi.api.helpers, jedi.file_io, jedi.inference.cache...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `jedi/inference/references.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.17)
- **Top Global Matches:** file_cluster_4: 6.17, file_cluster_16: 9.524, file_cluster_12: 10.172
- **Magnitude:** 367.88 | **LOC:** 320 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **9**; blast radius 3.945; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.6%), Complexity Load (formerly Cognitive Load) (70.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `find_references` **(Many-Argument Workhorses)** (Impact: 46.6)
  * `recurse_find_python_folders_and_files` **(Compute Cores)** (Impact: 20.7)
  * `_find_python_files_in_sys_path` **(Stateful Encapsulated Methods)** (Impact: 18.3)
  * `search_in_file_ios` **(Many-Argument Workhorses)** (Impact: 18.1)
  * `gitignored_paths` **(Type Conversions)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 160
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 64`, `args: 17`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 60`
* *Architecture:* `io: 2`, `api: 8`, `import: 9`
* *Defense:* `safety: 9`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.945
  * `Choke Point (Betweenness):` 0.001569 | `Ripple Effect (Closeness):` 0.136028
  * `Imports (Out-Degree: 6):` jedi.debug, jedi.file_io, jedi.inference.filters, jedi.inference.gradual.conversion, jedi.inference.imports, jedi.inference.names, os, parso...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `jedi/parser_utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.454)
- **Top Global Matches:** file_cluster_4: 7.454, file_cluster_12: 7.852, file_cluster_15: 9.929
- **Magnitude:** 364.1 | **LOC:** 346 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); it depends on **8**; blast radius 13.816; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.8%), Connectivity (formerly Api Exposure) (66.3%)
- **Documentation Coverage:** 43.5897% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_parent_scope` **(Compute Cores)** (Impact: 29.2)
    * *Intent:* """ Returns the underlying scope. """
  * `get_executable_nodes` **(Defensive Guards)** (Impact: 27.7)
    * *Intent:* """ For static analysis. """
  * `get_signature` **(Many-Argument Workhorses)** (Impact: 23.6)
  * `get_following_comment_same_line` **(Defensive Guards)** (Impact: 12.8)
    * *Intent:* """ returns (as string) any comment that appears on the same line, after the node, including the # "...
  * `expr_is_dotted` **(Compute Cores)** (Impact: 12.2)
    * *Intent:* """ Checks if a path looks like `name` or `name.foo.bar` and not `name()`. """
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 52 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 159
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 101`, `args: 24`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 55`, `planned_debt: 3`
* *Architecture:* `api: 18`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 14`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.816
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.177901
  * `Imports (Out-Degree: 0):` ast, inspect, parso, parso.cache, parso.python, re, textwrap, weakref
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `jedi/inference/gradual/typeshed.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.609)
- **Top Global Matches:** file_cluster_4: 8.609, file_cluster_12: 11.153, file_cluster_6: 12.45
- **Magnitude:** 351.32 | **LOC:** 311 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **12**; blast radius 4.428; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.5%), Complexity Load (formerly Cognitive Load) (65.3%)
- **Documentation Coverage:** 89.4737% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_try_to_load_stub` **(Many-Argument Workhorses)** (Impact: 60.8)
  * `wrapper` **(Many-Argument Workhorses)** (Impact: 30.9)
  * `_load_from_typeshed` **(Stateful Encapsulated Methods)** (Impact: 21.5)
  * `import_module_decorator` **(Compute Cores)** (Impact: 18.7)
  * `_get_typeshed_directories` **(Stateful Encapsulated Methods)** (Impact: 17.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 146
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 63`, `args: 13`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 54`, `planned_debt: 10`
* *Architecture:* `io: 14`, `api: 6`, `import: 12`
* *Defense:* `safety: 12`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.428
  * `Choke Point (Betweenness):` 0.000629 | `Ripple Effect (Closeness):` 0.120752
  * `Imports (Out-Degree: 8):` collections, functools, jedi, jedi.file_io, jedi.inference.base_value, jedi.inference.gradual.stub_value, jedi.inference.value, jedi.parser_utils...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `jedi/inference/arguments.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.991)
- **Top Global Matches:** file_cluster_12: 5.991, file_cluster_16: 8.82, file_cluster_15: 8.856
- **Magnitude:** 344.82 | **LOC:** 336 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **12**; blast radius 8.021; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.6%)
- **Documentation Coverage:** 84.7826% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `iterate_argument_clinic` **(Many-Argument Workhorses)** (Impact: 27.9)
    * *Intent:* """Uses a list with argument clinic information (see PEP 436)."""
  * `unpack` **(Compute Cores)** (Impact: 27.9)
  * `unpack_arglist` **(Defensive Guards)** (Impact: 16.7)
  * `_parse_argument_clinic` **(Stateful Encapsulated Methods)** (Impact: 16.6)
  * `_star_star_dict` **(Stateful Encapsulated Methods)** (Impact: 16.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 105`, `args: 28`, `func_start: 28`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 47`, `planned_debt: 2`
* *Architecture:* `api: 23`, `import: 12`
* *Defense:* `safety: 14`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.021
  * `Choke Point (Betweenness):` 0.000776 | `Ripple Effect (Closeness):` 0.164223
  * `Imports (Out-Degree: 10):` itertools, jedi, jedi.inference, jedi.inference.base_value, jedi.inference.cache, jedi.inference.lazy_value, jedi.inference.names, jedi.inference.utils...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `test/test_api/test_signatures.py` (PYTHON) | Magnitude: 35.42 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 43, args: 21, test: 8
- `test/completion/precedence.py` (PYTHON) | Magnitude: 61.22 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 22, core_var_decl: 22, design_snake_case: 22, indent_spaces: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `test/completion/async_.py` (PYTHON) | Magnitude: 137.58 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 40, concurrency: 27, args: 15
- `test/completion/basic.py` (PYTHON) | Magnitude: 178.66 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 65, state_mutation: 33, core_var_decl: 31
- `jedi/inference/gradual/utils.py` (PYTHON) | Magnitude: 33.78 | Delta: **0.124** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 9, state_mutation: 9, core_var_decl: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `jedi/api/errors.py` (PYTHON) | Magnitude: 25.5 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 17, api: 9, args: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `test/completion/named_param.py` (PYTHON) | Magnitude: 34.28 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 27, core_var_decl: 20, design_snake_case: 20, args: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `test/test_inference/test_context.py` (PYTHON) | Magnitude: 8.3 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 10, safety: 7, args: 2
- `jedi/inference/gradual/generics.py` (PYTHON) | Magnitude: 73.5 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 48, args: 19, func_start: 17
- `conftest.py` (PYTHON) | Magnitude: 101.66 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 51, test: 32, args: 23
- `test/test_parso_integration/test_parser_utils.py` (PYTHON) | Magnitude: 46.38 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 49, indent_spaces: 47, safety: 21, state_mutation: 13
- `test/test_inference/test_literals.py` (PYTHON) | Magnitude: 15.06 | Delta: **0.089** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 21, indent_spaces: 18, safety: 14, core_var_decl: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `jedi/inference/dynamic_params.py` (PYTHON) | Magnitude: 221.4 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 122, structural_boundaries: 61, core_var_decl: 41, design_snake_case: 40
- `jedi/plugins/pytest.py` (PYTHON) | Magnitude: 304.2 | Delta: **0.153** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 178, structural_boundaries: 75, branch: 68, core_var_decl: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `test/test_inference/test_fstring.py` (PYTHON) | Magnitude: 3.92 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `jedi/inference/flow_analysis.py` (PYTHON) | Magnitude: 174.46 | Delta: **0.112** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 81, structural_boundaries: 45, branch: 42, state_mutation: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `jedi/cache.py` (PYTHON) | Magnitude: 92.26 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 33, state_mutation: 21, core_var_decl: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `test/completion/completion.py` (PYTHON) | Magnitude: 7.34 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 12, safety_bypasses: 5, branch: 4

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `jedi/inference/value/function.py` -> Churn: **100.0%** | Cog Load: 92.2813% | Debt: 11.0614%
- `jedi/inference/syntax_tree.py` -> Churn: **99.66%** | Cog Load: 71.1655% | Debt: 12.1243%
- `jedi/api/completion.py` -> Churn: **58.68%** | Cog Load: 75.4759% | Debt: 8.3173%
- `jedi/inference/context.py` -> Churn: **58.68%** | Cog Load: 84.4275% | Debt: 99.9987%
- `jedi/inference/filters.py` -> Churn: **58.68%** | Cog Load: 57.8291% | Debt: 9.0799%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `jedi/api/completion.py` -> **Dave Halter** (100.0% isolated ownership) | Magnitude: 875.3
- `jedi/inference/names.py` -> **Dave Halter** (100.0% isolated ownership) | Magnitude: 686.48
- `jedi/api/__init__.py` -> **Dave Halter** (100.0% isolated ownership) | Magnitude: 638.78
- `jedi/inference/imports.py` -> **Dave Halter** (100.0% isolated ownership) | Magnitude: 564.38
- `jedi/inference/value/instance.py` -> **Dave Halter** (100.0% isolated ownership) | Magnitude: 543.02

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `jedi/api/__init__.py` -> **Severity: 2.829** (Bridge: 0.0283 * Flux: 100.0%)
- `jedi/inference/base_value.py` -> **Severity: 0.891** (Bridge: 0.0089 * Flux: 99.9665%)
- `jedi/api/project.py` -> **Severity: 0.799** (Bridge: 0.008 * Flux: 100.0%)
- `jedi/inference/names.py` -> **Severity: 0.643** (Bridge: 0.0064 * Flux: 100.0%)
- `jedi/inference/__init__.py` -> **Severity: 0.565** (Bridge: 0.0057 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `jedi/inference/__init__.py` -> **Severity: 14.912** (Embedded: 0.1828 * Error Risk: 81.5562%)
- `jedi/api/__init__.py` -> **Severity: 14.793** (Embedded: 0.1866 * Error Risk: 79.2702%)
- `jedi/inference/helpers.py` -> **Severity: 13.677** (Embedded: 0.175 * Error Risk: 78.1336%)
- `jedi/parser_utils.py` -> **Severity: 13.662** (Embedded: 0.1779 * Error Risk: 76.7931%)
- `jedi/api/project.py` -> **Severity: 13.471** (Embedded: 0.1757 * Error Risk: 76.6596%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `jedi/inference/base_value.py` -> **Severity: 3285.551** (Blast Radius: 34.909 * Doc Risk: 94.1176%)
- `jedi/inference/__init__.py` -> **Severity: 2217.481** (Blast Radius: 24.509 * Doc Risk: 90.4762%)
- `jedi/inference/names.py` -> **Severity: 1573.67** (Blast Radius: 16.452 * Doc Risk: 95.6522%)
- `jedi/inference/cache.py` -> **Severity: 1441.574** (Blast Radius: 15.569 * Doc Risk: 92.5926%)
- `jedi/plugins/__init__.py` -> **Severity: 1407.083** (Blast Radius: 16.885 * Doc Risk: 83.3333%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 140 literal sites + 9 sites through wrappers = 149

- `reraise_getitem_errors` (function, panics_and_aborts, primitive): 5 call sites in 2 files -- `jedi/inference/helpers.py`
- `raises` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `test/static_analysis/keywords.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 7608 call pairs -- scoped 41.5%, unique 0.0%, ambiguous 19.0%, external 39.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 7595 | 41.6% | 0.0% | 19.0% | 39.4% |
| shell | 11 | 0.0% | 0.0% | 0.0% | 100.0% |
| c | 2 | 0.0% | 0.0% | 0.0% | 100.0% |

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
