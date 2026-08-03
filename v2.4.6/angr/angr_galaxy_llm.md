# ARCHITECTURAL_BRIEF: angr
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/angr` |
| **Timestamp** | `2026-08-03T19:24:10.427747+00:00` |
| **Scan Duration** | `8.26s` |
| **Git Branch** | `master` |
| **Git Commit** | `ac1ad40678a32222344f788c7f74378bc213e50a` |
| **Git Remote** | `https://github.com/angr/angr.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1418 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
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
> **Architectural Drift Z-Score:** `5.71`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 936 | 53.5% |
| file_cluster_13 | 726 | 41.5% |
| file_cluster_0 | 33 | 1.9% |
| file_cluster_16 | 31 | 1.8% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 15.1 | 8.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.0 | 11.1 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 18.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 26.7 | 2.3 | 80.0 |
| API Exposure | 0.0 | 12.8 | 2.8 | 2.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 26.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 93.0 | 1.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 89.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.2 | 0.8 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 85.0 | 8.0 | 7.9 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 64.3 | 85.7 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 51.1 | 53.9 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 31.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `_match_acyclic_schemas` (@ `angr/analyses/decompiler/structuring/phoenix.py`) -> Impact: **4439.1** | LOC: 1911
- `_load_native` (@ `angr/state_plugins/unicorn_engine.py`) -> Impact: **3530.5** | LOC: 1502
- `alignment` (@ `angr/sim_type.py`) -> Impact: **2635.0** | LOC: 1051
- `__repr__` (@ `angr/calling_conventions.py`) -> Impact: **2435.6** | LOC: 699
- `_unify_local_variables` (@ `angr/analyses/decompiler/ail_simplifier.py`) -> Impact: **2352.2** | LOC: 1213
- `_generate_cfgnode` (@ `angr/analyses/cfg/cfg_fast.py`) -> Impact: **2212.1** | LOC: 842
- `get` (@ `angr/procedures/definitions/__init__.py`) -> Impact: **2131.6** | LOC: 772
  * *Intent:* """ self.types[name] = t def get(self, name: str, bottom_on_missing: bool = False, memo: set[str] | None = None) -> SimType: """
