# ARCHITECTURAL_BRIEF: black
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/psf/black.git` |
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
- **Scope:** 336 analyzed artifact(s), 28986 LOC.
- **Load-bearing artifact:** `src/black/mode.py` -- 19 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `tests/test_black.py` -- pulls in 40 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/black/trans.py` at magnitude 1989.46 (structural weight, not risk).
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
| Total Artifacts | 453 |
| Analyzed Artifacts (Scanned) | 336 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 117 |
| Total LOC | 28986 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 74.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3327 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2619 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.1982 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 301 | 27754 | 89.6% |
| YAML | 16 | 1059 | 4.8% |
| MARKDOWN | 11 | 0 | 3.3% |
| PLAINTEXT | 6 | 0 | 1.8% |
| DOCKERFILE | 1 | 18 | 0.3% |
| JSON | 1 | 155 | 0.3% |

## 4.1 SOURCE ENCODINGS
All 336 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 31%, Declarative / Non-Code 23%, Generic / Templated Code Files 12%, Interface Declarations Files 12%, Parameter Forwarders Files 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 319 | 94.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 17 | 5.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 117*

**Composition by Extension & Reason:**
- `.md`: 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 8002 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 41441 LOC)
- `no_extension`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 9x Excluded (Unsupported Extension: '.toml'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ipynb`: 6x Excluded (Unsupported Extension: '.ipynb')
- `.cfg`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.diff`: 4x Excluded (Unsupported Extension: '.diff')
- `.pie`: 3x Excluded (Unsupported Extension: '.pie'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.ini')
- `.vim`: 2x Excluded (Unsupported Extension: '.vim')
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.cff`: 1x Excluded (Unsupported Extension: '.cff')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.2 | 10.8 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.4 | 44.3 | 53.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.0 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 84.9 | 7.3 | 3.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 9.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 10.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 23.1 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.5 | 0.5 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 79.7 | 5.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 49.0 | 50.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 411 | 47 | 2 | `tests/test_black.py` |
| cleanup | 17 | 7 | 0 | `tests/data/cases/cantfit.py` |
| guards | 1097 | 98 | 7 | `tests/test_black.py` |
| danger | 1365 | 135 | 13 | `tests/data/cases/remove_except_types_parens.py` |
| concurrency | 855 | 59 | 3 | `tests/data/cases/remove_await_parens.py` |
| connectivity | 1932 | 166 | 14 | `tests/test_black.py` |
| io | 235 | 41 | 1 | `action/main.py` |
| crypto | 2 | 2 | 0 | `src/black/cache.py` |
| ipc | 14 | 10 | 0 | `scripts/diff_shades_gha_helper.py` |
| time | 15 | 4 | 0 | `tests/data/cases/conditional_expression.py` |
| serialization | 1 | 1 | 0 | `src/black/cache.py` |
| regex | 69 | 22 | 0 | `tests/test_black.py` |
| events | 21 | 7 | 0 | `src/black/__init__.py` |
| tests | 513 | 32 | 0 | `tests/test_black.py` |
| docs | 929 | 98 | 6 | `tests/data/cases/multiline_strings.py` |
| debt | 1323 | 125 | 10 | `tests/data/cases/preview_long_strings__regression.py` |
| mutation | 9595 | 195 | 64 | `tests/test_black.py` |
| dead_code | 338 | 49 | 1 | `tests/test_black.py` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 8 | 3 | 0 | `tests/data/cases/expression.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `action/main.py` (Hits: 31)
- `tests/data/cases/remove_with_brackets.py` (Hits: 30)
- `tests/test_black.py` (Hits: 24)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **mode.py** (`src/black/mode.py`) — 19 inbound connections
2. **__init__.py** (`src/black/__init__.py`) — 14 inbound connections
3. **nodes.py** (`src/black/nodes.py`) — 10 inbound connections
4. **output.py** (`src/black/output.py`) — 10 inbound connections
5. **report.py** (`src/black/report.py`) — 6 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_black.py** (`tests/test_black.py`) — 40 outbound dependencies
2. **__init__.py** (`src/black/__init__.py`) — 38 outbound dependencies
3. **files.py** (`src/black/files.py`) — 21 outbound dependencies
4. **import_spacing.py** (`tests/data/cases/import_spacing.py`) — 21 outbound dependencies
5. **concurrency.py** (`src/black/concurrency.py`) — 20 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `main` **(Many-Argument Workhorses)** (@ `src/black/__init__.py`) -> Impact: **311.8** | LOC: 223
- `whitespace` **(Many-Argument Workhorses)** (@ `src/black/nodes.py`) -> Impact: **240.4** | LOC: 249
  * *Intent:* """Return whitespace prefix if needed for the given `leaf`. `complex_subscript` signals whether the given leaf is part of a subscription which has non...
- `normalize_invisible_parens` **(Many-Argument Workhorses)** (@ `src/black/linegen.py`) -> Impact: **136.8** | LOC: 143
- `get_features_used` **(Many-Argument Workhorses)** (@ `src/black/__init__.py`) -> Impact: **127.9** | LOC: 168
- `_maybe_empty_lines_for_class_or_def` **(Many-Argument Workhorses)** (@ `src/black/lines.py`) -> Impact: **95.6** | LOC: 79
- `_maybe_empty_lines` **(Many-Argument Workhorses)** (@ `src/black/lines.py`) -> Impact: **91.2** | LOC: 92
- `maybe_make_parens_invisible_in_atom` **(Many-Argument Workhorses)** (@ `src/black/linegen.py`) -> Impact: **90.2** | LOC: 111
- `get_sources` **(Many-Argument Workhorses)** (@ `src/black/__init__.py`) -> Impact: **84.4** | LOC: 96
- `is_split_before_delimiter` **(Compute Cores)** (@ `src/black/brackets.py`) -> Impact: **84.4** | LOC: 94
  * *Intent:* """Return the priority of the `leaf` delimiter, given a line break before it. The delimiter priorities returned here are from those delimiters that wo...
- `_generate_ignored_nodes_from_fmt_skip` **(Many-Argument Workhorses)** (@ `src/black/comments.py`) -> Impact: **82.3** | LOC: 126

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/black` | 24 | 11036.46 | 33.8% | 5.84% |
| `tests` | 15 | 3357.04 | 13.36% | 0.0% |
| `scripts` | 10 | 647.92 | 38.42% | 19.84% |
| `src/blackd` | 4 | 479.36 | 69.27% | 0.0% |
| `.github/workflows` | 13 | 177.1 | 5.77% | 3.99% |
| `action` | 1 | 123.68 | 67.27% | 10.02% |
| `__monolith__` | 8 | 81.6 | 1.51% | 1.7% |
| `src/black/resources` | 2 | 28.62 | 0.0% | 0.0% |
| `profiling` | 1 | 19.04 | 0.0% | 0.0% |
| `.github` | 3 | 17.62 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `scripts/release_tests.py` -> **100.0%** Exposure
- `scripts/fuzz.py` -> **62.2459%** Exposure
- `.github/workflows/diff_shades.yml` -> **51.932%** Exposure
- `src/black/handle_ipynb_magics.py` -> **42.6996%** Exposure
- `src/black/schema.py` -> **37.7541%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `scripts/check_pre_commit_rev_in_example.py` -> **100.0%** Exposure
- `scripts/check_version_in_basics_example.py` -> **100.0%** Exposure
- `scripts/diff_shades_gha_helper.py` -> **100.0%** Exposure
- `scripts/generate_schema.py` -> **100.0%** Exposure
- `scripts/make_width_table.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/test_black.py` -> **155** Orphaned Functions | **12** Duplicates
- `tests/data/cases/docstring.py` -> **0** Orphaned Functions | **68** Duplicates
- `tests/data/cases/dummy_implementations.py` -> **0** Orphaned Functions | **58** Duplicates
- `tests/data/cases/stub.py` -> **0** Orphaned Functions | **44** Duplicates
- `tests/test_ipynb.py` -> **40** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `558` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/black/trans.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.003)
- **Top Global Matches:** file_cluster_6: 7.003, file_cluster_4: 10.828, file_cluster_8: 15.99
- **Magnitude:** 1989.46 | **LOC:** 2561 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **15**; blast radius 4.939; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (46.6%)
- **Documentation Coverage:** 47.4747% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_transform` **(Many-Argument Workhorses)** (Impact: 81.5)
  * `_merge_one_string_group` **(Many-Argument Workhorses)** (Impact: 56.8)
  * `do_match` **(Compute Cores)** (Impact: 55.5)
  * `do_transform` **(Many-Argument Workhorses)** (Impact: 54.1)
  * `_get_max_string_length` **(Many-Argument Workhorses)** (Impact: 49.4)
    * *Intent:* """ Calculates the max string length used when attempting to determine whether or not the target str...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 293 instances
* *State Mutation (weighted view):* 942
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 402`, `structural_boundaries: 338`, `args: 64`, `func_start: 62`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 356`, `fragile_debt: 2`
* *Architecture:* `api: 46`, `import: 15`
* *Defense:* `safety: 20`, `doc: 54`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.939
  * `Choke Point (Betweenness):` 0.000438 | `Ripple Effect (Closeness):` 0.019343
  * `Imports (Out-Degree: 8):` abc, black.comments, black.lines, black.mode, black.nodes, black.rusty, black.strings, blib2to3.pgen2...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/black/linegen.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.675)
- **Top Global Matches:** file_cluster_6: 6.675, file_cluster_4: 11.422, file_cluster_8: 14.984
- **Magnitude:** 1923.24 | **LOC:** 2049 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 44.4%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **17**; blast radius 3.415; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.4%), Complexity Load (formerly Cognitive Load) (55.2%)
- **Documentation Coverage:** 57.3913% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `normalize_invisible_parens` **(Many-Argument Workhorses)** (Impact: 136.8)
  * `maybe_make_parens_invisible_in_atom` **(Many-Argument Workhorses)** (Impact: 90.2)
  * `transform_line` **(Many-Argument Workhorses)** (Impact: 66.4)
  * `_first_right_hand_split` **(Many-Argument Workhorses)** (Impact: 58.7)
  * `_maybe_split_omitting_optional_parens` **(Many-Argument Workhorses)** (Impact: 57.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 203 instances
* *State Mutation (weighted view):* 650
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 490`, `structural_boundaries: 360`, `args: 64`, `func_start: 64`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 244`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 4`
* *Architecture:* `io: 1`, `api: 52`, `import: 17`
* *Defense:* `safety: 36`, `doc: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.415
  * `Choke Point (Betweenness):` 0.000719 | `Ripple Effect (Closeness):` 0.023881
  * `Imports (Out-Degree: 8):` black.brackets, black.comments, black.lines, black.mode, black.nodes, black.numerics, black.strings, black.trans...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/test_black.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.799)
- **Top Global Matches:** file_cluster_5: 7.799, file_cluster_12: 8.385, file_cluster_0: 9.477
- **Magnitude:** 1722.1 | **LOC:** 3302 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **40**; blast radius 2.474; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.0%), Guard Balance (formerly Safety Score) (59.0%), Complexity Load (formerly Cognitive Load) (29.3%), Concurrency Surface (formerly Concurrency) (25.9%)
- **Documentation Coverage:** 92.8375% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assert_collected_sources` **(Many-Argument Workhorses)** (Impact: 37.6)
  * `test_cache_key` **(Defensive Guards)** (Impact: 17.0)
    * *Intent:* # Test that all members of the mode enum affect the cache key. for field in fields(Mode): values: li...
  * `test_tab_comment_indentation` **(Compute Cores)** (Impact: 10.4)
  * `test_cache_file_length` **(Type Conversions)** (Impact: 9.6)
  * `tracefunc` **(Generic / Templated Code)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 115 instances
* *Concurrency (weighted view):* 33
* *State Mutation (weighted view):* 838
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 685`, `args: 209`, `func_start: 183`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 63`, `high_risk_execution: 3`, `state_mutation: 608`, `planned_debt: 8`, `duplicate_logic: 12`, `unreferenced_by_name: 155`
* *Architecture:* `io: 24`, `api: 187`, `concurrency: 8`, `import: 40`
* *Defense:* `safety: 149`, `doc: 45`, `test: 238`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` __future__, annotations, asyncio, black, black.cache, black.debug, black.files, black.mode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/black/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.832)
- **Top Global Matches:** file_cluster_6: 6.832, file_cluster_4: 12.356, file_cluster_8: 14.066
- **Magnitude:** 1423.88 | **LOC:** 1704 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 55.6%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **38**; blast radius 16.629; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.1%), Connectivity (formerly Api Exposure) (60.1%)
- **Documentation Coverage:** 79.0323% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 311.8)
  * `get_features_used` **(Many-Argument Workhorses)** (Impact: 127.9)
  * `get_sources` **(Many-Argument Workhorses)** (Impact: 84.4)
  * `reformat_one` **(Many-Argument Workhorses)** (Impact: 65.2)
    * *Intent:* # diff-shades depends on being to monkeypatch this function to operate. I know it's # not ideal, but...
  * `read_pyproject_toml` **(Many-Argument Workhorses)** (Impact: 35.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 136 instances
* *State Mutation (weighted view):* 424
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 323`, `structural_boundaries: 286`, `args: 34`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 152`, `fragile_debt: 5`
* *Architecture:* `io: 14`, `api: 29`, `concurrency: 1`, `import: 41`
* *Defense:* `safety: 37`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.629
  * `Choke Point (Betweenness):` 0.002515 | `Ripple Effect (Closeness):` 0.041978
  * `Imports (Out-Degree: 15):` _black_version, black.cache, black.comments, black.concurrency, black.const, black.files, black.handle_ipynb_magics, black.linegen...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `src/black/lines.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.882)
- **Top Global Matches:** file_cluster_4: 7.882, file_cluster_6: 10.863, file_cluster_9: 12.904
- **Magnitude:** 1123.2 | **LOC:** 1122 | **CtrlFlow:** 42.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 4.303; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.3%), Connectivity (formerly Api Exposure) (59.8%)
- **Documentation Coverage:** 28.3951% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_maybe_empty_lines_for_class_or_def` **(Many-Argument Workhorses)** (Impact: 95.6)
  * `_maybe_empty_lines` **(Many-Argument Workhorses)** (Impact: 91.2)
  * `can_omit_invisible_parens` **(Many-Argument Workhorses)** (Impact: 74.2)
  * `is_line_short_enough` **(Many-Argument Workhorses)** (Impact: 66.3)
    * *Intent:* """For non-multiline strings, return True if `line` is no longer than `line_length`. For multiline s...
  * `append` **(Many-Argument Workhorses)** (Impact: 35.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 120 instances
* *State Mutation (weighted view):* 375
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 321`, `structural_boundaries: 244`, `args: 44`, `func_start: 43`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 135`, `planned_debt: 1`
* *Architecture:* `api: 42`, `import: 11`
* *Defense:* `safety: 13`, `doc: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.303
  * `Choke Point (Betweenness):` 0.000165 | `Ripple Effect (Closeness):` 0.029934
  * `Imports (Out-Degree: 4):` black.brackets, black.mode, black.nodes, black.strings, blib2to3.pgen2, blib2to3.pytree, collections.abc, dataclasses...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/black/nodes.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.689)
- **Top Global Matches:** file_cluster_0: 8.689, file_cluster_15: 9.909, file_cluster_9: 10.455
- **Magnitude:** 924.44 | **LOC:** 1112 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **9**; blast radius 20.297; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (84.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.6%)
- **Documentation Coverage:** 22.6087% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `whitespace` **(Many-Argument Workhorses)** (Impact: 240.4)
    * *Intent:* """Return whitespace prefix if needed for the given `leaf`. `complex_subscript` signals whether the ...
  * `is_one_sequence_between` **(Many-Argument Workhorses)** (Impact: 26.3)
  * `is_simple_decorator_trailer` **(Compute Cores)** (Impact: 22.0)
    * *Intent:* """Return True iff `node` is a trailer valid in a simple decorator"""
  * `is_docstring` **(Compute Cores)** (Impact: 17.1)
  * `is_import` **(Compute Cores)** (Impact: 14.9)
    * *Intent:* """Return True if the given leaf starts an import statement."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 64 instances
* *State Mutation (weighted view):* 199
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 304`, `structural_boundaries: 415`, `args: 57`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `state_mutation: 71`, `planned_debt: 1`
* *Architecture:* `api: 58`, `import: 9`
* *Defense:* `safety: 21`, `doc: 47`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.297
  * `Choke Point (Betweenness):` 0.000594 | `Ripple Effect (Closeness):` 0.048358
  * `Imports (Out-Degree: 3):` black.cache, black.mode, black.strings, blib2to3, blib2to3.pgen2, blib2to3.pytree, collections.abc, mypy_extensions...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/black/comments.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.059)
- **Top Global Matches:** file_cluster_6: 7.059, file_cluster_4: 10.136, file_cluster_8: 16.742
- **Magnitude:** 806.76 | **LOC:** 828 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 55.6%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 4.303; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.9%), Complexity Load (formerly Cognitive Load) (48.7%)
- **Documentation Coverage:** 53.125% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_generate_ignored_nodes_from_fmt_skip` **(Many-Argument Workhorses)** (Impact: 82.3)
  * `_handle_regular_fmt_block` **(Many-Argument Workhorses)** (Impact: 76.3)
  * `_handle_comment_only_fmt_block` **(Many-Argument Workhorses)** (Impact: 37.9)
  * `generate_ignored_nodes` **(Many-Argument Workhorses)** (Impact: 36.4)
  * `list_comments` **(Many-Argument Workhorses)** (Impact: 32.2)
    * *Intent:* """Return a list of :class:`ProtoComment` objects parsed from the given `prefix`."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 112 instances
* *State Mutation (weighted view):* 345
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 143`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 121`, `dead_code: 1`
* *Architecture:* `api: 13`, `import: 9`
* *Defense:* `safety: 16`, `doc: 20`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.029934
  * `Imports (Out-Degree: 2):` black.mode, black.nodes, blib2to3.pgen2, blib2to3.pytree, collections.abc, dataclasses, functools, re...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tests/test_blackd.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.491)
- **Top Global Matches:** file_cluster_0: 6.491, file_cluster_13: 10.053, file_cluster_15: 10.437
- **Magnitude:** 803.9 | **LOC:** 450 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 2.474; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (55.2%), Complexity Load (formerly Cognitive Load) (50.0%), Connectivity (formerly Api Exposure) (12.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_blackd_format_code_limits_executor_queue` **(Type Conversions)** (Impact: 6.9)
  * `test_preserves_line_endings` **(Generic / Templated Code)** (Impact: 3.2)
  * `test_blackd_main` **(Generic / Templated Code)** (Impact: 3.1)
  * `test_normalizes_line_endings` **(Generic / Templated Code)** (Impact: 3.1)
  * `test_blackd_python_variant` **(Generic / Templated Code)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 88 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 563
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 177`, `args: 64`, `func_start: 46`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 82`, `planned_debt: 1`, `duplicate_logic: 6`, `unreferenced_by_name: 33`
* *Architecture:* `io: 2`, `api: 50`, `concurrency: 123`, `import: 15`
* *Defense:* `safety: 4`, `test: 44`, `sync_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` aiohttp, aiohttp.test_utils, asyncio, black, blackd, blackd.client, click.testing, concurrent.futures...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/black/strings.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.534)
- **Top Global Matches:** file_cluster_6: 8.534, file_cluster_4: 9.612, file_cluster_9: 15.882
- **Magnitude:** 423.66 | **LOC:** 392 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **6**; blast radius 10.198; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (57.5%)
- **Documentation Coverage:** 24.1379% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `normalize_fstring_quotes` **(Many-Argument Workhorses)** (Impact: 37.2)
  * `normalize_string_quotes` **(Compute Cores)** (Impact: 27.6)
    * *Intent:* """Prefer double quotes but only if it doesn't cause more escaping. Adds or removes backslashes as a...
  * `fix_multiline_docstring` **(Defensive Guards)** (Impact: 14.9)
    * *Intent:* # https://www.python.org/dev/peps/pep-0257/#handling-docstring-indentation assert docstring, "INTERN...
  * `normalize_string_prefix` **(Defensive Guards)** (Impact: 13.5)
    * *Intent:* """Make all string prefixes lowercase."""
  * `normalize_unicode_escape_sequences` **(Defensive Guards)** (Impact: 12.8)
    * *Intent:* """Replace hex codes in Unicode escape sequences with lowercase representation."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 77 instances
