# ARCHITECTURAL_BRIEF: pylint
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/pylint-dev/pylint.git` |
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
- **Scope:** 3177 analyzed artifact(s), 77591 LOC.
- **Load-bearing artifact:** `pylint/checkers/__init__.py` -- 98 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `pylint/lint/pylinter.py` -- pulls in 38 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `pylint/checkers/variables.py` at magnitude 3256.42 (structural weight, not risk).
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
| Total Artifacts | 4020 |
| Analyzed Artifacts (Scanned) | 3177 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 843 |
| Total LOC | 77591 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 79.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5119 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1074 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.2935 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 36 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 2359 | 75223 | 74.3% |
| PLAINTEXT | 727 | 0 | 22.9% |
| JSON | 64 | 915 | 2.0% |
| YAML | 18 | 1343 | 0.6% |
| MARKDOWN | 5 | 0 | 0.2% |
| HTML | 2 | 70 | 0.1% |
| BATCH | 1 | 35 | 0.0% |
| DOCKERFILE | 1 | 5 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 1 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 3175 |
| cp1252 | cp1252-fallback | 1 |
| utf-8 | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 69%, Parameter Forwarders Files 9%, Generic / Templated Code Files 6%, Declarative / Non-Code 4%, Interface Declarations Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2445 | 77.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 732 | 23.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 843*

**Composition by Extension & Reason:**
- `.rst`: 327x Excluded (Unsupported Extension: '.rst')
- `.rc`: 265x Excluded (Unsupported Extension: '.rc'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 92x Unsupported Format (.undeterminable), 11x Excluded (Unsupported Extension: '.false_positive'), 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 26x Excluded (Unsupported Extension: '.toml')
- `.mmd`: 23x Excluded (Unsupported Extension: '.mmd')
- `.dot`: 19x Excluded (Unsupported Extension: '.dot')
- `.puml`: 12x Excluded (Unsupported Extension: '.puml')
- `.py`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 311 LOC), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.ini`: 8x Excluded (Unsupported Extension: '.ini')
- `.bugfix`: 7x Excluded (Unsupported Extension: '.bugfix')
- `.png`: 6x Excluded (Explicitly Denied Extension: '.png')
- `.cfg`: 6x Excluded (Unsupported Extension: '.cfg')
- `.txt`: 4x Excluded (Binary Format Detected), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yaml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.feature`: 3x Excluded (Unsupported Extension: '.feature')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 86.1 | 5.7 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.1 | 35.5 | 50.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 5.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.1 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 89.2 | 7.5 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 13.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 73.1 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 17.1 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 41.4 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 998 | 291 | 0 | `pylint/checkers/refactoring/refactoring_checker.py` |
| cleanup | 28 | 16 | 0 | `tests/functional/c/consider/consider_using_with.py` |
| guards | 5486 | 548 | 2 | `pylint/checkers/variables.py` |
| danger | 3731 | 768 | 3 | `tests/functional/u/use/use_implicit_booleaness_not_comparison.py` |
| concurrency | 949 | 188 | 0 | `pylint/checkers/stdlib.py` |
| connectivity | 7722 | 1483 | 6 | `tests/functional/u/useless/useless_parent_delegation.py` |
| io | 1098 | 277 | 0 | `tests/functional/u/unspecified_encoding_py38.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 97 | 23 | 0 | `tests/functional/c/consider/consider_using_with.py` |
| time | 30 | 11 | 0 | `pylint/checkers/stdlib.py` |
| serialization | 2 | 2 | 0 | `pylint/checkers/base/basic_checker.py` |
| regex | 123 | 37 | 0 | `pylint/extensions/_check_docs_utils.py` |
| events | 293 | 68 | 0 | `pylint/checkers/exceptions.py` |
| tests | 1857 | 169 | 0 | `tests/test_self.py` |
| docs | 4721 | 1136 | 4 | `pylint/checkers/utils.py` |
| debt | 2342 | 710 | 2 | `tests/functional/t/too/too_many_statements.py` |
| mutation | 24717 | 1395 | 16 | `pylint/checkers/variables.py` |
| dead_code | 3268 | 864 | 2 | `tests/test_self.py` |
| credential | 1 | 1 | 0 | `pylint/checkers/base/basic_checker.py` |
| threat | 13 | 11 | 0 | `doc/data/messages/b/bidirectional-unicode/bad.py` |
| ml_ai | 23 | 16 | 0 | `tests/functional/s/shadowed_import.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/functional/u/unspecified_encoding_py38.py` (Hits: 52)
- `tests/lint/unittest_lint.py` (Hits: 44)
- `pylint/checkers/stdlib.py` (Hits: 40)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`pylint/checkers/__init__.py`) — 98 inbound connections
2. **__init__.py** (`pylint/lint/__init__.py`) — 93 inbound connections
3. **base_checker.py** (`pylint/checkers/base_checker.py`) — 75 inbound connections
4. **interfaces.py** (`pylint/interfaces.py`) — 63 inbound connections
5. **__init__.py** (`pylint/__init__.py`) — 60 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **pylinter.py** (`pylint/lint/pylinter.py`) — 38 outbound dependencies
2. **private_import.py** (`tests/functional/ext/private_import/private_import.py`) — 37 outbound dependencies
3. **imports.py** (`pylint/checkers/imports.py`) — 36 outbound dependencies
4. **test_self.py** (`tests/test_self.py`) — 33 outbound dependencies
5. **wrong_import_order.py** (`tests/functional/w/wrong_import_order.py`) — 27 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_is_variable_violation` **(Many-Argument Workhorses)** (@ `pylint/checkers/variables.py`) -> Impact: **172.7** | LOC: 154
- `_check_consumer` **(Many-Argument Workhorses)** (@ `pylint/checkers/variables.py`) -> Impact: **142.7** | LOC: 209
  * *Intent:* # pylint: disable = too-many-return-statements, too-many-branches
- `_check_is_unused` **(Many-Argument Workhorses)** (@ `pylint/checkers/variables.py`) -> Impact: **118.1** | LOC: 99
  * *Intent:* # pylint: disable = too-many-branches
- `visit_call` **(Many-Argument Workhorses)** (@ `pylint/checkers/typecheck.py`) -> Impact: **116.6** | LOC: 219
  * *Intent:* # pylint: disable = too-many-branches, too-many-locals, too-many-statements """Check that called functions/methods are inferred to callable objects, a...
- `_get_out_of_order_string` **(Many-Argument Workhorses)** (@ `pylint/checkers/imports.py`) -> Impact: **115.8** | LOC: 125
- `_emit_no_member` **(Many-Argument Workhorses)** (@ `pylint/checkers/typecheck.py`) -> Impact: **100.4** | LOC: 103
- `visit_assignname` **(Many-Argument Workhorses)** (@ `pylint/checkers/base/name_checker/checker.py`) -> Impact: **95.9** | LOC: 151
- `_make_linter_options` **(Compute Cores)** (@ `pylint/lint/base_options.py`) -> Impact: **94.0** | LOC: 380
  * *Intent:* """Return the options used in a PyLinter class."""
- `_loopvar_name` **(Many-Argument Workhorses)** (@ `pylint/checkers/variables.py`) -> Impact: **85.3** | LOC: 147
  * *Intent:* # pylint: disable-next=too-many-branches,too-many-statements # filter variables according to node's scope astmts = [s for s in node.lookup(node.name)[...
- `visit_binop` **(Many-Argument Workhorses)** (@ `pylint/checkers/strings.py`) -> Impact: **83.3** | LOC: 142

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pylint/checkers` | 33 | 13811.52 | 42.44% | 36.69% |
| `pylint/extensions` | 27 | 3259.12 | 38.62% | 54.6% |
| `pylint/checkers/refactoring` | 5 | 2541.48 | 46.82% | 7.55% |
| `pylint/pyreverse` | 13 | 2023.16 | 29.15% | 0.69% |
| `pylint/lint` | 10 | 1917.16 | 35.45% | 11.88% |
| `pylint/checkers/base` | 7 | 1789.7 | 36.67% | 6.55% |
| `tests` | 12 | 1712.68 | 14.77% | 0.0% |
| `tests/functional/u/used` | 49 | 1491.3 | 5.54% | 0.0% |
| `tests/functional/c/consider` | 35 | 1348.72 | 13.28% | 0.0% |
| `tests/checkers` | 17 | 1241.24 | 4.88% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `doc/data/messages/t/too-many-public-methods/good.py` -> **100.0%** Exposure
- `pylint/checkers/misc.py` -> **100.0%** Exposure
- `pylint/testutils/reporter_for_tests.py` -> **100.0%** Exposure
- `.github/ISSUE_TEMPLATE/BUG-REPORT.yml` -> **99.9758%** Exposure
- `pylint/checkers/async_checker.py` -> **99.958%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `doc/data/messages/t/too-complex/bad.py` -> **100.0%** Exposure
- `doc/data/messages/t/too-many-locals/bad.py` -> **100.0%** Exposure
- `doc/exts/pylint_extensions.py` -> **100.0%** Exposure
- `doc/test_messages_documentation.py` -> **100.0%** Exposure
- `pylint/__init__.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/test_self.py` -> **91** Orphaned Functions | **0** Duplicates
- `tests/lint/unittest_lint.py` -> **54** Orphaned Functions | **0** Duplicates
- `tests/functional/i/inconsistent/inconsistent_returns.py` -> **45** Orphaned Functions | **3** Duplicates
- `tests/functional/t/too/too_many_positional_arguments.py` -> **40** Orphaned Functions | **0** Duplicates
- `tests/checkers/unittest_utils.py` -> **39** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `3537` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `pylint/checkers/variables.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.651)
- **Top Global Matches:** file_cluster_6: 7.651, file_cluster_8: 12.354, file_cluster_4: 14.307
- **Magnitude:** 3256.42 | **LOC:** 3532 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 16.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.223; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.3%), Complexity Load (formerly Cognitive Load) (62.1%)
- **Documentation Coverage:** 58.4416% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_is_variable_violation` **(Many-Argument Workhorses)** (Impact: 172.7)
  * `_check_consumer` **(Many-Argument Workhorses)** (Impact: 142.7)
    * *Intent:* # pylint: disable = too-many-return-statements, too-many-branches
  * `_check_is_unused` **(Many-Argument Workhorses)** (Impact: 118.1)
    * *Intent:* # pylint: disable = too-many-branches
  * `_loopvar_name` **(Many-Argument Workhorses)** (Impact: 85.3)
    * *Intent:* # pylint: disable-next=too-many-branches,too-many-statements # filter variables according to node's ...
  * `_check_imports` **(Many-Argument Workhorses)** (Impact: 66.8)
    * *Intent:* # pylint: disable = too-many-branches
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 317 instances
* *State Mutation (weighted view):* 1016
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 933`, `structural_boundaries: 555`, `args: 113`, `func_start: 108`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 382`, `dead_code: 6`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 32`
* *Architecture:* `io: 3`, `api: 39`, `import: 23`
* *Defense:* `safety: 210`, `doc: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.223
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` X, __future__, astroid, astroid.exceptions, astroid.modutils, astroid.nodes, astroid.typing, collections...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pylint/checkers/refactoring/refactoring_checker.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.007)
- **Top Global Matches:** file_cluster_4: 9.007, file_cluster_6: 10.522, file_cluster_5: 13.44
- **Magnitude:** 1877.28 | **LOC:** 2455 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **17**; blast radius 0.261; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.8%), Complexity Load (formerly Cognitive Load) (61.0%)
- **Documentation Coverage:** 73.9496% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_check_unnecessary_comprehension` **(Many-Argument Workhorses)** (Impact: 67.9)
  * `_check_unnecessary_dict_index_lookup` **(Many-Argument Workhorses)** (Impact: 67.8)
  * `_check_unnecessary_list_index_lookup` **(Many-Argument Workhorses)** (Impact: 62.2)
  * `_check_simplifiable_if` **(Many-Argument Workhorses)** (Impact: 41.7)
    * *Intent:* """Check if the given if node can be simplified. The if statement can be reduced to a boolean expres...
  * `_check_chained_comparison` **(Stateful Encapsulated Methods)** (Impact: 40.9)
    * *Intent:* """Check if there is any chained comparison in the expression. Add a refactoring message if a boolOp...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 187 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 36
