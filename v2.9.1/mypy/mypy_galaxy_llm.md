# ARCHITECTURAL_BRIEF: mypy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/python/mypy.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1401 analyzed artifact(s), 216100 LOC.
- **Load-bearing artifact:** `mypy/typeshed/stdlib/collections/abc.pyi` -- 450 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `mypy/build.py` -- pulls in 91 dependencies, the widest assembly point in the scan.
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
| Analyzed Artifacts (Scanned) | 1401 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 465 |
| Total LOC | 216100 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 75.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5467 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3431 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 8.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.7745 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 57 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 1245 | 190678 | 88.9% |
| C | 104 | 18230 | 7.4% |
| PLAINTEXT | 15 | 0 | 1.1% |
| CPP | 12 | 6915 | 0.9% |
| MARKDOWN | 10 | 0 | 0.7% |
| SHELL | 6 | 76 | 0.4% |
| XML | 3 | 0 | 0.2% |
| YAML | 1 | 75 | 0.1% |
| DOCKERFILE | 1 | 8 | 0.1% |
| CSS | 1 | 70 | 0.1% |
| MAKEFILE | 1 | 9 | 0.1% |
| BATCH | 1 | 26 | 0.1% |
| M4 | 1 | 13 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `1.955`
> **Composition Archetype:** `Hub-Coupled App` (z +1.96; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 61%, Data / Markup / Trivial 18%, Declarative / Non-Code 6%, Large Core Modules (2) 5%, Many-Argument Workhorses Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1376 | 98.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 25 | 1.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 465*

**Composition by Extension & Reason:**
- `.test`: 261x Excluded (Unsupported Extension: '.test')
- `.rst`: 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 22x Excluded (Unsupported Extension: '.rst')
- `.pyi`: 3x Packed Payload Guard (Impossible Density: 4.02 hits/line), 2x Packed Payload Guard (Impossible Density: 3.16 hits/line), 2x Packed Payload Guard (Impossible Density: 4.03 hits/line)
- `.h`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Hex Payload: 8192 hex tokens in 1032 LOC)
- `.typed`: 15x Excluded (Unsupported Extension: '.typed')
- `no_extension`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 62 LOC)
- `.md`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4772 LOC)
- `.yml`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.patch`: 8x Excluded (Unsupported Extension: '.patch')
- `.py`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 211 LOC), 1x Excluded (Machine-Generated Source Code Signature: 60 LOC)
- `.pump`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 3x Excluded (Unsupported Extension: '.ini')
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 76 LOC)
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.1 | 15.9 | 5.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 53.4 | 63.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 35.9 | 10.7 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 18.9 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 31.7 | 12.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 31.4 | 13.3 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 91.7 | 1.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.1 | 0.8 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 78.6 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 7770 | 333 | 6 | `mypyc/external/googletest/src/gtest.cc` |
| cleanup | 49 | 24 | 0 | `mypyc/external/googletest/src/gtest-death-test.cc` |
| guards | 17984 | 794 | 28 | `mypy/checker.py` |
| danger | 8626 | 648 | 15 | `mypy/typeshed/stdlib/tkinter/__init__.pyi` |
| concurrency | 1900 | 233 | 2 | `mypy/test/teststubtest.py` |
| connectivity | 26300 | 1167 | 45 | `mypy/typeshed/stdlib/tkinter/__init__.pyi` |
| io | 4162 | 450 | 8 | `mypy/typeshed/stdlib/ast.pyi` |
| crypto | 27 | 21 | 0 | `mypy/typeshed/stdlib/ssl.pyi` |
| ipc | 209 | 51 | 0 | `misc/sync-typeshed.py` |
| time | 187 | 27 | 0 | `mypy/build.py` |
| serialization | 7 | 6 | 0 | `mypy/evalexpr.py` |
| regex | 148 | 43 | 0 | `misc/gen_blog_post_html.py` |
| events | 167 | 72 | 0 | `mypy/typeshed/stdlib/asyncio/events.pyi` |
| tests | 1243 | 84 | 0 | `mypyc/lib-rt/test_capi.cc` |
| docs | 3235 | 299 | 4 | `mypy/test/teststubtest.py` |
| debt | 4840 | 408 | 7 | `mypy/test/teststubtest.py` |
| mutation | 72728 | 1096 | 106 | `mypy/checker.py` |
| dead_code | 3267 | 607 | 5 | `mypy/test/testtypes.py` |
| credential | 1 | 1 | 0 | `misc/sync-typeshed.py` |
| threat | 2744 | 350 | 4 | `mypy/typeshed/stdlib/builtins.pyi` |
| ml_ai | 39 | 10 | 0 | `mypy/stubtest.py` |
| ui | 13 | 2 | 0 | `mypy/typeshed/stdlib/tkinter/__init__.pyi` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.2727**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `mypy/typeshed/stdlib/ast.pyi` (Hits: 236)
- `mypy/typeshed/stdlib/os/__init__.pyi` (Hits: 168)
- `mypy/typeshed/stdlib/socket.pyi` (Hits: 142)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **abc.pyi** (`mypy/typeshed/stdlib/collections/abc.pyi`) — 450 inbound connections
2. **sys.pyi** (`test-data/unit/lib-stub/sys.pyi`) — 400 inbound connections
3. **_typeshed.pyi** (`test-data/unit/lib-stub/_typeshed.pyi`) — 386 inbound connections
4. **__future__.pyi** (`mypy/typeshed/stdlib/__future__.pyi`) — 340 inbound connections
5. **nodes.py** (`mypy/nodes.py`) — 133 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **build.py** (`mypy/build.py`) — 91 outbound dependencies
2. **semanal.py** (`mypy/semanal.py`) — 55 outbound dependencies
3. **checker.py** (`mypy/checker.py`) — 50 outbound dependencies
4. **checkexpr.py** (`mypy/checkexpr.py`) — 45 outbound dependencies
5. **emitmodule.py** (`mypyc/codegen/emitmodule.py`) — 44 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `vgetargskeywords` **(Many-Argument Workhorses)** (@ `mypyc/lib-rt/getargs.c`) -> Impact: **289.7** | LOC: 343
  * *Intent:* #define IS_END_OF_FORMAT(c) (c == '\0' || c == ';' || c == ':')
- `vgetargskeywordsfast_impl` **(Many-Argument Workhorses)** (@ `mypyc/lib-rt/getargsfast.c`) -> Impact: **273.1** | LOC: 276
- `emit_cast` **(Many-Argument Workhorses)** (@ `mypyc/codegen/emit.py`) -> Impact: **269.9** | LOC: 224
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
| `mypy` | 114 | 95241.48 | 43.2% | 17.55% |
| `mypy/typeshed/stdlib` | 233 | 25963.88 | 12.9% | 48.22% |
| `mypyc/irbuild` | 28 | 15713.88 | 45.92% | 19.77% |
| `mypyc/lib-rt` | 37 | 7934.48 | 32.97% | 38.63% |
| `mypy/test` | 46 | 7797.56 | 19.61% | 0.0% |
| `mypyc/codegen` | 8 | 5932.78 | 48.24% | 8.01% |
| `mypy/plugins` | 11 | 4072.3 | 38.52% | 17.99% |
| `mypyc/ir` | 8 | 3757.98 | 45.02% | 28.91% |
| `mypy/typeshed/stdlib/tkinter` | 12 | 3706.82 | 1.73% | 54.43% |
| `mypy/server` | 11 | 3572.44 | 41.67% | 12.42% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `mypy/typeshed/stdlib/_blake2.pyi` -> **100.0%** Exposure
- `mypy/typeshed/stdlib/_csv.pyi` -> **100.0%** Exposure
- `mypy/typeshed/stdlib/_ctypes.pyi` -> **100.0%** Exposure
- `mypy/typeshed/stdlib/_frozen_importlib.pyi` -> **100.0%** Exposure
- `mypy/typeshed/stdlib/_frozen_importlib_external.pyi` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `misc/analyze_cache.py` -> **100.0%** Exposure
- `misc/apply-cache-diff.py` -> **100.0%** Exposure
- `misc/diff-cache.py` -> **100.0%** Exposure
- `misc/docker/build.py` -> **100.0%** Exposure
- `misc/gen_blog_post_html.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `mypy/typeshed/stdlib/builtins.pyi` -> **0** Orphaned Functions | **213** Duplicates
- `mypy/typeshed/stdlib/collections/__init__.pyi` -> **74** Orphaned Functions | **60** Duplicates
- `mypy/test/testtypes.py` -> **92** Orphaned Functions | **13** Duplicates
- `mypy/typeshed/stdlib/ast.pyi` -> **0** Orphaned Functions | **100** Duplicates
- `mypy/test/teststubgen.py` -> **83** Orphaned Functions | **15** Duplicates

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
- **Unknown Dependencies:** `6925` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `mypy/checker.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 9936.38 | **LOC:** 9583 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 54.2%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **50**; blast radius 0.471; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (89.8%), Connectivity (formerly Api Exposure) (85.5%)
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
* *Risk/State:* `safety_bypasses: 100`, `state_mutation: 1323`, `dead_code: 25`, `planned_debt: 69`, `fragile_debt: 9`
* *Architecture:* `api: 331`, `concurrency: 2`, `import: 47`
* *Defense:* `safety: 689`, `doc: 167`, `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.000626 | `Ripple Effect (Closeness):` 0.018169
  * `Imports (Out-Degree: 44):` __future__, collections, collections.abc, contextlib, cycle, itertools, mypy, mypy.binder...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `mypy/semanal.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 9310.16 | **LOC:** 8436 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 37.8%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **55**; blast radius 0.467; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.8%), Connectivity (formerly Api Exposure) (84.8%)
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
* *Risk/State:* `safety_bypasses: 69`, `state_mutation: 1344`, `dead_code: 19`, `planned_debt: 41`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 338`, `concurrency: 5`, `import: 34`
* *Defense:* `safety: 639`, `doc: 138`, `test: 2`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.467
  * `Choke Point (Betweenness):` 0.001069 | `Ripple Effect (Closeness):` 0.025403
  * `Imports (Out-Degree: 32):` X, Y, __future__, adds, b, bar, climbs, collections.abc...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `mypy/checkexpr.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 6998.18 | **LOC:** 6998 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 46.4%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **45**; blast radius 0.336; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.8%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.5%)
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
* *Risk/State:* `safety_bypasses: 78`, `state_mutation: 912`, `dead_code: 26`, `planned_debt: 36`, `fragile_debt: 5`, `duplicate_logic: 4`
* *Architecture:* `api: 211`, `import: 43`
* *Defense:* `safety: 483`, `doc: 128`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.336
  * `Choke Point (Betweenness):` 0.000122 | `Ripple Effect (Closeness):` 0.015625
  * `Imports (Out-Degree: 38):` __future__, collections, collections.abc, contextlib, cycles., enum, it, itertools...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `mypy/build.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4313.3 | **LOC:** 4822 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 57.7%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **91**; blast radius 0.601; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (92.5%), Connectivity (formerly Api Exposure) (90.7%)
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
* *Risk/State:* `safety_bypasses: 104`, `high_risk_execution: 2`, `state_mutation: 694`, `dead_code: 6`, `planned_debt: 35`, `fragile_debt: 6`
* *Architecture:* `io: 58`, `api: 157`, `import: 68`
* *Defense:* `safety: 132`, `doc: 89`, `immutability_locks: 23`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.601
  * `Choke Point (Betweenness):` 0.004136 | `Ripple Effect (Closeness):` 0.021344
  * `Imports (Out-Degree: 53):` A, B, P, X, __future__, an, and, at...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `mypy/types.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 3787.24 | **LOC:** 4453 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 31.8%
- **Blast Radius:** changing it is visible to **125** in-repo importer(s); it depends on **17**; blast radius 8.392; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.5%), Debt Markers (formerly Tech Debt) (77.5%)
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
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 515`, `dead_code: 4`, `planned_debt: 16`, `fragile_debt: 3`, `duplicate_logic: 26`
* *Architecture:* `io: 1`, `api: 337`, `import: 16`
* *Defense:* `safety: 189`, `doc: 65`, `immutability_locks: 103`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.392
  * `Choke Point (Betweenness):` 0.002142 | `Ripple Effect (Closeness):` 0.107527
  * `Imports (Out-Degree: 12):` __future__, abc, collections.abc, is, librt.internal, mypy.bogus_type, mypy.cache, mypy.expandtype...
  * `Imported By (In-Degree: 125):` (Excluded from Brief to save tokens)