* *State Mutation (weighted view):* 236
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 67`, `args: 15`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 82`
* *Architecture:* `io: 2`, `api: 14`, `import: 7`
* *Defense:* `safety: 7`, `doc: 18`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.198
  * `Choke Point (Betweenness):` 0.00025 | `Ripple Effect (Closeness):` 0.03493
  * `Imports (Out-Degree: 1):` black._width_table, blib2to3.pytree, functools, re, sys, typing
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/black/ranges.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.605)
- **Top Global Matches:** file_cluster_4: 8.605, file_cluster_5: 10.735, file_cluster_12: 10.988
- **Magnitude:** 414.66 | **LOC:** 535 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 6.023; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.5%), Complexity Load (formerly Cognitive Load) (41.7%)
- **Documentation Coverage:** 70.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_convert_unchanged_line_by_line` **(Stateful Encapsulated Methods)** (Impact: 37.2)
    * *Intent:* """Converts unchanged to STANDALONE_COMMENT line by line."""
  * `adjusted_lines` **(Many-Argument Workhorses)** (Impact: 21.9)
  * `_get_line_range` **(Stateful Encapsulated Methods)** (Impact: 18.2)
    * *Intent:* """Returns the line range of this node or list of nodes."""
  * `_calculate_lines_mappings` **(Many-Argument Workhorses)** (Impact: 16.0)
  * `_convert_nodes_to_standalone_comment` **(Stateful Encapsulated Methods)** (Impact: 15.3)
    * *Intent:* """Convert nodes to STANDALONE_COMMENT by modifying the tree inline."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 69 instances
* *State Mutation (weighted view):* 213
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 76`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 75`
* *Architecture:* `api: 8`, `import: 5`
* *Defense:* `safety: 8`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.023
  * `Choke Point (Betweenness):` 7.1e-05 | `Ripple Effect (Closeness):` 0.026959
  * `Imports (Out-Degree: 1):` black.nodes, blib2to3.pgen2.token, collections.abc, dataclasses, difflib
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/black/files.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.364)
- **Top Global Matches:** file_cluster_4: 11.364, file_cluster_6: 12.062, file_cluster_5: 13.297
- **Magnitude:** 334.72 | **LOC:** 427 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **21**; blast radius 3.591; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.7%), Connectivity (formerly Api Exposure) (44.9%)
- **Documentation Coverage:** 67.7419% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `gen_python_files` **(Many-Argument Workhorses)** (Impact: 67.4)
  * `find_project_root` **(Compute Cores)** (Impact: 30.2)
  * `strip_specifier_set` **(Type Conversions)** (Impact: 12.5)
    * *Intent:* """Strip minor versions for some specifiers in the specifier set. For background on version specifie...
  * `path_is_excluded` **(Type Conversions)** (Impact: 12.4)
  * `_path_is_ignored` **(Stateful Encapsulated Methods)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 109`, `args: 18`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 42`
* *Architecture:* `io: 5`, `api: 14`, `import: 22`
* *Defense:* `safety: 21`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.591
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.024651
  * `Imports (Out-Degree: 4):` black.handle_ipynb_magics, black.mode, black.output, black.report, collections.abc, colorama, colorama.initialise, functools...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/black/brackets.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.805)
- **Top Global Matches:** file_cluster_4: 7.805, file_cluster_0: 10.479, file_cluster_15: 11.68
- **Magnitude:** 304.02 | **LOC:** 384 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 3.75; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.3%), Connectivity (formerly Api Exposure) (58.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `is_split_before_delimiter` **(Compute Cores)** (Impact: 84.4)
    * *Intent:* """Return the priority of the `leaf` delimiter, given a line break before it. The delimiter prioriti...
  * `mark` **(Many-Argument Workhorses)** (Impact: 28.9)
    * *Intent:* """Mark `leaf` with bracket-related metadata. Keep track of delimiters. All leaves receive an int `b...
  * `get_leaves_inside_matching_brackets` **(Defensive Guards)** (Impact: 15.5)
    * *Intent:* """Return leaves that are inside matching brackets. The input `leaves` can have non-matching bracket...
  * `max_delimiter_priority_in_atom` **(Defensive Guards)** (Impact: 12.6)
    * *Intent:* """Return maximum delimiter priority inside `node`. This is specific to atoms with contents containe...
  * `maybe_decrement_after_for_loop_variable` **(Generic / Templated Code)** (Impact: 9.3)
    * *Intent:* """See `maybe_increment_for_loop_variable` above for explanation."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 86
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 107`, `args: 15`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 32`
* *Architecture:* `api: 16`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 8`, `doc: 17`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.75
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.02171
  * `Imports (Out-Degree: 1):` black.nodes, blib2to3.pgen2, blib2to3.pytree, collections.abc, dataclasses, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/black/handle_ipynb_magics.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.994)
- **Top Global Matches:** file_cluster_5: 6.994, file_cluster_12: 8.158, file_cluster_0: 8.965
- **Magnitude:** 302.14 | **LOC:** 516 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **15**; blast radius 4.704; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.6%), Connectivity (formerly Api Exposure) (52.9%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visit_Expr` **(Many-Argument Workhorses)** (Impact: 21.1)
    * *Intent:* """Look for magics in body of cell. For examples, !ls !!ls ?ls ??ls
  * `visit_Assign` **(Many-Argument Workhorses)** (Impact: 13.7)
    * *Intent:* """Look for system assign magics. For example, black_version = !black --version env = %env var would...
  * `validate_cell` **(Compute Cores)** (Impact: 10.0)
  * `remove_trailing_semicolon` **(Compute Cores)** (Impact: 10.0)
    * *Intent:* """Remove trailing semicolon from Jupyter notebook cell. For example, fig, ax = plt.subplots() ax.pl...
  * `put_trailing_semicolon_back` **(Compute Cores)** (Impact: 9.8)
    * *Intent:* """Put trailing semicolon back if cell originally had it. Mirrors the logic in `quiet` from `IPython...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 84`, `args: 19`, `func_start: 19`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 52`, `fragile_debt: 4`
* *Architecture:* `api: 19`, `import: 16`
* *Defense:* `safety: 13`, `doc: 17`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.704
  * `Choke Point (Betweenness):` 0.000159 | `Ripple Effect (Closeness):` 0.026959
  * `Imports (Out-Degree: 4):` IPython.core.inputtransformer2, ast, black.mode, black.output, black.report, collections, collections.abc, dataclasses...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/black/concurrency.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.53)
- **Top Global Matches:** file_cluster_6: 10.53, file_cluster_8: 14.603, file_cluster_4: 15.92
- **Magnitude:** 292.64 | **LOC:** 222 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **20**; blast radius 4.79; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.3%)
- **Documentation Coverage:** 45.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `schedule_formatting` **(Many-Argument Workhorses)** (Impact: 79.0)
  * `reformat_many` **(Many-Argument Workhorses)** (Impact: 28.5)
    * *Intent:* # diff-shades depends on being to monkeypatch this function to operate. I know it's # not ideal, but...
  * `shutdown` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* """Cancel all pending tasks on `loop`, wait for them, and close the loop."""
  * `maybe_use_uvloop` **(Defensive Guards)** (Impact: 3.9)
    * *Intent:* """If our environment has uvloop or winloop installed we use it otherwise a normal asyncio eventloop...
  * `cancel` **(Generic / Templated Code)** (Impact: 3.1)
    * *Intent:* """asyncio signal handler that cancels all `tasks` and reports to stderr."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 23 instances
* *Concurrency (weighted view):* 92
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 47`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 24`
* *Architecture:* `io: 4`, `api: 5`, `concurrency: 22`, `import: 20`
* *Defense:* `safety: 13`, `doc: 6`, `sync_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.79
  * `Choke Point (Betweenness):` 3.4e-05 | `Ripple Effect (Closeness):` 0.024876
  * `Imports (Out-Degree: 5):` __future__, asyncio, black, black.cache, black.mode, black.output, black.report, collections.abc...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/blackd/__init__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.145)
- **Top Global Matches:** file_cluster_6: 9.145, file_cluster_4: 9.213, file_cluster_12: 14.767
- **Magnitude:** 270.86 | **LOC:** 335 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **14**; blast radius 4.997; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (95.7%), Guard Balance (formerly Safety Score) (65.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_python_variant_header` **(Defensive Guards)** (Impact: 27.0)
  * `handle` **(Many-Argument Workhorses)** (Impact: 15.0)
  * `parse_mode` **(Defensive Guards)** (Impact: 12.3)
  * `format_code` **(Many-Argument Workhorses)** (Impact: 7.0)
  * `main` **(Many-Argument Workhorses)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 30 instances
* *Concurrency (weighted view):* 64
* *State Mutation (weighted view):* 119
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 68`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 59`
* *Architecture:* `io: 3`, `api: 10`, `concurrency: 14`, `import: 14`
* *Defense:* `safety: 18`, `sync_locks: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.997
  * `Choke Point (Betweenness):` 0.000244 | `Ripple Effect (Closeness):` 0.00597
  * `Imports (Out-Degree: 5):` .middlewares, _black_version, aiohttp, asyncio, black, black.concurrency, click, concurrent.futures...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/util.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 5.967)
- **Top Global Matches:** file_cluster_5: 5.967, file_cluster_12: 8.183, file_cluster_0: 9.729
- **Magnitude:** 247.38 | **LOC:** 357 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **18**; blast radius 5.347; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (66.5%), Connectivity (formerly Api Exposure) (56.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (26.6%), Complexity Load (formerly Cognitive Load) (23.5%)
- **Documentation Coverage:** 87.0968% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assert_format` **(Many-Argument Workhorses)** (Impact: 40.1)
  * `_assert_format_equal` **(Stateful Encapsulated Methods)** (Impact: 17.3)
  * `_assert_format_inner` **(Stateful Encapsulated Methods)** (Impact: 17.0)
  * `read_data_from_file` **(Generic / Templated Code)** (Impact: 12.7)
  * `get_flags_parser` **(I/O & Config Routines)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 85`, `args: 18`, `func_start: 17`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 44`
* *Architecture:* `io: 7`, `api: 17`, `import: 19`
* *Defense:* `safety: 9`, `doc: 6`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.347
  * `Choke Point (Betweenness):` 0.000193 | `Ripple Effect (Closeness):` 0.014925
  * `Imports (Out-Degree: 9):` .conftest, argparse, black, black.const, black.debug, black.mode, black.output, black.ranges...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `scripts/diff_shades_gha_helper.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.955)
- **Top Global Matches:** file_cluster_5: 7.955, file_cluster_12: 8.816, file_cluster_7: 10.574
- **Magnitude:** 219.62 | **LOC:** 232 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 2.474; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.6%), Complexity Load (formerly Cognitive Load) (62.0%), Debt Markers (formerly Tech Debt) (20.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `http_get` **(Many-Argument Workhorses)** (Impact: 17.1)
  * `comment_body` **(Many-Argument Workhorses)** (Impact: 17.1)
  * `set_output` **(Compute Cores)** (Impact: 11.2)
  * `config` **(I/O & Config Routines)** (Impact: 7.1)
  * `comment_details` **(Generic / Templated Code)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 141
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 48`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 55`, `unreferenced_by_name: 2`
* *Architecture:* `io: 13`, `api: 9`, `import: 14`
* *Defense:* `safety: 9`, `doc: 1`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` base64, click, diff_shades, json, os, os.path, packaging.version, pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_ipynb.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.11)
- **Top Global Matches:** file_cluster_0: 6.11, file_cluster_10: 8.983, file_cluster_13: 9.02
- **Magnitude:** 195.82 | **LOC:** 566 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 2.474; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (43.9%), Complexity Load (formerly Cognitive Load) (16.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.6%), Connectivity (formerly Api Exposure) (11.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_unable_to_replace_magics` **(Callbacks & Closures)** (Impact: 3.2)
  * `test_ipynb_and_pyi_flags` **(Defensive Guards)** (Impact: 2.8)
  * `test_cache_isnt_written_if_no_jupyter_deps_single` **(Type Conversions)** (Impact: 2.7)
  * `test_cache_isnt_written_if_no_jupyter_deps_dir` **(Type Conversions)** (Impact: 2.7)
  * `test_cell_magic_with_custom_python_magic` **(Generic / Templated Code)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 113`, `args: 45`, `func_start: 40`
* *Risk/State:* `state_mutation: 74`, `unreferenced_by_name: 40`
* *Architecture:* `io: 4`, `api: 40`, `import: 13`
* *Defense:* `safety: 24`, `test: 93`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` IPython, black, black.handle_ipynb_magics, click.testing, contextlib, dataclasses, pathlib, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/black/parsing.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.562)
- **Top Global Matches:** file_cluster_4: 9.562, file_cluster_6: 10.932, file_cluster_5: 13.509
- **Magnitude:** 177.66 | **LOC:** 245 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **12**; blast radius 6.856; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (57.9%), Complexity Load (formerly Cognitive Load) (53.0%), Connectivity (formerly Api Exposure) (24.6%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_stringify_ast` **(Defensive Guards)** (Impact: 43.4)
  * `lib2to3_parse` **(Defensive Guards)** (Impact: 16.3)
  * `get_grammars` **(Generic / Templated Code)** (Impact: 11.3)
  * `parse_ast` **(Defensive Guards)** (Impact: 8.1)
    * *Intent:* # TODO: support Python 4+ ;) versions = [(3, minor) for minor in range(3, sys.version_info[1] + 1)] ...
  * `_unwrap_tuples` **(Encapsulated Accessors)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 55`, `args: 10`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 29`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 6`, `import: 12`
* *Defense:* `safety: 26`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.856
  * `Choke Point (Betweenness):` 3.4e-05 | `Ripple Effect (Closeness):` 0.030224
  * `Imports (Out-Degree: 2):` ast, black.mode, black.nodes, blib2to3, blib2to3.pgen2, blib2to3.pgen2.grammar, blib2to3.pgen2.parse, blib2to3.pgen2.tokenize...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/black/output.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.802)
- **Top Global Matches:** file_cluster_5: 6.802, file_cluster_7: 9.814, file_cluster_12: 10.024
- **Magnitude:** 129.24 | **LOC:** 123 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **7**; blast radius 17.614; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (37.7%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `color_diff` **(Compute Cores)** (Impact: 10.6)
    * *Intent:* """Inject the ANSI color codes to the diff."""
  * `diff` **(Many-Argument Workhorses)** (Impact: 9.9)
    * *Intent:* """Return a unified diff string between strings `a` and `b`."""
  * `dump_to_file` **(Generic / Templated Code)** (Impact: 9.2)
    * *Intent:* """Dump `output` to a temporary file. Return path to the file."""
  * `_splitlines_no_ff` **(Stateful Encapsulated Methods)** (Impact: 7.6)
    * *Intent:* """Split a string into lines ignoring form feed and other chars. This mimics how the Python parser s...
  * `ipynb_diff` **(Many-Argument Workhorses)** (Impact: 7.5)
    * *Intent:* """Return a unified diff string between each cell in notebooks `a` and `b`."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 26`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 22`
* *Architecture:* `api: 6`, `import: 7`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.614
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.047026
  * `Imports (Out-Degree: 0):` click, difflib, json, mypy_extensions, re, tempfile, typing
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `action/main.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.099)
- **Top Global Matches:** file_cluster_9: 8.099, file_cluster_12: 12.68, file_cluster_15: 13.73
- **Magnitude:** 123.68 | **LOC:** 202 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 2.474; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.0%), Guard Balance (formerly Safety Score) (75.6%), Complexity Load (formerly Cognitive Load) (67.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (25.3%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_version_specifier_from_pyproject` **(I/O & Config Routines)** (Impact: 11.4)
  * `find_black_version_in_array` **(Defensive Guards)** (Impact: 11.0)
  * `determine_version_specifier` **(I/O & Config Routines)** (Impact: 9.0)
    * *Intent:* """Determine the version of Black to install. The version can be specified either via the `with.vers...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Cascading Flux:* 27 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 86
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 37`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 9`, `state_mutation: 32`, `planned_debt: 1`
* *Architecture:* `io: 31`, `api: 3`, `import: 8`
* *Defense:* `safety: 6`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, pathlib, re, shlex, shutil, subprocess, sys, tomllib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/blackd/client.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.839)
- **Top Global Matches:** file_cluster_9: 6.839, file_cluster_15: 12.865, file_cluster_16: 12.961
- **Magnitude:** 115.94 | **LOC:** 93 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 2.894; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 37.5)
  * `format_code` **(Compute Cores)** (Impact: 13.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 21
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 16`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `io: 3`, `api: 3`, `concurrency: 6`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.894
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.002985
  * `Imports (Out-Degree: 2):` aiohttp, aiohttp.typedefs, black
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/black/report.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.967)
- **Top Global Matches:** file_cluster_0: 8.967, file_cluster_5: 9.023, file_cluster_12: 9.092
- **Magnitude:** 115.88 | **LOC:** 108 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **5**; blast radius 6.692; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.5%), Connectivity (formerly Api Exposure) (65.1%)
- **Documentation Coverage:** 20.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `done` **(Compute Cores)** (Impact: 22.8)
    * *Intent:* """Increment the counter for successful reformatting. Write out a message."""
  * `__str__` **(Compute Cores)** (Impact: 19.8)
    * *Intent:* """Render a color report of the current state. Use `click.unstyle` to remove colors. """
  * `return_code` **(Generic / Templated Code)** (Impact: 6.5)
    * *Intent:* """Return the exit code that the app should use. This considers the current state of changed files a...
  * `path_ignored` **(Generic / Templated Code)** (Impact: 4.2)
  * `failed` **(Generic / Templated Code)** (Impact: 2.2)
    * *Intent:* """Increment the counter for failed reformatting. Write out a message."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 22`, `args: 5`, `func_start: 5`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`