* *State Mutation (weighted view):* 579
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 625`, `structural_boundaries: 450`, `args: 95`, `func_start: 93`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 42`, `high_risk_execution: 4`, `state_mutation: 205`, `dead_code: 1`
* *Architecture:* `io: 13`, `api: 28`, `concurrency: 6`, `import: 18`
* *Defense:* `safety: 118`, `doc: 39`, `sync_locks: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000315
  * `Imports (Out-Degree: 7):` __future__, astroid, astroid.util, collections, collections.abc, copy, functools, itertools...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pylint/checkers/utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.39)
- **Top Global Matches:** file_cluster_4: 9.39, file_cluster_0: 9.604, file_cluster_5: 9.672
- **Magnitude:** 1740.56 | **LOC:** 2352 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **39** in-repo importer(s); it depends on **19**; blast radius 4.531; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (89.2%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.0%)
- **Documentation Coverage:** 51.3834% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `defnode_in_scope` **(Defensive Guards)** (Impact: 54.3)
    * *Intent:* # pylint: disable = too-many-branches
  * `safe_infer` **(Defensive Guards)** (Impact: 41.2)
  * `parse_format_string` **(Compute Cores)** (Impact: 32.0)
  * `is_defined_before` **(Defensive Guards)** (Impact: 29.7)
    * *Intent:* """Check if the given variable node is defined before. Verify that the variable node is defined by a...
  * `unimplemented_abstract_methods` **(Defensive Guards)** (Impact: 25.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 150 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 482
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 520`, `structural_boundaries: 529`, `args: 129`, `func_start: 129`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 1`, `state_mutation: 182`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `io: 2`, `api: 113`, `import: 22`
* *Defense:* `safety: 187`, `doc: 87`, `test: 2`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.531
  * `Choke Point (Betweenness):` 3.9e-05 | `Ripple Effect (Closeness):` 0.025514
  * `Imports (Out-Degree: 2):` __future__, _string, astroid, astroid.context, astroid.exceptions, astroid.helpers, astroid.nodes._base_nodes, astroid.typing...
  * `Imported By (In-Degree: 39):` (Excluded from Brief to save tokens)

### `pylint/checkers/typecheck.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.591)
- **Top Global Matches:** file_cluster_6: 7.591, file_cluster_4: 10.736, file_cluster_8: 16.666
- **Magnitude:** 1724.94 | **LOC:** 2356 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **23**; blast radius 0.464; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.2%), Guard Balance (formerly Safety Score) (59.0%)
- **Documentation Coverage:** 83.6207% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visit_call` **(Many-Argument Workhorses)** (Impact: 116.6)
    * *Intent:* # pylint: disable = too-many-branches, too-many-locals, too-many-statements """Check that called fun...
  * `_emit_no_member` **(Many-Argument Workhorses)** (Impact: 100.4)
  * `visit_attribute` **(Many-Argument Workhorses)** (Impact: 60.3)
    * *Intent:* # pylint: disable = too-many-branches, too-many-statements
  * `_check_invalid_slice_index` **(Defensive Guards)** (Impact: 43.1)
    * *Intent:* # Check the type of each part of the slice invalid_slices_nodes: list[nodes.NodeNG] = [] for index i...
  * `visit_with` **(Many-Argument Workhorses)** (Impact: 40.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 178 instances
* *Concurrency (weighted view):* 39
* *State Mutation (weighted view):* 557
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 513`, `structural_boundaries: 404`, `args: 71`, `func_start: 70`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 201`, `planned_debt: 8`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 32`, `concurrency: 19`, `import: 25`
* *Defense:* `safety: 150`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.464
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.017168
  * `Imports (Out-Degree: 6):` __future__, astroid, astroid.context, astroid.exceptions, astroid.helpers, astroid.interpreter, astroid.modutils, astroid.nodes...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pylint/checkers/imports.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.348)
