# ARCHITECTURAL_BRIEF: coverage
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/coverage` |
| **Timestamp** | `2026-08-03T21:20:05.167468+00:00` |
| **Scan Duration** | `0.89s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 128 malicious artifacts.

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
| Total Artifacts | 312 |
| Analyzed Artifacts (Scanned) | 216 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 96 |
| Total LOC | 26669 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 69.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5849 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6568 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.9487 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 12 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 114 | 16829 | 52.8% |
| HTML | 70 | 8538 | 32.4% |
| PLAINTEXT | 13 | 0 | 6.0% |
| M4 | 7 | 54 | 3.2% |
| CSS | 4 | 455 | 1.9% |
| MAKEFILE | 2 | 248 | 0.9% |
| SHELL | 2 | 50 | 0.9% |
| JAVASCRIPT | 2 | 494 | 0.9% |
| XML | 1 | 0 | 0.5% |
| BINARY_THREAT | 1 | 1 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.465`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 94 | 43.5% |
| file_cluster_0 | 59 | 27.3% |
| file_cluster_13 | 35 | 16.2% |
| file_cluster_16 | 13 | 6.0% |
| file_cluster_17 | 1 | 0.5% |
| Unknown | 1 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 13 | 6.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 96*

**Composition by Extension & Reason:**
- `.rst`: 41x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 13x Excluded (Unsupported Extension: '.py,cover'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.pip`: 8x Excluded (Unsupported Extension: '.pip'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 8x Excluded (Explicitly Denied Extension: '.png')
- `.py`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 261 LOC)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.ini`: 2x Excluded (Unsupported Extension: '.ini')
- `.xml`: 1x Excluded (Machine-Generated Source Code Signature: 23 LOC), 1x Excluded (Machine-Generated Source Code Signature: 25 LOC)
- `.tok`: 2x Excluded (Unsupported Extension: '.tok')
- `.cff`: 1x Excluded (Unsupported Extension: '.cff')
- `.dtd`: 1x Excluded (Unsupported Extension: '.dtd')
- `.in`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.html`: 1x Excluded (Saturation: Line 88 exceeds 500 chars)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 84.4 | 4.4 | 2.5 | 0.0 |
| Error & Exception Exposure | 0.0 | 86.3 | 7.7 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 2.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.9 | 0.0 | 0.0 |
| API Exposure | 0.0 | 15.2 | 6.4 | 7.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 14.2 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 78.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 50.0 | 49.8 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 8.8 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 27.2 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 2.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 21.4 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 4.4 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `coverage-7.13.5/tests/gold/html/b_branch/b_py.html` (Hits: 74)
- `coverage-7.13.5/tests/gold/html/contexts/two_tests_py.html` (Hits: 64)
- `coverage-7.13.5/tests/gold/html/multiline/multiline_py.html` (Hits: 56)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **coverage_html_cb_bcae5fc4.js** (`coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js`) — 45 inbound connections
2. **coverage.css** (`coverage-7.13.5/doc/_static/coverage.css`) — 39 inbound connections
3. **helpers.py** (`coverage-7.13.5/tests/helpers.py`) — 24 inbound connections
4. **tests.js** (`coverage-7.13.5/tests/js/tests.js`) — 13 inbound connections
5. **parser.py** (`coverage-7.13.5/lab/parser.py`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_process.py** (`coverage-7.13.5/tests/test_process.py`) — 42 outbound dependencies
2. **test_report.py** (`coverage-7.13.5/tests/test_report.py`) — 38 outbound dependencies
3. **test_html.py** (`coverage-7.13.5/tests/test_html.py`) — 35 outbound dependencies
4. **test_api.py** (`coverage-7.13.5/tests/test_api.py`) — 32 outbound dependencies
5. **test_concurrency.py** (`coverage-7.13.5/tests/test_concurrency.py`) — 31 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `measurable_line` (@ `coverage-7.13.5/tests/test_concurrency.py`) -> Impact: **401.6** | LOC: 232
- `make_tree` (@ `coverage-7.13.5/tests/test_xml.py`) -> Impact: **374.0** | LOC: 549
- `sortColumn` (@ `coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js`) -> Impact: **274.8** | LOC: 387
- `one_file` (@ `coverage-7.13.5/lab/parser.py`) -> Impact: **178.4** | LOC: 68
  * *Intent:* # `filename` can have a line number suffix. In that case, extract those # embedded in the test files. if match := re.search(r"^(.*):(\d+)-(\d+)$", fil...
- `test_for_leaks` (@ `coverage-7.13.5/tests/test_oddball.py`) -> Impact: **130.5** | LOC: 428
  * *Intent:* # Test the core of bug 93: https://github.com/coveragepy/coveragepy/issues/93 # When recovering from a stack overflow, the Python trace function is # ...
- `test_completely_zero_reporting` (@ `coverage-7.13.5/tests/test_api.py`) -> Impact: **118.3** | LOC: 287
- `should_skip` (@ `coverage-7.13.5/igor.py`) -> Impact: **116.8** | LOC: 32
- `test_title_set_in_args` (@ `coverage-7.13.5/tests/test_html.py`) -> Impact: **116.8** | LOC: 430
- `disassemble` (@ `coverage-7.13.5/lab/parser.py`) -> Impact: **105.8** | LOC: 55
- `test_accented_directory` (@ `coverage-7.13.5/tests/test_html.py`) -> Impact: **105.6** | LOC: 121

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `trace` (@ `coverage-7.13.5/lab/run_trace.py`) -> **O(2^N) [Recursive]**
- `build_extension` (@ `coverage-7.13.5/setup.py`) -> **O(2^N) [Recursive]**
- `run` (@ `coverage-7.13.5/setup.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # `import sys` is needed because .pth files are executed only if they start # with `import `. with open(PTH_NAME, "w", encoding="utf-8") as pth_file: ...
- `measurable_line` (@ `coverage-7.13.5/tests/test_concurrency.py`) -> **O(2^N) [Recursive]**
- `make_tree` (@ `coverage-7.13.5/tests/test_xml.py`) -> **O(2^N) [Recursive]**
- `hack_line_numbers` (@ `coverage-7.13.5/lab/hack_pyc.py`) -> **O(2^N) [Recursive]**
- `read` (@ `coverage-7.13.5/lab/hack_pyc.py`) -> **O(2^N) [Recursive]**
- `write` (@ `coverage-7.13.5/lab/hack_pyc.py`) -> **O(2^N) [Recursive]**
- `show_off_off` (@ `coverage-7.13.5/lab/run_sysmon.py`) -> **O(2^N) [Recursive]**
- `main` (@ `coverage-7.13.5/lab/show_pyc.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `run_tests_with_coverage` (@ `coverage-7.13.5/igor.py`) -> DB Complexity: **67**
- `test_title_set_in_args` (@ `coverage-7.13.5/tests/test_html.py`) -> DB Complexity: **43**
- `sortColumn` (@ `coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js`) -> DB Complexity: **35**
- `show_off_off` (@ `coverage-7.13.5/lab/run_sysmon.py`) -> DB Complexity: **24**
- `_same_python_executable` (@ `coverage-7.13.5/tests/test_testing.py`) -> DB Complexity: **24**
- `show_pyc_file` (@ `coverage-7.13.5/lab/show_pyc.py`) -> DB Complexity: **20**
- `test_stdlib_symlink` (@ `coverage-7.13.5/tests/test_api.py`) -> DB Complexity: **19**
  * *Intent:* # Measure without the stdlib, but include colorsys. cov1 = coverage.Coverage(cover_pylib=False, include=["*/colorsys.py"]) self.start_import_stop(cov1...
- `Anonymous_Block_[Truncated]` (@ `coverage-7.13.5/lab/compare_times.sh`) -> DB Complexity: **18**
- `make_tree` (@ `coverage-7.13.5/tests/test_xml.py`) -> DB Complexity: **16**
- `test_no_toml_installed_explicit_toml` (@ `coverage-7.13.5/tests/test_config.py`) -> DB Complexity: **15**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `coverage-7.13.5/tests` | 51 | 8436.24 | 3.24% | 0.0% |
| `coverage-7.13.5/lab` | 17 | 1380.64 | 16.83% | 17.59% |
| `coverage-7.13.5` | 10 | 1217.9 | 2.48% | 9.83% |
| `coverage-7.13.5/tests/gold/html/support` | 2 | 423.27 | 51.76% | 0.0% |
| `coverage-7.13.5/ci` | 5 | 142.26 | 5.83% | 0.0% |
| `coverage-7.13.5/tests/js` | 2 | 94.2 | 5.32% | 0.0% |
| `coverage-7.13.5/doc` | 4 | 85.5 | 2.51% | 21.26% |
| `coverage-7.13.5/requirements` | 6 | 78.8 | 5.0% | 0.0% |
| `coverage-7.13.5/tests/modules/pkg1` | 6 | 67.28 | 5.0% | 0.0% |
| `coverage-7.13.5/tests/modules/pkg1/sub` | 4 | 44.16 | 5.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `coverage-7.13.5/lab/hack_pyc.py` -> **100.0%** Exposure
- `coverage-7.13.5/lab/extract_code.py` -> **99.9905%** Exposure
- `coverage-7.13.5/lab/compare_times.sh` -> **99.1183%** Exposure
- `coverage-7.13.5/doc/cog_helpers.py` -> **85.0342%** Exposure
- `coverage-7.13.5/setup.py` -> **70.1334%** Exposure
### Highest State Flux (Mutation/Volatility)
- `coverage-7.13.5/lab/hack_pyc.py` -> **99.999%** Exposure
- `coverage-7.13.5/lab/warn_executed.py` -> **97.3184%** Exposure
- `coverage-7.13.5/lab/pick.py` -> **95.9865%** Exposure
- `coverage-7.13.5/lab/run_trace.py` -> **89.7011%** Exposure
- `coverage-7.13.5/lab/parser.py` -> **48.556%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `coverage-7.13.5/tests/test_data.py` -> **78** Orphaned Functions | **2** Duplicates
- `coverage-7.13.5/tests/gold/html/styled/style.css` -> **0** Orphaned Functions | **65** Duplicates
- `coverage-7.13.5/tests/gold/html/support/style_cb_a5a05ca4.css` -> **0** Orphaned Functions | **65** Duplicates
- `coverage-7.13.5/tests/test_api.py` -> **55** Orphaned Functions | **4** Duplicates
- `coverage-7.13.5/tests/test_cmdline.py` -> **51** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`coverage-7.13.5/igor.py`** -> AI Confidence: **99.31%**
2. **`coverage-7.13.5/lab/parser.py`** -> AI Confidence: **99.31%**
3. **`coverage-7.13.5/lab/show_pyc.py`** -> AI Confidence: **99.31%**
4. **`coverage-7.13.5/lab/warn_executed.py`** -> AI Confidence: **99.31%**
5. **`coverage-7.13.5/tests/test_json.py`** -> AI Confidence: **99.31%**
6. **`coverage-7.13.5/tests/gold/html/Makefile`** -> AI Confidence: **99.29%**
7. **`coverage-7.13.5/lab/branches.py`** -> AI Confidence: **99.29%**
8. **`coverage-7.13.5/lab/treetopy.sh`** -> AI Confidence: **99.29%**
9. **`coverage-7.13.5/tests/test_sqlitedb.py`** -> AI Confidence: **99.24%**
10. **`coverage-7.13.5/tests/test_testing.py`** -> AI Confidence: **99.24%**
11. **`coverage-7.13.5/setup.py`** -> AI Confidence: **99.18%**
12. **`coverage-7.13.5/tests/test_api.py`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `coverage-7.13.5/tests/js/tests.js` -> **2.0428%** Exposure
- `coverage-7.13.5/tests/test_mixins.py` -> **0.0014%** Exposure
### Exploit Generation Surface
- `coverage-7.13.5/ci/update_rtfd.py` -> **100.0%** Exposure
- `coverage-7.13.5/igor.py` -> **100.0%** Exposure
- `coverage-7.13.5/lab/parser.py` -> **100.0%** Exposure
- `coverage-7.13.5/lab/run_sysmon.py` -> **100.0%** Exposure
- `coverage-7.13.5/lab/run_trace.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `coverage-7.13.5/Makefile` -> **100.0%** Exposure
- `coverage-7.13.5/lab/run_sysmon.py` -> **100.0%** Exposure
- `coverage-7.13.5/lab/run_trace.py` -> **100.0%** Exposure
- `coverage-7.13.5/lab/show_pyc.py` -> **100.0%** Exposure
- `coverage-7.13.5/setup.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `coverage-7.13.5/ci/session.py` -> **100.0%** Exposure
- `coverage-7.13.5/igor.py` -> **100.0%** Exposure
- `coverage-7.13.5/lab/goals.py` -> **100.0%** Exposure
- `coverage-7.13.5/lab/hack_pyc.py` -> **100.0%** Exposure
- `coverage-7.13.5/lab/parser.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1006` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `coverage-7.13.5/lab/run_trace.py` (PYTHON) -> Cumulative Risk: **818.57**
- **Archetype:** `file_cluster_8` (Distance: 9.385 IQR)
- **Magnitude:** 56.14 | **LOC:** 45 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `trace` (Impact: 51.6)

### 2. `coverage-7.13.5/setup.py` (PYTHON) -> Cumulative Risk: **766.37**
- **Archetype:** `file_cluster_13` (Distance: 10.098 IQR)
- **Magnitude:** 143.28 | **LOC:** 273 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `build_extension` (Impact: 44.3), `run` (Impact: 26.2), `run` (Impact: 14.2)

### 3. `coverage-7.13.5/lab/hack_pyc.py` (PYTHON) -> Cumulative Risk: **730.01**
- **Archetype:** `file_cluster_13` (Distance: 11.429 IQR)
- **Magnitude:** 130.08 | **LOC:** 99 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.999%)
- **Heaviest Functions:** `hack_line_numbers` (Impact: 65.1), `read` (Impact: 14.2), `write` (Impact: 14.2)

### 4. `coverage-7.13.5/lab/warn_executed.py` (PYTHON) -> Cumulative Risk: **690.15**
- **Archetype:** `file_cluster_13` (Distance: 10.991 IQR)
- **Magnitude:** 85.08 | **LOC:** 214 | **CtrlFlow:** 51.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9967%), State Flux (97.3184%)
- **Heaviest Functions:** `analyze_warnings` (Impact: 32.2), `main` (Impact: 14.5), `read_warn_patterns` (Impact: 12.8)

