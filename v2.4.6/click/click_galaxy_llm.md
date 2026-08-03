# ARCHITECTURAL_BRIEF: click
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/click` |
| **Timestamp** | `2026-08-03T21:19:57.612365+00:00` |
| **Scan Duration** | `0.52s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 47 malicious artifacts.

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
| Total Artifacts | 55 |
| Analyzed Artifacts (Scanned) | 49 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6 |
| Total LOC | 13657 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 89.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2828 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2134 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 26.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3204 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 47 | 13657 | 95.9% |
| PLAINTEXT | 1 | 0 | 2.0% |
| MARKDOWN | 1 | 0 | 2.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.787`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 21 | 42.9% |
| file_cluster_0 | 14 | 28.6% |
| file_cluster_16 | 6 | 12.2% |
| file_cluster_8 | 6 | 12.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 4.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6*

**Composition by Extension & Reason:**
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 69.0 | 11.5 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 22.2 | 1.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 21.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 20.6 | 0.0 | 0.0 |
| API Exposure | 0.3 | 13.2 | 6.6 | 6.0 | 5.0 |
| Concurrency Exposure | 0.0 | 99.4 | 5.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 23.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 7.6 | 0.7 | 0.0 | 0.0 |
| Specification Exposure | 40.0 | 100.0 | 90.9 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 28.9 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 66.3 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 59.8 | 100.0 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 4.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `click-8.3.2/src/click/_compat.py` (Hits: 43)
- `click-8.3.2/src/click/_termui_impl.py` (Hits: 39)
- `click-8.3.2/src/click/utils.py` (Hits: 34)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **_compat.py** (`click-8.3.2/src/click/_compat.py`) — 12 inbound connections
2. **core.py** (`click-8.3.2/src/click/core.py`) — 10 inbound connections
3. **types.py** (`click-8.3.2/src/click/types.py`) — 10 inbound connections
4. **exceptions.py** (`click-8.3.2/src/click/exceptions.py`) — 9 inbound connections
5. **utils.py** (`click-8.3.2/src/click/utils.py`) — 9 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **core.py** (`click-8.3.2/src/click/core.py`) — 26 outbound dependencies
2. **_termui_impl.py** (`click-8.3.2/src/click/_termui_impl.py`) — 25 outbound dependencies
3. **types.py** (`click-8.3.2/src/click/types.py`) — 18 outbound dependencies
4. **test_utils.py** (`click-8.3.2/tests/test_utils.py`) — 18 outbound dependencies
5. **termui.py** (`click-8.3.2/src/click/termui.py`) — 16 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `format_pct` (@ `click-8.3.2/src/click/_termui_impl.py`) -> Impact: **1766.1** | LOC: 646
- `__init__` (@ `click-8.3.2/src/click/types.py`) -> Impact: **1315.9** | LOC: 614
- `clear` (@ `click-8.3.2/src/click/termui.py`) -> Impact: **173.0** | LOC: 204
- `invoke` (@ `click-8.3.2/src/click/core.py`) -> Impact: **169.6** | LOC: 67
- `test_progressbar_update` (@ `click-8.3.2/tests/test_termui.py`) -> Impact: **160.2** | LOC: 433
- `parse_args` (@ `click-8.3.2/src/click/core.py`) -> Impact: **121.8** | LOC: 35
- `process_value` (@ `click-8.3.2/src/click/core.py`) -> Impact: **121.8** | LOC: 55
  * *Intent:* """Given a context and a command name, this returns a :class:`Command` object if it exists or returns ``None``. """
- `type_cast_value` (@ `click-8.3.2/src/click/core.py`) -> Impact: **107.7** | LOC: 54
- `shell_complete` (@ `click-8.3.2/src/click/core.py`) -> Impact: **106.8** | LOC: 37
  * *Intent:* #: The context class to create with :meth:`make_context`. #: .. versionadded:: 8.0 context_class: type[Context] = Context #: the default for the :attr...
- `format_message` (@ `click-8.3.2/src/click/exceptions.py`) -> Impact: **95.5** | LOC: 39

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `format_pct` (@ `click-8.3.2/src/click/_termui_impl.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `click-8.3.2/src/click/types.py`) -> **O(2^N) [Recursive]**
- `invoke` (@ `click-8.3.2/src/click/core.py`) -> **O(2^N) [Recursive]**
- `parse_args` (@ `click-8.3.2/src/click/core.py`) -> **O(2^N) [Recursive]**
- `get_command` (@ `click-8.3.2/src/click/core.py`) -> **O(2^N) [Recursive]**
- `command_path` (@ `click-8.3.2/src/click/core.py`) -> **O(2^N) [Recursive]**
  * *Intent:* #: Controls if styling output is wanted or not.