- **Top Global Matches:** file_cluster_5: 9.348, file_cluster_4: 9.393, file_cluster_12: 9.877
- **Magnitude:** 1026.9 | **LOC:** 1315 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **36**; blast radius 0.258; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.4%), Complexity Load (formerly Cognitive Load) (55.5%)
- **Documentation Coverage:** 58.9286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_out_of_order_string` **(Many-Argument Workhorses)** (Impact: 115.8)
  * `_get_first_import` **(Many-Argument Workhorses)** (Impact: 74.1)
  * `_add_imported_module` **(Stateful Encapsulated Methods)** (Impact: 23.9)
    * *Intent:* """Notify an imported module, used to analyze dependencies."""
  * `_check_reimport` **(Stateful Encapsulated Methods)** (Impact: 23.8)
  * `isort_leave_module` **(Defensive Guards)** (Impact: 20.5)
    * *Intent:* # Check imports are grouped by category (standard, 3rd party, local) std_imports, ext_imports, loc_i...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 131 instances
* *State Mutation (weighted view):* 420
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 265`, `structural_boundaries: 254`, `args: 44`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 158`, `planned_debt: 1`
* *Architecture:* `io: 6`, `api: 14`, `import: 26`
* *Defense:* `safety: 34`, `doc: 26`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.258
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.00063
  * `Imports (Out-Degree: 12):` __future__, a, alias, astroid, astroid.modutils, astroid.nodes._base_nodes, between, beyond...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pylint/checkers/strings.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.828)
- **Top Global Matches:** file_cluster_4: 6.828, file_cluster_6: 10.21, file_cluster_12: 12.617
- **Magnitude:** 836.16 | **LOC:** 1102 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.223; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.0%), Complexity Load (formerly Cognitive Load) (62.0%)
- **Documentation Coverage:** 83.0189% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visit_binop` **(Many-Argument Workhorses)** (Impact: 83.3)
  * `_check_new_format` **(Many-Argument Workhorses)** (Impact: 66.2)
    * *Intent:* """Check the new string formatting."""
  * `_check_new_format_specifiers` **(Many-Argument Workhorses)** (Impact: 54.2)
    * *Intent:* # pylint: disable = too-many-statements
  * `process_non_raw_string_token` **(Many-Argument Workhorses)** (Impact: 34.9)
  * `check_for_consistent_string_delimiters` **(Compute Cores)** (Impact: 28.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 97 instances
* *State Mutation (weighted view):* 307
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 154`, `args: 32`, `func_start: 32`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 113`, `fragile_debt: 2`, `unreferenced_by_name: 11`
* *Architecture:* `io: 1`, `api: 21`, `import: 16`
* *Defense:* `safety: 58`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.223
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` __future__, astroid, astroid.typing, collections, collections.abc, pylint.checkers, pylint.checkers.utils, pylint.interfaces...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pylint/lint/pylinter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.667)
- **Top Global Matches:** file_cluster_5: 7.667, file_cluster_12: 8.13, file_cluster_0: 9.265
- **Magnitude:** 817.34 | **LOC:** 1382 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **52** in-repo importer(s); it depends on **38**; blast radius 5.787; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (60.9%)
- **Documentation Coverage:** 49.3976% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_add_one_message` **(Many-Argument Workhorses)** (Impact: 74.1)
  * `_discover_files` **(Stateful Encapsulated Methods)** (Impact: 24.3)
    * *Intent:* """Discover python modules and packages in sub-directory. Returns iterator of paths to discovered mo...
  * `check` **(Many-Argument Workhorses)** (Impact: 20.0)
    * *Intent:* """Main checking entry: check a list of files or modules from their name. files_or_modules is either...
  * `set_current_module` **(Compute Cores)** (Impact: 18.9)
    * *Intent:* """Set the name of the currently analyzed module and init statistics for it. """
  * `enable_fail_on_messages` **(Compute Cores)** (Impact: 17.1)
    * *Intent:* """Enable 'fail on' msgs. Convert values in config.fail_on (which might be msg category, msg id, or ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 90 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 318
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 189`, `args: 48`, `func_start: 47`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 1`, `state_mutation: 138`, `planned_debt: 1`
* *Architecture:* `io: 17`, `api: 32`, `import: 40`
* *Defense:* `safety: 34`, `doc: 44`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.787
  * `Choke Point (Betweenness):` 0.000577 | `Ripple Effect (Closeness):` 0.032275
  * `Imports (Out-Degree: 26):` __future__, argparse, astroid, astroid.builder, astroid.modutils, collections, collections.abc, contextlib...
  * `Imported By (In-Degree: 52):` (Excluded from Brief to save tokens)

### `pylint/extensions/_check_docs_utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.028)
- **Top Global Matches:** file_cluster_4: 9.028, file_cluster_0: 10.058, file_cluster_5: 10.812
- **Magnitude:** 748.24 | **LOC:** 942 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.254; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (75.8%), Connectivity (formerly Api Exposure) (54.0%), Complexity Load (formerly Cognitive Load) (40.7%)
- **Documentation Coverage:** 75.7895% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `possible_exc_types` **(Defensive Guards)** (Impact: 36.7)
    * *Intent:* """Gets all the possible raised exception types for the given raise node. .. note:: Caught exception...
  * `match_param_docs` **(Compute Cores)** (Impact: 31.7)
    * *Intent:* """Matches parameter documentation section to parameter documentation rules."""
  * `args_with_annotation` **(Compute Cores)** (Impact: 31.1)
  * `_parse_section` **(Stateful Encapsulated Methods)** (Impact: 19.2)
  * `match_param_docs` **(Generic / Templated Code)** (Impact: 16.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 97 instances
* *State Mutation (weighted view):* 337
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 156`, `args: 51`, `func_start: 51`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 143`
* *Architecture:* `api: 47`, `import: 8`
* *Defense:* `safety: 9`, `doc: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.254
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000315
  * `Imports (Out-Degree: 1):` __future__, astroid, astroid.util, collections.abc, itertools, pylint.checkers, re
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/test_self.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.801)
- **Top Global Matches:** file_cluster_0: 6.801, file_cluster_13: 9.305, file_cluster_12: 9.335
- **Magnitude:** 748.02 | **LOC:** 1728 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **33**; blast radius 0.239; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.3%), Complexity Load (formerly Cognitive Load) (18.9%), Connectivity (formerly Api Exposure) (11.3%)
- **Documentation Coverage:** 71.9388% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_runtest` **(Stateful Encapsulated Methods)** (Impact: 15.7)
  * `test_fail_under` **(I/O & Config Routines)** (Impact: 10.6)
  * `test_relative_imports` **(Many-Argument Workhorses)** (Impact: 8.3)
  * `test_fail_on` **(Many-Argument Workhorses)** (Impact: 8.0)
  * `test_help_msg` **(Generic / Templated Code)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Cascading Flux:* 39 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 333
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 346`, `args: 102`, `func_start: 102`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 8`, `state_mutation: 255`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 91`
* *Architecture:* `io: 35`, `api: 97`, `import: 34`
* *Defense:* `safety: 94`, `doc: 49`, `test: 126`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.239
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000315
  * `Imports (Out-Degree: 13):` __future__, collections.abc, configparser, contextlib, copy, io, json, os...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pylint/checkers/base/basic_checker.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.352)
- **Top Global Matches:** file_cluster_4: 8.352, file_cluster_6: 9.587, file_cluster_12: 14.125
- **Magnitude:** 727.16 | **LOC:** 963 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **12**; blast radius 0.57; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.0%), Complexity Load (formerly Cognitive Load) (51.0%)
- **Documentation Coverage:** 39.6825% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visit_expr` **(Defensive Guards)** (Impact: 44.9)
    * *Intent:* """Check for various kind of statements without effect."""
  * `_check_reversed` **(Defensive Guards)** (Impact: 37.5)
    * *Intent:* """Check that the argument to `reversed` is a sequence."""
  * `_check_using_constant_test` **(Many-Argument Workhorses)** (Impact: 33.9)
  * `visit_lambda` **(Many-Argument Workhorses)** (Impact: 32.2)
    * *Intent:* """Check whether the lambda is suspicious."""
  * `_check_self_assigning_variable` **(Stateful Encapsulated Methods)** (Impact: 29.8)
    * *Intent:* # Detect assigning to the same variable. scope = node.scope() scope_locals = scope.locals rhs_names ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 9 instances
* *Amplified Cascading Flux:* 79 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 255
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 164`, `args: 37`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 12`, `state_mutation: 97`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 25`, `import: 13`
* *Defense:* `safety: 90`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.57
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.00254
  * `Imports (Out-Degree: 9):` __future__, astroid, collections, collections.abc, itertools, pylint, pylint.checkers, pylint.interfaces...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `pylint/checkers/base/name_checker/checker.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.741)
- **Top Global Matches:** file_cluster_4: 7.741, file_cluster_6: 11.538, file_cluster_12: 11.913
- **Magnitude:** 663.2 | **LOC:** 810 | **CtrlFlow:** 28.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **18**; blast radius 0.348; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.9%), Complexity Load (formerly Cognitive Load) (64.6%)
- **Documentation Coverage:** 82.3529% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visit_assignname` **(Many-Argument Workhorses)** (Impact: 95.9)
  * `_check_typevar` **(Many-Argument Workhorses)** (Impact: 66.5)
    * *Intent:* """Check for TypeVar lint violations."""
  * `_check_name` **(Stateful Encapsulated Methods)** (Impact: 41.9)
  * `_determine_function_name_type` **(Stateful Encapsulated Methods)** (Impact: 24.3)
  * `_is_multi_naming_match` **(Stateful Encapsulated Methods)** (Impact: 18.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 77 instances
* *State Mutation (weighted view):* 239
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 192`, `structural_boundaries: 115`, `args: 26`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 85`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 9`, `import: 20`
* *Defense:* `safety: 32`, `doc: 10`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.348
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.00063
  * `Imports (Out-Degree: 9):` __future__, argparse, astroid, astroid.typing, collections, collections.abc, enum, itertools...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pylint/checkers/stdlib.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.558)
