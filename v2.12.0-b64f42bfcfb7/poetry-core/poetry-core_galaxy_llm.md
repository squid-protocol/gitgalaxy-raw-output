# ARCHITECTURAL_BRIEF: poetry-core
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
- **Scope:** 412 analyzed artifact(s), 34253 LOC.
- **Load-bearing artifact:** `poetry_core-2.3.2/src/poetry/core/_vendor/packaging/utils.py` -- 21 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `poetry_core-2.3.2/src/poetry/core/masonry/builders/wheel.py` -- pulls in 29 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `poetry_core-2.3.2/src/poetry/core/_vendor/lark/load_grammar.py` at magnitude 1566.9 (structural weight, not risk).
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
| Total Artifacts | 591 |
| Analyzed Artifacts (Scanned) | 412 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 179 |
| Total LOC | 34253 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 69.7% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6555 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0596 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 11.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1157 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 21 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 342 | 32978 | 83.0% |
| PLAINTEXT | 43 | 0 | 10.4% |
| JSON | 9 | 1116 | 2.2% |
| SHELL | 6 | 12 | 1.5% |
| C | 5 | 147 | 1.2% |
| MARKDOWN | 4 | 0 | 1.0% |
| XML | 3 | 0 | 0.7% |

## 4.1 SOURCE ENCODINGS
All 412 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 59%, Generic / Templated Code Files 17%, Large Core Modules (2) 7%, Large Core Modules (3) 7%, Declarative / Non-Code 2%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 365 | 88.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 47 | 11.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 179*