- `timed_function` (@ `angr/state_plugins/solver.py`) -> Impact: **2129.5** | LOC: 882
- `_load_a_byte_as_int` (@ `angr/analyses/cfg/cfg_fast.py`) -> Impact: **2119.1** | LOC: 674
- `serialize_to_cmessage` (@ `angr/knowledge_plugins/cfg/cfg_model.py`) -> Impact: **2027.4** | LOC: 538

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `parse_function_args` (@ `angr/__main__.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """ Generate a sequence of functions in the project kb by their identifier in func_args. :param proj: Project to query. :param func_args: Sequence of ...
- `convert` (@ `angr/ailment/converter_vex.py`) -> **O(2^N) [Recursive]**
- `__repr__` (@ `angr/analyses/binary_optimizer.py`) -> **O(2^N) [Recursive]**
- `_get_simsuccessors` (@ `angr/analyses/cfg/cfg_emulated.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Get the state from our CFG
- `_load_a_byte_as_int` (@ `angr/analyses/cfg/cfg_fast.py`) -> **O(2^N) [Recursive]**
- `resolve` (@ `angr/analyses/cfg/indirect_jump_resolvers/jumptable.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # # Main class
- `_sync_steps` (@ `angr/analyses/congruency_check.py`) -> **O(2^N) [Recursive]**
- `add_def` (@ `angr/analyses/ddg.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """ Make a hard copy of `self`. :return: A new LiveDefinition instance. :rtype: angr.analyses.ddg.LiveDefinitions """
- `remove_claripy_bool_asts` (@ `angr/analyses/decompiler/condition_processor.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # the negation of the union of diverging conditions is the guarding condition for this node cond = claripy.Or(*map(claripy.Not, diverging_conditions))...
- `get_last_statement` (@ `angr/analyses/decompiler/condition_processor.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `test_decompiling_nl_i386_pie` (@ `tests/analyses/decompiler/test_decompiler.py`) -> DB Complexity: **360**
  * *Intent:* # Current decompilation output: # do # { # v1 = v0 + 1; # v3 = v2 + 1; # *(v2) = *(v0); # v0 = v1; # v2 = v3; # We can improve it by re-arranging the ...
- `help_[Truncated]` (@ `corpus_tests/scripts/snapshot_diff.sh`) -> DB Complexity: **253**
- `help_[Truncated]` (@ `corpus_tests/scripts/gh_ls.sh`) -> DB Complexity: **229**
- `Anonymous_Block_[Truncated]` (@ `corpus_tests/scripts/classify_diff.sh`) -> DB Complexity: **162**
- `help_[Truncated]` (@ `corpus_tests/scripts/gh_push_file.sh`) -> DB Complexity: **118**
- `_load_native` (@ `angr/state_plugins/unicorn_engine.py`) -> DB Complexity: **99**
- `make_operations` (@ `angr/engines/vex/claripy/irop.py`) -> DB Complexity: **87**
- `__str__` (@ `angr/ailment/expression.py`) -> DB Complexity: **83**
- `help` (@ `corpus_tests/scripts/gh_create_branch.sh`) -> DB Complexity: **67**
- `get` (@ `angr/procedures/definitions/__init__.py`) -> DB Complexity: **66**
  * *Intent:* """ self.types[name] = t def get(self, name: str, bottom_on_missing: bool = False, memo: set[str] | None = None) -> SimType: """

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `angr/analyses` | 36 | 30564.1 | 35.95% | 63.64% |
| `angr` | 31 | 27002.48 | 29.66% | 38.86% |
| `angr/analyses/decompiler` | 28 | 21450.38 | 27.23% | 14.82% |
| `angr/state_plugins` | 29 | 17678.3 | 34.49% | 35.64% |
| `angr/analyses/cfg` | 10 | 17515.2 | 26.16% | 22.75% |
| `angr/analyses/decompiler/optimization_passes` | 39 | 17327.14 | 25.81% | 27.43% |
| `angr/analyses/decompiler/peephole_optimizations` | 62 | 12156.29 | 19.19% | 4.84% |
| `angr/analyses/decompiler/structuring` | 7 | 12028.12 | 30.29% | 27.21% |
| `angr/ailment` | 12 | 8852.02 | 27.57% | 41.82% |
| `angr/analyses/typehoon` | 8 | 7410.72 | 31.08% | 40.43% |

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

### Obfuscation & Evasion Surface
- `tests/analyses/reaching_definitions/test_regressions.py` -> **100.0%** Exposure
- `tests/engines/test_hook.py` -> **99.8472%** Exposure
- `tests/analyses/cfg/test_noop_blocks.py` -> **83.2158%** Exposure
- `tests/analyses/test_disassembly.py` -> **41.5973%** Exposure
- `tests/storage/test_memview.py` -> **1.6151%** Exposure
### Exploit Generation Surface
- `angr/__main__.py` -> **100.0%** Exposure
- `angr/ailment/block.py` -> **100.0%** Exposure
- `angr/ailment/block_walker.py` -> **100.0%** Exposure
- `angr/ailment/converter_pcode.py` -> **100.0%** Exposure
- `angr/ailment/converter_vex.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `angr/angrdb/db.py` -> **100.0%** Exposure
- `angr/angrdb/serializers/variables.py` -> **100.0%** Exposure
- `angr/exploration_techniques/spiller.py` -> **100.0%** Exposure
- `angr/flirt/build_sig.py` -> **100.0%** Exposure
- `angr/procedures/libc/fopen.py` -> **100.0%** Exposure
### Raw Memory Manipulation
- `native/angr/src/automaton/state.rs` -> **0.0001%** Exposure
### Algorithmic DoS Exposure
- `angr/__main__.py` -> **100.0%** Exposure
- `angr/ailment/block.py` -> **100.0%** Exposure
- `angr/ailment/block_walker.py` -> **100.0%** Exposure
- `angr/ailment/converter_pcode.py` -> **100.0%** Exposure
- `angr/ailment/converter_vex.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `7202` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `angr/exploration_techniques/spiller.py` (PYTHON) -> Cumulative Risk: **888.83**
- **Archetype:** `file_cluster_13` (Distance: 11.356 IQR)
- **Magnitude:** 326.66 | **LOC:** 280 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `step` (Impact: 125.1), `_pickle` (Impact: 37.3), `_unpickle` (Impact: 22.1)

### 2. `angr/knowledge_plugins/cfg/spilling_cfg.py` (PYTHON) -> Cumulative Risk: **864.42**
- **Archetype:** `file_cluster_16` (Distance: 12.26 IQR)
- **Magnitude:** 1541.42 | **LOC:** 1183 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_load_from_lmdb_core` (Impact: 896.8), `copy` (Impact: 98.6), `_save_to_lmdb` (Impact: 57.0)

### 3. `angr/knowledge_plugins/cfg/spilling_digraph.py` (PYTHON) -> Cumulative Risk: **864.06**
- **Archetype:** `file_cluster_13` (Distance: 11.668 IQR)
- **Magnitude:** 795.46 | **LOC:** 598 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_deserialize_inner_dict` (Impact: 99.7), `_serialize_inner_dict` (Impact: 86.4), `copy` (Impact: 56.1)

### 4. `angr/state_plugins/trace_additions.py` (PYTHON) -> Cumulative Risk: **862.77**
- **Archetype:** `file_cluster_0` (Distance: 12.019 IQR)
- **Magnitude:** 1462.56 | **LOC:** 738 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `atoi_dumps` (Impact: 764.1), `get_real_len` (Impact: 59.8), `generic_info_hook` (Impact: 53.8)

### 5. `angr/distributed/worker.py` (PYTHON) -> Cumulative Risk: **862.68**
- **Archetype:** `file_cluster_13` (Distance: 9.821 IQR)
- **Magnitude:** 356.74 | **LOC:** 185 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `step` (Impact: 247.4), `step` (Impact: 54.2), `__init__` (Impact: 6.2)

### 6. `angr/analyses/disassembly.py` (PYTHON) -> Cumulative Risk: **861.61**
- **Archetype:** `file_cluster_13` (Distance: 13.15 IQR)
- **Magnitude:** 3861.7 | **LOC:** 1351 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 1580.7), `_render` (Impact: 421.5), `format_comment` (Impact: 417.0)

### 7. `angr/knowledge_plugins/functions/function_manager.py` (PYTHON) -> Cumulative Risk: **854.42**
- **Archetype:** `file_cluster_13` (Distance: 12.905 IQR)
- **Magnitude:** 2094.68 | **LOC:** 1488 | **CtrlFlow:** 42.8% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_generate_callmap_sif` (Impact: 761.3), `copy` (Impact: 86.4), `rebuild_callgraph` (Impact: 73.6)

### 8. `angr/ailment/expression.py` (PYTHON) -> Cumulative Risk: **827.54**
- **Archetype:** `file_cluster_0` (Distance: 13.045 IQR)
- **Magnitude:** 4567.56 | **LOC:** 2015 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `__str__` (Impact: 1419.7), `has_atom` (Impact: 181.1), `replace` (Impact: 171.7)

### 9. `angr/distributed/server.py` (PYTHON) -> Cumulative Risk: **824.61**
- **Archetype:** `file_cluster_13` (Distance: 11.517 IQR)
- **Magnitude:** 217.3 | **LOC:** 197 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `run` (Impact: 81.4), `on_worker_exit` (Impact: 18.4), `inc_active_workers` (Impact: 7.1)

### 10. `angr/vaults.py` (PYTHON) -> Cumulative Risk: **820.6**
- **Archetype:** `file_cluster_13` (Distance: 12.53 IQR)
- **Magnitude:** 406.18 | **LOC:** 368 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 28.0), `_get_persistent_id` (Impact: 25.6), `is_stored` (Impact: 17.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `angr/analyses/cfg/cfg_fast.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.055 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.214 IQR)
- **Top Global Matches:** file_cluster_8: 13.055, file_cluster_13: 13.113, file_cluster_7: 13.215
- **Magnitude:** 9209.58 | **LOC:** 5547 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 84.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (28.2465%), Tech Debt (35.291%)
**Top Internal Functions/Classes:**
  * `_generate_cfgnode` (Impact: 2212.1 | O(N^6) | DB: 7)
  * `_load_a_byte_as_int` (Impact: 2119.1 | O(2^N) | DB: 14)
  * `_job_queue_empty` (Impact: 560.4 | O(N^6) | DB: 14)
  * `_remove_redundant_overlapping_blocks` (Impact: 445.6 | O(N^6))
  * `_collect_data_references_by_scanning_stm` (Impact: 321.2 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1255`, `structural_boundaries: 528`, `args: 130`, `func_start: 125`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 381`, `dead_code: 26`, `planned_debt: 17`, `fragile_debt: 11`, `duplicate_logic: 8`
* *Architecture:* `api: 42`, `import: 41`
* *Defense:* `safety: 107`, `doc: 316`, `test: 14`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.647
  * `Choke Point (Betweenness):` 0.003796 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` .cfg_arch_options, cle.address_translator, .indirect_jump_resolvers.jumptable, sortedcontainers, angr.errors, angr.analyses.decompiler.clinic, angr.knowledge_plugins.cfg.types, archinfo...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `angr/sim_type.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.403 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.679 IQR)
- **Top Global Matches:** file_cluster_8: 12.403, file_cluster_0: 12.407, file_cluster_16: 12.534
- **Magnitude:** 7770.66 | **LOC:** 4480 | **CtrlFlow:** 47.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 42
- **Risk Profile:** Cognitive Load (26.5983%), Tech Debt (99.9306%)
**Top Internal Functions/Classes:**
  * `alignment` (Impact: 2635.0 | O(2^N) | DB: 42)
  * `extract` (Impact: 1783.1 | O(2^N) | DB: 24)
  * `store` (Impact: 942.0 | O(2^N) | DB: 18)
  * `normalize_cpp_function_name` (Impact: 208.2 | O(2^N))
  * `__eq__` (Impact: 169.2 | O(2^N) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 788`, `structural_boundaries: 857`, `args: 318`, `func_start: 317`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 65`, `high_risk_execution: 7`, `state_mutation: 313`, `dead_code: 5`, `planned_debt: 18`, `fragile_debt: 14`, `duplicate_logic: 77`
* *Architecture:* `api: 223`, `import: 21`
* *Defense:* `safety: 145`, `doc: 181`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 22.24
  * `Choke Point (Betweenness):` 0.018958 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` pycparser, angr.errors, archinfo, cxxheaderparser.simple, typing, claripy, collections.abc, collections...
  * `Imported By (In-Degree: 80):` (Excluded from Brief to save tokens)

### `angr/analyses/decompiler/structuring/phoenix.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.846 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.531 IQR)
- **Top Global Matches:** file_cluster_8: 11.846, file_cluster_17: 12.05, file_cluster_13: 12.116
- **Magnitude:** 7756.26 | **LOC:** 3648 | **CtrlFlow:** 70.8% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (44.0209%), Tech Debt (13.7754%)
**Top Internal Functions/Classes:**
  * `_match_acyclic_schemas` (Impact: 4439.1 | O(N^6) | DB: 20)
  * `_analyze_cyclic` (Impact: 1511.0 | O(N^6) | DB: 7)
    * *Intent:* # we could not make a loop after the last cycle refinement. restore the graph l.debug("Could not str...
  * `_remove_first_statement_if_jump` (Impact: 258.7 | O(2^N))
  * `_analyze` (Impact: 173.6 | O(N^6) | DB: 3)
  * `_refine_cyclic_determine_loop_body` (Impact: 142.3 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1027`, `structural_boundaries: 423`, `args: 86`, `func_start: 72`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 126`, `dead_code: 14`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 11`, `import: 22`
* *Defense:* `safety: 166`, `doc: 28`, `test: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.211
  * `Choke Point (Betweenness):` 0.003491 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` angr.ailment.statement, angr.analyses.decompiler.sequence_walker, angr.analyses.decompiler.node_replacer, typing, angr.ailment.block, angr.analyses.decompiler.counters.call_counter, networkx, claripy...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `angr/calling_conventions.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.716 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.187 IQR)
- **Top Global Matches:** file_cluster_0: 12.716, file_cluster_11: 12.771, file_cluster_17: 12.864
- **Magnitude:** 6576.1 | **LOC:** 2808 | **CtrlFlow:** 52.3% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (40.0435%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 2435.6 | O(2^N) | DB: 19)
  * `_classify` (Impact: 380.1 | O(2^N))
  * `_classify` (Impact: 197.8 | O(2^N))
  * `_classify` (Impact: 197.7 | O(2^N))
  * `_flatten` (Impact: 178.4 | O(2^N) | DB: 2)
    * *Intent:* # TODO: Make sure the information is correct ARG_REGS = ["rcx"] FP_ARG_REGS = [] RETURN_VAL = SimReg...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 626`, `structural_boundaries: 571`, `args: 172`, `func_start: 170`, `class_start: 49`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 220`, `dead_code: 7`, `planned_debt: 32`, `fragile_debt: 23`, `duplicate_logic: 92`
* *Architecture:* `api: 163`, `import: 13`
* *Defense:* `safety: 190`, `doc: 86`, `test: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.489
  * `Choke Point (Betweenness):` 0.001267 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .errors, collections.abc, .sim_type, this, logging, .state_plugins.sim_action_object, typing, collections...
  * `Imported By (In-Degree: 57):` (Excluded from Brief to save tokens)

### `angr/analyses/reassembler.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.311 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.826 IQR)
- **Top Global Matches:** file_cluster_13: 13.311, file_cluster_8: 13.376, file_cluster_0: 13.411
- **Magnitude:** 6136.1 | **LOC:** 2905 | **CtrlFlow:** 63.1% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 49
- **Risk Profile:** Cognitive Load (48.2685%), Tech Debt (99.8788%)
**Top Internal Functions/Classes:**
  * `assembly` (Impact: 935.2 | O(N^6) | DB: 49)
  * `__repr__` (Impact: 718.7 | O(2^N) | DB: 37)
  * `new_label` (Impact: 501.1 | O(2^N) | DB: 2)
  * `assembly` (Impact: 423.7 | O(2^N))
  * `_initialize` (Impact: 419.8 | O(N^6) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 630`, `structural_boundaries: 369`, `args: 117`, `func_start: 107`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 608`, `dead_code: 5`, `planned_debt: 10`, `fragile_debt: 3`, `duplicate_logic: 39`
* *Architecture:* `api: 92`, `import: 22`
* *Defense:* `safety: 21`, `doc: 230`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.345
  * `Choke Point (Betweenness):` 0.004952 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` .cfg.cfg_fast, pyvex, .cfg.cfg_emulated, angr.knowledge_plugins.cfg.memory_data, typing, capstone, networkx, angr.codenode...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `angr/analyses/cfg/cfg_emulated.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.011 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.513 IQR)
