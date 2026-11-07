# ARCHITECTURAL_BRIEF: cython
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/cython/cython.git` |
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
- **Scope:** 2014 analyzed artifact(s), 186668 LOC.
- **Load-bearing artifact:** `Cython/TestUtils.py` -- 45 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `runtests.py` -- pulls in 68 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `Cython/Compiler/ExprNodes.py` at magnitude 18949.94 (structural weight, not risk).
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
| Total Artifacts | 2705 |
| Analyzed Artifacts (Scanned) | 2014 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 691 |
| Total LOC | 186668 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 74.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5154 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0957 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.2018 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 30 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 1862 | 162161 | 92.5% |
| C | 81 | 21683 | 4.0% |
| PLAINTEXT | 28 | 0 | 1.4% |
| YAML | 15 | 1268 | 0.7% |
| CPP | 9 | 495 | 0.4% |
| MAKEFILE | 6 | 192 | 0.3% |
| CSS | 6 | 180 | 0.3% |
| MARKDOWN | 3 | 0 | 0.1% |
| JAVASCRIPT | 1 | 511 | 0.0% |
| SHELL | 1 | 173 | 0.0% |
| XML | 1 | 0 | 0.0% |
| BATCH | 1 | 5 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 3 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 2010 |
| cp1252 | cp1252-fallback | 2 |
| latin-1 | latin-1-fallback | 1 |
| utf-8 | bom | 1 |

> 1 guessed file(s) read as double-byte text that decodes strictly as euc_kr: if that is the estate's code page, rescan with `--source-encoding euc_kr` (or the right one of those). E.g. `tests/run/str_encoding_latin1.pyx`.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 33%, Parameter Forwarders Files 23%, Declarative / Non-Code 10%, Interface Declarations Files 8%, Large Core Modules (3) 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1982 | 98.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 32 | 1.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 691*

**Composition by Extension & Reason:**
- `.pyx`: 183x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 71 LOC), 1x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.py`: 181x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 39757 commas in 8716 LOC), 1x Excluded (Saturation: Line 16 exceeds 500 chars)
- `.srctree`: 111x Excluded (Unsupported Extension: '.srctree'), 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 75x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Excluded (Unsupported Extension: '.rst')
- `.pxd`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unsupported Format (.undeterminable)
- `.png`: 11x Excluded (Explicitly Denied Extension: '.png')
- `.h`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.broken`: 5x Excluded (Unsupported Extension: '.BROKEN')
- `.c`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 47 LOC)
- `.ipynb`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.nodistutils`: 2x Excluded (Unsupported Extension: '.nodistutils')
- `.gif`: 2x Excluded (Explicitly Denied Extension: '.gif')
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.csv`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.5 | 7.7 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.2 | 41.4 | 51.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 7.0 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 8.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.9 | 1.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.2 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 46.5 | 33.3 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2095 | 332 | 2 | `tests/run/python_bool_type.pyx` |
| cleanup | 95 | 32 | 0 | `Makefile` |
| guards | 9924 | 839 | 8 | `tests/run/builtin_exceptions.py` |
| danger | 5927 | 759 | 6 | `tests/run/test_grammar.py` |
| concurrency | 1663 | 139 | 0 | `tests/run/test_asyncgen.py` |
| connectivity | 17022 | 1220 | 15 | `Cython/Compiler/ExprNodes.py` |
| io | 1300 | 145 | 0 | `runtests.py` |
| crypto | 5 | 5 | 0 | `tests/run/reduce_pickle.pyx` |
| ipc | 76 | 11 | 0 | `runtests.py` |
| time | 51 | 20 | 0 | `runtests.py` |
| serialization | 14 | 6 | 0 | `Tools/dataclass_test_data/test_dataclasses.py` |
| regex | 145 | 43 | 0 | `tests/run/if_else_expr.pyx` |
| events | 177 | 35 | 0 | `tests/run/test_coroutines_pep492.pyx` |
| tests | 3735 | 392 | 3 | `tests/run/test_patma.py` |
| docs | 9207 | 1355 | 11 | `tests/run/extsubscript.py` |
| debt | 3057 | 441 | 3 | `Cython/Compiler/ExprNodes.py` |
| mutation | 67373 | 1427 | 50 | `Cython/Compiler/ExprNodes.py` |
| dead_code | 8773 | 1323 | 11 | `tests/run/test_patma.py` |
| credential | 18 | 7 | 0 | `tests/run/string_comparison.pyx` |
| threat | 78 | 10 | 0 | `tests/run/test_unicode.pyx` |
| ml_ai | 90 | 38 | 0 | `Cython/Utility/Optimize.c` |
| ui | 32 | 5 | 0 | `Doc/s5/ui/default/slides.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `runtests.py` (Hits: 284)
- `Tools/ci-run.sh` (Hits: 63)
- `Cython/Compiler/Main.py` (Hits: 54)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **TestUtils.py** (`Cython/TestUtils.py`) — 45 inbound connections
2. **Errors.py** (`Cython/Compiler/Errors.py`) — 33 inbound connections
3. **util.py** (`Demos/benchmarks/util.py`) — 26 inbound connections
4. **PyrexTypes.py** (`Cython/Compiler/PyrexTypes.py`) — 26 inbound connections
5. **Options.py** (`Cython/Compiler/Options.py`) — 24 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **runtests.py** (`runtests.py`) — 68 outbound dependencies
2. **ExprNodes.py** (`Cython/Compiler/ExprNodes.py`) — 34 outbound dependencies
3. **Code.py** (`Cython/Compiler/Code.py`) — 28 outbound dependencies
4. **ModuleNode.py** (`Cython/Compiler/ModuleNode.py`) — 27 outbound dependencies
5. **ParseTreeTransforms.py** (`Cython/Compiler/ParseTreeTransforms.py`) — 25 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `generate_function_definitions` **(Many-Argument Workhorses)** (@ `Cython/Compiler/Nodes.py`) -> Impact: **332.7** | LOC: 494
- `declare_c_class` **(Many-Argument Workhorses)** (@ `Cython/Compiler/Symtab.py`) -> Impact: **257.4** | LOC: 117
- `analyse` **(Many-Argument Workhorses)** (@ `Cython/Compiler/Nodes.py`) -> Impact: **231.7** | LOC: 166
- `runtests` **(Many-Argument Workhorses)** (@ `runtests.py`) -> Impact: **229.1** | LOC: 342
  * *Intent:* # faulthandler should be able to provide a limited traceback # in the event of a segmentation fault. Only available on Python 3.3+ try: import faultha...
- `declare_cfunction` **(Many-Argument Workhorses)** (@ `Cython/Compiler/Symtab.py`) -> Impact: **225.2** | LOC: 105
- `generate_tuple_and_keyword_parsing_code` **(Many-Argument Workhorses)** (@ `Cython/Compiler/Nodes.py`) -> Impact: **172.6** | LOC: 233
- `generate_type_ready_code` **(Many-Argument Workhorses)** (@ `Cython/Compiler/Nodes.py`) -> Impact: **166.2** | LOC: 238
  * *Intent:* # Also called from ModuleNode for early init types. # Generate a call to PyType_Ready for an extension # type defined in this module. type = entry.typ...