- **Top Global Matches:** file_cluster_4: 7.558, file_cluster_12: 11.715, file_cluster_16: 11.811
- **Magnitude:** 600.34 | **LOC:** 1005 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 0.349; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Concurrency Surface (formerly Concurrency) (80.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.0%)
- **Documentation Coverage:** 89.4737% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_check_open_call` **(Many-Argument Workhorses)** (Impact: 57.4)
  * `_check_env_function` **(Stateful Encapsulated Methods)** (Impact: 29.9)
  * `visit_call` **(Defensive Guards)** (Impact: 29.3)
    * *Intent:* """Visit a Call node."""
  * `_check_invalid_envvar_value` **(Stateful Encapsulated Methods)** (Impact: 27.7)
  * `_check_lru_cache_decorators` **(Defensive Guards)** (Impact: 22.8)
    * *Intent:* """Check if instance methods are decorated with functools.lru_cache."""
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 71 instances
* *Concurrency (weighted view):* 45
* *State Mutation (weighted view):* 221
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 98`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 5`, `state_mutation: 79`
* *Architecture:* `io: 40`, `api: 14`, `concurrency: 40`, `import: 12`
* *Defense:* `safety: 35`, `doc: 5`, `test: 23`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.349
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.00063
  * `Imports (Out-Degree: 7):` __future__, astroid, astroid.typing, collections.abc, pylint, pylint.checkers, pylint.interfaces, pylint.lint...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pylint/checkers/symilar.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.353)
- **Top Global Matches:** file_cluster_5: 7.353, file_cluster_0: 8.142, file_cluster_12: 8.563
- **Magnitude:** 582.04 | **LOC:** 933 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **19**; blast radius 1.749; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.6%), Connectivity (formerly Api Exposure) (46.8%)
- **Documentation Coverage:** 70.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `stripped_lines` **(Many-Argument Workhorses)** (Impact: 70.7)
  * `filter_noncode_lines` **(Many-Argument Workhorses)** (Impact: 21.2)
  * `append_stream` **(Many-Argument Workhorses)** (Impact: 15.0)
  * `_get_similarity_report` **(Stateful Encapsulated Methods)** (Impact: 15.0)
  * `_find_common` **(Many-Argument Workhorses)** (Impact: 13.7)
    * *Intent:* # pylint: disable = too-many-locals
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 66 instances
* *State Mutation (weighted view):* 246
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 140`, `args: 49`, `func_start: 48`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 1`, `state_mutation: 114`, `planned_debt: 2`
* *Architecture:* `io: 3`, `api: 34`, `import: 21`
* *Defense:* `safety: 14`, `doc: 33`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.749
  * `Choke Point (Betweenness):` 4.4e-05 | `Ripple Effect (Closeness):` 0.025248
  * `Imports (Out-Degree: 9):` __future__, argparse, astroid, collections, collections.abc, copy, functools, io...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `pylint/checkers/format.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.743)