- **Top Global Matches:** file_cluster_13: 13.011, file_cluster_11: 13.148, file_cluster_8: 13.161
- **Magnitude:** 5180.82 | **LOC:** 3454 | **CtrlFlow:** 68.5% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (32.4014%), Tech Debt (71.7758%)
**Top Internal Functions/Classes:**
  * `_try_resolving_indirect_jumps` (Impact: 710.7 | O(N^6) | DB: 2)
  * `_backward_slice_indirect` (Impact: 674.6 | O(N^6) | DB: 7)
  * `_process_hints` (Impact: 654.9 | O(N^6) | DB: 4)
    * *Intent:* """ if self._base_graph is None: # we don't do sorting if there is no base_graph return 0 MAX_JOBS =...
  * `_create_new_call_stack` (Impact: 638.0 | O(N^6) | DB: 6)
    * *Intent:* # Start symbolic exploration from each block state = self.project.factory.blank_state( addr=n.addr, ...
  * `_clean_pending_exits` (Impact: 521.5 | O(N^6) | DB: 2)
    * *Intent:* # If there is no valid exit in this branch and it's not # intentional (e.g. caused by a SimProcedure...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 638`, `structural_boundaries: 293`, `args: 88`, `func_start: 85`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 2`, `state_mutation: 267`, `dead_code: 17`, `planned_debt: 28`, `fragile_debt: 12`, `duplicate_logic: 5`
* *Architecture:* `io: 6`, `api: 43`, `import: 38`
* *Defense:* `safety: 50`, `doc: 319`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.48
  * `Choke Point (Betweenness):` 0.00132 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` angr.exploration_techniques.slicecutor, angr.errors, archinfo, sys, functools, angr.analyses.backward_slice, pyvex, angr.exploration_techniques.lengthlimiter...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `angr/analyses/cfg/indirect_jump_resolvers/jumptable.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.771 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.19 IQR)
- **Top Global Matches:** file_cluster_13: 12.771, file_cluster_0: 12.846, file_cluster_8: 12.909
- **Magnitude:** 4769.08 | **LOC:** 2519 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (37.1557%), Tech Debt (57.4413%)
**Top Internal Functions/Classes:**
  * `resolve` (Impact: 1907.2 | O(2^N) | DB: 2)
    * *Intent:* # # Main class
  * `_try_resolve_single_constant_loads` (Impact: 1561.9 | O(N^6) | DB: 12)
  * `_handle_expr_CCall` (Impact: 411.8 | O(N^5) | DB: 20)
  * `_extract_spoffset_from_expr` (Impact: 144.9 | O(2^N))
  * `_extract_regoffset_from_expr` (Impact: 144.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 496`, `structural_boundaries: 368`, `args: 87`, `func_start: 83`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 43`, `high_risk_execution: 5`, `state_mutation: 162`, `dead_code: 9`, `planned_debt: 2`, `fragile_debt: 6`, `duplicate_logic: 8`
* *Architecture:* `api: 58`, `import: 32`
* *Defense:* `safety: 153`, `doc: 91`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.332
  * `Choke Point (Betweenness):` 0.00232 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` angr.exploration_techniques.slicecutor, angr.engines.vex.claripy.datalayer, angr.errors, functools, .resolver, pyvex, angr.concretization_strategies, angr.analyses.propagator.top_checker_mixin...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `angr/ailment/expression.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.045 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.105 IQR)
- **Top Global Matches:** file_cluster_0: 13.045, file_cluster_8: 13.057, file_cluster_11: 13.142
- **Magnitude:** 4567.56 | **LOC:** 2015 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 83
- **Risk Profile:** Cognitive Load (90.6023%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__str__` (Impact: 1419.7 | O(2^N) | DB: 83)
  * `has_atom` (Impact: 181.1 | O(2^N) | DB: 1)
  * `replace` (Impact: 171.7 | O(2^N) | DB: 1)
  * `has_atom` (Impact: 108.7 | O(2^N))
  * `replace` (Impact: 97.6 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 418`, `structural_boundaries: 536`, `args: 202`, `func_start: 202`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 566`, `planned_debt: 2`, `duplicate_logic: 112`
* *Architecture:* `api: 151`, `import: 13`
* *Defense:* `safety: 65`, `doc: 6`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 24.866
  * `Choke Point (Betweenness):` 0.013775 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` enum, .statement, collections.abc, angr.calling_conventions, typing_extensions, typing, angr.sim_type, abc...
  * `Imported By (In-Degree: 139):` (Excluded from Brief to save tokens)

### `angr/analyses/decompiler/clinic.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.816 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.644 IQR)
- **Top Global Matches:** file_cluster_8: 12.816, file_cluster_13: 12.85, file_cluster_0: 12.906
- **Magnitude:** 4206.9 | **LOC:** 3763 | **CtrlFlow:** 68.1% | **Authorship Centralization:** 57.1%
- **Algorithmic:** O(N^6) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (35.589%), Tech Debt (16.7838%)
**Top Internal Functions/Classes:**
  * `_stage_semantic_variable_naming` (Impact: 923.1 | O(N^6) | DB: 13)
  * `_make_function_prototype` (Impact: 443.9 | O(N^6) | DB: 3)
  * `remove_empty_nodes` (Impact: 241.4 | O(N^6))
  * `_constrain_callee_prototypes` (Impact: 203.0 | O(N^6) | DB: 4)
  * `_rewrite_alloca` (Impact: 197.5 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 867`, `structural_boundaries: 406`, `args: 105`, `func_start: 100`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 298`, `dead_code: 13`, `planned_debt: 9`, `fragile_debt: 5`, `duplicate_logic: 2`
* *Architecture:* `api: 24`, `import: 47`
* *Defense:* `safety: 203`, `doc: 87`, `test: 35`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.977
  * `Choke Point (Betweenness):` 0.010811 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` .stack_item, .ail_simplifier, angr.errors, angr.utils.ssa, angr.procedures.stubs.UnresolvableCallTarget, .return_maker, .peephole_optimizations, angr.analyses.s_liveness...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `angr/state_plugins/unicorn_engine.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.03 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.764 IQR)
- **Top Global Matches:** file_cluster_8: 12.03, file_cluster_13: 12.084, file_cluster_7: 12.247
- **Magnitude:** 3969.6 | **LOC:** 1920 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 99
- **Risk Profile:** Cognitive Load (56.0859%), Tech Debt (19.9273%)
**Top Internal Functions/Classes:**
  * `_load_native` (Impact: 3530.5 | O(2^N) | DB: 99)
  * `name_stop` (Impact: 17.6 | O(N^4))
  * `__init__` (Impact: 10.5 | O(N^2) | DB: 6)
    * *Intent:* # # Because Unicorn leaks like crazy, we use one Uc object per thread...
  * `hook_add` (Impact: 9.2 | O(2^N))
  * `mem_map_ptr` (Impact: 7.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 303`, `structural_boundaries: 200`, `args: 68`, `func_start: 67`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 13`, `state_mutation: 254`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 54`, `concurrency: 7`, `import: 25`
* *Defense:* `safety: 25`, `doc: 46`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.332
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` angr.engines.vex.claripy.irop, angr.errors, archinfo, binascii, sys, ctypes, time, pyvex...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `angr/analyses/disassembly.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.15 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.077 IQR)
- **Top Global Matches:** file_cluster_13: 13.15, file_cluster_11: 13.293, file_cluster_0: 13.3
- **Magnitude:** 3861.7 | **LOC:** 1351 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (86.3449%), Tech Debt (99.9433%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 1580.7 | O(2^N) | DB: 46)
  * `_render` (Impact: 421.5 | O(2^N) | DB: 41)
  * `format_comment` (Impact: 417.0 | O(2^N) | DB: 11)
  * `dissect_instruction_by_default` (Impact: 205.1 | O(N^6) | DB: 9)
  * `parse_block` (Impact: 84.8 | O(N^4) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 330`, `structural_boundaries: 259`, `args: 94`, `func_start: 89`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 396`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 2`, `duplicate_logic: 25`
* *Architecture:* `api: 64`, `import: 19`
* *Defense:* `safety: 55`, `doc: 13`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.505
  * `Choke Point (Betweenness):` 0.001227 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` .disassembly_utils, angr.errors, archinfo, pyvex, angr.engines, typing, angr.knowledge_plugins, angr.utils.formatting...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `angr/analyses/typehoon/simple_solver.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.603 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.692 IQR)
- **Top Global Matches:** file_cluster_8: 12.603, file_cluster_16: 12.609, file_cluster_0: 12.65
- **Magnitude:** 3854.9 | **LOC:** 2141 | **CtrlFlow:** 70.1% | **Authorship Centralization:** 77.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (39.1406%), Tech Debt (65.9345%)
**Top Internal Functions/Classes:**
  * `_discover_equivalence` (Impact: 1047.1 | O(2^N))
  * `lookup` (Impact: 674.1 | O(2^N) | DB: 10)
  * `solve` (Impact: 255.7 | O(N^6) | DB: 1)
  * `_constraint_graph_saturate` (Impact: 156.3 | O(N^6) | DB: 1)
  * `compute_quotient_graph` (Impact: 138.3 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 616`, `structural_boundaries: 263`, `args: 74`, `func_start: 70`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 121`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 12`
* *Architecture:* `api: 29`, `import: 13`
* *Defense:* `safety: 207`, `doc: 70`, `test: 13`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.348
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` enum, angr.utils.constants, .variance, pprint, logging, networkx.drawing.nx_agraph, collections, .dfa...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `angr/analyses/decompiler/ail_simplifier.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.407 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.776 IQR)
- **Top Global Matches:** file_cluster_13: 12.407, file_cluster_8: 12.428, file_cluster_0: 12.499
- **Magnitude:** 3472.36 | **LOC:** 2274 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 45.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (45.0995%), Tech Debt (21.1961%)
**Top Internal Functions/Classes:**
  * `_unify_local_variables` (Impact: 2352.2 | O(N^6) | DB: 14)
  * `_rewrite_phi_const_exprs` (Impact: 166.8 | O(N^6))
  * `_compute_effective_sizes` (Impact: 164.0 | O(N^5))
  * `_narrow_exprs` (Impact: 162.0 | O(N^6))
  * `_compute_equivalence` (Impact: 98.8 | O(N^6))
    * *Intent:* # gp=self._gp,
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 623`, `structural_boundaries: 335`, `args: 56`, `func_start: 53`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 117`, `dead_code: 7`, `planned_debt: 4`, `fragile_debt: 2`, `duplicate_logic: 3`
* *Architecture:* `api: 10`, `import: 33`
* *Defense:* `safety: 137`, `doc: 37`, `test: 26`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.423
  * `Choke Point (Betweenness):` 0.002216 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` angr.knowledge_plugins.propagations.states, angr.ailment, angr.ailment.statement, angr.errors, angr.utils.ssa, angr.analyses.s_propagator, angr.knowledge_plugins.key_definitions.definition, angr.knowledge_plugins.functions.function...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `angr/analyses/ddg.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.277 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.704 IQR)
- **Top Global Matches:** file_cluster_13: 13.277, file_cluster_0: 13.3, file_cluster_11: 13.343
- **Magnitude:** 3083.74 | **LOC:** 1671 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (30.0596%), Tech Debt (99.5146%)
**Top Internal Functions/Classes:**
  * `add_def` (Impact: 778.2 | O(2^N) | DB: 10)
    * *Intent:* """ Make a hard copy of `self`. :return: A new LiveDefinition instance. :rtype: angr.analyses.ddg.Li...
  * `_construct` (Impact: 248.4 | O(N^6) | DB: 1)
  * `_handle_tmp_write` (Impact: 179.1 | O(N^5))
  * `_track` (Impact: 153.0 | O(N^5) | DB: 9)
  * `_handle_operation` (Impact: 130.3 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 315`, `structural_boundaries: 213`, `args: 78`, `func_start: 75`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 190`, `dead_code: 8`, `planned_debt: 10`, `fragile_debt: 2`, `duplicate_logic: 15`
* *Architecture:* `api: 51`, `import: 10`
* *Defense:* `safety: 37`, `doc: 183`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.398
  * `Choke Point (Betweenness):` 5.1e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` pyvex, angr.code_location, logging, collections, angr.sim_variable, angr.analyses, angr.errors, networkx...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `angr/knowledge_plugins/functions/function.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.158 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.173 IQR)
