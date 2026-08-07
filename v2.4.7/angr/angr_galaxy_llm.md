# ARCHITECTURAL_BRIEF: angr
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/angr` |
| **Timestamp** | `2026-08-07T03:46:44.464596+00:00` |
| **Scan Duration** | `7.81s` |
| **Git Branch** | `master` |
| **Git Commit** | `ac1ad40678a32222344f788c7f74378bc213e50a` |
| **Git Remote** | `https://github.com/angr/angr.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1418 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 1930 |
| Analyzed Artifacts (Scanned) | 1748 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 182 |
| Total LOC | 219765 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 90.6% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5445 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.245 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.2696 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 95 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 1393 | 191855 | 79.7% |
| JSON | 322 | 24792 | 18.4% |
| RUST | 15 | 2165 | 0.9% |
| PROTO | 5 | 296 | 0.3% |
| SHELL | 5 | 657 | 0.3% |
| PLAINTEXT | 4 | 0 | 0.2% |
| MARKDOWN | 4 | 0 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.709`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 936 | 53.5% |
| file_cluster_13 | 726 | 41.5% |
| file_cluster_0 | 34 | 1.9% |
| file_cluster_16 | 30 | 1.7% |
| file_cluster_17 | 6 | 0.3% |
| file_cluster_4 | 4 | 0.2% |
| file_cluster_11 | 1 | 0.1% |
| file_cluster_6 | 1 | 0.1% |
| file_cluster_7 | 1 | 0.1% |
| file_cluster_12 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 8 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 182*

**Composition by Extension & Reason:**
- `.rst`: 50x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 3523 LOC), 1x Excluded (Embedded Array/Matrix Payload: 6009 commas in 813 LOC)
- `.py`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 27 exceeds 500 chars), 2x Excluded (Saturation: Line 26 exceeds 500 chars)
- `.h`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Binary Format Detected)
- `.pickle`: 6x Excluded (Unsupported Extension: '.pickle')
- `.pyi`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 2x Unsupported Format (.toml), 1x Excluded (Unsupported Extension: '.toml')
- `.c`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cpp`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.bat`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 14.5 | 7.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.7 | 26.1 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 19.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 16.7 | 2.3 | 2.3 |
| API Exposure | 0.0 | 12.8 | 2.8 | 2.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 26.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 93.0 | 1.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 89.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.2 | 0.8 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 85.0 | 8.0 | 7.9 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 45.3 | 42.6 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/analyses/decompiler/test_decompiler.py` (Hits: 220)
- `corpus_tests/scripts/snapshot_diff.sh` (Hits: 72)
- `corpus_tests/scripts/gh_ls.sh` (Hits: 65)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **logging.py** (`angr/concretization_strategies/logging.py`) — 433 inbound connections
2. **common.py** (`tests/common.py`) — 180 inbound connections
3. **errors.py** (`angr/errors.py`) — 147 inbound connections
4. **expression.py** (`angr/ailment/expression.py`) — 139 inbound connections
5. **statement.py** (`angr/ailment/statement.py`) — 86 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`angr/analyses/decompiler/peephole_optimizations/__init__.py`) — 63 outbound dependencies
2. **__init__.py** (`angr/analyses/__init__.py`) — 52 outbound dependencies
3. **analysis.py** (`angr/analyses/analysis.py`) — 48 outbound dependencies
4. **clinic.py** (`angr/analyses/decompiler/clinic.py`) — 47 outbound dependencies
5. **__init__.py** (`angr/analyses/decompiler/optimization_passes/__init__.py`) — 41 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_match_acyclic_schemas` (@ `angr/analyses/decompiler/structuring/phoenix.py`) -> Impact: **1336.6** | LOC: 1911
- `_unify_local_variables` (@ `angr/analyses/decompiler/ail_simplifier.py`) -> Impact: **715.4** | LOC: 1213
- `_generate_cfgnode` (@ `angr/analyses/cfg/cfg_fast.py`) -> Impact: **662.1** | LOC: 842
- `_load_native` (@ `angr/state_plugins/unicorn_engine.py`) -> Impact: **568.7** | LOC: 1502
- `_analyze` (@ `angr/analyses/decompiler/optimization_passes/lowered_switch_simplifier.py`) -> Impact: **506.7** | LOC: 711
- `test_decompiling_nl_i386_pie` (@ `tests/analyses/decompiler/test_decompiler.py`) -> Impact: **495.3** | LOC: 2770
  * *Intent:* # Current decompilation output: # do # { # v1 = v0 + 1; # v3 = v2 + 1; # *(v2) = *(v0); # v0 = v1; # v2 = v3; # We can improve it by re-arranging the ...
- `_try_resolve_single_constant_loads` (@ `angr/analyses/cfg/indirect_jump_resolvers/jumptable.py`) -> Impact: **476.9** | LOC: 858
- `_analyze_cyclic` (@ `angr/analyses/decompiler/structuring/phoenix.py`) -> Impact: **463.2** | LOC: 880
  * *Intent:* # we could not make a loop after the last cycle refinement. restore the graph l.debug("Could not structure the cyclic graph. Restoring the region to t...
- `make_operations` (@ `angr/engines/vex/claripy/irop.py`) -> Impact: **455.6** | LOC: 1041
- `_analyze` (@ `angr/analyses/decompiler/optimization_passes/duplication_reverter/duplication_reverter.py`) -> Impact: **449.6** | LOC: 816
  * *Intent:* # Main Analysis # def _analyze(self, cache=None) -> bool: """

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `angr/analyses` | 36 | 11644.9 | 35.77% | 63.64% |
| `angr` | 31 | 9333.38 | 29.96% | 38.86% |
| `angr/analyses/decompiler` | 28 | 8127.78 | 27.25% | 14.96% |
| `angr/state_plugins` | 29 | 6482.6 | 33.62% | 35.64% |
| `angr/analyses/decompiler/optimization_passes` | 39 | 6239.84 | 25.82% | 27.43% |
| `angr/analyses/cfg` | 10 | 6140.6 | 26.12% | 22.75% |
| `angr/procedures/definitions/win32` | 310 | 5117.82 | 6.04% | 0.0% |
| `angr/analyses/decompiler/peephole_optimizations` | 62 | 4722.69 | 19.19% | 4.84% |
| `angr/analyses/decompiler/structuring` | 7 | 4410.22 | 30.29% | 38.62% |
| `angr/ailment` | 12 | 3537.02 | 27.57% | 41.82% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `angr/ailment/block_walker.py` -> **100.0%** Exposure
- `angr/ailment/expression.py` -> **100.0%** Exposure
- `angr/ailment/manager.py` -> **100.0%** Exposure
- `angr/ailment/statement.py` -> **100.0%** Exposure
- `angr/analyses/decompiler/goto_manager.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `angr/analyses/decompiler/counters/seq_cf_structure_counter.py` -> **100.0%** Exposure
- `angr/analyses/decompiler/region_walker.py` -> **100.0%** Exposure
- `angr/analyses/decompiler/ssailification/rewriting_state.py` -> **100.0%** Exposure
- `angr/analyses/decompiler/ssailification/traversal_state.py` -> **100.0%** Exposure
- `angr/analyses/reaching_definitions/subject.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `angr/ailment/expression.py` -> **0** Orphaned Functions | **112** Duplicates
- `angr/ailment/statement.py` -> **0** Orphaned Functions | **98** Duplicates
- `angr/calling_conventions.py` -> **0** Orphaned Functions | **92** Duplicates
- `angr/engines/pcode/behavior.py` -> **0** Orphaned Functions | **91** Duplicates
- `angr/ailment/block_walker.py` -> **0** Orphaned Functions | **87** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`native/angr/src/icicle.rs`** -> AI Confidence: **99.48%**
2. **`angr/analyses/cfg/cfg_fast.py`** -> AI Confidence: **99.39%**
3. **`angr/analyses/decompiler/optimization_passes/lowered_switch_simplifier.py`** -> AI Confidence: **99.39%**
4. **`angr/analyses/decompiler/optimization_passes/win_stack_canary_simplifier.py`** -> AI Confidence: **99.39%**
5. **`angr/analyses/decompiler/structuring/phoenix.py`** -> AI Confidence: **99.39%**
6. **`angr/analyses/variable_recovery/engine_base.py`** -> AI Confidence: **99.39%**
7. **`angr/engines/vex/lifter.py`** -> AI Confidence: **99.39%**
8. **`angr/analyses/typehoon/simple_solver.py`** -> AI Confidence: **99.35%**
9. **`angr/storage/memory_mixins/paged_memory/pages/list_page.py`** -> AI Confidence: **99.34%**
10. **`angr/__main__.py`** -> AI Confidence: **99.31%**
11. **`angr/analyses/backward_slice.py`** -> AI Confidence: **99.31%**
12. **`angr/analyses/binary_optimizer.py`** -> AI Confidence: **99.31%**
13. **`angr/analyses/bindiff.py`** -> AI Confidence: **99.31%**
14. **`angr/analyses/calling_convention/calling_convention.py`** -> AI Confidence: **99.31%**
15. **`angr/analyses/calling_convention/fact_collector.py`** -> AI Confidence: **99.31%**
16. **`angr/analyses/cfg/cfb.py`** -> AI Confidence: **99.31%**
17. **`angr/analyses/cfg/cfg_base.py`** -> AI Confidence: **99.31%**
18. **`angr/analyses/cfg/cfg_emulated.py`** -> AI Confidence: **99.31%**
19. **`angr/analyses/cfg/cfg_fast_soot.py`** -> AI Confidence: **99.31%**
20. **`angr/analyses/cfg/indirect_jump_resolvers/const_resolver.py`** -> AI Confidence: **99.31%**
21. **`angr/analyses/cfg/indirect_jump_resolvers/jumptable.py`** -> AI Confidence: **99.31%**
22. **`angr/analyses/complete_calling_conventions.py`** -> AI Confidence: **99.31%**
23. **`angr/analyses/ddg.py`** -> AI Confidence: **99.31%**
24. **`angr/analyses/decompiler/ail_simplifier.py`** -> AI Confidence: **99.31%**
25. **`angr/analyses/decompiler/block_simplifier.py`** -> AI Confidence: **99.31%**
26. **`angr/analyses/decompiler/callsite_maker.py`** -> AI Confidence: **99.31%**
27. **`angr/analyses/decompiler/clinic.py`** -> AI Confidence: **99.31%**
28. **`angr/analyses/decompiler/condition_processor.py`** -> AI Confidence: **99.31%**
29. **`angr/analyses/decompiler/decompiler.py`** -> AI Confidence: **99.31%**
30. **`angr/analyses/decompiler/dephication/graph_vvar_mapping.py`** -> AI Confidence: **99.31%**
31. **`angr/analyses/decompiler/dephication/rewriting_engine.py`** -> AI Confidence: **99.31%**
32. **`angr/analyses/decompiler/empty_node_remover.py`** -> AI Confidence: **99.31%**
33. **`angr/analyses/decompiler/expression_narrower.py`** -> AI Confidence: **99.31%**
34. **`angr/analyses/decompiler/graph_region.py`** -> AI Confidence: **99.31%**
35. **`angr/analyses/decompiler/optimization_passes/code_motion.py`** -> AI Confidence: **99.31%**
36. **`angr/analyses/decompiler/optimization_passes/condition_constprop.py`** -> AI Confidence: **99.31%**
37. **`angr/analyses/decompiler/optimization_passes/const_prop_reverter.py`** -> AI Confidence: **99.31%**
38. **`angr/analyses/decompiler/optimization_passes/duplication_reverter/ail_merge_graph.py`** -> AI Confidence: **99.31%**
39. **`angr/analyses/decompiler/optimization_passes/duplication_reverter/duplication_reverter.py`** -> AI Confidence: **99.31%**
40. **`angr/analyses/decompiler/optimization_passes/duplication_reverter/similarity.py`** -> AI Confidence: **99.31%**
41. **`angr/analyses/decompiler/optimization_passes/duplication_reverter/utils.py`** -> AI Confidence: **99.31%**
42. **`angr/analyses/decompiler/optimization_passes/eager_std_string_eval.py`** -> AI Confidence: **99.31%**
43. **`angr/analyses/decompiler/optimization_passes/inlined_string_transformation_simplifier.py`** -> AI Confidence: **99.31%**
44. **`angr/analyses/decompiler/optimization_passes/inlined_strlen_simplifier.py`** -> AI Confidence: **99.31%**
45. **`angr/analyses/decompiler/optimization_passes/ite_region_converter.py`** -> AI Confidence: **99.31%**
46. **`angr/analyses/decompiler/optimization_passes/optimization_pass.py`** -> AI Confidence: **99.31%**
47. **`angr/analyses/decompiler/optimization_passes/register_save_area_simplifier.py`** -> AI Confidence: **99.31%**
48. **`angr/analyses/decompiler/optimization_passes/register_save_area_simplifier_adv.py`** -> AI Confidence: **99.31%**
49. **`angr/analyses/decompiler/optimization_passes/ret_deduplicator.py`** -> AI Confidence: **99.31%**
50. **`angr/analyses/decompiler/optimization_passes/return_duplicator_base.py`** -> AI Confidence: **99.31%**
51. **`angr/analyses/decompiler/optimization_passes/stack_canary_simplifier.py`** -> AI Confidence: **99.31%**
52. **`angr/analyses/decompiler/optimization_passes/static_vvar_rewriter.py`** -> AI Confidence: **99.31%**
53. **`angr/analyses/decompiler/optimization_passes/switch_default_case_duplicator.py`** -> AI Confidence: **99.31%**
54. **`angr/analyses/decompiler/peephole_optimizations/inlined_memset.py`** -> AI Confidence: **99.31%**
55. **`angr/analyses/decompiler/peephole_optimizations/inlined_strcpy.py`** -> AI Confidence: **99.31%**
56. **`angr/analyses/decompiler/peephole_optimizations/inlined_strcpy_consolidation.py`** -> AI Confidence: **99.31%**
57. **`angr/analyses/decompiler/peephole_optimizations/inlined_wcscpy.py`** -> AI Confidence: **99.31%**
58. **`angr/analyses/decompiler/peephole_optimizations/inlined_wcscpy_consolidation.py`** -> AI Confidence: **99.31%**
59. **`angr/analyses/decompiler/region_identifier.py`** -> AI Confidence: **99.31%**
60. **`angr/analyses/decompiler/region_simplifiers/expr_folding.py`** -> AI Confidence: **99.31%**
61. **`angr/analyses/decompiler/region_simplifiers/goto.py`** -> AI Confidence: **99.31%**
62. **`angr/analyses/decompiler/region_simplifiers/loop.py`** -> AI Confidence: **99.31%**
63. **`angr/analyses/decompiler/region_simplifiers/switch_cluster_simplifier.py`** -> AI Confidence: **99.31%**
64. **`angr/analyses/decompiler/semantic_naming/boolean_naming.py`** -> AI Confidence: **99.31%**
65. **`angr/analyses/decompiler/semantic_naming/pointer_naming.py`** -> AI Confidence: **99.31%**
66. **`angr/analyses/decompiler/ssailification/rewriting.py`** -> AI Confidence: **99.31%**
67. **`angr/analyses/decompiler/ssailification/rewriting_engine.py`** -> AI Confidence: **99.31%**
68. **`angr/analyses/decompiler/ssailification/ssailification.py`** -> AI Confidence: **99.31%**
69. **`angr/analyses/decompiler/ssailification/traversal_engine.py`** -> AI Confidence: **99.31%**
70. **`angr/analyses/decompiler/ssailification/traversal_state.py`** -> AI Confidence: **99.31%**
71. **`angr/analyses/decompiler/structuring/dream.py`** -> AI Confidence: **99.31%**
72. **`angr/analyses/decompiler/structuring/structurer_base.py`** -> AI Confidence: **99.31%**
73. **`angr/analyses/decompiler/utils.py`** -> AI Confidence: **99.31%**
74. **`angr/analyses/deobfuscator/api_obf_finder.py`** -> AI Confidence: **99.31%**
75. **`angr/analyses/deobfuscator/data_transformation_embedder.py`** -> AI Confidence: **99.31%**
76. **`angr/analyses/deobfuscator/hash_lookup_api_deobfuscator.py`** -> AI Confidence: **99.31%**
77. **`angr/analyses/deobfuscator/string_obf_finder.py`** -> AI Confidence: **99.31%**
78. **`angr/analyses/deobfuscator/string_obf_opt_passes.py`** -> AI Confidence: **99.31%**
79. **`angr/analyses/disassembly.py`** -> AI Confidence: **99.31%**
80. **`angr/analyses/fcp/fcp.py`** -> AI Confidence: **99.31%**
81. **`angr/analyses/find_objects_static.py`** -> AI Confidence: **99.31%**
82. **`angr/analyses/flirt/flirt.py`** -> AI Confidence: **99.31%**
83. **`angr/analyses/flirt/flirt_sig.py`** -> AI Confidence: **99.31%**
84. **`angr/analyses/identifier/identify.py`** -> AI Confidence: **99.31%**
85. **`angr/analyses/identifier/runner.py`** -> AI Confidence: **99.31%**
86. **`angr/analyses/language_detector.py`** -> AI Confidence: **99.31%**
87. **`angr/analyses/loop_unroller/loop_unroller.py`** -> AI Confidence: **99.31%**
88. **`angr/analyses/outliner/outliner.py`** -> AI Confidence: **99.31%**
89. **`angr/analyses/patchfinder.py`** -> AI Confidence: **99.31%**
90. **`angr/analyses/pathfinder.py`** -> AI Confidence: **99.31%**
91. **`angr/analyses/propagator/propagator.py`** -> AI Confidence: **99.31%**
92. **`angr/analyses/proximity_graph.py`** -> AI Confidence: **99.31%**
93. **`angr/analyses/reaching_definitions/engine_ail.py`** -> AI Confidence: **99.31%**
94. **`angr/analyses/reaching_definitions/engine_vex.py`** -> AI Confidence: **99.31%**
95. **`angr/analyses/reaching_definitions/function_handler.py`** -> AI Confidence: **99.31%**
96. **`angr/analyses/reaching_definitions/reaching_definitions.py`** -> AI Confidence: **99.31%**
97. **`angr/analyses/reassembler.py`** -> AI Confidence: **99.31%**
98. **`angr/analyses/s_liveness.py`** -> AI Confidence: **99.31%**
99. **`angr/analyses/s_propagator.py`** -> AI Confidence: **99.31%**
100. **`angr/analyses/s_reaching_definitions/s_rda_view.py`** -> AI Confidence: **99.31%**
101. **`angr/analyses/s_reaching_definitions/s_reaching_definitions.py`** -> AI Confidence: **99.31%**
102. **`angr/analyses/stack_pointer_tracker.py`** -> AI Confidence: **99.31%**
103. **`angr/analyses/typehoon/typehoon.py`** -> AI Confidence: **99.31%**
104. **`angr/analyses/unpacker/packing_detector.py`** -> AI Confidence: **99.31%**
105. **`angr/analyses/variable_recovery/engine_ail.py`** -> AI Confidence: **99.31%**
106. **`angr/analyses/variable_recovery/variable_recovery_fast.py`** -> AI Confidence: **99.31%**
107. **`angr/analyses/veritesting.py`** -> AI Confidence: **99.31%**
108. **`angr/analyses/vfg.py`** -> AI Confidence: **99.31%**
109. **`angr/angrdb/serializers/structured_code.py`** -> AI Confidence: **99.31%**
110. **`angr/blade.py`** -> AI Confidence: **99.31%**
111. **`angr/calling_conventions.py`** -> AI Confidence: **99.31%**
112. **`angr/distributed/server.py`** -> AI Confidence: **99.31%**
113. **`angr/engines/icicle.py`** -> AI Confidence: **99.31%**
114. **`angr/engines/pcode/lifter.py`** -> AI Confidence: **99.31%**
115. **`angr/engines/successors.py`** -> AI Confidence: **99.31%**
116. **`angr/engines/unicorn.py`** -> AI Confidence: **99.31%**
117. **`angr/engines/vex/claripy/irop.py`** -> AI Confidence: **99.31%**
118. **`angr/engines/vex/heavy/heavy.py`** -> AI Confidence: **99.31%**
119. **`angr/exploration_techniques/explorer.py`** -> AI Confidence: **99.31%**
120. **`angr/exploration_techniques/suggestions.py`** -> AI Confidence: **99.31%**
121. **`angr/flirt/build_sig.py`** -> AI Confidence: **99.31%**
122. **`angr/knowledge_plugins/cfg/cfg_model.py`** -> AI Confidence: **99.31%**
123. **`angr/knowledge_plugins/cfg/cfg_node.py`** -> AI Confidence: **99.31%**
124. **`angr/knowledge_plugins/functions/function.py`** -> AI Confidence: **99.31%**
125. **`angr/knowledge_plugins/functions/function_parser.py`** -> AI Confidence: **99.31%**
126. **`angr/knowledge_plugins/key_definitions/definition.py`** -> AI Confidence: **99.31%**
127. **`angr/knowledge_plugins/key_definitions/live_definitions.py`** -> AI Confidence: **99.31%**
128. **`angr/knowledge_plugins/key_definitions/liveness.py`** -> AI Confidence: **99.31%**
129. **`angr/knowledge_plugins/key_definitions/rd_model.py`** -> AI Confidence: **99.31%**
130. **`angr/knowledge_plugins/propagations/propagation_model.py`** -> AI Confidence: **99.31%**
131. **`angr/knowledge_plugins/variables/variable_manager.py`** -> AI Confidence: **99.31%**
132. **`angr/mcp/server.py`** -> AI Confidence: **99.31%**
133. **`angr/misc/autoimport.py`** -> AI Confidence: **99.31%**
134. **`angr/procedures/definitions/parse_win32json.py`** -> AI Confidence: **99.31%**
135. **`angr/procedures/java_jni/__init__.py`** -> AI Confidence: **99.31%**
136. **`angr/procedures/libc/strlen.py`** -> AI Confidence: **99.31%**
137. **`angr/procedures/stubs/format_parser.py`** -> AI Confidence: **99.31%**
138. **`angr/project.py`** -> AI Confidence: **99.31%**
139. **`angr/sim_manager.py`** -> AI Confidence: **99.31%**
140. **`angr/sim_procedure.py`** -> AI Confidence: **99.31%**
141. **`angr/sim_state.py`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `7202` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `angr/analyses/disassembly.py` (PYTHON) -> Cumulative Risk: **691.69**
- **Archetype:** `file_cluster_13` (Distance: 13.15 IQR)
- **Magnitude:** 1211.6 | **LOC:** 1351 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Tech Debt (99.9433%), Documentation (92.8944%)
- **Heaviest Functions:** `__init__` (Impact: 239.1), `_render` (Impact: 68.1), `format_comment` (Impact: 63.6)

### 2. `angr/state_plugins/trace_additions.py` (PYTHON) -> Cumulative Risk: **686.27**
- **Archetype:** `file_cluster_0` (Distance: 12.019 IQR)
- **Magnitude:** 550.96 | **LOC:** 738 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9981%), State Flux (99.9888%)
- **Heaviest Functions:** `atoi_dumps` (Impact: 119.7), `generic_info_hook` (Impact: 29.5), `get_possible_len` (Impact: 20.9)

### 3. `angr/ailment/expression.py` (PYTHON) -> Cumulative Risk: **677.03**
- **Archetype:** `file_cluster_0` (Distance: 13.045 IQR)
- **Magnitude:** 1748.36 | **LOC:** 2015 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9988%), Documentation (94.5617%)
- **Heaviest Functions:** `__str__` (Impact: 267.9), `has_atom` (Impact: 37.0), `replace` (Impact: 35.7)

### 4. `angr/distributed/server.py` (PYTHON) -> Cumulative Risk: **671.83**
- **Archetype:** `file_cluster_13` (Distance: 11.517 IQR)
- **Magnitude:** 136.3 | **LOC:** 197 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Concurrency (99.0162%)
- **Heaviest Functions:** `run` (Impact: 25.1), `on_worker_exit` (Impact: 6.5), `inc_active_workers` (Impact: 3.6)

### 5. `angr/knowledge_plugins/cfg/spilling_cfg.py` (PYTHON) -> Cumulative Risk: **664.83**
- **Archetype:** `file_cluster_16` (Distance: 12.259 IQR)
- **Magnitude:** 686.52 | **LOC:** 1183 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.7404%), Documentation (98.0016%), Verification (80.0%)
- **Heaviest Functions:** `_load_from_lmdb_core` (Impact: 286.3), `copy` (Impact: 15.5), `_evict_n` (Impact: 15.4)

### 6. `angr/knowledge_plugins/cfg/cfg_node.py` (PYTHON) -> Cumulative Risk: **660.3**
- **Archetype:** `file_cluster_0` (Distance: 11.909 IQR)
- **Magnitude:** 477.04 | **LOC:** 761 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9999%), State Flux (99.9742%)
- **Heaviest Functions:** `parse_from_cmessage` (Impact: 50.6), `serialize_to_cmessage` (Impact: 30.6), `parse_from_cmessage` (Impact: 27.0)

### 7. `angr/knowledge_plugins/cfg/spilling_digraph.py` (PYTHON) -> Cumulative Risk: **650.11**
- **Archetype:** `file_cluster_13` (Distance: 11.664 IQR)
- **Magnitude:** 378.36 | **LOC:** 598 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.8893%), State Flux (96.3677%), Concurrency (84.7018%)
- **Heaviest Functions:** `_deserialize_inner_dict` (Impact: 30.4), `_serialize_inner_dict` (Impact: 23.2), `_load_from_lmdb_core` (Impact: 18.9)

### 8. `angr/analyses/typehoon/typevars.py` (PYTHON) -> Cumulative Risk: **642.51**
- **Archetype:** `file_cluster_13` (Distance: 12.14 IQR)
- **Magnitude:** 498.32 | **LOC:** 634 | **CtrlFlow:** 38.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9434%)
- **Heaviest Functions:** `replace` (Impact: 34.5), `replace` (Impact: 34.5), `replace` (Impact: 27.3)

### 9. `angr/sim_variable.py` (PYTHON) -> Cumulative Risk: **636.29**
- **Archetype:** `file_cluster_0` (Distance: 12.307 IQR)
- **Magnitude:** 351.16 | **LOC:** 498 | **CtrlFlow:** 33.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9944%)
- **Heaviest Functions:** `loc_repr` (Impact: 39.4), `loc_repr` (Impact: 34.5), `serialize_to_cmessage` (Impact: 13.4)

### 10. `angr/analyses/identifier/functions/fdprintf.py` (PYTHON) -> Cumulative Risk: **631.39**
- **Archetype:** `file_cluster_8` (Distance: 10.063 IQR)
- **Magnitude:** 104.22 | **LOC:** 123 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.1476%), Tech Debt (96.1917%)
- **Heaviest Functions:** `pre_test` (Impact: 60.0), `rand_str` (Impact: 8.2), `__init__` (Impact: 2.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `angr/analyses/cfg/cfg_fast.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.056 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.214 IQR)
- **Top Global Matches:** file_cluster_8: 13.056, file_cluster_13: 13.115, file_cluster_7: 13.216
- **Magnitude:** 2935.88 | **LOC:** 5547 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 84.6%
- **Risk Profile:** Cognitive Load (28.2336%), Tech Debt (35.291%)
**Top Internal Functions/Classes:**
  * `_generate_cfgnode` (Impact: 662.1)
  * `_load_a_byte_as_int` (Impact: 331.6)
  * `_job_queue_empty` (Impact: 170.7)
  * `_remove_redundant_overlapping_blocks` (Impact: 135.6)
  * `_func_addrs_from_prologues` (Impact: 96.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1255`, `structural_boundaries: 528`, `args: 130`, `func_start: 125`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 381`, `dead_code: 26`, `planned_debt: 17`, `fragile_debt: 11`, `duplicate_logic: 8`
* *Architecture:* `api: 42`, `import: 41`
* *Defense:* `safety: 107`, `doc: 316`, `test: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.647
  * `Choke Point (Betweenness):` 0.003796 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` cle, claripy, pyvex, angr.misc.ux, archinfo.arch_arm, .cfg_base, logging, angr.knowledge_plugins.cfg.spilling_cfg...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `angr/analyses/decompiler/structuring/phoenix.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.848 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.531 IQR)
- **Top Global Matches:** file_cluster_8: 11.848, file_cluster_17: 12.053, file_cluster_13: 12.118
- **Magnitude:** 2492.26 | **LOC:** 3648 | **CtrlFlow:** 70.8% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (44.0756%), Tech Debt (13.7754%)
**Top Internal Functions/Classes:**
  * `_match_acyclic_schemas` (Impact: 1336.6)
  * `_analyze_cyclic` (Impact: 463.2)
    * *Intent:* # we could not make a loop after the last cycle refinement. restore the graph l.debug("Could not str...
  * `_analyze` (Impact: 52.3)
  * `_refine_cyclic_determine_loop_body` (Impact: 41.7)
  * `_remove_first_statement_if_jump` (Impact: 38.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1027`, `structural_boundaries: 423`, `args: 86`, `func_start: 72`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 126`, `dead_code: 14`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 11`, `import: 22`
* *Defense:* `safety: 166`, `doc: 28`, `test: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.211
  * `Choke Point (Betweenness):` 0.003491 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` angr.ailment.statement, claripy, logging, typing, enum, angr.utils.constants, angr.analyses.decompiler.sequence_walker, angr.utils.graph...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `angr/analyses/reassembler.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.311 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.826 IQR)
- **Top Global Matches:** file_cluster_13: 13.311, file_cluster_8: 13.376, file_cluster_0: 13.411
- **Magnitude:** 2244.3 | **LOC:** 2905 | **CtrlFlow:** 63.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (48.2685%), Tech Debt (99.8788%)
**Top Internal Functions/Classes:**
  * `assembly` (Impact: 280.2)
  * `_initialize` (Impact: 129.7)
  * `_cgc_extended_application_handler` (Impact: 124.1)
  * `__repr__` (Impact: 116.0)
  * `new_label` (Impact: 74.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 630`, `structural_boundaries: 369`, `args: 117`, `func_start: 107`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 608`, `dead_code: 5`, `planned_debt: 10`, `fragile_debt: 3`, `duplicate_logic: 39`
* *Architecture:* `api: 92`, `import: 22`
* *Defense:* `safety: 21`, `doc: 230`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.345
  * `Choke Point (Betweenness):` 0.004952 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` cle, pyvex, angr.knowledge_plugins.cfg.memory_data, .cfg.cfg_fast, logging, typing, angr.knowledge_base, ...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `angr/sim_type.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.404 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.68 IQR)
- **Top Global Matches:** file_cluster_8: 12.404, file_cluster_0: 12.408, file_cluster_16: 12.534
- **Magnitude:** 2118.76 | **LOC:** 4480 | **CtrlFlow:** 47.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (25.7842%), Tech Debt (99.9306%)
**Top Internal Functions/Classes:**
  * `alignment` (Impact: 421.5)
  * `extract` (Impact: 318.5)
  * `store` (Impact: 190.7)
  * `c_repr` (Impact: 46.1)
  * `c_repr` (Impact: 46.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 788`, `structural_boundaries: 857`, `args: 322`, `func_start: 317`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 65`, `high_risk_execution: 7`, `state_mutation: 313`, `dead_code: 5`, `planned_debt: 18`, `fragile_debt: 14`, `duplicate_logic: 77`
* *Architecture:* `api: 223`, `import: 21`
* *Defense:* `safety: 145`, `doc: 181`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 22.24
  * `Choke Point (Betweenness):` 0.018958 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` angr.procedures.definitions, claripy, cxxheaderparser.simple, pycparser, logging, typing, enum, angr.sim_state...
  * `Imported By (In-Degree: 80):` (Excluded from Brief to save tokens)

### `angr/calling_conventions.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.716 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.187 IQR)
- **Top Global Matches:** file_cluster_0: 12.716, file_cluster_11: 12.772, file_cluster_17: 12.865
- **Magnitude:** 1865.4 | **LOC:** 2808 | **CtrlFlow:** 52.3% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (40.0467%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 377.9)
  * `_classify` (Impact: 56.1)
  * `next_arg` (Impact: 52.0)
  * `_match` (Impact: 43.5)
    * *Intent:* # sanitize the argument and request standardization again with SimTypeArray
  * `_match` (Impact: 41.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 626`, `structural_boundaries: 571`, `args: 172`, `func_start: 170`, `class_start: 49`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 220`, `dead_code: 7`, `planned_debt: 32`, `fragile_debt: 23`, `duplicate_logic: 92`
* *Architecture:* `api: 163`, `import: 13`
* *Defense:* `safety: 190`, `doc: 86`, `test: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.489
  * `Choke Point (Betweenness):` 0.001267 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` contextlib, collections, collections.abc, claripy, archinfo, .state_plugins.sim_action_object, .errors, logging...
  * `Imported By (In-Degree: 57):` (Excluded from Brief to save tokens)

### `angr/analyses/cfg/cfg_emulated.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.012 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.514 IQR)
- **Top Global Matches:** file_cluster_13: 13.012, file_cluster_11: 13.149, file_cluster_8: 13.162
- **Magnitude:** 1836.22 | **LOC:** 3454 | **CtrlFlow:** 68.5% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (32.0042%), Tech Debt (71.7758%)
**Top Internal Functions/Classes:**
  * `_try_resolving_indirect_jumps` (Impact: 208.6)
  * `_backward_slice_indirect` (Impact: 205.0)
  * `_process_hints` (Impact: 204.5)
    * *Intent:* """ if self._base_graph is None: # we don't do sorting if there is no base_graph return 0 MAX_JOBS =...
  * `_create_new_call_stack` (Impact: 194.8)
    * *Intent:* # Start symbolic exploration from each block state = self.project.factory.blank_state( addr=n.addr, ...
  * `_clean_pending_exits` (Impact: 162.1)
    * *Intent:* # If there is no valid exit in this branch and it's not # intentional (e.g. caused by a SimProcedure...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 638`, `structural_boundaries: 293`, `args: 89`, `func_start: 85`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 2`, `state_mutation: 267`, `dead_code: 17`, `planned_debt: 28`, `fragile_debt: 12`, `duplicate_logic: 5`
* *Architecture:* `io: 6`, `api: 43`, `import: 38`
* *Defense:* `safety: 50`, `doc: 319`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.48
  * `Choke Point (Betweenness):` 0.00132 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` functools, claripy, pyvex, angr.exploration_techniques.loop_seer, .cfg_base, angr.exploration_techniques.lengthlimiter, sys, angr.state_plugins.callstack...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `angr/analyses/decompiler/clinic.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.816 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.64 IQR)
- **Top Global Matches:** file_cluster_8: 12.816, file_cluster_13: 12.849, file_cluster_0: 12.905
- **Magnitude:** 1755.6 | **LOC:** 3763 | **CtrlFlow:** 68.1% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (35.6243%), Tech Debt (20.6824%)
**Top Internal Functions/Classes:**
  * `_stage_semantic_variable_naming` (Impact: 286.6)
  * `_make_function_prototype` (Impact: 133.8)
  * `remove_empty_nodes` (Impact: 71.4)
  * `handle_node` (Impact: 71.2)
  * `_constrain_callee_prototypes` (Impact: 60.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 867`, `structural_boundaries: 406`, `args: 105`, `func_start: 100`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 298`, `dead_code: 13`, `planned_debt: 9`, `fragile_debt: 5`, `duplicate_logic: 4`
* *Architecture:* `api: 24`, `import: 47`
* *Defense:* `safety: 203`, `doc: 87`, `test: 35`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.977
  * `Choke Point (Betweenness):` 0.010811 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` angr.knowledge_plugins.key_definitions, angr.utils.ssa, angr.knowledge_plugins.cfg.memory_data, angr.procedures.stubs.UnresolvableCallTarget, angr.analyses.typehoon, angr.knowledge_plugins.variables.variable_manager, logging, angr.analyses.cfg.cfg_base...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `angr/ailment/expression.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.045 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.105 IQR)
- **Top Global Matches:** file_cluster_0: 13.045, file_cluster_8: 13.057, file_cluster_11: 13.142
- **Magnitude:** 1748.36 | **LOC:** 2015 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (90.6023%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__str__` (Impact: 267.9)
  * `has_atom` (Impact: 37.0)
  * `replace` (Impact: 35.7)
  * `__str__` (Impact: 23.3)
  * `replace` (Impact: 21.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 418`, `structural_boundaries: 536`, `args: 202`, `func_start: 202`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 566`, `planned_debt: 2`, `duplicate_logic: 112`
* *Architecture:* `api: 151`, `import: 13`
* *Defense:* `safety: 65`, `doc: 6`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 24.866
  * `Choke Point (Betweenness):` 0.013775 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` abc, .tagged_object, claripy, angr.calling_conventions, collections.abc, archinfo, .statement, typing_extensions...
  * `Imported By (In-Degree: 139):` (Excluded from Brief to save tokens)

### `angr/state_plugins/unicorn_engine.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.027 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.763 IQR)
- **Top Global Matches:** file_cluster_8: 12.027, file_cluster_13: 12.079, file_cluster_7: 12.242
- **Magnitude:** 1437.8 | **LOC:** 1920 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (52.006%), Tech Debt (19.9273%)
**Top Internal Functions/Classes:**
  * `_load_native` (Impact: 568.7)
  * `_process_value` (Impact: 276.9)
  * `get_regs` (Impact: 52.4)
  * `set_regs` (Impact: 50.3)
  * `_report_symbolic_blocker` (Impact: 21.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 303`, `structural_boundaries: 200`, `args: 68`, `func_start: 67`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 13`, `state_mutation: 254`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 57`, `concurrency: 7`, `import: 25`
* *Defense:* `safety: 25`, `doc: 46`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.332
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` claripy, pyvex, sys, logging, angr.engines.vex.claripy.irop, binascii, angr.sim_state, importlib.resources...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/analyses/decompiler/test_decompiler.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.131 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.131 IQR)
- **Top Global Matches:** file_cluster_0: 13.131, file_cluster_17: 13.504, file_cluster_8: 13.53
- **Magnitude:** 1428.0 | **LOC:** 5443 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 44.4%
- **Risk Profile:** Cognitive Load (4.1659%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_decompiling_nl_i386_pie` (Impact: 495.3)
    * *Intent:* # Current decompilation output: # do # { # v1 = v0 + 1; # v3 = v2 + 1; # *(v2) = *(v0); # v0 = v1; #...
  * `test_decompiling_livectf_dc30_open_to_in` (Impact: 96.4)
  * `test_decompiling_armhf_float_int_convers` (Impact: 65.7)
  * `test_decompiling_rust_fmt_main` (Impact: 61.1)
    * *Intent:* # ensure we do not have redundant masking # ensure that we do not have multi-statement expressions i...
  * `test_decompiling_switch2_x86_64` (Impact: 35.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 488`, `structural_boundaries: 1110`, `args: 228`, `func_start: 228`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 16`, `dead_code: 41`, `planned_debt: 19`, `fragile_debt: 16`, `duplicate_logic: 3`, `orphaned_logic: 45`
* *Architecture:* `io: 220`, `api: 226`, `import: 22`
* *Defense:* `safety: 762`, `doc: 70`, `test: 946`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.281
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` functools, angr.knowledge_plugins.variables.variable_manager, logging, tests.common, os, angr.analyses.decompiler.structuring.phoenix, angr.analyses.decompiler, unittest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `angr/analyses/cfg/indirect_jump_resolvers/jumptable.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.769 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.19 IQR)
- **Top Global Matches:** file_cluster_13: 12.769, file_cluster_0: 12.844, file_cluster_8: 12.907
- **Magnitude:** 1395.28 | **LOC:** 2519 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (36.3492%), Tech Debt (57.4413%)
**Top Internal Functions/Classes:**
  * `_try_resolve_single_constant_loads` (Impact: 476.9)
  * `resolve` (Impact: 287.2)
    * *Intent:* # # Main class
  * `_handle_expr_CCall` (Impact: 148.5)
  * `_jumptable_precheck` (Impact: 28.4)
  * `_extract_spoffset_from_expr` (Impact: 24.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 496`, `structural_boundaries: 368`, `args: 87`, `func_start: 83`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 43`, `high_risk_execution: 5`, `state_mutation: 162`, `dead_code: 9`, `planned_debt: 2`, `fragile_debt: 6`, `duplicate_logic: 8`
* *Architecture:* `api: 58`, `import: 32`
* *Defense:* `safety: 153`, `doc: 91`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.332
  * `Choke Point (Betweenness):` 0.00232 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` functools, pyvex, claripy, angr.misc.ux, archinfo.arch_arm, logging, typing, enum...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `angr/knowledge_plugins/functions/function.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.158 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.173 IQR)
- **Top Global Matches:** file_cluster_0: 13.158, file_cluster_13: 13.283, file_cluster_11: 13.34
- **Magnitude:** 1366.72 | **LOC:** 2086 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (45.6075%), Tech Debt (99.5228%)
**Top Internal Functions/Classes:**
  * `find_declaration` (Impact: 206.5)
  * `dbg_print` (Impact: 92.3)
  * `local_runtime_values` (Impact: 44.4)
  * `_register_node` (Impact: 30.5)
    * *Intent:* """ Registers an edge between basic blocks in this function's transition graph. Arguments are CodeNo...
  * `prototype` (Impact: 28.9)
    * *Intent:* # update the cache if self._function_manager is not None: self._function_manager.set_function_return...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 405`, `structural_boundaries: 365`, `args: 119`, `func_start: 118`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 289`, `dead_code: 8`, `planned_debt: 6`, `fragile_debt: 3`, `duplicate_logic: 24`
* *Architecture:* `io: 1`, `api: 137`, `import: 32`
* *Defense:* `safety: 46`, `doc: 176`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.488
  * `Choke Point (Betweenness):` 0.002175 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` functools, angr.procedures.definitions, claripy, angr.serializable, angr.knowledge_plugins.cfg.memory_data, cle.backends.symbol, archinfo.arch_arm, matplotlib.pyplot...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `angr/engines/vex/claripy/irop.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.569 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.338 IQR)
- **Top Global Matches:** file_cluster_0: 13.569, file_cluster_13: 13.841, file_cluster_11: 13.872
- **Magnitude:** 1258.66 | **LOC:** 1296 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (61.9292%), Tech Debt (15.9117%)
**Top Internal Functions/Classes:**
  * `make_operations` (Impact: 455.6)
  * `_generic_pack_saturation` (Impact: 48.9)
  * `_op_mapped` (Impact: 29.2)
    * *Intent:* # # The actual operation handlers go here. # # pylint:disable=no-self-use,unused-argument def _op_ma...
  * `_auto_vectorize` (Impact: 23.3)
  * `_op_vector_float_mapped` (Impact: 18.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 248`, `structural_boundaries: 218`, `args: 86`, `func_start: 86`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 222`, `dead_code: 17`, `planned_debt: 2`, `fragile_debt: 4`
* *Architecture:* `api: 61`, `import: 12`
* *Defense:* `safety: 27`, `doc: 32`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.475
  * `Choke Point (Betweenness):` 0.000688 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` angr.state_plugins.sim_action_object, functools, pyvex, collections, math, itertools, re, claripy...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `angr/analyses/decompiler/ail_simplifier.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.417 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.777 IQR)
- **Top Global Matches:** file_cluster_13: 12.417, file_cluster_8: 12.44, file_cluster_0: 12.509
- **Magnitude:** 1219.76 | **LOC:** 2274 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 45.5%
- **Risk Profile:** Cognitive Load (45.4798%), Tech Debt (21.1961%)
**Top Internal Functions/Classes:**
  * `_unify_local_variables` (Impact: 715.4)
  * `_compute_effective_sizes` (Impact: 51.5)
  * `_rewrite_phi_const_exprs` (Impact: 49.9)
  * `_narrow_exprs` (Impact: 49.4)
  * `_simplify` (Impact: 41.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 623`, `structural_boundaries: 335`, `args: 56`, `func_start: 53`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 119`, `dead_code: 7`, `planned_debt: 4`, `fragile_debt: 2`, `duplicate_logic: 3`
* *Architecture:* `api: 10`, `import: 33`
* *Defense:* `safety: 137`, `doc: 37`, `test: 26`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.423
  * `Choke Point (Betweenness):` 0.002216 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` angr.knowledge_plugins.key_definitions, angr.ailment.statement, angr.utils.ssa, logging, typing, enum, .ailgraph_walker, angr.knowledge_plugins.key_definitions.definition...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `angr/analyses/disassembly.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.15 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.077 IQR)
- **Top Global Matches:** file_cluster_13: 13.15, file_cluster_11: 13.293, file_cluster_0: 13.3
- **Magnitude:** 1211.6 | **LOC:** 1351 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (86.3449%), Tech Debt (99.9433%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 239.1)
  * `_render` (Impact: 68.1)
  * `format_comment` (Impact: 63.6)
  * `dissect_instruction_by_default` (Impact: 62.2)
  * `parse_block` (Impact: 35.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 330`, `structural_boundaries: 259`, `args: 94`, `func_start: 89`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 396`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 2`, `duplicate_logic: 25`
* *Architecture:* `api: 64`, `import: 19`
* *Defense:* `safety: 55`, `doc: 13`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.505
  * `Choke Point (Betweenness):` 0.001227 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` pyvex, logging, typing, angr.block, , collections, collections.abc, angr.analyses...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `angr/analyses/ddg.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.276 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.704 IQR)
- **Top Global Matches:** file_cluster_13: 13.276, file_cluster_0: 13.3, file_cluster_11: 13.343
- **Magnitude:** 1109.34 | **LOC:** 1671 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.7871%), Tech Debt (99.5146%)
**Top Internal Functions/Classes:**
  * `add_def` (Impact: 120.8)
    * *Intent:* """ Make a hard copy of `self`. :return: A new LiveDefinition instance. :rtype: angr.analyses.ddg.Li...
  * `_construct` (Impact: 75.2)
  * `_handle_tmp_write` (Impact: 61.5)
  * `_track` (Impact: 54.6)
  * `data_sub_graph` (Impact: 41.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 315`, `structural_boundaries: 213`, `args: 78`, `func_start: 75`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 190`, `dead_code: 8`, `planned_debt: 10`, `fragile_debt: 2`, `duplicate_logic: 15`
* *Architecture:* `api: 51`, `import: 10`
* *Defense:* `safety: 37`, `doc: 183`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.398
  * `Choke Point (Betweenness):` 5.1e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` angr.sim_variable, claripy, collections, pyvex, angr.analyses, angr.code_location, networkx, angr.errors...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `angr/analyses/typehoon/simple_solver.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.603 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.692 IQR)
- **Top Global Matches:** file_cluster_8: 12.603, file_cluster_16: 12.609, file_cluster_0: 12.65
- **Magnitude:** 1076.4 | **LOC:** 2141 | **CtrlFlow:** 70.1% | **Authorship Centralization:** 77.8%
- **Risk Profile:** Cognitive Load (39.1406%), Tech Debt (65.9345%)
**Top Internal Functions/Classes:**
  * `_discover_equivalence` (Impact: 159.1)
  * `lookup` (Impact: 102.5)
  * `solve` (Impact: 78.2)
  * `compute_quotient_graph` (Impact: 48.2)
  * `_constraint_graph_saturate` (Impact: 46.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 616`, `structural_boundaries: 263`, `args: 74`, `func_start: 70`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 121`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 12`
* *Architecture:* `api: 29`, `import: 13`
* *Defense:* `safety: 207`, `doc: 70`, `test: 13`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.348
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` contextlib, collections, sortedcontainers, .typevars, .typeconsts, .variance, networkx.drawing.nx_agraph, networkx...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `angr/analyses/bindiff.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.682 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.769 IQR)
- **Top Global Matches:** file_cluster_0: 13.682, file_cluster_11: 13.72, file_cluster_13: 13.78
- **Magnitude:** 1069.78 | **LOC:** 1512 | **CtrlFlow:** 66.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.6899%), Tech Debt (28.1093%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 396.4)
  * `_compute_diff` (Impact: 108.9)
  * `_approximate_matcher_func_string_refs` (Impact: 67.1)
  * `_get_approximate_matches_between_matched` (Impact: 54.6)
  * `compare_statement_dict` (Impact: 35.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 379`, `structural_boundaries: 192`, `args: 60`, `func_start: 54`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 236`, `dead_code: 15`, `planned_debt: 5`, `duplicate_logic: 3`
* *Architecture:* `api: 29`, `import: 12`
* *Defense:* `safety: 28`, `doc: 135`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.345
  * `Choke Point (Betweenness):` 0.000304 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` angr.knowledge_plugins, types, functools, math, collections, angr.analyses, angr.knowledge_plugins.cfg.memory_data, networkx...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `angr/engines/vex/claripy/ccall.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.559 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.754 IQR)
