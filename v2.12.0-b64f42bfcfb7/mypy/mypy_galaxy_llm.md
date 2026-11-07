# ARCHITECTURAL_BRIEF: mypy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/python/mypy.git` |
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
- **Scope:** 700 analyzed artifact(s), 147142 LOC.
- **Load-bearing artifact:** `test-data/unit/lib-stub/typing.pyi` -- 258 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `mypy/build.py` -- pulls in 59 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `mypy/checker.py` at magnitude 9936.38 (structural weight, not risk).
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
| Total Artifacts | 1866 |
| Analyzed Artifacts (Scanned) | 700 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1166 |
| Total LOC | 147142 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 37.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5053 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2335 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 11.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.0822 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 43 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 544 | 127450 | 77.7% |
| C | 102 | 15752 | 14.6% |
| PLAINTEXT | 14 | 0 | 2.0% |
| MARKDOWN | 13 | 0 | 1.9% |
| YAML | 9 | 614 | 1.3% |
| SHELL | 6 | 76 | 0.9% |
| CPP | 4 | 3124 | 0.6% |
| XML | 3 | 0 | 0.4% |
| DOCKERFILE | 1 | 8 | 0.1% |
| CSS | 1 | 70 | 0.1% |
| MAKEFILE | 1 | 9 | 0.1% |
| BATCH | 1 | 26 | 0.1% |
| M4 | 1 | 13 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 700 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 43%, Data / Markup / Trivial 21%, Large Core Modules (2) 10%, Declarative / Non-Code 9%, Many-Argument Workhorses Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 673 | 96.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 27 | 3.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1166*

**Composition by Extension & Reason:**
- `.pyi`: 750x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.test`: 261x Excluded (Unsupported Extension: '.test')
- `.rst`: 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 22x Excluded (Unsupported Extension: '.rst')
- `.h`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Hex Payload: 8192 hex tokens in 1032 LOC)
- `.typed`: 15x Excluded (Unsupported Extension: '.typed')
- `no_extension`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable)
- `.cc`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.patch`: 8x Excluded (Unsupported Extension: '.patch')
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4772 LOC)
- `.pump`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 76 LOC)
- `.ini`: 3x Excluded (Unsupported Extension: '.ini')
- `.py`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 96.0 | 23.1 | 10.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.2 | 50.6 | 57.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 20.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 21.5 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 25.4 | 9.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 47.2 | 31.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 80.2 | 0.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.5 | 1.1 | 0.1 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 9.5 | 4.9 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 67.0 | 94.4 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1709 | 254 | 6 | `mypy/test/testtypes.py` |
| cleanup | 31 | 20 | 0 | `mypy/test/testipc.py` |
| guards | 11041 | 450 | 34 | `mypy/checker.py` |
| danger | 5173 | 381 | 20 | `mypyc/test-data/fixtures/ir.py` |
| concurrency | 935 | 103 | 2 | `mypy/test/teststubtest.py` |
| connectivity | 11307 | 522 | 41 | `mypy/semanal.py` |
| io | 1504 | 148 | 5 | `mypy/modulefinder.py` |
| crypto | 3 | 3 | 0 | `mypy/util.py` |
| ipc | 131 | 33 | 0 | `misc/sync-typeshed.py` |
| time | 120 | 21 | 0 | `mypy/build.py` |
| serialization | 6 | 5 | 0 | `mypy/evalexpr.py` |
| regex | 153 | 43 | 0 | `misc/gen_blog_post_html.py` |
| events | 58 | 30 | 0 | `mypy/build_worker/worker.py` |
| tests | 1121 | 70 | 0 | `mypyc/lib-rt/test_capi.cc` |
| docs | 3262 | 307 | 10 | `mypy/test/teststubtest.py` |
| debt | 2350 | 259 | 6 | `mypy/test/teststubtest.py` |
| mutation | 54729 | 534 | 205 | `mypy/checker.py` |
| dead_code | 1443 | 243 | 4 | `mypy/test/testtypes.py` |
| credential | 1 | 1 | 0 | `misc/sync-typeshed.py` |
| threat | 11 | 4 | 0 | `mypyc/lib-rt/base64/librt_base64.c` |
| ml_ai | 7 | 2 | 0 | `mypyc/lib-rt/float_ops.c` |
| ui | 1 | 1 | 0 | `mypy/known_modules.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.6125**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `mypy/modulefinder.py` (Hits: 80)
- `mypy/build.py` (Hits: 58)
- `mypy/report.py` (Hits: 53)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **typing.pyi** (`test-data/unit/lib-stub/typing.pyi`) — 258 inbound connections
2. **ir.py** (`mypyc/test-data/fixtures/ir.py`) — 149 inbound connections
3. **nodes.py** (`mypy/nodes.py`) — 133 inbound connections
4. **types.py** (`mypy/types.py`) — 126 inbound connections
5. **sys.pyi** (`test-data/unit/lib-stub/sys.pyi`) — 91 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **build.py** (`mypy/build.py`) — 59 outbound dependencies
2. **checker.py** (`mypy/checker.py`) — 47 outbound dependencies
3. **checkexpr.py** (`mypy/checkexpr.py`) — 44 outbound dependencies
4. **emitmodule.py** (`mypyc/codegen/emitmodule.py`) — 40 outbound dependencies
5. **stubtest.py** (`mypy/stubtest.py`) — 38 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `vgetargskeywords` **(Many-Argument Workhorses)** (@ `mypyc/lib-rt/getargs.c`) -> Impact: **284.4** | LOC: 343
  * *Intent:* #define IS_END_OF_FORMAT(c) (c == '\0' || c == ';' || c == ':')
- `emit_cast` **(Many-Argument Workhorses)** (@ `mypyc/codegen/emit.py`) -> Impact: **269.9** | LOC: 224
- `vgetargskeywordsfast_impl` **(Many-Argument Workhorses)** (@ `mypyc/lib-rt/getargsfast.c`) -> Impact: **267.8** | LOC: 276
- `format_type_inner` **(Many-Argument Workhorses)** (@ `mypy/messages.py`) -> Impact: **262.9** | LOC: 231
- `is_overlapping_types` **(Many-Argument Workhorses)** (@ `mypy/meet.py`) -> Impact: **231.3** | LOC: 314
- `check_assignment` **(Many-Argument Workhorses)** (@ `mypy/checker.py`) -> Impact: **215.9** | LOC: 202
- `process_options` **(Many-Argument Workhorses)** (@ `mypy/main.py`) -> Impact: **203.5** | LOC: 213
- `define_options` **(Many-Argument Workhorses)** (@ `mypy/main.py`) -> Impact: **201.4** | LOC: 893
- `emit_unbox` **(Many-Argument Workhorses)** (@ `mypyc/codegen/emit.py`) -> Impact: **199.3** | LOC: 191
- `analyze_class_attribute_access` **(Many-Argument Workhorses)** (@ `mypy/checkmember.py`) -> Impact: **198.0** | LOC: 203

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `mypy` | 114 | 95241.68 | 43.2% | 15.33% |
| `mypyc/irbuild` | 28 | 15713.88 | 45.92% | 17.1% |
| `mypy/test` | 47 | 7878.66 | 19.46% | 0.0% |
| `mypyc/lib-rt` | 37 | 7643.38 | 31.68% | 37.43% |
| `mypyc/codegen` | 8 | 5932.78 | 48.24% | 7.62% |
| `mypy/plugins` | 11 | 4072.3 | 38.52% | 15.03% |
| `mypyc/ir` | 8 | 3757.98 | 45.02% | 28.31% |
| `mypy/server` | 11 | 3572.44 | 41.67% | 9.73% |
| `mypyc/test` | 32 | 2619.36 | 14.74% | 0.0% |
| `mypyc/lib-rt/vecs` | 12 | 2607.22 | 24.64% | 6.19% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `mypyc/ir/ops.py` -> **100.0%** Exposure
- `mypyc/test-data/fixtures/ir.py` -> **100.0%** Exposure
- `mypyc/test-data/fixtures/typing-full.pyi` -> **100.0%** Exposure
- `test-data/pybind11_fixtures/expected_stubs_no_docs/pybind11_fixtures/__init__.pyi` -> **100.0%** Exposure
- `test-data/pybind11_fixtures/expected_stubs_no_docs/pybind11_fixtures/demo.pyi` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `misc/analyze_cache.py` -> **100.0%** Exposure
- `misc/apply-cache-diff.py` -> **100.0%** Exposure
- `misc/diff-cache.py` -> **100.0%** Exposure
- `misc/docker/build.py` -> **100.0%** Exposure
- `misc/gen_blog_post_html.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `mypyc/test-data/fixtures/ir.py` -> **76** Orphaned Functions | **32** Duplicates
- `mypy/test/testtypes.py` -> **92** Orphaned Functions | **13** Duplicates
- `mypy/test/teststubgen.py` -> **83** Orphaned Functions | **15** Duplicates
- `mypyc/ir/ops.py` -> **0** Orphaned Functions | **75** Duplicates
- `mypyc/test/test_emitfunc.py` -> **72** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `3829` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `mypy/checker.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.857)
- **Top Global Matches:** file_cluster_6: 8.857, file_cluster_4: 9.828, file_cluster_12: 16.312
- **Magnitude:** 9936.38 | **LOC:** 9583 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 61.3%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **47**; blast radius 0.97; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Connectivity (formerly Api Exposure) (85.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 68.1621% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_assignment` **(Many-Argument Workhorses)** (Impact: 215.9)
  * `check_func_def` **(Many-Argument Workhorses)** (Impact: 185.6)
  * `check_override` **(Many-Argument Workhorses)** (Impact: 176.3)
  * `narrow_type_by_identity_equality` **(Many-Argument Workhorses)** (Impact: 169.2)
  * `check_method_override_for_base_with_name` **(Many-Argument Workhorses)** (Impact: 147.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1105 instances
* *State Mutation (weighted view):* 3533
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2289`, `structural_boundaries: 1616`, `args: 346`, `func_start: 341`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 100`, `state_mutation: 1323`, `dead_code: 2`, `planned_debt: 69`, `fragile_debt: 9`
* *Architecture:* `api: 331`, `concurrency: 2`, `import: 47`
* *Defense:* `safety: 689`, `doc: 167`, `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.97
  * `Choke Point (Betweenness):` 0.002868 | `Ripple Effect (Closeness):` 0.036608
  * `Imports (Out-Degree: 47):` __future__, collections, collections.abc, contextlib, itertools, mypy, mypy.binder, mypy.checker_shared...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `mypy/semanal.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.704)