- `analyse_c_function_call` **(Many-Argument Workhorses)** (@ `Cython/Compiler/ExprNodes.py`) -> Impact: **159.3** | LOC: 207
- `best_match` **(Many-Argument Workhorses)** (@ `Cython/Compiler/PyrexTypes.py`) -> Impact: **137.0** | LOC: 147
  * *Intent:* """ Given a list args of arguments and a list of functions, choose one to call which seems to be the "best" fit for this list of arguments. This funct...
- `generate_dealloc_function` **(Many-Argument Workhorses)** (@ `Cython/Compiler/ModuleNode.py`) -> Impact: **136.9** | LOC: 179

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Cython/Compiler` | 51 | 84994.24 | 53.93% | 23.7% |
| `tests/run` | 958 | 59708.76 | 4.44% | 0.0% |
| `Cython/Utility` | 40 | 15545.76 | 37.52% | 18.02% |
| `Demos/benchmarks` | 35 | 6957.36 | 55.56% | 52.53% |
| `__monolith__` | 19 | 4538.04 | 9.62% | 7.72% |
| `Cython/Debugger` | 5 | 3838.08 | 34.06% | 26.48% |
| `tests/errors` | 275 | 3339.64 | 1.16% | 0.0% |
| `Cython` | 11 | 3287.62 | 39.6% | 11.3% |
| `tests/memoryview` | 25 | 2467.24 | 6.96% | 0.0% |
| `tests/compile` | 222 | 2121.4 | 1.2% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Cython/Includes/libcpp/exception.pxd` -> **100.0%** Exposure
- `Cython/Plex/Actions.pxd` -> **100.0%** Exposure
- `Cython/Utility/TestCythonScope.pyx` -> **100.0%** Exposure
- `Demos/benchmarks/bm_chaos.pxd` -> **100.0%** Exposure
- `Demos/benchmarks/bm_getitem.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Cython/Compiler/Errors.py` -> **100.0%** Exposure
- `Cython/Compiler/Pipeline.py` -> **100.0%** Exposure
- `Cython/Debugger/Cygdb.py` -> **100.0%** Exposure
- `Cython/Debugger/DebugWriter.py` -> **100.0%** Exposure
- `Cython/Debugger/libcython.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/run/test_patma.py` -> **306** Orphaned Functions | **4** Duplicates
- `Tools/dataclass_test_data/test_dataclasses.py` -> **203** Orphaned Functions | **29** Duplicates
- `tests/run/exttype_total_ordering.pyx` -> **1** Orphaned Functions | **201** Duplicates
- `tests/run/test_coroutines_pep492.pyx` -> **102** Orphaned Functions | **92** Duplicates
- `Cython/Compiler/ExprNodes.py` -> **0** Orphaned Functions | **186** Duplicates

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
- **Unknown Dependencies:** `1557` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `Cython/Compiler/ExprNodes.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.547)
- **Top Global Matches:** file_cluster_4: 7.547, file_cluster_12: 10.335, file_cluster_15: 11.019
- **Magnitude:** 18949.94 | **LOC:** 15821 | **CtrlFlow:** 33.4% | **Authorship Centralization:** 57.6%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **34**; blast radius 3.382; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (97.7%)
- **Documentation Coverage:** 97.0561% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `analyse_c_function_call` **(Many-Argument Workhorses)** (Impact: 159.3)
  * `generate_assignment_code` **(Many-Argument Workhorses)** (Impact: 132.9)
  * `coerce_to` **(Many-Argument Workhorses)** (Impact: 118.9)
    * *Intent:* # ----------------- Coercion ---------------------- # Coerce the result so that it can be assigned t...
  * `find_common_type` **(Many-Argument Workhorses)** (Impact: 116.5)
  * `generate_sequence_packing_code` **(Many-Argument Workhorses)** (Impact: 96.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 2357 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 7731
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3894`, `structural_boundaries: 4338`, `args: 1093`, `func_start: 1090`, `class_start: 158`
* *Risk/State:* `safety_bypasses: 166`, `state_mutation: 3017`, `dead_code: 7`, `planned_debt: 42`, `fragile_debt: 33`, `duplicate_logic: 186`
* *Architecture:* `io: 3`, `api: 1173`, `concurrency: 5`, `import: 56`
* *Defense:* `safety: 221`, `doc: 53`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.382
  * `Choke Point (Betweenness):` 0.000217 | `Ripple Effect (Closeness):` 0.018784
  * `Imports (Out-Degree: 22):` ..Debugging, ..Utils, .Annotate, .AutoDocTransforms, .Buffer, .Builtin, .Code, .DebugFlags...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `Cython/Compiler/Nodes.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.241)
- **Top Global Matches:** file_cluster_4: 7.241, file_cluster_6: 10.751, file_cluster_12: 12.903
- **Magnitude:** 12177.16 | **LOC:** 10867 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 56.0%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **24**; blast radius 3.539; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 95.1883% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate_function_definitions` **(Many-Argument Workhorses)** (Impact: 332.7)
  * `analyse` **(Many-Argument Workhorses)** (Impact: 231.7)
  * `generate_tuple_and_keyword_parsing_code` **(Many-Argument Workhorses)** (Impact: 172.6)
  * `generate_type_ready_code` **(Many-Argument Workhorses)** (Impact: 166.2)
    * *Intent:* # Also called from ModuleNode for early init types. # Generate a call to PyType_Ready for an extensi...
  * `analyse_declarations` **(Compute Cores)** (Impact: 130.9)
    * *Intent:* #print "CClassDefNode.analyse_declarations:", self.class_name #print "...visibility =", self.visibil...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1504 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 5021
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2580`, `structural_boundaries: 1736`, `args: 482`, `func_start: 478`, `class_start: 108`
* *Risk/State:* `safety_bypasses: 106`, `high_risk_execution: 1`, `state_mutation: 2013`, `dead_code: 14`, `planned_debt: 16`, `fragile_debt: 18`, `duplicate_logic: 62`
* *Architecture:* `api: 554`, `concurrency: 2`, `import: 73`
* *Defense:* `safety: 123`, `doc: 46`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.539
  * `Choke Point (Betweenness):` 0.000115 | `Ripple Effect (Closeness):` 0.019405
  * `Imports (Out-Degree: 20):` ..Utils, .Buffer, .Builtin, .Code, .DebugFlags, .Errors, .ExprNodes, .Future...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `Cython/Compiler/PyrexTypes.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.576)
- **Top Global Matches:** file_cluster_12: 8.576, file_cluster_15: 9.144, file_cluster_4: 9.346
- **Magnitude:** 6557.94 | **LOC:** 5896 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 41.7%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); it depends on **16**; blast radius 4.564; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (91.5%), Complexity Load (formerly Cognitive Load) (84.3%)
- **Documentation Coverage:** 92.8793% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `best_match` **(Many-Argument Workhorses)** (Impact: 137.0)
    * *Intent:* """ Given a list args of arguments and a list of functions, choose one to call which seems to be the...
  * `declaration_code` **(Many-Argument Workhorses)** (Impact: 76.5)
  * `write_noexcept_performance_hint` **(Many-Argument Workhorses)** (Impact: 52.0)
  * `create_to_py_utility_code` **(Compute Cores)** (Impact: 50.6)
    * *Intent:* # FIXME: it seems we're trying to coerce in more cases than we should if self.to_py_function is not ...
  * `same_c_signature_as_resolved_type` **(Many-Argument Workhorses)** (Impact: 46.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 686 instances
* *State Mutation (weighted view):* 2523
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1170`, `structural_boundaries: 1640`, `args: 538`, `func_start: 534`, `class_start: 61`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 1151`, `dead_code: 3`, `planned_debt: 12`, `fragile_debt: 19`, `duplicate_logic: 41`
* *Architecture:* `api: 482`, `import: 42`
* *Defense:* `safety: 64`, `doc: 44`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.564
  * `Choke Point (Betweenness):` 0.000145 | `Ripple Effect (Closeness):` 0.020365
  * `Imports (Out-Degree: 11):` .Buffer, .Builtin, .Code, .Errors, .MemoryView, .Naming, .Options, .StringEncoding...
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `Cython/Compiler/Optimize.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.2)
- **Top Global Matches:** file_cluster_4: 6.2, file_cluster_6: 9.341, file_cluster_12: 12.582
- **Magnitude:** 6260.08 | **LOC:** 5416 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **23**; blast radius 1.24; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.3%), Complexity Load (formerly Cognitive Load) (63.5%)
- **Documentation Coverage:** 70.6215% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_try_optimise_iterator_function` **(Many-Argument Workhorses)** (Impact: 124.3)
  * `_transform_carray_iteration` **(Many-Argument Workhorses)** (Impact: 108.4)
  * `_handle_simple_method_bytes_decode` **(Many-Argument Workhorses)** (Impact: 89.8)
    * *Intent:* """Replace char*.decode() by a direct C-API call to the corresponding codec, possibly resolving a sl...
  * `optimise_numeric_binop` **(Many-Argument Workhorses)** (Impact: 86.6)
    * *Intent:* """ Optimise math operators for (likely) float or small integer operations. """
  * `extract_conditions` **(Defensive Guards)** (Impact: 78.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 834 instances
* *State Mutation (weighted view):* 2745
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1244`, `structural_boundaries: 1168`, `args: 212`, `func_start: 212`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 63`, `state_mutation: 1077`, `dead_code: 5`, `planned_debt: 5`, `fragile_debt: 6`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 138`, `import: 23`
* *Defense:* `safety: 169`, `doc: 77`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.24
  * `Choke Point (Betweenness):` 5.1e-05 | `Ripple Effect (Closeness):` 0.016999
  * `Imports (Out-Degree: 15):` ..Utils, .Builtin, .Code, .Errors, .ExprNodes, .FlowControl, .Nodes, .Options...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `Cython/Compiler/Parsing.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.75)
- **Top Global Matches:** file_cluster_4: 7.75, file_cluster_6: 8.018, file_cluster_12: 14.514
- **Magnitude:** 6089.5 | **LOC:** 4770 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **15**; blast radius 0.723; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.4%)
- **Documentation Coverage:** 95.3728% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `p_statement` **(Many-Argument Workhorses)** (Impact: 133.9)
  * `p_c_simple_declarator` **(Many-Argument Workhorses)** (Impact: 105.8)
  * `p_c_class_definition` **(Many-Argument Workhorses)** (Impact: 79.7)
    * *Intent:* # s.sy == 'class' s.next() module_path = [] class_name = p_ident(s) while s.sy == '.': s.next() modu...
  * `p_c_simple_base_type` **(Many-Argument Workhorses)** (Impact: 78.8)
  * `p_dict_or_set_maker` **(Compute Cores)** (Impact: 73.2)
    * *Intent:* # since PEP 448: #dictorsetmaker: ( ((test ':' test | '**' expr) # (comp_for | (',' (test ':' test |...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 974 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 58
* *State Mutation (weighted view):* 3049
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1229`, `structural_boundaries: 754`, `args: 195`, `func_start: 194`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 65`, `high_risk_execution: 2`, `state_mutation: 1101`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 6`
* *Architecture:* `api: 190`, `concurrency: 13`, `import: 16`
* *Defense:* `safety: 51`, `doc: 11`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.723
  * `Choke Point (Betweenness):` 5e-05 | `Ripple Effect (Closeness):` 0.015236
  * `Imports (Out-Degree: 12):` .Builtin, .Errors, .ExprNodes, .Future, .MatchCaseNodes, .ModuleNode, .Nodes, .Options...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Cython/Compiler/ParseTreeTransforms.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.486)
- **Top Global Matches:** file_cluster_4: 7.486, file_cluster_12: 7.769, file_cluster_15: 9.601
- **Magnitude:** 5304.62 | **LOC:** 4706 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 54.5%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **25**; blast radius 2.932; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (87.7%), Complexity Load (formerly Cognitive Load) (81.0%), Guard Balance (formerly Safety Score) (80.7%)
- **Documentation Coverage:** 94.0068% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `try_to_parse_directive` **(Many-Argument Workhorses)** (Impact: 118.3)
  * `_inject_pickle_methods` **(Many-Argument Workhorses)** (Impact: 74.7)
  * `_extract_directives` **(Many-Argument Workhorses)** (Impact: 65.4)
    * *Intent:* """ Returns two dicts - directives applied to this function/class and directives applied to its cont...
  * `visit_SimpleCallNode` **(Compute Cores)** (Impact: 62.3)
    * *Intent:* # cython.foo function = node.function.as_cython_attribute() if function: if function in InterpretCom...
  * `create_class_from_scope` **(Many-Argument Workhorses)** (Impact: 62.2)
    * *Intent:* # move local variables into closure if node.is_generator: for scope in node.local_scope.iter_local_s...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 691 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 2371
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 980`, `structural_boundaries: 951`, `args: 313`, `func_start: 309`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 70`, `high_risk_execution: 1`, `state_mutation: 989`, `dead_code: 2`, `planned_debt: 11`, `fragile_debt: 6`, `duplicate_logic: 16`
* *Architecture:* `api: 285`, `concurrency: 1`, `import: 26`
* *Defense:* `safety: 76`, `doc: 49`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.932
  * `Choke Point (Betweenness):` 0.000299 | `Ripple Effect (Closeness):` 0.021766
  * `Imports (Out-Degree: 20):` ..., ..Shadow, ..__version__, .Builtin, .Code, .Dataclass, .Errors, .ExprNodes...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `Cython/Compiler/Symtab.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.78)
- **Top Global Matches:** file_cluster_4: 6.78, file_cluster_12: 9.057, file_cluster_15: 10.678
- **Magnitude:** 4893.1 | **LOC:** 3092 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 44.4%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **15**; blast radius 2.491; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (95.5%), Complexity Load (formerly Cognitive Load) (91.5%), Guard Balance (formerly Safety Score) (86.8%)
- **Documentation Coverage:** 95.2909% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `declare_c_class` **(Many-Argument Workhorses)** (Impact: 257.4)
  * `declare_cfunction` **(Many-Argument Workhorses)** (Impact: 225.2)
  * `declare_var` **(Many-Argument Workhorses)** (Impact: 130.1)
  * `declare_cfunction` **(Many-Argument Workhorses)** (Impact: 115.1)
  * `declare_var` **(Many-Argument Workhorses)** (Impact: 103.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 568 instances
* *State Mutation (weighted view):* 2012
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 784`, `structural_boundaries: 858`, `args: 184`, `func_start: 184`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 876`, `dead_code: 8`, `planned_debt: 7`, `fragile_debt: 6`, `duplicate_logic: 4`
* *Architecture:* `api: 180`, `import: 18`
* *Defense:* `safety: 17`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.491
  * `Choke Point (Betweenness):` 6.4e-05 | `Ripple Effect (Closeness):` 0.019313
  * `Imports (Out-Degree: 13):` ..Utils, .Builtin, .Code, .DebugFlags, .Errors, .Naming, .Nodes, .Options...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `Cython/Compiler/ModuleNode.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.316)