- **Top Global Matches:** file_cluster_4: 7.743, file_cluster_5: 10.944, file_cluster_12: 11.165
- **Magnitude:** 581.14 | **LOC:** 747 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.244; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.5%), Complexity Load (formerly Cognitive Load) (56.3%)
- **Documentation Coverage:** 54.7619% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_check_keyword_parentheses` **(Many-Argument Workhorses)** (Impact: 79.2)
    * *Intent:* # pylint: disable-next = too-many-return-statements, too-many-branches
  * `process_tokens` **(Many-Argument Workhorses)** (Impact: 39.0)
    * *Intent:* """Process tokens and search for: - too long lines (i.e. longer than <max_chars>) - optionally bad c...
  * `check_lines` **(Many-Argument Workhorses)** (Impact: 27.4)
  * `visit_default` **(Defensive Guards)** (Impact: 22.6)
    * *Intent:* """Check the node line number and check it if not yet done."""
  * `_check_line_ending` **(Stateful Encapsulated Methods)** (Impact: 21.1)
    * *Intent:* # check if line endings are mixed if self._last_line_ending is not None: # line_ending == "" indicat...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 72 instances
* *State Mutation (weighted view):* 232
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 121`, `args: 26`, `func_start: 25`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 88`
* *Architecture:* `api: 19`, `import: 13`
* *Defense:* `safety: 11`, `doc: 15`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000315
  * `Imports (Out-Degree: 8):` __future__, astroid, functools, pylint.checkers, pylint.checkers.utils, pylint.constants, pylint.interfaces, pylint.lint...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/lint/unittest_lint.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.965)
- **Top Global Matches:** file_cluster_0: 6.965, file_cluster_13: 9.002, file_cluster_15: 9.406
- **Magnitude:** 513.04 | **LOC:** 1280 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **27**; blast radius 0.223; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (40.1%), Complexity Load (formerly Cognitive Load) (19.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.1%), Connectivity (formerly Api Exposure) (11.5%)
- **Documentation Coverage:** 75.8065% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_more_args` **(Defensive Guards)** (Impact: 9.5)
  * `test_load_plugin_path_manipulation_case_6` **(I/O & Config Routines)** (Impact: 8.4)
    * *Intent:* """Case 6 refers to GitHub issue #7264. This is where we supply a plugin we want to load on both the...
  * `test_load_plugin_path_manipulation_case_3` **(I/O & Config Routines)** (Impact: 8.3)
    * *Intent:* """Case 3 refers to GitHub issue #7264. This is where we supply a plugin we want to load on the CLI ...
  * `test_one_arg` **(Defensive Guards)** (Impact: 7.6)
  * `test_two_similar_args` **(Defensive Guards)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 234
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 358`, `args: 62`, `func_start: 62`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 144`, `fragile_debt: 1`, `unreferenced_by_name: 54`
* *Architecture:* `io: 44`, `api: 64`, `import: 30`
* *Defense:* `safety: 177`, `doc: 19`, `test: 86`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.223
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` __future__, argparse, astroid, collections.abc, contextlib, io, os, os.path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pylint/pyreverse/inspector.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.409)
- **Top Global Matches:** file_cluster_0: 7.409, file_cluster_5: 8.715, file_cluster_12: 8.986
- **Magnitude:** 494.44 | **LOC:** 536 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **13**; blast radius 5.15; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (73.1%), Guard Balance (formerly Safety Score) (72.6%)
- **Documentation Coverage:** 52.7273% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `project_from_files` **(Many-Argument Workhorses)** (Impact: 31.1)
  * `handle` **(Many-Argument Workhorses)** (Impact: 22.7)
  * `handle` **(Many-Argument Workhorses)** (Impact: 22.7)
  * `visit_classdef` **(Defensive Guards)** (Impact: 18.5)
    * *Intent:* """Visit an nodes.Class node and optionally assign a unique id."""
  * `visit_assignname` **(Defensive Guards)** (Impact: 13.3)
    * *Intent:* """Visit an AssignName node and update locals_type for its frame."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 65 instances
* *State Mutation (weighted view):* 232
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 86`, `args: 30`, `func_start: 30`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 102`
* *Architecture:* `io: 5`, `api: 33`, `import: 14`
* *Defense:* `safety: 30`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.15
  * `Choke Point (Betweenness):` 0.000116 | `Ripple Effect (Closeness):` 0.026134
  * `Imports (Out-Degree: 5):` __future__, abc, astroid, astroid.exceptions, astroid.modutils, astroid.typing, collections.abc, os...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `pylint/checkers/base/basic_error_checker.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.408)
