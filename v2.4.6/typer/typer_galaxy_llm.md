# ARCHITECTURAL_BRIEF: typer
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/typer` |
| **Timestamp** | `2026-08-03T21:25:54.659576+00:00` |
| **Scan Duration** | `0.95s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 574 malicious artifacts.

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
| Total Artifacts | 579 |
| Analyzed Artifacts (Scanned) | 575 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4 |
| Total LOC | 16532 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 99.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4194 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5819 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3534 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 20 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 574 | 16532 | 99.8% |
| MARKDOWN | 1 | 0 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.068`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 361 | 62.8% |
| file_cluster_13 | 200 | 34.8% |
| file_cluster_0 | 10 | 1.7% |
| file_cluster_16 | 3 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 36.5 | 5.9 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 1.8 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 36.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 1.8 | 0.2 | 0.0 |
| API Exposure | 0.0 | 12.0 | 3.5 | 3.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 99.9 | 1.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 32.1 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 69.3 | 86.7 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 31.7 | 6.7 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 17.1 | 2.3 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 27.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 31.4 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `typer-0.24.1/tests/test_completion/test_completion_option_colon.py` (Hits: 25)
- `typer-0.24.1/tests/test_completion/test_completion.py` (Hits: 21)
- `typer-0.24.1/tests/test_completion/test_completion_complete.py` (Hits: 21)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **testing.py** (`typer-0.24.1/typer/testing.py`) — 169 inbound connections
2. **utils.py** (`typer-0.24.1/tests/utils.py`) — 14 inbound connections
3. **core.py** (`typer-0.24.1/typer/core.py`) — 13 inbound connections
4. **models.py** (`typer-0.24.1/typer/models.py`) — 8 inbound connections
5. **completion.py** (`typer-0.24.1/typer/completion.py`) — 7 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **main.py** (`typer-0.24.1/typer/main.py`) — 29 outbound dependencies
2. **rich_utils.py** (`typer-0.24.1/typer/rich_utils.py`) — 25 outbound dependencies
3. **core.py** (`typer-0.24.1/typer/core.py`) — 20 outbound dependencies
4. **test_others.py** (`typer-0.24.1/tests/test_others.py`) — 16 outbound dependencies
5. **cli.py** (`typer-0.24.1/typer/cli.py`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `get_help_record` (@ `typer-0.24.1/typer/core.py`) -> Impact: **1029.4** | LOC: 462
  * *Intent:* # Modified version of click.core.Option.get_help_record() # to support Arguments if self.hidden: return None name = self.make_metavar(ctx=ctx) help = ...
- `format_completion` (@ `typer-0.24.1/typer/_completion_classes.py`) -> Impact: **187.0** | LOC: 102
- `solve_typer_info_help` (@ `typer-0.24.1/typer/main.py`) -> Impact: **111.8** | LOC: 35
- `get_params_from_function` (@ `typer-0.24.1/typer/utils.py`) -> Impact: **81.9** | LOC: 80
- `get_typer_from_module` (@ `typer-0.24.1/typer/cli.py`) -> Impact: **72.3** | LOC: 46
  * *Intent:* # Try to get defined app if state.app: obj = getattr(module, state.app, None) if not isinstance(obj, typer.Typer): typer.echo(f"Not a Typer object: --...
- `app_dir` (@ `typer-0.24.1/tests/test_tutorial/test_launch/test_tutorial002.py`) -> Impact: **61.3** | LOC: 14
- `maybe_update_state` (@ `typer-0.24.1/typer/cli.py`) -> Impact: **55.0** | LOC: 19
- `get_command` (@ `typer-0.24.1/typer/main.py`) -> Impact: **49.8** | LOC: 36
- `solve_typer_info_defaults` (@ `typer-0.24.1/typer/main.py`) -> Impact: **36.6** | LOC: 33
- `maybe_add_run_to_cli` (@ `typer-0.24.1/typer/cli.py`) -> Impact: **36.5** | LOC: 11

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `get_help_record` (@ `typer-0.24.1/typer/core.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Modified version of click.core.Option.get_help_record() # to support Arguments if self.hidden: return None name = self.make_metavar(ctx=ctx) help = ...
- `app_dir` (@ `typer-0.24.1/tests/test_tutorial/test_launch/test_tutorial002.py`) -> **O(2^N) [Recursive]**
- `format_completion` (@ `typer-0.24.1/typer/_completion_classes.py`) -> **O(2^N) [Recursive]**
- `delete` (@ `typer-0.24.1/docs_src/commands/help/tutorial001_an_py310.py`) -> **O(2^N) [Recursive]**
- `create` (@ `typer-0.24.1/docs_src/commands/help/tutorial007_an_py310.py`) -> **O(2^N) [Recursive]**
- `format_help` (@ `typer-0.24.1/typer/core.py`) -> **O(2^N) [Recursive]**
- `create` (@ `typer-0.24.1/docs_src/commands/callback/tutorial001_py310.py`) -> **O(2^N) [Recursive]**
- `delete` (@ `typer-0.24.1/docs_src/commands/callback/tutorial001_py310.py`) -> **O(2^N) [Recursive]**
- `delete` (@ `typer-0.24.1/docs_src/commands/help/tutorial001_py310.py`) -> **O(2^N) [Recursive]**
- `create` (@ `typer-0.24.1/docs_src/commands/help/tutorial007_py310.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `get_help_record` (@ `typer-0.24.1/typer/core.py`) -> DB Complexity: **21**
  * *Intent:* # Modified version of click.core.Option.get_help_record() # to support Arguments if self.hidden: return None name = self.make_metavar(ctx=ctx) help = ...
- `format_completion` (@ `typer-0.24.1/typer/_completion_classes.py`) -> DB Complexity: **18**
- `test_script` (@ `typer-0.24.1/tests/test_completion/test_completion_complete_rich.py`) -> DB Complexity: **9**
- `test_completion_untyped_parameters` (@ `typer-0.24.1/tests/test_others.py`) -> DB Complexity: **9**
- `test_completion_untyped_parameters_diffe` (@ `typer-0.24.1/tests/test_others.py`) -> DB Complexity: **9**
- `test_script_completion_run` (@ `typer-0.24.1/tests/test_cli/test_completion_run.py`) -> DB Complexity: **6**
- `test_doc_html_output` (@ `typer-0.24.1/tests/test_cli/test_doc.py`) -> DB Complexity: **6**
- `test_script_completion_run` (@ `typer-0.24.1/tests/test_cli/test_sub_completion.py`) -> DB Complexity: **6**
- `test_install_completion` (@ `typer-0.24.1/tests/test_completion/test_completion.py`) -> DB Complexity: **6**
- `test_completion_source_bash` (@ `typer-0.24.1/tests/test_completion/test_completion.py`) -> DB Complexity: **6**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `typer-0.24.1/typer` | 16 | 3037.18 | 12.82% | 31.29% |
| `typer-0.24.1/tests` | 20 | 802.74 | 4.41% | 0.0% |
| `typer-0.24.1/tests/test_completion` | 13 | 417.82 | 3.49% | 0.0% |
| `typer-0.24.1/tests/test_cli` | 18 | 320.14 | 2.45% | 0.0% |
| `typer-0.24.1/docs_src/options_autocompletion` | 19 | 290.9 | 13.84% | 93.5% |
| `typer-0.24.1/tests/test_tutorial/test_commands/test_help` | 9 | 216.58 | 7.57% | 0.0% |
| `typer-0.24.1/tests/test_tutorial/test_subcommands` | 4 | 152.58 | 2.75% | 0.0% |
| `typer-0.24.1/docs_src/commands/help` | 13 | 149.3 | 5.68% | 91.43% |
| `typer-0.24.1/tests/test_tutorial/test_options_autocompletion` | 9 | 147.96 | 2.77% | 0.0% |
| `typer-0.24.1/tests/test_tutorial/test_arguments/test_help` | 9 | 136.76 | 6.88% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `typer-0.24.1/docs_src/arguments/default/tutorial001_an_py310.py` -> **100.0%** Exposure
- `typer-0.24.1/docs_src/arguments/default/tutorial001_py310.py` -> **100.0%** Exposure
- `typer-0.24.1/docs_src/arguments/envvar/tutorial001_an_py310.py` -> **100.0%** Exposure
- `typer-0.24.1/docs_src/arguments/envvar/tutorial001_py310.py` -> **100.0%** Exposure
- `typer-0.24.1/docs_src/arguments/envvar/tutorial002_py310.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `typer-0.24.1/docs_src/progressbar/tutorial006_py310.py` -> **99.9043%** Exposure
- `typer-0.24.1/typer/models.py` -> **99.8099%** Exposure
- `typer-0.24.1/docs_src/options_autocompletion/tutorial003_py310.py` -> **98.7711%** Exposure
- `typer-0.24.1/docs_src/options_autocompletion/tutorial003_an_py310.py` -> **98.2635%** Exposure
- `typer-0.24.1/docs_src/options_autocompletion/tutorial004_py310.py` -> **94.9664%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `typer-0.24.1/tests/test_others.py` -> **18** Orphaned Functions | **0** Duplicates
- `typer-0.24.1/tests/test_tutorial/test_subcommands/test_tutorial003.py` -> **16** Orphaned Functions | **0** Duplicates
- `typer-0.24.1/tests/test_completion/test_completion_option_colon.py` -> **13** Orphaned Functions | **0** Duplicates
- `typer-0.24.1/tests/test_tutorial/test_commands/test_help/test_tutorial001.py` -> **13** Orphaned Functions | **0** Duplicates
- `typer-0.24.1/tests/test_completion/test_completion_complete.py` -> **6** Orphaned Functions | **5** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`typer-0.24.1/typer/cli.py`** -> AI Confidence: **99.31%**
2. **`typer-0.24.1/typer/core.py`** -> AI Confidence: **99.31%**
3. **`typer-0.24.1/typer/main.py`** -> AI Confidence: **99.31%**
4. **`typer-0.24.1/typer/rich_utils.py`** -> AI Confidence: **99.31%**
5. **`typer-0.24.1/typer/_completion_shared.py`** -> AI Confidence: **99.23%**
6. **`typer-0.24.1/tests/test_tutorial/test_launch/test_tutorial002.py`** -> AI Confidence: **99.18%**
7. **`typer-0.24.1/docs_src/options/help/tutorial002_py310.py`** -> AI Confidence: **99.17%**
8. **`typer-0.24.1/typer/completion.py`** -> AI Confidence: **99.16%**
9. **`typer-0.24.1/tests/test_rich_markup_mode.py`** -> AI Confidence: **99.15%**
10. **`typer-0.24.1/typer/_completion_classes.py`** -> AI Confidence: **99.15%**
11. **`typer-0.24.1/tests/test_completion/test_completion_complete.py`** -> AI Confidence: **99.08%**
12. **`typer-0.24.1/tests/test_completion/test_completion_show.py`** -> AI Confidence: **99.08%**
13. **`typer-0.24.1/tests/test_others.py`** -> AI Confidence: **99.08%**
14. **`typer-0.24.1/tests/test_tutorial/test_app_dir/test_tutorial001.py`** -> AI Confidence: **99.08%**
15. **`typer-0.24.1/tests/test_tutorial/test_arguments/test_envvar/test_tutorial001.py`** -> AI Confidence: **99.08%**
16. **`typer-0.24.1/tests/test_tutorial/test_arguments/test_help/test_tutorial001.py`** -> AI Confidence: **99.08%**
17. **`typer-0.24.1/tests/test_tutorial/test_arguments/test_help/test_tutorial008.py`** -> AI Confidence: **99.08%**
18. **`typer-0.24.1/tests/test_tutorial/test_arguments/test_optional/test_tutorial000.py`** -> AI Confidence: **99.08%**
19. **`typer-0.24.1/tests/test_tutorial/test_arguments/test_optional/test_tutorial001.py`** -> AI Confidence: **99.08%**
20. **`typer-0.24.1/tests/test_tutorial/test_arguments/test_optional/test_tutorial003.py`** -> AI Confidence: **99.08%**
21. **`typer-0.24.1/tests/test_tutorial/test_commands/test_help/test_tutorial004.py`** -> AI Confidence: **99.08%**
22. **`typer-0.24.1/tests/test_tutorial/test_commands/test_help/test_tutorial005.py`** -> AI Confidence: **99.08%**
23. **`typer-0.24.1/tests/test_tutorial/test_commands/test_help/test_tutorial007.py`** -> AI Confidence: **99.08%**
24. **`typer-0.24.1/tests/test_tutorial/test_exceptions/test_tutorial001.py`** -> AI Confidence: **99.08%**
25. **`typer-0.24.1/tests/test_tutorial/test_exceptions/test_tutorial002.py`** -> AI Confidence: **99.08%**
26. **`typer-0.24.1/tests/test_tutorial/test_options/test_callback/test_tutorial003.py`** -> AI Confidence: **99.08%**
27. **`typer-0.24.1/tests/test_tutorial/test_options/test_callback/test_tutorial004.py`** -> AI Confidence: **99.08%**
28. **`typer-0.24.1/tests/test_tutorial/test_options/test_password/test_tutorial001.py`** -> AI Confidence: **99.08%**
29. **`typer-0.24.1/tests/test_tutorial/test_options/test_required/test_tutorial001_tutorial002.py`** -> AI Confidence: **99.08%**
30. **`typer-0.24.1/tests/test_tutorial/test_options/test_version/test_tutorial001.py`** -> AI Confidence: **99.08%**
31. **`typer-0.24.1/tests/test_tutorial/test_options/test_version/test_tutorial002.py`** -> AI Confidence: **99.08%**
32. **`typer-0.24.1/tests/test_tutorial/test_options/test_version/test_tutorial003.py`** -> AI Confidence: **99.08%**
33. **`typer-0.24.1/tests/test_tutorial/test_options_autocompletion/test_tutorial002.py`** -> AI Confidence: **99.08%**
34. **`typer-0.24.1/tests/test_tutorial/test_options_autocompletion/test_tutorial003.py`** -> AI Confidence: **99.08%**
35. **`typer-0.24.1/tests/test_tutorial/test_options_autocompletion/test_tutorial004_tutorial005.py`** -> AI Confidence: **99.08%**
36. **`typer-0.24.1/tests/test_tutorial/test_options_autocompletion/test_tutorial007.py`** -> AI Confidence: **99.08%**
37. **`typer-0.24.1/tests/test_tutorial/test_options_autocompletion/test_tutorial008.py`** -> AI Confidence: **99.08%**
38. **`typer-0.24.1/tests/test_tutorial/test_options_autocompletion/test_tutorial009.py`** -> AI Confidence: **99.08%**
39. **`typer-0.24.1/tests/test_tutorial/test_parameter_types/test_bool/test_tutorial002.py`** -> AI Confidence: **99.08%**
40. **`typer-0.24.1/tests/test_tutorial/test_parameter_types/test_file/test_tutorial001.py`** -> AI Confidence: **99.08%**
41. **`typer-0.24.1/tests/test_tutorial/test_parameter_types/test_file/test_tutorial002.py`** -> AI Confidence: **99.08%**
42. **`typer-0.24.1/tests/test_tutorial/test_parameter_types/test_file/test_tutorial003.py`** -> AI Confidence: **99.08%**
43. **`typer-0.24.1/tests/test_tutorial/test_parameter_types/test_file/test_tutorial004.py`** -> AI Confidence: **99.08%**
44. **`typer-0.24.1/tests/test_tutorial/test_parameter_types/test_file/test_tutorial005.py`** -> AI Confidence: **99.08%**
45. **`typer-0.24.1/tests/test_tutorial/test_parameter_types/test_number/test_tutorial001.py`** -> AI Confidence: **99.08%**
46. **`typer-0.24.1/tests/test_tutorial/test_parameter_types/test_path/test_tutorial001.py`** -> AI Confidence: **99.08%**
47. **`typer-0.24.1/tests/test_tutorial/test_printing/test_tutorial001.py`** -> AI Confidence: **99.08%**
48. **`typer-0.24.1/tests/test_tutorial/test_printing/test_tutorial002.py`** -> AI Confidence: **99.08%**
49. **`typer-0.24.1/tests/test_tutorial/test_progressbar/test_tutorial001.py`** -> AI Confidence: **99.08%**
50. **`typer-0.24.1/tests/test_tutorial/test_subcommands/test_tutorial001.py`** -> AI Confidence: **99.08%**
51. **`typer-0.24.1/tests/test_tutorial/test_subcommands/test_tutorial003.py`** -> AI Confidence: **99.08%**
52. **`typer-0.24.1/tests/test_tutorial/test_terminating/test_tutorial003.py`** -> AI Confidence: **99.08%**
53. **`typer-0.24.1/typer/__init__.py`** -> AI Confidence: **99.08%**
54. **`typer-0.24.1/typer/params.py`** -> AI Confidence: **99.08%**
55. **`typer-0.24.1/tests/test_completion/test_completion_install.py`** -> AI Confidence: **99.07%**
56. **`typer-0.24.1/tests/test_rich_utils.py`** -> AI Confidence: **99.07%**
57. **`typer-0.24.1/tests/test_tutorial/test_options/test_password/test_tutorial002.py`** -> AI Confidence: **99.07%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `typer-0.24.1/tests/test_rich_utils.py` -> **0.0001%** Exposure
### Exploit Generation Surface
- `typer-0.24.1/tests/test_cli/test_app_other_name.py` -> **100.0%** Exposure
- `typer-0.24.1/tests/test_cli/test_doc.py` -> **100.0%** Exposure
- `typer-0.24.1/tests/test_cli/test_extending_app.py` -> **100.0%** Exposure
- `typer-0.24.1/tests/test_cli/test_extending_empty_app.py` -> **100.0%** Exposure
- `typer-0.24.1/tests/test_cli/test_help.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `typer-0.24.1/tests/test_cli/test_app_other_name.py` -> **100.0%** Exposure
- `typer-0.24.1/tests/test_cli/test_completion_run.py` -> **100.0%** Exposure
- `typer-0.24.1/tests/test_cli/test_doc.py` -> **100.0%** Exposure
- `typer-0.24.1/tests/test_cli/test_empty_script.py` -> **100.0%** Exposure
- `typer-0.24.1/tests/test_cli/test_extending_app.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `typer-0.24.1/tests/test_cli/test_doc.py` -> **100.0%** Exposure
- `typer-0.24.1/tests/test_cli/test_extending_app.py` -> **100.0%** Exposure
- `typer-0.24.1/tests/test_cli/test_multi_app.py` -> **100.0%** Exposure
- `typer-0.24.1/tests/test_cli/test_multi_app_cli.py` -> **100.0%** Exposure
- `typer-0.24.1/tests/test_cli/test_multi_func.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1533` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `typer-0.24.1/typer/utils.py` (PYTHON) -> Cumulative Risk: **756.62**
- **Archetype:** `file_cluster_16` (Distance: 9.544 IQR)
- **Magnitude:** 179.2 | **LOC:** 198 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (99.9998%), Tech Debt (99.9995%), Algorithmic Dos (99.9937%)
- **Heaviest Functions:** `get_params_from_function` (Impact: 81.9), `__str__` (Impact: 17.8), `parse_boolean_env_var` (Impact: 10.8)

### 2. `typer-0.24.1/typer/_completion_classes.py` (PYTHON) -> Cumulative Risk: **727.18**
- **Archetype:** `file_cluster_13` (Distance: 12.478 IQR)
- **Magnitude:** 259.12 | **LOC:** 200 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9999%)
- **Heaviest Functions:** `format_completion` (Impact: 187.0), `get_completion_args` (Impact: 14.4), `get_completion_args` (Impact: 7.5)