- **Top Global Matches:** file_cluster_4: 6.316, file_cluster_6: 6.553, file_cluster_15: 14.622
- **Magnitude:** 4499.26 | **LOC:** 4346 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 43.8%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **27**; blast radius 1.495; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.5%), Complexity Load (formerly Cognitive Load) (76.2%)
- **Documentation Coverage:** 95.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate_dealloc_function` **(Many-Argument Workhorses)** (Impact: 136.9)
  * `generate_richcmp_function` **(Many-Argument Workhorses)** (Impact: 129.2)
  * `generate_new_function` **(Many-Argument Workhorses)** (Impact: 126.6)
  * `generate_module_init_func` **(Many-Argument Workhorses)** (Impact: 116.1)
  * `generate_cpp_class_definition` **(Many-Argument Workhorses)** (Impact: 86.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 460 instances
* *State Mutation (weighted view):* 1498
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1029`, `structural_boundaries: 748`, `args: 152`, `func_start: 152`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 6`, `state_mutation: 578`, `dead_code: 18`, `planned_debt: 8`, `fragile_debt: 6`
* *Architecture:* `io: 12`, `api: 136`, `import: 29`
* *Defense:* `safety: 26`, `doc: 11`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.495
  * `Choke Point (Betweenness):` 5.8e-05 | `Ripple Effect (Closeness):` 0.017212
  * `Imports (Out-Degree: 15):` ..Utils, ..__version__, .Annotate, .Code, .Errors, .Future, .Naming, .Nodes...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `tests/run/test_patma.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.717)
