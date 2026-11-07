# ARCHITECTURAL_BRIEF: micropython-ulab
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/v923z/micropython-ulab` |
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
- **Scope:** 191 analyzed artifact(s), 19252 LOC.
- **Load-bearing artifact:** `snippets/numpy/__init__.py` -- 73 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `code/numpy/numpy.c` -- pulls in 19 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `code/ndarray.c` at magnitude 2373.32 (structural weight, not risk).
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
| Total Artifacts | 333 |
| Analyzed Artifacts (Scanned) | 191 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 142 |
| Total LOC | 19252 |
| Volatility Index | 0.042 |
| % Scanned of codebase = | 57.4% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5256 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5901 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3575 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 112 | 3350 | 58.6% |
| C | 66 | 15647 | 34.6% |
| MARKDOWN | 4 | 0 | 2.1% |
| SHELL | 4 | 132 | 2.1% |
| PLAINTEXT | 3 | 0 | 1.6% |
| YAML | 1 | 87 | 0.5% |
| MAKEFILE | 1 | 36 | 0.5% |

## 4.1 SOURCE ENCODINGS
All 191 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 58%, Data / Markup / Trivial 17%, Many-Argument Workhorses Files 9%, Large Core Modules (2) 5%, Compute Cores Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 184 | 96.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 7 | 3.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 142*

**Composition by Extension & Reason:**
- `.exp`: 92x Excluded (Unsupported Extension: '.exp'), 1x Unsupported Format (.exp)
- `.ipynb`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tpl`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bat`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 96.2 | 20.1 | 7.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.0 | 49.6 | 55.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 4.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 9.6 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 6.7 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 95.8 | 0.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 27.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 6.0 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 24.8 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 64 | 17 | 0 | `snippets/scipy/signal/filter_design.py` |
| cleanup | 6 | 4 | 0 | `run-tests` |
| guards | 1586 | 140 | 21 | `code/ndarray.c` |
| danger | 532 | 100 | 6 | `code/numpy/carray/carray.c` |
| concurrency | 12 | 4 | 0 | `run-tests` |
| connectivity | 385 | 66 | 4 | `code/ndarray.h` |
| io | 91 | 10 | 0 | `run-tests` |
| crypto | 0 | 0 | 0 | - |
| ipc | 15 | 1 | 0 | `run-tests` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 2 | 1 | 0 | `run-tests` |
| events | 4 | 1 | 0 | `run-tests` |
| tests | 2 | 1 | 0 | `tests/1d/numpy/universal_functions.py` |
| docs | 23 | 9 | 0 | `snippets/scipy/signal/filter_design.py` |
| debt | 888 | 113 | 10 | `tests/2d/numpy/numericals.py` |
| mutation | 7081 | 148 | 110 | `code/ndarray.c` |
| dead_code | 81 | 18 | 0 | `code/ndarray.c` |
| credential | 0 | 0 | 0 | - |
| threat | 1 | 1 | 0 | `code/numpy/io/io.c` |
| ml_ai | 315 | 140 | 2 | `code/numpy/vector.c` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `run-tests` (Hits: 26)
- `build-cp.sh` (Hits: 19)
- `build.sh` (Hits: 17)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`snippets/numpy/__init__.py`) — 73 inbound connections
2. **ulab.h** (`code/ulab.h`) — 43 inbound connections
3. **ndarray.h** (`code/ndarray.h`) — 34 inbound connections
4. **ndarray.c** (`code/ndarray.c`) — 23 inbound connections
5. **ulab_tools.h** (`code/ulab_tools.h`) — 23 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **numpy.c** (`code/numpy/numpy.c`) — 19 outbound dependencies
2. **ulab.c** (`code/ulab.c`) — 18 outbound dependencies
3. **ndarray.c** (`code/ndarray.c`) — 15 outbound dependencies
4. **transform.c** (`code/numpy/transform.c`) — 13 outbound dependencies
5. **run-tests** (`run-tests`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ndarray_binary_more` **(Many-Argument Workhorses)** (@ `code/ndarray_operators.c`) -> Impact: **321.1** | LOC: 142
  * *Intent:* #endif /* NDARRAY_HAS_BINARY_OP_MULTIPLY */ #if NDARRAY_HAS_BINARY_OP_MORE | NDARRAY_HAS_BINARY_OP_MORE_EQUAL | NDARRAY_HAS_BINARY_OP_LESS | NDARRAY_H...
- `ndarray_binary_logical` **(Many-Argument Workhorses)** (@ `code/ndarray_operators.c`) -> Impact: **283.6** | LOC: 184
  * *Intent:* #endif /* NDARRAY_HAS_BINARY_OP_POWER */ #if NDARRAY_HAS_BINARY_OP_OR | NDARRAY_HAS_BINARY_OP_XOR | NDARRAY_HAS_BINARY_OP_AND
- `ndarray_binary_equality` **(Many-Argument Workhorses)** (@ `code/ndarray_operators.c`) -> Impact: **235.4** | LOC: 125
  * *Intent:* */ #if NDARRAY_HAS_BINARY_OP_EQUAL | NDARRAY_HAS_BINARY_OP_NOT_EQUAL
- `ndarray_unary_op` **(Many-Argument Workhorses)** (@ `code/ndarray.c`) -> Impact: **180.1** | LOC: 346
  * *Intent:* #endif /* NDARRAY_HAS_BINARY_OPS || NDARRAY_HAS_INPLACE_OPS */ #if NDARRAY_HAS_UNARY_OPS
- `ndarray_binary_op` **(Many-Argument Workhorses)** (@ `code/ndarray.c`) -> Impact: **170.9** | LOC: 218
  * *Intent:* #if NDARRAY_HAS_BINARY_OPS || NDARRAY_HAS_INPLACE_OPS