**Composition by Extension & Reason:**
- `.toml`: 91x Excluded (Unsupported Extension: '.toml')
- `.rst`: 41x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Unsupported Format (.undeterminable)
- `.typed`: 7x Excluded (Unsupported Extension: '.typed')
- `.lark`: 6x Excluded (Unsupported Extension: '.lark')
- `.py`: 1x Excluded (Saturation: Line 33 exceeds 500 chars)
- `.apache`: 1x Excluded (Unsupported Extension: '.APACHE')
- `.bsd`: 1x Excluded (Unsupported Extension: '.BSD')
- `.json`: 1x Excluded (Massive Static Asset Blob: 3638 LOC)
- `.zip`: 1x Excluded (Explicitly Denied Extension: '.zip')
- `.whl`: 1x Excluded (Unsupported Extension: '.whl')
- `.gz`: 1x Excluded (Explicitly Denied Extension: '.gz')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 19.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 91.0 | 33.5 | 46.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 11.1 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 97.5 | 15.2 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 99.5 | 0.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 30.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 51.0 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 40.2 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 724 | 91 | 6 | `poetry_core-2.3.2/tests/version/test_markers.py` |
| cleanup | 5 | 3 | 0 | `poetry_core-2.3.2/src/poetry/core/_vendor/lark/tools/standalone.py` |
| guards | 3200 | 144 | 21 | `poetry_core-2.3.2/tests/test_factory.py` |
| danger | 950 | 118 | 7 | `poetry_core-2.3.2/src/poetry/core/_vendor/tomli/_parser.py` |
| concurrency | 183 | 34 | 0 | `poetry_core-2.3.2/src/poetry/core/_vendor/packaging/tags.py` |
| connectivity | 2177 | 173 | 16 | `poetry_core-2.3.2/src/poetry/core/version/markers.py` |
| io | 306 | 80 | 2 | `poetry_core-2.3.2/tests/packages/test_main.py` |
| crypto | 4 | 4 | 0 | `poetry_core-2.3.2/src/poetry/core/_vendor/lark/load_grammar.py` |
| ipc | 41 | 7 | 0 | `poetry_core-2.3.2/src/poetry/core/masonry/builders/wheel.py` |
| time | 2 | 1 | 0 | `poetry_core-2.3.2/src/poetry/core/_vendor/tomli/_re.py` |
| serialization | 5 | 3 | 0 | `poetry_core-2.3.2/src/poetry/core/_vendor/lark/lark.py` |
| regex | 76 | 28 | 0 | `poetry_core-2.3.2/src/poetry/core/vcs/git.py` |
| events | 73 | 16 | 0 | `poetry_core-2.3.2/src/poetry/core/_vendor/lark/lexer.py` |
| tests | 1154 | 52 | 4 | `poetry_core-2.3.2/tests/test_factory.py` |
| docs | 575 | 103 | 4 | `poetry_core-2.3.2/src/poetry/core/_vendor/packaging/metadata.py` |
| debt | 109 | 39 | 0 | `poetry_core-2.3.2/src/poetry/core/version/markers.py` |
| mutation | 11065 | 207 | 87 | `poetry_core-2.3.2/src/poetry/core/_vendor/lark/load_grammar.py` |
| dead_code | 622 | 63 | 3 | `poetry_core-2.3.2/tests/version/test_markers.py` |
| credential | 5 | 3 | 0 | `poetry_core-2.3.2/src/poetry/core/vcs/git.py` |
| threat | 8 | 1 | 0 | `poetry_core-2.3.2/tests/packages/test_package.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 2 | 1 | 0 | `poetry_core-2.3.2/tests/packages/test_main.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `poetry_core-2.3.2/tests/packages/test_main.py` (Hits: 29)
- `poetry_core-2.3.2/tests/test_factory.py` (Hits: 22)
- `poetry_core-2.3.2/tests/masonry/builders/test_sdist.py` (Hits: 19)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **utils.py** (`poetry_core-2.3.2/src/poetry/core/_vendor/packaging/utils.py`) — 21 inbound connections
2. **__init__.py** (`poetry_core-2.3.2/src/poetry/core/constraints/version/__init__.py`) — 21 inbound connections
3. **dependency.py** (`poetry_core-2.3.2/src/poetry/core/packages/dependency.py`) — 20 inbound connections
4. **lexer.py** (`poetry_core-2.3.2/src/poetry/core/_vendor/lark/lexer.py`) — 19 inbound connections
5. **exceptions.py** (`poetry_core-2.3.2/src/poetry/core/_vendor/lark/exceptions.py`) — 18 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **wheel.py** (`poetry_core-2.3.2/src/poetry/core/masonry/builders/wheel.py`) — 29 outbound dependencies
2. **factory.py** (`poetry_core-2.3.2/src/poetry/core/factory.py`) — 25 outbound dependencies
3. **lark.py** (`poetry_core-2.3.2/src/poetry/core/_vendor/lark/lark.py`) — 23 outbound dependencies
4. **dependency.py** (`poetry_core-2.3.2/src/poetry/core/packages/dependency.py`) — 22 outbound dependencies
5. **package.py** (`poetry_core-2.3.2/src/poetry/core/packages/package.py`) — 22 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` **(Many-Argument Workhorses)** (@ `poetry_core-2.3.2/src/poetry/core/_vendor/lark/lark.py`) -> Impact: **135.6** | LOC: 192
- `_configure_package_metadata` **(Many-Argument Workhorses)** (@ `poetry_core-2.3.2/src/poetry/core/factory.py`) -> Impact: **120.2** | LOC: 151
- `compile` **(Many-Argument Workhorses)** (@ `poetry_core-2.3.2/src/poetry/core/_vendor/lark/load_grammar.py`) -> Impact: **114.2** | LOC: 124
  * *Intent:* # We change the trees in-place (to support huge grammars) # So deepcopy allows calling compile more than once. term_defs = [(n, (nr_deepcopy_tree(t), ...
- `predict_and_complete` **(Many-Argument Workhorses)** (@ `poetry_core-2.3.2/src/poetry/core/_vendor/lark/parsers/earley.py`) -> Impact: **86.6** | LOC: 91
  * *Intent:* """The core Earley Predictor and Completer. At each stage of the input, we handling any completed items (things that matched on the last cycle) and us...
- `create_nested_marker` **(Many-Argument Workhorses)** (@ `poetry_core-2.3.2/src/poetry/core/packages/utils/utils.py`) -> Impact: **85.1** | LOC: 109
- `_validate_legacy_vs_project` **(Many-Argument Workhorses)** (@ `poetry_core-2.3.2/src/poetry/core/factory.py`) -> Impact: **84.4** | LOC: 128
- `_parse` **(Many-Argument Workhorses)** (@ `poetry_core-2.3.2/src/poetry/core/_vendor/lark/parsers/xearley.py`) -> Impact: **82.3** | LOC: 128
- `create_from_pep_508` **(Many-Argument Workhorses)** (@ `poetry_core-2.3.2/src/poetry/core/packages/dependency.py`) -> Impact: **76.3** | LOC: 140
- `_merge_single_markers` **(Many-Argument Workhorses)** (@ `poetry_core-2.3.2/src/poetry/core/version/markers.py`) -> Impact: **75.0** | LOC: 99
- `__init__` **(Many-Argument Workhorses)** (@ `poetry_core-2.3.2/src/poetry/core/version/markers.py`) -> Impact: **71.1** | LOC: 81

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `poetry_core-2.3.2/src/poetry/core/_vendor/lark` | 17 | 5733.94 | 62.95% | 32.24% |
| `poetry_core-2.3.2/src/poetry/core/_vendor/lark/parsers` | 11 | 3065.06 | 64.01% | 23.9% |
| `poetry_core-2.3.2/src/poetry/core/_vendor/packaging` | 14 | 2873.96 | 42.7% | 24.04% |
| `poetry_core-2.3.2/src/poetry/core/packages` | 11 | 1837.66 | 69.19% | 0.84% |
| `poetry_core-2.3.2/src/poetry/core/version` | 6 | 1689.74 | 37.91% | 16.39% |
| `poetry_core-2.3.2/src/poetry/core/constraints/version` | 11 | 1469.24 | 47.82% | 0.0% |
| `poetry_core-2.3.2/src/poetry/core` | 3 | 1335.36 | 65.22% | 0.0% |
| `poetry_core-2.3.2/tests/packages` | 10 | 1294.76 | 18.35% | 0.0% |
| `poetry_core-2.3.2/src/poetry/core/masonry/builders` | 4 | 1126.48 | 52.01% | 0.0% |
| `poetry_core-2.3.2/tests/version` | 3 | 1091.96 | 8.84% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `poetry_core-2.3.2/src/poetry/core/_vendor/packaging/_structures.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/_vendor/lark/indenter.py` -> **99.9855%** Exposure
- `poetry_core-2.3.2/src/poetry/core/_vendor/lark/parsers/xearley.py` -> **99.917%** Exposure
- `poetry_core-2.3.2/src/poetry/core/_vendor/lark/tools/nearley.py` -> **99.7423%** Exposure
- `poetry_core-2.3.2/src/poetry/core/version/markers.py` -> **98.3465%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `poetry_core-2.3.2/src/poetry/core/_vendor/fastjsonschema/generator.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/_vendor/fastjsonschema/ref_resolver.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/_vendor/lark/common.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/_vendor/lark/exceptions.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/_vendor/lark/grammar.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `poetry_core-2.3.2/tests/version/test_markers.py` -> **87** Orphaned Functions | **0** Duplicates
- `poetry_core-2.3.2/tests/test_factory.py` -> **61** Orphaned Functions | **0** Duplicates
- `poetry_core-2.3.2/tests/packages/test_package.py` -> **47** Orphaned Functions | **0** Duplicates
- `poetry_core-2.3.2/tests/packages/test_dependency.py` -> **27** Orphaned Functions | **0** Duplicates
- `poetry_core-2.3.2/src/poetry/core/version/markers.py` -> **0** Orphaned Functions | **26** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1119` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `poetry_core-2.3.2/src/poetry/core/_vendor/lark/load_grammar.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.921)
- **Top Global Matches:** file_cluster_4: 8.921, file_cluster_12: 8.999, file_cluster_5: 9.633
- **Magnitude:** 1566.9 | **LOC:** 1430 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **21**; blast radius 1.652; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.7%), Guard Balance (formerly Safety Score) (72.4%)
- **Documentation Coverage:** 94.7761% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compile` **(Many-Argument Workhorses)** (Impact: 114.2)
    * *Intent:* # We change the trees in-place (to support huge grammars) # So deepcopy allows calling compile more ...
  * `load_grammar` **(Many-Argument Workhorses)** (Impact: 45.0)
  * `pattern` **(Defensive Guards)** (Impact: 33.3)
  * `_unpack_import` **(Stateful Encapsulated Methods)** (Impact: 31.9)
  * `do_import` **(Many-Argument Workhorses)** (Impact: 31.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 202 instances
* *State Mutation (weighted view):* 672
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 323`, `structural_boundaries: 313`, `args: 91`, `func_start: 84`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 268`, `planned_debt: 4`
* *Architecture:* `io: 15`, `api: 60`, `import: 20`
* *Defense:* `safety: 100`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.652
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.042468
  * `Imports (Out-Degree: 9):` .common, .exceptions, .grammar, .lexer, .parse_tree_builder, .parser_frontends, .tree, .utils...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/version/markers.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.514)
- **Top Global Matches:** file_cluster_5: 9.514, file_cluster_4: 9.941, file_cluster_0: 10.996
- **Magnitude:** 1498.64 | **LOC:** 1396 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **18**; blast radius 5.138; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.3%), Complexity Load (formerly Cognitive Load) (95.8%), Connectivity (formerly Api Exposure) (81.0%)
- **Documentation Coverage:** 93.9698% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_merge_single_markers` **(Many-Argument Workhorses)** (Impact: 75.0)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 71.1)
  * `intersect_simplify` **(Defensive Guards)** (Impact: 39.5)
    * *Intent:* """ Finds a couple of easy simplifications for intersection on MarkerUnions: - intersection with any...
  * `union_simplify` **(Defensive Guards)** (Impact: 39.4)
    * *Intent:* """ Finds a couple of easy simplifications for union on MultiMarkers: - union with any marker that a...
  * `_compact_markers` **(Many-Argument Workhorses)** (Impact: 38.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 200 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 616
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 293`, `structural_boundaries: 409`, `args: 120`, `func_start: 118`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 216`, `dead_code: 1`, `duplicate_logic: 26`
* *Architecture:* `io: 2`, `api: 93`, `concurrency: 2`, `import: 46`
* *Defense:* `safety: 80`, `doc: 10`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.138
  * `Choke Point (Betweenness):` 0.004404 | `Ripple Effect (Closeness):` 0.052927
  * `Imports (Out-Degree: 11):` __future__, abc, collections, collections.abc, functools, itertools, lark, packaging.utils...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/factory.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.136)