- **Top Global Matches:** file_cluster_0: 13.158, file_cluster_13: 13.282, file_cluster_11: 13.34
- **Magnitude:** 3031.72 | **LOC:** 2086 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (45.6951%), Tech Debt (99.5228%)
**Top Internal Functions/Classes:**
  * `find_declaration` (Impact: 691.5 | O(N^6) | DB: 20)
  * `dbg_print` (Impact: 300.1 | O(N^6) | DB: 8)
  * `local_runtime_values` (Impact: 144.0 | O(N^6) | DB: 3)
  * `prototype` (Impact: 98.1 | O(N^6) | DB: 3)
    * *Intent:* # update the cache if self._function_manager is not None: self._function_manager.set_function_return...
  * `_init_prototype_and_calling_convention` (Impact: 79.2 | O(N^5) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 405`, `structural_boundaries: 365`, `args: 119`, `func_start: 118`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 289`, `dead_code: 8`, `planned_debt: 6`, `fragile_debt: 3`, `duplicate_logic: 24`
* *Architecture:* `io: 1`, `api: 137`, `import: 32`
* *Defense:* `safety: 46`, `doc: 176`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.488
  * `Choke Point (Betweenness):` 0.002175 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` json, angr.knowledge_plugins.xrefs.xref, angr.project, angr.errors, os, functools, angr.calling_conventions, angr.knowledge_plugins.cfg.memory_data...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `angr/analyses/identifier/identify.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.359 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.146 IQR)