### `mypy/messages.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 3619.46 | **LOC:** 3428 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 31.6%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **21**; blast radius 1.018; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.8%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 391`, `dead_code: 2`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `api: 190`, `concurrency: 3`, `import: 21`
* *Defense:* `safety: 126`, `doc: 47`, `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.018
  * `Choke Point (Betweenness):` 0.001461 | `Ripple Effect (Closeness):` 0.066035
  * `Imports (Out-Degree: 18):` __future__, collections.abc, context., contextlib, difflib, itertools, mypy, mypy.erasetype...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `mypy/nodes.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 3197.56 | **LOC:** 5368 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **133** in-repo importer(s); it depends on **25**; blast radius 9.301; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.5%), Debt Markers (formerly Tech Debt) (83.7%)
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
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 838`, `dead_code: 15`, `planned_debt: 25`, `fragile_debt: 4`, `duplicate_logic: 32`
* *Architecture:* `io: 1`, `api: 336`, `import: 17`
* *Defense:* `safety: 123`, `doc: 101`, `immutability_locks: 136`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.301
  * `Choke Point (Betweenness):` 0.002226 | `Ripple Effect (Closeness):` 0.110664
  * `Imports (Out-Degree: 11):` ..., __future__, a.b.c, abc, collections, collections.abc, contextlib, cycle...
  * `Imported By (In-Degree: 133):` (Excluded from Brief to save tokens)

### `mypyc/irbuild/ll_builder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3193.88 | **LOC:** 3067 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 64.3%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **32**; blast radius 1.274; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.6%), Connectivity (formerly Api Exposure) (83.9%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 463`, `dead_code: 5`, `planned_debt: 17`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 119`, `import: 32`
* *Defense:* `safety: 107`, `doc: 77`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.274
  * `Choke Point (Betweenness):` 0.001652 | `Ripple Effect (Closeness):` 0.021956
  * `Imports (Out-Degree: 31):` __future__, collections.abc, mypy.argmap, mypy.nodes, mypy.operators, mypy.types, mypyc.common, mypyc.errors...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `mypy/typeanal.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2963.24 | **LOC:** 2804 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 23.1%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **22**; blast radius 0.404; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.4%), Connectivity (formerly Api Exposure) (84.4%), Complexity Load (formerly Cognitive Load) (83.7%)
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
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 411`, `dead_code: 2`, `planned_debt: 24`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 128`, `import: 20`
* *Defense:* `safety: 163`, `doc: 25`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.404
  * `Choke Point (Betweenness):` 3.4e-05 | `Ripple Effect (Closeness):` 0.021384
  * `Imports (Out-Degree: 18):` __future__, collections.abc, contextlib, cycle, itertools, mypy, mypy.errorcodes, mypy.errors...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `mypy/nativeparse.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2799.46 | **LOC:** 2095 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **18**; blast radius 0.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (64.6%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.01495
  * `Imports (Out-Degree: 11):` , __future__, ast_serialize, dependencies, librt.internal, metadata, mypy, mypy.cache...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mypy/typeshed/stdlib/tkinter/__init__.pyi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2652.54 | **LOC:** 4185 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.305; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Debt Markers (formerly Tech Debt) (98.5%), Guard Balance (formerly Safety Score) (80.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 10.3)
  * `configure` **(Many-Argument Workhorses)** (Impact: 10.0)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 9.9)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 9.8)
  * `configure` **(Many-Argument Workhorses)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 225
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 778`, `args: 684`, `func_start: 684`, `class_start: 56`
* *Risk/State:* `safety_bypasses: 241`, `high_risk_execution: 1`, `state_mutation: 189`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 70`
* *Architecture:* `io: 28`, `api: 686`, `import: 11`
* *Defense:* `sync_locks: 8`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.305
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` _tkinter, _typeshed, collections.abc, enum, sys, tkinter, tkinter.constants, tkinter.font...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mypy/fastparse.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2482.24 | **LOC:** 2257 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 26.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **18**; blast radius 0.423; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.5%), Complexity Load (formerly Cognitive Load) (83.5%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `safety_bypasses: 54`, `high_risk_execution: 2`, `state_mutation: 454`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `io: 8`, `api: 136`, `import: 19`
* *Defense:* `safety: 117`, `doc: 17`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.423
  * `Choke Point (Betweenness):` 0.000132 | `Ripple Effect (Closeness):` 0.020861
  * `Imports (Out-Degree: 17):` __future__, ast, collections.abc, mypy, mypy.errors, mypy.message_registry, mypy.nodes, mypy.options...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `mypy/subtypes.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 2395.82 | **LOC:** 2319 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **20**; blast radius 1.129; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.3%), Connectivity (formerly Api Exposure) (80.1%), Complexity Load (formerly Cognitive Load) (75.1%)
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
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 259`, `dead_code: 7`, `planned_debt: 21`, `fragile_debt: 1`
* *Architecture:* `api: 60`, `import: 21`
* *Defense:* `safety: 156`, `doc: 20`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.129
  * `Choke Point (Betweenness):` 0.001518 | `Ripple Effect (Closeness):` 0.066099
  * `Imports (Out-Degree: 18):` __future__, collections.abc, contextlib, mypy.applytype, mypy.checker_state, mypy.checkmember, mypy.constraints, mypy.erasetype...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `mypy/stubtest.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2353.34 | **LOC:** 2591 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 30.8%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **39**; blast radius 0.319; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.7%), Guard Balance (formerly Safety Score) (89.4%), Complexity Load (formerly Cognitive Load) (76.5%)
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
* *Risk/State:* `safety_bypasses: 67`, `high_risk_execution: 3`, `state_mutation: 286`, `dead_code: 3`, `planned_debt: 306`, `fragile_debt: 3`
* *Architecture:* `io: 19`, `api: 63`, `concurrency: 2`, `import: 45`
* *Defense:* `safety: 162`, `doc: 29`, `test: 2`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.319
  * `Choke Point (Betweenness):` 8.1e-05 | `Ripple Effect (Closeness):` 0.000693
  * `Imports (Out-Degree: 30):` __future__, argparse, collections, collections.abc, contextlib, copy, enum, functools...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mypy/stubgen.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2216.86 | **LOC:** 2056 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **36**; blast radius 0.321; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.7%), Complexity Load (formerly Cognitive Load) (78.2%), Connectivity (formerly Api Exposure) (59.5%)
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
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 1`, `state_mutation: 333`, `dead_code: 1`, `planned_debt: 16`
* *Architecture:* `io: 19`, `api: 108`, `concurrency: 3`, `import: 31`
* *Defense:* `safety: 106`, `doc: 29`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.321
  * `Choke Point (Betweenness):` 6.3e-05 | `Ripple Effect (Closeness):` 0.000693
  * `Imports (Out-Degree: 27):` __future__, and, argparse, collections.abc, from, is, keyword, mypy.build...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mypy/typeshed/stdlib/builtins.pyi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2151.74 | **LOC:** 2227 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.305; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (88.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__new__` **(Generic / Templated Code)** (Impact: 4.0)
  * `__new__` **(Generic / Templated Code)** (Impact: 3.8)
  * `__new__` **(Generic / Templated Code)** (Impact: 3.8)
  * `__new__` **(Generic / Templated Code)** (Impact: 3.6)
  * `open` **(Generic / Templated Code)** (Impact: 3.5)
    * *Intent:* # Text mode: always returns a TextIOWrapper
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 1017`, `args: 839`, `func_start: 839`, `class_start: 110`
* *Risk/State:* `safety_bypasses: 192`, `high_risk_execution: 5`, `state_mutation: 36`, `dead_code: 6`, `planned_debt: 5`, `fragile_debt: 3`, `duplicate_logic: 213`
* *Architecture:* `io: 60`, `api: 508`, `concurrency: 1`, `import: 16`
* *Defense:* `safety: 3`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.305
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` _ast, _collections_abc, _sitebuiltins, _typeshed, collections.abc, io, os, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mypy/constraints.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1822.96 | **LOC:** 1688 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **13**; blast radius 0.567; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.6%), Complexity Load (formerly Cognitive Load) (76.5%), Connectivity (formerly Api Exposure) (68.1%)
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
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 298`, `dead_code: 2`, `planned_debt: 15`, `fragile_debt: 4`
* *Architecture:* `api: 50`, `import: 13`
* *Defense:* `safety: 168`, `doc: 24`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.567
  * `Choke Point (Betweenness):` 0.000121 | `Ripple Effect (Closeness):` 0.052242
  * `Imports (Out-Degree: 12):` __future__, collections.abc, mypy.argmap, mypy.erasetype, mypy.infer, mypy.maptype, mypy.nodes, mypy.subtypes...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `mypy/checkmember.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1791.84 | **LOC:** 1589 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **15**; blast radius 0.388; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.2%)
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
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 236`, `dead_code: 4`, `planned_debt: 7`
* *Architecture:* `api: 35`, `import: 15`
* *Defense:* `safety: 131`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.000151 | `Ripple Effect (Closeness):` 0.052082
  * `Imports (Out-Degree: 14):` __future__, collections.abc, mypy, mypy.checker_shared, mypy.erasetype, mypy.expandtype, mypy.maptype, mypy.meet...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `mypyc/codegen/emit.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1643.16 | **LOC:** 1440 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **16**; blast radius 0.492; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.6%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (77.6%)
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
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 163`, `dead_code: 1`, `planned_debt: 9`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 64`, `import: 16`
* *Defense:* `safety: 73`, `doc: 33`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.492
  * `Choke Point (Betweenness):` 0.000154 | `Ripple Effect (Closeness):` 0.005099
  * `Imports (Out-Degree: 14):` __future__, collections.abc, mypyc.codegen.cstring, mypyc.codegen.literals, mypyc.common, mypyc.ir.class_ir, mypyc.ir.func_ir, mypyc.ir.ops...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `mypy/typeshed/stdlib/ast.pyi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1479.16 | **LOC:** 2100 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **10**; blast radius 0.807; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (95.2%), Guard Balance (formerly Safety Score) (92.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Generic / Templated Code)** (Impact: 3.8)
  * `__replace__` **(Generic / Templated Code)** (Impact: 3.8)
  * `__init__` **(Generic / Templated Code)** (Impact: 3.8)
  * `__replace__` **(Generic / Templated Code)** (Impact: 3.8)
  * `__init__` **(Generic / Templated Code)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 278`, `structural_boundaries: 576`, `args: 400`, `func_start: 400`, `class_start: 144`
