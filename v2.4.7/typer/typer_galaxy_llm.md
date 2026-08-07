# ARCHITECTURAL_BRIEF: typer
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/typer` |
| **Timestamp** | `2026-08-07T05:27:08.368097+00:00` |
| **Scan Duration** | `0.87s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 574 malicious artifacts.

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
| Error & Exception Exposure | 0.0 | 94.2 | 2.9 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 36.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 1.5 | 0.2 | 0.0 |
| API Exposure | 0.0 | 12.0 | 3.5 | 3.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 99.9 | 1.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 32.1 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 69.3 | 86.7 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 22.4 | 3.2 | 0.0 |
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

- `get_help_record` (@ `typer-0.24.1/typer/core.py`) -> Impact: **166.9** | LOC: 462
  * *Intent:* # Modified version of click.core.Option.get_help_record() # to support Arguments if self.hidden: return None name = self.make_metavar(ctx=ctx) help = ...
- `escape` (@ `typer-0.24.1/typer/_completion_classes.py`) -> Impact: **47.0** | LOC: 101
- `solve_typer_info_help` (@ `typer-0.24.1/typer/main.py`) -> Impact: **45.8** | LOC: 35
- `format_completion` (@ `typer-0.24.1/typer/_completion_classes.py`) -> Impact: **41.5** | LOC: 102
- `get_typer_from_module` (@ `typer-0.24.1/typer/cli.py`) -> Impact: **30.3** | LOC: 46
  * *Intent:* # Try to get defined app if state.app: obj = getattr(module, state.app, None) if not isinstance(obj, typer.Typer): typer.echo(f"Not a Typer object: --...