- `shell_complete` (@ `click-8.3.2/src/click/core.py`) -> **O(2^N) [Recursive]**
- `invoke` (@ `click-8.3.2/src/click/core.py`) -> **O(2^N) [Recursive]**
- `to_info_dict` (@ `click-8.3.2/src/click/core.py`) -> **O(2^N) [Recursive]**
- `flush` (@ `click-8.3.2/src/click/utils.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `format_pct` (@ `click-8.3.2/src/click/_termui_impl.py`) -> DB Complexity: **151**
- `__init__` (@ `click-8.3.2/src/click/types.py`) -> DB Complexity: **108**
- `get_app_dir` (@ `click-8.3.2/src/click/utils.py`) -> DB Complexity: **33**
- `clear` (@ `click-8.3.2/src/click/termui.py`) -> DB Complexity: **22**
- `test_path_option` (@ `click-8.3.2/tests/test_basic.py`) -> DB Complexity: **21**
- `test_sys_streams_restored_after_invoke` (@ `click-8.3.2/tests/test_stream_lifecycle.py`) -> DB Complexity: **18**
- `test_sys_streams_restored_after_exceptio` (@ `click-8.3.2/tests/test_stream_lifecycle.py`) -> DB Complexity: **12**
- `_symlinks_supported` (@ `click-8.3.2/tests/test_types.py`) -> DB Complexity: **12**
- `test_path_resolve_symlink` (@ `click-8.3.2/tests/test_types.py`) -> DB Complexity: **12**
- `visible_input` (@ `click-8.3.2/src/click/testing.py`) -> DB Complexity: **9**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `click-8.3.2/src/click` | 17 | 14796.83 | 24.79% | 58.36% |
| `click-8.3.2/tests` | 21 | 3681.38 | 3.39% | 0.0% |
| `click-8.3.2/tests/typing` | 9 | 116.58 | 5.33% | 0.0% |
| `click-8.3.2` | 2 | 2.26 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `click-8.3.2/src/click/exceptions.py` -> **100.0%** Exposure
- `click-8.3.2/src/click/shell_completion.py` -> **99.9999%** Exposure
- `click-8.3.2/src/click/decorators.py` -> **99.9943%** Exposure
- `click-8.3.2/src/click/core.py` -> **99.9931%** Exposure
- `click-8.3.2/src/click/utils.py` -> **99.988%** Exposure
### Highest State Flux (Mutation/Volatility)
- `click-8.3.2/src/click/_textwrap.py` -> **100.0%** Exposure
- `click-8.3.2/src/click/parser.py` -> **99.9979%** Exposure
- `click-8.3.2/src/click/_termui_impl.py` -> **99.9571%** Exposure
- `click-8.3.2/src/click/core.py` -> **96.9655%** Exposure
- `click-8.3.2/src/click/formatting.py` -> **95.3069%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `click-8.3.2/src/click/core.py` -> **0** Orphaned Functions | **54** Duplicates
- `click-8.3.2/tests/test_options.py` -> **33** Orphaned Functions | **4** Duplicates
- `click-8.3.2/tests/test_shell_completion.py` -> **34** Orphaned Functions | **0** Duplicates
- `click-8.3.2/tests/test_arguments.py` -> **32** Orphaned Functions | **0** Duplicates
- `click-8.3.2/tests/test_utils.py` -> **30** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`click-8.3.2/src/click/_termui_impl.py`** -> AI Confidence: **99.31%**
2. **`click-8.3.2/src/click/core.py`** -> AI Confidence: **99.31%**
3. **`click-8.3.2/src/click/formatting.py`** -> AI Confidence: **99.31%**
4. **`click-8.3.2/src/click/parser.py`** -> AI Confidence: **99.31%**
5. **`click-8.3.2/src/click/termui.py`** -> AI Confidence: **99.24%**
6. **`click-8.3.2/tests/test_termui.py`** -> AI Confidence: **99.18%**
7. **`click-8.3.2/tests/test_utils.py`** -> AI Confidence: **99.18%**
8. **`click-8.3.2/src/click/_compat.py`** -> AI Confidence: **99.16%**
9. **`click-8.3.2/src/click/shell_completion.py`** -> AI Confidence: **99.16%**
10. **`click-8.3.2/src/click/testing.py`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `click-8.3.2/tests/test_utils.py` -> **0.0004%** Exposure
### Exploit Generation Surface
- `click-8.3.2/src/click/_termui_impl.py` -> **100.0%** Exposure
- `click-8.3.2/src/click/core.py` -> **100.0%** Exposure
- `click-8.3.2/src/click/decorators.py` -> **100.0%** Exposure
- `click-8.3.2/src/click/exceptions.py` -> **100.0%** Exposure
- `click-8.3.2/src/click/formatting.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `click-8.3.2/src/click/_termui_impl.py` -> **100.0%** Exposure
- `click-8.3.2/tests/test_imports.py` -> **100.0%** Exposure
- `click-8.3.2/tests/test_utils.py` -> **0.5339%** Exposure
### Algorithmic DoS Exposure
- `click-8.3.2/src/click/_termui_impl.py` -> **100.0%** Exposure
- `click-8.3.2/src/click/core.py` -> **100.0%** Exposure
- `click-8.3.2/src/click/exceptions.py` -> **100.0%** Exposure
- `click-8.3.2/src/click/formatting.py` -> **100.0%** Exposure
- `click-8.3.2/src/click/parser.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `287` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `click-8.3.2/src/click/core.py` (PYTHON) -> Cumulative Risk: **839.95**
- **Archetype:** `file_cluster_16` (Distance: 12.519 IQR)
- **Magnitude:** 2129.36 | **LOC:** 3438 | **CtrlFlow:** 53.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9931%)
- **Heaviest Functions:** `invoke` (Impact: 169.6), `parse_args` (Impact: 121.8), `process_value` (Impact: 121.8)

### 2. `click-8.3.2/src/click/parser.py` (PYTHON) -> Cumulative Risk: **823.04**
- **Archetype:** `file_cluster_13` (Distance: 11.828 IQR)
- **Magnitude:** 375.36 | **LOC:** 533 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9979%)
- **Heaviest Functions:** `_match_short_opt` (Impact: 62.0), `_process_opts` (Impact: 31.6), `_process_args_for_options` (Impact: 31.1)

### 3. `click-8.3.2/src/click/_termui_impl.py` (PYTHON) -> Cumulative Risk: **819.3**
- **Archetype:** `file_cluster_13` (Distance: 12.113 IQR)
- **Magnitude:** 2042.84 | **LOC:** 853 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `format_pct` (Impact: 1766.1), `format_eta` (Impact: 18.0), `pct` (Impact: 14.1)

### 4. `click-8.3.2/src/click/utils.py` (PYTHON) -> Cumulative Risk: **799.46**
- **Archetype:** `file_cluster_13` (Distance: 11.55 IQR)
- **Magnitude:** 271.76 | **LOC:** 628 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.988%)
- **Heaviest Functions:** `make_default_short_help` (Impact: 44.0), `get_app_dir` (Impact: 28.9), `flush` (Impact: 26.4)

### 5. `click-8.3.2/src/click/testing.py` (PYTHON) -> Cumulative Risk: **782.51**
- **Archetype:** `file_cluster_13` (Distance: 11.472 IQR)
- **Magnitude:** 246.4 | **LOC:** 575 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (97.4018%)
- **Heaviest Functions:** `visible_input` (Impact: 21.7), `hidden_input` (Impact: 21.6), `_pause_echo` (Impact: 11.4)

### 6. `click-8.3.2/src/click/decorators.py` (PYTHON) -> Cumulative Risk: **774.4**
- **Archetype:** `file_cluster_16` (Distance: 10.958 IQR)
- **Magnitude:** 214.88 | **LOC:** 552 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9984%), Tech Debt (99.9943%)
- **Heaviest Functions:** `decorator` (Impact: 61.7), `decorator` (Impact: 25.0), `_param_memo` (Impact: 16.4)

### 7. `click-8.3.2/src/click/types.py` (PYTHON) -> Cumulative Risk: **758.13**
- **Archetype:** `file_cluster_13` (Distance: 11.579 IQR)
- **Magnitude:** 1562.84 | **LOC:** 1210 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.8846%)
- **Heaviest Functions:** `__init__` (Impact: 1315.9), `get_metavar` (Impact: 40.9), `normalize_choice` (Impact: 24.6)

### 8. `click-8.3.2/src/click/exceptions.py` (PYTHON) -> Cumulative Risk: **754.94**
- **Archetype:** `file_cluster_13` (Distance: 10.692 IQR)
- **Magnitude:** 300.78 | **LOC:** 309 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `format_message` (Impact: 95.5), `show` (Impact: 27.0), `__init__` (Impact: 18.2)

### 9. `click-8.3.2/src/click/shell_completion.py` (PYTHON) -> Cumulative Risk: **742.69**
- **Archetype:** `file_cluster_16` (Distance: 11.042 IQR)
- **Magnitude:** 298.92 | **LOC:** 668 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9999%)
- **Heaviest Functions:** `_check_version` (Impact: 80.4), `_is_incomplete_option` (Impact: 33.0), `_is_incomplete_argument` (Impact: 21.7)

### 10. `click-8.3.2/src/click/_winconsole.py` (PYTHON) -> Cumulative Risk: **711.51**
- **Archetype:** `file_cluster_13` (Distance: 9.547 IQR)
- **Magnitude:** 176.12 | **LOC:** 297 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (99.9998%), Tech Debt (99.9847%), Algorithmic Dos (99.9841%)
- **Heaviest Functions:** `readinto` (Impact: 27.4), `write` (Impact: 21.2), `get_buffer` (Impact: 17.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `click-8.3.2/src/click/_compat.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.108 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.989 IQR)
- **Top Global Matches:** file_cluster_16: 11.108, file_cluster_8: 11.175, file_cluster_13: 11.214
- **Magnitude:** 6552.45 | **LOC:** 623 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (16.0516%), Tech Debt (9.3628%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 159`, `args: 49`, `func_start: 49`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 11`, `planned_debt: 1`
* *Architecture:* `io: 43`, `api: 22`, `import: 15`
* *Defense:* `safety: 49`, `doc: 16`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 127.933
  * `Choke Point (Betweenness):` 0.030142 | `Ripple Effect (Closeness):` 0.335317
  * `Imports (Out-Degree: 2):` weakref, re, os, colorama, codecs, locale, typing, errno...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `click-8.3.2/src/click/core.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.519 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.148 IQR)
- **Top Global Matches:** file_cluster_16: 12.519, file_cluster_13: 12.58, file_cluster_11: 12.829
- **Magnitude:** 2129.36 | **LOC:** 3438 | **CtrlFlow:** 53.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (31.9593%), Tech Debt (99.9931%)
**Top Internal Functions/Classes:**
  * `invoke` (Impact: 169.6 | O(2^N) | DB: 2)
  * `parse_args` (Impact: 121.8 | O(2^N) | DB: 1)
  * `process_value` (Impact: 121.8 | O(N^6) | DB: 3)
    * *Intent:* """Given a context and a command name, this returns a :class:`Command` object if it exists or return...
  * `type_cast_value` (Impact: 107.7 | O(N^6) | DB: 3)
  * `shell_complete` (Impact: 106.8 | O(N^6) | DB: 2)
    * *Intent:* #: The context class to create with :meth:`make_context`. #: .. versionadded:: 8.0 context_class: ty...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 537`, `structural_boundaries: 467`, `args: 142`, `func_start: 140`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 150`, `state_mutation: 246`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 54`
* *Architecture:* `io: 17`, `api: 133`, `import: 54`
* *Defense:* `safety: 54`, `doc: 270`, `test: 6`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 122.737
  * `Choke Point (Betweenness):` 0.082986 | `Ripple Effect (Closeness):` 0.299645
  * `Imports (Out-Degree: 10):` ._utils, functools, .exceptions, .termui, .shell_completion, gettext, itertools, types...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `click-8.3.2/src/click/_termui_impl.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.113 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.539 IQR)
- **Top Global Matches:** file_cluster_13: 12.113, file_cluster_11: 12.424, file_cluster_0: 12.45
- **Magnitude:** 2042.84 | **LOC:** 853 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 151
- **Risk Profile:** Cognitive Load (64.6004%), Tech Debt (8.8816%)
**Top Internal Functions/Classes:**
  * `format_pct` (Impact: 1766.1 | O(2^N) | DB: 151)
  * `format_eta` (Impact: 18.0 | O(N^4))
  * `pct` (Impact: 14.1 | O(N^3))
  * `__iter__` (Impact: 10.6 | O(N^3))
  * `render_finish` (Impact: 10.6 | O(N^3))
    * *Intent:* # Iteration is defined in terms of a generator function, # returned by iter(self); use that to defin...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 170`, `args: 36`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 146`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 39`, `api: 31`, `import: 40`
* *Defense:* `safety: 32`, `doc: 16`, `test: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.161
  * `Choke Point (Betweenness):` 0.008163 | `Ripple Effect (Closeness):` 0.171748
  * `Imports (Out-Degree: 4):` shlex, .exceptions, pathlib, gettext, time, types, shutil, urllib.parse...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `click-8.3.2/src/click/types.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.579 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.082 IQR)