- **Top Global Matches:** file_cluster_4: 7.408, file_cluster_0: 10.076, file_cluster_16: 10.416
- **Magnitude:** 490.82 | **LOC:** 648 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 0.276; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.7%), Complexity Load (formerly Cognitive Load) (52.1%)
- **Documentation Coverage:** 63.2653% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_check_redefinition` **(Many-Argument Workhorses)** (Impact: 49.5)
  * `visit_functiondef` **(Compute Cores)** (Impact: 29.4)
  * `_check_in_loop` **(Stateful Encapsulated Methods)** (Impact: 23.2)
  * `_check_name_used_prior_global` **(Stateful Encapsulated Methods)** (Impact: 18.6)
  * `_check_inferred_class_is_abstract` **(Stateful Encapsulated Methods)** (Impact: 17.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 170
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 160`, `args: 31`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 62`
* *Architecture:* `api: 17`, `import: 9`
* *Defense:* `safety: 38`, `doc: 15`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.276
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000708
  * `Imports (Out-Degree: 5):` __future__, astroid, astroid.typing, itertools, pylint.checkers, pylint.checkers.base.basic_checker, pylint.checkers.utils, pylint.interfaces
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/functional/ext/consider_refactoring_into_while_condition/consider_refactoring_into_while_condition.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.908)
- **Top Global Matches:** file_cluster_12: 6.908, file_cluster_15: 8.57, file_cluster_4: 9.188
- **Magnitude:** 456.42 | **LOC:** 336 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (77.2%), Complexity Load (formerly Cognitive Load) (40.0%), Connectivity (formerly Api Exposure) (12.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_error_message_17` **(Compute Cores)** (Impact: 27.8)
  * `test_multi_break_condition_4` **(Compute Cores)** (Impact: 12.2)
  * `test_multi_break_condition_3` **(Compute Cores)** (Impact: 10.6)
  * `test_multi_break_condition_1` **(Compute Cores)** (Impact: 9.2)
  * `test_error_message_16` **(Callbacks & Closures)** (Impact: 7.6)
    * *Intent:* # Silly example but needed for coverage k = None while True: # [consider-refactoring-into-while-cond...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 189
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 92`, `args: 40`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 63`, `unreferenced_by_name: 38`
* *Architecture:* `api: 39`
* *Defense:* `doc: 1`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.223
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pylint/checkers/exceptions.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.45)
- **Top Global Matches:** file_cluster_4: 9.45, file_cluster_6: 10.963, file_cluster_5: 13.309
- **Magnitude:** 439.56 | **LOC:** 659 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **13**; blast radius 0.387; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.3%), Connectivity (formerly Api Exposure) (41.1%)
- **Documentation Coverage:** 84.6154% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_check_catching_non_exception` **(Many-Argument Workhorses)** (Impact: 47.7)
  * `visit_try` **(Defensive Guards)** (Impact: 36.7)
    * *Intent:* """Check for empty except."""
  * `_check_try_except_raise` **(Stateful Encapsulated Methods)** (Impact: 34.0)
  * `_check_raise_missing_from` **(Stateful Encapsulated Methods)** (Impact: 19.6)
  * `_check_misplaced_bare_raise` **(Stateful Encapsulated Methods)** (Impact: 14.9)
    * *Intent:* # Filter out if it's present in __exit__. scope = node.scope() if ( isinstance(scope, nodes.Function...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 135`, `args: 28`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 47`
* *Architecture:* `io: 2`, `api: 23`, `import: 14`
* *Defense:* `safety: 56`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.387
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.000945
  * `Imports (Out-Degree: 6):` __future__, astroid, astroid.context, astroid.typing, builtins, collections.abc, inspect, pylint...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pylint/extensions/docparams.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.364)
- **Top Global Matches:** file_cluster_6: 7.364, file_cluster_4: 8.598, file_cluster_9: 15.172
- **Magnitude:** 415.9 | **LOC:** 698 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.223; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.0%), Complexity Load (formerly Cognitive Load) (47.0%)
- **Documentation Coverage:** 88.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_arguments_in_docstring` **(Many-Argument Workhorses)** (Impact: 51.0)
  * `visit_raise` **(Compute Cores)** (Impact: 42.7)
  * `visit_return` **(Compute Cores)** (Impact: 25.6)
  * `visit_yield` **(Compute Cores)** (Impact: 22.4)
  * `check_functiondef_returns` **(Compute Cores)** (Impact: 16.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 145
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 108`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 53`, `unreferenced_by_name: 3`
* *Architecture:* `api: 11`, `import: 10`
* *Defense:* `safety: 5`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.223
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` __future__, astroid, pylint.checkers, pylint.extensions, pylint.extensions._check_docs_utils, pylint.interfaces, pylint.lint, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pylint/extensions/typing.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 8.206)
- **Top Global Matches:** file_cluster_16: 8.206, file_cluster_9: 8.634, file_cluster_0: 8.816
- **Magnitude:** 347.9 | **LOC:** 559 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.223; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.2%), Complexity Load (formerly Cognitive Load) (37.2%)
- **Documentation Coverage:** 72.4138% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_broken_callable_location` **(Stateful Encapsulated Methods)** (Impact: 26.2)
    * *Intent:* """Check if node would be a broken location for collections.abc.Callable."""
  * `_check_broken_noreturn` **(Stateful Encapsulated Methods)** (Impact: 20.5)
    * *Intent:* """Check for 'NoReturn' inside compound types."""
  * `leave_module` **(Stateful Encapsulated Methods)** (Impact: 19.4)
    * *Intent:* """After parsing of module is complete, add messages for 'consider-using-alias' check. Make sure res...
  * `_check_for_typing_alias` **(Stateful Encapsulated Methods)** (Impact: 18.1)
  * `visit_subscript` **(Defensive Guards)** (Impact: 16.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 85`, `args: 20`, `func_start: 20`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 43`
* *Architecture:* `io: 1`, `api: 12`, `import: 8`
* *Defense:* `safety: 22`, `doc: 11`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.223
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` __future__, astroid, pylint.checkers, pylint.checkers.utils, pylint.constants, pylint.interfaces, pylint.lint, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pylint/pyreverse/diagrams.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.475)
- **Top Global Matches:** file_cluster_5: 7.475, file_cluster_12: 9.169, file_cluster_0: 10.552
- **Magnitude:** 337.7 | **LOC:** 377 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **7**; blast radius 5.55; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (73.4%), Guard Balance (formerly Safety Score) (68.7%)
- **Documentation Coverage:** 30.2326% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `extract_relationships` **(Compute Cores)** (Impact: 25.4)
    * *Intent:* """Extract relationships between nodes in the diagram."""
  * `get_attrs` **(Many-Argument Workhorses)** (Impact: 24.5)
    * *Intent:* """Return visible attributes, possibly with class name."""
  * `class_names` **(Defensive Guards)** (Impact: 20.2)
    * *Intent:* """Return class names if needed in diagram."""
  * `get_methods` **(Defensive Guards)** (Impact: 10.9)
    * *Intent:* """Return visible methods."""
  * `get_module` **(Compute Cores)** (Impact: 10.8)
    * *Intent:* """Return a module by its name, looking also for relative imports; raise KeyError if not found. """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 77`, `args: 26`, `func_start: 24`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 58`, `planned_debt: 1`
* *Architecture:* `api: 26`, `import: 8`
* *Defense:* `safety: 23`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.55
  * `Choke Point (Betweenness):` 6.9e-05 | `Ripple Effect (Closeness):` 0.020005
  * `Imports (Out-Degree: 3):` __future__, astroid, collections.abc, pylint.checkers.utils, pylint.pyreverse.inspector, pylint.pyreverse.utils, typing
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `tests/functional/u/useless/useless_parent_delegation.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.362)
- **Top Global Matches:** file_cluster_5: 8.362, file_cluster_7: 9.271, file_cluster_12: 9.803
- **Magnitude:** 334.12 | **LOC:** 433 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.223; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (70.2%), Connectivity (formerly Api Exposure) (15.6%), Complexity Load (formerly Cognitive Load) (4.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__eq__` **(Parameter Forwarders)** (Impact: 3.6)
  * `passing_only_a_handful` **(Parameter Forwarders)** (Impact: 2.5)
  * `not_the_same_order` **(Parameter Forwarders)** (Impact: 2.3)
  * `with_default_argument_bis` **(Parameter Forwarders)** (Impact: 2.3)
    * *Intent:* # Although the default_arg is the same as in the base class, the call signature # differs. Thus it i...
  * `with_default_arg_quad` **(Parameter Forwarders)** (Impact: 2.3)
    * *Intent:* # Not useless because the default value is the same as in the base but the # call is different from ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 198`, `args: 105`, `func_start: 105`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 13`, `duplicate_logic: 4`, `unreferenced_by_name: 34`
* *Architecture:* `api: 114`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.223
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` random, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pylint/checkers/refactoring/recommendation_checker.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.48)
- **Top Global Matches:** file_cluster_6: 9.48, file_cluster_8: 10.545, file_cluster_4: 16.796
- **Magnitude:** 331.02 | **LOC:** 443 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.261; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (53.3%), Guard Balance (formerly Safety Score) (50.4%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_check_consider_using_enumerate` **(Defensive Guards)** (Impact: 52.1)
    * *Intent:* """Emit a convention whenever range and len are used for indexing."""
  * `_detect_replacable_format_call` **(Defensive Guards)** (Impact: 50.4)
    * *Intent:* """Check whether a string is used in a call to format() or '%' and whether it can be replaced by an ...
  * `_check_use_maxsplit_arg` **(Defensive Guards)** (Impact: 38.2)
    * *Intent:* """Add message when accessing first or last elements of a str.split() or str.rsplit(). """
  * `_check_consider_using_dict_items` **(Defensive Guards)** (Impact: 26.7)
    * *Intent:* """Add message when accessing dict values by index lookup."""
  * `_check_consider_iterating_dictionary` **(Stateful Encapsulated Methods)** (Impact: 25.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 78`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 29`, `dead_code: 2`
* *Architecture:* `io: 1`, `api: 6`, `import: 6`
* *Defense:* `safety: 41`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.261
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000315
  * `Imports (Out-Degree: 4):` __future__, astroid, pylint, pylint.checkers, pylint.interfaces
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pylint/checkers/spelling.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.82)
- **Top Global Matches:** file_cluster_4: 8.82, file_cluster_5: 8.971, file_cluster_12: 9.681
- **Magnitude:** 316.56 | **LOC:** 474 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.247; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.3%), Complexity Load (formerly Cognitive Load) (63.0%)
- **Documentation Coverage:** 96.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_check_spelling` **(Many-Argument Workhorses)** (Impact: 55.4)
    * *Intent:* # pylint: disable = too-many-statements
  * `process_tokens` **(Generic / Templated Code)** (Impact: 14.8)
  * `open` **(Compute Cores)** (Impact: 13.5)
  * `_get_enchant_dict_help` **(Stateful Encapsulated Methods)** (Impact: 12.8)
  * `next` **(Encapsulated Accessors)** (Impact: 12.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 89`, `args: 20`, `func_start: 20`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 51`
* *Architecture:* `io: 2`, `api: 22`, `import: 11`
* *Defense:* `safety: 5`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.247
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000315
  * `Imports (Out-Degree: 4):` __future__, astroid, enchant, enchant.tokenize, pylint.checkers, pylint.checkers.utils, pylint.lint, re...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `doc/data/messages/t/too-many-statements/bad.py` (PYTHON) | Magnitude: 23.5 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 17, branch: 4, state_mutation: 4, core_var_decl: 4
- `examples/custom.py` (PYTHON) | Magnitude: 29.52 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 14, branch: 6, state_mutation: 5
- `pylint/extensions/magic_value.py` (PYTHON) | Magnitude: 84.34 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 73, structural_boundaries: 30, branch: 20, state_mutation: 17
- `tests/test_check_parallel.py` (PYTHON) | Magnitude: 277.64 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 541, structural_boundaries: 199, core_var_decl: 117, design_snake_case: 117
- `tests/checkers/unittest_variables.py` (PYTHON) | Magnitude: 65.68 | Delta: **0.131** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 109, structural_boundaries: 45, core_var_decl: 39, design_snake_case: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `tests/functional/a/abstract/abstract_abc_methods.py` (PYTHON) | Magnitude: 6.66 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 4, doc: 4, api: 3
- `tests/functional/i/invalid/invalid_getnewargs/invalid_getnewargs_ex_returned.py` (PYTHON) | Magnitude: 39.34 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 40, indent_spaces: 31, args: 14, class_start: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `doc/data/messages/a/assert-on-string-literal/good.py` (PYTHON) | Magnitude: 3.16 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 2, indent_spaces: 2, args: 1, func_start: 1
- `tests/functional/o/overridden_final_method_regression.py` (PYTHON) | Magnitude: 2.14 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 2, structural_boundaries: 1, args: 1, func_start: 1
- `tests/functional/i/invalid/invalid_field_call.py` (PYTHON) | Magnitude: 17.16 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 15, core_var_decl: 14, design_snake_case: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `pylint/config/deprecation_actions.py` (PYTHON) | Magnitude: 22.38 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 22, core_var_decl: 21, design_pascal_case: 14
- `tests/functional/i/invalid/invalid_slice_index.py` (PYTHON) | Magnitude: 39.96 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 33, api: 17, doc: 17
- `tests/regrtest_data/func_block_disable_msg.py` (PYTHON) | Magnitude: 91.98 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 85, debug_prints: 28, structural_boundaries: 25, branch: 17
- `tests/functional/ext/docparams/raise/missing_raises_doc.py` (PYTHON) | Magnitude: 36.9 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 28, indent_spaces: 27, api: 15, args: 14
- `tests/functional/ext/redefined_variable_type/redefined_variable_type.py` (PYTHON) | Magnitude: 163.52 | Delta: **0.138** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 68, state_mutation: 39, core_var_decl: 31, design_snake_case: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/functional/r/regression_02/regression_4982.py` (PYTHON) | Magnitude: 9.26 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 5, doc: 4, api: 3
- `tests/functional/r/regression/regression_implicit_none_with_no_return.py` (PYTHON) | Magnitude: 6.18 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 3, args: 2, func_start: 2
- `doc/data/messages/s/self-cls-assignment/bad.py` (PYTHON) | Magnitude: 9.56 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 3, api: 3, state_mutation: 3
- `doc/data/messages/s/self-cls-assignment/good.py` (PYTHON) | Magnitude: 8.66 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 3, api: 3, args: 2
- `tests/functional/s/singledispatch/singledispatch_functions.py` (PYTHON) | Magnitude: 32.84 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 31, indent_spaces: 20, args: 12, func_start: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `doc/data/messages/e/exec-used/good.py` (PYTHON) | Magnitude: 5.62 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 3, core_var_decl: 3, design_snake_case: 3, structural_boundaries: 2
- `doc/data/messages/d/deprecated-decorator/bad.py` (PYTHON) | Magnitude: 3.6 | Delta: **0.146** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, api: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `doc/data/messages/b/bad-exception-cause/good.py` (PYTHON) | Magnitude: 5.24 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 4, safety: 2, state_mutation: 2
- `doc/data/messages/u/unused-private-member/good.py` (PYTHON) | Magnitude: 8.24 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 3, args: 2, func_start: 2
- `tests/functional/ext/docparams/raise/missing_raises_doc_required.py` (PYTHON) | Magnitude: 4.28 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 2, args: 2, func_start: 2
- `tests/functional/t/too/too_many_instance_attributes_py37.py` (PYTHON) | Magnitude: 3.06 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, args: 1, func_start: 1
- `doc/data/messages/o/overlapping-except/good/only_generic.py` (PYTHON) | Magnitude: 4.94 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 2, safety: 2, debug_prints: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/functional/r/regression_02/regression_2964.py` (PYTHON) | Magnitude: 9.62 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 4, doc: 3, args: 2
- `tests/functional/a/access/access_member_before_definition.py` (PYTHON) | Magnitude: 27.96 | Delta: **0.137** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 13, state_mutation: 9, api: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `pylint/testutils/__init__.py` (PYTHON) | Magnitude: 17.56 | Delta: **0.186** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 24, indent_spaces: 14, import: 12, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/checkers/unittest_non_ascii_name.py` (PYTHON) | Magnitude: 48.78 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 203, structural_boundaries: 66, core_var_decl: 65, design_snake_case: 64
- `tests/functional/t/trailing_whitespaces.py` (PYTHON) | Magnitude: 2.88 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: doc: 6, debug_prints: 5, indent_spaces: 3, structural_boundaries: 1
- `doc/data/messages/t/too-many-locals/bad.py` (PYTHON) | Magnitude: 35.94 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 20, state_mutation: 11, core_var_decl: 11, design_snake_case: 11
- `pylint/lint/__init__.py` (PYTHON) | Magnitude: 17.58 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 17, indent_spaces: 16, import: 9, branch: 1
- `tests/functional/w/wrong_import_order.py` (PYTHON) | Magnitude: 18.84 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 52, import: 35, indent_spaces: 9, safety: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `pylint/utils/file_state.py` (PYTHON) | Magnitude: 174.18 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 158, branch: 36, structural_boundaries: 31, state_mutation: 25
- `pylint/checkers/spelling.py` (PYTHON) | Magnitude: 316.56 | Delta: **0.151** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 311, structural_boundaries: 89, branch: 68, state_mutation: 51

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `pylint/checkers/imports.py` (PYTHON) | Magnitude: 1026.9 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 1028, branch: 265, structural_boundaries: 254, core_var_decl: 161
- `pylint/reporters/multi_reporter.py` (PYTHON) | Magnitude: 72.18 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 36, generics: 15, api: 14
- `pylint/testutils/configuration_test.py` (PYTHON) | Magnitude: 112.88 | Delta: **0.124** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 29, core_var_decl: 29, state_mutation: 26
- `pylint/utils/ast_walker.py` (PYTHON) | Magnitude: 90.5 | Delta: **0.137** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 24, state_mutation: 19, branch: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/functional/n/no/no_name_in_module.py` (PYTHON) | Magnitude: 18.16 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 42, import: 23, indent_spaces: 19, safety: 17
- `tests/functional/t/too/too_few_public_methods.py` (PYTHON) | Magnitude: 24.04 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 18, indent_spaces: 16, args: 8, func_start: 8
- `tests/functional/k/keyword_arg_before_vararg.py` (PYTHON) | Magnitude: 15.42 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 12, api: 5, core_var_decl: 5
- `tests/functional/u/used/used_before_assignment.py` (PYTHON) | Magnitude: 214.36 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 137, branch: 60, structural_boundaries: 54, state_mutation: 53
- `tests/functional/b/broad_exception/broad_exception_raised.py` (PYTHON) | Magnitude: 15.42 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 17, panics_and_aborts: 10, api: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `pylint/pyreverse/writer.py` (PYTHON) | Magnitude: 160.0 | Delta: **0.13** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 152, structural_boundaries: 37, core_var_decl: 37, design_snake_case: 37

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `pylint/testutils/_primer/primer_compare_command.py` -> Churn: **60.85%** | Cog Load: 60.2112% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/test_self.py` -> **Julian Grimm** (100.0% isolated ownership) | Magnitude: 748.02
- `pylint/checkers/base/basic_checker.py` -> **Pierre Sassoulas** (100.0% isolated ownership) | Magnitude: 727.16
- `pylint/checkers/stdlib.py` -> **Mehraz Hossain Rumman** (100.0% isolated ownership) | Magnitude: 600.34
- `tests/lint/unittest_lint.py` -> **Pierre Sassoulas** (100.0% isolated ownership) | Magnitude: 513.04
- `pylint/pyreverse/inspector.py` -> **Julian Grimm** (100.0% isolated ownership) | Magnitude: 494.44

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pylint/lint/pylinter.py` -> **Severity: 0.058** (Bridge: 0.0006 * Flux: 99.9968%)
- `pylint/lint/run.py` -> **Severity: 0.032** (Bridge: 0.0003 * Flux: 100.0%)
- `pylint/__init__.py` -> **Severity: 0.027** (Bridge: 0.0003 * Flux: 100.0%)
- `pylint/typing.py` -> **Severity: 0.016** (Bridge: 0.0003 * Flux: 59.6451%)
- `pylint/checkers/__init__.py` -> **Severity: 0.015** (Bridge: 0.0001 * Flux: 99.9998%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pylint/typing.py` -> **Severity: 2.684** (Embedded: 0.0351 * Error Risk: 76.5116%)
- `pylint/lint/run.py` -> **Severity: 2.317** (Embedded: 0.0302 * Error Risk: 76.8177%)
- `pylint/checkers/base_checker.py` -> **Severity: 2.293** (Embedded: 0.0336 * Error Risk: 68.2143%)
- `pylint/utils/utils.py` -> **Severity: 2.199** (Embedded: 0.0314 * Error Risk: 69.9473%)
- `pylint/__init__.py` -> **Severity: 2.161** (Embedded: 0.0329 * Error Risk: 65.7332%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pylint/typing.py` -> **Severity: 1477.1** (Blast Radius: 14.771 * Doc Risk: 100.0%)
- `pylint/reporters/ureports/nodes.py` -> **Severity: 975.801** (Blast Radius: 15.334 * Doc Risk: 63.6364%)
- `pylint/checkers/__init__.py` -> **Severity: 391.8** (Blast Radius: 7.836 * Doc Risk: 50.0%)
- `pylint/config/callback_actions.py` -> **Severity: 353.7** (Blast Radius: 3.537 * Doc Risk: 100.0%)
- `pylint/lint/pylinter.py` -> **Severity: 285.864** (Blast Radius: 5.787 * Doc Risk: 49.3976%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1729 literal sites + 45 sites through wrappers = 1774
- **`panics_and_aborts`:** 773 literal sites + 31 sites through wrappers = 804

- `_toml_has_config` (function, debug_prints, primitive): 3 call sites in 2 files -- `pylint/config/find_default_config_files.py`
- `exploding_apple` (function, debug_prints, primitive): 3 call sites in 1 files -- `tests/functional/b/broad_exception/broad_exception_raised.py`
- `exploding_apple` (function, debug_prints, primitive): 3 call sites in 1 files -- `tests/functional/b/broad_exception/broad_exception_raised_trystar.py`
- `exploding_apple` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `tests/functional/b/broad_exception/broad_exception_raised.py`
- `exploding_apple` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `tests/functional/b/broad_exception/broad_exception_raised_trystar.py`
- `__false_positive` (function, debug_prints, primitive): 2 call sites in 1 files -- `tests/functional/u/unused/unused_private_member.py`
- `_regex_transformer` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `pylint/config/argument.py`
- `_template_run` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `tests/config/test_config.py`
- `gen` (function, debug_prints, primitive): 2 call sites in 2 files -- `tests/functional/m/member/member_checks_async.py`
- `good_cm_except` (function, debug_prints, primitive): 2 call sites in 1 files -- `doc/data/messages/c/contextmanager-generator-missing-cleanup/good.py`
- `good_cm_except` (function, debug_prints, primitive): 2 call sites in 1 files -- `tests/functional/c/contextmanager_generator_missing_cleanup.py`
- `good_cm_except` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `doc/data/messages/c/contextmanager-generator-missing-cleanup/good.py`
*(+37 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 14512 call pairs -- scoped 30.1%, unique 0.0%, ambiguous 11.3%, external 58.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 14512 | 30.1% | 0.0% | 11.3% | 58.6% |

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