- `get_command` (@ `typer-0.24.1/typer/main.py`) -> Impact: **25.8** | LOC: 36
- `get_params_from_function` (@ `typer-0.24.1/typer/utils.py`) -> Impact: **25.2** | LOC: 80
- `maybe_update_state` (@ `typer-0.24.1/typer/cli.py`) -> Impact: **18.9** | LOC: 19
- `internal_convertor` (@ `typer-0.24.1/typer/main.py`) -> Impact: **17.3** | LOC: 4
- `test_help_table_alignment_with_styled_te` (@ `typer-0.24.1/tests/test_rich_utils.py`) -> Impact: **16.1** | LOC: 45

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `typer-0.24.1/typer` | 16 | 1470.88 | 12.74% | 31.29% |
| `typer-0.24.1/tests` | 20 | 779.44 | 4.04% | 0.0% |
| `typer-0.24.1/tests/test_completion` | 13 | 285.92 | 3.43% | 0.0% |
| `typer-0.24.1/tests/test_cli` | 18 | 225.64 | 2.37% | 0.0% |
| `typer-0.24.1/tests/test_tutorial/test_commands/test_help` | 9 | 209.28 | 7.57% | 0.0% |
| `typer-0.24.1/docs_src/options_autocompletion` | 19 | 181.8 | 13.84% | 93.5% |
| `typer-0.24.1/tests/test_tutorial/test_subcommands` | 4 | 137.98 | 2.75% | 0.0% |
| `typer-0.24.1/tests/test_tutorial/test_arguments/test_help` | 9 | 128.76 | 6.88% | 0.0% |
| `typer-0.24.1/tests/test_tutorial/test_options_autocompletion` | 9 | 125.96 | 2.77% | 0.0% |
| `typer-0.24.1/docs_src/commands/help` | 13 | 113.7 | 5.68% | 91.43% |

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
- `typer-0.24.1/tests/test_others.py` -> **18** Orphaned Functions | **17** Duplicates
- `typer-0.24.1/tests/test_ambiguous_params.py` -> **10** Orphaned Functions | **9** Duplicates
- `typer-0.24.1/tests/test_type_conversion.py` -> **14** Orphaned Functions | **3** Duplicates
- `typer-0.24.1/tests/test_rich_markup_mode.py` -> **9** Orphaned Functions | **7** Duplicates
- `typer-0.24.1/tests/test_tutorial/test_subcommands/test_tutorial003.py` -> **16** Orphaned Functions | **0** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1533` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `typer-0.24.1/docs_src/options_autocompletion/tutorial003_py310.py` (PYTHON) -> Cumulative Risk: **543.31**
- **Archetype:** `file_cluster_8` (Distance: 9.639 IQR)
- **Magnitude:** 13.26 | **LOC:** 28 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.708%), State Flux (98.7711%), Safety Score (76.5704%)
- **Heaviest Functions:** `complete_name` (Impact: 6.3), `main` (Impact: 1.6)

### 2. `typer-0.24.1/docs_src/options_autocompletion/tutorial003_an_py310.py` (PYTHON) -> Cumulative Risk: **537.59**
- **Archetype:** `file_cluster_13` (Distance: 9.422 IQR)
- **Magnitude:** 13.28 | **LOC:** 30 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.548%), State Flux (98.2635%), Safety Score (76.0213%)
- **Heaviest Functions:** `complete_name` (Impact: 6.3), `main` (Impact: 1.6)

### 3. `typer-0.24.1/typer/_completion_classes.py` (PYTHON) -> Cumulative Risk: **535.04**
- **Archetype:** `file_cluster_13` (Distance: 12.48 IQR)
- **Magnitude:** 141.12 | **LOC:** 200 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9999%), Documentation (95.4828%), Verification (80.0%)
- **Heaviest Functions:** `escape` (Impact: 47.0), `format_completion` (Impact: 41.5), `get_completion_args` (Impact: 7.4)

### 4. `typer-0.24.1/docs_src/options_autocompletion/tutorial004_py310.py` (PYTHON) -> Cumulative Risk: **516.76**
- **Archetype:** `file_cluster_8` (Distance: 9.024 IQR)
- **Magnitude:** 13.36 | **LOC:** 33 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (98.2394%), State Flux (94.9664%), Safety Score (74.0104%)
- **Heaviest Functions:** `complete_name` (Impact: 6.3), `main` (Impact: 1.6)

### 5. `typer-0.24.1/typer/utils.py` (PYTHON) -> Cumulative Risk: **513.65**
- **Archetype:** `file_cluster_16` (Distance: 9.541 IQR)
- **Magnitude:** 90.1 | **LOC:** 198 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9995%), Verification (80.0%), Safety Score (66.2203%)
- **Heaviest Functions:** `get_params_from_function` (Impact: 25.2), `__str__` (Impact: 9.2), `parse_boolean_env_var` (Impact: 7.4)

### 6. `typer-0.24.1/docs_src/options_autocompletion/tutorial004_an_py310.py` (PYTHON) -> Cumulative Risk: **511.71**
- **Archetype:** `file_cluster_13` (Distance: 9.003 IQR)
- **Magnitude:** 13.38 | **LOC:** 35 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (97.7023%), State Flux (93.8197%), Safety Score (73.5503%)
- **Heaviest Functions:** `complete_name` (Impact: 6.3), `main` (Impact: 1.6)

### 7. `typer-0.24.1/typer/core.py` (PYTHON) -> Cumulative Risk: **488.62**
- **Archetype:** `file_cluster_13` (Distance: 10.872 IQR)
- **Magnitude:** 277.88 | **LOC:** 822 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Safety Score (71.3208%), State Flux (68.725%)
- **Heaviest Functions:** `get_help_record` (Impact: 166.9), `format_help` (Impact: 6.5), `_split_opt` (Impact: 6.3)

### 8. `typer-0.24.1/typer/models.py` (PYTHON) -> Cumulative Risk: **478.16**
- **Archetype:** `file_cluster_16` (Distance: 10.425 IQR)
- **Magnitude:** 137.54 | **LOC:** 652 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8099%), Tech Debt (99.6638%), Safety Score (88.18%)
- **Heaviest Functions:** `__init__` (Impact: 3.0), `__init__` (Impact: 3.0), `__init__` (Impact: 3.0)

### 9. `typer-0.24.1/docs_src/parameter_types/custom_types/tutorial001_py310.py` (PYTHON) -> Cumulative Risk: **472.11**
- **Archetype:** `file_cluster_8` (Distance: 9.299 IQR)
- **Magnitude:** 12.86 | **LOC:** 30 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (90.1191%), Safety Score (64.3848%)
- **Heaviest Functions:** `main` (Impact: 2.8), `parse_custom_class` (Impact: 2.1), `__init__` (Impact: 1.8)

### 10. `typer-0.24.1/docs_src/parameter_types/custom_types/tutorial001_an_py310.py` (PYTHON) -> Cumulative Risk: **467.1**
- **Archetype:** `file_cluster_8` (Distance: 9.31 IQR)
- **Magnitude:** 11.68 | **LOC:** 32 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (89.1152%), Safety Score (64.0359%)
- **Heaviest Functions:** `parse_custom_class` (Impact: 2.1), `__init__` (Impact: 1.8), `__str__` (Impact: 1.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `typer-0.24.1/typer/main.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.175 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.128 IQR)
- **Top Global Matches:** file_cluster_8: 11.175, file_cluster_16: 11.241, file_cluster_13: 11.339
- **Magnitude:** 381.66 | **LOC:** 2014 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.1524%), Tech Debt (25.4487%)
**Top Internal Functions/Classes:**
  * `solve_typer_info_help` (Impact: 45.8)
  * `get_command` (Impact: 25.8)
  * `internal_convertor` (Impact: 17.3)
  * `solve_typer_info_defaults` (Impact: 15.7)
  * `wrapper` (Impact: 12.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 180`, `args: 39`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 80`, `high_risk_execution: 2`, `state_mutation: 73`, `duplicate_logic: 7`
* *Architecture:* `io: 13`, `api: 38`, `import: 27`
* *Defense:* `safety: 35`, `doc: 154`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 106.494
  * `Choke Point (Betweenness):` 0.004805 | `Ripple Effect (Closeness):` 0.149826
  * `Imports (Out-Degree: 7):` subprocess, , shutil, sys, uuid, datetime, os, .completion...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `typer-0.24.1/typer/core.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.872 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.061 IQR)
- **Top Global Matches:** file_cluster_13: 10.872, file_cluster_16: 10.961, file_cluster_8: 10.989
- **Magnitude:** 277.88 | **LOC:** 822 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.219%), Tech Debt (54.9718%)
**Top Internal Functions/Classes:**
  * `get_help_record` (Impact: 166.9)
    * *Intent:* # Modified version of click.core.Option.get_help_record() # to support Arguments if self.hidden: ret...
  * `format_help` (Impact: 6.5)
  * `_split_opt` (Impact: 6.3)
    * *Intent:* # Copy from click.parser._split_opt
  * `list_commands` (Impact: 3.7)
    * *Intent:* """Returns a list of subcommand names. Note that in Click's Group class, these are sorted. In Typer,...
  * `__init__` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 134`, `args: 34`, `func_start: 34`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 49`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 15`, `api: 20`, `import: 26`
* *Defense:* `safety: 30`, `doc: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 47.136
  * `Choke Point (Betweenness):` 0.000452 | `Ripple Effect (Closeness):` 0.115184
  * `Imports (Out-Degree: 2):` , sys, os, .completion, ._typing, click, warnings, difflib...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `typer-0.24.1/tests/test_others.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.27 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.9 IQR)