- **Top Global Matches:** file_cluster_12: 6.717, file_cluster_15: 6.976, file_cluster_11: 8.69
- **Magnitude:** 4051.3 | **LOC:** 3447 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.42; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (75.4%), Complexity Load (formerly Cognitive Load) (31.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.4%), Connectivity (formerly Api Exposure) (14.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_patma_174` **(Compute Cores)** (Impact: 18.1)
  * `test_patma_182` **(Compute Cores)** (Impact: 16.7)
  * `test_patma_177` **(Compute Cores)** (Impact: 13.9)
  * `http_error` **(Compute Cores)** (Impact: 13.4)
  * `test_patma_116` **(Compute Cores)** (Impact: 13.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 596 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 1801
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 710`, `structural_boundaries: 767`, `args: 359`, `func_start: 359`, `class_start: 65`
* *Risk/State:* `safety_bypasses: 33`, `high_risk_execution: 3`, `state_mutation: 609`, `fragile_debt: 9`, `duplicate_logic: 4`, `unreferenced_by_name: 306`
* *Architecture:* `io: 1`, `api: 373`, `import: 10`
* *Defense:* `safety: 2`, `doc: 44`, `test: 305`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Cython.TestUtils, array, collections, cython, dataclasses, enum, inspect, pyperf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `runtests.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.864)
- **Top Global Matches:** file_cluster_4: 7.864, file_cluster_6: 11.25, file_cluster_12: 11.895
- **Magnitude:** 3978.66 | **LOC:** 3333 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 43.5%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **68**; blast radius 0.897; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (83.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 46.9551% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runtests` **(Many-Argument Workhorses)** (Impact: 229.1)
    * *Intent:* # faulthandler should be able to provide a limited traceback # in the event of a segmentation fault....
  * `compile` **(Many-Argument Workhorses)** (Impact: 131.2)
  * `build_tests` **(Many-Argument Workhorses)** (Impact: 99.0)
  * `handle_directory` **(Many-Argument Workhorses)** (Impact: 94.0)
  * `main` **(I/O & Config Routines)** (Impact: 76.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 530 instances
* *High Risk Execution (weighted view):* 9
* *Concurrency (weighted view):* 66
* *State Mutation (weighted view):* 1761
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 761`, `structural_boundaries: 624`, `args: 165`, `func_start: 159`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 74`, `high_risk_execution: 16`, `state_mutation: 701`, `planned_debt: 5`, `fragile_debt: 4`
* *Architecture:* `io: 284`, `api: 153`, `concurrency: 11`, `import: 101`
* *Defense:* `safety: 126`, `doc: 11`, `test: 37`, `immutability_locks: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.897
  * `Choke Point (Betweenness):` 4.2e-05 | `Ripple Effect (Closeness):` 0.00138
  * `Imports (Out-Degree: 14):` Cython.Build.Dependencies, Cython.Compiler, Cython.Compiler.Main, Cython.Compiler.Options, Cython.Compiler.Pipeline, Cython.Compiler.Version, Cython.Runtime.refnanny, Cython.Shadow...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Cython/Compiler/Code.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.761)
- **Top Global Matches:** file_cluster_12: 7.761, file_cluster_4: 9.353, file_cluster_5: 9.998
- **Magnitude:** 3718.16 | **LOC:** 3881 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 42.1%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **28**; blast radius 3.575; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (83.0%), Complexity Load (formerly Cognitive Load) (75.7%)
- **Documentation Coverage:** 87.6712% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate_pystring_constants` **(Many-Argument Workhorses)** (Impact: 115.5)
    * *Intent:* # Concatenate all strings into one byte sequence and build a length index array. defines = self.part...
  * `allocate_temp` **(Many-Argument Workhorses)** (Impact: 54.3)
    * *Intent:* # temp handling """ Allocates a temporary (which may create a new one or get a previously allocated ...
  * `load` **(Many-Argument Workhorses)** (Impact: 52.1)
    * *Intent:* """ Load utility code from a file specified by from_file (relative to Cython/Utility) and name util_...
  * `put_pymethoddef` **(Many-Argument Workhorses)** (Impact: 48.9)
  * `generate_num_constants` **(Compute Cores)** (Impact: 47.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 408 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1450
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 602`, `structural_boundaries: 792`, `args: 303`, `func_start: 302`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 70`, `high_risk_execution: 2`, `state_mutation: 634`, `dead_code: 9`, `planned_debt: 7`, `duplicate_logic: 4`
* *Architecture:* `io: 13`, `api: 292`, `import: 32`
* *Defense:* `safety: 58`, `doc: 51`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.575
  * `Choke Point (Betweenness):` 0.000229 | `Ripple Effect (Closeness):` 0.019496
  * `Imports (Out-Degree: 13):` ..LZSS, ..StringIOTree, ..Tempita, ..Utils, .DebugFlags, .Errors, .Naming, .Options...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `tests/run/extsubscript.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 16.695)
- **Top Global Matches:** file_cluster_15: 16.695, file_cluster_16: 17.255, file_cluster_13: 17.257
- **Magnitude:** 2910.9 | **LOC:** 25865 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.42; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.0%), Connectivity (formerly Api Exposure) (12.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (8.9%), Complexity Load (formerly Cognitive Load) (1.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate_classes` **(Many-Argument Workhorses)** (Impact: 41.8)
  * `_gen_test_code` **(I/O & Config Routines)** (Impact: 33.9)
    * *Intent:* ###### END: generated test code ###### ################################################# ## This is ...
  * `_regen_test_file` **(Stateful Encapsulated Methods)** (Impact: 10.9)
  * `build_class_name` **(Compute Cores)** (Impact: 9.9)
  * `_print_setitem_Seq` **(Encapsulated Accessors)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 1749`, `args: 1091`, `func_start: 1091`, `class_start: 630`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 19`
* *Architecture:* `io: 2`, `api: 633`, `import: 4`
* *Defense:* `safety: 1`, `doc: 637`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` cython, itertools, string
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/run/test_coroutines_pep492.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.962)
- **Top Global Matches:** file_cluster_12: 7.962, file_cluster_7: 9.984, file_cluster_5: 10.524
- **Magnitude:** 2208.42 | **LOC:** 2595 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.42; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (58.4%), Complexity Load (formerly Cognitive Load) (25.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.4%)
- **Documentation Coverage:** 99.6748% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__test_for_1` **(Compute Cores)** (Impact: 24.9)
    * *Intent:* # old-style pre-Py3.5.2 protocol - no longer supported
  * `test_for_6` **(Compute Cores)** (Impact: 17.1)
  * `assertWarnsRegex` **(Defensive Guards)** (Impact: 17.0)
  * `test_comp_4` **(Compute Cores)** (Impact: 17.0)
  * `test_comp_2` **(Compute Cores)** (Impact: 12.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 84 instances
* *Amplified Cascading Flux:* 63 instances
* *High Risk Execution (weighted view):* 8
* *Concurrency (weighted view):* 738
* *State Mutation (weighted view):* 309
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 877`, `args: 357`, `func_start: 352`, `class_start: 53`
* *Risk/State:* `safety_bypasses: 56`, `high_risk_execution: 10`, `state_mutation: 183`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 4`, `duplicate_logic: 92`, `unreferenced_by_name: 102`
* *Architecture:* `io: 24`, `api: 299`, `concurrency: 318`, `import: 27`
* *Defense:* `safety: 67`, `doc: 93`, `test: 107`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Cython.Build.Inline, Cython.Compiler, Cython.TestUtils, StringIO, _testcapi, asyncio, contextlib, copy...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Cython/Debugger/libpython.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.461)
- **Top Global Matches:** file_cluster_12: 6.461, file_cluster_15: 8.739, file_cluster_16: 9.332
- **Magnitude:** 2206.78 | **LOC:** 2822 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **13**; blast radius 0.849; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.5%), Connectivity (formerly Api Exposure) (66.8%)
- **Documentation Coverage:** 73.065% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write_repr` **(Many-Argument Workhorses)** (Impact: 59.4)
    * *Intent:* # Write this out as a Python 3 str literal, i.e. without a "u" prefix # Get a PyUnicodeObject* withi...
  * `proxyval` **(Type Conversions)** (Impact: 48.6)
  * `step` **(Many-Argument Workhorses)** (Impact: 42.1)
    * *Intent:* """ Do a single step or step-over. Returns the result of the last gdb command that made execution st...
  * `invoke` **(Many-Argument Workhorses)** (Impact: 30.8)
  * `write_repr` **(Many-Argument Workhorses)** (Impact: 25.5)
    * *Intent:* # Write this out as a Python 3 bytes literal, i.e. with a "b" prefix # Get a PyStringObject* within ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 282 instances
* *Api Near Db Sink:* 7 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 963
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 362`, `structural_boundaries: 527`, `args: 186`, `func_start: 186`, `class_start: 55`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 4`, `state_mutation: 399`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 26`, `api: 190`, `import: 14`
* *Defense:* `safety: 72`, `doc: 71`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00149
  * `Imports (Out-Degree: 0):` functools, gdb, itertools, locale, os, pprint, re, sys...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tests/run/test_asyncgen.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.957)
- **Top Global Matches:** file_cluster_12: 6.957, file_cluster_7: 9.314, file_cluster_5: 10.065
- **Magnitude:** 1921.64 | **LOC:** 1370 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.42; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (54.4%), Complexity Load (formerly Cognitive Load) (46.5%), Connectivity (formerly Api Exposure) (13.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compare_generators` **(Defensive Guards)** (Impact: 14.1)
  * `async_iterate` **(Defensive Guards)** (Impact: 8.3)
  * `run_until_complete` **(Defensive Guards)** (Impact: 7.8)
  * `test_async_gen_asyncio_anext_05` **(Defensive Guards)** (Impact: 7.4)
  * `types_coroutine` **(Stateful Encapsulated Methods)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 177 instances
* *Amplified Cascading Flux:* 28 instances
* *High Risk Execution (weighted view):* 5
* *Concurrency (weighted view):* 1150
* *State Mutation (weighted view):* 234
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 446`, `args: 162`, `func_start: 160`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 6`, `state_mutation: 178`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 22`, `unreferenced_by_name: 49`
* *Architecture:* `io: 5`, `api: 163`, `concurrency: 265`, `import: 18`
* *Defense:* `safety: 107`, `doc: 7`, `test: 51`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Cython.Compiler.Errors, Cython.Shadow, Cython.TestUtils, StringIO, __future__, asyncio, contextlib, cython...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Cython/Utility/ObjectHandling.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.906)
- **Top Global Matches:** file_cluster_4: 6.906, file_cluster_16: 7.771, file_cluster_12: 9.223
- **Magnitude:** 1794.42 | **LOC:** 3353 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); blast radius 3.5; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.2%), Complexity Load (formerly Cognitive Load) (35.6%)
- **Documentation Coverage:** 41.3793% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__Pyx_SetItemInt_Fast` **(Many-Argument Workhorses)** (Impact: 66.7)
    * *Intent:* #endif
  * `__Pyx_GetItemInt_Fast` **(Many-Argument Workhorses)** (Impact: 57.0)
    * *Intent:* #endif
  * `__Pyx_PyObject_GetMethod` **(Many-Argument Workhorses)** (Impact: 51.1)
    * *Intent:* #endif /////////////// PyObjectGetMethod.proto /////////////// #if !(CYTHON_VECTORCALL && (__PYX_LIM...
  * `__Pyx_PyDict_NextRef` **(Many-Argument Workhorses)** (Impact: 42.5)
    * *Intent:* static int __Pyx_PyDict_NextRef(PyObject *p, Py_ssize_t *ppos, PyObject **pkey, PyObject **pvalue); ...
  * `__Pyx_PEP560_update_bases` **(Compute Cores)** (Impact: 36.8)
    * *Intent:* /////////////// Py3UpdateBases.proto /////////////// static PyObject* __Pyx_PEP560_update_bases(PyOb...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 220 instances
* *State Mutation (weighted view):* 677
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 479`, `structural_boundaries: 350`, `args: 333`, `func_start: 115`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 237`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 10`
* *Defense:* `safety: 25`, `doc: 155`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.5
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.00511
  * `Imports (Out-Degree: 4):` None
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `Cython/Compiler/FlowControl.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.374)
- **Top Global Matches:** file_cluster_4: 7.374, file_cluster_12: 7.784, file_cluster_15: 8.247
- **Magnitude:** 1780.54 | **LOC:** 1572 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 1.076; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (80.4%), Guard Balance (formerly Safety Score) (78.2%), Complexity Load (formerly Cognitive Load) (77.9%)
- **Documentation Coverage:** 89.9497% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_definitions` **(Many-Argument Workhorses)** (Impact: 100.4)
  * `visit_MatchNode` **(Many-Argument Workhorses)** (Impact: 48.7)
    * *Intent:* # https://peps.python.org/pep-0634/#side-effects-and-undefined-behavior # The specification of struc...
  * `mark_forloop_target` **(Compute Cores)** (Impact: 45.9)
    * *Intent:* # TODO: Remove redundancy with range optimization... is_special = False sequence = node.iterator.seq...
  * `mark_assignment` **(Many-Argument Workhorses)** (Impact: 40.9)
  * `render` **(Defensive Guards)** (Impact: 27.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 226 instances
* *State Mutation (weighted view):* 761
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 354`, `structural_boundaries: 263`, `args: 109`, `func_start: 109`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 309`, `dead_code: 6`, `planned_debt: 4`, `fragile_debt: 5`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 111`, `import: 11`
* *Defense:* `safety: 20`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.076
  * `Choke Point (Betweenness):` 3.2e-05 | `Ripple Effect (Closeness):` 0.013356
  * `Imports (Out-Degree: 10):` .Builtin, .Errors, .ExprNodes, .MatchCaseNodes, .Nodes, .Optimize, .Options, .PyrexTypes...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `tests/run/test_grammar.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 9.412)
- **Top Global Matches:** file_cluster_7: 9.412, file_cluster_12: 10.037, file_cluster_5: 10.099
- **Magnitude:** 1514.56 | **LOC:** 2041 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.42; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (38.6%), Concurrency Surface (formerly Concurrency) (24.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.6%)
- **Documentation Coverage:** 99.4475% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_genexps` **(Defensive Guards)** (Impact: 69.6)
    * *Intent:* # generator expression tests g = ([x for x in range(10)] for x in range(1)) self.assertEqual(next(g)...
  * `test_if_else_expr` **(Compute Cores)** (Impact: 64.9)
    * *Intent:* # Test ifelse expressions in various cases def _checkeval(msg, ret): "helper to check that evaluatio...
  * `test_listcomps` **(Compute Cores)** (Impact: 38.5)
    * *Intent:* # list comprehension tests nums = [1, 2, 3, 4, 5] strs = ["Apple", "Banana", "Coconut"] spcs = [" Ap...
  * `test_warn_missed_comma` **(Compute Cores)** (Impact: 33.3)
    * *Intent:* # FIXME: would be nice if this could actually raise a compile time warning as well def check(test): ...
  * `test_test` **(Compute Cores)** (Impact: 24.5)
    * *Intent:* # ### and_test ('or' and_test)* ### and_test: not_test ('and' not_test)* ### not_test: 'not' not_tes...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Cascading Flux:* 89 instances
* *High Risk Execution (weighted view):* 22
* *State Mutation (weighted view):* 413
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 311`, `structural_boundaries: 714`, `args: 275`, `func_start: 218`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 180`, `high_risk_execution: 29`, `state_mutation: 235`, `dead_code: 4`, `fragile_debt: 21`, `duplicate_logic: 15`, `unreferenced_by_name: 87`
* *Architecture:* `io: 4`, `api: 157`, `concurrency: 17`, `import: 24`
* *Defense:* `safety: 106`, `doc: 11`, `test: 86`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Cython.Build.Inline, Cython.Compiler.Main, Cython.TestUtils, StringIO, contextlib, cython, inspect, io...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Cython/Tempita/_tempita.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.977)
- **Top Global Matches:** file_cluster_6: 7.977, file_cluster_4: 9.314, file_cluster_12: 15.492
- **Magnitude:** 1503.3 | **LOC:** 1088 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 1.384; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.4%), Guard Balance (formerly Safety Score) (83.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 95.6989% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_signature` **(Many-Argument Workhorses)** (Impact: 77.8)
  * `parse_expr` **(Many-Argument Workhorses)** (Impact: 62.6)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 55.7)
  * `lex` **(Many-Argument Workhorses)** (Impact: 51.9)
    * *Intent:* ############################################################ ## Lexing and Parsing #################...
  * `trim_lex` **(Compute Cores)** (Impact: 46.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 224 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 705
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 291`, `structural_boundaries: 195`, `args: 57`, `func_start: 57`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 5`, `state_mutation: 257`
* *Architecture:* `io: 10`, `api: 34`, `import: 11`
* *Defense:* `safety: 45`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.384
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.014392
  * `Imports (Out-Degree: 1):` ._looper, cython, io, optparse, os, re, sys, tokenize...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Cython/Debugger/libcython.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.002)
- **Top Global Matches:** file_cluster_12: 7.002, file_cluster_4: 8.474, file_cluster_15: 8.636
- **Magnitude:** 1465.12 | **LOC:** 1549 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.512; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Connectivity (formerly Api Exposure) (65.2%), Complexity Load (formerly Cognitive Load) (41.7%)
- **Documentation Coverage:** 86.6197% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_break_funcname` **(Stateful Encapsulated Methods)** (Impact: 42.2)
  * `complete` **(Compute Cores)** (Impact: 37.6)
    * *Intent:* # https://sourceware.org/git/?p=binutils-gdb.git;a=blob;f=gdb/python/py-cmd.c;h=7143c1c5f7fdce9316a8...
  * `print_stackframe` **(Many-Argument Workhorses)** (Impact: 30.0)
    * *Intent:* """ Print a C, Cython or Python stack frame and the line of source code if available. """
  * `invoke` **(Many-Argument Workhorses)** (Impact: 25.6)
  * `invoke` **(Many-Argument Workhorses)** (Impact: 24.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 201 instances
* *Api Near Db Sink:* 4 instances
* *State Mutation (weighted view):* 716
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 243`, `args: 79`, `func_start: 77`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 3`, `state_mutation: 314`
* *Architecture:* `io: 9`, `api: 98`, `import: 14`
* *Defense:* `safety: 51`, `doc: 42`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.512
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000662
  * `Imports (Out-Degree: 2):` Cython.Debugger, collections, functools, gdb, inspect, itertools, lxml, pygments.formatters...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Cython/Utility/Optimize.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.429)
- **Top Global Matches:** file_cluster_6: 5.429, file_cluster_4: 10.584, file_cluster_8: 14.547
- **Magnitude:** 1301.24 | **LOC:** 2474 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 54.5%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 2.228; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (68.5%), Guard Balance (formerly Safety Score) (66.0%)
- **Documentation Coverage:** 60.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__Pyx__PyBytes_AsDouble_inf_nan` **(Compute Cores)** (Impact: 66.1)
  * `__Pyx_dict_iter_next` **(Many-Argument Workhorses)** (Impact: 65.2)
    * *Intent:* #endif
  * `__Pyx__PyUnicode_AsDouble_inf_nan` **(Many-Argument Workhorses)** (Impact: 65.2)
  * `__Pyx__PyNumber_PowerOf2` **(Many-Argument Workhorses)** (Impact: 44.6)
    * *Intent:* /////////////// PyNumberPow2.proto /////////////// #define __Pyx_PyNumber_InPlacePowerOf2(a, b, c) _...
  * `__Pyx_dict_iterator` **(Stateful Encapsulated Methods)** (Impact: 41.5)
    * *Intent:* /////////////// dict_iter /////////////// //@requires: ObjectHandling.c::UnpackTuple2 //@requires: O...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 216 instances
* *State Mutation (weighted view):* 673
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 852`, `structural_boundaries: 228`, `args: 159`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 241`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `safety: 16`, `doc: 46`, `immutability_locks: 35`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.228
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.002981
  * `Imports (Out-Degree: 3):` string.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Cython/Utility/MemoryView.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.482)
- **Top Global Matches:** file_cluster_12: 6.482, file_cluster_15: 6.81, file_cluster_16: 8.507
- **Magnitude:** 1233.38 | **LOC:** 1492 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 42.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.42; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.5%), Complexity Load (formerly Cognitive Load) (68.9%)
- **Documentation Coverage:** 94.4954% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__cinit__` **(Stateful Encapsulated Methods)** (Impact: 42.2)
  * `memoryview_copy_contents` **(Many-Argument Workhorses)** (Impact: 40.2)
  * `_copy_strided_to_strided` **(Many-Argument Workhorses)** (Impact: 28.4)
  * `__cinit__` **(Many-Argument Workhorses)** (Impact: 28.2)
  * `memview_slice` **(Many-Argument Workhorses)** (Impact: 24.5)
    * *Intent:* # ### Slicing a memoryview #
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 176 instances
* *State Mutation (weighted view):* 554
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 158`, `args: 85`, `func_start: 84`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 202`, `fragile_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 20`, `import: 4`
* *Defense:* `safety: 31`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, collections.abc, struct
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/run/test_exceptions.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.462)
- **Top Global Matches:** file_cluster_12: 8.462, file_cluster_7: 9.125, file_cluster_5: 10.365
- **Magnitude:** 1099.2 | **LOC:** 2469 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.42; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (62.7%), Complexity Load (formerly Cognitive Load) (21.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (15.6%), Connectivity (formerly Api Exposure) (13.0%)
- **Documentation Coverage:** 99.3671% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testSyntaxErrorOffset` **(Compute Cores)** (Impact: 30.4)
  * `check` **(Many-Argument Workhorses)** (Impact: 14.9)
  * `testExceptionCleanupState` **(Defensive Guards)** (Impact: 13.1)
    * *Intent:* #with self.assertRaises(UnboundLocalError): # e # Make sure exception state is cleaned up as soon as...
  * `testAttributes` **(I/O & Config Routines)** (Impact: 12.1)
    * *Intent:* # test that exception attributes are happy exceptionList = [ (BaseException, (), {}, {'args' : ()}),...
  * `lineno_after_raise` **(Defensive Guards)** (Impact: 10.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Cascading Flux:* 69 instances
* *High Risk Execution (weighted view):* 8
* *State Mutation (weighted view):* 412
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 498`, `args: 176`, `func_start: 163`, `class_start: 47`
* *Risk/State:* `safety_bypasses: 109`, `high_risk_execution: 14`, `state_mutation: 274`, `dead_code: 1`, `fragile_debt: 3`, `duplicate_logic: 7`, `unreferenced_by_name: 95`
* *Architecture:* `io: 28`, `api: 166`, `import: 24`
* *Defense:* `safety: 213`, `doc: 36`, `test: 113`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Cython.TestUtils, _, __future__, _testcapi, copy, division, errno, marshal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Cython/Utility/Coroutine.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.122)
- **Top Global Matches:** file_cluster_4: 9.122, file_cluster_12: 11.184, file_cluster_7: 12.077
- **Magnitude:** 1095.78 | **LOC:** 2304 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.504; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.6%)
- **Documentation Coverage:** 94.1176% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__Pyx__Coroutine_Throw` **(Many-Argument Workhorses)** (Impact: 48.9)
  * `__Pyx_Coroutine_AmSend` **(Many-Argument Workhorses)** (Impact: 47.0)
  * `__Pyx_PyGen__FetchStopIterationValue` **(Many-Argument Workhorses)** (Impact: 39.8)
    * *Intent:* // If StopIteration exception is set, fetches its 'value' // attribute if any, otherwise sets pvalue...
  * `__Pyx_Coroutine_Close` **(Compute Cores)** (Impact: 34.1)
  * `__Pyx__Coroutine_GetAwaitableIter` **(Compute Cores)** (Impact: 32.3)
    * *Intent:* // adapted from genobject.c in Py3.5
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 114 instances
* *State Mutation (weighted view):* 390
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 268`, `structural_boundaries: 212`, `args: 182`, `func_start: 73`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 82`, `state_mutation: 162`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 2`
* *Architecture:* `io: 3`, `api: 8`, `import: 2`
* *Defense:* `safety: 15`, `doc: 39`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000497
  * `Imports (Out-Degree: 6):` frameobject.h, pycore_frame.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Cython/Compiler/Main.py` (PYTHON | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.19)
- **Top Global Matches:** file_cluster_4: 7.19, file_cluster_12: 7.798, file_cluster_15: 9.369
- **Magnitude:** 1081.18 | **LOC:** 857 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **21**; blast radius 1.881; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.2%)
- **Documentation Coverage:** 90.5882% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `find_module` **(Many-Argument Workhorses)** (Impact: 100.7)
  * `search_include_directories` **(Many-Argument Workhorses)** (Impact: 50.4)
    * *Intent:* """ Search the list of include directories for the given file name. If a source file path or positio...
  * `run_pipeline` **(Many-Argument Workhorses)** (Impact: 33.5)
  * `compile` **(Many-Argument Workhorses)** (Impact: 23.9)
    * *Intent:* """ compile(source [, options], [, <option> = <value>]...) Compile one or more Pyrex implementation ...
  * `compile_multiple` **(Many-Argument Workhorses)** (Impact: 23.8)
    * *Intent:* """ compile_multiple(sources, options, cache) Compiles the given sequence of Pyrex implementation fi...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 154 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 505
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 178`, `args: 46`, `func_start: 46`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 3`, `state_mutation: 197`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `io: 54`, `api: 43`, `import: 25`
* *Defense:* `safety: 18`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.881
  * `Choke Point (Betweenness):` 0.000268 | `Ripple Effect (Closeness):` 0.015945
  * `Imports (Out-Degree: 15):` ..Build.Cache, ..Build.Dependencies, ..Build.SharedModule, ..Parser, ..Utils, .Builtin, .CmdLine, .CythonScope...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/run/ext_type_none_arg.pyx` (PYTHON) | Magnitude: 104.78 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 75, indent_spaces: 38, args: 32, func_start: 32
