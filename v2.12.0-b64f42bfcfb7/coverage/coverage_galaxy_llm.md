# ARCHITECTURAL_BRIEF: coverage
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
- **Scope:** 236 analyzed artifact(s), 28192 LOC.
- **Load-bearing artifact:** `coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js` -- 45 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `coverage-7.13.5/tests/test_api.py` -- pulls in 27 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `coverage-7.13.5/tests/test_data.py` at magnitude 679.28 (structural weight, not risk).
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
| Total Artifacts | 331 |
| Analyzed Artifacts (Scanned) | 236 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 95 |
| Total LOC | 28192 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 71.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5808 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6543 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3292 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 120 | 17453 | 50.8% |
| HTML | 67 | 8171 | 28.4% |
| PLAINTEXT | 13 | 0 | 5.5% |
| YAML | 12 | 1036 | 5.1% |
| M4 | 8 | 61 | 3.4% |
| MARKDOWN | 5 | 0 | 2.1% |
| CSS | 4 | 465 | 1.7% |
| MAKEFILE | 2 | 248 | 0.8% |
| SHELL | 2 | 50 | 0.8% |
| JAVASCRIPT | 2 | 708 | 0.8% |
| XML | 1 | 0 | 0.4% |

## 4.1 SOURCE ENCODINGS
All 236 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 63%, Generic / Templated Code Files 16%, Large Core Modules (2) 8%, Declarative / Non-Code 5%, Compute Cores Files 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 218 | 92.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 18 | 7.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 95*