- **Top Global Matches:** file_cluster_0: 11.27, file_cluster_13: 11.343, file_cluster_8: 11.385
- **Magnitude:** 156.02 | **LOC:** 340 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.246%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_callback_4_list_none` (Impact: 9.8)
  * `test_too_many_parsers` (Impact: 8.0)
  * `names_callback` (Impact: 6.2)
  * `test_forward_references` (Impact: 4.4)
  * `test_completion_argument` (Impact: 4.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 136`, `args: 39`, `func_start: 39`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `duplicate_logic: 17`, `orphaned_logic: 18`
* *Architecture:* `io: 9`, `api: 41`, `import: 17`
* *Defense:* `safety: 43`, `test: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` typer.completion, subprocess, typer._completion_shared, typer.core, .utils, sys, os, typer.testing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/typer/_completion_classes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.48 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.823 IQR)
- **Top Global Matches:** file_cluster_13: 12.48, file_cluster_6: 12.67, file_cluster_16: 12.702
- **Magnitude:** 141.12 | **LOC:** 200 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.7115%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `escape` (Impact: 47.0)
  * `format_completion` (Impact: 41.5)
  * `get_completion_args` (Impact: 7.4)
  * `_sanitize_help_text` (Impact: 4.4)
    * *Intent:* """Sanitizes the help text by removing rich tags"""
  * `get_completion_args` (Impact: 4.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 60`, `args: 18`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `dead_code: 5`, `planned_debt: 3`, `duplicate_logic: 6`
* *Architecture:* `io: 9`, `api: 22`, `import: 11`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.264
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.083545
  * `Imports (Out-Degree: 1):` importlib.util, , re, sys, click.parser, os, click.shell_completion, ._completion_shared...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `typer-0.24.1/typer/models.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.425 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.549 IQR)
- **Top Global Matches:** file_cluster_16: 10.425, file_cluster_8: 10.47, file_cluster_13: 10.717
- **Magnitude:** 137.54 | **LOC:** 652 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.3135%), Tech Debt (99.6638%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 3.0)
  * `__init__` (Impact: 3.0)
    * *Intent:* *,
  * `__init__` (Impact: 3.0)
  * `__init__` (Impact: 2.9)
  * `Default` (Impact: 2.2)
    * *Intent:* """ pass class FileBinaryRead(io.BufferedReader): """
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 59`, `args: 11`, `func_start: 11`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 88`, `planned_debt: 4`, `duplicate_logic: 8`
* *Architecture:* `api: 18`, `import: 9`
* *Defense:* `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.951
  * `Choke Point (Betweenness):` 8.7e-05 | `Ripple Effect (Closeness):` 0.10971
  * `Imports (Out-Degree: 1):` .main, collections.abc, click.shell_completion, typing, .core, inspect, warnings, click...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `typer-0.24.1/typer/rich_utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.867 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.42 IQR)