- **Top Global Matches:** file_cluster_13: 11.359, file_cluster_8: 11.373, file_cluster_0: 11.438
- **Magnitude:** 2828.74 | **LOC:** 826 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (68.7354%), Tech Debt (27.0311%)
**Top Internal Functions/Classes:**
  * `do_trace` (Impact: 1977.6 | O(2^N) | DB: 9)
    * *Intent:* # get to the callsite s = self.make_symbolic_state(self.project, self._reg_list, stack_length=200) s...
  * `__init__` (Impact: 362.4 | O(N^5) | DB: 17)
    * *Intent:* # self.project = project if not isinstance(self.project.loader.main_object, CGC): l.critical("The id...
  * `identify_func` (Impact: 80.2 | O(N^4))
  * `can_call_same_name` (Impact: 56.9 | O(N^6) | DB: 2)
  * `_no_sp_or_bp` (Impact: 42.8 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 138`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 13`, `state_mutation: 100`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 15`, `import: 13`
* *Defense:* `safety: 25`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.52
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .errors, logging, networkx, collections, itertools, angr.analyses, .runner, angr...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `angr/analyses/bindiff.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.683 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.769 IQR)
- **Top Global Matches:** file_cluster_0: 13.683, file_cluster_11: 13.722, file_cluster_13: 13.781
- **Magnitude:** 2747.58 | **LOC:** 1512 | **CtrlFlow:** 66.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 59
- **Risk Profile:** Cognitive Load (45.6899%), Tech Debt (28.1093%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 1284.1 | O(N^6) | DB: 59)
  * `_compute_diff` (Impact: 360.1 | O(N^6) | DB: 8)
  * `_approximate_matcher_func_string_refs` (Impact: 223.6 | O(N^6) | DB: 7)
  * `compare_statement_dict` (Impact: 166.9 | O(2^N))
  * `_get_approximate_matches_between_matched` (Impact: 147.9 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 379`, `structural_boundaries: 192`, `args: 60`, `func_start: 54`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 236`, `dead_code: 15`, `planned_debt: 5`, `duplicate_logic: 3`
* *Architecture:* `api: 29`, `import: 12`
* *Defense:* `safety: 28`, `doc: 135`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.345
  * `Choke Point (Betweenness):` 0.000304 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` functools, angr.knowledge_plugins.cfg.memory_data, logging, types, typing, collections, angr.analyses, angr.knowledge_plugins...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `angr/analyses/decompiler/utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.338 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.998 IQR)