- **Top Global Matches:** file_cluster_6: 8.704, file_cluster_4: 9.303, file_cluster_12: 16.065
- **Magnitude:** 9310.16 | **LOC:** 8436 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **36**; blast radius 0.903; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (84.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (81.3%), Guard Balance (formerly Safety Score) (69.5%)
- **Documentation Coverage:** 70.9302% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_and_set_up_type_alias` **(Many-Argument Workhorses)** (Impact: 128.1)
    * *Intent:* """Check if assignment creates a type alias and set it up as needed. Return True if it is a type ali...
  * `visit_call_expr` **(Many-Argument Workhorses)** (Impact: 103.6)
    * *Intent:* """Analyze a call expression. Some call expressions are recognized as special forms, including cast(...
  * `analyze_member_lvalue` **(Many-Argument Workhorses)** (Impact: 79.6)
  * `visit_decorator` **(Many-Argument Workhorses)** (Impact: 77.8)
  * `_lookup` **(Many-Argument Workhorses)** (Impact: 75.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1165 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 3674
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2145`, `structural_boundaries: 1468`, `args: 346`, `func_start: 342`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 69`, `state_mutation: 1344`, `dead_code: 8`, `planned_debt: 41`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 338`, `concurrency: 5`, `import: 34`
* *Defense:* `safety: 639`, `doc: 138`, `test: 2`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.903
  * `Choke Point (Betweenness):` 0.002364 | `Ripple Effect (Closeness):` 0.043561
  * `Imports (Out-Degree: 32):` __future__, climbs, collections.abc, contextlib, it, mypy, mypy.constant_fold, mypy.errorcodes...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `mypy/checkexpr.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.016)
- **Top Global Matches:** file_cluster_6: 8.016, file_cluster_4: 10.691, file_cluster_8: 17.219
- **Magnitude:** 6998.18 | **LOC:** 6998 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 54.2%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **44**; blast radius 0.675; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (77.7%), Connectivity (formerly Api Exposure) (74.5%)
- **Documentation Coverage:** 68.8995% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_callable_call` **(Many-Argument Workhorses)** (Impact: 194.4)
  * `visit_call_expr_inner` **(Many-Argument Workhorses)** (Impact: 129.5)
  * `dangerous_comparison` **(Many-Argument Workhorses)** (Impact: 125.3)
  * `accept` **(Many-Argument Workhorses)** (Impact: 114.2)
    * *Intent:* # # Helpers #
  * `check_argument_types` **(Many-Argument Workhorses)** (Impact: 101.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 804 instances
* *State Mutation (weighted view):* 2520
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1522`, `structural_boundaries: 1069`, `args: 223`, `func_start: 212`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 78`, `state_mutation: 912`, `dead_code: 5`, `planned_debt: 36`, `fragile_debt: 5`, `duplicate_logic: 4`
* *Architecture:* `api: 211`, `import: 43`
* *Defense:* `safety: 483`, `doc: 128`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.675
  * `Choke Point (Betweenness):` 0.0006 | `Ripple Effect (Closeness):` 0.031646
  * `Imports (Out-Degree: 41):` __future__, collections, collections.abc, contextlib, enum, it, itertools, mypy...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `mypy/build.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.453)
- **Top Global Matches:** file_cluster_4: 9.453, file_cluster_5: 9.912, file_cluster_12: 10.993
- **Magnitude:** 4313.5 | **LOC:** 4822 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 54.5%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **59**; blast radius 1.272; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (91.9%), Connectivity (formerly Api Exposure) (90.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 64.1196% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `new_state` **(Many-Argument Workhorses)** (Impact: 131.3)
  * `validate_meta` **(Many-Argument Workhorses)** (Impact: 121.7)
  * `find_cache_meta` **(Many-Argument Workhorses)** (Impact: 111.4)
  * `load_graph` **(Many-Argument Workhorses)** (Impact: 92.9)
  * `process_stale_scc` **(Many-Argument Workhorses)** (Impact: 89.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 583 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 1860
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 811`, `structural_boundaries: 601`, `args: 162`, `func_start: 157`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 104`, `high_risk_execution: 2`, `state_mutation: 694`, `dead_code: 2`, `planned_debt: 35`, `fragile_debt: 6`
* *Architecture:* `io: 58`, `api: 157`, `import: 68`
* *Defense:* `safety: 132`, `doc: 89`, `immutability_locks: 23`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.272
  * `Choke Point (Betweenness):` 0.01015 | `Ripple Effect (Closeness):` 0.0428
  * `Imports (Out-Degree: 44):` __future__, collections, collections.abc, contextlib, gc, heapq, importlib, json...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `mypy/types.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.879)
- **Top Global Matches:** file_cluster_5: 8.879, file_cluster_0: 8.911, file_cluster_12: 9.885
- **Magnitude:** 3787.24 | **LOC:** 4453 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 29.4%
- **Blast Radius:** changing it is visible to **126** in-repo importer(s); it depends on **15**; blast radius 17.019; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (77.1%), Complexity Load (formerly Cognitive Load) (75.1%)
- **Documentation Coverage:** 93.0576% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `copy_modified` **(Many-Argument Workhorses)** (Impact: 195.1)
  * `slice` **(Many-Argument Workhorses)** (Impact: 88.5)
  * `visit_callable_type` **(Many-Argument Workhorses)** (Impact: 76.7)
  * `copy_modified` **(Many-Argument Workhorses)** (Impact: 40.1)
  * `read_type` **(Compute Cores)** (Impact: 38.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 362 instances
* *State Mutation (weighted view):* 1239
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 666`, `structural_boundaries: 1132`, `args: 385`, `func_start: 385`, `class_start: 45`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 515`, `planned_debt: 16`, `fragile_debt: 3`, `duplicate_logic: 26`
* *Architecture:* `io: 1`, `api: 337`, `import: 16`
* *Defense:* `safety: 189`, `doc: 65`, `immutability_locks: 103`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.019
  * `Choke Point (Betweenness):` 0.003924 | `Ripple Effect (Closeness):` 0.206382
  * `Imports (Out-Degree: 13):` __future__, abc, collections.abc, librt.internal, mypy.bogus_type, mypy.cache, mypy.expandtype, mypy.nodes...
  * `Imported By (In-Degree: 126):` (Excluded from Brief to save tokens)

### `mypy/messages.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.552)
- **Top Global Matches:** file_cluster_5: 9.552, file_cluster_0: 9.59, file_cluster_4: 9.721
- **Magnitude:** 3619.46 | **LOC:** 3428 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **20**; blast radius 1.845; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.4%)
- **Documentation Coverage:** 88.2051% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `format_type_inner` **(Many-Argument Workhorses)** (Impact: 262.9)
  * `incompatible_argument` **(Many-Argument Workhorses)** (Impact: 182.0)
  * `report_protocol_problems` **(Many-Argument Workhorses)** (Impact: 173.1)
  * `has_no_attr` **(Many-Argument Workhorses)** (Impact: 147.9)
    * *Intent:* # # Specific operations # # The following operations are for generating specific error messages. The...
  * `pretty_callable` **(Many-Argument Workhorses)** (Impact: 110.0)
    * *Intent:* """Return a nice easily-readable representation of a callable type. For example: def [T <: int] f(se...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 341 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 1073
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 739`, `structural_boundaries: 643`, `args: 193`, `func_start: 191`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 391`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `api: 190`, `concurrency: 3`, `import: 21`
* *Defense:* `safety: 126`, `doc: 47`, `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.845
  * `Choke Point (Betweenness):` 0.002166 | `Ripple Effect (Closeness):` 0.084566
  * `Imports (Out-Degree: 16):` __future__, collections.abc, contextlib, difflib, itertools, mypy, mypy.erasetype, mypy.errorcodes...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `mypy/nodes.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.756)
- **Top Global Matches:** file_cluster_0: 7.756, file_cluster_5: 8.368, file_cluster_12: 9.239
- **Magnitude:** 3197.56 | **LOC:** 5368 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 46.7%
- **Blast Radius:** changing it is visible to **133** in-repo importer(s); it depends on **17**; blast radius 18.254; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (83.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 93.1338% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_arg_kinds` **(Compute Cores)** (Impact: 47.8)
  * `deserialize` **(Many-Argument Workhorses)** (Impact: 36.1)
  * `serialize` **(Compute Cores)** (Impact: 30.2)
    * *Intent:* # NOTE: This is where all ClassDefs originate, so there shouldn't be duplicates. data = { ".class": ...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 30.0)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 25.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 294 instances
* *State Mutation (weighted view):* 1426
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 379`, `structural_boundaries: 940`, `args: 329`, `func_start: 328`, `class_start: 99`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 838`, `dead_code: 9`, `planned_debt: 25`, `fragile_debt: 4`, `duplicate_logic: 32`
* *Architecture:* `io: 1`, `api: 336`, `import: 17`
* *Defense:* `safety: 123`, `doc: 101`, `immutability_locks: 136`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.254
  * `Choke Point (Betweenness):` 0.004643 | `Ripple Effect (Closeness):` 0.233105
  * `Imports (Out-Degree: 13):` __future__, abc, collections, collections.abc, contextlib, enum, librt.internal, mypy.cache...
  * `Imported By (In-Degree: 133):` (Excluded from Brief to save tokens)

### `mypyc/irbuild/ll_builder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.888)
- **Top Global Matches:** file_cluster_4: 7.888, file_cluster_6: 10.482, file_cluster_0: 12.89
- **Magnitude:** 3193.88 | **LOC:** 3067 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **32**; blast radius 1.886; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (83.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.9%)
- **Documentation Coverage:** 59.5918% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_construct_varargs` **(Many-Argument Workhorses)** (Impact: 161.1)
    * *Intent:* # Calls
  * `binary_op` **(Many-Argument Workhorses)** (Impact: 138.1)
    * *Intent:* # Other primitive operations """Perform a binary operation. Generate specialized operations based on...
  * `coerce` **(Many-Argument Workhorses)** (Impact: 132.3)
  * `native_args_to_positional` **(Many-Argument Workhorses)** (Impact: 86.7)
  * `gen_method_call` **(Many-Argument Workhorses)** (Impact: 66.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 351 instances
* *State Mutation (weighted view):* 1165
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 595`, `structural_boundaries: 644`, `args: 131`, `func_start: 128`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 463`, `planned_debt: 17`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 119`, `import: 32`
* *Defense:* `safety: 107`, `doc: 77`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.886
  * `Choke Point (Betweenness):` 0.002493 | `Ripple Effect (Closeness):` 0.028677
  * `Imports (Out-Degree: 31):` __future__, collections.abc, mypy.argmap, mypy.nodes, mypy.operators, mypy.types, mypyc.common, mypyc.errors...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `mypy/typeanal.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.586)
- **Top Global Matches:** file_cluster_4: 8.586, file_cluster_6: 10.252, file_cluster_5: 13.737
- **Magnitude:** 2963.24 | **LOC:** 2804 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 18.2%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **20**; blast radius 0.811; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (84.4%), Complexity Load (formerly Cognitive Load) (83.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 92.7126% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `instantiate_type_alias` **(Many-Argument Workhorses)** (Impact: 166.9)
  * `visit_unbound_type_nonoptional` **(Many-Argument Workhorses)** (Impact: 159.2)
  * `try_analyze_special_unbound_type` **(Many-Argument Workhorses)** (Impact: 142.8)
    * *Intent:* """Bind special type that is recognized through magic name such as 'typing.Any'. Return the bound ty...
  * `analyze_unbound_type_without_type_info` **(Many-Argument Workhorses)** (Impact: 75.4)
  * `set_any_tvars` **(Many-Argument Workhorses)** (Impact: 66.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 334 instances
* *State Mutation (weighted view):* 1079
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 623`, `structural_boundaries: 620`, `args: 128`, `func_start: 127`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 411`, `planned_debt: 24`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 128`, `import: 20`
* *Defense:* `safety: 163`, `doc: 25`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.811
  * `Choke Point (Betweenness):` 7.8e-05 | `Ripple Effect (Closeness):` 0.037109
  * `Imports (Out-Degree: 18):` __future__, collections.abc, contextlib, itertools, mypy, mypy.errorcodes, mypy.errors, mypy.expandtype...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `mypy/nativeparse.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.079)
- **Top Global Matches:** file_cluster_6: 9.079, file_cluster_8: 12.582, file_cluster_4: 15.626
- **Magnitude:** 2799.46 | **LOC:** 2095 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **15**; blast radius 0.74; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (64.6%)
- **Documentation Coverage:** 64.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read_expression` **(Many-Argument Workhorses)** (Impact: 164.4)
  * `read_statement` **(Many-Argument Workhorses)** (Impact: 116.5)
  * `fix_function_overloads` **(Many-Argument Workhorses)** (Impact: 87.1)
    * *Intent:* """Merge consecutive function overloads into OverloadedFuncDef nodes. This function processes a list...
  * `read_type` **(Many-Argument Workhorses)** (Impact: 81.6)
  * `read_pattern` **(Many-Argument Workhorses)** (Impact: 48.4)
    * *Intent:* """Read a pattern node from the buffer."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 598 instances
* *State Mutation (weighted view):* 1855
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 417`, `structural_boundaries: 221`, `args: 38`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 659`, `planned_debt: 4`
* *Architecture:* `io: 1`, `api: 38`, `import: 14`
* *Defense:* `safety: 53`, `doc: 19`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.74
  * `Choke Point (Betweenness):` 3.2e-05 | `Ripple Effect (Closeness):` 0.030181
  * `Imports (Out-Degree: 11):` __future__, ast_serialize, librt.internal, metadata, mypy, mypy.cache, mypy.nodes, mypy.options...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mypy/fastparse.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.866)
- **Top Global Matches:** file_cluster_5: 7.866, file_cluster_12: 9.26, file_cluster_0: 10.797
- **Magnitude:** 2482.24 | **LOC:** 2257 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **18**; blast radius 0.931; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (78.5%)
- **Documentation Coverage:** 93.5018% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_func_def` **(Many-Argument Workhorses)** (Impact: 114.0)
  * `fix_function_overloads` **(Many-Argument Workhorses)** (Impact: 87.0)
  * `translate_stmt_list` **(Many-Argument Workhorses)** (Impact: 64.9)
  * `parse` **(Many-Argument Workhorses)** (Impact: 43.5)
  * `_check_ifstmt_for_overloads` **(Stateful Encapsulated Methods)** (Impact: 32.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 348 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 443`, `structural_boundaries: 407`, `args: 142`, `func_start: 141`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 54`, `high_risk_execution: 2`, `state_mutation: 454`, `planned_debt: 1`
* *Architecture:* `io: 8`, `api: 136`, `import: 19`
* *Defense:* `safety: 117`, `doc: 17`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.931
  * `Choke Point (Betweenness):` 0.000168 | `Ripple Effect (Closeness):` 0.038027
  * `Imports (Out-Degree: 14):` __future__, ast, collections.abc, mypy, mypy.errors, mypy.message_registry, mypy.nodes, mypy.options...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `mypy/subtypes.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.815)
- **Top Global Matches:** file_cluster_8: 7.815, file_cluster_6: 11.542, file_cluster_4: 19.781
- **Magnitude:** 2395.82 | **LOC:** 2319 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **20**; blast radius 2.154; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (80.1%), Complexity Load (formerly Cognitive Load) (75.1%), Guard Balance (formerly Safety Score) (63.0%)
- **Documentation Coverage:** 84.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `are_parameters_compatible` **(Many-Argument Workhorses)** (Impact: 170.9)
  * `visit_instance` **(Many-Argument Workhorses)** (Impact: 124.4)
  * `is_protocol_implementation` **(Many-Argument Workhorses)** (Impact: 103.9)
  * `find_node_type` **(Many-Argument Workhorses)** (Impact: 71.6)
  * `find_member` **(Many-Argument Workhorses)** (Impact: 69.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 230 instances
* *State Mutation (weighted view):* 719
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 628`, `structural_boundaries: 527`, `args: 64`, `func_start: 64`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 259`, `dead_code: 3`, `planned_debt: 21`, `fragile_debt: 1`
* *Architecture:* `api: 60`, `import: 21`
* *Defense:* `safety: 156`, `doc: 20`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.154
  * `Choke Point (Betweenness):` 0.002598 | `Ripple Effect (Closeness):` 0.078219
  * `Imports (Out-Degree: 19):` __future__, collections.abc, contextlib, mypy.applytype, mypy.checker_state, mypy.checkmember, mypy.constraints, mypy.erasetype...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `mypy/stubtest.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.676)
- **Top Global Matches:** file_cluster_6: 9.676, file_cluster_4: 12.013, file_cluster_5: 17.172
- **Magnitude:** 2353.34 | **LOC:** 2591 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 27.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **38**; blast radius 0.643; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.7%), Complexity Load (formerly Cognitive Load) (76.5%), Guard Balance (formerly Safety Score) (67.0%)
- **Documentation Coverage:** 83.913% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_verify_signature` **(Many-Argument Workhorses)** (Impact: 140.0)
  * `get_mypy_type_of_runtime_value` **(Defensive Guards)** (Impact: 84.5)
  * `verify_mypyfile` **(Many-Argument Workhorses)** (Impact: 79.5)
  * `verify_typeinfo` **(Many-Argument Workhorses)** (Impact: 72.3)
  * `test_stubs` **(Many-Argument Workhorses)** (Impact: 65.8)
    * *Intent:* """This is stubtest! It's time to test the stubs!"""
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 258 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 802
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 609`, `structural_boundaries: 479`, `args: 87`, `func_start: 86`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 67`, `high_risk_execution: 3`, `state_mutation: 286`, `planned_debt: 306`, `fragile_debt: 3`
* *Architecture:* `io: 19`, `api: 63`, `concurrency: 2`, `import: 45`
* *Defense:* `safety: 162`, `doc: 29`, `test: 2`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.643
  * `Choke Point (Betweenness):` 0.0002 | `Ripple Effect (Closeness):` 0.001431
  * `Imports (Out-Degree: 24):` __future__, argparse, collections, collections.abc, contextlib, copy, enum, functools...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mypy/stubgen.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.324)
- **Top Global Matches:** file_cluster_4: 8.324, file_cluster_6: 11.275, file_cluster_5: 12.093
- **Magnitude:** 2216.86 | **LOC:** 2056 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **32**; blast radius 0.643; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (78.2%), Guard Balance (formerly Safety Score) (71.0%), Connectivity (formerly Api Exposure) (59.5%)
- **Documentation Coverage:** 87.156% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `is_alias_expression` **(Defensive Guards)** (Impact: 64.7)
    * *Intent:* """Return True for things that look like target for an alias. Used to know if assignments look like ...
  * `_get_func_args` **(Many-Argument Workhorses)** (Impact: 61.2)
  * `get_str_default_of_node` **(Defensive Guards)** (Impact: 53.4)
    * *Intent:* """Get a string representation of the default value of a node. Returns a 2-tuple of the default and ...
  * `process_typeddict` **(Stateful Encapsulated Methods)** (Impact: 52.7)
  * `_get_func_return` **(Stateful Encapsulated Methods)** (Impact: 48.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 271 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 875
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 500`, `structural_boundaries: 389`, `args: 116`, `func_start: 116`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 1`, `state_mutation: 333`, `planned_debt: 16`
* *Architecture:* `io: 19`, `api: 108`, `concurrency: 3`, `import: 31`
* *Defense:* `safety: 106`, `doc: 29`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.643
  * `Choke Point (Betweenness):` 0.000179 | `Ripple Effect (Closeness):` 0.001431
  * `Imports (Out-Degree: 24):` __future__, and, argparse, collections.abc, is, keyword, mypy.build, mypy.errors...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mypy/constraints.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.886)
- **Top Global Matches:** file_cluster_6: 8.886, file_cluster_4: 11.023, file_cluster_5: 16.84
- **Magnitude:** 1822.96 | **LOC:** 1688 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **13**; blast radius 1.195; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (76.5%), Guard Balance (formerly Safety Score) (70.9%), Connectivity (formerly Api Exposure) (68.1%)
- **Documentation Coverage:** 77.0642% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visit_instance` **(Many-Argument Workhorses)** (Impact: 155.7)
    * *Intent:* # Non-leaf types
  * `infer_constraints_for_callable` **(Many-Argument Workhorses)** (Impact: 122.1)
  * `visit_callable_type` **(Many-Argument Workhorses)** (Impact: 77.3)
    * *Intent:* # Normalize callables before matching against each other. # Note that non-normalized callables can b...
  * `_infer_constraints` **(Many-Argument Workhorses)** (Impact: 72.4)
  * `build_constraints_for_simple_unpack` **(Many-Argument Workhorses)** (Impact: 54.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 256 instances
* *State Mutation (weighted view):* 810
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 405`, `structural_boundaries: 321`, `args: 54`, `func_start: 54`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 298`, `planned_debt: 15`, `fragile_debt: 4`
* *Architecture:* `api: 50`, `import: 13`
* *Defense:* `safety: 168`, `doc: 24`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.195
  * `Choke Point (Betweenness):` 0.000266 | `Ripple Effect (Closeness):` 0.065815
  * `Imports (Out-Degree: 12):` __future__, collections.abc, mypy.argmap, mypy.erasetype, mypy.infer, mypy.maptype, mypy.nodes, mypy.subtypes...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `mypy/checkmember.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.528)