- **Top Global Matches:** file_cluster_13: 10.867, file_cluster_8: 10.961, file_cluster_16: 11.13
- **Magnitude:** 126.1 | **LOC:** 754 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.2965%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `rich_format_error` (Impact: 11.4)
  * `rich_render_text` (Impact: 4.2)
  * `_get_rich_console` (Impact: 3.4)
  * `rich_to_html` (Impact: 2.4)
  * `escape_before_html_export` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 87`, `args: 15`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 60`, `dead_code: 1`
* *Architecture:* `api: 17`, `import: 24`
* *Defense:* `safety: 22`, `doc: 22`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.139
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.001742
  * `Imports (Out-Degree: 2):` rich.align, rich.emoji, rich.padding, os, .core, rich, click, io...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `typer-0.24.1/typer/cli.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.939 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.283 IQR)
- **Top Global Matches:** file_cluster_8: 9.939, file_cluster_13: 9.958, file_cluster_16: 10.195
- **Magnitude:** 124.08 | **LOC:** 318 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.5894%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_typer_from_module` (Impact: 30.3)
    * *Intent:* # Try to get defined app if state.app: obj = getattr(module, state.app, None) if not isinstance(obj,...
  * `maybe_update_state` (Impact: 18.9)
  * `maybe_add_run_to_cli` (Impact: 12.6)
  * `get_typer_from_state` (Impact: 11.2)
  * `print_version` (Impact: 6.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 57`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 6`
* *Architecture:* `io: 4`, `api: 16`, `import: 14`
* *Defense:* `safety: 17`, `doc: 4`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.738
  * `Choke Point (Betweenness):` 0.000123 | `Ripple Effect (Closeness):` 0.001742
  * `Imports (Out-Degree: 1):` importlib.util, , as, re, sys, typing, .core, click...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `typer-0.24.1/tests/test_rich_markup_mode.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.161 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.853 IQR)
- **Top Global Matches:** file_cluster_8: 11.161, file_cluster_0: 11.218, file_cluster_17: 11.338
- **Magnitude:** 112.26 | **LOC:** 333 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (1.9839%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_markup_mode_newline_mixed` (Impact: 15.0)
  * `test_markup_mode_newline_pr815` (Impact: 11.5)
  * `test_markup_mode_newline_issue447` (Impact: 11.5)
  * `test_markup_mode_bullets_single_newline` (Impact: 11.5)
  * `test_markup_mode_bullets_double_newline` (Impact: 11.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 58`, `args: 16`, `func_start: 16`
* *Risk/State:* `duplicate_logic: 7`, `orphaned_logic: 9`
* *Architecture:* `io: 2`, `api: 16`, `import: 7`
* *Defense:* `safety: 34`, `doc: 14`, `test: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` typer.completion, subprocess, sys, os, typer.testing, pytest, typer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_type_conversion.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.509 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.541 IQR)
- **Top Global Matches:** file_cluster_0: 11.509, file_cluster_8: 11.714, file_cluster_13: 11.729
- **Magnitude:** 91.7 | **LOC:** 171 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.2082%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `opt` (Impact: 8.7)
  * `opt` (Impact: 8.7)
  * `test_optional` (Impact: 6.0)
  * `test_union_type_optional` (Impact: 6.0)
  * `test_optional_tuple` (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 55`, `args: 17`, `func_start: 17`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `duplicate_logic: 3`, `orphaned_logic: 14`
* *Architecture:* `io: 1`, `api: 19`, `import: 7`
* *Defense:* `safety: 28`, `test: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` typer.testing, typing, enum, pytest, click, pathlib, typer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/typer/utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.541 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.314 IQR)
- **Top Global Matches:** file_cluster_16: 9.541, file_cluster_8: 9.56, file_cluster_13: 9.651
- **Magnitude:** 90.1 | **LOC:** 198 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.8905%), Tech Debt (99.9995%)
**Top Internal Functions/Classes:**
  * `get_params_from_function` (Impact: 25.2)
  * `__str__` (Impact: 9.2)
  * `parse_boolean_env_var` (Impact: 7.4)
  * `_param_type_to_user_string` (Impact: 6.5)
    * *Intent:* # Render a `ParameterInfo` subclass for use in error messages. # User code doesn't call `*Info` dire...
  * `__str__` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 57`, `args: 12`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 8`, `duplicate_logic: 8`