- **Top Global Matches:** file_cluster_13: 11.579, file_cluster_16: 11.582, file_cluster_8: 11.841
- **Magnitude:** 1562.84 | **LOC:** 1210 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 108
- **Risk Profile:** Cognitive Load (15.1054%), Tech Debt (99.8846%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 1315.9 | O(2^N) | DB: 108)
  * `get_metavar` (Impact: 40.9 | O(N^4))
  * `normalize_choice` (Impact: 24.6 | O(N^3))
  * `to_info_dict` (Impact: 11.1 | O(N^3))
  * `split_envvar_value` (Impact: 5.4 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 233`, `args: 66`, `func_start: 66`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 40`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 16`
* *Architecture:* `io: 29`, `api: 60`, `import: 25`
* *Defense:* `safety: 37`, `doc: 87`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 104.722
  * `Choke Point (Betweenness):` 0.041585 | `Ripple Effect (Closeness):` 0.327519
  * `Imports (Out-Degree: 5):` os, typing_extensions, .exceptions, operator, .shell_completion, typing, .utils, stat...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `click-8.3.2/tests/test_options.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.076 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.521 IQR)
- **Top Global Matches:** file_cluster_8: 11.076, file_cluster_0: 11.09, file_cluster_7: 11.531
- **Magnitude:** 531.98 | **LOC:** 2504 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (2.3433%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_dual_options_custom_type_sentinel_f` (Impact: 89.0 | O(N^5))
    * *Intent:* # Passing --config with an argument that does not exist raises an error.
  * `test_choice_usage_rendering` (Impact: 25.9 | O(N^3))
  * `test_flag_value_on_option_with_zero_or_o` (Impact: 17.4 | O(N^3))
  * `test_invalid_nargs` (Impact: 14.2 | O(N^3))
  * `test_callable_flag_value_not_instantiate` (Impact: 14.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 632`, `args: 163`, `func_start: 162`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 25`, `duplicate_logic: 4`, `orphaned_logic: 33`
* *Architecture:* `io: 4`, `api: 174`, `import: 13`
* *Defense:* `safety: 225`, `doc: 62`, `test: 343`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.525
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` re, os, tempfile, typing, click.testing, pytest, sys, contextlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/tests/test_termui.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.992 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.316 IQR)
- **Top Global Matches:** file_cluster_0: 10.992, file_cluster_8: 11.175, file_cluster_13: 11.429
- **Magnitude:** 427.26 | **LOC:** 713 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (6.8709%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_progressbar_update` (Impact: 160.2 | O(N^4) | DB: 7)
  * `test_progressbar_length_hint` (Impact: 23.1 | O(N^4) | DB: 2)
  * `test_progressbar_is_iterator` (Impact: 21.4 | O(N^5))
  * `test_progressbar_format_progress_line_wi` (Impact: 14.4 | O(N^3))
  * `test_progressbar_strip_regression` (Impact: 13.7 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 164`, `args: 68`, `func_start: 58`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 11`, `orphaned_logic: 20`
* *Architecture:* `io: 1`, `api: 54`, `import: 8`
* *Defense:* `safety: 59`, `doc: 8`, `test: 121`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.525
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` click._termui_impl, tempfile, time, pytest, click._compat, click.exceptions, platform
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/src/click/parser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.828 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.699 IQR)
- **Top Global Matches:** file_cluster_13: 11.828, file_cluster_16: 12.018, file_cluster_8: 12.132
- **Magnitude:** 375.36 | **LOC:** 533 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (45.3004%), Tech Debt (99.4905%)
**Top Internal Functions/Classes:**
  * `_match_short_opt` (Impact: 62.0 | O(N^5) | DB: 3)
    * *Intent:* # [arg0, arg1, ..., arg(i-1), arg(i), arg(i+1), ..., arg(N-1)] # ^ # (we are about to process arg(i)...
  * `_process_opts` (Impact: 31.6 | O(N^4) | DB: 1)
  * `_process_args_for_options` (Impact: 31.1 | O(N^4) | DB: 3)
  * `process` (Impact: 28.7 | O(N^3) | DB: 8)
  * `_fetch` (Impact: 20.4 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 92`, `args: 21`, `func_start: 21`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 107`, `planned_debt: 3`, `duplicate_logic: 6`
* *Architecture:* `api: 10`, `import: 21`
* *Defense:* `safety: 9`, `doc: 13`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.28
  * `Choke Point (Betweenness):` 0.009338 | `Ripple Effect (Closeness):` 0.210199
  * `Imports (Out-Degree: 4):` ._utils, .exceptions, .shell_completion, typing, difflib, warnings, gettext, .core...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `click-8.3.2/tests/test_utils.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.105 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.625 IQR)
- **Top Global Matches:** file_cluster_0: 11.105, file_cluster_8: 11.229, file_cluster_13: 11.327
- **Magnitude:** 350.38 | **LOC:** 749 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (3.8378%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_echo_via_pager` (Impact: 52.2 | O(N^4) | DB: 6)
  * `test_echo_writing_to_standard_error` (Impact: 27.2 | O(N^2))
  * `test_prompts` (Impact: 19.2 | O(N^3))
  * `test_iter_lazyfile` (Impact: 17.7 | O(N^4) | DB: 3)
  * `test_open_file` (Impact: 14.9 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 192`, `args: 49`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`, `dead_code: 1`, `orphaned_logic: 30`
* *Architecture:* `io: 31`, `api: 40`, `import: 19`
* *Defense:* `safety: 97`, `doc: 6`, `test: 151`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.525
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` click._termui_impl, click.utils, os, functools, tempfile, pathlib, stat, fractions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/src/click/exceptions.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.692 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.136 IQR)
- **Top Global Matches:** file_cluster_13: 10.692, file_cluster_16: 10.774, file_cluster_8: 10.933
- **Magnitude:** 300.78 | **LOC:** 309 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (19.5896%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `format_message` (Impact: 95.5 | O(N^5))
  * `show` (Impact: 27.0 | O(N^4))
  * `__init__` (Impact: 18.2 | O(2^N) | DB: 1)
  * `format_message` (Impact: 17.9 | O(N^3))
  * `__str__` (Impact: 17.6 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 69`, `args: 20`, `func_start: 20`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 21`, `duplicate_logic: 19`
* *Architecture:* `io: 1`, `api: 19`, `import: 12`
* *Defense:* `safety: 1`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 61.785
  * `Choke Point (Betweenness):` 0.017332 | `Ripple Effect (Closeness):` 0.293403
  * `Imports (Out-Degree: 4):` typing, .utils, gettext, .core, ._compat, collections.abc, __future__, .globals
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `click-8.3.2/src/click/shell_completion.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.042 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.297 IQR)
- **Top Global Matches:** file_cluster_16: 11.042, file_cluster_13: 11.046, file_cluster_8: 11.39
- **Magnitude:** 298.92 | **LOC:** 668 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (16.5749%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `_check_version` (Impact: 80.4 | O(N^6))
  * `_is_incomplete_option` (Impact: 33.0 | O(N^3))
    * *Intent:* """Shell completion for Zsh."""
  * `_is_incomplete_argument` (Impact: 21.7 | O(N^3))
  * `get_completion_args` (Impact: 18.0 | O(N^3) | DB: 7)
  * `split_arg_string` (Impact: 13.0 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 115`, `args: 27`, `func_start: 27`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 1`, `state_mutation: 17`, `planned_debt: 1`, `duplicate_logic: 12`
* *Architecture:* `io: 6`, `api: 26`, `import: 17`
* *Defense:* `safety: 11`, `doc: 82`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 62.815
  * `Choke Point (Betweenness):` 0.00314 | `Ripple Effect (Closeness):` 0.251488
  * `Imports (Out-Degree: 2):` re, shlex, os, typing, .utils, gettext, .core, collections.abc...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `click-8.3.2/tests/test_arguments.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.157 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.621 IQR)
- **Top Global Matches:** file_cluster_0: 11.157, file_cluster_8: 11.507, file_cluster_17: 11.842
- **Magnitude:** 293.36 | **LOC:** 630 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (4.227%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_file_args` (Impact: 22.7 | O(N^4) | DB: 3)
  * `test_file_atomics` (Impact: 18.2 | O(N^3) | DB: 9)
  * `test_nargs_envvar` (Impact: 17.7 | O(N^2))
  * `test_required_argument` (Impact: 16.7 | O(N^3))
    * *Intent:* """Test how a required argument is processing the provided values."""
  * `test_nargs_mismatch_with_tuple_type` (Impact: 10.7 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 166`, `args: 65`, `func_start: 65`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `orphaned_logic: 32`
* *Architecture:* `io: 5`, `api: 67`, `import: 5`
* *Defense:* `safety: 69`, `doc: 8`, `test: 111`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.525
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unittest, pytest, sys, click._utils, click
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/src/click/termui.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.704 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.882 IQR)
- **Top Global Matches:** file_cluster_13: 11.704, file_cluster_16: 11.956, file_cluster_0: 12.155
- **Magnitude:** 290.96 | **LOC:** 884 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (21.377%), Tech Debt (77.2174%)
**Top Internal Functions/Classes:**
  * `clear` (Impact: 173.0 | O(N^3) | DB: 22)
  * `prompt_func` (Impact: 25.8 | O(N^4))
  * `_format_default` (Impact: 9.2 | O(N^2))
  * `hidden_prompt_func` (Impact: 2.2 | O(N^1))
  * `progressbar` (Impact: 1.9 | O(N^1))
    * *Intent:* # Echo the last character to stdout to work around an issue where
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 119`, `args: 23`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 39`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `io: 3`, `api: 23`, `import: 27`
* *Defense:* `safety: 24`, `doc: 83`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.531
  * `Choke Point (Betweenness):` 0.010284 | `Ripple Effect (Closeness):` 0.20119
  * `Imports (Out-Degree: 6):` .globals, .exceptions, typing, .utils, ._termui_impl, gettext, ._compat, getpass...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `click-8.3.2/tests/test_basic.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.306 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.26 IQR)
- **Top Global Matches:** file_cluster_0: 11.306, file_cluster_8: 11.666, file_cluster_13: 11.96
- **Magnitude:** 284.9 | **LOC:** 742 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (2.4796%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_path_option` (Impact: 23.0 | O(N^3) | DB: 21)
  * `test_datetime_option_default` (Impact: 21.3 | O(N^4) | DB: 1)
  * `test_file_lazy_mode` (Impact: 19.2 | O(N^3) | DB: 6)
  * `test_flag_value_dual_options` (Impact: 17.4 | O(N^2))
  * `test_uuid_option` (Impact: 9.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 239`, `args: 76`, `func_start: 76`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 2`, `fragile_debt: 2`, `orphaned_logic: 23`
* *Architecture:* `io: 9`, `api: 76`, `import: 7`
* *Defense:* `safety: 115`, `doc: 14`, `test: 152`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.525
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` os, pytest, itertools, __future__, enum, click._utils, click
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/tests/test_context.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.285 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.299 IQR)
- **Top Global Matches:** file_cluster_0: 11.285, file_cluster_13: 11.707, file_cluster_8: 11.713
- **Magnitude:** 281.76 | **LOC:** 783 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (2.523%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_with_resource_nested_exception` (Impact: 29.4 | O(N^4) | DB: 3)
  * `test_with_resource_exception` (Impact: 28.6 | O(N^4) | DB: 3)
  * `test_no_state_leaks` (Impact: 11.2 | O(N^3) | DB: 2)
    * *Intent:* """Demonstrate state leaks with a specific case of the generic test above. Use a logger as a real-wo...
  * `test_multiple_eager_callbacks` (Impact: 9.8 | O(N^3) | DB: 1)
  * `test_hiding_of_unset_sentinel_in_callbac` (Impact: 9.0 | O(N^3))
    * *Intent:* """Fix: https://github.com/pallets/click/issues/3136"""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 219`, `args: 77`, `func_start: 77`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 20`, `orphaned_logic: 23`
* *Architecture:* `api: 79`, `import: 12`
* *Defense:* `safety: 81`, `doc: 26`, `test: 118`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.525
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` logging, click.core, pytest, contextlib, click.decorators, types, click
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/src/click/utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.55 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.017 IQR)
- **Top Global Matches:** file_cluster_13: 11.55, file_cluster_16: 11.782, file_cluster_8: 12.071
- **Magnitude:** 271.76 | **LOC:** 628 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (25.8093%), Tech Debt (99.988%)
**Top Internal Functions/Classes:**
  * `make_default_short_help` (Impact: 44.0 | O(N^3))
  * `get_app_dir` (Impact: 28.9 | O(N^3) | DB: 33)
  * `flush` (Impact: 26.4 | O(2^N))
  * `close` (Impact: 14.1 | O(2^N))
  * `open` (Impact: 13.7 | O(N^4) | DB: 5)
    * *Intent:* """Opens the file if it's not yet open. This call might fail with a :exc:`FileError`. Not handling t...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 126`, `args: 31`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 29`, `duplicate_logic: 14`
* *Architecture:* `io: 34`, `api: 27`, `import: 24`
* *Defense:* `safety: 19`, `doc: 58`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 81.632
  * `Choke Point (Betweenness):` 0.007883 | `Ripple Effect (Closeness):` 0.287415
  * `Imports (Out-Degree: 4):` re, os, functools, .globals, typing_extensions, .exceptions, typing, errno...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `click-8.3.2/src/click/testing.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.472 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.952 IQR)
- **Top Global Matches:** file_cluster_13: 11.472, file_cluster_16: 11.601, file_cluster_0: 11.65
- **Magnitude:** 246.4 | **LOC:** 575 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (17.6079%), Tech Debt (97.3901%)
**Top Internal Functions/Classes:**
  * `visible_input` (Impact: 21.7 | O(N^4) | DB: 9)
  * `hidden_input` (Impact: 21.6 | O(N^4) | DB: 6)
  * `_pause_echo` (Impact: 11.4 | O(N^2))
  * `readlines` (Impact: 10.5 | O(2^N))
  * `_getchar` (Impact: 10.4 | O(N^4) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 108`, `args: 34`, `func_start: 34`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 29`, `duplicate_logic: 8`
* *Architecture:* `io: 32`, `api: 31`, `import: 18`
* *Defense:* `safety: 25`, `doc: 49`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.918
  * `Choke Point (Betweenness):` 0.01578 | `Ripple Effect (Closeness):` 0.0625
  * `Imports (Out-Degree: 3):` shlex, os, tempfile, typing, , types, .core, ._compat...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `click-8.3.2/tests/test_stream_lifecycle.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.242 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.184 IQR)
- **Top Global Matches:** file_cluster_0: 12.242, file_cluster_13: 12.445, file_cluster_8: 12.517
- **Magnitude:** 223.86 | **LOC:** 539 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (2.533%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_invoke_with_threads_writing_to_stre` (Impact: 15.0 | O(N^3))
  * `test_invoke_with_thread_pool` (Impact: 14.6 | O(N^3))
  * `test_invoke_with_logger_and_prompt` (Impact: 12.0 | O(2^N))
  * `test_logging_with_cli_log_level` (Impact: 11.5 | O(N^3) | DB: 3)
  * `test_invoke_with_stream_handler_on_stder` (Impact: 11.4 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 138`, `args: 49`, `func_start: 47`
* *Risk/State:* `state_mutation: 3`, `orphaned_logic: 24`
* *Architecture:* `io: 12`, `api: 47`, `concurrency: 8`, `import: 13`
* *Defense:* `safety: 69`, `doc: 54`, `test: 97`, `sync_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.525
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` logging, click.testing, concurrent.futures, gc, pytest, sys, io, __future__...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/tests/test_commands.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.876 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.513 IQR)
- **Top Global Matches:** file_cluster_0: 10.876, file_cluster_8: 11.272, file_cluster_13: 11.612
- **Magnitude:** 215.56 | **LOC:** 576 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (3.0378%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_object_propagation` (Impact: 22.6 | O(N^4))
  * `test_custom_parser` (Impact: 16.2 | O(N^4) | DB: 2)
  * `test_help_param_priority` (Impact: 13.6 | O(N^3))
  * `test_invoked_subcommand` (Impact: 11.4 | O(N^3))
  * `test_auto_shorthelp` (Impact: 8.5 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 167`, `args: 65`, `func_start: 65`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 7`, `fragile_debt: 1`, `orphaned_logic: 22`
* *Architecture:* `api: 66`, `import: 4`
* *Defense:* `safety: 69`, `doc: 8`, `test: 95`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.525
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` re, optparse, click, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/src/click/decorators.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.958 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.052 IQR)
- **Top Global Matches:** file_cluster_16: 10.958, file_cluster_13: 11.18, file_cluster_0: 11.478
- **Magnitude:** 214.88 | **LOC:** 552 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (13.957%), Tech Debt (99.9943%)
**Top Internal Functions/Classes:**
  * `decorator` (Impact: 61.7 | O(N^4) | DB: 2)
    * *Intent:* *,
  * `decorator` (Impact: 25.0 | O(N^5))
  * `_param_memo` (Impact: 16.4 | O(N^3) | DB: 2)
  * `confirmation_option` (Impact: 11.2 | O(N^3))
    * *Intent:* # variant: with optional string name, no cls argument provided.
  * `password_option` (Impact: 5.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 112`, `args: 33`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 18`, `duplicate_logic: 13`
* *Architecture:* `api: 39`, `import: 15`
* *Defense:* `safety: 11`, `doc: 50`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.097
  * `Choke Point (Betweenness):` 0.000369 | `Ripple Effect (Closeness):` 0.20119
  * `Imports (Out-Degree: 3):` functools, typing_extensions, typing, .utils, gettext, .core, importlib.metadata, __future__...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `click-8.3.2/tests/test_testing.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.579 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.431 IQR)
- **Top Global Matches:** file_cluster_0: 11.579, file_cluster_8: 11.852, file_cluster_13: 12.132
- **Magnitude:** 188.68 | **LOC:** 472 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (2.357%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_runner_with_stream` (Impact: 14.0 | O(N^4))
  * `test_runner` (Impact: 13.8 | O(N^4))
  * `test_echo_stdin_stream` (Impact: 13.8 | O(N^4))
  * `test_catch_exceptions` (Impact: 6.3 | O(N^2))
  * `test_catch_exceptions_cli_runner` (Impact: 6.2 | O(N^2))
    * *Intent:* """Test that invoke `catch_exceptions` takes the value from CliRunner if not set explicitly."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 165`, `args: 54`, `func_start: 54`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `orphaned_logic: 22`
* *Architecture:* `io: 12`, `api: 57`, `import: 7`
* *Defense:* `safety: 86`, `doc: 6`, `test: 114`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.525
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` os, click.testing, pytest, sys, io, click.exceptions, click
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/src/click/formatting.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.11 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.122 IQR)
- **Top Global Matches:** file_cluster_16: 11.11, file_cluster_13: 11.18, file_cluster_7: 11.508
- **Magnitude:** 187.38 | **LOC:** 302 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (13.1373%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `write_usage` (Impact: 28.4 | O(N^5))
  * `_flush_par` (Impact: 21.2 | O(N^3) | DB: 2)
  * `join_options` (Impact: 16.8 | O(N^3) | DB: 1)
  * `measure_table` (Impact: 14.3 | O(N^3))
  * `section` (Impact: 10.9 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 42`, `args: 18`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 25`
* *Architecture:* `api: 24`, `import: 8`
* *Defense:* `safety: 4`, `doc: 42`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.531
  * `Choke Point (Betweenness):` 0.012057 | `Ripple Effect (Closeness):` 0.20119
  * `Imports (Out-Degree: 3):` gettext, ._compat, ._textwrap, collections.abc, contextlib, __future__, shutil, .parser
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `click-8.3.2/tests/test_shell_completion.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.047 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.259 IQR)
- **Top Global Matches:** file_cluster_8: 11.047, file_cluster_0: 11.103, file_cluster_13: 11.216
- **Magnitude:** 185.76 | **LOC:** 562 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (2.6806%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_files_closed` (Impact: 14.9 | O(N^3) | DB: 3)
    * *Intent:* # Now, "mysh" is finally in available shells assert "mysh" in click.shell_completion._available_shel...
  * `test_nested_group` (Impact: 7.8 | O(N^6))
  * `test_hidden` (Impact: 6.1 | O(N^5))
  * `test_help_option` (Impact: 5.4 | O(N^1))
  * `test_chained` (Impact: 4.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 201`, `args: 42`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 3`, `orphaned_logic: 34`
* *Architecture:* `io: 1`, `api: 40`, `import: 15`
* *Defense:* `safety: 99`, `doc: 6`, `test: 152`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.525
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` warnings, click.types, click.core, pytest, click.shell_completion, collections.abc, textwrap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/src/click/_winconsole.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.547 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.542 IQR)
- **Top Global Matches:** file_cluster_13: 9.547, file_cluster_8: 9.73, file_cluster_16: 9.912
- **Magnitude:** 176.12 | **LOC:** 297 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (17.9243%), Tech Debt (99.9847%)
**Top Internal Functions/Classes:**
  * `readinto` (Impact: 27.4 | O(N^4))
  * `write` (Impact: 21.2 | O(2^N))
  * `get_buffer` (Impact: 17.9 | O(N^3))
  * `_get_error_message` (Impact: 12.3 | O(N^3))
  * `write` (Impact: 11.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 107`, `args: 20`, `func_start: 20`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 3`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `io: 1`, `api: 18`, `import: 28`
* *Defense:* `safety: 15`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 59.892
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.210199
  * `Imports (Out-Degree: 1):` typing_extensions, typing, ctypes.wintypes, msvcrt, time, ctypes, ._compat, sys...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `click-8.3.2/tests/test_types.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.74 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.393 IQR)
- **Top Global Matches:** file_cluster_8: 9.74, file_cluster_0: 9.95, file_cluster_13: 10.046
- **Magnitude:** 160.62 | **LOC:** 258 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (5.5418%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_path_surrogates` (Impact: 58.1 | O(N^3) | DB: 6)
  * `test_file_surrogates` (Impact: 16.1 | O(N^2))
  * `test_cast_multi_default` (Impact: 11.5 | O(N^2))
  * `_symlinks_supported` (Impact: 10.9 | O(N^3) | DB: 12)
  * `_non_utf8_filenames_supported` (Impact: 10.8 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 70`, `args: 16`, `func_start: 14`
* *Risk/State:* `orphaned_logic: 11`
* *Architecture:* `io: 17`, `api: 12`, `import: 7`
* *Defense:* `safety: 16`, `doc: 2`, `test: 45`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.525
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tempfile, pathlib, os.path, pytest, platform, click
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `click-8.3.2/tests/test_formatting.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.885 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.252 IQR)
- **Top Global Matches:** file_cluster_0: 10.885, file_cluster_8: 11.134, file_cluster_7: 11.482
- **Magnitude:** 145.78 | **LOC:** 369 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (1.5501%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_basic_functionality` (Impact: 9.2 | O(N^2))
  * `test_truncating_docstring` (Impact: 8.8 | O(N^2))
  * `test_formatting_usage_error_metavar_bad_` (Impact: 8.5 | O(N^2))
  * `test_formatting_custom_type_metavar` (Impact: 7.9 | O(N^3))
  * `test_wrapping_long_options_strings` (Impact: 7.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 81`, `args: 39`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `orphaned_logic: 17`
* *Architecture:* `api: 40`, `import: 1`
* *Defense:* `safety: 30`, `doc: 25`, `test: 47`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.525
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` click
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `click-8.3.2/tests/test_custom_classes.py` (PYTHON) | Magnitude: 42.26 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 44, api: 20, test: 17
- `click-8.3.2/tests/test_utils.py` (PYTHON) | Magnitude: 350.38 | Delta: **0.124 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 515, structural_boundaries: 192, test: 151, safety: 97
- `click-8.3.2/tests/test_termui.py` (PYTHON) | Magnitude: 427.26 | Delta: **0.183 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 432, structural_boundaries: 164, test: 121, args: 68
- `click-8.3.2/tests/test_stream_lifecycle.py` (PYTHON) | Magnitude: 223.86 | Delta: **0.203 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 277, structural_boundaries: 138, test: 97, safety: 69
- `click-8.3.2/tests/test_command_decorators.py` (PYTHON) | Magnitude: 33.26 | Delta: **0.219 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 35, test: 19, api: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `click-8.3.2/src/click/types.py` (PYTHON) | Magnitude: 1562.84 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 627, structural_boundaries: 233, branch: 140, doc: 87
- `click-8.3.2/tests/test_compat.py` (PYTHON) | Magnitude: 5.02 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 4, api: 2, test: 2
- `click-8.3.2/tests/typing/typing_progressbar.py` (PYTHON) | Magnitude: 26.32 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 9, branch: 4, generics: 4
- `click-8.3.2/src/click/exceptions.py` (PYTHON) | Magnitude: 300.78 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 162, structural_boundaries: 69, branch: 41, doc: 27
- `click-8.3.2/src/click/testing.py` (PYTHON) | Magnitude: 246.4 | Delta: **0.129 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 309, structural_boundaries: 108, encapsulation: 60, branch: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `click-8.3.2/src/click/shell_completion.py` (PYTHON) | Magnitude: 298.92 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 248, structural_boundaries: 115, doc: 82, branch: 62
- `click-8.3.2/src/click/core.py` (PYTHON) | Magnitude: 2129.36 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1644, branch: 537, structural_boundaries: 467, doc: 270
- `click-8.3.2/src/click/_compat.py` (PYTHON) | Magnitude: 6552.45 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 373, structural_boundaries: 159, encapsulation: 112, branch: 88
- `click-8.3.2/src/click/formatting.py` (PYTHON) | Magnitude: 187.38 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 175, structural_boundaries: 42, doc: 42, branch: 41
- `click-8.3.2/tests/typing/typing_aliased_group.py` (PYTHON) | Magnitude: 62.1 | Delta: **0.116 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 19, indent_spaces: 19, generics: 7, api: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `click-8.3.2/tests/test_options.py` (PYTHON) | Magnitude: 531.98 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1733, structural_boundaries: 632, test: 343, safety: 225
- `click-8.3.2/tests/test_imports.py` (PYTHON) | Magnitude: 25.38 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 8, concurrency: 6, branch: 4
- `click-8.3.2/tests/test_parser.py` (PYTHON) | Magnitude: 9.2 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 12, test: 8, encapsulation: 5
- `click-8.3.2/tests/test_shell_completion.py` (PYTHON) | Magnitude: 185.76 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 344, structural_boundaries: 201, test: 152, encapsulation: 112
- `click-8.3.2/tests/test_types.py` (PYTHON) | Magnitude: 160.62 | Delta: **0.21 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 160, structural_boundaries: 70, test: 45, branch: 33

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `click-8.3.2/src/click/core.py` -> **Severity: 8.047** (Bridge: 0.083 * Flux: 96.9655%)
- `click-8.3.2/src/click/types.py` -> **Severity: 2.184** (Bridge: 0.0416 * Flux: 52.5217%)
- `click-8.3.2/src/click/exceptions.py` -> **Severity: 1.573** (Bridge: 0.0173 * Flux: 90.7645%)
- `click-8.3.2/src/click/testing.py` -> **Severity: 1.208** (Bridge: 0.0158 * Flux: 76.5431%)
- `click-8.3.2/src/click/formatting.py` -> **Severity: 1.149** (Bridge: 0.0121 * Flux: 95.3069%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `click-8.3.2/src/click/_compat.py` -> **Severity: 26.825** (Embedded: 0.3353 * Error Risk: 80.0%)
- `click-8.3.2/src/click/core.py` -> **Severity: 22.109** (Embedded: 0.2996 * Error Risk: 73.7828%)
- `click-8.3.2/src/click/types.py` -> **Severity: 21.523** (Embedded: 0.3275 * Error Risk: 65.7143%)
- `click-8.3.2/src/click/utils.py` -> **Severity: 18.887** (Embedded: 0.2874 * Error Risk: 65.7143%)
- `click-8.3.2/src/click/globals.py` -> **Severity: 15.686** (Embedded: 0.2387 * Error Risk: 65.7143%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `click-8.3.2/src/click/core.py` -> **Severity: 11565.176** (Blast Radius: 122.737 * Doc Risk: 94.2273%)
- `click-8.3.2/src/click/types.py` -> **Severity: 8541.964** (Blast Radius: 104.722 * Doc Risk: 81.568%)
- `click-8.3.2/src/click/utils.py` -> **Severity: 7612.608** (Blast Radius: 81.632 * Doc Risk: 93.2552%)
- `click-8.3.2/src/click/exceptions.py` -> **Severity: 6176.325** (Blast Radius: 61.785 * Doc Risk: 99.9648%)
- `click-8.3.2/src/click/_winconsole.py` -> **Severity: 5977.126** (Blast Radius: 59.892 * Doc Risk: 99.7984%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