### 3. `typer-0.24.1/typer/core.py` (PYTHON) -> Cumulative Risk: **703.41**
- **Archetype:** `file_cluster_13` (Distance: 10.872 IQR)
- **Magnitude:** 1167.08 | **LOC:** 822 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Verification (80.0%)
- **Heaviest Functions:** `get_help_record` (Impact: 1029.4), `format_help` (Impact: 24.5), `_split_opt` (Impact: 9.3)

### 4. `typer-0.24.1/typer/main.py` (PYTHON) -> Cumulative Risk: **653.12**
- **Archetype:** `file_cluster_8` (Distance: 11.181 IQR)
- **Magnitude:** 616.16 | **LOC:** 2014 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9996%), Verification (80.0%)
- **Heaviest Functions:** `solve_typer_info_help` (Impact: 111.8), `get_command` (Impact: 49.8), `solve_typer_info_defaults` (Impact: 36.6)

### 5. `typer-0.24.1/docs_src/options_autocompletion/tutorial003_py310.py` (PYTHON) -> Cumulative Risk: **647.32**
- **Archetype:** `file_cluster_8` (Distance: 9.676 IQR)
- **Magnitude:** 20.86 | **LOC:** 28 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.708%), State Flux (98.7711%)
- **Heaviest Functions:** `complete_name` (Impact: 12.3), `main` (Impact: 3.2)