* *Architecture:* `api: 8`, `import: 6`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.339
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001742
  * `Imports (Out-Degree: 2):` collections.abc, typing, ._typing, inspect, copy, .models
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `typer-0.24.1/tests/test_rich_utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.901 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.242 IQR)
- **Top Global Matches:** file_cluster_0: 11.901, file_cluster_13: 11.947, file_cluster_8: 11.966
- **Magnitude:** 75.98 | **LOC:** 225 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (1.7767%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_help_table_alignment_with_styled_te` (Impact: 16.1)
  * `test_rich_markup_import_regression` (Impact: 6.0)
  * `test_metavar_highlighter` (Impact: 3.2)
  * `example` (Impact: 3.2)
  * `test_rich_doesnt_print_None_default` (Impact: 3.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 71`, `args: 16`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 3`, `duplicate_logic: 6`, `orphaned_logic: 8`
* *Architecture:* `io: 2`, `api: 16`, `import: 8`
* *Defense:* `safety: 42`, `doc: 12`, `test: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` typer.completion, tests.utils, typer, sys, typer.rich_utils, pytest, typer.testing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_ambiguous_params.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_0` (Drift: 9.918 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.217 IQR)
- **Top Global Matches:** file_cluster_0: 9.918, file_cluster_8: 10.044, file_cluster_13: 10.348
- **Magnitude:** 72.1 | **LOC:** 233 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.9623%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_forbid_default_factory_and_default_` (Impact: 4.4)
  * `test_forbid_default_and_default_factory_` (Impact: 4.4)
  * `test_forbid_default_value_in_annotated_a` (Impact: 4.2)
  * `test_forbid_annotated_param_and_default_` (Impact: 4.2)
  * `test_forbid_multiple_typer_params_in_ann` (Impact: 4.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 52`, `args: 21`, `func_start: 21`
* *Risk/State:* `dead_code: 1`, `duplicate_logic: 9`, `orphaned_logic: 10`
* *Architecture:* `api: 21`, `import: 5`
* *Defense:* `safety: 14`, `test: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` typer, typing, typer.utils, pytest, typer.testing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_tutorial/test_subcommands/test_tutorial003.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.456 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.78 IQR)
- **Top Global Matches:** file_cluster_8: 12.456, file_cluster_13: 12.591, file_cluster_0: 12.721
- **Magnitude:** 61.42 | **LOC:** 179 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.8032%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_scripts` (Impact: 4.5)
  * `mod` (Impact: 3.8)
  * `test_help` (Impact: 2.1)
  * `test_help_items` (Impact: 2.1)
  * `test_items_create` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 97`, `args: 18`, `func_start: 18`
* *Risk/State:* `orphaned_logic: 16`
* *Architecture:* `io: 2`, `api: 18`, `import: 9`
* *Defense:* `safety: 62`, `test: 83`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` subprocess, docs_src.subcommands.tutorial003_py310, sys, os, docs_src.subcommands, pytest, typer.testing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_tutorial/test_commands/test_help/test_tutorial001.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.697 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.763 IQR)
- **Top Global Matches:** file_cluster_8: 12.697, file_cluster_13: 12.772, file_cluster_0: 12.961
- **Magnitude:** 54.56 | **LOC:** 122 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.6923%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_help` (Impact: 6.6)
  * `test_help_delete_all` (Impact: 4.5)
  * `test_help_delete` (Impact: 4.4)
  * `test_help_create` (Impact: 4.2)
  * `test_script` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 69`, `args: 13`, `func_start: 13`
* *Risk/State:* `orphaned_logic: 13`
* *Architecture:* `io: 1`, `api: 13`, `import: 7`
* *Defense:* `safety: 47`, `test: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` subprocess, sys, types, importlib, pytest, typer.testing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/typer/completion.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.181 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.498 IQR)
- **Top Global Matches:** file_cluster_8: 8.181, file_cluster_13: 8.259, file_cluster_16: 8.671
- **Magnitude:** 52.28 | **LOC:** 147 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.3775%), Tech Debt (17.0432%)
**Top Internal Functions/Classes:**
  * `show_callback` (Impact: 12.9)
  * `install_callback` (Impact: 10.5)
  * `_install_completion_placeholder_function` (Impact: 6.4)
    * *Intent:* # Create a fake command function to extract the completion parameters
  * `_install_completion_no_auto_placeholder_` (Impact: 6.3)
  * `get_completion_inspect_parameters` (Impact: 5.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 36`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 10`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 7`, `import: 12`
* *Defense:* `safety: 3`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 35.44
  * `Choke Point (Betweenness):` 0.00178 | `Ripple Effect (Closeness):` 0.11055
  * `Imports (Out-Degree: 4):` .utils, sys, collections.abc, .params, os, ._completion_classes, click.shell_completion, ._completion_shared...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `typer-0.24.1/tests/test_completion/test_completion_complete.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.762 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.686 IQR)