- `run_tests` **(Many-Argument Workhorses)** (@ `run-tests`) -> Impact: **159.4** | LOC: 248
- `ndarray_binary_subtract` **(Many-Argument Workhorses)** (@ `code/ndarray_operators.c`) -> Impact: **155.9** | LOC: 102
  * *Intent:* #endif /* NDARRAY_HAS_BINARY_OP_MORE | NDARRAY_HAS_BINARY_OP_MORE_EQUAL | NDARRAY_HAS_BINARY_OP_LESS | NDARRAY_HAS_BINARY_OP_LESS_EQUAL */ #if NDARRAY...
- `ndarray_binary_true_divide` **(Many-Argument Workhorses)** (@ `code/ndarray_operators.c`) -> Impact: **155.3** | LOC: 89
  * *Intent:* #endif /* NDARRAY_HAS_BINARY_OP_SUBTRACT */ #if NDARRAY_HAS_BINARY_OP_TRUE_DIVIDE
- `ndarray_binary_modulo` **(Many-Argument Workhorses)** (@ `code/ndarray_operators.c`) -> Impact: **150.3** | LOC: 96
  * *Intent:* #endif /* NDARRAY_HAS_BINARY_OP_ADD */ #if NDARRAY_HAS_BINARY_OP_MODULO
- `ndarray_binary_floor_divide` **(Many-Argument Workhorses)** (@ `code/ndarray_operators.c`) -> Impact: **150.2** | LOC: 93
  * *Intent:* #endif /* NDARRAY_HAS_BINARY_OP_TRUE_DIVIDE */ #if NDARRAY_HAS_BINARY_OP_FLOOR_DIVIDE

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `code/numpy` | 22 | 5656.94 | 28.22% | 2.68% |
| `code` | 12 | 5541.54 | 27.16% | 15.93% |
| `tests/2d/numpy` | 46 | 1250.62 | 10.46% | 0.0% |
| `snippets/scipy/signal` | 2 | 1080.36 | 25.52% | 5.49% |
| `code/numpy/carray` | 4 | 1042.04 | 18.58% | 13.59% |
| `__monolith__` | 9 | 948.72 | 33.18% | 1.28% |
| `code/numpy/io` | 2 | 819.8 | 36.9% | 0.0% |
| `code/numpy/linalg` | 4 | 763.4 | 35.08% | 10.62% |
| `code/scipy/integrate` | 2 | 662.26 | 32.67% | 0.0% |
| `tests/1d/numpy` | 14 | 438.96 | 12.43% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/workflows/build.yml` -> **99.9876%** Exposure
- `code/ulab_tools.c` -> **99.5405%** Exposure
- `snippets/numpy/core/fromnumeric.py` -> **97.0688%** Exposure
- `code/numpy/ndarray/ndarray_iter.c` -> **81.7574%** Exposure
- `snippets/rclass.py` -> **79.35%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `build-cp.sh` -> **100.0%** Exposure
- `build.sh` -> **100.0%** Exposure
- `code/micropython.mk` -> **100.0%** Exposure
- `code/ndarray.c` -> **100.0%** Exposure
- `code/numpy/approx.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `code/ndarray.c` -> **22** Orphaned Functions | **0** Duplicates
- `code/ndarray_operators.c` -> **14** Orphaned Functions | **0** Duplicates
- `code/ulab_tools.c` -> **12** Orphaned Functions | **0** Duplicates
- `code/numpy/carray/carray.c` -> **6** Orphaned Functions | **0** Duplicates
- `.github/workflows/build.yml` -> **0** Orphaned Functions | **4** Duplicates

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
- **Unknown Dependencies:** `541` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `code/ndarray.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.137)
- **Top Global Matches:** file_cluster_6: 7.137, file_cluster_4: 8.942, file_cluster_12: 16.019
- **Magnitude:** 2373.32 | **LOC:** 2118 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **15**; blast radius 12.932; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ndarray_unary_op` **(Many-Argument Workhorses)** (Impact: 180.1)
    * *Intent:* #endif /* NDARRAY_HAS_BINARY_OPS || NDARRAY_HAS_INPLACE_OPS */ #if NDARRAY_HAS_UNARY_OPS
  * `ndarray_binary_op` **(Many-Argument Workhorses)** (Impact: 170.9)
    * *Intent:* #if NDARRAY_HAS_BINARY_OPS || NDARRAY_HAS_INPLACE_OPS
  * `ndarray_assign_from_boolean_index` **(Many-Argument Workhorses)** (Impact: 133.6)
  * `ndarray_dtype_make_new` **(Many-Argument Workhorses)** (Impact: 54.1)
  * `ndarray_print` **(Many-Argument Workhorses)** (Impact: 50.2)
    * *Intent:* #endif
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 309 instances
* *State Mutation (weighted view):* 961
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 516`, `structural_boundaries: 188`, `args: 186`, `func_start: 70`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 343`, `dead_code: 6`, `planned_debt: 7`, `unreferenced_by_name: 22`
* *Architecture:* `api: 57`, `import: 15`
* *Defense:* `safety: 105`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.932
  * `Choke Point (Betweenness):` 0.003286 | `Ripple Effect (Closeness):` 0.121832
  * `Imports (Out-Degree: 8):` math.h, ndarray.h, ndarray_operators.h, carray.h, carray_tools.h, binary.h, obj.h, objint.h...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `code/ndarray_operators.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 20.727)
- **Top Global Matches:** file_cluster_3: 20.727, file_cluster_1: 29.196, file_cluster_8: 41.962
- **Magnitude:** 2353.18 | **LOC:** 1246 | **CtrlFlow:** 59.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 3.59; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ndarray_binary_more` **(Many-Argument Workhorses)** (Impact: 321.1)
    * *Intent:* #endif /* NDARRAY_HAS_BINARY_OP_MULTIPLY */ #if NDARRAY_HAS_BINARY_OP_MORE | NDARRAY_HAS_BINARY_OP_M...
  * `ndarray_binary_logical` **(Many-Argument Workhorses)** (Impact: 283.6)
    * *Intent:* #endif /* NDARRAY_HAS_BINARY_OP_POWER */ #if NDARRAY_HAS_BINARY_OP_OR | NDARRAY_HAS_BINARY_OP_XOR | ...
  * `ndarray_binary_equality` **(Many-Argument Workhorses)** (Impact: 235.4)
    * *Intent:* */ #if NDARRAY_HAS_BINARY_OP_EQUAL | NDARRAY_HAS_BINARY_OP_NOT_EQUAL
  * `ndarray_binary_subtract` **(Many-Argument Workhorses)** (Impact: 155.9)
    * *Intent:* #endif /* NDARRAY_HAS_BINARY_OP_MORE | NDARRAY_HAS_BINARY_OP_MORE_EQUAL | NDARRAY_HAS_BINARY_OP_LESS...
  * `ndarray_binary_true_divide` **(Many-Argument Workhorses)** (Impact: 155.3)
    * *Intent:* #endif /* NDARRAY_HAS_BINARY_OP_SUBTRACT */ #if NDARRAY_HAS_BINARY_OP_TRUE_DIVIDE
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 134 instances
* *State Mutation (weighted view):* 404
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 676`, `structural_boundaries: 57`, `args: 40`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 136`, `unreferenced_by_name: 14`
* *Architecture:* `api: 14`, `import: 8`
* *Defense:* `safety: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.59
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.065789
  * `Imports (Out-Degree: 8):` math.h, ndarray.h, ndarray_operators.h, carray.h, objtuple.h, runtime.h, ulab.h, ulab_tools.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `code/numpy/numerical.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.92)