**Composition by Extension & Reason:**
- `.rst`: 41x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 13x Excluded (Unsupported Extension: 'no_extension'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.pip`: 9x Excluded (Unsupported Extension: '.pip')
- `.png`: 8x Excluded (Explicitly Denied Extension: '.png')
- `.html`: 1x Excluded (Saturation: Line 88 exceeds 500 chars), 1x Packed Payload Guard (Impossible Density: 4.43 hits/line), 1x Packed Payload Guard (Impossible Density: 4.44 hits/line)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.ini`: 2x Excluded (Unsupported Extension: '.ini')
- `.xml`: 1x Excluded (Machine-Generated Source Code Signature: 23 LOC), 1x Excluded (Machine-Generated Source Code Signature: 25 LOC)
- `.tok`: 2x Excluded (Unsupported Extension: '.tok')
- `.cff`: 1x Excluded (Unsupported Extension: '.cff')
- `.pth`: 1x Excluded (Unsupported Extension: '.pth')
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 261 LOC)
- `.dtd`: 1x Excluded (Unsupported Extension: '.dtd')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 78.6 | 7.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 88.1 | 27.0 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 89.9 | 1.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.3 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 96.3 | 8.1 | 9.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 10.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 12.7 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 27.5 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 220 | 45 | 3 | `coverage-7.13.5/tests/test_api.py` |
| cleanup | 32 | 3 | 0 | `coverage-7.13.5/Makefile` |
| guards | 1787 | 76 | 23 | `coverage-7.13.5/tests/test_report.py` |
| danger | 386 | 67 | 4 | `coverage-7.13.5/tests/test_json.py` |
| concurrency | 133 | 91 | 1 | `coverage-7.13.5/tests/test_concurrency.py` |
| connectivity | 2805 | 147 | 23 | `coverage-7.13.5/tests/test_arcs.py` |
| io | 2295 | 137 | 29 | `coverage-7.13.5/tests/gold/html/omit_1/main_py.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 28 | 9 | 0 | `coverage-7.13.5/tests/test_concurrency.py` |
| time | 15 | 7 | 0 | `coverage-7.13.5/tests/test_concurrency.py` |
| serialization | 17 | 6 | 0 | `coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js` |
| regex | 65 | 25 | 1 | `coverage-7.13.5/tests/test_process.py` |
| events | 95 | 75 | 1 | `coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js` |
| tests | 1722 | 48 | 20 | `coverage-7.13.5/tests/test_data.py` |
| docs | 1565 | 154 | 14 | `coverage-7.13.5/tests/test_arcs.py` |
| debt | 297 | 64 | 4 | `coverage-7.13.5/igor.py` |
| mutation | 10666 | 168 | 93 | `coverage-7.13.5/tests/test_data.py` |
| dead_code | 1196 | 54 | 14 | `coverage-7.13.5/tests/test_arcs.py` |
| credential | 3 | 3 | 0 | `coverage-7.13.5/Makefile` |
| threat | 3 | 3 | 0 | `coverage-7.13.5/tests/test_execfile.py` |
| ml_ai | 2 | 2 | 0 | `coverage-7.13.5/Makefile` |
| ui | 371 | 73 | 6 | `coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `coverage-7.13.5/tests/gold/html/omit_1/main_py.html` (Hits: 41)
- `coverage-7.13.5/tests/gold/html/omit_2/main_py.html` (Hits: 41)
- `coverage-7.13.5/tests/gold/html/omit_3/main_py.html` (Hits: 41)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **coverage_html_cb_bcae5fc4.js** (`coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js`) — 45 inbound connections
2. **coveragetest.py** (`coverage-7.13.5/tests/coveragetest.py`) — 40 inbound connections
3. **helpers.py** (`coverage-7.13.5/tests/helpers.py`) — 27 inbound connections
4. **__init__.py** (`coverage-7.13.5/tests/__init__.py`) — 14 inbound connections
5. **goldtest.py** (`coverage-7.13.5/tests/goldtest.py`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_api.py** (`coverage-7.13.5/tests/test_api.py`) — 27 outbound dependencies
2. **test_html.py** (`coverage-7.13.5/tests/test_html.py`) — 27 outbound dependencies
3. **test_report.py** (`coverage-7.13.5/tests/test_report.py`) — 27 outbound dependencies
4. **test_process.py** (`coverage-7.13.5/tests/test_process.py`) — 25 outbound dependencies
5. **test_concurrency.py** (`coverage-7.13.5/tests/test_concurrency.py`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `one_file` **(Many-Argument Workhorses)** (@ `coverage-7.13.5/lab/parser.py`) -> Impact: **51.4** | LOC: 67
  * *Intent:* """Process just one file."""
- `_make_summary` **(Many-Argument Workhorses)** (@ `coverage-7.13.5/tests/test_json.py`) -> Impact: **48.5** | LOC: 65
- `check_coverage` **(Many-Argument Workhorses)** (@ `coverage-7.13.5/tests/coveragetest.py`) -> Impact: **40.8** | LOC: 86
- `should_skip` **(Compute Cores)** (@ `coverage-7.13.5/igor.py`) -> Impact: **34.7** | LOC: 35
  * *Intent:* """Is there a reason to skip these tests? Return empty string to run tests, or a message about why we are skipping the tests. """
- `assert_warnings` **(Many-Argument Workhorses)** (@ `coverage-7.13.5/tests/coveragetest.py`) -> Impact: **32.2** | LOC: 62
- `test_if_else` **(Compute Cores)** (@ `coverage-7.13.5/tests/test_templite.py`) -> Impact: **31.2** | LOC: 31
- `compare` **(Many-Argument Workhorses)** (@ `coverage-7.13.5/tests/goldtest.py`) -> Impact: **30.9** | LOC: 80
- `arc_ascii_art` **(Compute Cores)** (@ `coverage-7.13.5/lab/parser.py`) -> Impact: **29.6** | LOC: 38
  * *Intent:* """Draw arcs as ascii art. Returns a dictionary mapping line numbers to ascii strings to draw for that line. """
- `wire_up_filter` **(I/O & Config Routines)** (@ `coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js`) -> Impact: **29.6** | LOC: 132
  * *Intent:* // Create the events for the filter box.
- `show_code` **(Many-Argument Workhorses)** (@ `coverage-7.13.5/lab/show_pyc.py`) -> Impact: **28.8** | LOC: 55
  * *Intent:* # fmt: on

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `coverage-7.13.5/tests` | 55 | 10269.5 | 10.99% | 0.0% |
| `coverage-7.13.5/lab` | 17 | 1107.92 | 33.03% | 8.95% |
| `coverage-7.13.5` | 9 | 584.4 | 6.28% | 7.24% |
| `coverage-7.13.5/tests/gold/html/support` | 2 | 512.15 | 48.1% | 0.0% |
| `coverage-7.13.5/ci` | 5 | 253.16 | 26.96% | 0.0% |
| `coverage-7.13.5/.github/workflows` | 8 | 249.32 | 8.28% | 0.0% |
| `coverage-7.13.5/requirements` | 7 | 92.44 | 0.0% | 0.0% |
| `coverage-7.13.5/doc` | 4 | 75.3 | 6.62% | 17.72% |
| `coverage-7.13.5/tests/modules/pkg1` | 6 | 75.28 | 0.0% | 0.0% |
| `coverage-7.13.5/tests/modules/process_test` | 2 | 74.16 | 11.01% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `coverage-7.13.5/lab/hack_pyc.py` -> **89.9121%** Exposure
- `coverage-7.13.5/doc/cog_helpers.py` -> **70.8855%** Exposure
- `coverage-7.13.5/igor.py` -> **65.1355%** Exposure
- `coverage-7.13.5/lab/extract_code.py` -> **62.2459%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `coverage-7.13.5/ci/comment_on_fixes.py` -> **100.0%** Exposure
- `coverage-7.13.5/ci/update_rtfd.py` -> **100.0%** Exposure
- `coverage-7.13.5/igor.py` -> **100.0%** Exposure
- `coverage-7.13.5/lab/goals.py` -> **100.0%** Exposure
- `coverage-7.13.5/lab/hack_pyc.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `coverage-7.13.5/tests/test_arcs.py` -> **112** Orphaned Functions | **0** Duplicates
- `coverage-7.13.5/tests/test_data.py` -> **80** Orphaned Functions | **0** Duplicates
- `coverage-7.13.5/tests/test_api.py` -> **79** Orphaned Functions | **0** Duplicates
- `coverage-7.13.5/tests/test_coverage.py` -> **71** Orphaned Functions | **0** Duplicates
- `coverage-7.13.5/tests/test_process.py` -> **70** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `987` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `coverage-7.13.5/tests/test_data.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.553)
- **Top Global Matches:** file_cluster_5: 7.553, file_cluster_0: 8.372, file_cluster_12: 8.643
- **Magnitude:** 679.28 | **LOC:** 1130 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 2.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (56.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (35.0%), Concurrency Surface (formerly Concurrency) (20.2%)
- **Documentation Coverage:** 92.0455% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make_data_files` **(Type Conversions)** (Impact: 14.9)
    * *Intent:* """Make a number data files. `spec` is a string dictating the data for each file. Same characters in...
  * `test_update_conflicting_file_tracers` **(Compute Cores)** (Impact: 7.9)
  * `test_update_file_tracer_vs_no_file_tracer` **(Compute Cores)** (Impact: 7.8)
  * `test_thread_stress` **(Defensive Guards)** (Impact: 6.6)
  * `test_meta_data` **(Defensive Guards)** (Impact: 5.2)
    * *Intent:* # TODO: do we care about this? # The metadata written to the data file shouldn't interfere with # ha...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 52 instances
* *Api Near Db Sink:* 2 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 325
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 225`, `args: 89`, `func_start: 88`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 221`, `planned_debt: 1`, `fragile_debt: 6`, `unreferenced_by_name: 80`
* *Architecture:* `io: 8`, `api: 93`, `concurrency: 2`, `import: 20`
* *Defense:* `safety: 66`, `doc: 14`, `test: 117`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, collections.abc, coverage.data, coverage.exceptions, coverage.files, coverage.types, gc, glob...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_api.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.135)
- **Top Global Matches:** file_cluster_0: 8.135, file_cluster_5: 8.258, file_cluster_12: 8.766
- **Magnitude:** 630.92 | **LOC:** 1661 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 2.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.1%), Concurrency Surface (formerly Concurrency) (17.4%), Connectivity (formerly Api Exposure) (12.8%)
- **Documentation Coverage:** 83.8384% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clean_files` **(Generic / Templated Code)** (Impact: 10.5)
    * *Intent:* """Remove names matching `pats` from `files`, a list of file names."""
  * `test_pretend_to_be_nose_with_cover` **(Many-Argument Workhorses)** (Impact: 9.7)
    * *Intent:* """This is what the nose --with-cover plugin does."""
  * `test_pretend_to_be_pytestcov` **(Many-Argument Workhorses)** (Impact: 7.2)
    * *Intent:* """Act like pytest-cov."""
  * `test_combining_bad_data` **(Many-Argument Workhorses)** (Impact: 7.0)
    * *Intent:* # If you try to combine a bad data file, then you will get a warning, # and the file will remain. se...
  * `test_stdlib` **(Defensive Guards)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 28 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 217
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 339`, `args: 99`, `func_start: 99`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 161`, `unreferenced_by_name: 79`
* *Architecture:* `io: 40`, `api: 113`, `concurrency: 1`, `import: 28`
* *Defense:* `safety: 114`, `doc: 70`, `test: 108`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, b, collections.abc, colorsys, coverage, coverage.data, coverage.exceptions, coverage.files...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_html.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.942)
- **Top Global Matches:** file_cluster_0: 6.942, file_cluster_12: 8.939, file_cluster_5: 9.367
- **Magnitude:** 600.64 | **LOC:** 1573 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 2.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (12.3%), Complexity Load (formerly Cognitive Load) (11.1%)
- **Documentation Coverage:** 80.6061% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assert_valid_hrefs` **(Defensive Guards)** (Impact: 11.5)
    * *Intent:* """Assert that the hrefs in htmlcov/*.html are valid. Doesn't check external links (those with a pro...
  * `test_dynamic_contexts` **(Defensive Guards)** (Impact: 9.4)
  * `test_dynamic_contexts_relative_files` **(Defensive Guards)** (Impact: 9.3)
  * `handle_starttag` **(Defensive Guards)** (Impact: 8.7)
  * `assert_htmlcov_files_exist` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* """Assert that all the expected htmlcov files exist."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 218
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 312`, `args: 83`, `func_start: 83`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 4`, `state_mutation: 146`, `dead_code: 1`, `fragile_debt: 2`, `unreferenced_by_name: 63`
* *Architecture:* `io: 34`, `api: 91`, `import: 25`
* *Defense:* `safety: 64`, `doc: 67`, `test: 75`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, collections, coverage, coverage.exceptions, coverage.files, coverage.html, coverage.report_core, coverage.types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_process.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.689)
- **Top Global Matches:** file_cluster_0: 6.689, file_cluster_13: 9.276, file_cluster_15: 9.412
- **Magnitude:** 583.1 | **LOC:** 1772 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 2.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (40.5%), Connectivity (formerly Api Exposure) (12.1%), Complexity Load (formerly Cognitive Load) (11.7%)
- **Documentation Coverage:** 89.7436% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_pth_and_source_work_together` **(Many-Argument Workhorses)** (Impact: 19.7)
  * `test_execv_patch` **(Many-Argument Workhorses)** (Impact: 11.8)
  * `test_fork` **(Defensive Guards)** (Impact: 11.5)
  * `test_os_exit` **(Defensive Guards)** (Impact: 8.9)
  * `test_timid` **(Defensive Guards)** (Impact: 8.4)
    * *Intent:* # When meta-coverage testing, this test doesn't work, because it finds # coverage.py's own trace fun...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 36 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 223
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 307`, `args: 78`, `func_start: 78`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 151`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 70`
* *Architecture:* `io: 38`, `api: 90`, `import: 24`
* *Defense:* `safety: 149`, `doc: 85`, `test: 103`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, coverage, coverage.data, coverage.files, coverage.sqldata, csv, foo, glob...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_concurrency.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.116)
- **Top Global Matches:** file_cluster_0: 7.116, file_cluster_12: 8.972, file_cluster_5: 9.417
- **Magnitude:** 547.36 | **LOC:** 865 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 2.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (61.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (22.6%)
- **Documentation Coverage:** 81.0811% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_thread_safe_save_data` **(Compute Cores)** (Impact: 18.4)
    * *Intent:* # Non-regression test for: https://github.com/coveragepy/coveragepy/issues/581 # Create some Python ...
  * `cant_trace_msg` **(Compute Cores)** (Impact: 16.7)
    * *Intent:* """What might coverage.py say about a concurrency setting and imported module?"""
  * `test_sigterm_multiprocessing_saves_data` **(Many-Argument Workhorses)** (Impact: 14.6)
    * *Intent:* # A terminated process should save its coverage data. self.make_file( "clobbered.py", """\ import mu...
  * `try_multiprocessing_code` **(Many-Argument Workhorses)** (Impact: 14.3)
  * `try_some_code` **(Many-Argument Workhorses)** (Impact: 12.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 68 instances
* *Concurrency (weighted view):* 62
* *State Mutation (weighted view):* 243
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 141`, `args: 38`, `func_start: 37`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 107`, `unreferenced_by_name: 29`
* *Architecture:* `io: 8`, `api: 42`, `concurrency: 17`, `import: 25`
* *Defense:* `safety: 42`, `doc: 40`, `test: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` __future__, collections.abc, coverage, coverage.data, coverage.exceptions, coverage.files, coverage.misc, coverage.sqldata...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.095)
- **Top Global Matches:** file_cluster_10: 8.095, file_cluster_15: 8.829, file_cluster_12: 9.694
- **Magnitude:** 505.46 | **LOC:** 736 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **45** in-repo importer(s); blast radius 112.994; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (78.6%), Guard Balance (formerly Safety Score) (69.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Concurrency Surface (formerly Concurrency) (23.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wire_up_filter` **(I/O & Config Routines)** (Impact: 29.6)
    * *Intent:* // Create the events for the filter box.
  * `sortColumn` **(Defensive Guards)** (Impact: 19.6)
  * `select_line_or_chunk` **(Defensive Guards)** (Impact: 13.2)
    * *Intent:* // Select line number lineno, or if it is in a colored chunk, select the // entire chunk
  * `getCellValue` **(Defensive Guards)** (Impact: 11.0)
    * *Intent:* // Helpers for table sorting
  * `wire_up_sorting` **(I/O & Config Routines)** (Impact: 10.8)
    * *Intent:* // Set up the click-to-sort columns.
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 86 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 287
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 81`, `args: 55`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 115`
* *Architecture:* `io: 12`, `concurrency: 1`
* *Defense:* `safety: 30`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 112.994
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.189076
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 45):` (Excluded from Brief to save tokens)

### `coverage-7.13.5/tests/test_arcs.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.852)
- **Top Global Matches:** file_cluster_0: 6.852, file_cluster_15: 10.169, file_cluster_13: 10.28
- **Magnitude:** 446.22 | **LOC:** 2425 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 2.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (41.1%), Connectivity (formerly Api Exposure) (12.5%), Complexity Load (formerly Cognitive Load) (1.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_exception_group` **(I/O & Config Routines)** (Impact: 5.6)
    * *Intent:* # PyPy3.11 traces this incorrectly: https://github.com/pypy/pypy/issues/5354 if env.PYPY: missing = ...
  * `test_split_match_case` **(Defensive Guards)** (Impact: 5.4)
  * `test_pathologically_long_code_object` **(Defensive Guards)** (Impact: 4.7)
    * *Intent:* # https://github.com/coveragepy/coveragepy/issues/359 # Long code objects sometimes cause problems. ...
  * `test_absurd_wildcards` **(Defensive Guards)** (Impact: 4.2)
    * *Intent:* # https://github.com/coveragepy/coveragepy/issues/1421 self.check_coverage( """\ def absurd(x): matc...
  * `test_async_for` **(I/O & Config Routines)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 179`, `args: 112`, `func_start: 112`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 22`, `fragile_debt: 1`, `unreferenced_by_name: 112`
* *Architecture:* `io: 1`, `api: 127`, `import: 11`
* *Defense:* `safety: 31`, `doc: 158`, `test: 118`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` __future__, coverage, coverage.data, coverage.files, coverage.python, pytest, tests.coveragetest, tests.helpers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_report.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.002)
- **Top Global Matches:** file_cluster_0: 6.002, file_cluster_13: 9.305, file_cluster_15: 9.306
- **Magnitude:** 418.94 | **LOC:** 1298 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 2.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (35.4%), Connectivity (formerly Api Exposure) (11.7%), Complexity Load (formerly Cognitive Load) (11.1%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make_rigged_file` **(Generic / Templated Code)** (Impact: 5.1)
    * *Intent:* """Create a file that will have specific results. `stmts` and `miss` are ints, the number of stateme...
  * `get_summary_text` **(Generic / Templated Code)** (Impact: 4.4)
    * *Intent:* """Get text output from the SummaryReporter. The arguments are tuples: (name, value) for Coverage.se...
  * `test_report_include_relative_files_and_wildcard_path` **(Defensive Guards)** (Impact: 4.2)
  * `test_report_precision` **(Defensive Guards)** (Impact: 4.2)
  * `test_dotpy_not_python_ignored` **(Generic / Templated Code)** (Impact: 4.2)
    * *Intent:* # We run a Python file, and when reporting, we can't parse it as Python, # but we've said to ignore ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 170
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 277`, `args: 63`, `func_start: 63`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 134`, `fragile_debt: 3`, `unreferenced_by_name: 55`
* *Architecture:* `io: 4`, `api: 66`, `import: 22`
* *Defense:* `safety: 154`, `doc: 52`, `test: 75`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, coverage, coverage.control, coverage.data, coverage.exceptions, coverage.files, coverage.report, coverage.types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_config.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.482)
- **Top Global Matches:** file_cluster_0: 6.482, file_cluster_13: 9.413, file_cluster_12: 9.502
- **Magnitude:** 410.12 | **LOC:** 1142 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 2.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (33.5%), Concurrency Surface (formerly Concurrency) (23.5%), Connectivity (formerly Api Exposure) (11.9%)
- **Documentation Coverage:** 84.127% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assert_config_settings_are_correct` **(Defensive Guards)** (Impact: 9.3)
    * *Intent:* """Check that `cov` has all the settings from LOTSA_SETTINGS."""
  * `test_force_environment` **(Defensive Guards)** (Impact: 8.0)
  * `test_exceptions_from_missing_toml_things` **(Generic / Templated Code)** (Impact: 7.7)
  * `test_tweak_error_checking` **(Generic / Templated Code)** (Impact: 7.6)
    * *Intent:* # Trying to set an unknown config value raises an error. cov = coverage.Coverage() with pytest.raise...
  * `test_core_option` **(Defensive Guards)** (Impact: 5.6)
    * *Intent:* # Test that the core option can be set in the configuration file. self.del_environ("COVERAGE_CORE") ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 27 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 251`, `args: 63`, `func_start: 63`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 80`, `unreferenced_by_name: 56`
* *Architecture:* `io: 8`, `api: 66`, `concurrency: 2`, `import: 15`
* *Defense:* `safety: 128`, `doc: 56`, `test: 108`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, coverage, coverage.config, coverage.exceptions, coverage.tomlconfig, coverage.types, os, pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_cmdline.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.511)
- **Top Global Matches:** file_cluster_5: 7.511, file_cluster_12: 8.082, file_cluster_0: 8.385
- **Magnitude:** 407.5 | **LOC:** 1664 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 2.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.8%), Concurrency Surface (formerly Concurrency) (28.3%), Connectivity (formerly Api Exposure) (11.8%)
- **Documentation Coverage:** 94.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mock_command_line` **(Many-Argument Workhorses)** (Impact: 13.5)
  * `command_line` **(Defensive Guards)** (Impact: 11.2)
    * *Intent:* """Stub for command_line, the arg determines what it will do."""
  * `cmd_executes` **(Many-Argument Workhorses)** (Impact: 11.1)
  * `cmd_help` **(Defensive Guards)** (Impact: 8.3)
  * `test_fail_under` **(Generic / Templated Code)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 14 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 204`, `args: 73`, `func_start: 71`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 3`, `state_mutation: 72`, `planned_debt: 2`, `unreferenced_by_name: 53`
* *Architecture:* `io: 5`, `api: 79`, `concurrency: 3`, `import: 23`
* *Defense:* `safety: 70`, `doc: 119`, `test: 75`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, ast, collections.abc, coverage, coverage.cmdline, coverage.config, coverage.control, coverage.exceptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_plugins.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.857)
- **Top Global Matches:** file_cluster_0: 7.857, file_cluster_12: 8.678, file_cluster_5: 8.72
- **Magnitude:** 397.36 | **LOC:** 1334 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 2.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.5%), Connectivity (formerly Api Exposure) (11.6%), Complexity Load (formerly Cognitive Load) (9.5%)
- **Documentation Coverage:** 83.7838% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_bad_plugin` **(Many-Argument Workhorses)** (Impact: 26.3)
  * `test_plugin_sys_info` **(Defensive Guards)** (Impact: 7.5)
  * `run_all_functions` **(Defensive Guards)** (Impact: 6.6)
    * *Intent:* """Run all functions in `suite_name` under coverage."""
  * `get_plugin_options` **(Generic / Templated Code)** (Impact: 5.5)
    * *Intent:* """Just return the options for `plugin` if this is the right module."""
  * `make_render_and_caller` **(I/O & Config Routines)** (Impact: 5.2)
    * *Intent:* """Make the render.py and caller.py files we need."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 197`, `args: 55`, `func_start: 55`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 88`, `planned_debt: 4`, `fragile_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 41`
* *Architecture:* `io: 5`, `api: 64`, `import: 20`
* *Defense:* `safety: 75`, `doc: 59`, `test: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, collections.abc, coverage, coverage.data, coverage.exceptions, coverage.misc, coverage.plugin, coverage.plugin_support...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/igor.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.941)
- **Top Global Matches:** file_cluster_4: 7.941, file_cluster_15: 8.527, file_cluster_12: 8.977
- **Magnitude:** 396.74 | **LOC:** 555 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 2.879; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.2%), Debt Markers (formerly Tech Debt) (65.1%)
- **Documentation Coverage:** 0.9804% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `should_skip` **(Compute Cores)** (Impact: 34.7)
    * *Intent:* """Is there a reason to skip these tests? Return empty string to run tests, or a message about why w...
  * `run_tests_with_coverage` **(Many-Argument Workhorses)** (Impact: 13.3)
    * *Intent:* """Run tests, but with coverage."""
  * `main` **(Compute Cores)** (Impact: 11.2)
    * *Intent:* """Main command-line execution for igor. Verbs are taken from the command line, and extra words take...
  * `message` **(Generic / Templated Code)** (Impact: 10.8)
    * *Intent:* """All messages come through here, keep the data we want."""
  * `do_test_with_core` **(Compute Cores)** (Impact: 9.5)
    * *Intent:* """Run tests with a particular core."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 59 instances
* *State Mutation (weighted view):* 217
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 87`, `args: 25`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 99`, `unreferenced_by_name: 11`
* *Architecture:* `io: 37`, `api: 24`, `import: 22`
* *Defense:* `safety: 8`, `doc: 28`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` coverage, coverage.html, coverage.version, datetime, glob, inspect, itertools, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.533)
- **Top Global Matches:** file_cluster_0: 6.533, file_cluster_15: 9.633, file_cluster_12: 9.726
- **Magnitude:** 379.68 | **LOC:** 1323 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 2.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (34.6%), Complexity Load (formerly Cognitive Load) (12.1%), Connectivity (formerly Api Exposure) (11.7%)
- **Documentation Coverage:** 96.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_excluding_function` **(I/O & Config Routines)** (Impact: 7.4)
  * `test_line_endings` **(Defensive Guards)** (Impact: 4.9)
  * `test_fuzzed_double_parse` **(Generic / Templated Code)** (Impact: 4.8)
    * *Intent:* # https://bugs.chromium.org/p/oss-fuzz/issues/detail?id=50381 # The second parse used to raise `Type...
  * `test_os_error` **(Generic / Templated Code)** (Impact: 4.5)
  * `test_excluding_bug1713` **(Defensive Guards)** (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 141
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 222`, `args: 60`, `func_start: 60`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 115`, `fragile_debt: 1`, `unreferenced_by_name: 58`
* *Architecture:* `io: 1`, `api: 66`, `import: 11`
* *Defense:* `safety: 124`, `doc: 86`, `test: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` __future__, ast, coverage, coverage.exceptions, coverage.parser, pytest, re, tests.coveragetest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/coveragetest.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.464)
- **Top Global Matches:** file_cluster_0: 7.464, file_cluster_5: 7.92, file_cluster_12: 8.778
- **Magnitude:** 370.88 | **LOC:** 527 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **40** in-repo importer(s); it depends on **22**; blast radius 60.235; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (96.3%), Guard Balance (formerly Safety Score) (66.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (22.0%)
- **Documentation Coverage:** 31.0345% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_coverage` **(Many-Argument Workhorses)** (Impact: 40.8)
  * `assert_warnings` **(Many-Argument Workhorses)** (Impact: 32.2)
  * `make_data_file` **(Many-Argument Workhorses)** (Impact: 16.9)
  * `run_command_status` **(Many-Argument Workhorses)** (Impact: 11.0)
    * *Intent:* """Run the command-line `cmd` in a subprocess, and print its output. Use this when you need to test ...
  * `get_report` **(Many-Argument Workhorses)** (Impact: 10.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 109`, `args: 29`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 70`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `io: 12`, `api: 31`, `import: 24`
* *Defense:* `safety: 26`, `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 60.235
  * `Choke Point (Betweenness):` 0.000984 | `Ripple Effect (Closeness):` 0.168067
  * `Imports (Out-Degree: 2):` __future__, collections, collections.abc, contextlib, coverage, coverage.cmdline, coverage.data, coverage.misc...
  * `Imported By (In-Degree: 40):` (Excluded from Brief to save tokens)

### `coverage-7.13.5/tests/test_files.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.96)
- **Top Global Matches:** file_cluster_0: 5.96, file_cluster_12: 8.737, file_cluster_13: 8.927
- **Magnitude:** 298.86 | **LOC:** 805 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 2.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.9%), Connectivity (formerly Api Exposure) (11.9%), Complexity Load (formerly Cognitive Load) (8.7%)
- **Documentation Coverage:** 89.1304% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `globs_to_regex_params` **(Many-Argument Workhorses)** (Impact: 11.6)
  * `assert_mapped` **(Defensive Guards)** (Impact: 7.4)
    * *Intent:* """Assert that `inp` mapped through `aliases` produces `out`. If the aliases are not relative, then ...
  * `test_multiple_patterns` **(Generic / Templated Code)** (Impact: 6.8)
    * *Intent:* # also test the debugfn... msgs: list[str] = [] aliases = PathAliases(debugfn=msgs.append, relative=...
  * `test_dot` **(Defensive Guards)** (Impact: 5.8)
  * `test_globs_to_regex` **(Type Conversions)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 111`, `args: 48`, `func_start: 46`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 61`, `unreferenced_by_name: 41`
* *Architecture:* `io: 16`, `api: 52`, `import: 14`
* *Defense:* `safety: 25`, `doc: 13`, `test: 69`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` __future__, collections.abc, coverage, coverage.exceptions, coverage.files, itertools, os, os.path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_json.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 11.389)
- **Top Global Matches:** file_cluster_5: 11.389, file_cluster_7: 12.738, file_cluster_4: 13.02
- **Magnitude:** 293.98 | **LOC:** 567 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 2.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (76.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (28.2%), Connectivity (formerly Api Exposure) (3.8%)
- **Documentation Coverage:** 88.2353% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_make_summary` **(Many-Argument Workhorses)** (Impact: 48.5)
  * `_make_file_result` **(Many-Argument Workhorses)** (Impact: 16.6)
  * `test_line_and_branch_coverage` **(Many-Argument Workhorses)** (Impact: 12.7)
  * `test_regions` **(Many-Argument Workhorses)** (Impact: 10.4)
  * `_make_region` **(Many-Argument Workhorses)** (Impact: 10.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 33`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 89`, `fragile_debt: 2`, `unreferenced_by_name: 5`
* *Architecture:* `io: 2`, `api: 7`, `import: 9`
* *Defense:* `safety: 1`, `doc: 13`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, coverage, datetime, json, os, pytest, tests.coveragetest, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_coverage.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.154)
- **Top Global Matches:** file_cluster_0: 6.154, file_cluster_2: 9.296, file_cluster_15: 9.321
- **Magnitude:** 285.84 | **LOC:** 1860 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 2.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.7%), Connectivity (formerly Api Exposure) (11.7%), Complexity Load (formerly Cognitive Load) (1.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_failed_coverage` **(Compute Cores)** (Impact: 5.3)
    * *Intent:* # If the lines are wrong, the message shows right and wrong. with pytest.raises(AssertionError, matc...
  * `test_exceptions_really_fail` **(Generic / Templated Code)** (Impact: 5.1)
    * *Intent:* # An assert in the checked code will really raise up to us. with pytest.raises(AssertionError, match...
  * `test_attribute_annotation` **(Generic / Templated Code)** (Impact: 4.9)
  * `test_no_data_to_report_on_annotate` **(Generic / Templated Code)** (Impact: 3.1)
    * *Intent:* # Reporting with no data produces a nice message and no output # directory. with pytest.raises(NoDat...
  * `test_no_data_to_report_on_html` **(Generic / Templated Code)** (Impact: 3.1)
    * *Intent:* # Reporting with no data produces a nice message and no output # directory. with pytest.raises(NoDat...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 99`, `args: 71`, `func_start: 71`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `unreferenced_by_name: 71`
* *Architecture:* `api: 81`, `import: 6`
* *Defense:* `safety: 1`, `doc: 130`, `test: 79`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, coverage, coverage.exceptions, pytest, tests.coveragetest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/lab/parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.772)
- **Top Global Matches:** file_cluster_8: 7.772, file_cluster_6: 9.582, file_cluster_4: 17.949
- **Magnitude:** 283.74 | **LOC:** 221 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 2.879; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.8%), Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `one_file` **(Many-Argument Workhorses)** (Impact: 51.4)
    * *Intent:* """Process just one file."""
  * `arc_ascii_art` **(Compute Cores)** (Impact: 29.6)
    * *Intent:* """Draw arcs as ascii art. Returns a dictionary mapping line numbers to ascii strings to draw for th...
  * `main` **(Compute Cores)** (Impact: 16.9)
    * *Intent:* """A main function for trying the code from the command line."""
  * `disassemble` **(Compute Cores)** (Impact: 15.3)
    * *Intent:* """Disassemble code, for ad-hoc experimenting."""
  * `first_all_blanks` **(Type Conversions)** (Impact: 7.6)
    * *Intent:* """Find the first position that is all blank in the strings ss."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 138
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 30`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 48`
* *Architecture:* `io: 1`, `api: 9`, `import: 11`
* *Defense:* `safety: 2`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collections, coverage.parser, coverage.python, dis, glob, optparse, os, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_debug.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.19)
- **Top Global Matches:** file_cluster_5: 7.19, file_cluster_12: 8.892, file_cluster_0: 8.902
- **Magnitude:** 275.58 | **LOC:** 512 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 2.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.4%), Complexity Load (formerly Cognitive Load) (18.9%), Connectivity (formerly Api Exposure) (12.6%)
- **Documentation Coverage:** 86.3636% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_short_stack_full` **(Defensive Guards)** (Impact: 8.0)
  * `test_debug_sys_ctracer` **(Defensive Guards)** (Impact: 4.6)
  * `test_short_stack_frame_ids` **(Defensive Guards)** (Impact: 4.6)
  * `test_debug_callers` **(Defensive Guards)** (Impact: 3.6)
  * `test_short_filename` **(Defensive Guards)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 167`, `args: 48`, `func_start: 45`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 69`, `fragile_debt: 2`, `unreferenced_by_name: 34`
* *Architecture:* `io: 11`, `api: 50`, `import: 16`
* *Defense:* `safety: 74`, `doc: 18`, `test: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, ast, collections.abc, coverage, coverage.debug, coverage.exceptions, io, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_templite.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.892)
- **Top Global Matches:** file_cluster_0: 7.892, file_cluster_12: 9.856, file_cluster_5: 10.067
- **Magnitude:** 273.28 | **LOC:** 388 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 2.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.4%), Connectivity (formerly Api Exposure) (12.2%), Complexity Load (formerly Cognitive Load) (9.1%)
- **Documentation Coverage:** 88.2353% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_if_else` **(Compute Cores)** (Impact: 31.2)
  * `test_malformed_else` **(Compute Cores)** (Impact: 17.3)
  * `test_if` **(Compute Cores)** (Impact: 16.9)
  * `test_malformed_for` **(Compute Cores)** (Impact: 14.5)
  * `test_malformed_if` **(Compute Cores)** (Impact: 13.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 80`, `args: 37`, `func_start: 34`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 14`, `unreferenced_by_name: 29`
* *Architecture:* `api: 37`, `import: 7`
* *Defense:* `safety: 6`, `doc: 9`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, coverage.templite, pytest, re, tests.coveragetest, types, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_xml.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.381)
- **Top Global Matches:** file_cluster_0: 7.381, file_cluster_5: 7.942, file_cluster_12: 8.1
- **Magnitude:** 260.24 | **LOC:** 616 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 2.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.9%), Connectivity (formerly Api Exposure) (11.8%), Complexity Load (formerly Cognitive Load) (10.0%)
- **Documentation Coverage:** 76.9231% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make_tree` **(Many-Argument Workhorses)** (Impact: 12.4)
    * *Intent:* """Make a tree of packages. Makes `width` directories, named d0 .. d{width-1}. Each directory has __...
  * `test_relative_source` **(Defensive Guards)** (Impact: 9.3)
  * `package_and_class_tags` **(Generic / Templated Code)** (Impact: 9.0)
    * *Intent:* """Run an XML report on `cov`, and get the package and class tags."""
  * `unbackslash` **(Defensive Guards)** (Impact: 8.9)
    * *Intent:* """Find strings in `v`, and replace backslashes with slashes throughout."""
  * `assert_source` **(Defensive Guards)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 172`, `args: 39`, `func_start: 39`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 71`, `fragile_debt: 1`, `unreferenced_by_name: 29`
* *Architecture:* `io: 6`, `api: 44`, `import: 20`
* *Defense:* `safety: 37`, `doc: 25`, `test: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` .sample, .subpackage, .test, __future__, collections.abc, coverage, coverage.exceptions, coverage.files...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/helpers.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.895)
- **Top Global Matches:** file_cluster_5: 6.895, file_cluster_12: 10.502, file_cluster_7: 10.607
- **Magnitude:** 244.16 | **LOC:** 417 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **27** in-repo importer(s); it depends on **21**; blast radius 80.31; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (74.7%), Guard Balance (formerly Safety Score) (74.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (23.5%)
- **Documentation Coverage:** 30.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make_file` **(Many-Argument Workhorses)** (Impact: 27.7)
  * `re_lines` **(Generic / Templated Code)** (Impact: 10.6)
    * *Intent:* """Return a list of lines selected by `pat` in the string `text`. If `match` is false, the selection...
  * `re_lines_text` **(Generic / Templated Code)** (Impact: 10.2)
    * *Intent:* """Return the multi-line text of lines selected by `pat`."""
  * `arcz_to_arcs` **(Defensive Guards)** (Impact: 10.2)
    * *Intent:* """Convert a compact textual representation of arcs to a list of pairs. The text has space-separated...
  * `assert_coverage_warnings` **(Defensive Guards)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 97`, `args: 26`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 3`, `state_mutation: 42`, `dead_code: 1`
* *Architecture:* `io: 23`, `api: 23`, `import: 21`
* *Defense:* `safety: 18`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 80.31
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.133352
  * `Imports (Out-Degree: 0):` __future__, collections, collections.abc, contextlib, coverage, coverage.debug, coverage.exceptions, coverage.types...
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `coverage-7.13.5/tests/test_testing.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.322)
- **Top Global Matches:** file_cluster_0: 6.322, file_cluster_15: 9.016, file_cluster_12: 9.57
- **Magnitude:** 228.22 | **LOC:** 494 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 2.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (44.5%), Complexity Load (formerly Cognitive Load) (13.3%), Connectivity (formerly Api Exposure) (11.7%)
- **Documentation Coverage:** 95.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_same_python_executable` **(Stateful Encapsulated Methods)** (Impact: 9.9)
    * *Intent:* """Determine if `e1` and `e2` refer to the same Python executable. Either path could include symboli...
  * `test_assert_warnings` **(Compute Cores)** (Impact: 9.5)
  * `test_file_count` **(Compute Cores)** (Impact: 8.6)
  * `test_re_lines_inverted` **(Defensive Guards)** (Impact: 6.9)
  * `test_file_exists` **(Generic / Templated Code)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 147`, `args: 34`, `func_start: 34`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 36`, `planned_debt: 7`, `unreferenced_by_name: 29`
* *Architecture:* `io: 11`, `api: 40`, `import: 13`
* *Defense:* `safety: 22`, `doc: 15`, `test: 71`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` __future__, coverage, coverage.exceptions, coverage.files, coverage.types, datetime, os, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_oddball.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.37)
- **Top Global Matches:** file_cluster_12: 7.37, file_cluster_5: 7.507, file_cluster_0: 8.574
- **Magnitude:** 224.16 | **LOC:** 790 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 2.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (11.0%), Connectivity (formerly Api Exposure) (10.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_exception` **(I/O & Config Routines)** (Impact: 11.6)
    * *Intent:* # Python 2.3's trace function doesn't get called with "return" if the # scope is exiting due to an e...
  * `test_long_recursion_recovery` **(Defensive Guards)** (Impact: 9.7)
    * *Intent:* # Test the core of bug 93: https://github.com/coveragepy/coveragepy/issues/93 # When recovering from...
  * `test_setting_new_trace_function` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* # https://github.com/coveragepy/coveragepy/issues/436 if testenv.SETTRACE_CORE or not env.PYBEHAVIOR...
  * `test_for_leaks` **(I/O & Config Routines)** (Impact: 7.9)
    * *Intent:* # Our original bad memory leak only happened on line numbers > 255, so # make a code object with mor...
  * `test_eval_codeobject_leak` **(Defensive Guards)** (Impact: 6.1)
    * *Intent:* # https://github.com/coveragepy/coveragepy/issues/1924 code = """\ for i in range(10_000): r = eval(...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 92`, `args: 18`, `func_start: 18`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 43`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 5`, `unreferenced_by_name: 18`
* *Architecture:* `io: 3`, `api: 28`, `import: 15`
* *Defense:* `safety: 33`, `doc: 39`, `test: 30`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, coverage, coverage.data, coverage.files, coverage.misc, os.path, py_compile, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_context.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.245)
- **Top Global Matches:** file_cluster_5: 6.245, file_cluster_12: 9.866, file_cluster_7: 10.358
- **Magnitude:** 188.04 | **LOC:** 312 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 2.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (62.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (24.8%), Connectivity (formerly Api Exposure) (12.7%)
- **Documentation Coverage:** 91.5254% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_combining_arc_contexts` **(Defensive Guards)** (Impact: 10.6)
  * `test_combining_line_contexts` **(Defensive Guards)** (Impact: 6.9)
  * `test_dynamic_alone` **(Generic / Templated Code)** (Impact: 3.9)
  * `test_static_and_dynamic` **(Generic / Templated Code)** (Impact: 3.9)
  * `get_qualname` **(Generic / Templated Code)** (Impact: 3.5)
    * *Intent:* """Helper to return qualname_from_frame for the caller."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 88`, `args: 29`, `func_start: 29`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 40`, `duplicate_logic: 4`, `unreferenced_by_name: 16`
* *Architecture:* `io: 5`, `api: 37`, `import: 13`
* *Defense:* `safety: 16`, `doc: 8`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.879
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, coverage, coverage.context, coverage.data, coverage.types, inspect, os.path, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `coverage-7.13.5/tests/test_api.py` (PYTHON) | Magnitude: 630.92 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 977, structural_boundaries: 339, core_var_decl: 212, design_snake_case: 190

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `coverage-7.13.5/tests/test_oddball.py` (PYTHON) | Magnitude: 224.16 | Delta: **0.137** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 286, structural_boundaries: 92, core_var_decl: 65, design_snake_case: 58

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `coverage-7.13.5/lab/show_pyc.py` (PYTHON) | Magnitude: 152.56 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 155, branch: 34, core_var_decl: 34, design_snake_case: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `coverage-7.13.5/.github/workflows/dependency-review.yml` (YAML) | Magnitude: 17.56 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 23, branch: 3, args: 3, structural_boundaries: 2
- `coverage-7.13.5/.github/workflows/codeql-analysis.yml` (YAML) | Magnitude: 17.84 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 4, import: 4, immutability_locks: 4
- `coverage-7.13.5/tests/modules/usepkgs.py` (PYTHON) | Magnitude: 12.6 | Delta: **0.162** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 5, import: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `coverage-7.13.5/tests/osinfo.py` (PYTHON) | Magnitude: 34.28 | Delta: **0.154** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 22, state_mutation: 13, core_var_decl: 10

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js` -> **Severity: 13.057** (Embedded: 0.1891 * Error Risk: 69.0571%)
- `coverage-7.13.5/tests/coveragetest.py` -> **Severity: 11.178** (Embedded: 0.1681 * Error Risk: 66.5095%)
- `coverage-7.13.5/tests/helpers.py` -> **Severity: 9.948** (Embedded: 0.1334 * Error Risk: 74.6009%)
- `coverage-7.13.5/tests/mixins.py` -> **Severity: 5.894** (Embedded: 0.0904 * Error Risk: 65.2113%)
- `coverage-7.13.5/tests/goldtest.py` -> **Severity: 1.525** (Embedded: 0.021 * Error Risk: 72.5763%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js` -> **Severity: 11299.4** (Blast Radius: 112.994 * Doc Risk: 100.0%)
- `coverage-7.13.5/tests/helpers.py` -> **Severity: 2409.3** (Blast Radius: 80.31 * Doc Risk: 30.0%)
- `coverage-7.13.5/tests/coveragetest.py` -> **Severity: 1869.363** (Blast Radius: 60.235 * Doc Risk: 31.0345%)
- `coverage-7.13.5/tests/js/tests.js` -> **Severity: 532.6** (Blast Radius: 5.326 * Doc Risk: 100.0%)
- `coverage-7.13.5/tests/mixins.py` -> **Severity: 475.707** (Blast Radius: 30.921 * Doc Risk: 15.3846%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 5960 call pairs -- scoped 17.6%, unique 0.0%, ambiguous 16.1%, external 66.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 5772 | 18.0% | 0.0% | 16.6% | 65.4% |
| javascript | 183 | 7.1% | 0.0% | 0.0% | 92.9% |
| shell | 5 | 0.0% | 0.0% | 0.0% | 100.0% |

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
