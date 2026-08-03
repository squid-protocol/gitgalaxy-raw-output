# ARCHITECTURAL_BRIEF: python-simplebench
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/python-simplebench` |
| **Timestamp** | `2026-08-03T21:26:39.348639+00:00` |
| **Scan Duration** | `7.28s` |
| **Git Branch** | `main` |
| **Git Commit** | `f36f50afe458be260d7490a0746168ea70423537` |
| **Git Remote** | `https://github.com/JerilynFranz/python-simplebench.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 283 malicious artifacts.

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
| Total Artifacts | 1704 |
| Analyzed Artifacts (Scanned) | 729 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 975 |
| Total LOC | 139301 |
| Volatility Index | 0.012 |
| % Scanned of codebase = | 42.8% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5136 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0889 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.6118 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 43 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 271 | 19948 | 37.2% |
| HTML | 244 | 108998 | 33.5% |
| PLAINTEXT | 176 | 1 | 24.1% |
| CSS | 17 | 8252 | 2.3% |
| JAVASCRIPT | 10 | 955 | 1.4% |
| MARKDOWN | 2 | 0 | 0.3% |
| YAML | 2 | 37 | 0.3% |
| JSON | 2 | 1036 | 0.3% |
| XML | 2 | 0 | 0.3% |
| MAKEFILE | 1 | 20 | 0.1% |
| BATCH | 1 | 52 | 0.1% |
| CSV | 1 | 2 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.75`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_0 | 244 | 33.5% |
| file_cluster_13 | 145 | 19.9% |
| file_cluster_8 | 124 | 17.0% |
| file_cluster_16 | 34 | 4.7% |
| file_cluster_17 | 4 | 0.5% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 177 | 24.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 975*

**Composition by Extension & Reason:**
- `.html`: 308x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 217x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 169x Excluded (Unsupported Extension: '.rst'), 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.doctree`: 134x Excluded (Unsupported Extension: '.doctree'), 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 258 LOC), 1x Excluded (Machine-Generated Source Code Signature: 320 LOC)
- `.js`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 2 exceeds 500 chars), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.css`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Static Asset Blob without Intent: 1266 LOC), 2x Excluded (Machine-Generated Source Code Signature: 278 LOC)
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 51001 LOC exceeds safe regex boundaries), 1x Excluded (Unsupported Extension: '.code-workspace')
- `.png`: 6x Excluded (Explicitly Denied Extension: '.png')
- `.map`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.map'), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.yaml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.inv`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.inv')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 75.0 | 7.5 | 6.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 5.8 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 4.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.6 | 2.3 | 0.0 |
| API Exposure | 0.0 | 13.9 | 6.8 | 5.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 5.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 11.1 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 88.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 6.7 | 0.5 | 0.5 | 0.5 |
| Volatility Exposure | 0.0 | 100.0 | 21.9 | 31.6 | 31.6 |
| Documentation Exposure | 0.0 | 100.0 | 59.4 | 86.7 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 17.2 | 3.2 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 12.2 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `documentation/html/genindex.html` (Hits: 3505)
- `documentation/html/source/simplebench.html` (Hits: 2804)
- `documentation/html/source/simplebench.stats.html` (Hits: 1162)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **simplebench.enums.html** (`documentation/html/source/simplebench.enums.html`) — 81 inbound connections
2. **simplebench.exceptions.html** (`documentation/html/source/simplebench.exceptions.html`) — 75 inbound connections
3. **simplebench.case.html** (`documentation/html/source/simplebench.case.html`) — 37 inbound connections
4. **simplebench.reporters.reporter.html** (`documentation/html/source/simplebench.reporters.reporter.html`) — 32 inbound connections
5. **argparse.py** (`tests/factories/argparse.py`) — 24 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **reporter.py** (`src/simplebench/reporters/reporter/reporter.py`) — 27 outbound dependencies
2. **session.py** (`src/simplebench/session.py`) — 22 outbound dependencies
3. **case.py** (`src/simplebench/case.py`) — 21 outbound dependencies
4. **reporter.py** (`src/simplebench/reporters/json/reporter/reporter.py`) — 21 outbound dependencies
5. **_orchestration.py** (`src/simplebench/reporters/reporter/mixins/_orchestration.py`) — 21 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `benchmark` (@ `src/simplebench/decorators.py`) -> Impact: **1217.3** | LOC: 175
- `report` (@ `src/simplebench/session.py`) -> Impact: **754.9** | LOC: 306
- `render` (@ `src/simplebench/reporters/rich_table/reporter/reporter.py`) -> Impact: **477.6** | LOC: 122
- `dispatch_to_targets` (@ `src/simplebench/reporters/reporter/mixins/_orchestration.py`) -> Impact: **447.0** | LOC: 107
- `render` (@ `src/simplebench/reporters/csv/reporter/reporter.py`) -> Impact: **408.4** | LOC: 109
- `calibrate_rounds` (@ `src/simplebench/runners.py`) -> Impact: **319.6** | LOC: 82
  * *Intent:* # We force a garbage collection before measuring memory usage to reduce noise # from uncollected garbage. It is run separately from the timing to avoi...