- **Top Global Matches:** file_cluster_8: 8.762, file_cluster_13: 9.165, file_cluster_7: 9.378
- **Magnitude:** 49.84 | **LOC:** 188 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.198%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_completion_complete_subcommand_fish` (Impact: 4.8)
  * `test_completion_complete_subcommand_powe` (Impact: 4.8)
  * `test_completion_complete_subcommand_pwsh` (Impact: 4.8)
  * `test_completion_complete_subcommand_zsh` (Impact: 2.9)
  * `test_completion_complete_subcommand_bash` (Impact: 2.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 39`, `args: 11`, `func_start: 11`
* *Risk/State:* `duplicate_logic: 5`, `orphaned_logic: 6`
* *Architecture:* `io: 21`, `api: 11`, `import: 8`
* *Defense:* `safety: 10`, `doc: 4`, `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` subprocess, sys, os, types, importlib, pytest, pathlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_suggest_commands.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.069 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.755 IQR)
- **Top Global Matches:** file_cluster_0: 12.069, file_cluster_8: 12.342, file_cluster_13: 12.442
- **Magnitude:** 49.22 | **LOC:** 99 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (1.5259%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_typo_suggestion_multiple_matches` (Impact: 4.4)
  * `test_typo_suggestion_exact_match_works` (Impact: 2.7)
  * `test_typo_suggestion_enabled` (Impact: 2.6)
    * *Intent:* """Test that typo suggestions work when enabled"""
  * `test_typo_suggestion_no_matches` (Impact: 2.6)
  * `test_typo_suggestion_disabled` (Impact: 2.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 35`, `args: 15`, `func_start: 15`
* *Risk/State:* `duplicate_logic: 9`, `orphaned_logic: 5`
* *Architecture:* `api: 15`, `import: 2`
* *Defense:* `safety: 17`, `doc: 10`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` typer.testing, typer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_completion/test_completion_option_colon.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.075 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.631 IQR)
- **Top Global Matches:** file_cluster_8: 10.075, file_cluster_13: 10.774, file_cluster_7: 10.847
- **Magnitude:** 48.56 | **LOC:** 220 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_completion_colon_bash_all` (Impact: 2.5)
  * `test_completion_colon_bash_partial` (Impact: 2.5)
  * `test_completion_colon_bash_single` (Impact: 2.5)
  * `test_completion_colon_powershell_all` (Impact: 2.5)
  * `test_completion_colon_powershell_partial` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 57`, `args: 13`, `func_start: 13`
* *Risk/State:* `planned_debt: 1`, `orphaned_logic: 13`
* *Architecture:* `io: 25`, `api: 13`, `import: 4`
* *Defense:* `safety: 38`, `test: 51`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` subprocess, os, , sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_annotated.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.629 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.599 IQR)
- **Top Global Matches:** file_cluster_0: 11.629, file_cluster_8: 11.747, file_cluster_13: 11.764
- **Magnitude:** 43.34 | **LOC:** 98 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.4973%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_annotated_option_with_argname_doesn` (Impact: 6.0)
  * `cmd` (Impact: 4.5)
  * `test_annotated_custom_path` (Impact: 4.3)
  * `test_annotated_argument_with_default_fac` (Impact: 2.6)
  * `test_annotated_argument_with_default` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 40`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `duplicate_logic: 4`, `orphaned_logic: 6`