- **Top Global Matches:** file_cluster_8: 9.136, file_cluster_6: 18.428, file_cluster_3: 20.747
- **Magnitude:** 1247.1 | **LOC:** 1087 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **25**; blast radius 3.196; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_configure_package_metadata` **(Many-Argument Workhorses)** (Impact: 120.2)
  * `_validate_legacy_vs_project` **(Many-Argument Workhorses)** (Impact: 84.4)
  * `_validate_strict` **(Many-Argument Workhorses)** (Impact: 59.9)
  * `create_dependency` **(Many-Argument Workhorses)** (Impact: 56.2)
  * `_configure_package_dependencies` **(Many-Argument Workhorses)** (Impact: 52.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 196 instances
* *State Mutation (weighted view):* 615
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 132`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 223`
* *Architecture:* `io: 1`, `api: 7`, `import: 41`
* *Defense:* `safety: 31`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.196
  * `Choke Point (Betweenness):` 0.002725 | `Ripple Effect (Closeness):` 0.019465
  * `Imports (Out-Degree: 18):` __future__, collections, collections.abc, itertools, logging, packaging.licenses, packaging.utils, pathlib...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/tests/version/test_markers.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.924)
- **Top Global Matches:** file_cluster_4: 7.924, file_cluster_0: 10.878, file_cluster_15: 11.086
- **Magnitude:** 1057.4 | **LOC:** 2764 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.213; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (22.6%), Connectivity (formerly Api Exposure) (11.3%)
- **Documentation Coverage:** 93.1818% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_complex_intersection_with_itertools_product_duplicates` **(Compute Cores)** (Impact: 42.8)
    * *Intent:* """ Real-world example from https://github.com/python-poetry/poetry/issues/10250. (Only occurs if th...
  * `test_complex_union_is_deterministic` **(Compute Cores)** (Impact: 33.4)
    * *Intent:* """ This test might fail sporadically if marker operations are not deterministic! """
  * `test_intersection_avoids_combinatorial_explosion` **(Defensive Guards)** (Impact: 26.5)
    * *Intent:* """ combinatorial explosion without AtomicMultiMarker and AtomicMarkerUnion based gevent constraint ...
  * `test_merging_python_version_and_python_full_version` **(Many-Argument Workhorses)** (Impact: 19.4)
  * `test_complex_union` **(I/O & Config Routines)** (Impact: 18.6)
    * *Intent:* """ real world example on the way to get mutually exclusive markers for numpy(>=1.21.2) of https://p...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 130 instances
* *State Mutation (weighted view):* 434
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 866`, `structural_boundaries: 256`, `args: 88`, `func_start: 88`
* *Risk/State:* `state_mutation: 174`, `unreferenced_by_name: 87`
* *Architecture:* `io: 4`, `api: 88`, `import: 20`
* *Defense:* `safety: 131`, `doc: 6`, `test: 113`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, os, poetry.core.constraints.generic, poetry.core.constraints.version, poetry.core.version.markers, pytest, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `poetry_core-2.3.2/tests/test_factory.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.327)
- **Top Global Matches:** file_cluster_12: 9.327, file_cluster_5: 9.605, file_cluster_4: 9.747
- **Magnitude:** 819.02 | **LOC:** 2109 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 1.213; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.3%), Complexity Load (formerly Cognitive Load) (22.6%), Connectivity (formerly Api Exposure) (10.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_create_poetry` **(Defensive Guards)** (Impact: 46.8)
  * `test_create_poetry_with_license_type` **(Many-Argument Workhorses)** (Impact: 41.1)
  * `complete_legacy_duplicate_warnings` **(I/O & Config Routines)** (Impact: 25.8)
  * `test_create_poetry_with_nested_dependency_groups` **(Many-Argument Workhorses)** (Impact: 16.9)
  * `test_validate_with_license_type` **(Many-Argument Workhorses)** (Impact: 15.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 368
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 355`, `args: 68`, `func_start: 64`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 204`, `unreferenced_by_name: 61`
* *Architecture:* `io: 22`, `api: 64`, `import: 21`
* *Defense:* `safety: 190`, `doc: 41`, `test: 116`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` __future__, collections, packaging.utils, pathlib, poetry.core.constraints.version, poetry.core.factory, poetry.core.packages.dependency, poetry.core.packages.dependency_group...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `poetry_core-2.3.2/src/poetry/core/_vendor/lark/parsers/earley_forest.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.668)
- **Top Global Matches:** file_cluster_12: 6.668, file_cluster_7: 8.566, file_cluster_5: 9.241
- **Magnitude:** 799.78 | **LOC:** 803 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 1.508; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (54.4%)
- **Documentation Coverage:** 72.7941% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visit` **(Many-Argument Workhorses)** (Impact: 37.4)
    * *Intent:* # Visiting is a list of IDs of all symbol/intermediate nodes currently in # the stack. It serves two...
  * `transform_packed_node` **(Defensive Guards)** (Impact: 29.1)
  * `_call_rule_func` **(Stateful Encapsulated Methods)** (Impact: 12.4)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 11.6)
  * `visit_packed_node_out` **(Type Conversions)** (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 104 instances
* *State Mutation (weighted view):* 377
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 185`, `args: 76`, `func_start: 76`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 169`, `duplicate_logic: 2`
* *Architecture:* `api: 59`, `import: 10`
* *Defense:* `safety: 20`, `doc: 31`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.508
  * `Choke Point (Betweenness):` 3.7e-05 | `Ripple Effect (Closeness):` 0.005474
  * `Imports (Out-Degree: 4):` ..parse_tree_builder, ..tree, ..utils, ..visitors, collections, functools, importlib, operator...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/_vendor/tomli/_parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.041)
- **Top Global Matches:** file_cluster_5: 8.041, file_cluster_12: 9.364, file_cluster_0: 11.355
- **Magnitude:** 735.34 | **LOC:** 783 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 11.856; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.7%), Connectivity (formerly Api Exposure) (69.7%)
- **Documentation Coverage:** 91.1765% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_value` **(Many-Argument Workhorses)** (Impact: 50.7)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 36.7)
  * `parse_inline_table` **(Many-Argument Workhorses)** (Impact: 21.8)
  * `loads` **(Defensive Guards)** (Impact: 20.8)
    * *Intent:* """Parse TOML from a string."""
  * `parse_basic_str` **(Defensive Guards)** (Impact: 19.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 101 instances
* *State Mutation (weighted view):* 317
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 138`, `args: 36`, `func_start: 36`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 115`
* *Architecture:* `io: 2`, `api: 37`, `import: 8`
* *Defense:* `safety: 48`, `doc: 7`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.856
  * `Choke Point (Betweenness):` 0.000546 | `Ripple Effect (Closeness):` 0.026002
  * `Imports (Out-Degree: 2):` ._re, ._types, __future__, collections.abc, sys, types, typing, warnings
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/_vendor/lark/lexer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.21)
- **Top Global Matches:** file_cluster_5: 6.21, file_cluster_12: 8.966, file_cluster_7: 10.732
- **Magnitude:** 732.04 | **LOC:** 703 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **13**; blast radius 19.993; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.5%)
- **Documentation Coverage:** 98.0392% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Defensive Guards)** (Impact: 30.1)
  * `_check_regex_collisions` **(Stateful Encapsulated Methods)** (Impact: 26.1)
  * `next_token` **(Many-Argument Workhorses)** (Impact: 25.6)
  * `_create_unless` **(Stateful Encapsulated Methods)** (Impact: 21.1)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 19.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 317
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 210`, `args: 70`, `func_start: 66`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 141`
* *Architecture:* `api: 45`, `import: 13`
* *Defense:* `safety: 31`, `doc: 6`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.993
  * `Choke Point (Betweenness):` 0.001344 | `Ripple Effect (Closeness):` 0.06064
  * `Imports (Out-Degree: 5):` .common, .exceptions, .grammar, .parsers.lalr_parser_state, .utils, abc, contextlib, copy...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/_vendor/packaging/tags.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.852)
- **Top Global Matches:** file_cluster_5: 8.852, file_cluster_12: 9.268, file_cluster_4: 9.617
- **Magnitude:** 640.14 | **LOC:** 657 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 6.971; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.5%), Guard Balance (formerly Safety Score) (81.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 72.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mac_platforms` **(Many-Argument Workhorses)** (Impact: 36.8)
  * `cpython_tags` **(Many-Argument Workhorses)** (Impact: 36.4)
  * `_cpython_abis` **(Stateful Encapsulated Methods)** (Impact: 27.5)
  * `_mac_binary_formats` **(Stateful Encapsulated Methods)** (Impact: 22.3)
  * `generic_tags` **(Many-Argument Workhorses)** (Impact: 19.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 89 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 93`, `args: 31`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 103`, `planned_debt: 1`
* *Architecture:* `io: 8`, `api: 20`, `concurrency: 8`, `import: 11`
* *Defense:* `safety: 5`, `doc: 16`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.971
  * `Choke Point (Betweenness):` 0.001015 | `Ripple Effect (Closeness):` 0.050351
  * `Imports (Out-Degree: 2):` ._manylinux, ._musllinux, __future__, importlib.machinery, logging, platform, re, struct...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/_vendor/lark/lark.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.994)
- **Top Global Matches:** file_cluster_5: 7.994, file_cluster_12: 9.787, file_cluster_4: 10.771
- **Magnitude:** 569.32 | **LOC:** 681 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **23**; blast radius 6.203; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.1%), Complexity Load (formerly Cognitive Load) (77.8%)
- **Documentation Coverage:** 60.4651% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 135.6)
  * `__init__` **(Defensive Guards)** (Impact: 24.1)
  * `_load` **(Stateful Encapsulated Methods)** (Impact: 15.7)
  * `save` **(Compute Cores)** (Impact: 12.6)
    * *Intent:* """Saves the instance into the given file object Useful for caching and multiprocessing. """
  * `lex` **(Defensive Guards)** (Impact: 10.8)
    * *Intent:* """Only lex (and postlex) the text, without parsing it. Only relevant when lexer='basic' When dont_i...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 89 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 284
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 109`, `args: 22`, `func_start: 22`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 3`, `state_mutation: 106`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 9`, `api: 18`, `import: 24`
* *Defense:* `safety: 28`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.203
  * `Choke Point (Betweenness):` 0.003291 | `Ripple Effect (Closeness):` 0.055564
  * `Imports (Out-Degree: 12):` .__version__, .common, .exceptions, .grammar, .lexer, .load_grammar, .parse_tree_builder, .parser_frontends...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/packages/dependency.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.235)
- **Top Global Matches:** file_cluster_4: 8.235, file_cluster_0: 11.072, file_cluster_5: 11.826
- **Magnitude:** 563.98 | **LOC:** 546 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **22**; blast radius 11.928; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.2%), Guard Balance (formerly Safety Score) (77.9%), Connectivity (formerly Api Exposure) (55.5%)
- **Documentation Coverage:** 91.3043% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_from_pep_508` **(Many-Argument Workhorses)** (Impact: 76.3)
  * `to_pep_508` **(Many-Argument Workhorses)** (Impact: 36.2)
  * `marker` **(Stateful Encapsulated Methods)** (Impact: 31.5)
  * `_make_file_or_dir_dep` **(Many-Argument Workhorses)** (Impact: 20.4)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 13.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 85 instances