- **Top Global Matches:** file_cluster_8: 8.92, file_cluster_3: 17.854, file_cluster_6: 19.984
- **Magnitude:** 1457.5 | **LOC:** 1430 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 2.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.2%), Guard Balance (formerly Safety Score) (72.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `numerical_sum_mean_std_ndarray` **(Many-Argument Workhorses)** (Impact: 111.7)
  * `numerical_all_any` **(Many-Argument Workhorses)** (Impact: 105.6)
    * *Intent:* #if ULAB_NUMPY_HAS_ALL | ULAB_NUMPY_HAS_ANY
  * `numerical_cross` **(Compute Cores)** (Impact: 83.1)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_CROSS //| def cross(a: ulab.numpy.ndarray, b: ulab.numpy.ndarray) -> ulab....
  * `numerical_argmin_argmax_ndarray` **(Many-Argument Workhorses)** (Impact: 79.4)
  * `numerical_roll` **(Many-Argument Workhorses)** (Impact: 68.0)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_ROLL //| def roll(array: ulab.numpy.ndarray, distance: int, *, axis: Optio...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 204 instances
* *State Mutation (weighted view):* 638
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 327`, `structural_boundaries: 75`, `args: 100`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 230`, `planned_debt: 2`
* *Architecture:* `api: 15`, `import: 12`
* *Defense:* `safety: 75`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` ulab.h, ulab_tools.h, carray_tools.h, math.h, numerical.h, builtin.h, misc.h, obj.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/create.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.227)
- **Top Global Matches:** file_cluster_3: 7.227, file_cluster_8: 24.091, file_cluster_6: 36.94
- **Magnitude:** 1111.08 | **LOC:** 1217 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 2.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_take` **(Many-Argument Workhorses)** (Impact: 99.5)
  * `create_meshgrid` **(Many-Argument Workhorses)** (Impact: 66.0)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_MESHGRID //| def meshgrid(*xi, indexing="xy"): //| """ //| .. param: xi //...
  * `create_concatenate` **(Many-Argument Workhorses)** (Impact: 55.7)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_CONCATENATE //| def concatenate(arrays: Tuple[ulab.numpy.ndarray], *, axis...
  * `create_arange` **(Many-Argument Workhorses)** (Impact: 48.8)
    * *Intent:* //| """ //| .. param: start //| First value in the array, optional, defaults to 0 //| .. param: stop...
  * `create_logspace` **(Many-Argument Workhorses)** (Impact: 40.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 180 instances
* *State Mutation (weighted view):* 550
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 224`, `structural_boundaries: 31`, `args: 66`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 190`, `planned_debt: 2`
* *Architecture:* `api: 14`, `import: 9`
* *Defense:* `safety: 94`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ulab.h, ulab_tools.h, create.h, math.h, obj.h, runtime.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `snippets/scipy/signal/filter_design.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.197)
- **Top Global Matches:** file_cluster_6: 7.197, file_cluster_4: 8.897, file_cluster_12: 15.436
- **Magnitude:** 1069.84 | **LOC:** 1480 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 10.687; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (51.0%)
- **Documentation Coverage:** 63.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `iirfilter` **(Many-Argument Workhorses)** (Impact: 124.5)
  * `zpk2sos` **(Many-Argument Workhorses)** (Impact: 77.0)
    * *Intent:* """ Return second-order sections from zeros, poles, and gain of a system Parameters ---------- z : a...
  * `buttord` **(Many-Argument Workhorses)** (Impact: 61.5)
    * *Intent:* """Butterworth filter order selection. Return the order of the lowest order digital or analog Butter...
  * `zpk2tf` **(Many-Argument Workhorses)** (Impact: 28.9)
    * *Intent:* """ Return polynomial transfer function representation from zeros and poles Parameters ---------- z ...
  * `_cplxreal` **(Many-Argument Workhorses)** (Impact: 22.5)
    * *Intent:* """ Split into complex and real parts, combining conjugate pairs. The 1-D input vector `z` is split ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 194 instances
* *State Mutation (weighted view):* 626
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 81`, `args: 23`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 238`, `planned_debt: 4`
* *Architecture:* `api: 15`, `import: 5`
* *Defense:* `safety: 17`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.687
  * `Choke Point (Betweenness):` 0.001337 | `Ripple Effect (Closeness):` 0.017763
  * `Imports (Out-Degree: 8):` ...numpy, math, ulab
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `code/numpy/carray/carray.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.639)
- **Top Global Matches:** file_cluster_8: 10.639, file_cluster_6: 15.595, file_cluster_4: 23.562
- **Magnitude:** 975.46 | **LOC:** 835 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **12**; blast radius 4.001; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `carray_binary_subtract` **(Many-Argument Workhorses)** (Impact: 92.4)
  * `carray_binary_equal_not_equal` **(Many-Argument Workhorses)** (Impact: 75.6)
  * `carray_binary_add` **(Many-Argument Workhorses)** (Impact: 68.6)
  * `carray_binary_divide` **(Many-Argument Workhorses)** (Impact: 65.6)
  * `carray_binary_multiply` **(Many-Argument Workhorses)** (Impact: 38.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 132 instances
* *State Mutation (weighted view):* 448
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 23`, `args: 19`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 184`, `unreferenced_by_name: 6`
* *Architecture:* `api: 10`, `import: 12`
* *Defense:* `safety: 37`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.001
  * `Choke Point (Betweenness):` 4e-05 | `Ripple Effect (Closeness):` 0.067132
  * `Imports (Out-Degree: 6):` ndarray.h, ulab.h, ulab_tools.h, carray.h, math.h, builtin.h, misc.h, obj.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `code/numpy/io/io.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.237)
- **Top Global Matches:** file_cluster_3: 6.237, file_cluster_8: 20.506, file_cluster_6: 33.424
- **Magnitude:** 806.16 | **LOC:** 807 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 2.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.4%), Complexity Load (formerly Cognitive Load) (73.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `io_loadtxt` **(Many-Argument Workhorses)** (Impact: 146.1)
  * `io_load` **(Many-Argument Workhorses)** (Impact: 79.9)
  * `io_savetxt` **(Many-Argument Workhorses)** (Impact: 54.0)
  * `io_save` **(Many-Argument Workhorses)** (Impact: 34.7)
  * `io_format_float` **(Many-Argument Workhorses)** (Impact: 16.8)
    * *Intent:* #endif /* ULAB_NUMPY_HAS_SAVE */ #if ULAB_NUMPY_HAS_SAVETXT
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 139 instances
* *State Mutation (weighted view):* 428
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 33`, `args: 44`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 150`
* *Architecture:* `io: 16`, `import: 12`
* *Defense:* `safety: 27`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ndarray.h, ulab_tools.h, vfs.h, io.h, math.h, builtin.h, formatfloat.h, obj.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run-tests` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.544)
- **Top Global Matches:** file_cluster_8: 7.544, file_cluster_6: 11.24, file_cluster_4: 19.555
- **Magnitude:** 766.62 | **LOC:** 571 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 2.003; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.2%), Concurrency Surface (formerly Concurrency) (95.8%), Guard Balance (formerly Safety Score) (81.7%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_tests` **(Many-Argument Workhorses)** (Impact: 159.4)
  * `run_micropython` **(Many-Argument Workhorses)** (Impact: 103.8)
  * `run_one_test` **(Compute Cores)** (Impact: 47.6)
  * `main` **(I/O & Config Routines)** (Impact: 31.1)
  * `convert_regex_escapes` **(Type Conversions)** (Impact: 10.7)
    * *Intent:* # unescape wanted regex chars and escape unwanted ones
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 103 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 325
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 79`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 4`, `state_mutation: 119`, `unreferenced_by_name: 2`
* *Architecture:* `io: 26`, `api: 14`, `concurrency: 6`, `import: 14`
* *Defense:* `safety: 9`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` argparse, glob, multiprocessing, multiprocessing.pool, os, platform, pty, pyboard...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/compare.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.395)
- **Top Global Matches:** file_cluster_8: 11.395, file_cluster_3: 16.351, file_cluster_6: 22.583
- **Magnitude:** 663.64 | **LOC:** 774 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 2.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.4%), Guard Balance (formerly Safety Score) (74.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compare_function` **(Many-Argument Workhorses)** (Impact: 127.0)
    * *Intent:* #endif /* ULAB_NUMPY_HAS_BINCOUNT */
  * `compare_bincount` **(Many-Argument Workhorses)** (Impact: 74.2)
    * *Intent:* #include <math.h> #include <stdlib.h> #include <string.h> #include "py/obj.h" #include "py/runtime.h...
  * `compare_where` **(Many-Argument Workhorses)** (Impact: 41.5)
    * *Intent:* //| //| :param condition: //| Input scalar or array. If an element (or scalar) is truthy, //| the co...
  * `compare_nonzero` **(Compute Cores)** (Impact: 35.9)
    * *Intent:* #if ULAB_NUMPY_HAS_NONZERO //| def nonzero(x: _ScalarOrArrayLike) -> ulab.numpy.ndarray: //| """ //|...
  * `compare_isinf_isfinite` **(Compute Cores)** (Impact: 35.4)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_ISFINITE | ULAB_NUMPY_HAS_ISINF
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 87 instances
* *State Mutation (weighted view):* 276
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 33`, `args: 67`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 102`
* *Architecture:* `api: 10`, `import: 11`
* *Defense:* `safety: 22`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` ndarray_operators.h, ulab.h, ulab_tools.h, carray_tools.h, compare.h, math.h, misc.h, obj.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/bitwise.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 10.147)
- **Top Global Matches:** file_cluster_3: 10.147, file_cluster_8: 16.712, file_cluster_6: 29.175
- **Magnitude:** 660.46 | **LOC:** 431 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 2.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bitwise_left_shift_loop` **(Many-Argument Workhorses)** (Impact: 87.9)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_LEFT_SHIFT
  * `bitwise_right_shift_loop` **(Many-Argument Workhorses)** (Impact: 87.9)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_RIGHT_SHIFT
  * `bitwise_bitwise_and_loop` **(Many-Argument Workhorses)** (Impact: 74.1)
    * *Intent:* * */ #include <math.h> #include <stdio.h> #include <stdlib.h> #include <string.h> #include "py/obj.h...
  * `bitwise_bitwise_or_loop` **(Many-Argument Workhorses)** (Impact: 74.1)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_BITWISE_OR
  * `bitwise_bitwise_xor_loop` **(Many-Argument Workhorses)** (Impact: 74.1)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_BITWISE_XOR
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 26`, `args: 23`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 67`
* *Architecture:* `api: 11`, `import: 7`
* *Defense:* `safety: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bitwise.h, math.h, obj.h, runtime.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/scipy/integrate/integrate.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.718)
- **Top Global Matches:** file_cluster_6: 5.718, file_cluster_4: 9.263, file_cluster_8: 16.008
- **Magnitude:** 645.92 | **LOC:** 702 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 2.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tanhsinh` **(Many-Argument Workhorses)** (Impact: 81.8)
    * *Intent:* // integrate function f, range a..b, max levels n, error tolerance eps
  * `exp_sinh_opt_d` **(Many-Argument Workhorses)** (Impact: 42.7)
    * *Intent:* #if ULAB_INTEGRATE_HAS_TANHSINH // Tanh-Sinh, Sinh-Sinh and Exp-Sinh quadrature // https://www.geniv...
  * `qromb` **(Many-Argument Workhorses)** (Impact: 16.1)
    * *Intent:* #endif /* ULAB_INTEGRATE_HAS_TANHSINH */ #if ULAB_INTEGRATE_HAS_ROMBERG // Romberg quadrature // Thi...
  * `qakro` **(Many-Argument Workhorses)** (Impact: 15.0)
  * `integrate_tanhsinh` **(Stateful Encapsulated Methods)** (Impact: 14.1)
    * *Intent:* //| ) -> float: //| """ //| :param callable f: The function to integrate //| :param float a: The low...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 125 instances
* *State Mutation (weighted view):* 382
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 18`, `args: 29`, `func_start: 13`
* *Risk/State:* `state_mutation: 132`, `dead_code: 1`
* *Architecture:* `api: 8`, `import: 9`
* *Defense:* `safety: 4`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ndarray.h, ulab.h, ulab_tools.h, integrate.h, math.h, misc.h, obj.h, objtuple.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/linalg/linalg.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.605)
- **Top Global Matches:** file_cluster_8: 9.605, file_cluster_6: 18.716, file_cluster_3: 20.905
- **Magnitude:** 526.2 | **LOC:** 543 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 2.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.6%), Complexity Load (formerly Cognitive Load) (68.1%), Debt Markers (formerly Tech Debt) (8.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `linalg_qr` **(Many-Argument Workhorses)** (Impact: 54.0)
    * *Intent:* #if ULAB_MAX_DIMS > 1 //| def qr(m: ulab.numpy.ndarray) -> Tuple[ulab.numpy.ndarray, ulab.numpy.ndar...
  * `linalg_norm` **(Many-Argument Workhorses)** (Impact: 38.2)
    * *Intent:* #endif //| def norm(x: ulab.numpy.ndarray) -> float: //| """ //| :param ~ulab.numpy.ndarray x: a vec...
  * `linalg_cholesky` **(Defensive Guards)** (Impact: 24.0)
    * *Intent:* //| """Linear algebra functions""" //| #if ULAB_MAX_DIMS > 1 //| def cholesky(A: ulab.numpy.ndarray)...
  * `linalg_det` **(Defensive Guards)** (Impact: 21.3)
    * *Intent:* //| def det(m: ulab.numpy.ndarray) -> float: //| """ //| :param: m, a square matrix //| :return floa...
  * `linalg_eig` **(Defensive Guards)** (Impact: 13.8)
    * *Intent:* #endif #if ULAB_MAX_DIMS > 1 //| def eig(m: ulab.numpy.ndarray) -> Tuple[ulab.numpy.ndarray, ulab.nu...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 118 instances
* *State Mutation (weighted view):* 360
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 15`, `args: 39`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 124`, `planned_debt: 1`
* *Architecture:* `import: 10`
* *Defense:* `safety: 48`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` ulab.h, ulab_tools.h, carray_tools.h, linalg.h, math.h, misc.h, obj.h, runtime.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/vector.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.231)
- **Top Global Matches:** file_cluster_6: 8.231, file_cluster_4: 12.101, file_cluster_8: 16.197
- **Magnitude:** 502.72 | **LOC:** 979 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 2.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.2%), Complexity Load (formerly Cognitive Load) (30.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `vector_exp` **(Many-Argument Workhorses)** (Impact: 110.1)
    * *Intent:* #endif /* ULAB_MATH_FUNCTIONS_OUT_KEYWORD */ #endif /* ULAB_SCIPY_SPECIAL_HAS_ERFC */ #if ULAB_NUMPY...
  * `vector_generic_vector` **(Many-Argument Workhorses)** (Impact: 53.4)
    * *Intent:* #include "../ulab.h" #include "../ulab_tools.h" #include "carray/carray_tools.h" #include "vector.h"...
  * `vector_sqrt` **(Many-Argument Workhorses)** (Impact: 36.2)
    * *Intent:* #endif /* ULAB_MATH_FUNCTIONS_OUT_KEYWORD */ #endif /* ULAB_NUMPY_HAS_SINH */ #if ULAB_NUMPY_HAS_SQR...
  * `vector_arctan2` **(Many-Argument Workhorses)** (Impact: 28.3)
    * *Intent:* #endif /* ULAB_MATH_FUNCTIONS_OUT_KEYWORD */ #endif /* ULAB_NUMPY_HAS_ATANH */ #if ULAB_NUMPY_HAS_AR...
  * `vector_vectorized_function_call` **(Many-Argument Workhorses)** (Impact: 26.8)
    * *Intent:* #endif /* ULAB_MATH_FUNCTIONS_OUT_KEYWORD */ #endif /* ULAB_NUMPY_HAS_TANH */ #if ULAB_NUMPY_HAS_VEC...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 143
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 37`, `args: 57`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 61`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 11`
* *Defense:* `safety: 22`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` ulab.h, ulab_tools.h, carray_tools.h, math.h, binary.h, obj.h, objarray.h, runtime.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/transform.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.124)
- **Top Global Matches:** file_cluster_3: 8.124, file_cluster_8: 21.36, file_cluster_6: 34.04
- **Magnitude:** 403.7 | **LOC:** 457 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 2.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.7%), Complexity Load (formerly Cognitive Load) (68.3%), Debt Markers (formerly Tech Debt) (9.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `transform_delete` **(Many-Argument Workhorses)** (Impact: 74.8)
    * *Intent:* #endif /* ULAB_NUMPY_HAS_COMPRESS */ #if ULAB_NUMPY_HAS_DELETE
  * `transform_compress` **(Many-Argument Workhorses)** (Impact: 48.7)
    * *Intent:* #include <math.h> #include <stdlib.h> #include <string.h> #include "py/obj.h" #include "py/runtime.h...
  * `transform_dot` **(Defensive Guards)** (Impact: 25.3)
    * *Intent:* #endif /* ULAB_NUMPY_HAS_DELETE */ #if ULAB_MAX_DIMS > 1 #if ULAB_NUMPY_HAS_DOT //| def dot(m1: ulab...
  * `transform_size` **(Stateful Encapsulated Methods)** (Impact: 13.7)
    * *Intent:* #endif /* ULAB_NUMPY_HAS_DOT */ #endif /* ULAB_MAX_DIMS > 1 */ #if ULAB_NUMPY_HAS_SIZE
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 73 instances
* *State Mutation (weighted view):* 233
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 10`, `args: 39`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 87`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 1`, `import: 13`
* *Defense:* `safety: 48`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` ulab.h, ulab_tools.h, carray_tools.h, math.h, numerical.h, misc.h, obj.h, runtime.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/utils/utils.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.496)
- **Top Global Matches:** file_cluster_8: 9.496, file_cluster_6: 18.288, file_cluster_3: 21.276
- **Magnitude:** 362.82 | **LOC:** 415 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 2.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.4%), Complexity Load (formerly Cognitive Load) (72.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `utils_from_intbuffer_helper` **(Many-Argument Workhorses)** (Impact: 89.1)
    * *Intent:* #if ULAB_UTILS_HAS_FROM_INT16_BUFFER | ULAB_UTILS_HAS_FROM_UINT16_BUFFER | ULAB_UTILS_HAS_FROM_INT32...
  * `utils_spectrogram` **(Many-Argument Workhorses)** (Impact: 72.6)
    * *Intent:* #endif /* ULAB_UTILS_HAS_FROM_INT16_BUFFER | ULAB_UTILS_HAS_FROM_UINT16_BUFFER | ULAB_UTILS_HAS_FROM...
  * `utils_from_int16_buffer` **(Encapsulated Accessors)** (Impact: 2.1)
    * *Intent:* #ifdef ULAB_UTILS_HAS_FROM_INT16_BUFFER
  * `utils_from_uint16_buffer` **(Encapsulated Accessors)** (Impact: 2.1)
    * *Intent:* #endif #ifdef ULAB_UTILS_HAS_FROM_UINT16_BUFFER
  * `utils_from_int32_buffer` **(Encapsulated Accessors)** (Impact: 2.1)
    * *Intent:* #endif #ifdef ULAB_UTILS_HAS_FROM_INT32_BUFFER
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 184
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 11`, `args: 34`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 62`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `safety: 21`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` fft_tools.h, ulab_tools.h, math.h, misc.h, obj.h, runtime.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/ulab_tools.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 9.851)
- **Top Global Matches:** file_cluster_7: 9.851, file_cluster_12: 9.928, file_cluster_5: 11.352
- **Magnitude:** 315.16 | **LOC:** 332 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **5**; blast radius 8.705; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ndarray_upcast_dtype` **(Compute Cores)** (Impact: 43.1)
    * *Intent:* #if NDARRAY_BINARY_USES_FUN_POINTER | ULAB_NUMPY_HAS_WHERE
  * `ulab_tools_inspect_out` **(Many-Argument Workhorses)** (Impact: 20.9)
  * `ndarray_get_float_index` **(Defensive Guards)** (Impact: 18.7)
  * `ndarray_get_float_value` **(Compute Cores)** (Impact: 16.3)
  * `tools_reduce_axes` **(Many-Argument Workhorses)** (Impact: 15.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 68`, `args: 34`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 29`, `planned_debt: 1`, `unreferenced_by_name: 12`
* *Architecture:* `api: 23`, `import: 5`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.705
  * `Choke Point (Betweenness):` 0.000306 | `Ripple Effect (Closeness):` 0.102796
  * `Imports (Out-Degree: 4):` ndarray.h, runtime.h, string.h, ulab.h, ulab_tools.h
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `code/numpy/fft/fft_tools.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.678)
- **Top Global Matches:** file_cluster_9: 8.678, file_cluster_12: 12.105, file_cluster_7: 13.831
- **Magnitude:** 307.88 | **LOC:** 267 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 2.854; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fft_fft_ifft` **(Many-Argument Workhorses)** (Impact: 34.9)
  * `fft_fft_ifft` **(Defensive Guards)** (Impact: 21.5)
    * *Intent:* /* * The following function is a helper interface to the python side. * It has been factored out fro...
  * `fft_kernel` **(Many-Argument Workhorses)** (Impact: 20.1)
    * *Intent:* #else /* ULAB_SUPPORTS_COMPLEX & ULAB_FFT_IS_NUMPY_COMPATIBLE */
  * `fft_kernel` **(Many-Argument Workhorses)** (Impact: 18.2)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 205
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 6`, `args: 17`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 81`, `planned_debt: 2`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `safety: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.854
  * `Choke Point (Betweenness):` 0.000228 | `Ripple Effect (Closeness):` 0.010526
  * `Imports (Out-Degree: 6):` ndarray.h, ulab_tools.h, carray_tools.h, fft_tools.h, math.h, runtime.h, string.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `code/scipy/optimize/optimize.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.123)
- **Top Global Matches:** file_cluster_6: 7.123, file_cluster_4: 9.289, file_cluster_16: 15.728
- **Magnitude:** 229.2 | **LOC:** 418 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 2.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.4%), Complexity Load (formerly Cognitive Load) (64.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `optimize_fmin` **(Many-Argument Workhorses)** (Impact: 44.5)
    * *Intent:* //| ) -> float: //| """ //| :param callable f: The function to bisect //| :param float x0: The initi...
  * `optimize_bisect` **(Stateful Encapsulated Methods)** (Impact: 20.2)
    * *Intent:* //| ) -> float: //| """ //| :param callable f: The function to bisect //| :param float a: The left s...
  * `optimize_jacobi` **(Many-Argument Workhorses)** (Impact: 17.5)
    * *Intent:* #endif #if ULAB_SCIPY_OPTIMIZE_HAS_CURVE_FIT
  * `optimize_curve_fit` **(Many-Argument Workhorses)** (Impact: 15.2)
  * `optimize_newton` **(Stateful Encapsulated Methods)** (Impact: 13.9)
    * *Intent:* //| ) -> float: //| """ //| :param callable f: The function to bisect //| :param float x0: The initi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 106
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 10`, `args: 44`, `func_start: 7`
* *Risk/State:* `state_mutation: 38`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `import: 8`
* *Defense:* `safety: 6`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ndarray.h, ulab.h, ulab_tools.h, math.h, optimize.h, misc.h, obj.h, runtime.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/poly.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.701)
- **Top Global Matches:** file_cluster_8: 7.701, file_cluster_6: 17.744, file_cluster_3: 20.226
- **Magnitude:** 223.3 | **LOC:** 219 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 2.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poly_polyfit` **(Many-Argument Workhorses)** (Impact: 42.1)
    * *Intent:* */ #include "py/obj.h" #include "py/runtime.h" #include "py/objarray.h" #include "../ulab.h" #includ...
  * `poly_polyval` **(Many-Argument Workhorses)** (Impact: 18.5)
  * `poly_eval` **(Stateful Encapsulated Methods)** (Impact: 4.4)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_POLYVAL
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 5`, `args: 27`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 51`, `planned_debt: 2`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `safety: 11`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` ulab.h, ulab_tools.h, carray_tools.h, linalg_tools.h, poly.h, obj.h, objarray.h, runtime.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/scipy/linalg/linalg.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 10.193)
- **Top Global Matches:** file_cluster_9: 10.193, file_cluster_12: 12.357, file_cluster_7: 13.204
- **Magnitude:** 223.14 | **LOC:** 282 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 2.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (62.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `solve_triangular` **(Many-Argument Workhorses)** (Impact: 30.9)
    * *Intent:* //| def solve_triangular(A: ulab.numpy.ndarray, b: ulab.numpy.ndarray, lower: bool) -> ulab.numpy.nd...
  * `cho_solve` **(Many-Argument Workhorses)** (Impact: 23.8)
    * *Intent:* //| def cho_solve(L: ulab.numpy.ndarray, b: ulab.numpy.ndarray) -> ulab.numpy.ndarray: //| """ //| :...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 165
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 8`, `args: 30`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 73`
* *Architecture:* `import: 10`
* *Defense:* `safety: 10`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` linalg_tools.h, ulab.h, ulab_tools.h, linalg.h, math.h, misc.h, obj.h, runtime.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/random/random.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.4)
- **Top Global Matches:** file_cluster_6: 7.4, file_cluster_4: 9.6, file_cluster_16: 16.35
- **Magnitude:** 209.44 | **LOC:** 362 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 2.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.7%), Complexity Load (formerly Cognitive Load) (56.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `random_random` **(Many-Argument Workhorses)** (Impact: 38.2)
    * *Intent:* #endif /* ULAB_NUMPY_RANDOM_HAS_NORMAL */ #if ULAB_NUMPY_RANDOM_HAS_RANDOM
  * `random_normal` **(Many-Argument Workhorses)** (Impact: 21.6)
    * *Intent:* #endif #if ULAB_NUMPY_RANDOM_HAS_NORMAL
  * `random_generator_make_new` **(Many-Argument Workhorses)** (Impact: 20.1)
  * `random_uniform` **(Stateful Encapsulated Methods)** (Impact: 14.6)
    * *Intent:* #endif /* ULAB_NUMPY_RANDOM_HAS_RANDOM */ #if ULAB_NUMPY_RANDOM_HAS_UNIFORM
  * `pcg32_next` **(Encapsulated Accessors)** (Impact: 3.2)
    * *Intent:* // END OF GENERATOR COMPONENTS
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 16`, `args: 29`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 50`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 14`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` math.h, builtin.h, obj.h, runtime.h, random.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/numpy/linalg/linalg_tools.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.085)
- **Top Global Matches:** file_cluster_9: 6.085, file_cluster_15: 12.393, file_cluster_16: 12.402
- **Magnitude:** 203.68 | **LOC:** 171 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 2.459; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.4%), Complexity Load (formerly Cognitive Load) (72.2%), Debt Markers (formerly Tech Debt) (34.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `linalg_jacobi_rotations` **(Many-Argument Workhorses)** (Impact: 34.2)
    * *Intent:* /* * The following function calculates the eigenvalues and eigenvectors of a symmetric * real matrix...
  * `linalg_invert_matrix` **(Defensive Guards)** (Impact: 25.3)
    * *Intent:* */ #include <math.h> #include <string.h> #include "py/runtime.h" #include "linalg_tools.h" /* * The ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 9`, `args: 10`, `func_start: 2`
* *Risk/State:* `state_mutation: 52`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.459
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.010526
  * `Imports (Out-Degree: 1):` linalg_tools.h, math.h, runtime.h, string.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `code/numpy/approx.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.438)
- **Top Global Matches:** file_cluster_3: 9.438, file_cluster_8: 21.888, file_cluster_6: 34.363
- **Magnitude:** 186.12 | **LOC:** 228 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 2.003; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `approx_interp` **(Many-Argument Workhorses)** (Impact: 40.4)
    * *Intent:* //| left: Optional[_float] = None, //| right: Optional[_float] = None //| ) -> ulab.numpy.ndarray: /...
  * `approx_trapz` **(Stateful Encapsulated Methods)** (Impact: 21.6)
    * *Intent:* #endif #if ULAB_NUMPY_HAS_TRAPZ //| def trapz(y: ulab.numpy.ndarray, x: Optional[ulab.numpy.ndarray]...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 5`, `args: 6`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 51`
* *Architecture:* `import: 10`
* *Defense:* `safety: 7`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.003
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` ulab.h, ulab_tools.h, approx.h, carray_tools.h, math.h, misc.h, obj.h, runtime.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `code/ndarray.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 4.869)
- **Top Global Matches:** file_cluster_17: 4.869, file_cluster_2: 6.462, file_cluster_12: 7.288
- **Magnitude:** 167.48 | **LOC:** 809 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **34** in-repo importer(s); it depends on **5**; blast radius 49.286; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (84.9%), Guard Balance (formerly Safety Score) (43.3%), Dead Code Surface (formerly Dead Code) (5.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 29`, `args: 57`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 77`, `dead_code: 1`
* *Architecture:* `api: 62`, `import: 5`
* *Defense:* `safety: 94`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 49.286
  * `Choke Point (Betweenness):` 0.000185 | `Ripple Effect (Closeness):` 0.21375
  * `Imports (Out-Degree: 1):` binary.h, objarray.h, objlist.h, objstr.h, ulab.h
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `code/numpy/numerical.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 4.968)
- **Top Global Matches:** file_cluster_17: 4.968, file_cluster_2: 5.096, file_cluster_15: 7.185
- **Magnitude:** 106.38 | **LOC:** 524 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 2.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.0%), Guard Balance (formerly Safety Score) (50.9%), Debt Markers (formerly Tech Debt) (9.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 82`, `planned_debt: 2`
* *Architecture:* `import: 2`
* *Defense:* `safety: 41`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.806
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.021053
  * `Imports (Out-Degree: 2):` ndarray.h, ulab.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `tests/2d/scipy/integrate.py` (PYTHON) | Magnitude: 20.48 | Delta: **0.101** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: debug_prints: 11, core_var_decl: 9, design_snake_case: 9, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tests/2d/numpy/linalg.py` (PYTHON) | Magnitude: 73.7 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 52, design_snake_case: 52, state_mutation: 39, design_short_vars: 28
- `snippets/numpy/lib/function_base.py` (PYTHON) | Magnitude: 22.76 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 8, core_var_decl: 7, design_snake_case: 7
- `snippets/numpy/core/numeric.py` (PYTHON) | Magnitude: 7.3 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, import: 2, indent_spaces: 2, core_var_decl: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `code/numpy/io/io.h` (C) | Magnitude: 13.64 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: macros: 2
- `code/numpy/transform.h` (C) | Magnitude: 15.3 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: import: 8, macros: 2, scientific: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `snippets/numpy/lib/type_check.py` (PYTHON) | Magnitude: 34.86 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 11, branch: 7, state_mutation: 6
- `code/ulab_tools.c` (C) | Magnitude: 315.16 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 181, branch: 89, structural_boundaries: 68, pointers: 63

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `code/numpy/create.c` -> Churn: **100.0%** | Cog Load: 73.4844% | Debt: 8.4228%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `code/numpy/create.c` -> **Iyassou Shimels** (100.0% isolated ownership) | Magnitude: 1111.08

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `code/ndarray.c` -> **Severity: 0.329** (Bridge: 0.0033 * Flux: 100.0%)
- `snippets/scipy/signal/filter_design.py` -> **Severity: 0.134** (Bridge: 0.0013 * Flux: 100.0%)
- `snippets/numpy/core/fromnumeric.py` -> **Severity: 0.09** (Bridge: 0.0009 * Flux: 100.0%)
- `snippets/numpy/lib/polynomial.py` -> **Severity: 0.076** (Bridge: 0.0008 * Flux: 100.0%)
- `snippets/numpy/lib/function_base.py` -> **Severity: 0.055** (Bridge: 0.0006 * Flux: 99.9932%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `snippets/numpy/__init__.py` -> **Severity: 19.244** (Embedded: 0.3546 * Error Risk: 54.2752%)
- `snippets/numpy/core/__init__.py` -> **Severity: 14.119** (Embedded: 0.2017 * Error Risk: 70.0%)
- `snippets/numpy/lib/__init__.py` -> **Severity: 13.789** (Embedded: 0.197 * Error Risk: 70.0%)
- `snippets/numpy/core/multiarray.py` -> **Severity: 11.184** (Embedded: 0.1598 * Error Risk: 70.0%)
- `snippets/numpy/lib/polynomial.py` -> **Severity: 10.701** (Embedded: 0.1421 * Error Risk: 75.2927%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `snippets/numpy/core/multiarray.py` -> **Severity: 6445.7** (Blast Radius: 64.457 * Doc Risk: 100.0%)
- `snippets/numpy/core/shape_base.py` -> **Severity: 1858.3** (Blast Radius: 18.583 * Doc Risk: 100.0%)
- `snippets/numpy/lib/function_base.py` -> **Severity: 1477.5** (Blast Radius: 14.775 * Doc Risk: 100.0%)
- `snippets/numpy/lib/polynomial.py` -> **Severity: 1477.5** (Blast Radius: 14.775 * Doc Risk: 100.0%)
- `snippets/numpy/lib/block.py` -> **Severity: 1363.9** (Blast Radius: 13.639 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2705 call pairs -- scoped 8.9%, unique 9.5%, ambiguous 1.0%, external 80.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 1832 | 8.8% | 14.0% | 0.0% | 77.2% |
| python | 846 | 9.3% | 0.0% | 3.1% | 87.6% |
| shell | 27 | 7.4% | 0.0% | 0.0% | 92.6% |

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