* *Architecture:* `io: 2`, `api: 12`, `import: 5`
* *Defense:* `safety: 19`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` typer, sys, typing, pathlib, typer.testing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/typer/params.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.202 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.147 IQR)
- **Top Global Matches:** file_cluster_8: 8.202, file_cluster_16: 8.48, file_cluster_7: 8.65
- **Magnitude:** 39.46 | **LOC:** 1832 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.4113%), Tech Debt (86.9027%)
**Top Internal Functions/Classes:**
  * `Option` (Impact: 3.9)
    * *Intent:* # Parameter default: Annotated[ Any | None, Doc( """
  * `Argument` (Impact: 3.9)
    * *Intent:* """ For a CLI Option representing a [number](https://typer.tiangolo.com/tutorial/parameter-types/num...
  * `Option` (Impact: 3.0)
    * *Intent:* # Overload for Option created with custom type 'parser' # Parameter default: Any | None = ..., *para...
  * `Option` (Impact: 3.0)
    * *Intent:* # Overload for Option created with custom type 'click_type' # Parameter default: Any | None = ..., *...
  * `Argument` (Impact: 3.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 30`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 38`, `planned_debt: 9`, `duplicate_logic: 6`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `doc: 162`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.865
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.082675
  * `Imports (Out-Degree: 1):` collections.abc, datetime, click.shell_completion, typing, enum, click, pathlib, .models...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `typer-0.24.1/tests/test_completion/test_completion.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.149 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.82 IQR)
- **Top Global Matches:** file_cluster_8: 9.149, file_cluster_0: 9.454, file_cluster_13: 9.588
- **Magnitude:** 38.48 | **LOC:** 167 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.6597%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_install_completion` (Impact: 4.5)
  * `test_completion_source_bash` (Impact: 2.4)
  * `test_completion_source_zsh` (Impact: 2.4)
  * `test_completion_source_powershell` (Impact: 2.4)
  * `test_completion_source_pwsh` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 34`, `args: 10`, `func_start: 10`
* *Risk/State:* `fragile_debt: 1`, `orphaned_logic: 10`
* *Architecture:* `io: 21`, `api: 10`, `import: 6`
* *Defense:* `safety: 14`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` subprocess, sys, os, ..utils, pathlib, docs_src.typer_app
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_tutorial/test_subcommands/test_tutorial001.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.281 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.46 IQR)
- **Top Global Matches:** file_cluster_13: 12.281, file_cluster_8: 12.335, file_cluster_0: 12.428
- **Magnitude:** 38.02 | **LOC:** 100 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.2008%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_scripts` (Impact: 4.2)
  * `mod` (Impact: 3.8)
  * `test_help` (Impact: 2.1)
  * `test_help_items` (Impact: 2.1)
  * `test_help_users` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 53`, `args: 11`, `func_start: 11`
* *Risk/State:* `orphaned_logic: 9`
* *Architecture:* `io: 2`, `api: 11`, `import: 8`
* *Defense:* `safety: 28`, `test: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` subprocess, sys, os, docs_src.subcommands, docs_src.subcommands.tutorial001_py310, pytest, typer.testing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_cli/test_doc.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.249 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.331 IQR)
- **Top Global Matches:** file_cluster_8: 8.249, file_cluster_13: 9.118, file_cluster_7: 9.217
- **Magnitude:** 36.94 | **LOC:** 199 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.5948%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_doc_file_not_existing` (Impact: 4.3)
  * `test_doc_html_output` (Impact: 3.5)
  * `test_doc_title_output` (Impact: 3.4)
  * `test_doc_output` (Impact: 3.3)
  * `test_doc` (Impact: 2.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 28`, `args: 8`, `func_start: 8`
* *Risk/State:* `high_risk_execution: 3`, `orphaned_logic: 8`
* *Architecture:* `io: 10`, `api: 8`, `import: 5`
* *Defense:* `safety: 13`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` subprocess, as, sys, os, pathlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/tests/test_tutorial/test_parameter_types/test_number/test_tutorial001.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.207 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.921 IQR)
- **Top Global Matches:** file_cluster_13: 12.207, file_cluster_8: 12.296, file_cluster_0: 12.528
- **Magnitude:** 36.42 | **LOC:** 92 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.4259%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_invalid_id` (Impact: 4.3)
  * `test_invalid_age` (Impact: 4.2)
  * `test_invalid_score` (Impact: 3.8)
  * `test_help` (Impact: 2.4)
  * `test_script` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 47`, `args: 9`, `func_start: 9`