### 6. `typer-0.24.1/docs_src/options_autocompletion/tutorial003_an_py310.py` (PYTHON) -> Cumulative Risk: **642.1**
- **Archetype:** `file_cluster_13` (Distance: 9.457 IQR)
- **Magnitude:** 20.88 | **LOC:** 30 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9999%), Tech Debt (99.548%), Algorithmic Dos (98.3849%)
- **Heaviest Functions:** `complete_name` (Impact: 12.3), `main` (Impact: 3.2)

### 7. `typer-0.24.1/docs_src/options_autocompletion/tutorial004_py310.py` (PYTHON) -> Cumulative Risk: **624.1**
- **Archetype:** `file_cluster_8` (Distance: 9.063 IQR)
- **Magnitude:** 20.96 | **LOC:** 33 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9982%), Tech Debt (98.2394%), Algorithmic Dos (98.0361%)
- **Heaviest Functions:** `complete_name` (Impact: 12.3), `main` (Impact: 3.2)

### 8. `typer-0.24.1/docs_src/options_autocompletion/tutorial004_an_py310.py` (PYTHON) -> Cumulative Risk: **619.87**
- **Archetype:** `file_cluster_13` (Distance: 9.04 IQR)
- **Magnitude:** 20.98 | **LOC:** 35 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.997%), Algorithmic Dos (97.9408%), Tech Debt (97.7023%)
- **Heaviest Functions:** `complete_name` (Impact: 12.3), `main` (Impact: 3.2)