- `__init__` (@ `src/simplebench/case.py`) -> Impact: **314.0** | LOC: 107
- `report` (@ `src/simplebench/reporters/reporter/reporter.py`) -> Impact: **280.7** | LOC: 81
- `default_runner` (@ `src/simplebench/runners.py`) -> Impact: **267.0** | LOC: 143
- `validate_iterable_of_type` (@ `src/simplebench/validators/validate_iterable_of_type.py`) -> Impact: **251.1** | LOC: 88

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `benchmark` (@ `src/simplebench/decorators.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `src/simplebench/reporters/choices/choices.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `src/simplebench/reporters/choices/choices_conf.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # pylint: disable=useless-parent-delegation from __future__ import annotations from typing import Iterable from simplebench.reporters.choice.choice_co...
- `__setitem__` (@ `src/simplebench/reporters/graph/matplotlib/theme/base.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """Initialize a :class:`~.Theme` instance. :param rcparams: The rcParams to use for the theme. If ``None``, the default Matplotlib rcParams will be us...
- `__delitem__` (@ `src/simplebench/reporters/graph/matplotlib/theme/base.py`) -> **O(2^N) [Recursive]**
- `register` (@ `src/simplebench/reporters/reporter_manager/manager.py`) -> **O(2^N) [Recursive]**
- `run` (@ `src/simplebench/runners.py`) -> **O(2^N) [Recursive]**
- `report` (@ `src/simplebench/session.py`) -> **O(2^N) [Recursive]**
- `run` (@ `src/simplebench/case.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # All checks passed
- `parse_args` (@ `src/simplebench/session.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """Whether the reporter flags have been added to the ArgumentParser."""

### Highest Data Gravity (Database Complexity)
- `render` (@ `src/simplebench/reporters/csv/reporter/reporter.py`) -> DB Complexity: **28**
- `Stemmer` (@ `documentation/html/_static/language_data.js`) -> DB Complexity: **27**
- `_sanitize_output` (@ `documentation/_helpers/doctest_utils.py`) -> DB Complexity: **19**
- `__init__` (@ `src/simplebench/case.py`) -> DB Complexity: **17**
- `addCopyButtonToCodeCells` (@ `documentation/html/_static/copybutton.js`) -> DB Complexity: **16**
- `report` (@ `src/simplebench/session.py`) -> DB Complexity: **15**
- `__eq__` (@ `src/simplebench/reporters/choice/choice.py`) -> DB Complexity: **14**
- `__eq__` (@ `src/simplebench/reporters/choice/choice_conf.py`) -> DB Complexity: **14**
  * *Intent:* # Ensure that if one is None and the other is not, we set the None one # to the opposite of the other to maintain mutual exclusivity # and to prevent ...
- `render` (@ `src/simplebench/reporters/rich_table/reporter/reporter.py`) -> DB Complexity: **14**
- `_performSearch` (@ `documentation/html/_static/searchtools.js`) -> DB Complexity: **14**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/simplebench` | 15 | 6485.82 | 15.01% | 13.33% |
| `__monolith__` | 5 | 5029.74 | 7.19% | 0.0% |
| `src/simplebench/validators` | 4 | 1673.42 | 6.15% | 73.98% |
| `tests` | 13 | 1592.24 | 3.99% | 0.0% |
| `src/simplebench/stats` | 6 | 1287.3 | 14.94% | 16.67% |
| `src/simplebench/reporters/reporter/mixins` | 5 | 1216.3 | 8.21% | 3.59% |
| `src/simplebench/reporters/reporter` | 6 | 1151.78 | 18.92% | 9.21% |
| `documentation/html/_static` | 16 | 1142.34 | 19.91% | 28.5% |
| `tests/factories` | 11 | 820.8 | 4.8% | 0.0% |
| `tests/reporters/reporter/mixins` | 5 | 794.42 | 2.81% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `documentation/html/_downloads/88e7aae14d90ceb1db4850c2e54e5bc2/minimal_parameterized_benchmark.py` -> **100.0%** Exposure
- `documentation/html/_downloads/bd0058ed5532d517f4f50491559904ce/basic_benchmark.py` -> **100.0%** Exposure
- `documentation/tutorials/basic/basic_benchmark.py` -> **100.0%** Exposure
- `documentation/tutorials/parameterized/minimal_parameterized_benchmark.py` -> **100.0%** Exposure
- `src/simplebench/doc_utils.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/simplebench/reporters/csv/reporter/reporter.py` -> **100.0%** Exposure
- `test_plan.py` -> **100.0%** Exposure
- `documentation/html/_sphinx_design_static/design-tabs.js` -> **100.0%** Exposure
- `documentation/html/_static/design-tabs.js` -> **100.0%** Exposure
- `documentation/html/_static/language_data.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/test_decorators.py` -> **29** Orphaned Functions | **9** Duplicates
- `src/simplebench/stats/stats.py` -> **0** Orphaned Functions | **32** Duplicates
- `src/simplebench/tasks.py` -> **0** Orphaned Functions | **17** Duplicates
- `tests/factories/reporter/reporter_methods.py` -> **0** Orphaned Functions | **15** Duplicates
- `tests/test_case.py` -> **14** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/simplebench/cli.py`** -> AI Confidence: **99.31%**
2. **`src/simplebench/decorators.py`** -> AI Confidence: **99.31%**
3. **`src/simplebench/reporters/csv/reporter/reporter.py`** -> AI Confidence: **99.31%**
4. **`src/simplebench/reporters/reporter/mixins/_argparse.py`** -> AI Confidence: **99.31%**
5. **`src/simplebench/reporters/reporter/mixins/_orchestration.py`** -> AI Confidence: **99.31%**
6. **`src/simplebench/reporters/rich_table/reporter/reporter.py`** -> AI Confidence: **99.31%**
7. **`src/simplebench/runners.py`** -> AI Confidence: **99.31%**
8. **`src/simplebench/tasks.py`** -> AI Confidence: **99.31%**
9. **`tests/reporters/reporter/mixins/test_prioritization.py`** -> AI Confidence: **99.31%**
10. **`tests/reporters/reporter/test_reporter_config.py`** -> AI Confidence: **99.31%**
11. **`tests/test_case.py`** -> AI Confidence: **99.31%**
12. **`src/simplebench/case.py`** -> AI Confidence: **99.24%**
13. **`src/simplebench/reporters/graph/matplotlib/reporter/options/options.py`** -> AI Confidence: **99.24%**
14. **`src/simplebench/reporters/graph/scatterplot/reporter/reporter.py`** -> AI Confidence: **99.24%**
15. **`src/simplebench/session.py`** -> AI Confidence: **99.24%**
16. **`tests/reporters/reporter/test_reporter.py`** -> AI Confidence: **99.24%**
17. **`tests/test_results.py`** -> AI Confidence: **99.24%**
18. **`tests/test_stats.py`** -> AI Confidence: **99.24%**
19. **`src/simplebench/reporters/choices/_base.py`** -> AI Confidence: **99.23%**
20. **`src/simplebench/reporters/choice/choice.py`** -> AI Confidence: **99.18%**
21. **`src/simplebench/reporters/json/reporter/reporter.py`** -> AI Confidence: **99.18%**
22. **`src/simplebench/reporters/reporter/prioritized.py`** -> AI Confidence: **99.18%**
23. **`src/simplebench/timers/info.py`** -> AI Confidence: **99.18%**
24. **`src/simplebench/type_proxies/case_type_proxy.py`** -> AI Confidence: **99.18%**
25. **`tests/factories/reporter/report_log_metadata.py`** -> AI Confidence: **99.18%**
26. **`tests/reporters/reporter/mixins/test_argparse.py`** -> AI Confidence: **99.18%**
27. **`tests/reporters/reporter/mixins/test_targets.py`** -> AI Confidence: **99.18%**
28. **`tests/reporters/validators/test_validate_report_renderer.py`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `src/simplebench/case.py` -> **100.0%** Exposure
- `src/simplebench/cli.py` -> **100.0%** Exposure
- `src/simplebench/decorators.py` -> **100.0%** Exposure
- `src/simplebench/doc_utils.py` -> **100.0%** Exposure
- `src/simplebench/iteration.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `documentation/_helpers/doctest_utils.py` -> **100.0%** Exposure
- `documentation/html/_static/searchtools.js` -> **78.2113%** Exposure
### Algorithmic DoS Exposure
- `documentation/_helpers/doctest_utils.py` -> **100.0%** Exposure
- `src/simplebench/case.py` -> **100.0%** Exposure
- `src/simplebench/cli.py` -> **100.0%** Exposure
- `src/simplebench/iteration.py` -> **100.0%** Exposure
- `src/simplebench/reporters/choice/choice.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1204` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/simplebench/timeout/timeout.py` (PYTHON) -> Cumulative Risk: **798.17**
- **Archetype:** `file_cluster_13` (Distance: 12.643 IQR)
- **Magnitude:** 105.66 | **LOC:** 180 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `run` (Impact: 36.5), `_set_timeout_interval` (Impact: 17.9), `_target_wrapper` (Impact: 10.1)

### 2. `src/simplebench/reporters/csv/reporter/reporter.py` (PYTHON) -> Cumulative Risk: **756.25**
- **Archetype:** `file_cluster_13` (Distance: 12.675 IQR)
- **Magnitude:** 511.98 | **LOC:** 213 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `render` (Impact: 408.4), `__init__` (Impact: 14.2)

### 3. `src/simplebench/case.py` (PYTHON) -> Cumulative Risk: **748.04**
- **Archetype:** `file_cluster_16` (Distance: 12.284 IQR)
- **Magnitude:** 1048.72 | **LOC:** 1016 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 314.0), `run` (Impact: 199.6), `validate_action_signature` (Impact: 115.6)

### 4. `documentation/_helpers/doctest_utils.py` (PYTHON) -> Cumulative Risk: **744.29**
- **Archetype:** `file_cluster_13` (Distance: 9.204 IQR)
- **Magnitude:** 65.06 | **LOC:** 99 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `_sanitize_output` (Impact: 58.9)

### 5. `src/simplebench/stats/stats.py` (PYTHON) -> Cumulative Risk: **743.23**
- **Archetype:** `file_cluster_16` (Distance: 11.601 IQR)
- **Magnitude:** 562.32 | **LOC:** 614 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `__eq__` (Impact: 86.8), `__eq__` (Impact: 86.8), `from_dict` (Impact: 43.1)

### 6. `src/simplebench/reporters/rich_table/reporter/reporter.py` (PYTHON) -> Cumulative Risk: **715.57**
- **Archetype:** `file_cluster_13` (Distance: 11.437 IQR)
- **Magnitude:** 539.42 | **LOC:** 226 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9974%)
- **Heaviest Functions:** `render` (Impact: 477.6), `__init__` (Impact: 14.2)

### 7. `src/simplebench/session.py` (PYTHON) -> Cumulative Risk: **709.96**
- **Archetype:** `file_cluster_13` (Distance: 13.349 IQR)
- **Magnitude:** 1176.02 | **LOC:** 607 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `report` (Impact: 754.9), `run` (Impact: 105.7), `parse_args` (Impact: 84.2)

### 8. `src/simplebench/tasks.py` (PYTHON) -> Cumulative Risk: **707.57**
- **Archetype:** `file_cluster_16` (Distance: 12.829 IQR)
- **Magnitude:** 923.3 | **LOC:** 534 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9999%)
- **Heaviest Functions:** `update` (Impact: 229.8), `__init__` (Impact: 82.0), `__init__` (Impact: 60.8)

### 9. `documentation/html/_static/searchtools.js` (JAVASCRIPT) -> Cumulative Risk: **705.83**
- **Archetype:** `file_cluster_17` (Distance: 12.179 IQR)
- **Magnitude:** 452.38 | **LOC:** 633 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.5749%)
- **Heaviest Functions:** `performTermsSearch` (Impact: 88.2), `_performSearch` (Impact: 87.9), `_displayItem` (Impact: 50.6)

### 10. `src/simplebench/validators/validate_iterable_of_type.py` (PYTHON) -> Cumulative Risk: **665.48**
- **Archetype:** `file_cluster_16` (Distance: 10.888 IQR)
- **Magnitude:** 269.28 | **LOC:** 158 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (99.9692%), Tech Debt (99.6245%), Algorithmic Dos (98.5296%)
- **Heaviest Functions:** `validate_iterable_of_type` (Impact: 251.1), `validate_iterable_of_type` (Impact: 5.2), `validate_iterable_of_type` (Impact: 5.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/decorators.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.383 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.606 IQR)
- **Top Global Matches:** file_cluster_16: 10.383, file_cluster_13: 10.423, file_cluster_8: 10.522
- **Magnitude:** 1238.5 | **LOC:** 373 | **CtrlFlow:** 55.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (9.5644%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `benchmark` (Impact: 1217.3 | O(2^N) | DB: 1)
  * `get_registered_cases` (Impact: 1.9 | O(N^1))
  * `clear_registered_cases` (Impact: 1.9 | O(N^1) | DB: 1)
  * `validate_timer` (Impact: 1.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 33`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 4`
* *Architecture:* `api: 8`, `import: 10`
* *Defense:* `safety: 6`, `doc: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .exceptions, .case, .vcs, .validators, simplebench, typing, __future__, .doc_utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/session.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.349 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.299 IQR)
- **Top Global Matches:** file_cluster_13: 13.349, file_cluster_16: 13.441, file_cluster_0: 13.526
- **Magnitude:** 1176.02 | **LOC:** 607 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (31.4834%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `report` (Impact: 754.9 | O(2^N) | DB: 15)
  * `run` (Impact: 105.7 | O(2^N) | DB: 4)
  * `parse_args` (Impact: 84.2 | O(2^N) | DB: 2)
    * *Intent:* """Whether the reporter flags have been added to the ArgumentParser."""
  * `__init__` (Impact: 80.3 | O(N^4) | DB: 8)
  * `report_keys` (Impact: 26.5 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 113`, `args: 29`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 71`
* *Architecture:* `io: 1`, `api: 30`, `import: 21`
* *Defense:* `safety: 20`, `doc: 122`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` simplebench.reporters.protocols, mybenchmark.runners, simplebench.reporters.choices, simplebench.reporters.reporter, __future__, simplebench.enums, simplebench.reporters.choice, pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/validators/misc.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.337 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.972 IQR)
- **Top Global Matches:** file_cluster_8: 11.337, file_cluster_16: 11.343, file_cluster_7: 11.51
- **Magnitude:** 1117.94 | **LOC:** 1100 | **CtrlFlow:** 47.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (5.9043%), Tech Debt (96.6814%)
**Top Internal Functions/Classes:**
  * `validate_int_range` (Impact: 128.7 | O(2^N))
  * `validate_dirpath` (Impact: 111.1 | O(N^4))
  * `validate_sequence_of_str` (Impact: 96.0 | O(N^6))
  * `validate_string` (Impact: 91.5 | O(N^3))
  * `validate_float_range` (Impact: 86.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 152`, `args: 28`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 1`, `duplicate_logic: 13`
* *Architecture:* `io: 1`, `api: 30`, `import: 6`
* *Defense:* `safety: 41`, `doc: 200`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` simplebench.type_proxies.lazy_type_proxy, pathlib, simplebench.validators.exceptions, simplebench.exceptions, typing, re
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/case.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.284 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.156 IQR)
- **Top Global Matches:** file_cluster_16: 12.284, file_cluster_13: 12.348, file_cluster_0: 12.466
- **Magnitude:** 1048.72 | **LOC:** 1016 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (38.9214%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 314.0 | O(N^6) | DB: 17)
  * `run` (Impact: 199.6 | O(2^N) | DB: 2)
    * *Intent:* # All checks passed
  * `validate_action_signature` (Impact: 115.6 | O(N^6))
  * `validate_variation_cols` (Impact: 64.1 | O(N^6))
  * `validate_kwargs_variations` (Impact: 53.7 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 127`, `args: 30`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 39`
* *Architecture:* `io: 1`, `api: 31`, `import: 20`
* *Defense:* `safety: 20`, `doc: 125`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .enums, __future__, simplebench.defaults, .results, .tasks, pathlib, .vcs, simplebench...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/tasks.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.829 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 6.269 IQR)
- **Top Global Matches:** file_cluster_16: 12.829, file_cluster_13: 12.936, file_cluster_8: 13.115
- **Magnitude:** 923.3 | **LOC:** 534 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (21.5892%), Tech Debt (99.9994%)
**Top Internal Functions/Classes:**
  * `update` (Impact: 229.8 | O(2^N) | DB: 1)
  * `__init__` (Impact: 82.0 | O(N^6))
  * `__init__` (Impact: 60.8 | O(N^5) | DB: 3)
  * `update` (Impact: 49.8 | O(2^N) | DB: 3)
  * `reset` (Impact: 43.7 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 76`, `args: 29`, `func_start: 29`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 49`, `duplicate_logic: 17`
* *Architecture:* `api: 30`, `import: 8`
* *Defense:* `safety: 15`, `doc: 158`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .enums, rich.progress, .exceptions, .exceptions.tasks, .session, typing, __future__, rich.console
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/runners.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.112 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.587 IQR)
- **Top Global Matches:** file_cluster_13: 11.112, file_cluster_16: 11.174, file_cluster_8: 11.476
- **Magnitude:** 870.66 | **LOC:** 544 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (9.8692%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `calibrate_rounds` (Impact: 319.6 | O(N^6))
    * *Intent:* # We force a garbage collection before measuring memory usage to reduce noise # from uncollected gar...
  * `default_runner` (Impact: 267.0 | O(N^5) | DB: 2)
  * `run` (Impact: 98.7 | O(2^N))
  * `_run_timed_iteration` (Impact: 86.1 | O(N^4))
    * *Intent:* # The Timeout class acts similarly to a context manager, but here we use it # to wrap the entire ben...
  * `__init__` (Impact: 45.8 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 59`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 9`, `dead_code: 2`
* *Architecture:* `io: 3`, `api: 6`, `import: 19`
* *Defense:* `safety: 8`, `doc: 70`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .enums, importlib.util, .defaults, .iteration, __future__, .results, gc, .tasks...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/reporters/reporter/mixins/_orchestration.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.381 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.353 IQR)
- **Top Global Matches:** file_cluster_8: 10.381, file_cluster_13: 10.445, file_cluster_7: 10.587
- **Magnitude:** 745.9 | **LOC:** 467 | **CtrlFlow:** 64.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.1708%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dispatch_to_targets` (Impact: 447.0 | O(N^6))
  * `render_by_case` (Impact: 151.0 | O(N^5))
  * `render_by_section` (Impact: 134.6 | O(N^4))
  * `_validate_render_by_args` (Impact: 3.5 | O(N^2))
    * *Intent:* """Mixin for orchestration-related functionality for the Reporter class. It provides methods to orch...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 50`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 5`, `import: 19`
* *Defense:* `safety: 7`, `doc: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.196
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001374
  * `Imports (Out-Degree: 15):` simplebench.validators, simplebench.reporters.protocols, simplebench.reporters.reporter.prioritized, __future__, simplebench.enums, rich.text, rich.table, pathlib...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/simplebench/reporters/reporter/reporter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.776 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.409 IQR)
- **Top Global Matches:** file_cluster_13: 11.776, file_cluster_16: 11.916, file_cluster_11: 12.018
- **Magnitude:** 722.5 | **LOC:** 647 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (37.4191%), Tech Debt (40.0538%)
**Top Internal Functions/Classes:**
  * `report` (Impact: 280.7 | O(N^6) | DB: 6)
  * `set_default_options` (Impact: 87.4 | O(2^N))
  * `_validate_subclass_config` (Impact: 76.2 | O(N^4))
    * *Intent:* """Deferred import of core types to avoid circular imports during initialization. This imports :clas...
  * `get_base_unit_for_section` (Impact: 37.2 | O(N^5))
  * `run_report` (Impact: 32.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 120`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 10`, `planned_debt: 12`
* *Architecture:* `io: 3`, `api: 31`, `import: 25`
* *Defense:* `safety: 15`, `doc: 123`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` simplebench.validators, simplebench.reporters.protocols, __future__, simplebench.reporters.reporter.config, of, simplebench.enums, simplebench.reporters.choices.choices, simplebench.defaults...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/stats/stats.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.601 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.321 IQR)
- **Top Global Matches:** file_cluster_16: 11.601, file_cluster_0: 11.824, file_cluster_13: 11.862
- **Magnitude:** 562.32 | **LOC:** 614 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (40.0547%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__eq__` (Impact: 86.8 | O(N^6))
  * `__eq__` (Impact: 86.8 | O(N^6))
  * `from_dict` (Impact: 43.1 | O(N^6))
  * `from_dict` (Impact: 28.9 | O(N^6))
  * `mean` (Impact: 28.0 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 102`, `args: 35`, `func_start: 35`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 32`, `duplicate_logic: 32`
* *Architecture:* `api: 30`, `import: 8`
* *Defense:* `safety: 5`, `doc: 108`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ..si_units, statistics, ..validators, typing, math, __future__, .exceptions.stats, ..exceptions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/reporters/rich_table/reporter/reporter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.437 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.989 IQR)
- **Top Global Matches:** file_cluster_13: 11.437, file_cluster_8: 11.918, file_cluster_17: 12.009
- **Magnitude:** 539.42 | **LOC:** 226 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (43.824%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 477.6 | O(N^6) | DB: 14)
  * `__init__` (Impact: 14.2 | O(2^N))
    * *Intent:* **Defined command-line flags:**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 38`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 42`
* *Architecture:* `api: 3`, `import: 16`
* *Defense:* `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` rich.table, simplebench.utils, .config, simplebench.validators, .exceptions, validation, simplebench.case, simplebench.type_proxies...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/reporters/csv/reporter/reporter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.675 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.265 IQR)
- **Top Global Matches:** file_cluster_13: 12.675, file_cluster_16: 13.209, file_cluster_8: 13.293
- **Magnitude:** 511.98 | **LOC:** 213 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (46.6065%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `render` (Impact: 408.4 | O(N^6) | DB: 28)
  * `__init__` (Impact: 14.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 42`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 84`
* *Architecture:* `api: 3`, `import: 18`
* *Defense:* `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` .config, simplebench.validators, __future__, simplebench.enums, simplebench.si_units, simplebench.defaults, simplebench.exceptions, simplebench.reporters.reporter.options...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/reporters/reporter/mixins/test_prioritization.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.227 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.102 IQR)
- **Top Global Matches:** file_cluster_16: 10.227, file_cluster_8: 10.261, file_cluster_13: 10.452
- **Magnitude:** 485.86 | **LOC:** 663 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (3.6608%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_prioritized_options_testspecs` (Impact: 192.6 | O(N^5) | DB: 4)
  * `get_prioritized_file_append_and_unique_t` (Impact: 165.3 | O(N^6) | DB: 1)
  * `get_prioritized_file_suffix_testspecs` (Impact: 20.9 | O(N^6) | DB: 1)
  * `get_prioritized_default_targets_testspec` (Impact: 20.7 | O(N^6) | DB: 1)
  * `get_prioritized_subdir_testspecs` (Impact: 20.7 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 58`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 24`, `orphaned_logic: 9`
* *Architecture:* `api: 15`, `import: 12`
* *Defense:* `safety: 5`, `doc: 75`, `test: 17`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` pytest, ....factories, simplebench.case, dataclasses, simplebench.exceptions, simplebench.reporters.choices.choices_conf, simplebench.reporters.reporter.exceptions, simplebench.reporters.reporter.options...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/reporters/graph/matplotlib/reporter/options/options.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.34 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.5 IQR)
- **Top Global Matches:** file_cluster_16: 12.34, file_cluster_0: 12.481, file_cluster_13: 12.533
- **Magnitude:** 456.0 | **LOC:** 638 | **CtrlFlow:** 39.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (45.6204%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 132.5 | O(N^5) | DB: 2)
  * `set_default_y_starts_at_zero` (Impact: 17.7 | O(N^4) | DB: 1)
  * `set_default_x_labels_rotation` (Impact: 17.7 | O(N^4))
    * *Intent:* """ return cls._HARDCODED_IMAGE_TYPE _DEFAULT_WIDTH: int | None = None """:meta private:"""
  * `set_default_style` (Impact: 17.7 | O(N^4) | DB: 1)
  * `set_default_theme` (Impact: 17.7 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 82`, `args: 33`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 50`, `import: 8`
* *Defense:* `safety: 4`, `doc: 185`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` .exceptions, ...theme, simplebench.validators, simplebench.reporters.graph.options, ...enums.style, simplebench.exceptions, typing, simplebench.reporters.graph.enums.image_type
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `documentation/html/_static/searchtools.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.179 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.151 IQR)
- **Top Global Matches:** file_cluster_17: 12.179, file_cluster_8: 12.591, file_cluster_11: 12.693
- **Magnitude:** 452.38 | **LOC:** 633 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (50.4951%), Tech Debt (9.8548%)
**Top Internal Functions/Classes:**
  * `performTermsSearch` (Impact: 88.2 | O(N^3) | DB: 8)
  * `_performSearch` (Impact: 87.9 | O(N^3) | DB: 14)
  * `_displayItem` (Impact: 50.6 | O(N^3) | DB: 8)
  * `performObjectSearch` (Impact: 39.8 | O(N^2) | DB: 4)
  * `_parseQuery` (Impact: 17.5 | O(N^2) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 69`, `args: 41`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 103`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 2`, `concurrency: 2`
* *Defense:* `safety: 23`, `doc: 6`, `immutability_locks: 71`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_decorators.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.152 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.254 IQR)
- **Top Global Matches:** file_cluster_0: 12.152, file_cluster_16: 12.202, file_cluster_8: 12.273
- **Magnitude:** 424.02 | **LOC:** 708 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (1.7546%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_run_decorated_case` (Impact: 26.4 | O(N^3))
  * `test_decorator_use_field_for_n_valid` (Impact: 19.1 | O(N^3))
  * `test_benchmark_decorator_registers_case` (Impact: 15.4 | O(N^3))
  * `test_decorator_invalid_use_field_for_n_t` (Impact: 9.5 | O(N^4))
    * *Intent:* """Test that the ``@benchmark`` decorator raises expected errors for invalid use_field_for_n type.""...
  * `test_decorator_use_field_for_n_not_in_kw` (Impact: 9.5 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 241`, `args: 77`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 38`, `duplicate_logic: 9`, `orphaned_logic: 29`
* *Architecture:* `api: 78`, `import: 7`
* *Defense:* `safety: 74`, `doc: 100`, `test: 145`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` pytest, simplebench.session, simplebench.exceptions, __future__, simplebench.enums, simplebench.decorators, simplebench.defaults
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/reporters/choice/choice_conf.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.878 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.802 IQR)
- **Top Global Matches:** file_cluster_13: 12.878, file_cluster_16: 12.92, file_cluster_0: 13.036
- **Magnitude:** 398.76 | **LOC:** 485 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (48.823%), Tech Debt (12.112%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 205.3 | O(N^5) | DB: 8)
  * `__eq__` (Impact: 66.0 | O(N^4) | DB: 14)
    * *Intent:* # Ensure that if one is None and the other is not, we set the None one # to the opposite of the othe...
  * `__hash__` (Impact: 4.4 | O(N^3))
  * `flags` (Impact: 2.8 | O(N^2))
  * `flag_type` (Impact: 2.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 51`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 62`, `planned_debt: 1`
* *Architecture:* `api: 18`, `import: 8`
* *Defense:* `safety: 1`, `doc: 129`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` collections.abc, simplebench.validators, simplebench.reporters.protocols, simplebench.reporters.choice.exceptions, simplebench.exceptions, typing, simplebench.reporters.reporter.options, simplebench.enums
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/factories/reporter/base.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.762 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.759 IQR)
- **Top Global Matches:** file_cluster_16: 11.762, file_cluster_13: 11.804, file_cluster_0: 12.053
- **Magnitude:** 386.14 | **LOC:** 751 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.2885%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `choice_factory` (Impact: 104.2 | O(N^6))
  * `choices_factory` (Impact: 54.6 | O(N^5))
  * `choice_conf_factory` (Impact: 43.9 | O(N^6))
  * `reporter_factory` (Impact: 36.5 | O(N^5))
  * `__init__` (Impact: 26.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 90`, `args: 27`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `duplicate_logic: 8`
* *Architecture:* `api: 31`, `import: 20`
* *Defense:* `safety: 9`, `doc: 160`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` simplebench.reporters.choices, simplebench.enums, .._utils, simplebench.reporters.choice, rich.text, rich.table, ..argparse, .reporter_config...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/results.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.41 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.0 IQR)
- **Top Global Matches:** file_cluster_16: 10.41, file_cluster_8: 10.744, file_cluster_13: 10.82
- **Magnitude:** 373.8 | **LOC:** 670 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (15.4685%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `results_section` (Impact: 47.9 | O(N^5))
  * `_validate_variation_cols` (Impact: 43.5 | O(N^5))
  * `_validate_variation_marks` (Impact: 37.5 | O(N^5))
  * `_validate_iterations` (Impact: 21.6 | O(N^5))
  * `_validate_peak_memory` (Impact: 18.9 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 130`, `args: 33`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 4`
* *Architecture:* `api: 25`, `import: 10`
* *Defense:* `safety: 13`, `doc: 112`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .enums, .stats, .defaults, .validators, simplebench.exceptions, typing, .iteration, __future__...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/cli.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.306 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.362 IQR)
- **Top Global Matches:** file_cluster_13: 10.306, file_cluster_8: 10.479, file_cluster_16: 10.707
- **Magnitude:** 317.36 | **LOC:** 235 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (9.1998%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 163.4 | O(N^4) | DB: 10)
  * `_configure_session_from_args` (Impact: 121.0 | O(N^6))
  * `_create_parser` (Impact: 25.1 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 36`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`
* *Architecture:* `io: 5`, `api: 2`, `import: 12`
* *Defense:* `safety: 10`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .enums, .exceptions, .case, pathlib, .session, .decorators, sys, typing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/factories/argparse.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.05%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.824 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.756 IQR)
- **Top Global Matches:** file_cluster_16: 11.824, file_cluster_13: 11.859, file_cluster_8: 11.941
- **Magnitude:** 316.32 | **LOC:** 192 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.1905%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `list_of_strings_flag_factory` (Impact: 113.5 | O(N^6))
  * `boolean_flag_factory` (Impact: 91.9 | O(N^6))
    * *Intent:* """ if args is None: args = [] if argparser is not None: return argparser.parse_args(args=args) arg_...
  * `argument_parser_factory` (Impact: 78.1 | O(N^6))
  * `reporter_namespace_factory` (Impact: 13.6 | O(N^2))
  * `namespace_factory` (Impact: 9.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 23`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 5`
* *Architecture:* `api: 8`, `import: 6`
* *Defense:* `safety: 11`, `doc: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.901
  * `Choke Point (Betweenness):` 6.9e-05 | `Ripple Effect (Closeness):` 0.034738
  * `Imports (Out-Degree: 2):` ._primitives, typing, __future__, simplebench.enums, re, argparse
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `tests/test_case.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.148 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.457 IQR)
- **Top Global Matches:** file_cluster_8: 10.148, file_cluster_16: 10.397, file_cluster_7: 10.423
- **Magnitude:** 309.48 | **LOC:** 1140 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (2.7506%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_run` (Impact: 28.8 | O(N^3))
  * `postrun_benchmark_case` (Impact: 13.9 | O(N^2))
  * `broken_benchcase_missing_bench` (Impact: 12.8 | O(N^3))
  * `benchcase_with_size_and_factor` (Impact: 10.9 | O(N^2))
  * `base_casekwargs` (Impact: 7.7 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 137`, `args: 57`, `func_start: 49`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 1`, `orphaned_logic: 14`
* *Architecture:* `api: 50`, `import: 18`
* *Defense:* `safety: 10`, `doc: 138`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` functools, __future__, simplebench.exceptions.case, simplebench.enums, pytest, simplebench.runners, simplebench.exceptions, simplebench.reporters.reporter.options...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/reporters/validators/test_validate_report_renderer.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.89 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.141 IQR)
- **Top Global Matches:** file_cluster_13: 10.89, file_cluster_16: 10.905, file_cluster_8: 10.937
- **Magnitude:** 306.18 | **LOC:** 588 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.1233%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_report` (Impact: 32.6 | O(N^4))
  * `invalid_render_with_extra_return_type` (Impact: 15.1 | O(N^3))
  * `invalid_render_case_wrong_type` (Impact: 14.9 | O(N^3))
  * `invalid_render_case_missing_type_hint` (Impact: 14.9 | O(N^3))
    * *Intent:* """An invalid render method for testing purposes. :param case: The benchmark case. :type case: Case ...
  * `invalid_render_extra_parameter` (Impact: 10.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 118`, `args: 25`, `func_start: 25`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `orphaned_logic: 4`
* *Architecture:* `io: 1`, `api: 26`, `import: 19`
* *Defense:* `doc: 219`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` ...testspec, simplebench.reporters.protocols, simplebench.enums, simplebench.reporters.choice, rich.text, rich.table, pytest, ...factories...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/simplebench/reporters/graph/scatterplot/reporter/reporter.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.054 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.485 IQR)
- **Top Global Matches:** file_cluster_13: 10.054, file_cluster_8: 10.531, file_cluster_16: 10.605
- **Magnitude:** 299.98 | **LOC:** 223 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (11.6012%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_old_render` (Impact: 157.2 | O(N^6) | DB: 2)
  * `render` (Impact: 114.2 | O(N^6) | DB: 2)
    * *Intent:* """ _OPTIONS_TYPE: ClassVar[type[ScatterPlotOptions]] = ScatterPlotOptions # pylint: disable=line-to...
  * `__init__` (Impact: 14.2 | O(2^N))
    * *Intent:* **Defined command-line flags:** * ``--scatter-plot: {filesystem, callback}`` (default=filesystem) * ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 49`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 8`
* *Architecture:* `api: 4`, `import: 19`
* *Defense:* `doc: 30`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` .config, simplebench.validators, validation, __future__, simplebench.enums, simplebench.si_units, simplebench.exceptions, .options...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_stats.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.415 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.967 IQR)
- **Top Global Matches:** file_cluster_8: 9.415, file_cluster_7: 9.879, file_cluster_16: 10.11
- **Magnitude:** 284.16 | **LOC:** 1109 | **CtrlFlow:** 40.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (1.9966%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_stats_initalization` (Impact: 98.7 | O(N^5) | DB: 1)
  * `test_computed_stats_values` (Impact: 69.3 | O(N^4))
    * *Intent:* """Test that computed stats properties exist and are read-only. :param stats_instances: List of stat...
  * `test_as_dict` (Impact: 26.3 | O(N^3))
  * `test_computed_stats_read_only` (Impact: 16.4 | O(N^3))
    * *Intent:* """ for stats_instance in stats_instances: test.name = f"{test.name} ({type(stats_instance).__name__...
  * `test_stats_init` (Impact: 5.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 124`, `args: 18`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 3`, `orphaned_logic: 11`
* *Architecture:* `api: 16`, `import: 10`
* *Defense:* `safety: 31`, `doc: 73`, `test: 71`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.986
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` pytest, statistics, simplebench.stats, enum, simplebench.exceptions, typing, .testspec, simplebench.enums...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `documentation/html/py-modindex.html` (HTML) | Magnitude: 0.08 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1205, decorators: 447, io: 401, ui_framework: 173
- `tests/test_decorators.py` (PYTHON) | Magnitude: 424.02 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 423, structural_boundaries: 241, test: 145, doc: 100
- `documentation/html/reports/csv_report_field_definitions.html` (HTML) | Magnitude: 0.07 | Delta: **0.154 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 252, indent_spaces: 226, decorators: 164, io: 102
- `documentation/html/_modules/index.html` (HTML) | Magnitude: 0.06 | Delta: **0.26 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: io: 227, indent_spaces: 208, structural_boundaries: 140, decorators: 110
- `documentation/html/reports/rich_table_report.html` (HTML) | Magnitude: 0.08 | Delta: **0.295 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 356, decorators: 309, indent_spaces: 244, io: 134

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/reporters/validators/test_validate_report_renderer.py` (PYTHON) | Magnitude: 306.18 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 256, doc: 219, structural_boundaries: 118, branch: 43
- `tests/type_proxies/test_case_type.py` (PYTHON) | Magnitude: 7.2 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 9, doc: 6, test: 5
- `src/simplebench/type_proxies/__init__.py` (PYTHON) | Magnitude: 16.28 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 8, doc: 4, import: 4
- `tests/factories/reporter/reporter_methods.py` (PYTHON) | Magnitude: 192.38 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 191, doc: 86, structural_boundaries: 69, branch: 29
- `tests/factories/session.py` (PYTHON) | Magnitude: 17.54 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 32, structural_boundaries: 22, indent_spaces: 8, import: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/simplebench/iteration.py` (PYTHON) | Magnitude: 160.58 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 106, doc: 50, encapsulation: 47, structural_boundaries: 44
- `tests/cache_factory.py` (PYTHON) | Magnitude: 133.3 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 67, doc: 42, structural_boundaries: 29, encapsulation: 26
- `tests/factories/path.py` (PYTHON) | Magnitude: 12.08 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 25, structural_boundaries: 17, api: 6, args: 5
- `tests/reporters/reporter/mixins/test_prioritization.py` (PYTHON) | Magnitude: 485.86 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 447, doc: 75, structural_boundaries: 58, branch: 56
- `tests/factories/argparse.py` (PYTHON) | Magnitude: 316.32 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 75, branch: 45, doc: 38, structural_boundaries: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `documentation/html/_static/sphinx_highlight.js` (JAVASCRIPT) | Magnitude: 154.86 | Delta: **0.182 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 103, branch: 26, structural_boundaries: 25, immutability_locks: 18
- `documentation/html/_sphinx_design_static/design-tabs.js` (JAVASCRIPT) | Magnitude: 84.12 | Delta: **0.222 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 47, state_mutation: 31, branch: 13, structural_boundaries: 13
- `documentation/html/_static/design-tabs.js` (JAVASCRIPT) | Magnitude: 84.12 | Delta: **0.222 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 47, state_mutation: 31, branch: 13, structural_boundaries: 13
- `documentation/html/_static/searchtools.js` (JAVASCRIPT) | Magnitude: 452.38 | Delta: **0.412 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 333, state_mutation: 103, branch: 80, immutability_locks: 71

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/simplebench/reporters/csv/reporter/options/fields.py` (PYTHON) | Magnitude: 16.32 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 28, indent_spaces: 12, structural_boundaries: 5, import: 2
- `src/simplebench/reporters/rich_table/reporter/options/fields.py` (PYTHON) | Magnitude: 16.32 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 28, indent_spaces: 12, structural_boundaries: 5, import: 2
- `src/simplebench/validators/misc.py` (PYTHON) | Magnitude: 1117.94 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 514, doc: 200, structural_boundaries: 152, branch: 135
- `src/simplebench/timers/exceptions.py` (PYTHON) | Magnitude: 15.24 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 20, indent_spaces: 8, structural_boundaries: 5, import: 2
- `src/simplebench/stats/__init__.py` (PYTHON) | Magnitude: 16.34 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 10, import: 5, doc: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `documentation/_static/custom.css` -> Churn: **94.64%** | Cog Load: 5.3338% | Debt: 79.673%
- `src/simplebench/exceptions/__init__.py` -> Churn: **73.25%** | Cog Load: 5.1716% | Debt: 100.0%
- `documentation/tutorials/parameterized/minimal_parameterized_benchmark.py` -> Churn: **63.09%** | Cog Load: 5.0% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/simplebench/decorators.py` -> **Jerilyn** (100.0% isolated ownership) | Magnitude: 1238.5
- `src/simplebench/session.py` -> **Jerilyn** (100.0% isolated ownership) | Magnitude: 1176.02
- `src/simplebench/case.py` -> **Jerilyn** (100.0% isolated ownership) | Magnitude: 1048.72
- `src/simplebench/runners.py` -> **Jerilyn** (100.0% isolated ownership) | Magnitude: 870.66
- `src/simplebench/stats/stats.py` -> **Jerilyn** (100.0% isolated ownership) | Magnitude: 562.32

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tests/cache_factory.py` -> **Severity: 1.516** (Embedded: 0.0262 * Error Risk: 57.7778%)
- `tests/kwargs/results_kwargs.py` -> **Severity: 0.211** (Embedded: 0.0027 * Error Risk: 76.875%)
- `tests/kwargs/case_kwargs.py` -> **Severity: 0.166** (Embedded: 0.0027 * Error Risk: 60.303%)
- `tests/factories/reporter/reporter_methods.py` -> **Severity: 0.141** (Embedded: 0.0027 * Error Risk: 51.3675%)
- `src/simplebench/reporters/choices/_base.py` -> **Severity: 0.127** (Embedded: 0.0027 * Error Risk: 46.129%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/simplebench/timeout/enums.py` -> **Severity: 137.224** (Blast Radius: 15.698 * Doc Risk: 8.7415%)
- `src/simplebench/reporters/graph/matplotlib/theme/base.py` -> **Severity: 126.591** (Blast Radius: 1.266 * Doc Risk: 99.9932%)
- `src/simplebench/reporters/reporter/mixins/_prioritization.py` -> **Severity: 119.6** (Blast Radius: 1.196 * Doc Risk: 100.0%)
- `src/simplebench/reporters/reporter/mixins/_targets.py` -> **Severity: 118.674** (Blast Radius: 1.196 * Doc Risk: 99.2259%)
- `src/simplebench/reporters/choices/_base.py` -> **Severity: 108.687** (Blast Radius: 1.476 * Doc Risk: 73.6363%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