* *Risk/State:* `orphaned_logic: 9`
* *Architecture:* `io: 1`, `api: 9`, `import: 9`
* *Defense:* `safety: 27`, `test: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.939
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` subprocess, sys, typer.testing, types, importlib, pytest, typer, typer.core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typer-0.24.1/typer/_typing.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_16` (Drift: 8.071 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.795 IQR)
- **Top Global Matches:** file_cluster_16: 8.071, file_cluster_8: 8.488, file_cluster_13: 8.671
- **Magnitude:** 35.78 | **LOC:** 74 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.222%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `all_literal_values` (Impact: 8.4)
    * *Intent:* """ This method is used to retrieve all Literal values as Literal can be used recursively (see https...
  * `is_none_type` (Impact: 6.2)
  * `is_union` (Impact: 5.0)
  * `is_callable_type` (Impact: 4.1)
  * `is_literal_type` (Impact: 2.1)
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

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `typer-0.24.1/docs_src/subcommands/callback_override/tutorial004_py310.py` (PYTHON) | Magnitude: 11.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 5, args: 4, func_start: 4
- `typer-0.24.1/tests/test_rich_utils.py` (PYTHON) | Magnitude: 75.98 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 132, structural_boundaries: 71, test: 48, safety: 42
- `typer-0.24.1/docs_src/subcommands/callback_override/tutorial003_py310.py` (PYTHON) | Magnitude: 8.98 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, args: 3, func_start: 3
- `typer-0.24.1/tests/test_exit_errors.py` (PYTHON) | Magnitude: 25.02 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 18, test: 9, args: 8
- `typer-0.24.1/tests/test_others.py` (PYTHON) | Magnitude: 156.02 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 219, structural_boundaries: 136, test: 67, safety: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `typer-0.24.1/tests/test_completion/path_example.py` (PYTHON) | Magnitude: 2.26 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, import: 2, encapsulation: 2, indent_spaces: 2
- `typer-0.24.1/docs_src/subcommands/name_help/tutorial007_py310.py` (PYTHON) | Magnitude: 6.36 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, doc: 6, args: 4, func_start: 4
- `typer-0.24.1/tests/test_tutorial/test_printing/test_tutorial001.py` (PYTHON) | Magnitude: 9.24 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 17, test: 8, import: 7
- `typer-0.24.1/tests/test_tutorial/test_commands/test_one_or_multiple/test_tutorial002.py` (PYTHON) | Magnitude: 9.58 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 18, indent_spaces: 15, test: 11, safety: 8
- `typer-0.24.1/tests/test_tutorial/test_prompt/test_tutorial002.py` (PYTHON) | Magnitude: 9.58 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 18, indent_spaces: 15, test: 11, safety: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `typer-0.24.1/typer/utils.py` (PYTHON) | Magnitude: 90.1 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 125, structural_boundaries: 57, branch: 31, generics: 22
- `typer-0.24.1/typer/models.py` (PYTHON) | Magnitude: 137.54 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 383, state_mutation: 88, structural_boundaries: 59, generics: 49
- `typer-0.24.1/typer/_typing.py` (PYTHON) | Magnitude: 35.78 | Delta: **0.417 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 24, generics: 14, safety_bypasses: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `typer-0.24.1/tests/test_corner_cases.py` (PYTHON) | Magnitude: 10.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 24, test: 19, indent_spaces: 18, safety: 14
- `typer-0.24.1/docs_src/parameter_types/custom_types/tutorial001_an_py310.py` (PYTHON) | Magnitude: 11.68 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 10, args: 4, func_start: 4
- `typer-0.24.1/docs_src/options_autocompletion/tutorial003_py310.py` (PYTHON) | Magnitude: 13.26 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 4, branch: 3, state_mutation: 3
- `typer-0.24.1/tests/test_tutorial/test_first_steps/test_tutorial006.py` (PYTHON) | Magnitude: 20.12 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
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
- `typer-0.24.1/typer/_typing.py` -> **Severity: 10.346** (Embedded: 0.1099 * Error Risk: 94.162%)
- `typer-0.24.1/typer/main.py` -> **Severity: 10.141** (Embedded: 0.1498 * Error Risk: 67.6877%)
- `typer-0.24.1/typer/models.py` -> **Severity: 9.674** (Embedded: 0.1097 * Error Risk: 88.18%)
- `typer-0.24.1/typer/completion.py` -> **Severity: 8.388** (Embedded: 0.1105 * Error Risk: 75.8716%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `typer-0.24.1/typer/testing.py` -> **Severity: 7882.239** (Blast Radius: 124.154 * Doc Risk: 63.4876%)
- `typer-0.24.1/typer/_typing.py` -> **Severity: 3144.933** (Blast Radius: 34.479 * Doc Risk: 91.213%)
- `typer-0.24.1/typer/completion.py` -> **Severity: 1927.713** (Blast Radius: 35.44 * Doc Risk: 54.3937%)
- `typer-0.24.1/typer/main.py` -> **Severity: 1269.44** (Blast Radius: 106.494 * Doc Risk: 11.9203%)
- `typer-0.24.1/typer/core.py` -> **Severity: 1184.561** (Blast Radius: 47.136 * Doc Risk: 25.1307%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