### 9. `typer-0.24.1/typer/models.py` (PYTHON) -> Cumulative Risk: **603.48**
- **Archetype:** `file_cluster_16` (Distance: 10.425 IQR)
- **Magnitude:** 145.14 | **LOC:** 652 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (99.9999%), State Flux (99.8099%), Tech Debt (99.6638%)
- **Heaviest Functions:** `__init__` (Impact: 4.0), `__init__` (Impact: 4.0), `__init__` (Impact: 4.0)

### 10. `typer-0.24.1/typer/cli.py` (PYTHON) -> Cumulative Risk: **587.71**
- **Archetype:** `file_cluster_8` (Distance: 9.939 IQR)
- **Magnitude:** 259.98 | **LOC:** 318 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (96.1449%)
- **Heaviest Functions:** `get_typer_from_module` (Impact: 72.3), `maybe_update_state` (Impact: 55.0), `maybe_add_run_to_cli` (Impact: 36.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `typer-0.24.1/typer/core.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.872 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.061 IQR)
- **Top Global Matches:** file_cluster_13: 10.872, file_cluster_16: 10.961, file_cluster_8: 10.989
- **Magnitude:** 1167.08 | **LOC:** 822 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (30.219%), Tech Debt (54.9718%)
**Top Internal Functions/Classes:**
  * `get_help_record` (Impact: 1029.4 | O(2^N) | DB: 21)
    * *Intent:* # Modified version of click.core.Option.get_help_record() # to support Arguments if self.hidden: ret...
  * `format_help` (Impact: 24.5 | O(2^N))
  * `_split_opt` (Impact: 9.3 | O(N^2))
    * *Intent:* # Copy from click.parser._split_opt
  * `list_commands` (Impact: 5.4 | O(N^2))
    * *Intent:* """Returns a list of subcommand names. Note that in Click's Group class, these are sorted. In Typer,...
  * `__init__` (Impact: 3.5 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 134`, `args: 34`, `func_start: 34`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 49`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 15`, `api: 20`, `import: 26`
* *Defense:* `safety: 30`, `doc: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 47.136
  * `Choke Point (Betweenness):` 0.000452 | `Ripple Effect (Closeness):` 0.115184
  * `Imports (Out-Degree: 2):` click, click.utils, collections.abc, inspect, ._typing, gettext, click.types, difflib...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `typer-0.24.1/typer/main.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.181 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.128 IQR)