* *State Mutation (weighted view):* 263
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 161`, `args: 35`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 93`
* *Architecture:* `io: 4`, `api: 35`, `import: 46`
* *Defense:* `safety: 5`, `doc: 5`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.928
  * `Choke Point (Betweenness):` 0.007111 | `Ripple Effect (Closeness):` 0.056253
  * `Imports (Out-Degree: 17):` __future__, collections.abc, contextlib, os, packaging.utils, pathlib, poetry.core.constraints.generic, poetry.core.constraints.version...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/_vendor/lark/parsers/earley.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 16.804)
- **Top Global Matches:** file_cluster_3: 16.804, file_cluster_1: 34.017, file_cluster_8: 37.477
- **Magnitude:** 521.08 | **LOC:** 313 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 1.566; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.0%), Complexity Load (formerly Cognitive Load) (80.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `predict_and_complete` **(Many-Argument Workhorses)** (Impact: 86.6)
    * *Intent:* """The core Earley Predictor and Completer. At each stage of the input, we handling any completed it...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 62.2)
  * `_parse` **(Many-Argument Workhorses)** (Impact: 60.9)
  * `parse` **(Many-Argument Workhorses)** (Impact: 36.5)
  * `scan` **(Many-Argument Workhorses)** (Impact: 30.1)
    * *Intent:* # def create_leo_transitives(origin, start): # ... # removed at commit 4c1cfb2faf24e8f8bff7112627a00...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 74 instances
* *State Mutation (weighted view):* 226
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 43`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 78`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 6`, `import: 12`
* *Defense:* `safety: 5`, `doc: 3`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.566
  * `Choke Point (Betweenness):` 6.5e-05 | `Ripple Effect (Closeness):` 0.004866
  * `Imports (Out-Degree: 9):` ..common, ..exceptions, ..grammar, ..lexer, ..tree, ..utils, .earley_common, .earley_forest...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/packages/utils/utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.312)
- **Top Global Matches:** file_cluster_6: 9.312, file_cluster_8: 12.458, file_cluster_4: 15.784
- **Magnitude:** 500.96 | **LOC:** 434 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **16**; blast radius 9.848; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.6%), Connectivity (formerly Api Exposure) (74.6%), Complexity Load (formerly Cognitive Load) (68.6%)
- **Documentation Coverage:** 57.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_nested_marker` **(Many-Argument Workhorses)** (Impact: 85.1)
  * `normalize_python_version_markers` **(Compute Cores)** (Impact: 40.4)
  * `convert_markers` **(Defensive Guards)** (Impact: 26.3)
  * `url_to_path` **(Compute Cores)** (Impact: 20.4)
    * *Intent:* """ Convert an RFC8089 file URI to path. The logic used here is borrowed from pip https://github.com...
  * `add_constraint` **(Generic / Templated Code)** (Impact: 8.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 85 instances
* *State Mutation (weighted view):* 264
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 97`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 94`
* *Architecture:* `io: 2`, `api: 14`, `import: 32`
* *Defense:* `safety: 16`, `doc: 6`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.848
  * `Choke Point (Betweenness):` 0.001838 | `Ripple Effect (Closeness):` 0.05171
  * `Imports (Out-Degree: 7):` __future__, bz2, contextlib, dataclasses, functools, lzma, pathlib, poetry.core.constraints.generic...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/packages/package.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.477)
- **Top Global Matches:** file_cluster_5: 6.477, file_cluster_12: 8.352, file_cluster_0: 8.521
- **Magnitude:** 496.24 | **LOC:** 681 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **22**; blast radius 2.068; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.9%), Guard Balance (formerly Safety Score) (69.9%)
- **Documentation Coverage:** 88.764% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `all_classifiers` **(Compute Cores)** (Impact: 21.0)
  * `to_dependency` **(Defensive Guards)** (Impact: 16.2)
  * `with_dependency_groups` **(Many-Argument Workhorses)** (Impact: 13.1)
  * `__repr__` **(Compute Cores)** (Impact: 12.7)
  * `full_pretty_version` **(Compute Cores)** (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 207
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 189`, `args: 47`, `func_start: 46`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 81`, `planned_debt: 2`
* *Architecture:* `io: 2`, `api: 45`, `import: 40`
* *Defense:* `safety: 13`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.068
  * `Choke Point (Betweenness):` 0.00055 | `Ripple Effect (Closeness):` 0.020093
  * `Imports (Out-Degree: 17):` __future__, collections.abc, packaging.licenses, packaging.utils, pathlib, poetry.core.constraints.version, poetry.core.constraints.version.exceptions, poetry.core.packages.dependency...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/_vendor/packaging/specifiers.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.622)