- **Top Global Matches:** file_cluster_6: 8.528, file_cluster_8: 10.615, file_cluster_4: 15.968
- **Magnitude:** 1791.84 | **LOC:** 1589 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **15**; blast radius 0.762; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.2%), Guard Balance (formerly Safety Score) (68.2%)
- **Documentation Coverage:** 84.4156% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `analyze_class_attribute_access` **(Many-Argument Workhorses)** (Impact: 198.0)
  * `analyze_var` **(Many-Argument Workhorses)** (Impact: 134.4)
  * `analyze_member_var_access` **(Many-Argument Workhorses)** (Impact: 93.8)
  * `analyze_instance_member_access` **(Many-Argument Workhorses)** (Impact: 72.8)
    * *Intent:* # The several functions that follow implement analyze_member_access for various # types and aren't d...
  * `check_self_arg` **(Many-Argument Workhorses)** (Impact: 59.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 219 instances
* *State Mutation (weighted view):* 674
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 384`, `structural_boundaries: 254`, `args: 36`, `func_start: 36`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 236`, `dead_code: 2`, `planned_debt: 7`
* *Architecture:* `api: 35`, `import: 15`
* *Defense:* `safety: 131`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.762
  * `Choke Point (Betweenness):` 0.000299 | `Ripple Effect (Closeness):` 0.06543
  * `Imports (Out-Degree: 14):` __future__, collections.abc, mypy, mypy.checker_shared, mypy.erasetype, mypy.expandtype, mypy.maptype, mypy.meet...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `mypyc/codegen/emit.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.595)
- **Top Global Matches:** file_cluster_4: 7.595, file_cluster_0: 10.284, file_cluster_12: 11.202
- **Magnitude:** 1643.16 | **LOC:** 1440 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **16**; blast radius 1.015; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (77.6%), Complexity Load (formerly Cognitive Load) (65.5%)
- **Documentation Coverage:** 73.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emit_cast` **(Many-Argument Workhorses)** (Impact: 269.9)
  * `emit_unbox` **(Many-Argument Workhorses)** (Impact: 199.3)
  * `emit_box` **(Many-Argument Workhorses)** (Impact: 72.4)
  * `emit_dec_ref` **(Many-Argument Workhorses)** (Impact: 48.4)
    * *Intent:* # Otherwise assume it's an unboxed, pointerless value and do nothing.
  * `tuple_undefined_check_cond` **(Many-Argument Workhorses)** (Impact: 33.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 139 instances
* *State Mutation (weighted view):* 441
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 345`, `structural_boundaries: 189`, `args: 64`, `func_start: 64`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 163`, `planned_debt: 9`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 64`, `import: 16`
* *Defense:* `safety: 73`, `doc: 33`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.015
  * `Choke Point (Betweenness):` 0.000231 | `Ripple Effect (Closeness):` 0.010535
  * `Imports (Out-Degree: 13):` __future__, collections.abc, mypyc.codegen.cstring, mypyc.codegen.literals, mypyc.common, mypyc.ir.class_ir, mypyc.ir.func_ir, mypyc.ir.ops...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `mypyc/irbuild/builder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.725)
- **Top Global Matches:** file_cluster_5: 7.725, file_cluster_0: 7.922, file_cluster_12: 8.782
- **Magnitude:** 1475.1 | **LOC:** 1738 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **36**; blast radius 1.54; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.2%)
- **Documentation Coverage:** 78.125% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_assignment_target` **(Many-Argument Workhorses)** (Impact: 59.7)
  * `assign` **(Defensive Guards)** (Impact: 46.9)
  * `call_refexpr_with_args` **(Many-Argument Workhorses)** (Impact: 31.2)
  * `read` **(Defensive Guards)** (Impact: 26.2)
  * `get_dict_base_type_from_type` **(Defensive Guards)** (Impact: 22.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 152 instances
* *State Mutation (weighted view):* 558
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 418`, `args: 127`, `func_start: 126`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 254`, `planned_debt: 3`
* *Architecture:* `api: 129`, `import: 36`
* *Defense:* `safety: 105`, `doc: 38`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.54
  * `Choke Point (Betweenness):` 0.003637 | `Ripple Effect (Closeness):` 0.023844
  * `Imports (Out-Degree: 35):` __future__, collections.abc, contextlib, mypy.build, mypy.join, mypy.maptype, mypy.nodes, mypy.types...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `mypyc/irbuild/specialize.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.748)