- **Top Global Matches:** file_cluster_8: 11.181, file_cluster_16: 11.247, file_cluster_13: 11.344
- **Magnitude:** 616.16 | **LOC:** 2014 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (12.6192%), Tech Debt (25.4487%)
**Top Internal Functions/Classes:**
  * `solve_typer_info_help` (Impact: 111.8 | O(N^4))
  * `get_command` (Impact: 49.8 | O(N^3) | DB: 4)
  * `solve_typer_info_defaults` (Impact: 36.6 | O(N^4))
  * `internal_convertor` (Impact: 34.5 | O(N^3))
  * `wrapper` (Impact: 30.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 180`, `args: 39`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 80`, `high_risk_execution: 2`, `state_mutation: 73`, `duplicate_logic: 7`
* *Architecture:* `io: 13`, `api: 38`, `import: 27`
* *Defense:* `safety: 35`, `doc: 154`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 106.494
  * `Choke Point (Betweenness):` 0.004805 | `Ripple Effect (Closeness):` 0.149826
  * `Imports (Out-Degree: 7):` click, inspect, collections.abc, subprocess, platform, ._typing, shutil, .add...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `typer-0.24.1/typer/cli.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.939 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.283 IQR)
- **Top Global Matches:** file_cluster_8: 9.939, file_cluster_13: 9.958, file_cluster_16: 10.195
- **Magnitude:** 259.98 | **LOC:** 318 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (30.5894%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_typer_from_module` (Impact: 72.3 | O(N^4) | DB: 3)
    * *Intent:* # Try to get defined app if state.app: obj = getattr(module, state.app, None) if not isinstance(obj,...
  * `maybe_update_state` (Impact: 55.0 | O(N^5) | DB: 3)
  * `maybe_add_run_to_cli` (Impact: 36.5 | O(N^5))
  * `get_typer_from_state` (Impact: 21.6 | O(N^3) | DB: 3)
  * `callback` (Impact: 12.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 57`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 6`
* *Architecture:* `io: 4`, `api: 16`, `import: 14`
* *Defense:* `safety: 17`, `doc: 4`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.738
  * `Choke Point (Betweenness):` 0.000123 | `Ripple Effect (Closeness):` 0.001742
  * `Imports (Out-Degree: 1):` click, typer.core, , importlib.util, pathlib, sys, typing, typer...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `typer-0.24.1/typer/_completion_classes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.478 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.823 IQR)
- **Top Global Matches:** file_cluster_13: 12.478, file_cluster_6: 12.668, file_cluster_16: 12.7
- **Magnitude:** 259.12 | **LOC:** 200 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (10.8929%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `format_completion` (Impact: 187.0 | O(2^N) | DB: 18)
  * `get_completion_args` (Impact: 14.4 | O(N^3) | DB: 3)
  * `get_completion_args` (Impact: 7.5 | O(N^3) | DB: 6)
  * `_sanitize_help_text` (Impact: 6.4 | O(N^2))
    * *Intent:* """Sanitizes the help text by removing rich tags"""
  * `complete` (Impact: 5.4 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 60`, `args: 18`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `dead_code: 5`, `planned_debt: 3`, `duplicate_logic: 6`
* *Architecture:* `io: 9`, `api: 22`, `import: 11`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.264
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.083545
  * `Imports (Out-Degree: 1):` click, , importlib.util, click.parser, sys, typing, ._completion_shared, re...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `typer-0.24.1/typer/utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.544 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.314 IQR)
- **Top Global Matches:** file_cluster_16: 9.544, file_cluster_8: 9.563, file_cluster_13: 9.654
- **Magnitude:** 179.2 | **LOC:** 198 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (18.8905%), Tech Debt (99.9995%)
**Top Internal Functions/Classes:**
  * `get_params_from_function` (Impact: 81.9 | O(N^5))
  * `__str__` (Impact: 17.8 | O(N^3))
  * `parse_boolean_env_var` (Impact: 10.8 | O(N^2))
  * `__str__` (Impact: 10.7 | O(N^3))
  * `__str__` (Impact: 10.7 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 57`, `args: 12`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 8`, `duplicate_logic: 8`
* *Architecture:* `api: 8`, `import: 6`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.339
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001742
  * `Imports (Out-Degree: 2):` collections.abc, inspect, ._typing, .models, typing, copy
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `typer-0.24.1/tests/test_others.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.299 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.89 IQR)
- **Top Global Matches:** file_cluster_0: 11.299, file_cluster_13: 11.366, file_cluster_8: 11.383
- **Magnitude:** 150.12 | **LOC:** 340 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (2.9605%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_callback_4_list_none` (Impact: 18.4 | O(N^3))
  * `test_too_many_parsers` (Impact: 15.0 | O(N^3))
  * `test_completion_argument` (Impact: 7.8 | O(N^3) | DB: 6)
  * `test_forward_references` (Impact: 6.1 | O(N^2))
  * `test_install_invalid_shell` (Impact: 5.9 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 136`, `args: 39`, `func_start: 39`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `orphaned_logic: 18`
* *Architecture:* `io: 9`, `api: 41`, `import: 17`
* *Defense:* `safety: 43`, `test: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` click, typer.core, unittest, subprocess, typer._completion_shared, pathlib, typer.main, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/typer/models.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.425 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.549 IQR)
- **Top Global Matches:** file_cluster_16: 10.425, file_cluster_8: 10.47, file_cluster_13: 10.717
- **Magnitude:** 145.14 | **LOC:** 652 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (16.3135%), Tech Debt (99.6638%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 4.0 | O(N^3))
  * `__init__` (Impact: 4.0 | O(N^3))
    * *Intent:* *,
  * `__init__` (Impact: 4.0 | O(N^3))
  * `__init__` (Impact: 3.7 | O(N^2))
  * `__init__` (Impact: 2.7 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 59`, `args: 11`, `func_start: 11`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 88`, `planned_debt: 4`, `duplicate_logic: 8`
* *Architecture:* `api: 18`, `import: 9`
* *Defense:* `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.951
  * `Choke Point (Betweenness):` 8.7e-05 | `Ripple Effect (Closeness):` 0.10971
  * `Imports (Out-Degree: 1):` click, io, collections.abc, inspect, warnings, typing, .main, typer...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `typer-0.24.1/typer/rich_utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.867 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.42 IQR)
- **Top Global Matches:** file_cluster_13: 10.867, file_cluster_8: 10.961, file_cluster_16: 11.13
- **Magnitude:** 144.8 | **LOC:** 754 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (34.2965%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `rich_format_error` (Impact: 26.4 | O(N^4))
  * `_get_rich_console` (Impact: 7.1 | O(N^4))
  * `rich_render_text` (Impact: 4.2 | O(N^1))
  * `rich_to_html` (Impact: 2.4 | O(N^1))
  * `escape_before_html_export` (Impact: 2.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 87`, `args: 15`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 60`, `dead_code: 1`
* *Architecture:* `api: 17`, `import: 24`
* *Defense:* `safety: 22`, `doc: 22`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.139
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.001742
  * `Imports (Out-Degree: 2):` click, io, rich.emoji, collections.abc, inspect, rich.markdown, rich.columns, rich.table...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `typer-0.24.1/tests/test_rich_markup_mode.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.151 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.885 IQR)
- **Top Global Matches:** file_cluster_8: 11.151, file_cluster_0: 11.23, file_cluster_17: 11.357
- **Magnitude:** 131.46 | **LOC:** 333 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (1.9839%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_markup_mode_newline_mixed` (Impact: 21.9 | O(N^2))
  * `test_markup_mode_newline_pr815` (Impact: 16.7 | O(N^2))
  * `test_markup_mode_newline_issue447` (Impact: 16.7 | O(N^2))
  * `test_markup_mode_bullets_single_newline` (Impact: 16.7 | O(N^2))
  * `test_markup_mode_bullets_double_newline` (Impact: 16.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 58`, `args: 16`, `func_start: 16`
* *Risk/State:* `orphaned_logic: 9`
* *Architecture:* `io: 2`, `api: 16`, `import: 7`
* *Defense:* `safety: 34`, `doc: 14`, `test: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` subprocess, sys, typer, typer.completion, os, typer.testing, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/typer/completion.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.246 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.498 IQR)
- **Top Global Matches:** file_cluster_8: 8.246, file_cluster_13: 8.319, file_cluster_16: 8.73
- **Magnitude:** 93.68 | **LOC:** 147 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (10.3775%), Tech Debt (17.0432%)
**Top Internal Functions/Classes:**
  * `show_callback` (Impact: 24.9 | O(N^3) | DB: 6)
  * `_install_completion_placeholder_function` (Impact: 16.6 | O(N^2))
    * *Intent:* # Create a fake command function to extract the completion parameters
  * `install_callback` (Impact: 15.5 | O(N^2) | DB: 3)
  * `_install_completion_no_auto_placeholder_` (Impact: 15.3 | O(N^2))
  * `get_completion_inspect_parameters` (Impact: 10.9 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 36`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 10`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 7`, `import: 12`
* *Defense:* `safety: 3`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 35.44
  * `Choke Point (Betweenness):` 0.00178 | `Ripple Effect (Closeness):` 0.11055
  * `Imports (Out-Degree: 4):` click, ._completion_classes, collections.abc, .models, sys, typing, ._completion_shared, .params...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `typer-0.24.1/tests/test_rich_utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.906 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.265 IQR)
- **Top Global Matches:** file_cluster_0: 11.906, file_cluster_8: 11.947, file_cluster_13: 11.948
- **Magnitude:** 82.38 | **LOC:** 225 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (1.7549%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_help_table_alignment_with_styled_te` (Impact: 30.0 | O(N^3))
  * `test_rich_markup_import_regression` (Impact: 11.2 | O(N^3) | DB: 6)
  * `test_rich_doesnt_print_None_default` (Impact: 4.8 | O(N^3))
  * `test_metavar_highlighter` (Impact: 4.2 | O(N^2))
  * `test_rich_utils_click_rewrapp` (Impact: 3.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 71`, `args: 16`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 3`, `orphaned_logic: 8`
* *Architecture:* `io: 2`, `api: 16`, `import: 8`
* *Defense:* `safety: 42`, `doc: 12`, `test: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` typer.rich_utils, sys, typer, typer.completion, typer.testing, tests.utils, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_type_conversion.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.431 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.463 IQR)
- **Top Global Matches:** file_cluster_0: 11.431, file_cluster_8: 11.612, file_cluster_13: 11.644
- **Magnitude:** 81.2 | **LOC:** 171 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.2082%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_optional` (Impact: 11.2 | O(N^3))
  * `test_union_type_optional` (Impact: 11.2 | O(N^3))
  * `test_optional_tuple` (Impact: 11.2 | O(N^3))
  * `test_tuple_parameter_elements_are_conver` (Impact: 7.7 | O(N^3))
    * *Intent:* # Tuple elements that aren't converted by Click (i.e. Path or Enum) # should be recursively converte...
  * `test_list_parameters_convert_to_lists` (Impact: 7.6 | O(N^3))
    * *Intent:* # Lists containing objects that are converted by Click (i.e. not Path or Enum) # should not be inadv...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 55`, `args: 17`, `func_start: 17`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `orphaned_logic: 8`
* *Architecture:* `io: 1`, `api: 19`, `import: 7`
* *Defense:* `safety: 28`, `test: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` click, pathlib, typing, typer, typer.testing, enum, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_completion/test_completion_complete.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.762 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.686 IQR)
- **Top Global Matches:** file_cluster_8: 8.762, file_cluster_13: 9.165, file_cluster_7: 9.378
- **Magnitude:** 76.04 | **LOC:** 188 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (2.198%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_completion_complete_subcommand_fish` (Impact: 8.8 | O(N^3) | DB: 6)
  * `test_completion_complete_subcommand_powe` (Impact: 8.8 | O(N^3) | DB: 6)
  * `test_completion_complete_subcommand_pwsh` (Impact: 8.8 | O(N^3) | DB: 6)
  * `test_completion_complete_subcommand_zsh` (Impact: 4.9 | O(N^3) | DB: 6)
  * `test_completion_complete_subcommand_bash` (Impact: 4.8 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 39`, `args: 11`, `func_start: 11`
* *Risk/State:* `duplicate_logic: 5`, `orphaned_logic: 6`
* *Architecture:* `io: 21`, `api: 11`, `import: 8`
* *Defense:* `safety: 10`, `doc: 4`, `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` subprocess, pathlib, sys, importlib, os, types, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_tutorial/test_launch/test_tutorial002.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.403 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.764 IQR)
- **Top Global Matches:** file_cluster_13: 9.403, file_cluster_8: 9.861, file_cluster_0: 9.933
- **Magnitude:** 74.2 | **LOC:** 48 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (6.1118%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `app_dir` (Impact: 61.3 | O(2^N))
  * `test_cli` (Impact: 6.3 | O(N^2))
  * `test_script` (Impact: 2.9 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 20`, `args: 3`, `func_start: 3`
* *Risk/State:* `orphaned_logic: 2`
* *Architecture:* `io: 2`, `api: 3`, `import: 8`
* *Defense:* `safety: 3`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` docs_src.launch, subprocess, unittest.mock, pathlib, sys, typer, typer.testing, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_completion/test_completion_option_colon.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.075 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.631 IQR)
- **Top Global Matches:** file_cluster_8: 10.075, file_cluster_13: 10.774, file_cluster_7: 10.847
- **Magnitude:** 70.16 | **LOC:** 220 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_completion_colon_bash_all` (Impact: 4.2 | O(N^3) | DB: 6)
  * `test_completion_colon_bash_partial` (Impact: 4.2 | O(N^3) | DB: 6)
  * `test_completion_colon_bash_single` (Impact: 4.2 | O(N^3) | DB: 6)
  * `test_completion_colon_zsh_all` (Impact: 4.2 | O(N^3) | DB: 6)
  * `test_completion_colon_zsh_partial` (Impact: 4.2 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 57`, `args: 13`, `func_start: 13`
* *Risk/State:* `planned_debt: 1`, `orphaned_logic: 13`
* *Architecture:* `io: 25`, `api: 13`, `import: 4`
* *Defense:* `safety: 38`, `test: 51`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, , subprocess, os
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_tutorial/test_subcommands/test_tutorial003.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.456 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.78 IQR)
- **Top Global Matches:** file_cluster_8: 12.456, file_cluster_13: 12.591, file_cluster_0: 12.721
- **Magnitude:** 68.32 | **LOC:** 179 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (2.8032%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_scripts` (Impact: 7.9 | O(N^3) | DB: 6)
  * `mod` (Impact: 5.5 | O(N^2))
  * `app` (Impact: 3.6 | O(2^N))
  * `test_help` (Impact: 2.1 | O(N^1))
  * `test_help_items` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 97`, `args: 18`, `func_start: 18`
* *Risk/State:* `orphaned_logic: 16`
* *Architecture:* `io: 2`, `api: 18`, `import: 9`
* *Defense:* `safety: 62`, `test: 83`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` subprocess, docs_src.subcommands, sys, docs_src.subcommands.tutorial003_py310, typer.testing, os, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_ambiguous_params.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_0` (Drift: 9.954 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.238 IQR)
- **Top Global Matches:** file_cluster_0: 9.954, file_cluster_8: 10.049, file_cluster_13: 10.378
- **Magnitude:** 67.7 | **LOC:** 233 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.4569%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_forbid_default_factory_and_default_` (Impact: 6.1 | O(N^2))
  * `test_forbid_default_and_default_factory_` (Impact: 6.1 | O(N^2))
  * `test_forbid_default_value_in_annotated_a` (Impact: 5.9 | O(N^2))
  * `test_forbid_annotated_param_and_default_` (Impact: 5.9 | O(N^2))
  * `test_forbid_multiple_typer_params_in_ann` (Impact: 5.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 52`, `args: 21`, `func_start: 21`
* *Risk/State:* `dead_code: 1`, `orphaned_logic: 10`
* *Architecture:* `api: 21`, `import: 5`
* *Defense:* `safety: 14`, `test: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` typer.utils, typing, typer, typer.testing, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_completion/test_completion.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.149 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.82 IQR)
- **Top Global Matches:** file_cluster_8: 9.149, file_cluster_0: 9.454, file_cluster_13: 9.588
- **Magnitude:** 57.78 | **LOC:** 167 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (2.6597%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_install_completion` (Impact: 8.0 | O(N^3) | DB: 6)
  * `test_completion_source_bash` (Impact: 4.2 | O(N^3) | DB: 6)
  * `test_completion_source_powershell` (Impact: 4.2 | O(N^3) | DB: 6)
  * `test_completion_source_pwsh` (Impact: 4.2 | O(N^3) | DB: 6)
  * `test_show_completion` (Impact: 4.1 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 34`, `args: 10`, `func_start: 10`
* *Risk/State:* `fragile_debt: 1`, `orphaned_logic: 10`
* *Architecture:* `io: 21`, `api: 10`, `import: 6`
* *Defense:* `safety: 14`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` subprocess, pathlib, docs_src.typer_app, sys, os, ..utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/typer/_typing.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_16` (Drift: 8.071 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.795 IQR)
- **Top Global Matches:** file_cluster_16: 8.071, file_cluster_8: 8.488, file_cluster_13: 8.671
- **Magnitude:** 57.78 | **LOC:** 74 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.222%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `all_literal_values` (Impact: 24.4 | O(2^N))
    * *Intent:* """ This method is used to retrieve all Literal values as Literal can be used recursively (see https...
  * `is_none_type` (Impact: 12.2 | O(N^3))
  * `is_union` (Impact: 5.0 | O(N^1))
  * `is_callable_type` (Impact: 4.1 | O(N^1))
  * `is_literal_type` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 24`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 12`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.479
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.109874
  * `Imports (Out-Degree: 0):` collections.abc, types, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `typer-0.24.1/tests/test_completion/test_completion_install.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.424 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.049 IQR)
- **Top Global Matches:** file_cluster_8: 9.424, file_cluster_0: 9.715, file_cluster_13: 9.732
- **Magnitude:** 56.86 | **LOC:** 174 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (3.6405%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_completion_install_powershell` (Impact: 18.8 | O(N^4))
  * `test_completion_install_zsh` (Impact: 12.3 | O(N^3) | DB: 6)
  * `test_completion_install_bash` (Impact: 8.8 | O(N^3) | DB: 6)
  * `test_completion_install_fish` (Impact: 4.8 | O(N^3) | DB: 6)
  * `test_completion_install_no_shell` (Impact: 4.0 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 39`, `args: 5`, `func_start: 5`
* *Risk/State:* `high_risk_execution: 2`, `orphaned_logic: 5`
* *Architecture:* `io: 9`, `api: 5`, `import: 9`
* *Defense:* `safety: 19`, `test: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` shellingham, unittest, subprocess, pathlib, docs_src.typer_app, sys, typer.testing, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_tutorial/test_commands/test_help/test_tutorial001.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.697 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.763 IQR)
- **Top Global Matches:** file_cluster_8: 12.697, file_cluster_13: 12.772, file_cluster_0: 12.961
- **Magnitude:** 55.56 | **LOC:** 122 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (7.6923%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_help` (Impact: 6.6 | O(N^1))
  * `test_help_delete_all` (Impact: 4.5 | O(N^1))
  * `test_help_delete` (Impact: 4.4 | O(N^1))
  * `test_help_create` (Impact: 4.2 | O(N^1))
  * `test_script` (Impact: 3.4 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 69`, `args: 13`, `func_start: 13`
* *Risk/State:* `orphaned_logic: 13`
* *Architecture:* `io: 1`, `api: 13`, `import: 7`
* *Defense:* `safety: 47`, `test: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` subprocess, sys, importlib, typer.testing, types, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_cli/test_doc.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.249 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.331 IQR)
- **Top Global Matches:** file_cluster_8: 8.249, file_cluster_13: 9.118, file_cluster_7: 9.217
- **Magnitude:** 53.44 | **LOC:** 199 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (4.0408%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_doc_file_not_existing` (Impact: 7.8 | O(N^3) | DB: 3)
  * `test_doc_html_output` (Impact: 5.5 | O(N^3) | DB: 6)
  * `test_doc_title_output` (Impact: 5.4 | O(N^3) | DB: 3)
  * `test_doc_output` (Impact: 5.3 | O(N^3) | DB: 3)
  * `test_doc` (Impact: 4.6 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 28`, `args: 8`, `func_start: 8`
* *Risk/State:* `high_risk_execution: 3`, `orphaned_logic: 8`
* *Architecture:* `io: 10`, `api: 8`, `import: 5`
* *Defense:* `safety: 13`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` subprocess, pathlib, sys, os, as
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/docs_src/commands/callback/tutorial001_py310.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.746 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 6.602 IQR)
- **Top Global Matches:** file_cluster_8: 8.746, file_cluster_0: 9.102, file_cluster_7: 9.117
- **Magnitude:** 47.68 | **LOC:** 37 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.9435%), Tech Debt (97.7023%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 18.3 | O(2^N))
  * `delete` (Impact: 18.3 | O(2^N))
  * `main` (Impact: 7.6 | O(N^2))
    * *Intent:* """ Manage users in the awesome CLI app. """
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 4`, `args: 3`, `func_start: 3`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/typer/params.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.212 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.147 IQR)
- **Top Global Matches:** file_cluster_8: 8.212, file_cluster_16: 8.489, file_cluster_7: 8.659
- **Magnitude:** 46.66 | **LOC:** 1832 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.4113%), Tech Debt (86.9027%)
**Top Internal Functions/Classes:**
  * `Option` (Impact: 6.5 | O(N^3))
    * *Intent:* # Parameter default: Annotated[ Any | None, Doc( """
  * `Argument` (Impact: 6.5 | O(N^3))
    * *Intent:* """ For a CLI Option representing a [number](https://typer.tiangolo.com/tutorial/parameter-types/num...
  * `Option` (Impact: 3.5 | O(N^2))
    * *Intent:* # Overload for Option created with custom type 'parser' # Parameter default: Any | None = ..., *para...
  * `Option` (Impact: 3.5 | O(N^2))
    * *Intent:* # Overload for Option created with custom type 'click_type' # Parameter default: Any | None = ..., *...
  * `Argument` (Impact: 3.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 30`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 38`, `planned_debt: 9`, `duplicate_logic: 6`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `doc: 162`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.082675
  * `Imports (Out-Degree: 1):` click, collections.abc, pathlib, .models, typing, annotated_doc, enum, click.shell_completion...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `typer-0.24.1/tests/test_tutorial/test_subcommands/test_tutorial001.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.281 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.46 IQR)
- **Top Global Matches:** file_cluster_13: 12.281, file_cluster_8: 12.335, file_cluster_0: 12.428
- **Magnitude:** 44.92 | **LOC:** 100 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (3.2008%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_scripts` (Impact: 7.6 | O(N^3) | DB: 6)
  * `mod` (Impact: 5.5 | O(N^2))
  * `app` (Impact: 3.6 | O(2^N))
  * `test_help` (Impact: 2.1 | O(N^1))
  * `test_help_items` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 53`, `args: 11`, `func_start: 11`
* *Risk/State:* `orphaned_logic: 9`
* *Architecture:* `io: 2`, `api: 11`, `import: 8`
* *Defense:* `safety: 28`, `test: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` docs_src.subcommands.tutorial001_py310, subprocess, docs_src.subcommands, sys, typer.testing, os, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `typer-0.24.1/docs_src/subcommands/callback_override/tutorial004_py310.py` (PYTHON) | Magnitude: 11.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 5, args: 4, func_start: 4
- `typer-0.24.1/tests/test_rich_utils.py` (PYTHON) | Magnitude: 82.38 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 132, structural_boundaries: 71, test: 48, safety: 42
- `typer-0.24.1/docs_src/subcommands/callback_override/tutorial003_py310.py` (PYTHON) | Magnitude: 8.98 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, args: 3, func_start: 3
- `typer-0.24.1/tests/test_exit_errors.py` (PYTHON) | Magnitude: 21.22 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 18, test: 9, args: 8
- `typer-0.24.1/tests/test_others.py` (PYTHON) | Magnitude: 150.12 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 219, structural_boundaries: 136, test: 67, safety: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `typer-0.24.1/tests/test_completion/path_example.py` (PYTHON) | Magnitude: 2.26 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, import: 2, encapsulation: 2, indent_spaces: 2
- `typer-0.24.1/docs_src/subcommands/name_help/tutorial007_py310.py` (PYTHON) | Magnitude: 6.36 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, doc: 6, args: 4, func_start: 4
- `typer-0.24.1/tests/test_tutorial/test_printing/test_tutorial001.py` (PYTHON) | Magnitude: 11.74 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 17, test: 8, import: 7
- `typer-0.24.1/tests/test_tutorial/test_commands/test_one_or_multiple/test_tutorial002.py` (PYTHON) | Magnitude: 10.38 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 18, indent_spaces: 15, test: 11, safety: 8
- `typer-0.24.1/tests/test_tutorial/test_prompt/test_tutorial002.py` (PYTHON) | Magnitude: 10.38 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 18, indent_spaces: 15, test: 11, safety: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `typer-0.24.1/typer/utils.py` (PYTHON) | Magnitude: 179.2 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 125, structural_boundaries: 57, branch: 31, generics: 22
- `typer-0.24.1/typer/models.py` (PYTHON) | Magnitude: 145.14 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 383, state_mutation: 88, structural_boundaries: 59, generics: 49
- `typer-0.24.1/typer/_typing.py` (PYTHON) | Magnitude: 57.78 | Delta: **0.417 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 24, generics: 14, safety_bypasses: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `typer-0.24.1/tests/test_corner_cases.py` (PYTHON) | Magnitude: 10.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 24, test: 19, indent_spaces: 18, safety: 14
- `typer-0.24.1/docs_src/options_autocompletion/tutorial003_py310.py` (PYTHON) | Magnitude: 20.86 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, branch: 3, state_mutation: 3
- `typer-0.24.1/docs_src/parameter_types/custom_types/tutorial001_an_py310.py` (PYTHON) | Magnitude: 13.78 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 10, args: 4, func_start: 4
- `typer-0.24.1/tests/test_tutorial/test_first_steps/test_tutorial006.py` (PYTHON) | Magnitude: 20.92 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 26, indent_spaces: 22, test: 18, safety: 12
- `typer-0.24.1/docs_src/commands/one_or_multiple/tutorial001_py310.py` (PYTHON) | Magnitude: 5.8 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 3, args: 2, func_start: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `typer-0.24.1/typer/main.py` -> **Severity: 0.244** (Bridge: 0.0048 * Flux: 50.7988%)
- `typer-0.24.1/typer/core.py` -> **Severity: 0.031** (Bridge: 0.0005 * Flux: 68.725%)
- `typer-0.24.1/typer/models.py` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 99.8099%)
- `typer-0.24.1/typer/cli.py` -> **Severity: 0.002** (Bridge: 0.0001 * Flux: 20.2473%)
- `typer-0.24.1/typer/rich_utils.py` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 86.9201%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `typer-0.24.1/typer/testing.py` -> **Severity: 23.557** (Embedded: 0.2945 * Error Risk: 80.0%)
- `typer-0.24.1/typer/main.py` -> **Severity: 9.358** (Embedded: 0.1498 * Error Risk: 62.4624%)
- `typer-0.24.1/typer/_typing.py` -> **Severity: 8.79** (Embedded: 0.1099 * Error Risk: 80.0%)
- `typer-0.24.1/typer/completion.py` -> **Severity: 8.388** (Embedded: 0.1105 * Error Risk: 75.8716%)
- `typer-0.24.1/typer/core.py` -> **Severity: 7.962** (Embedded: 0.1152 * Error Risk: 69.1236%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `typer-0.24.1/typer/testing.py` -> **Severity: 11424.08** (Blast Radius: 124.154 * Doc Risk: 92.0154%)
- `typer-0.24.1/typer/main.py` -> **Severity: 3672.85** (Blast Radius: 106.494 * Doc Risk: 34.4888%)
- `typer-0.24.1/typer/completion.py` -> **Severity: 3479.478** (Blast Radius: 35.44 * Doc Risk: 98.1794%)
- `typer-0.24.1/typer/_typing.py` -> **Severity: 3447.079** (Blast Radius: 34.479 * Doc Risk: 99.9762%)
- `typer-0.24.1/typer/core.py` -> **Severity: 1985.241** (Blast Radius: 47.136 * Doc Risk: 42.1173%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