- **Top Global Matches:** file_cluster_5: 7.622, file_cluster_0: 8.399, file_cluster_12: 9.337
- **Magnitude:** 484.64 | **LOC:** 1020 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **7**; blast radius 4.742; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.9%), Complexity Load (formerly Cognitive Load) (52.9%)
- **Documentation Coverage:** 55.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `filter` **(Many-Argument Workhorses)** (Impact: 29.9)
  * `filter` **(Many-Argument Workhorses)** (Impact: 27.0)
  * `contains` **(Many-Argument Workhorses)** (Impact: 20.7)
  * `__and__` **(Defensive Guards)** (Impact: 18.8)
    * *Intent:* """Return a SpecifierSet which is a combination of the two sets. :param other: The other object to c...
  * `_compare_greater_than` **(Stateful Encapsulated Methods)** (Impact: 15.4)
    * *Intent:* # Convert our spec to a Version instance, since we'll want to work with # it as a version. spec = Ve...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 166
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 116`, `args: 49`, `func_start: 47`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 68`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 28`, `import: 7`
* *Defense:* `safety: 11`, `doc: 34`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.742
  * `Choke Point (Betweenness):` 0.000291 | `Ripple Effect (Closeness):` 0.010138
  * `Imports (Out-Degree: 2):` .utils, .version, __future__, abc, itertools, re, typing
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/_vendor/lark/parse_tree_builder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.083)
- **Top Global Matches:** file_cluster_12: 8.083, file_cluster_4: 9.047, file_cluster_5: 10.395
- **Magnitude:** 454.78 | **LOC:** 392 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 2.129; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.8%)
- **Documentation Coverage:** 98.2759% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `maybe_create_child_filter` **(Many-Argument Workhorses)** (Impact: 43.8)
    * *Intent:* # Prepare empty_indices as: How many Nones to insert at each index? if _empty_indices: assert _empty...
  * `__call__` **(Stateful Encapsulated Methods)** (Impact: 19.0)
  * `create_callback` **(Defensive Guards)** (Impact: 18.9)
  * `__call__` **(Stateful Encapsulated Methods)** (Impact: 18.4)
  * `__call__` **(Compute Cores)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 179
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 85`, `args: 29`, `func_start: 29`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 79`
* *Architecture:* `api: 15`, `import: 8`
* *Defense:* `safety: 13`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.129
  * `Choke Point (Betweenness):` 3e-05 | `Ripple Effect (Closeness):` 0.043948
  * `Imports (Out-Degree: 4):` .exceptions, .lexer, .tree, .visitors, functools, itertools, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/constraints/version/version_range.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.7)
- **Top Global Matches:** file_cluster_6: 7.7, file_cluster_4: 10.401, file_cluster_8: 16.936
- **Magnitude:** 442.26 | **LOC:** 473 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **9**; blast radius 11.0; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `difference` **(Many-Argument Workhorses)** (Impact: 53.1)
  * `intersect` **(Defensive Guards)** (Impact: 36.2)
  * `allows` **(Compute Cores)** (Impact: 33.5)
  * `union` **(Compute Cores)** (Impact: 32.0)
  * `allows_any` **(Defensive Guards)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 153`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 45`
* *Architecture:* `api: 24`, `import: 16`
* *Defense:* `safety: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.0
  * `Choke Point (Betweenness):` 0.00031 | `Ripple Effect (Closeness):` 0.070958
  * `Imports (Out-Degree: 5):` __future__, contextlib, functools, poetry.core.constraints.version.empty_constraint, poetry.core.constraints.version.version, poetry.core.constraints.version.version_constraint, poetry.core.constraints.version.version_range_constraint, poetry.core.constraints.version.version_union...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/masonry/builders/sdist.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.89)
- **Top Global Matches:** file_cluster_8: 8.89, file_cluster_6: 12.868, file_cluster_4: 20.899
- **Magnitude:** 434.9 | **LOC:** 433 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **21**; blast radius 2.143; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.0%)
- **Documentation Coverage:** 90.4762% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `find_packages` **(Many-Argument Workhorses)** (Impact: 43.6)
  * `build_setup` **(Compute Cores)** (Impact: 43.3)
  * `convert_dependencies` **(Many-Argument Workhorses)** (Impact: 34.8)
  * `build` **(Many-Argument Workhorses)** (Impact: 14.5)
  * `find_files_to_add` **(Generic / Templated Code)** (Impact: 8.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 77 instances
* *State Mutation (weighted view):* 252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 85`, `args: 12`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 98`
* *Architecture:* `io: 7`, `api: 11`, `import: 25`
* *Defense:* `safety: 5`, `doc: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.143
  * `Choke Point (Betweenness):` 0.000246 | `Ripple Effect (Closeness):` 0.010138
  * `Imports (Out-Degree: 5):` __future__, collections, collections.abc, contextlib, copy, functools, gzip, io...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/_vendor/lark/visitors.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.802)
- **Top Global Matches:** file_cluster_5: 6.802, file_cluster_12: 8.575, file_cluster_7: 10.695
- **Magnitude:** 433.52 | **LOC:** 597 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **8**; blast radius 4.379; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (81.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.0%)
- **Documentation Coverage:** 89.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `v_args` **(Many-Argument Workhorses)** (Impact: 32.0)
    * *Intent:* """A convenience decorator factory for modifying the behavior of user-supplied callback methods of `...
  * `transform` **(Defensive Guards)** (Impact: 22.6)
    * *Intent:* # Tree to postfix rev_postfix = [] q: List[Branch[_Leaf_T]] = [tree] while q: t = q.pop() rev_postfi...
  * `_apply_v_args` **(Stateful Encapsulated Methods)** (Impact: 16.5)
  * `merge_transformers` **(Many-Argument Workhorses)** (Impact: 16.4)
    * *Intent:* """Merge a collection of transformers into the base_transformer, each into its own 'namespace'. When...
  * `_call_userfunc` **(Stateful Encapsulated Methods)** (Impact: 12.9)
    * *Intent:* # Assumes tree is already transformed children = new_children if new_children is not None else tree....
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 146
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 154`, `args: 49`, `func_start: 49`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 58`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 31`, `import: 8`
* *Defense:* `safety: 31`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.379
  * `Choke Point (Betweenness):` 6.7e-05 | `Ripple Effect (Closeness):` 0.054134
  * `Imports (Out-Degree: 4):` .exceptions, .lexer, .tree, .utils, abc, functools, inspect, typing
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/tests/masonry/builders/test_sdist.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.41)
- **Top Global Matches:** file_cluster_5: 7.41, file_cluster_12: 8.038, file_cluster_0: 9.144
- **Magnitude:** 432.52 | **LOC:** 883 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **20**; blast radius 1.615; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (61.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.6%), Complexity Load (formerly Cognitive Load) (27.0%)
- **Documentation Coverage:** 94.8718% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_package_target_dir` **(Defensive Guards)** (Impact: 9.4)
  * `test_make_setup` **(Defensive Guards)** (Impact: 8.7)
  * `test_convert_dependencies` **(I/O & Config Routines)** (Impact: 8.2)
  * `test_sdist_members_mtime_default` **(Defensive Guards)** (Impact: 8.0)
  * `test_default_with_excluded_data` **(Defensive Guards)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 12 instances
* *Amplified Cascading Flux:* 41 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 250`, `args: 39`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 12`, `state_mutation: 170`
* *Architecture:* `io: 19`, `api: 39`, `import: 23`
* *Defense:* `safety: 137`, `doc: 2`, `test: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.615
  * `Choke Point (Betweenness):` 4.1e-05 | `Ripple Effect (Closeness):` 0.003244
  * `Imports (Out-Degree: 7):` __future__, ast, collections.abc, email.parser, gzip, hashlib, logging, packaging.utils...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/_vendor/packaging/metadata.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.78)