- **Top Global Matches:** file_cluster_8: 9.559, file_cluster_7: 10.191, file_cluster_1: 10.464
- **Magnitude:** 943.74 | **LOC:** 2110 | **CtrlFlow:** 46.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (10.1636%), Tech Debt (13.1486%)
**Top Internal Functions/Classes:**
  * `pc_calculate_condition` (Impact: 98.6)
    * *Intent:* # This function takes a condition that is being checked (ie, zero bit), and basically # returns that...
  * `x86g_calculate_aad_aam` (Impact: 68.2)
  * `arm64g_calculate_flag_n` (Impact: 66.1)
    * *Intent:* ARM64CondCC = 3 # /* <u (lower) (aka LO) : C=0 */ ARM64CondMI = 4 # /* minus (negative) : N=1 */ ARM...
  * `pc_calculate_rdata_all_WRK` (Impact: 65.9)
    * *Intent:* # sanity check cc_op = op_concretize(cc_op) if cc_op == data[platform]["OpTypes"]["G_CC_OP_COPY"]: l...
  * `arm64g_calculate_condition` (Impact: 55.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 282`, `args: 101`, `func_start: 101`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `dead_code: 5`, `planned_debt: 9`, `fragile_debt: 3`
* *Architecture:* `api: 115`, `import: 8`
* *Defense:* `safety: 15`, `doc: 9`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.318
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` angr.state_plugins.sim_action_object, claripy, archinfo.arch_arm, angr.sim_options, angr.errors, logging, angr, __future__
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `angr/analyses/decompiler/utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.338 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.998 IQR)
- **Top Global Matches:** file_cluster_13: 12.338, file_cluster_8: 12.405, file_cluster_16: 12.469
- **Magnitude:** 919.46 | **LOC:** 1241 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (16.6339%), Tech Debt (36.1627%)
**Top Internal Functions/Classes:**
  * `insert_node` (Impact: 107.1)
  * `switch_extract_bitwiseand_jumptable_info` (Impact: 92.8)
  * `switch_extract_cmp_bounds_from_condition` (Impact: 57.0)
  * `switch_extract_switch_expr_from_jump_tar` (Impact: 52.8)
  * `remove_last_statement` (Impact: 27.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 391`, `structural_boundaries: 259`, `args: 52`, `func_start: 52`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 54`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 2`, `api: 73`, `import: 22`
* *Defense:* `safety: 112`, `doc: 52`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.623
  * `Choke Point (Betweenness):` 0.004357 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` angr.analyses.decompiler.peephole_optimizations.base, logging, typing, types, angr.utils.ail, angr.ailment, pdb, .structuring.structurer_nodes...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `angr/knowledge_plugins/functions/function_manager.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.905 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.13 IQR)