- **Top Global Matches:** file_cluster_13: 12.338, file_cluster_8: 12.405, file_cluster_16: 12.469
- **Magnitude:** 2733.26 | **LOC:** 1241 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (16.6339%), Tech Debt (36.1627%)
**Top Internal Functions/Classes:**
  * `insert_node` (Impact: 621.5 | O(2^N) | DB: 4)
  * `switch_extract_bitwiseand_jumptable_info` (Impact: 268.8 | O(N^5))
  * `switch_extract_cmp_bounds_from_condition` (Impact: 164.9 | O(N^5))
  * `switch_extract_switch_expr_from_jump_tar` (Impact: 152.8 | O(N^5))
  * `remove_last_statement` (Impact: 131.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 391`, `structural_boundaries: 259`, `args: 52`, `func_start: 52`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 54`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 2`, `api: 73`, `import: 22`
* *Defense:* `safety: 112`, `doc: 52`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.623
  * `Choke Point (Betweenness):` 0.004357 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` angr.analyses.decompiler.peephole_optimizations.base, angr.analyses.decompiler.structuring, angr.ailment, angr.analyses.decompiler.decompilation_options, pathlib, .seq_to_blocks, typing, angr.ailment.block...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `tests/analyses/decompiler/test_decompiler.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.13 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.131 IQR)
- **Top Global Matches:** file_cluster_0: 13.13, file_cluster_17: 13.504, file_cluster_8: 13.53
- **Magnitude:** 2727.5 | **LOC:** 5443 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 44.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 360
- **Risk Profile:** Cognitive Load (4.1679%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_decompiling_nl_i386_pie` (Impact: 1208.9 | O(N^5) | DB: 360)
    * *Intent:* # Current decompilation output: # do # { # v1 = v0 + 1; # v3 = v2 + 1; # *(v2) = *(v0); # v0 = v1; #...
  * `test_decompiling_livectf_dc30_open_to_in` (Impact: 210.7 | O(N^4) | DB: 39)
  * `test_decompiling_armhf_float_int_convers` (Impact: 154.0 | O(N^4) | DB: 15)
  * `test_decompiling_rust_fmt_main` (Impact: 144.2 | O(N^4) | DB: 13)
    * *Intent:* # ensure we do not have redundant masking # ensure that we do not have multi-statement expressions i...
  * `test_decompiling_1after909_doit` (Impact: 77.9 | O(N^5) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 488`, `structural_boundaries: 1110`, `args: 228`, `func_start: 228`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 16`, `dead_code: 41`, `planned_debt: 19`, `fragile_debt: 16`, `duplicate_logic: 3`, `orphaned_logic: 45`
* *Architecture:* `io: 220`, `api: 226`, `import: 22`
* *Defense:* `safety: 762`, `doc: 70`, `test: 946`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.281
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` angr.analyses.decompiler.structuring, angr.ailment, os, angr.analyses.decompiler.decompilation_options, functools, time, angr.sim_type, unittest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `angr/knowledge_plugins/variables/variable_manager.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.776 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.169 IQR)
- **Top Global Matches:** file_cluster_13: 12.776, file_cluster_16: 12.792, file_cluster_8: 12.908
- **Magnitude:** 2705.6 | **LOC:** 1386 | **CtrlFlow:** 58.0% | **Authorship Centralization:** 62.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (37.8471%), Tech Debt (18.7625%)
**Top Internal Functions/Classes:**
  * `parse_from_cmessage` (Impact: 1973.7 | O(2^N) | DB: 9)
    * *Intent:* # TODO: Types
  * `serialize_to_cmessage` (Impact: 264.9 | O(2^N) | DB: 23)
  * `get_variable_accesses` (Impact: 142.4 | O(2^N) | DB: 2)
  * `find_variable_by_stmt` (Impact: 10.2 | O(N^3))
  * `__getstate__` (Impact: 8.5 | O(N^3))
    * *Intent:* # # Serialization
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 335`, `structural_boundaries: 243`, `args: 83`, `func_start: 72`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 181`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 68`, `import: 24`
* *Defense:* `safety: 56`, `doc: 83`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.93
  * `Choke Point (Betweenness):` 0.001178 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` angr.knowledge_plugins.plugin, angr.knowledge_plugins.types, angr.keyed_region, cle.backends.elf.compilation_unit, typing, angr.sim_type, .variable_access, angr...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `angr/storage/file.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.753 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.831 IQR)
- **Top Global Matches:** file_cluster_0: 12.753, file_cluster_13: 12.876, file_cluster_17: 12.95
- **Magnitude:** 2636.14 | **LOC:** 1213 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (46.7681%), Tech Debt (95.7811%)
**Top Internal Functions/Classes:**
  * `read` (Impact: 1664.6 | O(2^N) | DB: 28)
  * `_prep_generic` (Impact: 501.4 | O(N^4) | DB: 22)
  * `set_state` (Impact: 42.4 | O(2^N) | DB: 2)
  * `__init__` (Impact: 34.6 | O(2^N) | DB: 6)
  * `make_ident` (Impact: 32.1 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 245`, `args: 97`, `func_start: 97`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 5`, `state_mutation: 175`, `dead_code: 2`, `planned_debt: 5`, `duplicate_logic: 10`
* *Architecture:* `api: 96`, `import: 9`
* *Defense:* `safety: 22`, `doc: 113`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.848
  * `Choke Point (Betweenness):` 0.000245 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` angr.state_plugins.plugin, logging, angr.state_plugins.sim_action_object, itertools, angr, angr.errors, .memory_mixins, claripy...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `angr/knowledge_plugins/cfg/cfg_model.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.27 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.786 IQR)
- **Top Global Matches:** file_cluster_13: 12.27, file_cluster_16: 12.417, file_cluster_11: 12.491
- **Magnitude:** 2454.92 | **LOC:** 1221 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 71.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (38.6277%), Tech Debt (55.7937%)
**Top Internal Functions/Classes:**
  * `serialize_to_cmessage` (Impact: 2027.4 | O(2^N) | DB: 23)
  * `clear_region_for_reflow` (Impact: 95.3 | O(N^6) | DB: 2)
  * `_guess_data_type_elfheader` (Impact: 36.1 | O(N^4))
    * *Intent:* # Is it an unicode string? # TODO: Support unicode string longer than the max length if len(data) >=...
  * `addr_type` (Impact: 28.0 | O(2^N) | DB: 1)
  * `mark_node_addr_has_return` (Impact: 12.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 283`, `structural_boundaries: 191`, `args: 50`, `func_start: 50`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 106`, `dead_code: 1`, `planned_debt: 7`, `fragile_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 49`, `import: 24`
* *Defense:* `safety: 30`, `doc: 110`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.478
  * `Choke Point (Betweenness):` 0.002155 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` sortedcontainers, angr.errors, .types, angr.knowledge_plugins.xrefs, typing, networkx, .indirect_jump, .cfg_node...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `angr/state_plugins/solver.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.069 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.756 IQR)
- **Top Global Matches:** file_cluster_0: 12.069, file_cluster_16: 12.308, file_cluster_13: 12.363
- **Magnitude:** 2289.26 | **LOC:** 1129 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (15.7099%), Tech Debt (10.0968%)
**Top Internal Functions/Classes:**
  * `timed_function` (Impact: 2129.5 | O(2^N) | DB: 27)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 247`, `args: 92`, `func_start: 92`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 8`, `state_mutation: 63`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 84`, `import: 15`
* *Defense:* `safety: 25`, `doc: 160`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.501
  * `Choke Point (Betweenness):` 0.000363 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` functools, time, .sim_action, logging, typing, angr.sim_state, angr.utils.balancer, .inspect...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `angr/procedures/definitions/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.586 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.445 IQR)