### 5. `coverage-7.13.5/lab/show_pyc.py` (PYTHON) -> Cumulative Risk: **672.25**
- **Archetype:** `file_cluster_8` (Distance: 8.766 IQR)
- **Magnitude:** 215.76 | **LOC:** 218 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `show_pyc_file` (Impact: 100.2), `main` (Impact: 35.3), `lnotab_interpreted` (Impact: 26.9)

### 6. `coverage-7.13.5/lab/run_sysmon.py` (PYTHON) -> Cumulative Risk: **618.17**
- **Archetype:** `file_cluster_8` (Distance: 8.132 IQR)
- **Magnitude:** 54.2 | **LOC:** 120 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `show_off_off` (Impact: 20.4), `bytes_to_lines` (Impact: 10.8), `show_off` (Impact: 9.4)

### 7. `coverage-7.13.5/igor.py` (PYTHON) -> Cumulative Risk: **615.33**
- **Archetype:** `file_cluster_13` (Distance: 10.825 IQR)
- **Magnitude:** 410.24 | **LOC:** 555 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (92.3966%)
- **Heaviest Functions:** `should_skip` (Impact: 116.8), `run_tests_with_coverage` (Impact: 83.2), `do_release_version` (Impact: 51.4)

### 8. `coverage-7.13.5/lab/parser.py` (PYTHON) -> Cumulative Risk: **605.74**
- **Archetype:** `file_cluster_13` (Distance: 10.1 IQR)
- **Magnitude:** 471.04 | **LOC:** 221 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (97.1199%)
- **Heaviest Functions:** `one_file` (Impact: 178.4), `disassemble` (Impact: 105.8), `arc_ascii_art` (Impact: 98.7)