* *Architecture:* `io: 1`, `api: 8`, `import: 5`
* *Defense:* `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.692
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.031199
  * `Imports (Out-Degree: 1):` black.output, click, dataclasses, enum, pathlib
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `scripts/release.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.973)
- **Top Global Matches:** file_cluster_0: 5.973, file_cluster_11: 8.939, file_cluster_15: 9.167
- **Magnitude:** 110.66 | **LOC:** 249 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 2.474; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (67.2%), Connectivity (formerly Api Exposure) (52.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (42.3%)
- **Documentation Coverage:** 48.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_next_version` **(Type Conversions)** (Impact: 7.7)
    * *Intent:* """Workout the year and month + version number we need to move to"""
  * `get_git_tags` **(Generic / Templated Code)** (Impact: 7.6)
    * *Intent:* # TODO: Do better with alpha + beta releases # Maybe we vendor packaging library """Pull out all tag...
  * `_handle_debug` **(Encapsulated Accessors)** (Impact: 4.6)
    * *Intent:* """Turn on debugging if asked otherwise INFO default"""
  * `add_template_to_changes` **(Generic / Templated Code)** (Impact: 3.9)
    * *Intent:* """Add the template to CHANGES.md if it does not exist"""
  * `update_version_in_docs` **(Generic / Templated Code)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 53`, `args: 14`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 29`, `planned_debt: 2`
* *Architecture:* `io: 8`, `api: 14`, `import: 8`
* *Defense:* `safety: 2`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, argparse, datetime, logging, pathlib, re, subprocess, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/optional.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 12.238)
- **Top Global Matches:** file_cluster_6: 12.238, file_cluster_8: 16.125, file_cluster_4: 16.811
- **Magnitude:** 107.88 | **LOC:** 134 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 2.474; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (77.3%), Complexity Load (formerly Cognitive Load) (29.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (9.9%), Connectivity (formerly Api Exposure) (7.3%)
- **Documentation Coverage:** 72.7273% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pytest_configure` **(Defensive Guards)** (Impact: 25.3)
    * *Intent:* """Optional tests are markers. Use the syntax in https://docs.pytest.org/en/stable/mark.html#registe...
  * `pytest_collection_modifyitems` **(Generic / Templated Code)** (Impact: 9.4)
  * `no` **(Generic / Templated Code)** (Impact: 3.0)
  * `pytest_addoption` **(Generic / Templated Code)** (Impact: 1.9)
  * `skip_mark` **(Generic / Templated Code)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 28`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 24`, `unreferenced_by_name: 3`
* *Architecture:* `api: 5`, `import: 11`
* *Defense:* `safety: 2`, `doc: 2`, `test: 4`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _pytest.config, _pytest.config.argparsing, _pytest.mark.structures, _pytest.nodes, functools, itertools, logging, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `scripts/make_width_table.py` (PYTHON) | Magnitude: 41.34 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 11, state_mutation: 10, core_var_decl: 10
- `src/black/report.py` (PYTHON) | Magnitude: 115.88 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 60, core_var_decl: 29, branch: 26, design_snake_case: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/data/cases/preview_long_dict_values.py` (PYTHON) | Magnitude: 0.09 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 209, core_var_decl: 52, design_snake_case: 52, state_mutation: 40
- `tests/data/cases/multiline_strings.py` (PYTHON) | Magnitude: 0.09 | Delta: **0.118** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: doc: 118, indent_spaces: 101, core_var_decl: 38, state_mutation: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scripts/fuzz.py` (PYTHON) | Magnitude: 8.14 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 31, core_var_decl: 14, design_snake_case: 14, structural_boundaries: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `tests/data/cases/type_param_defaults.py` (PYTHON) | Magnitude: 0.03 | Delta: **0.184** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 34, indent_spaces: 17, args: 10, func_start: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tests/data/cases/comments.py` (PYTHON) | Magnitude: 0.05 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 18, state_mutation: 9, core_var_decl: 8
- `tests/data/cases/preview_hug_parens_with_braces_and_square_brackets.py` (PYTHON) | Magnitude: 0.04 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 177, branch: 22, comprehensions: 14, structural_boundaries: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `.github/workflows/zizmor.yml` (YAML) | Magnitude: 16.42 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 2, doc: 2, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/blackd/__init__.py` (PYTHON) | Magnitude: 270.86 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 232, core_var_decl: 107, design_snake_case: 92, structural_boundaries: 68

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/data/cases/collections.py` (PYTHON) | Magnitude: 0.05 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 74, core_var_decl: 35, structural_boundaries: 26, state_mutation: 23
- `tests/data/cases/context_managers_autodetect_311.py` (PYTHON) | Magnitude: 0.02 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 16, indent_spaces: 14, safety: 4, safety_bypasses: 4
- `tests/data/cases/bracketmatch.py` (PYTHON) | Magnitude: 0.02 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: closures: 8, args: 6, branch: 4, core_var_decl: 4
- `tests/data/cases/context_managers_39.py` (PYTHON) | Magnitude: 0.01 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 94, structural_boundaries: 84, safety_bypasses: 22, core_var_decl: 15

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/workflows/diff_shades.yml` -> Churn: **74.43%** | Cog Load: 9.888% | Debt: 51.932%
- `src/black/__init__.py` -> Churn: **57.39%** | Cog Load: 51.8425% | Debt: 12.5205%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/test_blackd.py` -> **Jelle Zijlstra** (100.0% isolated ownership) | Magnitude: 803.9
- `src/black/ranges.py` -> **Hugo van Kemenade** (100.0% isolated ownership) | Magnitude: 414.66
- `src/black/brackets.py` -> **Hugo van Kemenade** (100.0% isolated ownership) | Magnitude: 304.02
- `scripts/diff_shades_gha_helper.py` -> **cobalt** (100.0% isolated ownership) | Magnitude: 219.62
- `tests/test_ipynb.py` -> **Jelle Zijlstra** (100.0% isolated ownership) | Magnitude: 195.82

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/black/__init__.py` -> **Severity: 0.251** (Bridge: 0.0025 * Flux: 99.9962%)
- `src/black/linegen.py` -> **Severity: 0.072** (Bridge: 0.0007 * Flux: 100.0%)
- `src/black/nodes.py` -> **Severity: 0.059** (Bridge: 0.0006 * Flux: 99.9539%)
- `src/black/trans.py` -> **Severity: 0.044** (Bridge: 0.0004 * Flux: 100.0%)
- `src/black/strings.py` -> **Severity: 0.025** (Bridge: 0.0003 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/black/output.py` -> **Severity: 3.849** (Embedded: 0.047 * Error Risk: 81.845%)
- `src/black/mode.py` -> **Severity: 3.778** (Embedded: 0.0637 * Error Risk: 59.327%)
- `src/black/strings.py` -> **Severity: 2.967** (Embedded: 0.0349 * Error Risk: 84.932%)
- `src/black/nodes.py` -> **Severity: 2.88** (Embedded: 0.0484 * Error Risk: 59.5657%)
- `src/black/__init__.py` -> **Severity: 2.69** (Embedded: 0.042 * Error Risk: 64.0862%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/black/mode.py` -> **Severity: 2173.12** (Blast Radius: 27.164 * Doc Risk: 80.0%)
- `src/black/__init__.py` -> **Severity: 1314.228** (Blast Radius: 16.629 * Doc Risk: 79.0323%)
- `src/black/output.py` -> **Severity: 704.56** (Blast Radius: 17.614 * Doc Risk: 40.0%)
- `src/black/parsing.py` -> **Severity: 587.657** (Blast Radius: 6.856 * Doc Risk: 85.7143%)
- `src/blackd/__init__.py` -> **Severity: 499.7** (Blast Radius: 4.997 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 4328 call pairs -- scoped 29.8%, unique 0.0%, ambiguous 4.1%, external 66.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 4328 | 29.8% | 0.0% | 4.1% | 66.1% |

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
