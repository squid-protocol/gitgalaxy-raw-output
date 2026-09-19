# ARCHITECTURAL_BRIEF: pathspec
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
- **Scope:** 81 analyzed artifact(s), 8897 LOC.
- **Load-bearing artifact:** `pathspec-1.0.4/pathspec/pattern.py` -- 19 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `pathspec-1.0.4/tests/test_04_pathspec.py` -- pulls in 19 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `pathspec-1.0.4/tests/test_04_pathspec.py` at magnitude 428.96 (structural weight, not risk).
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
| Total Artifacts | 117 |
| Analyzed Artifacts (Scanned) | 81 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 36 |
| Total LOC | 8897 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 69.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3116 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2512 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.5583 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 7 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 76 | 8887 | 93.8% |
| MARKDOWN | 2 | 0 | 2.5% |
| PLAINTEXT | 2 | 0 | 2.5% |
| MAKEFILE | 1 | 10 | 1.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `0.633`
> **Composition Archetype:** `Small Flat Repo (2)` (z +0.63; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 57%, Data / Markup / Trivial 11%, Many-Argument Workhorses Files 9%, Declarative / Non-Code 5%, Encapsulated Accessors Files 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 77 | 95.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 4.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 36*

**Composition by Extension & Reason:**
- `.rst`: 10x Excluded (Unsupported Extension: '.rst'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 6x Statistical Anomaly (Z-Score: -5.92 < -4.75), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 174 LOC)
- `.json`: 2x Excluded (Static Asset Blob without Intent: 1201 LOC), 1x Excluded (Static Asset Blob without Intent: 1691 LOC), 1x Excluded (Static Asset Blob without Intent: 1711 LOC)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.ini`: 2x Excluded (Unsupported Extension: '.ini')
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 78.5 | 13.3 | 9.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.6 | 62.0 | 62.2 | 62.2 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 53.5 | 98.9 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 12.3 | 2.4 | 2.4 |
| Connectivity (formerly API Exposure) | 0.0 | 72.7 | 16.5 | 10.0 | 7.7 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 65.1 | 77.5 | 69.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 65.8 | 1.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 67.3 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 144 | 18 | 3 | `pathspec-1.0.4/tests/test_04_pathspec.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 202 | 25 | 9 | `pathspec-1.0.4/benchmarks/hyperscan_gitignore_r2.py` |
| danger | 146 | 46 | 6 | `pathspec-1.0.4/tests/util.py` |
| concurrency | 38 | 5 | 0 | `pathspec-1.0.4/pathspec/pathspec.py` |
| connectivity | 661 | 72 | 14 | `pathspec-1.0.4/tests/test_02_gitignore_basic.py` |
| io | 53 | 9 | 1 | `pathspec-1.0.4/pathspec/util.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 3 | 1 | 0 | `pathspec-1.0.4/testpypi_prepublish.py` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 20 | 5 | 0 | `pathspec-1.0.4/tests/test_02_gitignore_basic.py` |
| events | 0 | 0 | 0 | - |
| tests | 561 | 43 | 14 | `pathspec-1.0.4/tests/test_02_gitignore_basic.py` |
| docs | 444 | 75 | 12 | `pathspec-1.0.4/tests/test_02_gitignore_basic.py` |
| debt | 48 | 9 | 1 | `pathspec-1.0.4/prebuild.py` |
| mutation | 2807 | 71 | 69 | `pathspec-1.0.4/tests/test_04_pathspec.py` |
| dead_code | 441 | 43 | 12 | `pathspec-1.0.4/tests/test_02_gitignore_basic.py` |
| credential | 0 | 0 | 0 | - |
| threat | 39 | 15 | 2 | `pathspec-1.0.4/pathspec/util.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pathspec-1.0.4/pathspec/util.py` (Hits: 25)
- `pathspec-1.0.4/tests/util.py` (Hits: 10)
- `pathspec-1.0.4/benchmarks/gen_md_tables.py` (Hits: 4)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **pattern.py** (`pathspec-1.0.4/pathspec/pattern.py`) — 19 inbound connections
2. **_typing.py** (`pathspec-1.0.4/pathspec/_typing.py`) — 16 inbound connections
3. **backend.py** (`pathspec-1.0.4/pathspec/backend.py`) — 9 inbound connections
4. **util.py** (`pathspec-1.0.4/pathspec/util.py`) — 9 inbound connections
5. **pathspec.py** (`pathspec-1.0.4/pathspec/_backends/hyperscan/pathspec.py`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_04_pathspec.py** (`pathspec-1.0.4/tests/test_04_pathspec.py`) — 19 outbound dependencies
2. **util.py** (`pathspec-1.0.4/tests/util.py`) — 18 outbound dependencies
3. **test_01_util.py** (`pathspec-1.0.4/tests/test_01_util.py`) — 13 outbound dependencies
4. **test_05_gitignore.py** (`pathspec-1.0.4/tests/test_05_gitignore.py`) — 13 outbound dependencies
5. **agg.py** (`pathspec-1.0.4/pathspec/_backends/agg.py`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `pattern_to_regex` **(Many-Argument Workhorses)** (@ `pathspec-1.0.4/benchmarks/gitwildmatch_v1.py`) -> Impact: **90.8** | LOC: 188
- `__normalize_segments` **(Many-Argument Workhorses)** (@ `pathspec-1.0.4/pathspec/patterns/gitignore/basic.py`) -> Impact: **44.4** | LOC: 91
- `_init_db` **(Many-Argument Workhorses)** (@ `pathspec-1.0.4/pathspec/_backends/hyperscan/gitignore.py`) -> Impact: **40.9** | LOC: 103
- `pattern_to_regex` **(Many-Argument Workhorses)** (@ `pathspec-1.0.4/pathspec/patterns/gitignore/basic.py`) -> Impact: **38.8** | LOC: 117
- `debug_results` **(Defensive Guards)** (@ `pathspec-1.0.4/tests/util.py`) -> Impact: **36.5** | LOC: 71
  * *Intent:* """ Format the check results message. *spec* (:class:`~pathspec.PathSpec`) is the path-spec. *results* (:class:`~collections.abc.Iterable` or :class:`...
- `_init_set` **(Many-Argument Workhorses)** (@ `pathspec-1.0.4/pathspec/_backends/re2/gitignore.py`) -> Impact: **35.7** | LOC: 88
- `_translate_segment_glob` **(Compute Cores)** (@ `pathspec-1.0.4/pathspec/patterns/gitignore/base.py`) -> Impact: **33.8** | LOC: 111
  * *Intent:* """ Translates the glob pattern to a regular expression. This is used in the constructor to translate a path segment glob pattern to its corresponding...
- `__on_match` **(Stateful Encapsulated Methods)** (@ `pathspec-1.0.4/benchmarks/hyperscan_gitignore_r1.py`) -> Impact: **33.5** | LOC: 36
- `__on_match` **(Stateful Encapsulated Methods)** (@ `pathspec-1.0.4/benchmarks/hyperscan_gitignore_r1.py`) -> Impact: **33.5** | LOC: 36
- `_translate_segment_glob` **(Compute Cores)** (@ `pathspec-1.0.4/benchmarks/gitwildmatch_v1.py`) -> Impact: **33.3** | LOC: 100
  * *Intent:* # NOTE: This is derived from `fnmatch.translate()` and is similar to the # POSIX function `fnmatch()` with the `FNM_PATHNAME` flag set. escape = False...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pathspec-1.0.4/benchmarks` | 43 | 2819.8 | 10.48% | 93.81% |
| `pathspec-1.0.4/tests` | 5 | 1303.72 | 10.02% | 0.0% |
| `pathspec-1.0.4/pathspec` | 8 | 790.42 | 14.1% | 1.26% |
| `pathspec-1.0.4/pathspec/_backends/hyperscan` | 4 | 337.66 | 20.37% | 0.0% |
| `pathspec-1.0.4/pathspec/patterns/gitignore` | 3 | 336.0 | 33.99% | 0.0% |
| `pathspec-1.0.4/pathspec/_backends/re2` | 4 | 263.24 | 25.51% | 0.0% |
| `pathspec-1.0.4` | 6 | 94.32 | 8.07% | 0.0% |
| `pathspec-1.0.4/pathspec/_backends/simple` | 2 | 87.6 | 19.45% | 0.0% |
| `pathspec-1.0.4/pathspec/_backends` | 2 | 58.32 | 14.83% | 0.0% |
| `pathspec-1.0.4/pathspec/patterns` | 2 | 19.44 | 2.32% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `pathspec-1.0.4/benchmarks/conftest.py` -> **100.0%** Exposure
- `pathspec-1.0.4/benchmarks/hyperscan_pathspec_r1.py` -> **99.9289%** Exposure
- `pathspec-1.0.4/benchmarks/bench_gitignore_match_file_p100.py` -> **99.8388%** Exposure
- `pathspec-1.0.4/benchmarks/bench_gitignore_match_file_p15.py` -> **99.8388%** Exposure
- `pathspec-1.0.4/benchmarks/bench_gitignore_match_file_p150.py` -> **99.8388%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `pathspec-1.0.4/benchmarks/gen_md_tables.py` -> **100.0%** Exposure
- `pathspec-1.0.4/benchmarks/gitwildmatch_v1.py` -> **100.0%** Exposure
- `pathspec-1.0.4/benchmarks/hyperscan_gitignore_r1.py` -> **100.0%** Exposure
- `pathspec-1.0.4/benchmarks/hyperscan_gitignore_r2.py` -> **100.0%** Exposure
- `pathspec-1.0.4/benchmarks/hyperscan_pathspec_r1.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pathspec-1.0.4/tests/test_02_gitignore_basic.py` -> **55** Orphaned Functions | **0** Duplicates
- `pathspec-1.0.4/tests/test_04_pathspec.py` -> **36** Orphaned Functions | **0** Duplicates
- `pathspec-1.0.4/tests/test_01_util.py` -> **20** Orphaned Functions | **2** Duplicates
- `pathspec-1.0.4/benchmarks/conftest.py` -> **20** Orphaned Functions | **0** Duplicates
- `pathspec-1.0.4/tests/test_05_gitignore.py` -> **18** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `358` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `pathspec-1.0.4/tests/test_04_pathspec.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 428.96 | **LOC:** 1044 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 7.148; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (77.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (10.5%), Complexity Load (formerly Cognitive Load) (8.4%)
- **Documentation Coverage:** 3.7037% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parameterize_from_lines` **(Many-Argument Workhorses)** (Impact: 17.1)
  * `test_01_match_file_2_exclude` **(Compute Cores)** (Impact: 6.5)
    * *Intent:* """ Test matching a single file that is excluded. """
  * `test_01_match_file_3_unmatch` **(Compute Cores)** (Impact: 6.5)
    * *Intent:* """ Test match a single file that is unmatched. """
  * `test_05_match_tree_entries` **(I/O & Config Routines)** (Impact: 4.6)
    * *Intent:* """ Test matching a file tree. """
  * `test_05_match_tree_files` **(Type Conversions)** (Impact: 4.6)
    * *Intent:* """ Test matching a file tree. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 207
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 141`, `args: 41`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 125`, `unreferenced_by_name: 36`
* *Architecture:* `io: 2`, `api: 41`, `import: 20`
* *Defense:* `safety: 2`, `doc: 43`, `test: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` .util, collections.abc, contextlib, functools, os, pathlib, pathspec, pathspec._backends.hyperscan.pathspec...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pathspec-1.0.4/pathspec/util.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 411.68 | **LOC:** 848 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **10**; blast radius 29.954; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (66.0%)
- **Documentation Coverage:** 41.0714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_iter_tree_entries_next` **(Many-Argument Workhorses)** (Impact: 30.8)
  * `detailed_match_files` **(Many-Argument Workhorses)** (Impact: 30.2)
  * `_iter_tree_files_next` **(Many-Argument Workhorses)** (Impact: 22.6)
  * `check_match_file` **(Generic / Templated Code)** (Impact: 20.1)
  * `register_pattern` **(Many-Argument Workhorses)** (Impact: 11.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 92`, `args: 31`, `func_start: 31`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 48`, `planned_debt: 1`
* *Architecture:* `io: 25`, `api: 30`, `import: 10`
* *Defense:* `safety: 8`, `doc: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 29.954
  * `Choke Point (Betweenness):` 0.000936 | `Ripple Effect (Closeness):` 0.114266
  * `Imports (Out-Degree: 2):` ._typing, .pattern, collections.abc, dataclasses, os, os.path, pathlib, posixpath...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `pathspec-1.0.4/benchmarks/hyperscan_gitignore_r1.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 358.82 | **LOC:** 299 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 11.199; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.8%), Guard Balance (formerly Safety Score) (99.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__on_match` **(Stateful Encapsulated Methods)** (Impact: 33.5)
  * `__on_match` **(Stateful Encapsulated Methods)** (Impact: 33.5)
  * `on_match` **(Many-Argument Workhorses)** (Impact: 30.9)
  * `on_match` **(Many-Argument Workhorses)** (Impact: 30.9)
  * `match_file` **(Generic / Templated Code)** (Impact: 24.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 46`, `args: 12`, `func_start: 12`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 57`, `duplicate_logic: 6`
* *Architecture:* `api: 10`, `import: 8`
* *Defense:* `safety: 2`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.199
  * `Choke Point (Betweenness):` 0.000356 | `Ripple Effect (Closeness):` 0.022989
  * `Imports (Out-Degree: 2):` __future__, benchmarks.hyperscan_pathspec_r1, collections.abc, hyperscan, pathspec.pattern, pathspec.patterns.gitignore.spec, typing, typing_extensions
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pathspec-1.0.4/benchmarks/gitwildmatch_v1.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 325.62 | **LOC:** 343 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 19.3; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pattern_to_regex` **(Many-Argument Workhorses)** (Impact: 90.8)
  * `_translate_segment_glob` **(Compute Cores)** (Impact: 33.3)
    * *Intent:* # NOTE: This is derived from `fnmatch.translate()` and is similar to the # POSIX function `fnmatch()...
  * `escape` **(Defensive Guards)** (Impact: 15.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 60 instances
* *State Mutation (weighted view):* 180
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 25`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 60`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `safety: 6`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.3
  * `Choke Point (Betweenness):` 0.000535 | `Ripple Effect (Closeness):` 0.022989
  * `Imports (Out-Degree: 2):` pathspec._typing, pathspec.pattern, pathspec.patterns.gitignore.spec, re, typing, typing_extensions
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pathspec-1.0.4/benchmarks/hyperscan_gitignore_r2.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 305.88 | **LOC:** 299 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 11.199; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.1%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (58.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_init_db` **(Many-Argument Workhorses)** (Impact: 32.5)
  * `__on_match` **(Stateful Encapsulated Methods)** (Impact: 25.3)
  * `on_match` **(Many-Argument Workhorses)** (Impact: 23.3)
  * `on_match` **(Many-Argument Workhorses)** (Impact: 23.3)
  * `match_file` **(Generic / Templated Code)** (Impact: 19.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 50`, `args: 11`, `func_start: 11`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 50`, `duplicate_logic: 2`
* *Architecture:* `api: 10`, `import: 10`
* *Defense:* `safety: 11`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.199
  * `Choke Point (Betweenness):` 0.001426 | `Ripple Effect (Closeness):` 0.022989
  * `Imports (Out-Degree: 4):` __future__, collections.abc, hyperscan, pathspec._backends.hyperscan._base, pathspec._backends.hyperscan.gitignore, pathspec._backends.hyperscan.pathspec, pathspec.pattern, pathspec.patterns.gitignore.spec...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pathspec-1.0.4/tests/test_02_gitignore_basic.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 280.04 | **LOC:** 929 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 7.148; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (56.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (11.4%), Complexity Load (formerly Cognitive Load) (6.8%)
- **Documentation Coverage:** 0.9009% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_07_match_bytes_and_bytes_complete` **(Type Conversions)** (Impact: 3.6)
    * *Intent:* """ Test byte string patterns matching byte string paths. """
  * `test_01_relative` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """ Tests a relative path pattern. This should match: spam spam/ foo/spam spam/foo
  * `test_03_inner_double_asterisk` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """ Tests a path with an inner double-asterisk directory. This should match: left/right left/bar/rig...
  * `test_03_only_double_asterisk` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """ Tests a double-asterisk pattern which matches everything. """
  * `test_03_duplicate_leading_double_asterisk_edge_case` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """ Regression test for duplicate leading **/ bug. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 73`, `args: 56`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `state_mutation: 80`, `planned_debt: 2`, `fragile_debt: 3`, `unreferenced_by_name: 55`
* *Architecture:* `api: 56`, `import: 5`
* *Defense:* `doc: 58`, `test: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` pathspec.patterns.gitignore.base, pathspec.patterns.gitignore.basic, pathspec.util, re, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pathspec-1.0.4/tests/test_05_gitignore.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 258.92 | **LOC:** 692 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 7.148; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (76.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (8.9%), Connectivity (formerly Api Exposure) (8.9%)
- **Documentation Coverage:** 7.6923% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parameterize_from_lines` **(Many-Argument Workhorses)** (Impact: 15.3)
  * `test_02_issue_41_a` **(I/O & Config Routines)** (Impact: 4.6)
    * *Intent:* """ Test including a file and excluding a directory with the same name pattern, scenario A. """
  * `test_02_issue_41_b` **(I/O & Config Routines)** (Impact: 4.6)
    * *Intent:* """ Test including a file and excluding a directory with the same name pattern, scenario B. """
  * `test_02_issue_41_c` **(I/O & Config Routines)** (Impact: 4.6)
    * *Intent:* """ Test including a file and excluding a directory with the same name pattern, scenario C. """
  * `test_03_subdir` **(I/O & Config Routines)** (Impact: 4.5)
    * *Intent:* """ Test matching files in a subdirectory of an included directory. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 85`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 83`, `unreferenced_by_name: 18`
* *Architecture:* `api: 20`, `import: 14`
* *Defense:* `safety: 2`, `doc: 22`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` .util, collections.abc, contextlib, functools, pathspec._backends.hyperscan.gitignore, pathspec._backends.re2.gitignore, pathspec._backends.simple.gitignore, pathspec._typing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pathspec-1.0.4/pathspec/patterns/gitignore/basic.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 224.78 | **LOC:** 318 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 12.172; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (57.2%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__normalize_segments` **(Many-Argument Workhorses)** (Impact: 44.4)
  * `pattern_to_regex` **(Many-Argument Workhorses)** (Impact: 38.8)
  * `__translate_segments` **(Many-Argument Workhorses)** (Impact: 27.6)
    * *Intent:* """ Translate the pattern segments to regular expressions. *pattern_segs* (:class:`list` of :class:`...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 109
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 31`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 37`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 7`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.172
  * `Choke Point (Betweenness):` 0.000111 | `Ripple Effect (Closeness):` 0.036782
  * `Imports (Out-Degree: 1):` .base, pathspec, pathspec._typing, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pathspec-1.0.4/tests/test_01_util.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 177.6 | **LOC:** 711 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 7.148; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (11.2%), Complexity Load (formerly Cognitive Load) (3.2%)
- **Documentation Coverage:** 5.8824% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_02_many` **(I/O & Config Routines)** (Impact: 5.7)
    * *Intent:* """ Test matching files individually. """
  * `test_02_link_1_check_symlink` **(Defensive Guards)** (Impact: 3.8)
    * *Intent:* """ Tests whether links can be created. """
  * `require_symlink` **(Generic / Templated Code)** (Impact: 3.1)
    * *Intent:* """ Skips the test if `os.symlink` is not supported. """
  * `test_01_files_1_entries` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """ Tests to make sure all files are found. """
  * `test_02_link_2_links_1_entries` **(I/O & Config Routines)** (Impact: 2.9)
    * *Intent:* """ Tests to make sure links to directories and files work. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 68`, `args: 34`, `func_start: 34`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 36`, `duplicate_logic: 2`, `unreferenced_by_name: 20`
* *Architecture:* `io: 4`, `api: 38`, `import: 13`
* *Defense:* `safety: 3`, `doc: 38`, `test: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` collections.abc, errno, functools, os, os.path, pathlib, pathspec.patterns.gitignore.basic, pathspec.util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pathspec-1.0.4/pathspec/pathspec.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 174.46 | **LOC:** 461 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 8.122; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.9%), Connectivity (formerly Api Exposure) (72.7%)
- **Documentation Coverage:** 67.7419% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_lines` **(Many-Argument Workhorses)** (Impact: 16.6)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 13.3)
  * `match_files` **(Many-Argument Workhorses)** (Impact: 13.1)
  * `match_entries` **(Many-Argument Workhorses)** (Impact: 13.0)
  * `__eq__` **(Defensive Guards)** (Impact: 7.4)
    * *Intent:* """ Tests the equality of this path-spec with *other* (:class:`PathSpec`) by comparing their :attr:`...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 53`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 20`
* *Architecture:* `api: 16`, `import: 10`
* *Defense:* `safety: 5`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.015326
  * `Imports (Out-Degree: 5):` __future__, collections.abc, itertools, pathspec, pathspec._backends.agg, pathspec._typing, pathspec.backend, pathspec.pattern...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pathspec-1.0.4/benchmarks/hyperscan_pathspec_r1.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 166.68 | **LOC:** 250 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 17.984; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.9%), Guard Balance (formerly Safety Score) (96.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_init_db` **(Stateful Encapsulated Methods)** (Impact: 13.2)
  * `match_file` **(Generic / Templated Code)** (Impact: 6.3)
  * `match_file` **(Generic / Templated Code)** (Impact: 6.2)
  * `__on_match` **(Stateful Encapsulated Methods)** (Impact: 6.0)
  * `__on_match` **(Stateful Encapsulated Methods)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 52`, `args: 14`, `func_start: 14`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 34`, `duplicate_logic: 6`
* *Architecture:* `api: 12`, `import: 8`
* *Defense:* `safety: 7`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.984
  * `Choke Point (Betweenness):` 0.001203 | `Ripple Effect (Closeness):` 0.041051
  * `Imports (Out-Degree: 3):` __future__, collections.abc, hyperscan, pathspec._backends.hyperscan._base, pathspec._backends.hyperscan.pathspec, pathspec.pattern, typing, typing_extensions
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pathspec-1.0.4/pathspec/_backends/hyperscan/gitignore.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 165.76 | **LOC:** 246 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 11.204; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.4%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 71.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_init_db` **(Many-Argument Workhorses)** (Impact: 40.9)
  * `__on_match` **(Stateful Encapsulated Methods)** (Impact: 25.6)
  * `match_file` **(Stateful Encapsulated Methods)** (Impact: 6.5)
    * *Intent:* """ Check the file against the patterns. *file* (:class:`str`) is the normalized file path to check....
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 30`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 29`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `safety: 13`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.204
  * `Choke Point (Betweenness):` 6.4e-05 | `Ripple Effect (Closeness):` 0.051202
  * `Imports (Out-Degree: 2):` ._base, .pathspec, __future__, collections.abc, hyperscan, pathspec._typing, pathspec.pattern, pathspec.patterns.gitignore.spec...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pathspec-1.0.4/tests/util.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 158.2 | **LOC:** 257 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 9.174; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (97.3%), Connectivity (formerly Api Exposure) (61.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (22.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `debug_results` **(Defensive Guards)** (Impact: 36.5)
    * *Intent:* """ Format the check results message. *spec* (:class:`~pathspec.PathSpec`) is the path-spec. *result...
  * `require_backend` **(Type Conversions)** (Impact: 7.7)
    * *Intent:* """ Skip the test if the backend library is not installed. *name* (:class:`str` or :data:`None`) is ...
  * `debug_includes` **(Generic / Templated Code)** (Impact: 5.0)
    * *Intent:* """ Format the match files message. *spec* (:class:`~pathspec.PathSpec`) is the path-spec. *files* (...
  * `get_includes` **(Generic / Templated Code)** (Impact: 4.7)
    * *Intent:* """ Get the included files from the check results. *results* (:class:`~collections.abc.Iterable` or ...
  * `make_links` **(Generic / Templated Code)** (Impact: 4.2)
    * *Intent:* """ Create the specified links. *temp_dir* (:class:`pathlib.Path`) is the temporary directory to use...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 54`, `args: 13`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 23`
* *Architecture:* `io: 10`, `api: 12`, `import: 18`
* *Defense:* `safety: 7`, `doc: 13`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.174
  * `Choke Point (Betweenness):` 0.001069 | `Ripple Effect (Closeness):` 0.011494
  * `Imports (Out-Degree: 8):` __future__, collections.abc, itertools, os, os.path, pathlib, pathspec, pathspec._backends.hyperscan._base...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pathspec-1.0.4/pathspec/_backends/re2/gitignore.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 135.2 | **LOC:** 180 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 8.824; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.6%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_init_set` **(Many-Argument Workhorses)** (Impact: 35.7)
  * `match_file` **(Many-Argument Workhorses)** (Impact: 21.4)
    * *Intent:* """ Check the file against the patterns. *file* (:class:`str`) is the normalized file path to check....
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 25`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 25`
* *Architecture:* `api: 3`, `import: 8`
* *Defense:* `safety: 9`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.824
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.030651
  * `Imports (Out-Degree: 2):` ._base, .pathspec, __future__, pathspec._typing, pathspec.pattern, pathspec.patterns.gitignore.spec, re2, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pathspec-1.0.4/pathspec/_backends/hyperscan/pathspec.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 125.16 | **LOC:** 252 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **10**; blast radius 17.166; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (34.3%)
- **Documentation Coverage:** 57.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_init_db` **(Many-Argument Workhorses)** (Impact: 21.6)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 16.7)
  * `match_file` **(Stateful Encapsulated Methods)** (Impact: 6.5)
    * *Intent:* """ Check the file against the patterns. *file* (:class:`str`) is the normalized file path to check....
  * `__on_match` **(Stateful Encapsulated Methods)** (Impact: 6.4)
  * `_make_db` **(Encapsulated Accessors)** (Impact: 1.4)
    * *Intent:* """ Create the Hyperscan database. Returns the database (:class:`hyperscan.Database`). """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 33`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 23`
* *Architecture:* `api: 3`, `import: 10`
* *Defense:* `safety: 10`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.166
  * `Choke Point (Betweenness):` 0.001913 | `Ripple Effect (Closeness):` 0.09387
  * `Imports (Out-Degree: 4):` .._utils, ._base, .base, __future__, collections.abc, hyperscan, pathspec._typing, pathspec.backend...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `pathspec-1.0.4/pathspec/patterns/gitignore/base.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 96.62 | **LOC:** 177 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 9.933; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (44.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_translate_segment_glob` **(Compute Cores)** (Impact: 33.8)
    * *Intent:* """ Translates the glob pattern to a regular expression. This is used in the constructor to translat...
  * `escape` **(Defensive Guards)** (Impact: 15.4)
    * *Intent:* """ Escape special characters in the given string. *s* (:class:`str` or :class:`bytes`) a filename o...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 14`, `args: 2`, `func_start: 2`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 2`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.933
  * `Choke Point (Betweenness):` 0.000111 | `Ripple Effect (Closeness):` 0.022989
  * `Imports (Out-Degree: 2):` pathspec._typing, pathspec.pattern, re
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pathspec-1.0.4/pathspec/pattern.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 94.24 | **LOC:** 242 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **6**; blast radius 86.624; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.0%), Connectivity (formerly Api Exposure) (67.0%)
- **Documentation Coverage:** 21.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 20.7)
  * `match_file` **(Generic / Templated Code)** (Impact: 11.2)
    * *Intent:* """ Matches this pattern against the specified file. *file* (:class:`str` or :class:`bytes`) is the ...
  * `match` **(Compute Cores)** (Impact: 7.8)
    * *Intent:* """ .. version-deprecated:: 0.10.0 This method is no longer used. Use the :meth:`self.match_file <.P...
  * `__eq__` **(Defensive Guards)** (Impact: 7.4)
    * *Intent:* """ Tests the equality of this regex pattern with *other* (:class:`RegexPattern`) by comparing their...
  * `pattern_to_regex` **(Generic / Templated Code)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 31`, `args: 8`, `func_start: 8`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 13`
* *Architecture:* `api: 9`, `import: 6`
* *Defense:* `safety: 5`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 86.624
  * `Choke Point (Betweenness):` 0.000531 | `Ripple Effect (Closeness):` 0.252313
  * `Imports (Out-Degree: 1):` ._typing, __future__, collections.abc, dataclasses, re, typing
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `pathspec-1.0.4/pathspec/_backends/simple/gitignore.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 78.12 | **LOC:** 105 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **6**; blast radius 12.875; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (42.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `match_file` **(Compute Cores)** (Impact: 31.9)
    * *Intent:* """ Check the file against the patterns. *file* (:class:`str`) is the normalized file path to check....
  * `__init__` **(Generic / Templated Code)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 17`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 13`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.875
  * `Choke Point (Betweenness):` 0.000376 | `Ripple Effect (Closeness):` 0.051724
  * `Imports (Out-Degree: 2):` .pathspec, collections.abc, pathspec._typing, pathspec.pattern, pathspec.patterns.gitignore.spec, typing
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pathspec-1.0.4/pathspec/_backends/re2/pathspec.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 70.18 | **LOC:** 188 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **10**; blast radius 9.69; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (30.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_init_set` **(Many-Argument Workhorses)** (Impact: 16.3)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 11.3)
  * `match_file` **(Generic / Templated Code)** (Impact: 6.3)
    * *Intent:* """ Check the file against the patterns. *file* (:class:`str`) is the normalized file path to check....
  * `_make_set` **(Encapsulated Accessors)** (Impact: 1.4)
    * *Intent:* """ Create the re2 regex set. Returns the set (:class:`re2.Set`). """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 30`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 12`
* *Architecture:* `api: 3`, `import: 10`
* *Defense:* `safety: 5`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.69
  * `Choke Point (Betweenness):` 0.000465 | `Ripple Effect (Closeness):` 0.046935
  * `Imports (Out-Degree: 4):` .._utils, ._base, .base, __future__, collections.abc, pathspec._typing, pathspec.backend, pathspec.pattern...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pathspec-1.0.4/benchmarks/bench_gitignore_150p_to_6500f.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 67.58 | **LOC:** 233 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 7.148; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.5%), Mutation Surface (formerly State Flux) (69.4%), Guard Balance (formerly Safety Score) (54.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_match` **(Generic / Templated Code)** (Impact: 3.6)
  * `bench_hs_r1_block_closure` **(Generic / Templated Code)** (Impact: 2.5)
    * *Intent:* # Hyperscan backend.
  * `bench_hs_r1_block_state` **(Generic / Templated Code)** (Impact: 2.5)
  * `bench_hs_r1_stream_closure` **(Generic / Templated Code)** (Impact: 2.5)
  * `bench_hs_r2_block_closure` **(Generic / Templated Code)** (Impact: 2.5)
    * *Intent:* # def bench_hs_r1_stream_state( # benchmark: BenchmarkFixture, # cpython_files: set[str], # cpython_...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 28`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 14`, `dead_code: 1`, `unreferenced_by_name: 13`
* *Architecture:* `api: 14`, `import: 7`
* *Defense:* `doc: 1`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` benchmarks.hyperscan_gitignore_r1, benchmarks.hyperscan_gitignore_r2, functools, pathspec, pathspec._backends.simple.gitignore, pytest, pytest_benchmark.fixture
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pathspec-1.0.4/benchmarks/bench_gitignore_15p_to_400f.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 67.56 | **LOC:** 217 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 7.148; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.5%), Mutation Surface (formerly State Flux) (69.8%), Guard Balance (formerly Safety Score) (54.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_match` **(Generic / Templated Code)** (Impact: 3.6)
  * `bench_hs_r1_block_closure` **(Generic / Templated Code)** (Impact: 2.5)
    * *Intent:* # Hyperscan backend.
  * `bench_hs_r1_block_state` **(Generic / Templated Code)** (Impact: 2.5)
  * `bench_hs_r1_stream_closure` **(Generic / Templated Code)** (Impact: 2.5)
  * `bench_hs_r2_block_closure` **(Generic / Templated Code)** (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 28`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 14`, `unreferenced_by_name: 13`
* *Architecture:* `api: 14`, `import: 7`
* *Defense:* `doc: 1`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` benchmarks.hyperscan_gitignore_r1, benchmarks.hyperscan_gitignore_r2, functools, pathspec, pathspec._backends.simple.gitignore, pytest, pytest_benchmark.fixture
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pathspec-1.0.4/benchmarks/conftest.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 66.56 | **LOC:** 195 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 7.148; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (12.3%), Complexity Load (formerly Cognitive Load) (2.7%)
- **Documentation Coverage:** 68.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cpython_gi_lines_all` **(Generic / Templated Code)** (Impact: 5.9)
  * `cpython_gi_lines_5` **(Generic / Templated Code)** (Impact: 1.8)
  * `cpython_gi_lines_15` **(Generic / Templated Code)** (Impact: 1.7)
  * `cpython_gi_lines_25` **(Generic / Templated Code)** (Impact: 1.7)
  * `cpython_gi_lines_50` **(Generic / Templated Code)** (Impact: 1.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 55`, `args: 25`, `func_start: 25`
* *Risk/State:* `unreferenced_by_name: 20`
* *Architecture:* `io: 1`, `api: 25`, `import: 3`
* *Defense:* `doc: 8`, `test: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pathlib, pathspec.util, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pathspec-1.0.4/benchmarks/bench_gitwildmatch_15p_to_400f.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 63.68 | **LOC:** 197 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 7.148; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.6%), Mutation Surface (formerly State Flux) (77.5%), Guard Balance (formerly Safety Score) (55.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_match` **(Generic / Templated Code)** (Impact: 3.6)
  * `bench_hs_gitignore_v1` **(Generic / Templated Code)** (Impact: 2.5)
    * *Intent:* # Hyperscan backend.
  * `bench_hs_gitignore_v2` **(Generic / Templated Code)** (Impact: 2.5)
  * `bench_hs_pathspec_v1` **(Generic / Templated Code)** (Impact: 2.5)
  * `bench_hs_pathspec_v2` **(Generic / Templated Code)** (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 21`, `args: 13`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 14`, `unreferenced_by_name: 12`
* *Architecture:* `api: 13`, `import: 4`
* *Defense:* `doc: 1`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` benchmarks.gitwildmatch_v1, pathspec, pytest, pytest_benchmark.fixture
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pathspec-1.0.4/benchmarks/bench_pathspec_match_file_p100.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 61.84 | **LOC:** 191 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 7.148; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.7%), Mutation Surface (formerly State Flux) (78.3%), Guard Balance (formerly Safety Score) (53.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bench_hs_v1_end` **(Generic / Templated Code)** (Impact: 2.5)
    * *Intent:* # Hyperscan backend.
  * `bench_hs_v1_middle` **(Generic / Templated Code)** (Impact: 2.5)
  * `bench_hs_v1_none` **(Generic / Templated Code)** (Impact: 2.5)
  * `bench_hs_v1_start` **(Generic / Templated Code)** (Impact: 2.5)
  * `bench_re2_v1_end` **(Generic / Templated Code)** (Impact: 2.5)
    * *Intent:* # Re2 backend.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 18`, `args: 13`, `func_start: 13`
* *Risk/State:* `state_mutation: 14`, `unreferenced_by_name: 12`
* *Architecture:* `api: 13`, `import: 3`
* *Defense:* `doc: 1`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pathspec, pytest, pytest_benchmark.fixture
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pathspec-1.0.4/benchmarks/bench_pathspec_match_file_p15.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 61.84 | **LOC:** 191 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 7.148; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.7%), Mutation Surface (formerly State Flux) (78.3%), Guard Balance (formerly Safety Score) (53.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bench_hs_v1_end` **(Generic / Templated Code)** (Impact: 2.5)
    * *Intent:* # Hyperscan backend.
  * `bench_hs_v1_middle` **(Generic / Templated Code)** (Impact: 2.5)
  * `bench_hs_v1_none` **(Generic / Templated Code)** (Impact: 2.5)
  * `bench_hs_v1_start` **(Generic / Templated Code)** (Impact: 2.5)
  * `bench_re2_v1_end` **(Generic / Templated Code)** (Impact: 2.5)
    * *Intent:* # Re2 backend.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 18`, `args: 13`, `func_start: 13`
* *Risk/State:* `state_mutation: 14`, `unreferenced_by_name: 12`
* *Architecture:* `api: 13`, `import: 3`
* *Defense:* `doc: 1`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pathspec, pytest, pytest_benchmark.fixture
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

- `pathspec-1.0.4/pathspec/_backends/agg.py` -> **Severity: 0.321** (Bridge: 0.0032 * Flux: 99.9411%)
- `pathspec-1.0.4/pathspec/_backends/hyperscan/pathspec.py` -> **Severity: 0.191** (Bridge: 0.0019 * Flux: 100.0%)
- `pathspec-1.0.4/benchmarks/hyperscan_gitignore_r2.py` -> **Severity: 0.143** (Bridge: 0.0014 * Flux: 100.0%)
- `pathspec-1.0.4/pathspec/gitignore.py` -> **Severity: 0.128** (Bridge: 0.0013 * Flux: 96.0509%)
- `pathspec-1.0.4/benchmarks/hyperscan_pathspec_r1.py` -> **Severity: 0.12** (Bridge: 0.0012 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pathspec-1.0.4/pathspec/pattern.py` -> **Severity: 19.674** (Embedded: 0.2523 * Error Risk: 77.9763%)
- `pathspec-1.0.4/pathspec/util.py` -> **Severity: 10.344** (Embedded: 0.1143 * Error Risk: 90.5251%)
- `pathspec-1.0.4/pathspec/_backends/hyperscan/pathspec.py` -> **Severity: 8.725** (Embedded: 0.0939 * Error Risk: 92.9457%)
- `pathspec-1.0.4/pathspec/backend.py` -> **Severity: 6.988** (Embedded: 0.1186 * Error Risk: 58.904%)
- `pathspec-1.0.4/pathspec/_typing.py` -> **Severity: 6.561** (Embedded: 0.2555 * Error Risk: 25.6764%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pathspec-1.0.4/pathspec/_typing.py` -> **Severity: 12296.96** (Blast Radius: 153.712 * Doc Risk: 80.0%)
- `pathspec-1.0.4/benchmarks/gitwildmatch_v1.py` -> **Severity: 1930.0** (Blast Radius: 19.3 * Doc Risk: 100.0%)
- `pathspec-1.0.4/pathspec/pattern.py` -> **Severity: 1856.231** (Blast Radius: 86.624 * Doc Risk: 21.4286%)
- `pathspec-1.0.4/benchmarks/hyperscan_pathspec_r1.py` -> **Severity: 1798.4** (Blast Radius: 17.984 * Doc Risk: 100.0%)
- `pathspec-1.0.4/pathspec/_backends/_utils.py` -> **Severity: 1537.0** (Blast Radius: 15.37 * Doc Risk: 100.0%)

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