- **Top Global Matches:** file_cluster_13: 12.586, file_cluster_11: 12.697, file_cluster_16: 12.786
- **Magnitude:** 2276.3 | **LOC:** 1053 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 66
- **Risk Profile:** Cognitive Load (25.0609%), Tech Debt (45.0385%)
**Top Internal Functions/Classes:**
  * `get` (Impact: 2131.6 | O(2^N) | DB: 66)
    * *Intent:* """ self.types[name] = t def get(self, name: str, bottom_on_missing: bool = False, memo: set[str] | ...
  * `set_names` (Impact: 7.1 | O(N^3) | DB: 1)
  * `__contains__` (Impact: 5.3 | O(N^2))
  * `add` (Impact: 3.2 | O(N^2))
  * `__init__` (Impact: 2.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 208`, `args: 72`, `func_start: 70`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 57`, `dead_code: 1`, `planned_debt: 22`, `fragile_debt: 1`
* *Architecture:* `io: 14`, `api: 58`, `import: 27`
* *Defense:* `safety: 25`, `doc: 195`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.281
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` json, angr.misc, angr.errors, archinfo, angr.procedures.stubs.syscall_stub, os, angr.calling_conventions, typing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `angr/analyses/decompiler/condition_processor.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.552 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.685 IQR)
- **Top Global Matches:** file_cluster_8: 11.552, file_cluster_13: 11.7, file_cluster_11: 11.763
- **Magnitude:** 2272.22 | **LOC:** 1397 | **CtrlFlow:** 57.8% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (26.5489%), Tech Debt (10.048%)
**Top Internal Functions/Classes:**
  * `remove_claripy_bool_asts` (Impact: 368.6 | O(2^N) | DB: 3)
    * *Intent:* # the negation of the union of diverging conditions is the guarding condition for this node cond = c...
  * `get_last_statement` (Impact: 342.6 | O(2^N))
  * `_extract_common_subexpressions` (Impact: 329.7 | O(2^N) | DB: 2)
  * `have_opposite_edge_conditions` (Impact: 178.6 | O(N^5))
  * `recover_edge_condition` (Impact: 142.4 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 361`, `structural_boundaries: 264`, `args: 127`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 87`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 29`, `import: 22`
* *Defense:* `safety: 75`, `doc: 17`, `test: 4`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.287
  * `Choke Point (Betweenness):` 0.000442 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` collections.abc, angr.block, logging, angr.utils.ail, typing, collections, angr.ailment, sympy...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `angr/ailment/expression.py` (PYTHON) | Magnitude: 4567.56 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1632, state_mutation: 566, structural_boundaries: 536, branch: 418
- `angr/engines/pcode/behavior.py` (PYTHON) | Magnitude: 598.18 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 316, structural_boundaries: 205, encapsulation: 115, doc: 114
- `angr/knowledge_plugins/cfg/block_id.py` (PYTHON) | Magnitude: 90.5 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 22, state_mutation: 19, branch: 13
- `angr/knowledge_plugins/cfg/cfg_node.py` (PYTHON) | Magnitude: 784.84 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 574, state_mutation: 156, structural_boundaries: 134, encapsulation: 133
- `native/angr/src/fuzzer/corpus.rs` (RUST) | Magnitude: 583.16 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 334, structural_boundaries: 78, generics: 76, safety: 68

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `angr/analyses/vfg.py` (PYTHON) | Magnitude: 1808.54 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 994, encapsulation: 299, structural_boundaries: 229, branch: 228

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `corpus_tests/scripts/gh_push_file.sh` (SHELL) | Magnitude: 7.85 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 60, io: 36, state_mutation: 22, branch: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `angr/analyses/forward_analysis/forward_analysis.py` (PYTHON) | Magnitude: 604.2 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 290, encapsulation: 178, structural_boundaries: 121, doc: 68
- `angr/utils/graph.py` (PYTHON) | Magnitude: 1083.1 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 540, branch: 204, encapsulation: 135, structural_boundaries: 128
- `angr/analyses/decompiler/region_simplifiers/ifelse.py` (PYTHON) | Magnitude: 248.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 63, branch: 21, structural_boundaries: 14, encapsulation: 14
- `tests/exploration_techniques/test_stub_stasher.py` (PYTHON) | Magnitude: 5.1 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 8, test: 7, encapsulation: 6
- `tests/procedures/posix/test_chroot.py` (PYTHON) | Magnitude: 5.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 9, import: 6, test: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `angr/analyses/purity/engine.py` (PYTHON) | Magnitude: 725.56 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 437, encapsulation: 238, structural_boundaries: 201, branch: 97
- `angr/utils/library.py` (PYTHON) | Magnitude: 99.38 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 98, doc: 30, branch: 28, structural_boundaries: 25
- `angr/utils/tagged_interval_map.py` (PYTHON) | Magnitude: 125.06 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 54, encapsulation: 30, structural_boundaries: 24, branch: 20
- `angr/utils/doms.py` (PYTHON) | Magnitude: 362.58 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 103, encapsulation: 59, branch: 45, structural_boundaries: 30
- `angr/knowledge_plugins/obfuscations.py` (PYTHON) | Magnitude: 19.24 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 8, safety_bypasses: 6, state_mutation: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `angr/analyses/binary_optimizer.py` (PYTHON) | Magnitude: 1528.26 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 369, branch: 152, structural_boundaries: 105, state_mutation: 62
- `angr/analyses/identifier/functions/skip_realloc.py` (PYTHON) | Magnitude: 119.0 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 29, branch: 15, state_mutation: 12
- `angr/analyses/decompiler/optimization_passes/lowered_switch_simplifier.py` (PYTHON) | Magnitude: 2038.94 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 708, branch: 300, state_mutation: 120, structural_boundaries: 114
- `angr/analyses/identifier/functions/skip_calloc.py` (PYTHON) | Magnitude: 96.74 | Delta: **0.128 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 26, branch: 12, args: 6
- `tests/analyses/test_disassembly.py` (PYTHON) | Magnitude: 99.28 | Delta: **0.224 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 149, sec_reflection_metaprogramming: 132, structural_boundaries: 76, safety: 57

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `corpus_tests/scripts/gh_ls.sh` (SHELL) | Magnitude: 17.21 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 112, io: 65, branch: 54, structural_boundaries: 37
- `corpus_tests/scripts/classify_diff.sh` (SHELL) | Magnitude: 17.72 | Delta: **0.133 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 82, state_mutation: 79, branch: 62, io: 54
- `angr/misc/picklable_lock.py` (PYTHON) | Magnitude: 64.18 | Delta: **0.172 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 21, indent_spaces: 20, encapsulation: 17, concurrency: 13
- `corpus_tests/scripts/snapshot_diff.sh` (SHELL) | Magnitude: 38.28 | Delta: **0.263 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 150, state_mutation: 79, io: 72, branch: 68

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `angr/procedures/java_jni/array_operations.py` (PYTHON) | Magnitude: 236.66 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 136, structural_boundaries: 49, api: 25, encapsulation: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `angr/serializable.py` (PYTHON) | Magnitude: 22.36 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 19, indent_spaces: 16, structural_boundaries: 10, api: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `angr/procedures/posix/htonl.py` (PYTHON) | Magnitude: 9.24 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 4, api: 2, import: 2
- `angr/procedures/posix/htons.py` (PYTHON) | Magnitude: 9.24 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 4, api: 2, import: 2
- `tests/perf/perf_concrete_execution.py` (PYTHON) | Magnitude: 4.42 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 9, import: 5, io: 4
- `angr/analyses/decompiler/graph_region.py` (PYTHON) | Magnitude: 827.12 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 326, branch: 126, structural_boundaries: 59, state_mutation: 32
- `angr/knowledge_plugins/callsite_prototypes.py` (PYTHON) | Magnitude: 70.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
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

- `angr/analyses/cfg/cfg_fast.py` -> **Fish** (84.6% isolated ownership) | Magnitude: 9209.58
- `angr/analyses/bindiff.py` -> **pre-commit-ci[bot]** (100.0% isolated ownership) | Magnitude: 2747.58
- `angr/storage/file.py` -> **Fish** (100.0% isolated ownership) | Magnitude: 2636.14
- `angr/analyses/calling_convention/calling_convention.py` -> **Audrey Dutcher** (100.0% isolated ownership) | Magnitude: 2131.32
- `angr/storage/memory_mixins/paged_memory/paged_memory_mixin.py` -> **Fish** (100.0% isolated ownership) | Magnitude: 2127.62

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

- `angr/concretization_strategies/logging.py` -> **Severity: 9260.063** (Blast Radius: 92.601 * Doc Risk: 99.9996%)
- `angr/errors.py` -> **Severity: 3299.2** (Blast Radius: 32.992 * Doc Risk: 100.0%)
- `angr/ailment/expression.py` -> **Severity: 2486.6** (Blast Radius: 24.866 * Doc Risk: 100.0%)
- `angr/sim_type.py` -> **Severity: 2224.0** (Blast Radius: 22.24 * Doc Risk: 100.0%)
- `angr/ailment/statement.py` -> **Severity: 1436.6** (Blast Radius: 14.366 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