- `Tools/cython-epydoc.py` (PYTHON) | Magnitude: 0.02 | Delta: **0.145** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 11, state_mutation: 9, core_var_decl: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `tests/run/methodmangling_cdef.pyx` (PYTHON) | Magnitude: 36.66 | Delta: **0.13** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 26, args: 15, func_start: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/run/builtin_float.py` (PYTHON) | Magnitude: 41.28 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 26, explicit_casts: 21, args: 12
- `tests/run/exttype_freelist.pyx` (PYTHON) | Magnitude: 43.04 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 34, state_mutation: 15, args: 14
- `tests/errors/pep492_badsyntax_async4.pyx` (PYTHON) | Magnitude: 8.26 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 3, concurrency: 3, args: 2, func_start: 2
- `tests/run/locals_T732.pyx` (PYTHON) | Magnitude: 20.76 | Delta: **0.121** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, state_mutation: 10, core_var_decl: 10, debug_prints: 9
- `tests/run/generator_expressions_nested.pyx` (PYTHON) | Magnitude: 45.32 | Delta: **0.172** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: branch: 26, structural_boundaries: 16, doc: 9, args: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/run/cyfunction.pyx` (PYTHON) | Magnitude: 122.98 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 75, indent_spaces: 58, api: 41, args: 39
- `tests/run/for_in_string.pyx` (PYTHON) | Magnitude: 114.96 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 66, branch: 30, structural_boundaries: 28, decorators: 18
- `tests/memoryview/view_return_errors.pyx` (PYTHON) | Magnitude: 9.9 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 22, branch: 11, panics_and_aborts: 8, structural_boundaries: 2
- `tests/run/bytearray_coercion.pyx` (PYTHON) | Magnitude: 75.64 | Delta: **0.112** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 32, state_mutation: 22, core_var_decl: 14
- `tests/run/cdef_multiple_inheritance.pyx` (PYTHON) | Magnitude: 18.1 | Delta: **0.112** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 18, args: 9, func_start: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/run/builtin_min_max.pyx` (PYTHON) | Magnitude: 51.94 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 72, decorators: 28, structural_boundaries: 27, core_var_decl: 18
- `tests/run/builtin_subtype_methods_T653.pyx` (PYTHON) | Magnitude: 110.28 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 44, args: 18, func_start: 18
- `tests/run/hasattr.py` (PYTHON) | Magnitude: 13.76 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 8, api: 5, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `tests/errors/e_typing_optional.py` (PYTHON) | Magnitude: 14.72 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 12, generics: 12, indent_spaces: 7, safety_bypasses: 5
- `tests/run/richcmp_str_equals.py` (PYTHON) | Magnitude: 11.12 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 8, args: 4, func_start: 4
- `tests/compile/cython_compiled_folding.py` (PYTHON) | Magnitude: 6.96 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 22, indent_spaces: 13, branch: 11, import: 8
- `Cython/Includes/cpython/datetime.pxd` (PYTHON) | Magnitude: 128.06 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 177, structural_boundaries: 64, args: 52, func_start: 52
- `tests/errors/e_autotestdict.pyx` (PYTHON) | Magnitude: 3.2 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, safety_bypasses: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tests/buffers/buffmt.pyx` (PYTHON) | Magnitude: 106.44 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 142, core_var_decl: 35, design_snake_case: 35, structural_boundaries: 29
- `tests/run/builtin_basestring.pyx` (PYTHON) | Magnitude: 36.98 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 15, state_mutation: 8, core_var_decl: 8
- `tests/run/addop.pyx` (PYTHON) | Magnitude: 39.02 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 17, args: 9, func_start: 9
- `tests/run/unicode_slicing.pyx` (PYTHON) | Magnitude: 32.58 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 8, args: 7, func_start: 7
- `tests/errors/e_assert.pyx` (PYTHON) | Magnitude: 4.62 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 9, safety: 8, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `Demos/benchmarks/bm_fused_types.py` (PYTHON) | Magnitude: 104.0 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 69, state_mutation: 23, core_var_decl: 23, design_snake_case: 23
- `Cython/Compiler/Future.py` (PYTHON) | Magnitude: 10.86 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: state_mutation: 9, core_var_decl: 9, design_snake_case: 9, structural_boundaries: 4
- `Cython/Utility/__init__.py` (PYTHON) | Magnitude: 23.8 | Delta: **0.138** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 8, branch: 6, structural_boundaries: 6, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/errors/pep492_badsyntax_async5.pyx` (PYTHON) | Magnitude: 4.16 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, api: 1
- `tests/run/str_subclass_kwargs.pyx` (PYTHON) | Magnitude: 3.54 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, api: 1
- `Cython/Compiler/Naming.py` (PYTHON) | Magnitude: 165.94 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 165, core_var_decl: 153, design_snake_case: 153, state_mutation: 150
- `tests/run/time_pxd.pyx` (PYTHON) | Magnitude: 96.62 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 35, core_var_decl: 24, state_mutation: 23, design_snake_case: 23
- `tests/run/posix_time.pyx` (PYTHON) | Magnitude: 18.62 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 18, state_mutation: 12, structural_boundaries: 7, core_var_decl: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `Cython/Utility/CommonStructures.c` (C) | Magnitude: 130.18 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 128, pointers: 51, branch: 30, structural_boundaries: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `tests/errors/e_typing_errors.pyx` (PYTHON) | Magnitude: 30.94 | Delta: **0.207** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: generics: 26, structural_boundaries: 22, indent_spaces: 21, safety_bypasses: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/run/r_hordijk1.pyx` (PYTHON) | Magnitude: 1.62 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 4, args: 1, func_start: 1
- `Cython/Compiler/Tests/TestTreeFragment.py` (PYTHON) | Magnitude: 51.8 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 42, state_mutation: 21, core_var_decl: 19, design_short_vars: 18
- `Cython/Utility/MemoryView.pxd` (PYTHON) | Magnitude: 48.08 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 55, args: 17, func_start: 16, api: 15
- `tests/run/set_iter.pyx` (PYTHON) | Magnitude: 39.58 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 12, decorators: 7, branch: 6
- `tests/run/pycmp.pyx` (PYTHON) | Magnitude: 17.1 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 23, state_mutation: 13, core_var_decl: 13, design_snake_case: 13

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Cython/Compiler/ExprNodes.py` -> Churn: **97.66%** | Cog Load: 91.4423% | Debt: 98.776%
- `runtests.py` -> Churn: **83.51%** | Cog Load: 92.6195% | Debt: 10.1057%
- `Cython/Compiler/Code.py` -> Churn: **82.96%** | Cog Load: 75.6966% | Debt: 14.7079%
- `Cython/Compiler/ModuleNode.py` -> Churn: **78.46%** | Cog Load: 76.195% | Debt: 10.6989%
- `Cython/Compiler/Nodes.py` -> Churn: **70.32%** | Cog Load: 90.1236% | Debt: 76.8927%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/run/extsubscript.py` -> **scoder** (100.0% isolated ownership) | Magnitude: 2910.9
- `tests/run/test_asyncgen.py` -> **Stefan Behnel** (100.0% isolated ownership) | Magnitude: 1921.64
- `Cython/Compiler/FlowControl.py` -> **da-woods** (100.0% isolated ownership) | Magnitude: 1780.54
- `tests/run/test_grammar.py` -> **Stefan Behnel** (100.0% isolated ownership) | Magnitude: 1514.56
- `Cython/Tempita/_tempita.py` -> **Stefan Behnel** (100.0% isolated ownership) | Magnitude: 1503.3

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Cython/TestUtils.py` -> **Severity: 0.059** (Bridge: 0.0006 * Flux: 100.0%)
- `Cython/Compiler/TreeFragment.py` -> **Severity: 0.035** (Bridge: 0.0003 * Flux: 100.0%)
- `Cython/Compiler/ParseTreeTransforms.py` -> **Severity: 0.03** (Bridge: 0.0003 * Flux: 100.0%)
- `Cython/Compiler/Main.py` -> **Severity: 0.027** (Bridge: 0.0003 * Flux: 100.0%)
- `Cython/Compiler/Code.py` -> **Severity: 0.023** (Bridge: 0.0002 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Cython/Compiler/Errors.py` -> **Severity: 1.845** (Embedded: 0.0241 * Error Risk: 76.5315%)
- `Cython/Compiler/TreeFragment.py` -> **Severity: 1.758** (Embedded: 0.0203 * Error Risk: 86.7634%)
- `Cython/Compiler/ParseTreeTransforms.py` -> **Severity: 1.757** (Embedded: 0.0218 * Error Risk: 80.7066%)
- `Cython/Compiler/Symtab.py` -> **Severity: 1.677** (Embedded: 0.0193 * Error Risk: 86.8231%)
- `Cython/Compiler/Options.py` -> **Severity: 1.655** (Embedded: 0.0234 * Error Risk: 70.721%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Cython/Shadow.py` -> **Severity: 925.019** (Blast Radius: 9.562 * Doc Risk: 96.7391%)
- `Cython/TestUtils.py` -> **Severity: 751.058** (Blast Radius: 9.12 * Doc Risk: 82.3529%)
- `Cython/Compiler/Visitor.py` -> **Severity: 585.9** (Blast Radius: 6.076 * Doc Risk: 96.4286%)
- `Cython/Compiler/Errors.py` -> **Severity: 581.2** (Blast Radius: 5.812 * Doc Risk: 100.0%)
- `Cython/Compiler/PyrexTypes.py` -> **Severity: 423.901** (Blast Radius: 4.564 * Doc Risk: 92.8793%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1237 literal sites + 1302 sites through wrappers = 2539
- **`panics_and_aborts`:** 1370 literal sites + 110 sites through wrappers = 1480

- `_print_delitem_Map` (function, debug_prints, primitive): 180 call sites in 1 files -- `tests/run/extsubscript.py`
- `_print_delitem_Seq` (function, debug_prints, primitive): 180 call sites in 1 files -- `tests/run/extsubscript.py`
- `_print_getitem_Map` (function, debug_prints, primitive): 180 call sites in 1 files -- `tests/run/extsubscript.py`
- `_print_getitem_Seq` (function, debug_prints, primitive): 180 call sites in 1 files -- `tests/run/extsubscript.py`
- `_print_setitem_Map` (function, debug_prints, primitive): 180 call sites in 1 files -- `tests/run/extsubscript.py`
- `_print_setitem_Seq` (function, debug_prints, primitive): 180 call sites in 1 files -- `tests/run/extsubscript.py`
- `reversed` (function, debug_prints, primitive): 142 call sites in 19 files -- `tests/run/cpp_iterators.pyx`
- `f` (function, debug_prints, primitive): 33 call sites in 1 files -- `tests/run/pep448_test_extcall.pyx`
- `eval` (function, panics_and_aborts, primitive): 28 call sites in 13 files -- `tests/run/test_grammar.py`
- `g` (function, debug_prints, primitive): 13 call sites in 1 files -- `tests/run/pep448_test_extcall.pyx`
- `inner_raising_func` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `tests/run/test_exceptions.pyx`
- `_checkeval` (function, debug_prints, primitive): 7 call sites in 1 files -- `tests/run/test_grammar.py`
*(+67 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 41937 call pairs -- scoped 37.5%, unique 0.3%, ambiguous 24.8%, external 37.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 38204 | 39.8% | 0.0% | 27.2% | 33.0% |
| c | 3504 | 12.0% | 3.6% | 0.0% | 84.4% |
| cpp | 103 | 32.0% | 1.0% | 0.0% | 67.0% |
| javascript | 99 | 48.5% | 0.0% | 0.0% | 51.5% |
| shell | 27 | 0.0% | 0.0% | 0.0% | 100.0% |

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