- **Top Global Matches:** file_cluster_13: 12.905, file_cluster_16: 12.95, file_cluster_0: 13.059
- **Magnitude:** 893.88 | **LOC:** 1488 | **CtrlFlow:** 42.8% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (35.4506%), Tech Debt (99.9998%)
**Top Internal Functions/Classes:**
  * `_generate_callmap_sif` (Impact: 233.0)
    * *Intent:* # Note that we use shallow copy of Function instances and do not update Function._function_manager t...
  * `_load_from_lmdb_core` (Impact: 24.1)
  * `rebuild_callgraph` (Impact: 21.7)
  * `get` (Impact: 20.6)
    * *Intent:* """ Clear all functions from memory and spilled storage. """
  * `_evict_n` (Impact: 14.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 327`, `args: 124`, `func_start: 123`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 132`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 37`
* *Architecture:* `io: 3`, `api: 90`, `concurrency: 25`, `import: 28`
* *Defense:* `safety: 71`, `doc: 134`, `test: 1`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.919
  * `Choke Point (Betweenness):` 0.000797 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` cle, angr.knowledge_plugins.plugin, weakref, bisect, logging, lmdb, typing, archinfo.arch_soot...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `angr/analyses/reaching_definitions/engine_ail.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.194 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.067 IQR)
- **Top Global Matches:** file_cluster_8: 10.194, file_cluster_13: 10.5, file_cluster_17: 10.607
- **Magnitude:** 849.56 | **LOC:** 1171 | **CtrlFlow:** 65.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (36.4891%), Tech Debt (19.0317%)
**Top Internal Functions/Classes:**
  * `_handle_stmt_Assignment` (Impact: 134.9)
  * `_handle_binop_Shr` (Impact: 46.7)
  * `_handle_binop_Sar` (Impact: 46.7)
  * `_handle_binop_Shl` (Impact: 46.5)
  * `_handle_expr_Register` (Impact: 43.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 363`, `structural_boundaries: 190`, `args: 63`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 18`, `dead_code: 2`, `planned_debt: 9`, `fragile_debt: 3`
* *Architecture:* `api: 46`, `import: 22`
* *Defense:* `safety: 33`, `doc: 2`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.281
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` claripy, logging, typing, angr.storage.memory_mixins.paged_memory.pages.multi_values, angr.engines.light.engine, angr.ailment, angr.knowledge_plugins.key_definitions.constants, collections.abc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `angr/analyses/decompiler/structuring/structurer_base.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.974 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.014 IQR)
- **Top Global Matches:** file_cluster_8: 11.974, file_cluster_0: 11.983, file_cluster_13: 11.995
- **Magnitude:** 849.34 | **LOC:** 1141 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.1714%), Tech Debt (95.4189%)
**Top Internal Functions/Classes:**
  * `_remove_redundant_jumps` (Impact: 71.1)
  * `_rewrite_conditional_jump_to_break` (Impact: 59.1)
  * `_rewrite_conditional_jumps_to_breaks` (Impact: 46.2)
  * `replace_nodes` (Impact: 40.8)
  * `_rewrite_jumps_to_continues` (Impact: 39.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 288`, `structural_boundaries: 183`, `args: 49`, `func_start: 48`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 56`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 3`, `duplicate_logic: 10`
* *Architecture:* `api: 27`, `import: 17`
* *Defense:* `safety: 120`, `doc: 27`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.415
  * `Choke Point (Betweenness):` 0.00043 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` angr.analyses.decompiler.utils, angr.analyses.decompiler.sequence_walker, claripy, collections, angr.analyses, angr.analyses.decompiler.condition_processor, angr.analyses.decompiler.label_collector, angr.knowledge_plugins.functions...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `angr/storage/file.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.753 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.831 IQR)