### 9. `coverage-7.13.5/tests/helpers.py` (PYTHON) -> Cumulative Risk: **544.61**
- **Archetype:** `file_cluster_13` (Distance: 12.184 IQR)
- **Magnitude:** 116.06 | **LOC:** 417 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `__getattr__` (Impact: 14.2), `subprocess_popen` (Impact: 13.2), `_correct_encoding` (Impact: 11.0)

### 10. `coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js` (JAVASCRIPT) -> Cumulative Risk: **543.02**
- **Archetype:** `file_cluster_17` (Distance: 12.006 IQR)
- **Magnitude:** 416.58 | **LOC:** 736 | **CtrlFlow:** 57.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Concurrency (96.8772%)
- **Heaviest Functions:** `sortColumn` (Impact: 274.8), `getCellValue` (Impact: 21.4), `rowComparator` (Impact: 9.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `coverage-7.13.5/tests/test_data.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.743 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.8 IQR)
- **Top Global Matches:** file_cluster_16: 11.743, file_cluster_8: 11.799, file_cluster_13: 11.858
- **Magnitude:** 705.28 | **LOC:** 1130 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (5.0961%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `make_data_files` (Impact: 42.8 | O(N^5) | DB: 1)
  * `test_update_conflicting_file_tracers` (Impact: 25.0 | O(N^3) | DB: 2)
  * `test_update_file_tracer_vs_no_file_trace` (Impact: 25.0 | O(N^3) | DB: 2)
  * `test_update_cant_mix_lines_and_arcs` (Impact: 24.9 | O(N^3) | DB: 2)
  * `test_thread_stress` (Impact: 22.7 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 201`, `args: 88`, `func_start: 88`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 48`, `planned_debt: 1`, `fragile_debt: 6`, `duplicate_logic: 2`, `orphaned_logic: 78`
* *Architecture:* `io: 8`, `api: 93`, `concurrency: 7`, `import: 20`
* *Defense:* `safety: 67`, `doc: 28`, `test: 182`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` typing, os, gc, collections.abc, coverage.data, threading, glob, os.path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_api.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.01 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.776 IQR)
- **Top Global Matches:** file_cluster_16: 12.01, file_cluster_8: 12.066, file_cluster_13: 12.124
- **Magnitude:** 681.94 | **LOC:** 1661 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (2.066%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_completely_zero_reporting` (Impact: 118.3 | O(N^5) | DB: 6)
  * `clean_files` (Impact: 30.6 | O(N^5) | DB: 1)
  * `test_moving_stuff` (Impact: 22.6 | O(N^4) | DB: 4)
  * `test_switch_context_unstarted` (Impact: 21.4 | O(N^3))
    * *Intent:* # measuring labeled coverage via public API, # with static label prefix. self.make_test_files() # Te...
  * `test_config_crash` (Impact: 21.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 292`, `args: 99`, `func_start: 99`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 14`, `duplicate_logic: 4`, `orphaned_logic: 55`
* *Architecture:* `io: 44`, `api: 113`, `concurrency: 1`, `import: 31`
* *Defense:* `safety: 114`, `doc: 140`, `test: 222`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` sys, typing, os, usepkgs, io, collections.abc, textwrap, coverage.data...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_concurrency.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.162 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.307 IQR)
- **Top Global Matches:** file_cluster_13: 12.162, file_cluster_16: 12.313, file_cluster_0: 12.377
- **Magnitude:** 648.66 | **LOC:** 865 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (10.8465%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `measurable_line` (Impact: 401.6 | O(2^N) | DB: 1)
  * `test_thread_safe_save_data` (Impact: 86.9 | O(N^5) | DB: 13)
  * `test_coverage_stop_in_threads` (Impact: 23.1 | O(N^4) | DB: 8)
  * `test_missing_module` (Impact: 14.2 | O(N^3) | DB: 3)
  * `start_method_fixture` (Impact: 6.4 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 122`, `args: 38`, `func_start: 37`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 12`, `orphaned_logic: 8`
* *Architecture:* `io: 8`, `api: 42`, `concurrency: 37`, `import: 25`
* *Defense:* `safety: 42`, `doc: 80`, `test: 88`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` sys, os, gevent, collections.abc, coverage.data, threading, glob, os.path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_html.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.483 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.592 IQR)
- **Top Global Matches:** file_cluster_16: 11.483, file_cluster_13: 11.531, file_cluster_8: 11.546
- **Magnitude:** 570.4 | **LOC:** 1573 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (2.6289%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_title_set_in_args` (Impact: 116.8 | O(N^4) | DB: 43)
  * `test_accented_directory` (Impact: 105.6 | O(N^4) | DB: 3)
  * `handle_starttag` (Impact: 18.5 | O(N^3) | DB: 2)
  * `assert_htmlcov_files_exist` (Impact: 18.3 | O(N^3) | DB: 7)
  * `open` (Impact: 18.2 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 284`, `args: 83`, `func_start: 83`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 4`, `state_mutation: 23`, `dead_code: 2`, `fragile_debt: 2`, `duplicate_logic: 4`, `orphaned_logic: 23`
* *Architecture:* `io: 34`, `api: 91`, `import: 30`
* *Defense:* `safety: 64`, `doc: 136`, `test: 139`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` helper2, sys, typing, json, not_covered, os, sub.another, collections...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/a1_coverage.pth` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/lab/parser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.1 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.87 IQR)
- **Top Global Matches:** file_cluster_13: 10.1, file_cluster_8: 10.231, file_cluster_7: 10.448
- **Magnitude:** 471.04 | **LOC:** 221 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (16.0075%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `one_file` (Impact: 178.4 | O(N^6) | DB: 1)
    * *Intent:* # `filename` can have a line number suffix. In that case, extract those # embedded in the test files...
  * `disassemble` (Impact: 105.8 | O(N^6) | DB: 3)
  * `arc_ascii_art` (Impact: 98.7 | O(N^6))
    * *Intent:* """ plus_ones = set() arc_chars = collections.defaultdict(str) for lfrom, lto in sorted(arcs): if lf...
  * `main` (Impact: 56.0 | O(N^6) | DB: 3)
  * `all_code_objects` (Impact: 10.9 | O(N^2) | DB: 2)
    * *Intent:* """Iterate over all the code objects in `code`."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 30`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 9`
* *Architecture:* `io: 2`, `api: 9`, `import: 11`
* *Defense:* `safety: 3`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.206
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.018605
  * `Imports (Out-Degree: 0):` sys, coverage.python, os, re, collections, dis, coverage.parser, textwrap...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `coverage-7.13.5/tests/test_testing.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.005 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.445 IQR)
- **Top Global Matches:** file_cluster_16: 11.005, file_cluster_8: 11.034, file_cluster_13: 11.101
- **Magnitude:** 434.42 | **LOC:** 494 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (2.7429%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_assert_warnings` (Impact: 80.3 | O(N^4))
  * `test_file_count` (Impact: 32.7 | O(N^3))
  * `test_assert_no_warnings` (Impact: 22.3 | O(N^4))
  * `test_failing_proxy` (Impact: 18.5 | O(N^3))
  * `test_assert_recent_datetime` (Impact: 18.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 99`, `args: 34`, `func_start: 34`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`, `planned_debt: 7`, `orphaned_logic: 29`
* *Architecture:* `io: 11`, `api: 40`, `import: 13`
* *Defense:* `safety: 22`, `doc: 30`, `test: 93`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` datetime, sys, coverage.types, tests.coveragetest, coverage, os, re, warnings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_xml.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.876 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.052 IQR)
- **Top Global Matches:** file_cluster_8: 10.876, file_cluster_16: 10.877, file_cluster_13: 10.904
- **Magnitude:** 432.74 | **LOC:** 616 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (1.6464%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `make_tree` (Impact: 374.0 | O(2^N) | DB: 16)
  * `run_doit` (Impact: 3.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 157`, `args: 39`, `func_start: 39`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 3`, `fragile_debt: 1`
* *Architecture:* `io: 6`, `api: 44`, `import: 21`
* *Defense:* `safety: 37`, `doc: 50`, `test: 72`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` typing, os, x01y, d0.d0, collections.abc, os.path, tests.coveragetest, coverage...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_config.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.498 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.625 IQR)
- **Top Global Matches:** file_cluster_16: 12.498, file_cluster_8: 12.52, file_cluster_0: 12.614
- **Magnitude:** 427.62 | **LOC:** 1142 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (2.123%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_no_toml_installed_explicit_toml` (Impact: 80.9 | O(N^4) | DB: 15)
  * `assert_config_settings_are_correct` (Impact: 35.3 | O(2^N))
  * `test_tweak_error_checking` (Impact: 31.7 | O(N^3))
  * `test_tweak_plugin_options` (Impact: 18.0 | O(N^3))
  * `test_no_toml_installed_no_toml` (Impact: 17.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 221`, `args: 63`, `func_start: 63`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1`, `orphaned_logic: 36`
* *Architecture:* `io: 8`, `api: 66`, `concurrency: 2`, `import: 15`
* *Defense:* `safety: 128`, `doc: 112`, `test: 235`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` coverage.config, pathlib, coverage.types, tests.coveragetest, coverage, os, coverage.exceptions, coverage.tomlconfig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_cmdline.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.413 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.301 IQR)
- **Top Global Matches:** file_cluster_8: 11.413, file_cluster_16: 11.44, file_cluster_13: 11.612
- **Magnitude:** 419.8 | **LOC:** 1664 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (1.7816%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `command_line` (Impact: 37.2 | O(N^5) | DB: 6)
  * `test_version` (Impact: 14.3 | O(N^3))
    * *Intent:* """, ) self.cmd_executes( "run --concurrency=gevent foo.py", """\ cov = Coverage(concurrency=['geven...
  * `test_internalraise` (Impact: 10.5 | O(N^3))
  * `test_fail_under_with_precision` (Impact: 10.0 | O(N^3))
  * `assert_same_mock_calls` (Impact: 8.5 | O(N^3))
    * *Intent:* """Assert that `m1.mock_calls` and `m2.mock_calls` are the same."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 197`, `args: 73`, `func_start: 71`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 6`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 4`, `orphaned_logic: 51`
* *Architecture:* `io: 5`, `api: 79`, `concurrency: 3`, `import: 23`
* *Defense:* `safety: 73`, `doc: 238`, `test: 142`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` sys, typing, coverage.config, coverage.cmdline, os, collections.abc, textwrap, coverage.types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.006 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.439 IQR)
- **Top Global Matches:** file_cluster_17: 12.006, file_cluster_8: 12.126, file_cluster_2: 12.32
- **Magnitude:** 416.58 | **LOC:** 736 | **CtrlFlow:** 57.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (84.3714%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sortColumn` (Impact: 274.8 | O(N^4) | DB: 35)
  * `getCellValue` (Impact: 21.4 | O(N^3) | DB: 1)
    * *Intent:* // Helpers for table sorting
  * `rowComparator` (Impact: 9.4 | O(N^2) | DB: 2)
  * `on_click` (Impact: 5.5 | O(N^2))
  * `debounce` (Impact: 3.9 | O(N^3) | DB: 1)
    * *Intent:* // General helpers
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 49`, `args: 38`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 83`
* *Architecture:* `io: 2`, `api: 2`, `concurrency: 6`
* *Defense:* `safety: 23`, `immutability_locks: 27`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 127.04
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.209302
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 45):` (Excluded from Brief to save tokens)

### `coverage-7.13.5/igor.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.825 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.185 IQR)
- **Top Global Matches:** file_cluster_13: 10.825, file_cluster_8: 10.992, file_cluster_7: 11.189
- **Magnitude:** 410.24 | **LOC:** 555 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 67
- **Risk Profile:** Cognitive Load (10.275%), Tech Debt (28.1406%)
**Top Internal Functions/Classes:**
  * `should_skip` (Impact: 116.8 | O(N^6) | DB: 12)
  * `run_tests_with_coverage` (Impact: 83.2 | O(N^5) | DB: 67)
  * `do_release_version` (Impact: 51.4 | O(N^3) | DB: 7)
  * `print_banner` (Impact: 42.5 | O(N^3) | DB: 9)
  * `label_for_core` (Impact: 21.3 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 78`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 18`, `orphaned_logic: 5`
* *Architecture:* `io: 49`, `api: 24`, `import: 23`
* *Defense:* `safety: 10`, `doc: 56`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sys, os, of, textwrap, glob, os.path, coverage, sysconfig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_parser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.628 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.78 IQR)
- **Top Global Matches:** file_cluster_16: 12.628, file_cluster_8: 12.647, file_cluster_7: 12.886
- **Magnitude:** 297.64 | **LOC:** 1323 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (1.435%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_os_error` (Impact: 22.0 | O(N^4))
    * *Intent:* # coding: utf-8 a = 1; b = 2 if len([]): a = 5 # ✘cover """, exclude="✘cover", ) assert parser.state...
  * `test_fuzzed_double_parse` (Impact: 17.9 | O(N^3))
    * *Intent:* # on 3.10 this passes ast.parse but fails on tokenize.generate_tokens pytest.param( "\r'\\\n'''", id...
  * `test_not_python` (Impact: 10.6 | O(N^3))
  * `test_multiline_exclusion_block` (Impact: 8.4 | O(N^3))
  * `test_multiline_exclusion_match_all` (Impact: 7.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 214`, `args: 60`, `func_start: 60`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `fragile_debt: 1`, `orphaned_logic: 55`
* *Architecture:* `io: 1`, `api: 66`, `import: 11`
* *Defense:* `safety: 124`, `doc: 182`, `test: 194`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` abc, tests.coveragetest, coverage, re, ast, __future__, pytest, coverage.parser...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_coverage.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.277 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.039 IQR)
- **Top Global Matches:** file_cluster_8: 10.277, file_cluster_16: 10.388, file_cluster_7: 10.509
- **Magnitude:** 245.94 | **LOC:** 1860 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (1.3551%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_attribute_annotation` (Impact: 10.7 | O(N^3))
  * `test_no_data_to_report_on_annotate` (Impact: 10.7 | O(N^3))
  * `test_no_data_to_report_on_html` (Impact: 10.7 | O(N^3))
  * `test_failed_coverage` (Impact: 10.6 | O(N^3))
  * `test_exceptions_really_fail` (Impact: 10.6 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 92`, `args: 71`, `func_start: 71`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `orphaned_logic: 38`
* *Architecture:* `api: 81`, `import: 6`
* *Defense:* `safety: 1`, `doc: 284`, `test: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sys, tests.coveragetest, coverage, __future__, pytest, string, coverage.exceptions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_arcs.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.754 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.283 IQR)
- **Top Global Matches:** file_cluster_16: 10.754, file_cluster_8: 10.775, file_cluster_7: 11.045
- **Magnitude:** 243.12 | **LOC:** 2425 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (1.2907%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_zero_coverage_while_loop` (Impact: 3.7 | O(N^3))
  * `test_simple_sequence` (Impact: 2.7 | O(N^2))
  * `test_function_def` (Impact: 2.7 | O(N^2))
  * `test_if` (Impact: 2.7 | O(N^2))
  * `test_if_else` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 176`, `args: 112`, `func_start: 112`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `fragile_debt: 1`, `orphaned_logic: 36`
* *Architecture:* `io: 1`, `api: 127`, `import: 11`
* *Defense:* `safety: 31`, `doc: 316`, `test: 149`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` asyncio, typing, tests.coveragetest, coverage, contextlib, itertools, coverage.files, __future__...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_process.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.37 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.696 IQR)
- **Top Global Matches:** file_cluster_16: 12.37, file_cluster_8: 12.377, file_cluster_0: 12.38
- **Magnitude:** 240.06 | **LOC:** 1772 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (1.7585%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fullname` (Impact: 20.4 | O(N^4))
  * `path` (Impact: 8.2 | O(2^N) | DB: 3)
  * `test_report_99p9_is_not_ok` (Impact: 7.5 | O(N^3))
  * `test_subprocess_with_pth_files` (Impact: 4.0 | O(N^3) | DB: 3)
  * `make_b_or_c_py` (Impact: 3.9 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 290`, `args: 78`, `func_start: 78`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 24`
* *Architecture:* `io: 35`, `api: 90`, `import: 26`
* *Defense:* `safety: 149`, `doc: 170`, `test: 250`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` sys, typing, coverage.cmdline, os, textwrap, coverage.data, threading, glob...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_debug.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.229 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.459 IQR)
- **Top Global Matches:** file_cluster_16: 12.229, file_cluster_13: 12.272, file_cluster_8: 12.383
- **Magnitude:** 235.98 | **LOC:** 512 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (2.2155%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_short_stack_full` (Impact: 18.2 | O(N^3) | DB: 9)
  * `test_info_formatter_with_generator` (Impact: 16.4 | O(N^3))
  * `test_debug_sys_ctracer` (Impact: 10.7 | O(N^3))
  * `test_short_stack_frame_ids` (Impact: 8.2 | O(N^2) | DB: 1)
  * `test_auto_repr` (Impact: 7.6 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 164`, `args: 48`, `func_start: 45`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 7`, `fragile_debt: 2`, `orphaned_logic: 24`
* *Architecture:* `io: 10`, `api: 50`, `import: 16`
* *Defense:* `safety: 76`, `doc: 36`, `test: 116`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` tests, sys, typing, tests.coveragetest, coverage, os, re, ast...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_files.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.619 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.279 IQR)
- **Top Global Matches:** file_cluster_8: 9.619, file_cluster_16: 9.797, file_cluster_0: 10.052
- **Magnitude:** 227.06 | **LOC:** 805 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (1.9633%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_glob_matcher_overload` (Impact: 78.0 | O(N^4) | DB: 12)
  * `test_relative_dir_for_root` (Impact: 24.3 | O(N^5) | DB: 3)
  * `test_invalid_globs` (Impact: 8.0 | O(N^2))
  * `assertMatches` (Impact: 7.0 | O(N^2))
  * `test_module_matcher` (Impact: 6.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 105`, `args: 48`, `func_start: 46`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `orphaned_logic: 13`
* *Architecture:* `io: 16`, `api: 52`, `import: 14`
* *Defense:* `safety: 25`, `doc: 26`, `test: 94`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` os.path, typing, tests.coveragetest, coverage, os, re, itertools, coverage.files...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_plugins.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.727 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.281 IQR)
- **Top Global Matches:** file_cluster_8: 11.727, file_cluster_16: 11.736, file_cluster_13: 11.848
- **Magnitude:** 224.76 | **LOC:** 1334 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (2.0016%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_exception_if_plugins_on_pytracer` (Impact: 18.2 | O(N^3))
  * `lines` (Impact: 11.6 | O(2^N))
  * `get_plugin_options` (Impact: 10.8 | O(N^3) | DB: 1)
  * `test_missing_plugin_raises_import_error` (Impact: 10.7 | O(N^3))
    * *Intent:* """, ) msg_pat = "Plugin module 'no_plugin' didn't define a coverage_init function" with pytest.rais...
  * `test_cant_import` (Impact: 10.5 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 183`, `args: 55`, `func_start: 55`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 6`, `planned_debt: 4`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 19`
* *Architecture:* `io: 5`, `api: 64`, `import: 20`
* *Defense:* `safety: 76`, `doc: 120`, `test: 122`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` typing, sys, os, io, collections.abc, coverage.data, os.path, other...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_templite.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.621 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.415 IQR)
- **Top Global Matches:** file_cluster_8: 9.621, file_cluster_16: 9.638, file_cluster_13: 10.01
- **Magnitude:** 218.18 | **LOC:** 388 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.2305%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_bad_names` (Impact: 92.1 | O(N^3))
  * `test_passthrough` (Impact: 17.6 | O(N^4))
    * *Intent:* """ pat = "^" + re.escape(msg) + "$" return pytest.raises(TempliteSyntaxError, match=pat) # type: ig...
  * `test_exception_during_evaluation` (Impact: 13.4 | O(N^4))
    * *Intent:* # TypeError: Couldn't evaluate {{ foo.bar.baz }}: regex = "^Couldn't evaluate None.bar$" with pytest...
  * `test_malformed_end` (Impact: 10.6 | O(N^3))
  * `test_if` (Impact: 8.3 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 59`, `args: 37`, `func_start: 34`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `orphaned_logic: 10`
* *Architecture:* `api: 37`, `import: 7`
* *Defense:* `safety: 6`, `doc: 18`, `test: 39`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typing, coverage.templite, tests.coveragetest, re, __future__, pytest, types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_report.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.348 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.538 IQR)
- **Top Global Matches:** file_cluster_8: 12.348, file_cluster_16: 12.415, file_cluster_13: 12.496
- **Magnitude:** 216.84 | **LOC:** 1298 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (1.4855%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_sort_report_by_invalid_option` (Impact: 10.6 | O(N^3))
  * `test_report_with_invalid_format` (Impact: 10.6 | O(N^3))
    * *Intent:* """\ class Mine: @property def thing(self) -> int: return 17 print(Mine().thing) """, )
  * `test_empty_files` (Impact: 7.6 | O(N^3))
  * `test_report_including` (Impact: 5.6 | O(N^3))
  * `test_tracing_pyc_file` (Impact: 4.7 | O(N^2) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 265`, `args: 63`, `func_start: 63`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`, `fragile_debt: 3`, `orphaned_logic: 30`
* *Architecture:* `io: 4`, `api: 66`, `import: 28`
* *Defense:* `safety: 154`, `doc: 108`, `test: 229`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` covered, nested.submodule.mycode, the, not_covered, os, a, file1, file10...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/lab/show_pyc.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.766 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.298 IQR)
- **Top Global Matches:** file_cluster_8: 8.766, file_cluster_13: 9.012, file_cluster_7: 9.298
- **Magnitude:** 215.76 | **LOC:** 218 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (11.3269%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `show_pyc_file` (Impact: 100.2 | O(N^5) | DB: 20)
  * `main` (Impact: 35.3 | O(2^N) | DB: 3)
  * `lnotab_interpreted` (Impact: 26.9 | O(N^4))
  * `show_hex` (Impact: 16.4 | O(N^3))
  * `flag_words` (Impact: 10.7 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 19`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 3`
* *Architecture:* `io: 7`, `api: 9`, `import: 8`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, struct, binascii, warnings, dis, time, types, marshal
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_sqlitedb.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.162 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.788 IQR)
- **Top Global Matches:** file_cluster_13: 10.162, file_cluster_8: 10.214, file_cluster_16: 10.23
- **Magnitude:** 204.02 | **LOC:** 98 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.3128%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_retry_execute_failure` (Impact: 36.8 | O(N^6))
  * `test_retry_executemany_void_failure` (Impact: 30.8 | O(N^6))
  * `test_execute_void_can_refuse_failure` (Impact: 26.4 | O(N^5))
  * `test_error_reporting` (Impact: 26.3 | O(N^5))
  * `test_retry_executemany_void` (Impact: 21.3 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 42`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `orphaned_logic: 8`
* *Architecture:* `api: 9`, `import: 7`
* *Defense:* `safety: 2`, `doc: 6`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` tests.coveragetest, __future__, pytest, coverage.sqlitedb, unittest, coverage.exceptions, tests.helpers
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_oddball.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.512 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.35 IQR)
- **Top Global Matches:** file_cluster_13: 11.512, file_cluster_0: 11.696, file_cluster_16: 11.764
- **Magnitude:** 197.5 | **LOC:** 790 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (2.5011%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_for_leaks` (Impact: 130.5 | O(N^5) | DB: 9)
    * *Intent:* # Test the core of bug 93: https://github.com/coveragepy/coveragepy/issues/93 # When recovering from...
  * `test_long_recursion` (Impact: 13.2 | O(N^4))
  * `test_long_recursion_recovery` (Impact: 4.0 | O(N^3))
  * `test_threading` (Impact: 2.7 | O(N^2))
  * `test_thread_run` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 87`, `args: 18`, `func_start: 18`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 7`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 5`, `orphaned_logic: 6`
* *Architecture:* `io: 3`, `api: 28`, `import: 16`
* *Defense:* `safety: 34`, `doc: 82`, `test: 63`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` xml.dom.minidom, sys, coverage.data, threading, os.path, bug416a, tests.coveragetest, coverage...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `coverage-7.13.5/tests/test_context.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.509 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.625 IQR)
- **Top Global Matches:** file_cluster_16: 11.509, file_cluster_13: 11.515, file_cluster_8: 11.856
- **Magnitude:** 176.04 | **LOC:** 312 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (3.4361%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_combining_arc_contexts` (Impact: 28.1 | O(N^4) | DB: 4)
  * `test_combining_line_contexts` (Impact: 18.5 | O(N^4) | DB: 4)
  * `get_qualname` (Impact: 16.1 | O(2^N))
  * `test_dynamic_alone` (Impact: 8.0 | O(N^3) | DB: 3)
  * `test_static_and_dynamic` (Impact: 8.0 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 87`, `args: 29`, `func_start: 29`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 6`, `orphaned_logic: 16`
* *Architecture:* `io: 5`, `api: 37`, `import: 13`
* *Defense:* `safety: 16`, `doc: 16`, `test: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` os.path, tests, typing, coverage.types, tests.coveragetest, coverage, coverage.context, __future__...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `coverage-7.13.5/tests/modules/pkg1/__init__.py` (PYTHON) | **Drift Ratio: 1.59x**
  * **Global Archetype:** `file_cluster_8` (Drift: 5.875 IQR)
  * **Local Reality:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 9.33 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `coverage-7.13.5/tests/gold/html/styled/index.html` (HTML) | Magnitude: 0.03 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 104, decorators: 38, args: 29, structural_boundaries: 28
- `coverage-7.13.5/tests/gold/html/b_branch/index.html` (HTML) | Magnitude: 0.04 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 129, decorators: 52, args: 43, structural_boundaries: 32
- `coverage-7.13.5/tests/gold/html/multiline/index.html` (HTML) | Magnitude: 0.04 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 129, decorators: 52, args: 43, structural_boundaries: 32
- `coverage-7.13.5/tests/gold/html/partial/index.html` (HTML) | Magnitude: 0.04 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 129, decorators: 52, args: 43, structural_boundaries: 32
- `coverage-7.13.5/tests/gold/html/b_branch/function_index.html` (HTML) | Magnitude: 0.04 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 179, decorators: 76, args: 68, structural_boundaries: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `coverage-7.13.5/tests/test_numbits.py` (PYTHON) | Magnitude: 81.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 133, structural_boundaries: 47, test: 22, generics: 18
- `coverage-7.13.5/tests/plugin1.py` (PYTHON) | Magnitude: 34.78 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 29, indent_spaces: 22, doc: 16, api: 9
- `coverage-7.13.5/tests/osinfo.py` (PYTHON) | Magnitude: 42.68 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 21, doc: 12, branch: 7
- `coverage-7.13.5/lab/pick.py` (PYTHON) | Magnitude: 18.44 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, branch: 7, structural_boundaries: 4, state_mutation: 3
- `coverage-7.13.5/tests/test_sqlitedb.py` (PYTHON) | Magnitude: 204.02 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 42, branch: 28, test: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `coverage-7.13.5/tests/test_phystokens.py` (PYTHON) | Magnitude: 57.76 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 155, structural_boundaries: 75, test: 51, safety: 28
- `coverage-7.13.5/tests/test_context.py` (PYTHON) | Magnitude: 176.04 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 156, structural_boundaries: 87, test: 38, api: 37
- `coverage-7.13.5/tests/test_process.py` (PYTHON) | Magnitude: 240.06 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 859, structural_boundaries: 290, test: 250, doc: 170
- `coverage-7.13.5/tests/test_parser.py` (PYTHON) | Magnitude: 297.64 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 481, structural_boundaries: 214, test: 194, doc: 182
- `coverage-7.13.5/tests/test_arcs.py` (PYTHON) | Magnitude: 243.12 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 731, doc: 316, structural_boundaries: 176, test: 149

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js` (JAVASCRIPT) | Magnitude: 416.58 | Delta: **0.12 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 284, state_mutation: 83, branch: 67, structural_boundaries: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `coverage-7.13.5/tests/test_xml.py` (PYTHON) | Magnitude: 432.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 404, structural_boundaries: 157, test: 72, doc: 50
- `coverage-7.13.5/tests/gold/html/a/index.html` (HTML) | Magnitude: 0.03 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 103, decorators: 38, args: 29, structural_boundaries: 28
- `coverage-7.13.5/tests/gold/html/bom/index.html` (HTML) | Magnitude: 0.03 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 103, decorators: 38, args: 29, structural_boundaries: 28
- `coverage-7.13.5/tests/gold/html/contexts/index.html` (HTML) | Magnitude: 0.03 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 103, decorators: 38, args: 29, structural_boundaries: 28
- `coverage-7.13.5/tests/gold/html/isolatin1/index.html` (HTML) | Magnitude: 0.03 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 103, decorators: 38, args: 29, structural_boundaries: 28

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `coverage-7.13.5/tests/helpers.py` -> **Severity: 8.341** (Embedded: 0.1118 * Error Risk: 74.6009%)
- `coverage-7.13.5/tests/gold/html/support/coverage_html_cb_bcae5fc4.js` -> **Severity: 2.185** (Embedded: 0.2093 * Error Risk: 10.4396%)
- `coverage-7.13.5/ci/session.py` -> **Severity: 0.884** (Embedded: 0.014 * Error Risk: 63.3333%)
- `coverage-7.13.5/tests/modules/plugins/another.py` -> **Severity: 0.744** (Embedded: 0.0093 * Error Risk: 80.0%)
- `coverage-7.13.5/tests/mixins.py` -> **Severity: 0.303** (Embedded: 0.0047 * Error Risk: 65.2113%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `coverage-7.13.5/ci/session.py` -> **Severity: 1148.999** (Blast Radius: 11.49 * Doc Risk: 99.9999%)
- `coverage-7.13.5/lab/parser.py` -> **Severity: 991.206** (Blast Radius: 10.206 * Doc Risk: 97.1199%)
- `coverage-7.13.5/setup.py` -> **Severity: 362.744** (Blast Radius: 4.612 * Doc Risk: 78.6523%)
- `coverage-7.13.5/lab/platform_info.py` -> **Severity: 323.7** (Blast Radius: 3.237 * Doc Risk: 100.0%)
- `coverage-7.13.5/lab/hack_pyc.py` -> **Severity: 323.69** (Blast Radius: 3.237 * Doc Risk: 99.9968%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