* *Risk/State:* `safety_bypasses: 139`, `high_risk_execution: 16`, `state_mutation: 88`, `planned_debt: 1`, `duplicate_logic: 100`
* *Architecture:* `io: 236`, `api: 298`, `import: 12`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.807
  * `Choke Point (Betweenness):` 5.1e-05 | `Ripple Effect (Closeness):` 0.040079
  * `Imports (Out-Degree: 4):` _ast, _typeshed, ast, builtins, collections.abc, os, sys, types...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `mypyc/irbuild/builder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1475.1 | **LOC:** 1738 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 35.3%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **39**; blast radius 0.762; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.9%), Test Surface (formerly Verification) (80.0%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.762
  * `Choke Point (Betweenness):` 0.001317 | `Ripple Effect (Closeness):` 0.012316
  * `Imports (Out-Degree: 35):` __future__, collections.abc, contextlib, machinery, mypy.build, mypy.join, mypy.maptype, mypy.nodes...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `mypyc/irbuild/specialize.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1440.94 | **LOC:** 1549 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 35.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **25**; blast radius 0.333; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (66.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.333
  * `Choke Point (Betweenness):` 5.5e-05 | `Ripple Effect (Closeness):` 0.00431
  * `Imports (Out-Degree: 24):` __future__, collections.abc, mypy.nodes, mypy.types, mypyc.ir.ops, mypyc.ir.rtypes, mypyc.irbuild.builder, mypyc.irbuild.constant_fold...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mypyc/lib-rt/pythoncapi_compat.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 1435.92 | **LOC:** 2595 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **4**; blast radius 1.915; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.5%), Complexity Load (formerly Cognitive Load) (40.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PyConfig_Get` **(Compute Cores)** (Impact: 53.5)
    * *Intent:* #endif #if 0x03080000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x030E0000 && !defined(PYPY_VERSION)
  * `PyObject_Vectorcall` **(Many-Argument Workhorses)** (Impact: 43.7)
    * *Intent:* #endif // gh-105922 added PyObject_Vectorcall() to Python 3.9.0a4 #if PY_VERSION_HEX < 0x030900A4
  * `PyDict_Pop` **(Stateful Encapsulated Methods)** (Impact: 28.1)
    * *Intent:* #endif // gh-111262 added PyDict_Pop() and PyDict_PopString() to Python 3.13.0a2 #if PY_VERSION_HEX ...
  * `PyTime_PerfCounter` **(Stateful Encapsulated Methods)** (Impact: 26.0)
  * `PyUnicode_EqualToUTF8AndSize` **(Many-Argument Workhorses)** (Impact: 25.1)
    * *Intent:* #endif // gh-110289 added PyUnicode_EqualToUTF8() and PyUnicode_EqualToUTF8AndSize() // to Python 3....
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 143 instances
* *State Mutation (weighted view):* 435
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 474`, `structural_boundaries: 308`, `args: 274`, `func_start: 136`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 149`
* *Architecture:* `io: 1`, `api: 105`, `import: 4`
* *Defense:* `safety: 31`, `immutability_locks: 60`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00831
  * `Imports (Out-Degree: 0):` Python.h, frameobject.h, stddef.h, structmember.h
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `mypy/errors.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1381.9 | **LOC:** 1472 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 46.7%
- **Blast Radius:** changing it is visible to **52** in-repo importer(s); it depends on **24**; blast radius 2.326; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.3%), Connectivity (formerly Api Exposure) (91.6%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 252`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 4`
* *Architecture:* `io: 10`, `api: 64`, `import: 21`
* *Defense:* `safety: 12`, `doc: 40`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.326
  * `Choke Point (Betweenness):` 0.002142 | `Ripple Effect (Closeness):` 0.069887
  * `Imports (Out-Degree: 18):` __future__, collections, collections.abc, context, context., if, itertools, librt.internal...
  * `Imported By (In-Degree: 52):` (Excluded from Brief to save tokens)

### `mypyc/irbuild/expression.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1376.72 | **LOC:** 1303 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 23.1%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **28**; blast radius 0.355; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.9%)
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
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 218`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 2`
* *Architecture:* `api: 48`, `import: 28`
* *Defense:* `safety: 72`, `doc: 13`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.355
  * `Choke Point (Betweenness):` 5.7e-05 | `Ripple Effect (Closeness):` 0.004885
  * `Imports (Out-Degree: 27):` __future__, collections.abc, math, mypy.nodes, mypy.types, mypyc.common, mypyc.ir.class_ir, mypyc.ir.func_ir...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `mypy/checker.py` -> Churn: **100.0%** | Cog Load: 61.0449% | Debt: 14.5132%
- `mypy/build.py` -> Churn: **92.54%** | Cog Load: 53.8268% | Debt: 16.0444%
- `mypy/semanal.py` -> Churn: **84.78%** | Cog Load: 63.1844% | Debt: 13.739%
- `mypy/checkexpr.py` -> Churn: **78.48%** | Cog Load: 57.6852% | Debt: 19.1556%
- `mypyc/codegen/emitmodule.py` -> Churn: **70.41%** | Cog Load: 52.6717% | Debt: 10.9934%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `mypy/nativeparse.py` -> **Ivan Levkivskyi** (83.3% isolated ownership) | Magnitude: 2799.46
- `mypy/typeshed/stdlib/ast.pyi` -> **Marc Mueller** (100.0% isolated ownership) | Magnitude: 1479.16
- `mypyc/lib-rt/pythoncapi_compat.h` -> **Shantanu** (100.0% isolated ownership) | Magnitude: 1435.92
- `mypy/plugins/attrs.py` -> **getzze** (100.0% isolated ownership) | Magnitude: 1166.22
- `mypy/server/deps.py` -> **David Foster** (100.0% isolated ownership) | Magnitude: 1093.12

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `mypy/util.py` -> **Severity: 0.648** (Bridge: 0.0065 * Flux: 100.0%)
- `mypy/build.py` -> **Severity: 0.414** (Bridge: 0.0041 * Flux: 100.0%)
- `mypy/plugins/ctypes.py` -> **Severity: 0.367** (Bridge: 0.0037 * Flux: 100.0%)
- `mypy/nodes.py` -> **Severity: 0.223** (Bridge: 0.0022 * Flux: 99.9997%)
- `mypy/errors.py` -> **Severity: 0.214** (Bridge: 0.0021 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `mypy/typeshed/stdlib/collections/abc.pyi` -> **Severity: 24.882** (Embedded: 0.3854 * Error Risk: 64.5656%)
- `test-data/unit/lib-stub/_typeshed.pyi` -> **Severity: 22.219** (Embedded: 0.3016 * Error Risk: 73.6639%)
- `test-data/unit/lib-stub/sys.pyi` -> **Severity: 21.688** (Embedded: 0.3466 * Error Risk: 62.5811%)
- `mypy/typeshed/stdlib/_collections_abc.pyi` -> **Severity: 15.574** (Embedded: 0.2326 * Error Risk: 66.9491%)
- `mypy/typeshed/stdlib/__future__.pyi` -> **Severity: 14.079** (Embedded: 0.2325 * Error Risk: 60.5532%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `test-data/unit/lib-stub/_typeshed.pyi` -> **Severity: 6434.3** (Blast Radius: 64.343 * Doc Risk: 100.0%)
- `mypy/typeshed/stdlib/_collections_abc.pyi` -> **Severity: 5404.5** (Blast Radius: 54.045 * Doc Risk: 100.0%)
- `mypy/typeshed/stdlib/__future__.pyi` -> **Severity: 3637.1** (Blast Radius: 36.371 * Doc Risk: 100.0%)
- `mypy/nodes.py` -> **Severity: 866.237** (Blast Radius: 9.301 * Doc Risk: 93.1338%)
- `mypy/typeshed/stdlib/re.pyi` -> **Severity: 826.9** (Blast Radius: 8.269 * Doc Risk: 100.0%)

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