- **Top Global Matches:** file_cluster_0: 12.753, file_cluster_13: 12.875, file_cluster_17: 12.949
- **Magnitude:** 840.64 | **LOC:** 1213 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (46.1143%), Tech Debt (95.7811%)
**Top Internal Functions/Classes:**
  * `read` (Impact: 255.8)
  * `_prep_generic` (Impact: 210.3)
  * `make_ident` (Impact: 11.3)
  * `set_state` (Impact: 11.2)
  * `__init__` (Impact: 9.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 245`, `args: 97`, `func_start: 97`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 5`, `state_mutation: 175`, `dead_code: 2`, `planned_debt: 5`, `duplicate_logic: 10`
* *Architecture:* `api: 96`, `import: 9`
* *Defense:* `safety: 22`, `doc: 113`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.848
  * `Choke Point (Betweenness):` 0.000245 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` angr.state_plugins.sim_action_object, claripy, itertools, angr.state_plugins.plugin, .memory_mixins, angr.errors, logging, angr...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `angr/analyses/vfg.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 12.902 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.207 IQR)
- **Top Global Matches:** file_cluster_11: 12.902, file_cluster_13: 12.907, file_cluster_0: 13.02
- **Magnitude:** 773.14 | **LOC:** 1894 | **CtrlFlow:** 49.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (35.0396%), Tech Debt (97.4279%)
**Top Internal Functions/Classes:**
  * `_job_sorting_key` (Impact: 140.1)
  * `__repr__` (Impact: 54.8)
  * `_set_return_address` (Impact: 48.8)
  * `_handle_successor_multitargets` (Impact: 44.6)
  * `_remove_pending_return` (Impact: 20.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 229`, `args: 72`, `func_start: 72`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 39`, `high_risk_execution: 1`, `state_mutation: 200`, `dead_code: 6`, `planned_debt: 23`, `fragile_debt: 5`, `duplicate_logic: 9`
* *Architecture:* `api: 33`, `import: 23`
* *Defense:* `safety: 49`, `doc: 158`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.345
  * `Choke Point (Betweenness):` 0.00069 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` claripy, archinfo.arch_arm, angr.state_plugins.callstack, logging, typing, angr.procedures, angr.knowledge_base, angr.sim_state...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `angr/analyses/purity/engine.py` (PYTHON) | Magnitude: 425.66 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 437, encapsulation: 238, structural_boundaries: 201, branch: 97
- `angr/ailment/expression.py` (PYTHON) | Magnitude: 1748.36 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1632, state_mutation: 566, structural_boundaries: 536, branch: 418
- `angr/engines/pcode/behavior.py` (PYTHON) | Magnitude: 331.58 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 316, structural_boundaries: 205, encapsulation: 115, doc: 114
- `angr/knowledge_plugins/cfg/block_id.py` (PYTHON) | Magnitude: 66.7 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 22, state_mutation: 19, branch: 13
- `angr/knowledge_plugins/cfg/cfg_node.py` (PYTHON) | Magnitude: 477.04 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 574, state_mutation: 156, structural_boundaries: 134, encapsulation: 133

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `angr/analyses/vfg.py` (PYTHON) | Magnitude: 773.14 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 994, encapsulation: 299, structural_boundaries: 229, branch: 228

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `corpus_tests/scripts/gh_push_file.sh` (SHELL) | Magnitude: 6.6 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 60, io: 36, state_mutation: 25, branch: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `angr/analyses/forward_analysis/forward_analysis.py` (PYTHON) | Magnitude: 274.7 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 290, encapsulation: 178, structural_boundaries: 121, doc: 68
- `angr/analyses/decompiler/region_simplifiers/ifelse.py` (PYTHON) | Magnitude: 71.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 63, branch: 21, structural_boundaries: 14, encapsulation: 14
- `tests/exploration_techniques/test_stub_stasher.py` (PYTHON) | Magnitude: 4.2 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 8, test: 7, encapsulation: 6
- `tests/procedures/posix/test_chroot.py` (PYTHON) | Magnitude: 4.7 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 9, import: 6, test: 5
- `angr/analyses/identifier/func.py` (PYTHON) | Magnitude: 39.22 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 19, api: 14, state_mutation: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `angr/utils/graph.py` (PYTHON) | Magnitude: 450.5 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 540, branch: 204, encapsulation: 135, structural_boundaries: 128
- `angr/utils/library.py` (PYTHON) | Magnitude: 67.78 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 98, doc: 30, branch: 28, structural_boundaries: 25
- `angr/utils/tagged_interval_map.py` (PYTHON) | Magnitude: 67.26 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 54, encapsulation: 30, structural_boundaries: 24, branch: 20
- `angr/utils/doms.py` (PYTHON) | Magnitude: 150.68 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 103, encapsulation: 59, branch: 45, structural_boundaries: 30
- `angr/knowledge_plugins/obfuscations.py` (PYTHON) | Magnitude: 12.24 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 8, safety_bypasses: 6, state_mutation: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `angr/analyses/binary_optimizer.py` (PYTHON) | Magnitude: 397.06 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 369, branch: 152, structural_boundaries: 105, state_mutation: 62
- `angr/analyses/identifier/functions/skip_realloc.py` (PYTHON) | Magnitude: 63.9 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 29, branch: 15, state_mutation: 12
- `angr/analyses/decompiler/optimization_passes/lowered_switch_simplifier.py` (PYTHON) | Magnitude: 740.34 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 708, branch: 300, state_mutation: 120, structural_boundaries: 114
- `angr/analyses/identifier/functions/skip_calloc.py` (PYTHON) | Magnitude: 50.64 | Delta: **0.128 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 26, branch: 12, args: 6
- `tests/analyses/test_disassembly.py` (PYTHON) | Magnitude: 62.88 | Delta: **0.224 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 149, sec_reflection_metaprogramming: 132, structural_boundaries: 76, safety: 57

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `corpus_tests/scripts/gh_ls.sh` (SHELL) | Magnitude: 14.92 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 112, io: 65, branch: 54, state_mutation: 46
- `corpus_tests/scripts/classify_diff.sh` (SHELL) | Magnitude: 17.49 | Delta: **0.135 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 82, indent_spaces: 82, branch: 62, io: 54
- `angr/misc/picklable_lock.py` (PYTHON) | Magnitude: 39.88 | Delta: **0.172 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 21, indent_spaces: 20, encapsulation: 17, concurrency: 13
- `corpus_tests/scripts/snapshot_diff.sh` (SHELL) | Magnitude: 23.74 | Delta: **0.264 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 150, state_mutation: 80, io: 72, branch: 68

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `angr/procedures/java_jni/array_operations.py` (PYTHON) | Magnitude: 92.46 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 136, structural_boundaries: 49, api: 25, encapsulation: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `angr/serializable.py` (PYTHON) | Magnitude: 17.96 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 19, indent_spaces: 16, structural_boundaries: 10, api: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `angr/procedures/posix/htonl.py` (PYTHON) | Magnitude: 5.84 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 4, api: 2, import: 2
- `angr/procedures/posix/htons.py` (PYTHON) | Magnitude: 5.84 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 4, api: 2, import: 2
- `tests/perf/perf_concrete_execution.py` (PYTHON) | Magnitude: 4.42 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 9, import: 5, io: 4
- `angr/analyses/decompiler/graph_region.py` (PYTHON) | Magnitude: 285.42 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 326, branch: 126, structural_boundaries: 59, state_mutation: 32
- `angr/knowledge_plugins/callsite_prototypes.py` (PYTHON) | Magnitude: 41.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 32, encapsulation: 19, api: 17

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `angr/knowledge_plugins/cfg/spilling_cfg.py` -> Churn: **61.28%** | Cog Load: 44.6733% | Debt: 68.5066%
- `angr/knowledge_plugins/cfg/cfg_model.py` -> Churn: **59.6%** | Cog Load: 38.6277% | Debt: 55.7937%
- `angr/analyses/calling_convention/fact_collector.py` -> Churn: **56.15%** | Cog Load: 58.0523% | Debt: 22.4064%
- `angr/knowledge_plugins/cfg/spilling_digraph.py` -> Churn: **51.7%** | Cog Load: 26.9501% | Debt: 99.8893%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `angr/analyses/cfg/cfg_fast.py` -> **Fish** (84.6% isolated ownership) | Magnitude: 2935.88
- `angr/analyses/bindiff.py` -> **pre-commit-ci[bot]** (100.0% isolated ownership) | Magnitude: 1069.78
- `angr/analyses/decompiler/structuring/structurer_base.py` -> **Fish** (100.0% isolated ownership) | Magnitude: 849.34
- `angr/storage/file.py` -> **Fish** (100.0% isolated ownership) | Magnitude: 840.64
- `angr/analyses/calling_convention/calling_convention.py` -> **Audrey Dutcher** (100.0% isolated ownership) | Magnitude: 764.32

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `angr/project.py` -> **Severity: 4.602** (Bridge: 0.046 * Flux: 99.9841%)
- `angr/analyses/analysis.py` -> **Severity: 4.335** (Bridge: 0.0434 * Flux: 99.899%)
- `angr/sim_state.py` -> **Severity: 3.88** (Bridge: 0.0392 * Flux: 99.0318%)
- `angr/sim_type.py` -> **Severity: 1.514** (Bridge: 0.019 * Flux: 79.8607%)
- `angr/ailment/expression.py` -> **Severity: 1.377** (Bridge: 0.0138 * Flux: 99.9988%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `angr/errors.py` -> **Severity: 3299.2** (Blast Radius: 32.992 * Doc Risk: 100.0%)
- `angr/concretization_strategies/logging.py` -> **Severity: 2844.453** (Blast Radius: 92.601 * Doc Risk: 30.7173%)
- `angr/ailment/expression.py` -> **Severity: 2351.371** (Blast Radius: 24.866 * Doc Risk: 94.5617%)
- `angr/ailment/statement.py` -> **Severity: 1436.6** (Blast Radius: 14.366 * Doc Risk: 100.0%)
- `angr/sim_type.py` -> **Severity: 1381.26** (Blast Radius: 22.24 * Doc Risk: 62.107%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