- **Top Global Matches:** file_cluster_5: 7.78, file_cluster_12: 10.075, file_cluster_4: 11.54
- **Magnitude:** 429.74 | **LOC:** 863 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 1.213; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (90.7%), Guard Balance (formerly Safety Score) (67.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 61.2903% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_email` **(Many-Argument Workhorses)** (Impact: 42.6)
    * *Intent:* """Parse a distribution's metadata stored as email headers (e.g. from ``METADATA``). This function r...
  * `_process_license_files` **(Stateful Encapsulated Methods)** (Impact: 20.3)
  * `from_email` **(Defensive Guards)** (Impact: 15.3)
    * *Intent:* """Parse metadata from email headers. If *validate* is true, the metadata will be validated. All exc...
  * `from_raw` **(Many-Argument Workhorses)** (Impact: 14.8)
    * *Intent:* """Create an instance from :class:`RawMetadata`. If *validate* is true, all metadata will be validat...
  * `_process_description_content_type` **(Stateful Encapsulated Methods)** (Impact: 13.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 65 instances
* *State Mutation (weighted view):* 217
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 102`, `args: 24`, `func_start: 24`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 87`, `planned_debt: 2`, `unreferenced_by_name: 15`
* *Architecture:* `io: 5`, `api: 7`, `import: 13`
* *Defense:* `safety: 42`, `doc: 43`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .licenses, .requirements, .specifiers, .utils, .version, __future__, email.feedparser, email.header...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `poetry_core-2.3.2/src/poetry/core/_vendor/lark/parsers/lalr_analysis.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 10.385)
- **Top Global Matches:** file_cluster_5: 10.385, file_cluster_12: 10.79, file_cluster_4: 10.828
- **Magnitude:** 423.0 | **LOC:** 335 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 2.862; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.6%), Complexity Load (formerly Cognitive Load) (80.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compute_lalr1_states` **(Compute Cores)** (Impact: 48.3)
  * `traverse` **(Many-Argument Workhorses)** (Impact: 23.8)
    * *Intent:* # x: single node # S: stack # N: weights # X: nodes # R: relation (see above) # G: set valued functi...
  * `compute_includes_lookback` **(Compute Cores)** (Impact: 21.2)
  * `compute_reads_relations` **(Defensive Guards)** (Impact: 18.7)
    * *Intent:* # handle start state for root in self.lr0_start_states.values(): assert(len(root.kernel) == 1) for r...
  * `from_ParseTable` **(Type Conversions)** (Impact: 14.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 205
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 60`, `args: 20`, `func_start: 17`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 79`
* *Architecture:* `api: 19`, `import: 7`
* *Defense:* `safety: 5`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.862
  * `Choke Point (Betweenness):` 0.000411 | `Ripple Effect (Closeness):` 0.037428
  * `Imports (Out-Degree: 5):` ..common, ..exceptions, ..grammar, ..utils, .grammar_analysis, collections, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/_vendor/lark/parser_frontends.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.078)
- **Top Global Matches:** file_cluster_5: 7.078, file_cluster_12: 8.038, file_cluster_7: 9.995
- **Magnitude:** 405.58 | **LOC:** 285 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 1.808; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 23.9)
  * `create_earley_parser` **(Compute Cores)** (Impact: 18.8)
  * `create_lalr_parser` **(Compute Cores)** (Impact: 14.2)
  * `_wrap_lexer` **(C Struct Operations)** (Impact: 14.1)
    * *Intent:* ###{standalone
  * `parse` **(Defensive Guards)** (Impact: 13.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 168
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 92`, `args: 29`, `func_start: 29`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 66`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 23`, `import: 9`
* *Defense:* `safety: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.808
  * `Choke Point (Betweenness):` 0.001261 | `Ripple Effect (Closeness):` 0.042756
  * `Imports (Out-Degree: 8):` .common, .exceptions, .lexer, .parsers, .parsers.lalr_analysis, .parsers.lalr_parser, .tree, .utils...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/_vendor/lark/parsers/cyk.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.333)
- **Top Global Matches:** file_cluster_12: 6.333, file_cluster_15: 8.91, file_cluster_16: 9.16
- **Magnitude:** 391.64 | **LOC:** 341 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 1.213; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (75.1%), Guard Balance (formerly Safety Score) (72.2%)
- **Documentation Coverage:** 61.9048% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_parse` **(Stateful Encapsulated Methods)** (Impact: 27.7)
    * *Intent:* """Parses sentence 's' using CNF grammar 'g'."""
  * `_term` **(Stateful Encapsulated Methods)** (Impact: 21.9)
    * *Intent:* """Applies the TERM rule on 'g' (see top comment)."""
  * `__init__` **(Defensive Guards)** (Impact: 16.4)
  * `revert_cnf` **(Defensive Guards)** (Impact: 15.2)
    * *Intent:* """Reverts a parse tree (RuleNode) to its original non-CNF form (Node)."""
  * `_remove_unit_rule` **(Stateful Encapsulated Methods)** (Impact: 10.7)
    * *Intent:* """Removes 'rule' from 'g' without changing the language produced by 'g'."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 166
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 95`, `args: 34`, `func_start: 34`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 62`, `duplicate_logic: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 14`, `import: 6`
* *Defense:* `safety: 31`, `doc: 19`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.213
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ..exceptions, ..grammar, ..lexer, ..tree, collections, itertools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `poetry_core-2.3.2/src/poetry/core/masonry/builders/builder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.625)
- **Top Global Matches:** file_cluster_6: 8.625, file_cluster_4: 10.23, file_cluster_5: 16.226
- **Magnitude:** 353.44 | **LOC:** 391 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **12**; blast radius 2.105; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.9%), Guard Balance (formerly Safety Score) (70.3%)
- **Documentation Coverage:** 92.1053% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `find_files_to_add` **(Many-Argument Workhorses)** (Impact: 40.4)
    * *Intent:* """ Finds all files to add to the tarball """
  * `find_excluded_files` **(Stateful Encapsulated Methods)** (Impact: 29.5)
  * `get_metadata_content` **(Compute Cores)** (Impact: 25.8)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 13.4)
  * `is_excluded` **(Compute Cores)** (Impact: 12.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 75`, `args: 23`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 47`
* *Architecture:* `io: 2`, `api: 19`, `import: 14`
* *Defense:* `safety: 6`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.105
  * `Choke Point (Betweenness):` 0.00025 | `Ripple Effect (Closeness):` 0.010838
  * `Imports (Out-Degree: 6):` __future__, functools, logging, pathlib, poetry.core.masonry.metadata, poetry.core.masonry.utils.module, poetry.core.masonry.utils.package_include, poetry.core.poetry...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `poetry_core-2.3.2/tests/vcs/test_vcs.py` (PYTHON) | Magnitude: 66.14 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 493, structural_boundaries: 77, safety: 34, core_var_decl: 24
- `poetry_core-2.3.2/tests/integration/test_pep517_backend.py` (PYTHON) | Magnitude: 9.26 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 12, import: 5, core_var_decl: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `poetry_core-2.3.2/tests/constraints/generic/test_multi_constraint.py` (PYTHON) | Magnitude: 9.46 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 22, import: 8, safety: 5
- `poetry_core-2.3.2/tests/constraints/generic/test_union_constraint.py` (PYTHON) | Magnitude: 9.46 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 22, import: 8, safety: 5
- `poetry_core-2.3.2/src/poetry/core/constraints/version/__init__.py` (PYTHON) | Magnitude: 17.46 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 20, import: 10, indent_spaces: 10, api: 1
- `poetry_core-2.3.2/src/poetry/core/constraints/generic/__init__.py` (PYTHON) | Magnitude: 17.38 | Delta: **0.135** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 18, import: 9, indent_spaces: 8, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `poetry_core-2.3.2/src/poetry/core/_vendor/lark/load_grammar.py` (PYTHON) | Magnitude: 1566.9 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 986, branch: 323, structural_boundaries: 313, state_mutation: 268
- `poetry_core-2.3.2/src/poetry/core/_vendor/lark/exceptions.py` (PYTHON) | Magnitude: 216.82 | Delta: **0.204** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 150, structural_boundaries: 57, state_mutation: 54, branch: 35

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `poetry_core-2.3.2/src/poetry/core/packages/dependency.py` -> **Severity: 0.711** (Bridge: 0.0071 * Flux: 100.0%)
- `poetry_core-2.3.2/src/poetry/core/version/markers.py` -> **Severity: 0.44** (Bridge: 0.0044 * Flux: 100.0%)
- `poetry_core-2.3.2/src/poetry/core/_vendor/lark/lark.py` -> **Severity: 0.329** (Bridge: 0.0033 * Flux: 100.0%)
- `poetry_core-2.3.2/src/poetry/core/factory.py` -> **Severity: 0.273** (Bridge: 0.0027 * Flux: 100.0%)
- `poetry_core-2.3.2/src/poetry/core/_vendor/packaging/utils.py` -> **Severity: 0.219** (Bridge: 0.0022 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `poetry_core-2.3.2/src/poetry/core/_vendor/packaging/version.py` -> **Severity: 5.448** (Embedded: 0.0791 * Error Risk: 68.8899%)
- `poetry_core-2.3.2/src/poetry/core/_vendor/packaging/utils.py` -> **Severity: 5.225** (Embedded: 0.0734 * Error Risk: 71.2221%)
- `poetry_core-2.3.2/src/poetry/core/_vendor/lark/utils.py` -> **Severity: 4.981** (Embedded: 0.0623 * Error Risk: 80.0%)
- `poetry_core-2.3.2/src/poetry/core/_vendor/lark/lexer.py` -> **Severity: 4.7** (Embedded: 0.0606 * Error Risk: 77.5129%)
- `poetry_core-2.3.2/src/poetry/core/constraints/version/version_union.py` -> **Severity: 4.503** (Embedded: 0.066 * Error Risk: 68.1984%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `poetry_core-2.3.2/src/poetry/core/constraints/version/version.py` -> **Severity: 2917.7** (Blast Radius: 29.177 * Doc Risk: 100.0%)
- `poetry_core-2.3.2/src/poetry/core/constraints/version/version_constraint.py` -> **Severity: 2010.4** (Blast Radius: 20.104 * Doc Risk: 100.0%)
- `poetry_core-2.3.2/src/poetry/core/_vendor/lark/lexer.py` -> **Severity: 1960.098** (Blast Radius: 19.993 * Doc Risk: 98.0392%)
- `poetry_core-2.3.2/src/poetry/core/_vendor/lark/utils.py` -> **Severity: 1864.835** (Blast Radius: 21.351 * Doc Risk: 87.3418%)
- `poetry_core-2.3.2/src/poetry/core/constraints/version/version_range_constraint.py` -> **Severity: 1672.2** (Blast Radius: 16.722 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 7068 call pairs -- scoped 39.1%, unique 0.0%, ambiguous 10.9%, external 50.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 7056 | 39.1% | 0.0% | 11.0% | 49.9% |
| c | 12 | 0.0% | 0.0% | 0.0% | 100.0% |

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