- **Top Global Matches:** file_cluster_4: 7.748, file_cluster_6: 9.747, file_cluster_0: 13.384
- **Magnitude:** 1440.94 | **LOC:** 1549 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **25**; blast radius 0.666; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.2%), Connectivity (formerly Api Exposure) (66.0%)
- **Documentation Coverage:** 80.8696% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `translate_fstring` **(Defensive Guards)** (Impact: 63.2)
    * *Intent:* """Special case for f-string, which is translated into str.join() in mypy AST. This specializer opti...
  * `specialize_int_to_bytes` **(Many-Argument Workhorses)** (Impact: 59.4)
    * *Intent:* # int.to_bytes(length, byteorder, signed=False) if any(kind not in (ARG_POS, ARG_NAMED) for kind in ...
  * `translate_isinstance` **(Many-Argument Workhorses)** (Impact: 52.3)
    * *Intent:* """Special case for builtins.isinstance. Prevent coercions on the thing we are checking the instance...
  * `bytes_decode_fast_path` **(Many-Argument Workhorses)** (Impact: 50.9)
    * *Intent:* """Specialize common cases of obj.decode for most used encodings and strict errors."""
  * `str_encode_fast_path` **(Defensive Guards)** (Impact: 50.5)
    * *Intent:* """Specialize common cases of str.encode for most used encodings and strict errors."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 176 instances
* *State Mutation (weighted view):* 552
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 314`, `structural_boundaries: 285`, `args: 59`, `func_start: 57`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 200`, `planned_debt: 3`
* *Architecture:* `api: 56`, `import: 25`
* *Defense:* `safety: 66`, `doc: 27`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.666
  * `Choke Point (Betweenness):` 7.6e-05 | `Ripple Effect (Closeness):` 0.006979
  * `Imports (Out-Degree: 24):` __future__, collections.abc, mypy.nodes, mypy.types, mypyc.ir.ops, mypyc.ir.rtypes, mypyc.irbuild.builder, mypyc.irbuild.constant_fold...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mypy/errors.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.904)
- **Top Global Matches:** file_cluster_4: 8.904, file_cluster_5: 11.303, file_cluster_6: 11.954
- **Magnitude:** 1381.9 | **LOC:** 1472 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 53.8%
- **Blast Radius:** changing it is visible to **52** in-repo importer(s); it depends on **21**; blast radius 4.654; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (91.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.5%)
- **Documentation Coverage:** 58.1967% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `report` **(Many-Argument Workhorses)** (Impact: 83.0)
  * `add_error_info` **(Many-Argument Workhorses)** (Impact: 55.5)
  * `report_internal_error` **(Many-Argument Workhorses)** (Impact: 52.1)
  * `format_messages_default` **(Many-Argument Workhorses)** (Impact: 50.9)
  * `render_messages` **(Many-Argument Workhorses)** (Impact: 47.5)
    * *Intent:* """Translate the messages into a sequence of tuples. Each tuple is of form (path, line, col, severit...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 160 instances
* *State Mutation (weighted view):* 572
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 259`, `structural_boundaries: 236`, `args: 70`, `func_start: 66`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 252`, `planned_debt: 2`, `fragile_debt: 4`
* *Architecture:* `io: 10`, `api: 64`, `import: 21`
* *Defense:* `safety: 12`, `doc: 40`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.654
  * `Choke Point (Betweenness):` 0.002198 | `Ripple Effect (Closeness):` 0.131004
  * `Imports (Out-Degree: 17):` __future__, collections, collections.abc, itertools, librt.internal, mypy, mypy.cache, mypy.error_formatter...
  * `Imported By (In-Degree: 52):` (Excluded from Brief to save tokens)

### `mypyc/irbuild/expression.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.88)
- **Top Global Matches:** file_cluster_6: 7.88, file_cluster_4: 8.619, file_cluster_0: 15.587
- **Magnitude:** 1376.72 | **LOC:** 1303 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **28**; blast radius 0.708; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.3%), Complexity Load (formerly Cognitive Load) (67.9%)
- **Documentation Coverage:** 85.8491% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `try_specialize_in_expr` **(Many-Argument Workhorses)** (Impact: 60.2)
  * `translate_super_method_call` **(Many-Argument Workhorses)** (Impact: 59.5)
  * `transform_name_expr` **(Many-Argument Workhorses)** (Impact: 56.5)
    * *Intent:* # Name and attribute references
  * `translate_method_call` **(Defensive Guards)** (Impact: 44.9)
    * *Intent:* """Generate IR for an arbitrary call of form e.m(...). This can also deal with calls to module-level...
  * `transform_basic_comparison` **(Many-Argument Workhorses)** (Impact: 44.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 186 instances
* *State Mutation (weighted view):* 590
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 286`, `structural_boundaries: 286`, `args: 59`, `func_start: 53`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 218`, `planned_debt: 5`, `fragile_debt: 2`
* *Architecture:* `api: 48`, `import: 28`
* *Defense:* `safety: 72`, `doc: 13`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.708
  * `Choke Point (Betweenness):` 0.000228 | `Ripple Effect (Closeness):` 0.008608
  * `Imports (Out-Degree: 27):` __future__, collections.abc, math, mypy.nodes, mypy.types, mypyc.common, mypyc.ir.class_ir, mypyc.ir.func_ir...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mypy/meet.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.398)
- **Top Global Matches:** file_cluster_6: 8.398, file_cluster_4: 10.89, file_cluster_9: 17.432
- **Magnitude:** 1309.7 | **LOC:** 1276 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **10**; blast radius 1.156; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (77.2%), Complexity Load (formerly Cognitive Load) (70.0%), Guard Balance (formerly Safety Score) (50.3%)
- **Documentation Coverage:** 78.7234% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `is_overlapping_types` **(Many-Argument Workhorses)** (Impact: 231.3)
  * `narrow_declared_type` **(Defensive Guards)** (Impact: 84.2)
    * *Intent:* """Return the declared type narrowed down to another type."""
  * `visit_instance` **(Defensive Guards)** (Impact: 64.8)
  * `meet_tuples` **(Many-Argument Workhorses)** (Impact: 47.9)
    * *Intent:* """Meet two tuple types while handling variadic entries. This is surprisingly tricky, and we don't h...
  * `typed_dict_mapping_overlap` **(Defensive Guards)** (Impact: 39.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 112 instances
* *State Mutation (weighted view):* 356
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 382`, `structural_boundaries: 368`, `args: 47`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 132`, `dead_code: 1`, `planned_debt: 11`, `fragile_debt: 1`
* *Architecture:* `api: 46`, `import: 11`
* *Defense:* `safety: 187`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.156
  * `Choke Point (Betweenness):` 0.000196 | `Ripple Effect (Closeness):` 0.071483
  * `Imports (Out-Degree: 9):` __future__, collections.abc, mypy, mypy.erasetype, mypy.join, mypy.maptype, mypy.state, mypy.subtypes...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `mypyc/lib-rt/pythoncapi_compat.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.438)
- **Top Global Matches:** file_cluster_15: 6.438, file_cluster_12: 7.689, file_cluster_16: 8.405
- **Magnitude:** 1263.02 | **LOC:** 2595 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **4**; blast radius 7.077; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Connectivity (formerly Api Exposure) (83.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PyConfig_Get` **(Compute Cores)** (Impact: 39.3)
    * *Intent:* #endif #if 0x03080000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x030E0000 && !defined(PYPY_VERSION)
  * `PyObject_Vectorcall` **(Many-Argument Workhorses)** (Impact: 37.0)
    * *Intent:* #endif // gh-105922 added PyObject_Vectorcall() to Python 3.9.0a4 #if PY_VERSION_HEX < 0x030900A4
  * `_PyBytesWriter_Resize_impl` **(Many-Argument Workhorses)** (Impact: 22.3)
  * `PyDict_SetDefaultRef` **(Many-Argument Workhorses)** (Impact: 21.9)
    * *Intent:* #endif // gh-114329 added PyList_GetItemRef() to Python 3.13.0a4 #if PY_VERSION_HEX < 0x030D00A4
  * `PyTime_PerfCounter` **(Compute Cores)** (Impact: 21.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 136 instances
* *State Mutation (weighted view):* 421
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 464`, `args: 285`, `func_start: 136`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 149`
* *Architecture:* `io: 1`, `api: 97`, `import: 2`
* *Defense:* `safety: 17`, `immutability_locks: 60`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.077
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.02341
  * `Imports (Out-Degree: 0):` Python.h, frameobject.h, stddef.h, structmember.h
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `mypy/typeops.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.655)
- **Top Global Matches:** file_cluster_4: 9.655, file_cluster_6: 10.224, file_cluster_5: 14.386
- **Magnitude:** 1257.24 | **LOC:** 1345 | **CtrlFlow:** 39.9% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **30** in-repo importer(s); it depends on **16**; blast radius 2.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (84.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.3%)
- **Documentation Coverage:** 53.8462% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make_simplified_union` **(Many-Argument Workhorses)** (Impact: 65.3)
  * `bind_self` **(Many-Argument Workhorses)** (Impact: 56.3)
  * `type_object_type` **(Many-Argument Workhorses)** (Impact: 46.5)
    * *Intent:* """Return the type of a type object. For a generic type G with type variables T and S the type is ge...
  * `_remove_redundant_union_items` **(Many-Argument Workhorses)** (Impact: 45.4)
  * `false_only` **(Defensive Guards)** (Impact: 36.1)
    * *Intent:* """ Restricted version of t with only False-ish values """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 148 instances
* *State Mutation (weighted view):* 451
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 306`, `args: 52`, `func_start: 52`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 155`, `dead_code: 4`, `planned_debt: 10`
* *Architecture:* `api: 49`, `import: 18`
* *Defense:* `safety: 114`, `doc: 31`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.806
  * `Choke Point (Betweenness):` 0.001946 | `Ripple Effect (Closeness):` 0.082846
  * `Imports (Out-Degree: 14):` __future__, collections.abc, itertools, mypy.checker_state, mypy.copytype, mypy.expandtype, mypy.infer, mypy.maptype...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `mypyc/ir/ops.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.13)
- **Top Global Matches:** file_cluster_0: 7.13, file_cluster_5: 10.946, file_cluster_13: 11.375
- **Magnitude:** 1227.84 | **LOC:** 2107 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 63.6%
- **Blast Radius:** changing it is visible to **73** in-repo importer(s); it depends on **11**; blast radius 12.981; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 96.861% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 14.9)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 12.6)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 11.7)
  * `stolen` **(Defensive Guards)** (Impact: 10.2)
  * `stolen` **(Defensive Guards)** (Impact: 10.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 57 instances
* *State Mutation (weighted view):* 359
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 577`, `args: 250`, `func_start: 250`, `class_start: 54`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 245`, `planned_debt: 5`, `fragile_debt: 1`, `duplicate_logic: 75`
* *Architecture:* `api: 250`, `import: 11`
* *Defense:* `safety: 52`, `doc: 61`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.981
  * `Choke Point (Betweenness):` 0.001704 | `Ripple Effect (Closeness):` 0.110297
  * `Imports (Out-Degree: 10):` __future__, abc, collections.abc, mypy_extensions, mypyc.codegen.literals, mypyc.common, mypyc.ir.class_ir, mypyc.ir.deps...
  * `Imported By (In-Degree: 73):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `mypy/test/testformatter.py` (PYTHON) | Magnitude: 13.74 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 67, structural_boundaries: 30, safety: 17, core_var_decl: 9
- `mypy/find_sources.py` (PYTHON) | Magnitude: 210.42 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 127, structural_boundaries: 57, branch: 45, core_var_decl: 33
- `mypyc/irbuild/statement.py` (PYTHON) | Magnitude: 1136.12 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 926, core_var_decl: 214, design_snake_case: 208, state_mutation: 206

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `mypy/typevars.py` (PYTHON) | Magnitude: 43.86 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 21, core_var_decl: 11, design_snake_case: 10
- `mypyc/lib-rt/int_ops.c` (C) | Magnitude: 522.54 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 476, branch: 134, structural_boundaries: 98, pointers: 91
- `mypy/test/testpythoneval.py` (PYTHON) | Magnitude: 102.82 | Delta: **0.17** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 28, state_mutation: 25, core_var_decl: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `test-data/packages/typedpkg/typedpkg/sample.py` (PYTHON) | Magnitude: 2.66 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 4, args: 1, func_start: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `mypyc/lib-rt/base64/arch/ssse3/enc_loop.c` (C) | Magnitude: 41.7 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 42, pointers: 13, state_mutation: 9, structural_boundaries: 7
- `mypyc/lib-rt/base64/arch/avx512/enc_loop.c` (C) | Magnitude: 38.18 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 41, pointers: 13, state_mutation: 8, structural_boundaries: 7
- `mypyc/lib-rt/base64/arch/generic/32/enc_loop.c` (C) | Magnitude: 41.06 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 45, pointers: 17, state_mutation: 8, structural_boundaries: 7
- `mypyc/lib-rt/base64/arch/generic/64/enc_loop.c` (C) | Magnitude: 41.34 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 49, pointers: 21, state_mutation: 8, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `mypy/message_registry.py` (PYTHON) | Magnitude: 23.36 | Delta: **0.138** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: core_var_decl: 162, immutability_locks: 155, design_pascal_case: 154, structural_boundaries: 131

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `misc/docker/build.py` (PYTHON) | Magnitude: 27.48 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 18, state_mutation: 10, core_var_decl: 10, design_snake_case: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `mypyc/lib-rt/vecs/librt_vecs.h` (C) | Magnitude: 424.78 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 341, pointers: 295, structural_boundaries: 164, api: 160
- `mypy/exportjson.py` (PYTHON) | Magnitude: 371.3 | Delta: **0.175** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 453, structural_boundaries: 185, branch: 117, generics: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `mypy/types.py` (PYTHON) | Magnitude: 3787.24 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 2950, structural_boundaries: 1132, branch: 666, core_var_decl: 574
- `mypy/messages.py` (PYTHON) | Magnitude: 3619.46 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 2714, branch: 739, core_var_decl: 645, structural_boundaries: 643
- `mypyc/doc/conf.py` (PYTHON) | Magnitude: 25.3 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 10, core_var_decl: 9, design_snake_case: 9, structural_boundaries: 7
- `mypy/semanal_main.py` (PYTHON) | Magnitude: 404.04 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 288, structural_boundaries: 92, state_mutation: 74, core_var_decl: 73
- `mypy/split_namespace.py` (PYTHON) | Magnitude: 23.9 | Delta: **0.192** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 13, reflection_metaprogramming: 9, safety_bypasses: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `mypy/server/update.py` (PYTHON) | Magnitude: 1131.0 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 708, state_mutation: 200, branch: 184, core_var_decl: 164

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `mypy/checker.py` -> Churn: **100.0%** | Cog Load: 61.0449% | Debt: 14.4205%
- `mypy/build.py` -> Churn: **91.88%** | Cog Load: 53.8268% | Debt: 15.8347%
- `mypy/semanal.py` -> Churn: **81.27%** | Cog Load: 63.1844% | Debt: 13.5968%
- `mypy/checkexpr.py` -> Churn: **77.69%** | Cog Load: 57.6852% | Debt: 18.9287%
- `mypyc/codegen/emitmodule.py` -> Churn: **67.82%** | Cog Load: 52.6717% | Debt: 10.5035%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `mypy/nativeparse.py` -> **Ivan Levkivskyi** (83.3% isolated ownership) | Magnitude: 2799.46
- `mypy/stubgenc.py` -> **Marc Mueller** (100.0% isolated ownership) | Magnitude: 1219.3
- `mypy/plugins/attrs.py` -> **getzze** (100.0% isolated ownership) | Magnitude: 1166.22
- `mypy/join.py` -> **Shantanu** (100.0% isolated ownership) | Magnitude: 1007.9
- `mypy/suggestions.py` -> **Marc Mueller** (100.0% isolated ownership) | Magnitude: 990.6

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `mypy/build.py` -> **Severity: 1.015** (Bridge: 0.0101 * Flux: 100.0%)
- `mypy/dmypy_server.py` -> **Severity: 0.581** (Bridge: 0.0058 * Flux: 100.0%)
- `mypy/dmypy/client.py` -> **Severity: 0.575** (Bridge: 0.0058 * Flux: 99.9965%)
- `mypy/api.py` -> **Severity: 0.541** (Bridge: 0.0054 * Flux: 99.6316%)
- `mypy/nodes.py` -> **Severity: 0.464** (Bridge: 0.0046 * Flux: 99.9997%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `test-data/unit/lib-stub/typing.pyi` -> **Severity: 39.183** (Embedded: 0.4328 * Error Risk: 90.5265%)
- `mypyc/test-data/fixtures/ir.py` -> **Severity: 29.026** (Embedded: 0.3027 * Error Risk: 95.8764%)
- `mypy/util.py` -> **Severity: 15.933** (Embedded: 0.2101 * Error Risk: 75.8442%)
- `test-data/unit/fixtures/dataclasses.pyi` -> **Severity: 15.92** (Embedded: 0.1726 * Error Risk: 92.2171%)
- `mypy/options.py` -> **Severity: 15.886** (Embedded: 0.1952 * Error Risk: 81.3679%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `test-data/unit/lib-stub/typing.pyi` -> **Severity: 14179.4** (Blast Radius: 141.794 * Doc Risk: 100.0%)
- `mypyc/test-data/fixtures/ir.py` -> **Severity: 3364.3** (Blast Radius: 33.643 * Doc Risk: 100.0%)
- `test-data/unit/lib-stub/_typeshed.pyi` -> **Severity: 1888.8** (Blast Radius: 18.888 * Doc Risk: 100.0%)
- `mypy/nodes.py` -> **Severity: 1700.064** (Blast Radius: 18.254 * Doc Risk: 93.1338%)
- `mypy/types.py` -> **Severity: 1583.747** (Blast Radius: 17.019 * Doc Risk: 93.0576%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 377 literal sites + 51 sites through wrappers = 428
- **`panics_and_aborts`:** 753 literal sites + 45 sites through wrappers = 798

- `CPyError_OutOfMemory` (function, debug_prints, primitive): 20 call sites in 4 files -- `mypyc/lib-rt/exc_ops.c`
- `CPyError_OutOfMemory` (function, panics_and_aborts, primitive): 20 call sites in 4 files -- `mypyc/lib-rt/exc_ops.c`
- `fail` (function, panics_and_aborts, primitive): 10 call sites in 1 files -- `mypy/main.py`
- `fail` (function, debug_prints, primitive): 8 call sites in 1 files -- `mypy/dmypy/client.py`
- `fail` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `mypy/dmypy/client.py`
- `print_offset` (function, debug_prints, primitive): 5 call sites in 1 files -- `misc/incremental_checker.py`
- `heading` (function, debug_prints, primitive): 4 call sites in 1 files -- `misc/perf_compare.py`
- `report` (function, debug_prints, primitive): 3 call sites in 1 files -- `misc/perf_checker.py`
- `error_callback` (function, debug_prints, primitive): 2 call sites in 1 files -- `mypy/stubtest.py`
- `error_callback` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `mypy/stubtest.py`
- `fail` (function, debug_prints, primitive): 2 call sites in 1 files -- `mypyc/lib-rt/test_capi.cc`
- `fail` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `mypyc/build.py`
*(+7 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 33883 call pairs -- scoped 54.1%, unique 0.6%, ambiguous 29.5%, external 15.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 30330 | 58.1% | 0.0% | 32.9% | 9.1% |
| c | 2876 | 19.2% | 6.7% | 0.4% | 73.7% |
| cpp | 656 | 25.8% | 1.5% | 0.0% | 72.7% |
| shell | 21 | 4.8% | 0.0% | 0.0% | 95.2% |

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
