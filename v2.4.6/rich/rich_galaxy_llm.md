# ARCHITECTURAL_BRIEF: rich
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/rich` |
| **Timestamp** | `2026-08-03T19:40:43.308656+00:00` |
| **Scan Duration** | `1.3s` |
| **Git Branch** | `master` |
| **Git Commit** | `fc41075a3206d2a5fd846c6f41c4d2becab814fa` |
| **Git Remote** | `https://github.com/Textualize/rich.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 178 malicious artifacts.

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
| Total Artifacts | 553 |
| Analyzed Artifacts (Scanned) | 399 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 154 |
| Total LOC | 25134 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 72.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3036 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2224 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 11.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.4482 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 20 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JSON | 179 | 834 | 44.9% |
| PYTHON | 176 | 24256 | 44.1% |
| MARKDOWN | 39 | 0 | 9.8% |
| MAKEFILE | 1 | 15 | 0.3% |
| YAML | 1 | 4 | 0.3% |
| XML | 1 | 1 | 0.3% |
| BATCH | 1 | 24 | 0.3% |
| PLAINTEXT | 1 | 0 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.667`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 80 | 20.1% |
| file_cluster_13 | 73 | 18.3% |
| file_cluster_16 | 24 | 6.0% |
| file_cluster_0 | 3 | 0.8% |
| file_cluster_7 | 1 | 0.3% |
| file_cluster_2 | 1 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Minified & Vendor Opaque Mass | 177 | 44.4% |
| Static: Literature & Documentation | 40 | 10.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 154*

**Composition by Extension & Reason:**
- `.rst`: 63x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 481 LOC), 1x Excluded (Saturation: Line 94 exceeds 500 chars)
- `.png`: 16x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2386 LOC)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.gif`: 5x Excluded (Explicitly Denied Extension: '.gif')
- `.svg`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.ini')
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ai`: 1x Excluded (Explicitly Denied Extension: '.ai')
- `.bat`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 79.1 | 5.5 | 0.0 | 0.0 |
| Error & Exception Exposure | 0.0 | 92.1 | 6.1 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 4.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.2 | 0.0 | 0.0 |
| API Exposure | 0.0 | 14.7 | 2.1 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 54.8 | 0.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 9.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 7.2 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 45.4 | 20.0 | 0.0 |
| Instability Exposure | 0.0 | 6.1 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 16.9 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 20.5 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 88.7 | 0.2 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 14.2 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/test_win32_console.py` (Hits: 28)
- `tests/test_console.py` (Hits: 27)
- `rich/console.py` (Hits: 22)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **console.py** (`rich/console.py`) — 108 inbound connections
2. **text.py** (`rich/text.py`) — 54 inbound connections
3. **style.py** (`rich/style.py`) — 44 inbound connections
4. **segment.py** (`rich/segment.py`) — 29 inbound connections
5. **measure.py** (`rich/measure.py`) — 26 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **console.py** (`rich/console.py`) — 53 outbound dependencies
2. **progress.py** (`rich/progress.py`) — 31 outbound dependencies
3. **syntax.py** (`rich/syntax.py`) — 27 outbound dependencies
4. **live.py** (`rich/live.py`) — 26 outbound dependencies
5. **pretty.py** (`rich/pretty.py`) — 25 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` (@ `rich/progress.py`) -> Impact: **3032.4** | LOC: 881
- `__init__` (@ `rich/console.py`) -> Impact: **1819.6** | LOC: 570
- `_traverse` (@ `rich/pretty.py`) -> Impact: **1062.7** | LOC: 254
- `create` (@ `rich/markdown.py`) -> Impact: **857.6** | LOC: 352
- `__init__` (@ `rich/logging.py`) -> Impact: **683.5** | LOC: 161
- `_make_ansi_codes` (@ `rich/style.py`) -> Impact: **333.4** | LOC: 242
- `escape` (@ `rich/markup.py`) -> Impact: **312.3** | LOC: 183
- `do_replace` (@ `rich/repr.py`) -> Impact: **308.3** | LOC: 104
- `render_stack` (@ `rich/traceback.py`) -> Impact: **259.8** | LOC: 104
- `__str__` (@ `rich/style.py`) -> Impact: **251.7** | LOC: 46

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `stop` (@ `rich/live.py`) -> **O(2^N) [Recursive]**
- `refresh` (@ `rich/live.py`) -> **O(2^N) [Recursive]**
- `create` (@ `rich/markdown.py`) -> **O(2^N) [Recursive]**
- `_traverse` (@ `rich/pretty.py`) -> **O(2^N) [Recursive]**
- `iter_tokens` (@ `rich/pretty.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `rich/progress.py`) -> **O(2^N) [Recursive]**
- `do_replace` (@ `rich/repr.py`) -> **O(2^N) [Recursive]**
- `render_stack` (@ `rich/traceback.py`) -> **O(2^N) [Recursive]**
- `write` (@ `rich/file_proxy.py`) -> **O(2^N) [Recursive]**
- `highlight` (@ `rich/highlighter.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Captures the start and end of JSON strings, handling escaped quotes JSON_STR = r"(?<![\\\w])(?P<str>b?\".*?(?<!\\)\")" JSON_WHITESPACE = {" ", "\n",...

### Highest Data Gravity (Database Complexity)
- `__init__` (@ `rich/console.py`) -> DB Complexity: **56**
- `print` (@ `tests/test_console.py`) -> DB Complexity: **51**
- `__init__` (@ `rich/progress.py`) -> DB Complexity: **39**
- `create` (@ `rich/markdown.py`) -> DB Complexity: **27**
- `_enable_redirect_io` (@ `rich/live.py`) -> DB Complexity: **26**
- `__init__` (@ `rich/logging.py`) -> DB Complexity: **18**
- `__init__` (@ `rich/_log_render.py`) -> DB Complexity: **15**
- `test_handler` (@ `tests/test_traceback.py`) -> DB Complexity: **12**
- `decode_line` (@ `rich/ansi.py`) -> DB Complexity: **11**
- `test_ansi_in_pretty_repr` (@ `tests/test_pretty.py`) -> DB Complexity: **10**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `rich` | 75 | 18782.9 | 17.09% | 19.31% |
| `tests` | 56 | 3272.5 | 3.76% | 0.0% |
| `examples` | 36 | 871.58 | 8.96% | 0.0% |
| `__monolith__` | 30 | 248.88 | 1.32% | 0.0% |
| `benchmarks` | 3 | 227.8 | 6.38% | 33.33% |
| `benchmarks/results/darrenburns-2022-mbp` | 177 | 190.68 | 0.03% | 0.0% |
| `rich/_unicode_data` | 2 | 72.2 | 6.19% | 0.0% |
| `benchmarks/results` | 1 | 25.3 | 0.0% | 0.0% |
| `questions` | 11 | 11.0 | 0.0% | 0.0% |
| `imgs` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `rich/containers.py` -> **100.0%** Exposure
- `rich/markdown.py` -> **99.9999%** Exposure
- `rich/prompt.py` -> **99.9986%** Exposure
- `rich/_windows.py` -> **99.9871%** Exposure
- `benchmarks/benchmarks.py` -> **99.9792%** Exposure
### Highest State Flux (Mutation/Volatility)
- `rich/rule.py` -> **100.0%** Exposure
- `rich/spinner.py` -> **99.9999%** Exposure
- `rich/_log_render.py` -> **99.9998%** Exposure
- `rich/theme.py` -> **99.998%** Exposure
- `rich/status.py` -> **99.9957%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/test_text.py` -> **66** Orphaned Functions | **0** Duplicates
- `tests/test_console.py` -> **41** Orphaned Functions | **0** Duplicates
- `rich/markdown.py` -> **0** Orphaned Functions | **38** Duplicates
- `tests/test_progress.py` -> **34** Orphaned Functions | **0** Duplicates
- `tests/test_win32_console.py` -> **25** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`examples/table_movie.py`** -> AI Confidence: **99.39%**
2. **`rich/_inspect.py`** -> AI Confidence: **99.31%**
3. **`rich/_log_render.py`** -> AI Confidence: **99.31%**
4. **`rich/align.py`** -> AI Confidence: **99.31%**
5. **`rich/ansi.py`** -> AI Confidence: **99.31%**
6. **`rich/columns.py`** -> AI Confidence: **99.31%**
7. **`rich/console.py`** -> AI Confidence: **99.31%**
8. **`rich/live.py`** -> AI Confidence: **99.31%**
9. **`rich/markup.py`** -> AI Confidence: **99.31%**
10. **`rich/pretty.py`** -> AI Confidence: **99.31%**
11. **`rich/progress_bar.py`** -> AI Confidence: **99.31%**
12. **`rich/segment.py`** -> AI Confidence: **99.31%**
13. **`rich/style.py`** -> AI Confidence: **99.31%**
14. **`rich/syntax.py`** -> AI Confidence: **99.31%**
15. **`rich/table.py`** -> AI Confidence: **99.31%**
16. **`rich/text.py`** -> AI Confidence: **99.31%**
17. **`rich/traceback.py`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `tests/test_tree.py` -> **88.7233%** Exposure
- `tests/test_console.py` -> **0.0083%** Exposure
- `tests/test_cells.py` -> **0.0006%** Exposure
- `tests/test_rule.py` -> **0.0003%** Exposure
- `tests/test_control.py` -> **0.0002%** Exposure
### Exploit Generation Surface
- `benchmarks/benchmarks.py` -> **100.0%** Exposure
- `rich/_inspect.py` -> **100.0%** Exposure
- `rich/_log_render.py` -> **100.0%** Exposure
- `rich/_win32_console.py` -> **100.0%** Exposure
- `rich/_wrap.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `tools/make_width_tables.py` -> **100.0%** Exposure
- `rich/_win32_console.py` -> **27.301%** Exposure
### Algorithmic DoS Exposure
- `benchmarks/benchmarks.py` -> **100.0%** Exposure
- `examples/listdir.py` -> **100.0%** Exposure
- `examples/print_calendar.py` -> **100.0%** Exposure
- `examples/tree.py` -> **100.0%** Exposure
- `rich/_inspect.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `794` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `rich/text.py` (PYTHON) -> Cumulative Risk: **739.6**
- **Archetype:** `file_cluster_16` (Distance: 11.535 IQR)
- **Magnitude:** 1108.04 | **LOC:** 1364 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `divide` (Impact: 112.7), `markup` (Impact: 70.5), `expand_tabs` (Impact: 68.5)

### 2. `rich/prompt.py` (PYTHON) -> Cumulative Risk: **738.56**
- **Archetype:** `file_cluster_16` (Distance: 11.521 IQR)
- **Magnitude:** 201.26 | **LOC:** 401 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `process_response` (Impact: 37.4), `__call__` (Impact: 34.3), `make_prompt` (Impact: 22.0)

### 3. `rich/console.py` (PYTHON) -> Cumulative Risk: **731.09**
- **Archetype:** `file_cluster_16` (Distance: 12.411 IQR)
- **Magnitude:** 2334.52 | **LOC:** 2685 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (93.7856%)
- **Heaviest Functions:** `__init__` (Impact: 1819.6), `_is_jupyter` (Impact: 19.1), `stringify` (Impact: 12.2)

### 4. `rich/align.py` (PYTHON) -> Cumulative Risk: **728.31**
- **Archetype:** `file_cluster_13` (Distance: 10.0 IQR)
- **Magnitude:** 190.36 | **LOC:** 321 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.999%)
- **Heaviest Functions:** `generate_segments` (Impact: 98.9), `blank_lines` (Impact: 18.2), `blank_lines` (Impact: 10.2)

### 5. `rich/live.py` (PYTHON) -> Cumulative Risk: **727.49**
- **Archetype:** `file_cluster_13` (Distance: 12.125 IQR)
- **Magnitude:** 797.22 | **LOC:** 405 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `stop` (Impact: 244.4), `refresh` (Impact: 195.7), `start` (Impact: 84.6)

### 6. `rich/markdown.py` (PYTHON) -> Cumulative Risk: **722.34**
- **Archetype:** `file_cluster_13` (Distance: 11.437 IQR)
- **Magnitude:** 1165.72 | **LOC:** 794 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `create` (Impact: 857.6), `create` (Impact: 24.8), `render_bullet` (Impact: 16.6)

### 7. `rich/repr.py` (PYTHON) -> Cumulative Risk: **720.88**
- **Archetype:** `file_cluster_16` (Distance: 10.41 IQR)
- **Magnitude:** 332.54 | **LOC:** 150 | **CtrlFlow:** 45.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.6101%)
- **Heaviest Functions:** `do_replace` (Impact: 308.3), `auto` (Impact: 2.1), `auto` (Impact: 1.8)

### 8. `rich/progress.py` (PYTHON) -> Cumulative Risk: **719.72**
- **Archetype:** `file_cluster_16` (Distance: 11.535 IQR)
- **Magnitude:** 3542.0 | **LOC:** 1717 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (98.3355%)
- **Heaviest Functions:** `__init__` (Impact: 3032.4), `__call__` (Impact: 32.0), `render` (Impact: 21.1)

### 9. `rich/cells.py` (PYTHON) -> Cumulative Risk: **717.68**
- **Archetype:** `file_cluster_16` (Distance: 11.089 IQR)
- **Magnitude:** 193.26 | **LOC:** 353 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9957%)
- **Heaviest Functions:** `_cell_len` (Impact: 49.6), `get_character_cell_size` (Impact: 32.4), `set_cell_size` (Impact: 24.9)

### 10. `rich/file_proxy.py` (PYTHON) -> Cumulative Risk: **706.54**
- **Archetype:** `file_cluster_13` (Distance: 11.776 IQR)
- **Magnitude:** 127.3 | **LOC:** 58 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `write` (Impact: 84.2), `flush` (Impact: 7.2), `fileno` (Impact: 5.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `rich/progress.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.535 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.316 IQR)
- **Top Global Matches:** file_cluster_16: 11.535, file_cluster_13: 11.723, file_cluster_8: 11.972
- **Magnitude:** 3542.0 | **LOC:** 1717 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (19.6703%), Tech Debt (93.4353%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 3032.4 | O(2^N) | DB: 39)
  * `__call__` (Impact: 32.0 | O(N^5))
  * `render` (Impact: 21.1 | O(2^N))
  * `run` (Impact: 18.0 | O(N^4) | DB: 1)
  * `render` (Impact: 18.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 265`, `args: 96`, `func_start: 96`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 114`, `duplicate_logic: 23`
* *Architecture:* `io: 8`, `api: 92`, `concurrency: 1`, `import: 34`
* *Defense:* `safety: 9`, `doc: 162`, `test: 1`, `sync_locks: 6`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.139
  * `Choke Point (Betweenness):` 0.001645 | `Ripple Effect (Closeness):` 0.020101
  * `Imports (Out-Degree: 11):` .panel, threading, datetime, types, abc, .text, mmap, io...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `rich/console.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.411 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.411 IQR)
- **Top Global Matches:** file_cluster_16: 12.411, file_cluster_13: 12.469, file_cluster_0: 12.755
- **Magnitude:** 2334.52 | **LOC:** 2685 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 56
- **Risk Profile:** Cognitive Load (28.3305%), Tech Debt (92.7955%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 1819.6 | O(N^5) | DB: 56)
  * `_is_jupyter` (Impact: 19.1 | O(N^2) | DB: 3)
  * `stringify` (Impact: 12.2 | O(N^5))
  * `get_windows_console_features` (Impact: 10.8 | O(2^N) | DB: 1)
  * `__enter__` (Impact: 10.6 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 351`, `structural_boundaries: 355`, `args: 116`, `func_start: 116`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 213`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 22`
* *Architecture:* `io: 22`, `api: 98`, `concurrency: 14`, `import: 54`
* *Defense:* `safety: 51`, `doc: 236`, `test: 4`, `sync_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 104.767
  * `Choke Point (Betweenness):` 0.035788 | `Ripple Effect (Closeness):` 0.287036
  * `Imports (Out-Degree: 33):` ._log_render, html, threading, ._export_format, inspect, .markup, .emoji, datetime...
  * `Imported By (In-Degree: 108):` (Excluded from Brief to save tokens)

### `rich/pretty.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.508 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.224 IQR)
- **Top Global Matches:** file_cluster_16: 10.508, file_cluster_13: 10.522, file_cluster_8: 10.66
- **Magnitude:** 1521.62 | **LOC:** 1017 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (11.1317%), Tech Debt (38.3079%)
**Top Internal Functions/Classes:**
  * `_traverse` (Impact: 1062.7 | O(2^N))
  * `iter_tokens` (Impact: 146.6 | O(2^N))
  * `expand` (Impact: 36.3 | O(N^4))
  * `to_repr` (Impact: 30.8 | O(N^4))
  * `display_hook` (Impact: 29.1 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 154`, `args: 44`, `func_start: 34`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 18`, `duplicate_logic: 6`
* *Architecture:* `io: 3`, `api: 27`, `import: 31`
* *Defense:* `safety: 40`, `doc: 48`, `test: 5`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.234
  * `Choke Point (Betweenness):` 0.001421 | `Ripple Effect (Closeness):` 0.16574
  * `Imports (Out-Degree: 9):` reprlib, .cells, inspect, types, array, .text, .measure, ._loop...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `rich/markdown.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.437 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.924 IQR)
- **Top Global Matches:** file_cluster_13: 11.437, file_cluster_16: 11.541, file_cluster_0: 11.779
- **Magnitude:** 1165.72 | **LOC:** 794 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (23.3373%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 857.6 | O(2^N) | DB: 27)
  * `create` (Impact: 24.8 | O(N^3))
  * `render_bullet` (Impact: 16.6 | O(N^3) | DB: 1)
  * `on_child_close` (Impact: 16.4 | O(N^3) | DB: 2)
  * `create` (Impact: 9.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 159`, `args: 57`, `func_start: 57`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 67`, `duplicate_logic: 38`
* *Architecture:* `io: 2`, `api: 51`, `import: 23`
* *Defense:* `safety: 17`, `doc: 58`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.102
  * `Choke Point (Betweenness):` 0.001016 | `Ripple Effect (Closeness):` 0.11342
  * `Imports (Out-Degree: 11):` argparse, .segment, .text, markdown_it, io, rich.console, ._loop, .jupyter...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `rich/text.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.535 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.288 IQR)
- **Top Global Matches:** file_cluster_16: 11.535, file_cluster_13: 11.702, file_cluster_8: 11.852
- **Magnitude:** 1108.04 | **LOC:** 1364 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (24.6541%), Tech Debt (94.2518%)
**Top Internal Functions/Classes:**
  * `divide` (Impact: 112.7 | O(N^6))
  * `markup` (Impact: 70.5 | O(2^N))
  * `expand_tabs` (Impact: 68.5 | O(N^6) | DB: 2)
  * `render` (Impact: 67.6 | O(N^4))
  * `align` (Impact: 56.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 179`, `args: 65`, `func_start: 65`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 109`, `planned_debt: 2`, `duplicate_logic: 12`
* *Architecture:* `api: 74`, `import: 22`
* *Defense:* `safety: 16`, `doc: 112`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 44.177
  * `Choke Point (Betweenness):` 0.007499 | `Ripple Effect (Closeness):` 0.214977
  * `Imports (Out-Degree: 15):` .cells, .markup, .emoji, .segment, .measure, .align, rich.console, ._loop...
  * `Imported By (In-Degree: 54):` (Excluded from Brief to save tokens)

### `rich/live.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.125 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.977 IQR)
- **Top Global Matches:** file_cluster_13: 12.125, file_cluster_16: 12.567, file_cluster_11: 12.614
- **Magnitude:** 797.22 | **LOC:** 405 | **CtrlFlow:** 50.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (31.6856%), Tech Debt (72.8766%)
**Top Internal Functions/Classes:**
  * `stop` (Impact: 244.4 | O(2^N) | DB: 3)
  * `refresh` (Impact: 195.7 | O(2^N) | DB: 1)
  * `start` (Impact: 84.6 | O(2^N) | DB: 4)
  * `renderable` (Impact: 49.0 | O(2^N))
    * *Intent:* """Disable redirecting of stdout / stderr."""
  * `_enable_redirect_io` (Impact: 30.8 | O(N^4) | DB: 26)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 86`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 82`, `dead_code: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 10`, `api: 15`, `concurrency: 1`, `import: 28`
* *Defense:* `safety: 11`, `doc: 26`, `test: 1`, `sync_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.086
  * `Choke Point (Betweenness):` 0.002524 | `Ripple Effect (Closeness):` 0.167907
  * `Imports (Out-Degree: 10):` ipywidgets, .panel, threading, types, .text, .align, .live, random...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `rich/style.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.715 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.075 IQR)
- **Top Global Matches:** file_cluster_16: 10.715, file_cluster_13: 11.028, file_cluster_0: 11.071
- **Magnitude:** 764.46 | **LOC:** 793 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (36.1135%), Tech Debt (17.7747%)
**Top Internal Functions/Classes:**
  * `_make_ansi_codes` (Impact: 333.4 | O(N^6) | DB: 4)
  * `__str__` (Impact: 251.7 | O(N^5) | DB: 1)
  * `copy` (Impact: 14.8 | O(N^3))
  * `on` (Impact: 13.7 | O(N^2) | DB: 1)
  * `_make_color` (Impact: 10.5 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 112`, `args: 38`, `func_start: 38`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 43`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 35`, `import: 10`
* *Defense:* `safety: 9`, `doc: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 36.843
  * `Choke Point (Betweenness):` 0.001097 | `Ripple Effect (Closeness):` 0.209712
  * `Imports (Out-Degree: 2):` , pickle, .repr, typing, random, operator, sys, functools...
  * `Imported By (In-Degree: 44):` (Excluded from Brief to save tokens)

### `rich/logging.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.732 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.421 IQR)
- **Top Global Matches:** file_cluster_13: 10.732, file_cluster_8: 10.978, file_cluster_16: 11.0
- **Magnitude:** 733.96 | **LOC:** 298 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (12.9735%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 683.5 | O(2^N) | DB: 18)
  * `divide` (Impact: 14.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 39`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 26`
* *Architecture:* `io: 1`, `api: 6`, `import: 14`
* *Defense:* `safety: 10`, `doc: 10`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.9
  * `Choke Point (Betweenness):` 0.00038 | `Ripple Effect (Closeness):` 0.124707
  * `Imports (Out-Degree: 5):` .text, ._log_render, rich._null_file, .traceback, pathlib, , .highlighter, typing...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `rich/traceback.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.529 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.79 IQR)
- **Top Global Matches:** file_cluster_13: 10.529, file_cluster_16: 10.676, file_cluster_0: 10.786
- **Magnitude:** 598.0 | **LOC:** 925 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (22.7627%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `render_stack` (Impact: 259.8 | O(2^N) | DB: 7)
  * `_render_stack` (Impact: 151.9 | O(N^6) | DB: 3)
  * `ipy_excepthook_closure` (Impact: 50.2 | O(N^5) | DB: 2)
  * `safe_str` (Impact: 10.3 | O(N^4))
  * `from_exception` (Impact: 7.9 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 109`, `args: 21`, `func_start: 20`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 51`, `dead_code: 2`
* *Architecture:* `io: 15`, `api: 21`, `import: 28`
* *Defense:* `safety: 24`, `doc: 18`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.451
  * `Choke Point (Betweenness):` 0.001417 | `Ripple Effect (Closeness):` 0.163109
  * `Imports (Out-Degree: 9):` traceback, .panel, pygments.lexers, inspect, types, .text, .constrain, pygments.token...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `rich/syntax.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.849 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.861 IQR)
- **Top Global Matches:** file_cluster_13: 10.849, file_cluster_16: 10.911, file_cluster_8: 11.031
- **Magnitude:** 498.52 | **LOC:** 986 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (14.6847%), Tech Debt (65.1355%)
**Top Internal Functions/Classes:**
  * `tokens_to_spans` (Impact: 61.8 | O(N^6))
  * `guess_lexer` (Impact: 55.4 | O(N^5) | DB: 3)
  * `_apply_stylized_ranges` (Impact: 48.1 | O(N^5))
  * `get_style_for_token` (Impact: 21.9 | O(N^5))
  * `get_style_for_token` (Impact: 21.8 | O(N^5))
    * *Intent:* # Styles form a hierarchy # e.g. ("foo", "bar", "baz") to ("foo", "bar") to ("foo",) get_style = sel...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 132`, `args: 31`, `func_start: 31`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 69`, `duplicate_logic: 9`
* *Architecture:* `io: 5`, `api: 25`, `import: 28`
* *Defense:* `safety: 20`, `doc: 56`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.731
  * `Choke Point (Betweenness):` 0.001307 | `Ripple Effect (Closeness):` 0.136285
  * `Imports (Out-Degree: 12):` argparse, rich.padding, .cells, pygments.lexers, .segment, abc, .text, pygments.token...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `rich/color.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.369 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.104 IQR)
- **Top Global Matches:** file_cluster_13: 10.369, file_cluster_8: 10.412, file_cluster_16: 10.565
- **Magnitude:** 399.96 | **LOC:** 622 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (12.5625%), Tech Debt (20.0306%)
**Top Internal Functions/Classes:**
  * `downgrade` (Impact: 122.4 | O(N^5) | DB: 3)
  * `parse` (Impact: 85.7 | O(N^5))
  * `get_ansi_codes` (Impact: 70.6 | O(N^3))
  * `from_ansi` (Impact: 10.8 | O(N^3))
  * `system` (Impact: 7.2 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 124`, `args: 18`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `state_mutation: 25`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 30`, `import: 17`
* *Defense:* `safety: 15`, `doc: 46`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.734
  * `Choke Point (Betweenness):` 0.002658 | `Ripple Effect (Closeness):` 0.17476
  * `Imports (Out-Degree: 6):` .text, re, .color_triplet, .repr, .console, typing, ._palettes, .style...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `rich/segment.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.832 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.57 IQR)
- **Top Global Matches:** file_cluster_16: 9.832, file_cluster_13: 10.072, file_cluster_7: 10.174
- **Magnitude:** 372.9 | **LOC:** 784 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (23.6434%), Tech Debt (41.7012%)
**Top Internal Functions/Classes:**
  * `_split_cells` (Impact: 61.8 | O(N^5))
  * `split_lines` (Impact: 55.6 | O(N^6))
  * `simplify` (Impact: 32.1 | O(N^5))
  * `strip_links` (Impact: 30.8 | O(N^4))
    * *Intent:* """ _height = height or len(lines) blank = ( [cls(" " * width + "\n", style)] if new_lines else [cls...
  * `remove_color` (Impact: 26.7 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 94`, `args: 28`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 13`, `duplicate_logic: 4`
* *Architecture:* `api: 42`, `import: 13`
* *Defense:* `safety: 3`, `doc: 56`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.133
  * `Choke Point (Betweenness):` 0.003089 | `Ripple Effect (Closeness):` 0.188203
  * `Imports (Out-Degree: 6):` .cells, itertools, rich.console, .console, typing, .style, operator, enum...
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `tests/test_progress.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.708 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.059 IQR)
- **Top Global Matches:** file_cluster_8: 11.708, file_cluster_13: 11.824, file_cluster_16: 11.983
- **Magnitude:** 372.34 | **LOC:** 691 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (4.477%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_wrap_file_task_total` (Impact: 37.6 | O(N^5) | DB: 10)
  * `test_wrap_file` (Impact: 26.8 | O(N^4) | DB: 10)
  * `test_progress_track` (Impact: 21.0 | O(N^3))
  * `test_progress_max_refresh` (Impact: 19.3 | O(N^3) | DB: 2)
  * `test_open` (Impact: 18.4 | O(N^3) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 167`, `args: 44`, `func_start: 44`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 27`, `orphaned_logic: 34`
* *Architecture:* `io: 12`, `api: 44`, `import: 13`
* *Defense:* `safety: 89`, `doc: 4`, `test: 111`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` tempfile, io, rich.console, rich.highlighter, pytest, rich.progress_bar, os, .render...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_text.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.252 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.968 IQR)
- **Top Global Matches:** file_cluster_8: 12.252, file_cluster_0: 12.66, file_cluster_13: 12.661
- **Magnitude:** 362.92 | **LOC:** 1130 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (2.6064%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_render` (Impact: 28.9 | O(N^4) | DB: 1)
  * `test_append_tokens` (Impact: 18.3 | O(N^4))
  * `test_soft_wrap` (Impact: 9.2 | O(N^2))
    * *Intent:* """Regression text for https://github.com/Textualize/rich/issues/3479"""
  * `test_append` (Impact: 8.4 | O(N^2) | DB: 4)
  * `test_highlight_regex` (Impact: 6.8 | O(N^3))
    * *Intent:* # As a string text = Text("peek-a-boo") count = text.highlight_regex(r"NEVER_MATCH", "red") assert c...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 345`, `args: 92`, `func_start: 92`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 31`, `orphaned_logic: 66`
* *Architecture:* `api: 92`, `import: 8`
* *Defense:* `safety: 235`, `doc: 32`, `test: 334`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` re, rich.style, io, rich.measure, rich.console, typing, pytest, rich.text
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rich/_inspect.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.995 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.483 IQR)
- **Top Global Matches:** file_cluster_13: 11.995, file_cluster_16: 12.175, file_cluster_12: 12.362
- **Magnitude:** 362.54 | **LOC:** 273 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^6) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (48.2124%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_render` (Impact: 210.8 | O(N^6) | DB: 2)
  * `_get_signature` (Impact: 52.1 | O(N^4))
  * `_make_title` (Impact: 17.8 | O(N^3))
  * `_get_formatted_doc` (Impact: 10.9 | O(N^3))
  * `get_object_types_mro_as_strings` (Impact: 6.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 58`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 36`
* *Architecture:* `api: 9`, `concurrency: 1`, `import: 11`
* *Defense:* `safety: 16`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.805
  * `Choke Point (Betweenness):` 0.000263 | `Ripple Effect (Closeness):` 0.005025
  * `Imports (Out-Degree: 6):` .text, .control, .panel, .highlighter, typing, inspect, .pretty, .table...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `rich/markup.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.813 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.426 IQR)
- **Top Global Matches:** file_cluster_13: 9.813, file_cluster_16: 9.962, file_cluster_8: 10.155
- **Magnitude:** 351.2 | **LOC:** 252 | **CtrlFlow:** 55.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (10.2585%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `escape` (Impact: 312.3 | O(N^6) | DB: 5)
  * `markup` (Impact: 10.8 | O(N^3))
  * `__str__` (Impact: 10.6 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 43`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 6`
* *Architecture:* `io: 1`, `api: 8`, `import: 11`
* *Defense:* `safety: 8`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.617
  * `Choke Point (Betweenness):` 0.002272 | `Ripple Effect (Closeness):` 0.165207
  * `Imports (Out-Degree: 6):` .text, re, .emoji, typing, rich.table, ast, .style, operator...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `tests/test_console.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.771 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.836 IQR)
- **Top Global Matches:** file_cluster_8: 10.771, file_cluster_13: 10.782, file_cluster_16: 10.849
- **Magnitude:** 344.08 | **LOC:** 1130 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 51
- **Risk Profile:** Cognitive Load (3.6183%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `print` (Impact: 104.5 | O(2^N) | DB: 51)
  * `test_console_options_update` (Impact: 14.1 | O(N^2) | DB: 3)
  * `test_capture` (Impact: 10.7 | O(N^3))
  * `get_terminal_size_mock_impl` (Impact: 10.3 | O(N^3) | DB: 9)
  * `test_get_style_error` (Impact: 8.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 169`, `args: 55`, `func_start: 71`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 92`, `state_mutation: 17`, `orphaned_logic: 41`
* *Architecture:* `io: 27`, `api: 55`, `import: 24`
* *Defense:* `safety: 61`, `doc: 16`, `test: 195`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` rich.style, rich.padding, datetime, rich._null_file, io, rich.console, rich.control, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rich/repr.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.41 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.902 IQR)
- **Top Global Matches:** file_cluster_16: 10.41, file_cluster_13: 10.638, file_cluster_0: 10.686
- **Magnitude:** 332.54 | **LOC:** 150 | **CtrlFlow:** 45.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (26.171%), Tech Debt (99.0462%)
**Top Internal Functions/Classes:**
  * `do_replace` (Impact: 308.3 | O(2^N) | DB: 2)
  * `auto` (Impact: 2.1 | O(N^1))
  * `auto` (Impact: 1.8 | O(N^1))
  * `auto` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 29`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 6`, `duplicate_logic: 3`
* *Architecture:* `api: 11`, `import: 4`
* *Defense:* `safety: 8`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.191
  * `Choke Point (Betweenness):` 0.000373 | `Ripple Effect (Closeness):` 0.1152
  * `Imports (Out-Degree: 1):` inspect, rich.console, functools, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `rich/ansi.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.803 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.978 IQR)
- **Top Global Matches:** file_cluster_13: 8.803, file_cluster_8: 8.864, file_cluster_7: 9.035
- **Magnitude:** 256.18 | **LOC:** 242 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (7.1335%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `decode_line` (Impact: 174.6 | O(N^6) | DB: 11)
  * `_ansi_tokenize` (Impact: 56.1 | O(N^4))
  * `decode` (Impact: 7.2 | O(N^3))
  * `__init__` (Impact: 2.7 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 28`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `io: 3`, `api: 5`, `import: 12`
* *Defense:* `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.275
  * `Choke Point (Betweenness):` 0.000126 | `Ripple Effect (Closeness):` 0.135924
  * `Imports (Out-Degree: 4):` .text, re, io, pty, typing, os, .style, contextlib...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tests/test_traceback.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.081 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.686 IQR)
- **Top Global Matches:** file_cluster_8: 12.081, file_cluster_0: 12.269, file_cluster_13: 12.278
- **Magnitude:** 246.78 | **LOC:** 400 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (2.5184%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_handler` (Impact: 50.9 | O(N^6) | DB: 12)
  * `test_nested_exception` (Impact: 15.1 | O(N^3))
  * `test_caused_exception` (Impact: 15.1 | O(N^3))
  * `test_traceback_console_theme_applies` (Impact: 12.4 | O(N^3))
    * *Intent:* """ Ensure that themes supplied via Console init work on Tracebacks. Regression test for https://git...
  * `test_recursive_exception` (Impact: 11.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 99`, `args: 35`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `orphaned_logic: 21`
* *Architecture:* `io: 9`, `api: 35`, `import: 8`
* *Defense:* `safety: 88`, `doc: 12`, `test: 69`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` re, io, rich.traceback, rich.console, typing, pytest, rich.theme, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/downloader.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.513 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.643 IQR)
- **Top Global Matches:** file_cluster_13: 9.513, file_cluster_8: 9.898, file_cluster_4: 10.198
- **Magnitude:** 241.64 | **LOC:** 82 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (15.9933%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 21`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 5`, `api: 3`, `concurrency: 3`, `import: 9`
* *Defense:* `doc: 6`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` concurrent.futures, signal, threading, typing, urllib.request, rich.progress, os.path, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rich/_win32_console.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.753 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.939 IQR)
- **Top Global Matches:** file_cluster_8: 9.753, file_cluster_16: 9.818, file_cluster_7: 9.998
- **Magnitude:** 218.78 | **LOC:** 662 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (5.435%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `write_styled` (Impact: 61.7 | O(N^4))
    * *Intent:* """Set the cursor info - used for adjusting cursor visibility and width Args: std_handle (wintypes.H...
  * `move_cursor_forward` (Impact: 11.0 | O(N^3))
  * `move_cursor_backward` (Impact: 11.0 | O(N^3))
  * `move_cursor_to` (Impact: 10.7 | O(N^3))
  * `GetConsoleMode` (Impact: 6.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 68`, `args: 29`, `func_start: 29`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 8`
* *Architecture:* `io: 2`, `api: 36`, `import: 9`
* *Defense:* `safety: 3`, `doc: 62`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.452
  * `Choke Point (Betweenness):` 0.001138 | `Ripple Effect (Closeness):` 0.164151
  * `Imports (Out-Degree: 3):` rich.style, ctypes, rich.console, typing, sys, time, rich.color
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `benchmarks/benchmarks.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.781 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.563 IQR)
- **Top Global Matches:** file_cluster_8: 9.781, file_cluster_13: 9.904, file_cluster_7: 10.436
- **Magnitude:** 216.28 | **LOC:** 219 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (14.1453%), Tech Debt (99.9792%)
**Top Internal Functions/Classes:**
  * `setup` (Impact: 8.2 | O(2^N) | DB: 4)
  * `time_wrapping_unicode_heavy_warm_cache` (Impact: 7.1 | O(N^3))
  * `_print_table` (Impact: 4.6 | O(N^3))
  * `setup` (Impact: 3.9 | O(N^3) | DB: 1)
  * `setup` (Impact: 3.8 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 72`, `args: 43`, `func_start: 43`, `class_start: 9`
* *Risk/State:* `state_mutation: 15`, `duplicate_logic: 7`
* *Architecture:* `api: 76`, `import: 10`
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` rich.style, io, rich.console, rich.pretty, benchmarks, rich.table, rich.segment, rich.syntax...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rich/_log_render.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.985 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.372 IQR)
- **Top Global Matches:** file_cluster_13: 10.985, file_cluster_16: 11.162, file_cluster_8: 11.222
- **Magnitude:** 209.22 | **LOC:** 95 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (79.1391%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 174.6 | O(N^5) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 20`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 31`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.634
  * `Choke Point (Betweenness):` 0.000133 | `Ripple Effect (Closeness):` 0.160561
  * `Imports (Out-Degree: 3):` .text, rich.console, typing, .containers, datetime, .table, .console
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/test_pretty.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.436 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.106 IQR)
- **Top Global Matches:** file_cluster_0: 11.436, file_cluster_16: 11.457, file_cluster_8: 11.544
- **Magnitude:** 207.42 | **LOC:** 760 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (2.2411%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_ansi_in_pretty_repr` (Impact: 30.4 | O(N^3) | DB: 10)
  * `test_dataclass_no_attribute` (Impact: 6.1 | O(N^2))
    * *Intent:* """ Test that can use None as key to have tuple positional values and with a default. """
  * `test_ipy_display_hook__special_repr_rais` (Impact: 4.5 | O(N^3))
    * *Intent:* # should be repr as-is
  * `test_ipy_display_hook__multiple_special_` (Impact: 4.3 | O(N^3))
    * *Intent:* """ The case where there are multiple IPython special _repr_*_ methods on the object, and one of the...
  * `test_user_dict` (Impact: 4.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 234`, `args: 77`, `func_start: 77`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 7`, `orphaned_logic: 23`
* *Architecture:* `io: 21`, `api: 85`, `import: 14`
* *Defense:* `safety: 88`, `doc: 22`, `test: 140`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` array, io, rich.measure, rich.console, rich.pretty, typing, pytest, attr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/test_pretty.py` (PYTHON) | Magnitude: 207.42 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 450, structural_boundaries: 234, test: 140, safety: 88
- `tests/test_repr.py` (PYTHON) | Magnitude: 106.46 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 51, state_mutation: 21, test: 20
- `tests/test_inspect.py` (PYTHON) | Magnitude: 160.86 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 321, structural_boundaries: 121, test: 53, args: 51

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/test_theme.py` (PYTHON) | Magnitude: 28.2 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 23, test: 15, safety: 8
- `rich/theme.py` (PYTHON) | Magnitude: 72.56 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 21, state_mutation: 19, doc: 16
- `tests/test_file_proxy.py` (PYTHON) | Magnitude: 15.96 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 14, test: 10, import: 5
- `examples/recursive_error.py` (PYTHON) | Magnitude: 5.8 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 4, args: 2, func_start: 2
- `rich/align.py` (PYTHON) | Magnitude: 190.36 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 230, structural_boundaries: 53, branch: 48, generics: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `rich/__init__.py` (PYTHON) | Magnitude: 23.1 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 73, structural_boundaries: 23, encapsulation: 20, doc: 12
- `rich/pretty.py` (PYTHON) | Magnitude: 1521.62 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 706, branch: 157, structural_boundaries: 154, encapsulation: 153
- `rich/scope.py` (PYTHON) | Magnitude: 12.48 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 23, generics: 11, import: 9
- `examples/exception.py` (PYTHON) | Magnitude: 19.0 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 7, doc: 6, branch: 3
- `rich/console.py` (PYTHON) | Magnitude: 2334.52 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1612, structural_boundaries: 355, branch: 351, encapsulation: 324

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/test_markdown.py` (PYTHON) | Magnitude: 27.28 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 25, doc: 20, sec_reflection_metaprogramming: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `rich/errors.py` (PYTHON) | Magnitude: 23.68 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 18, structural_boundaries: 9, class_start: 9, api: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `examples/attrs.py` (PYTHON) | Magnitude: 18.8 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 14, import: 6, branch: 3
- `tools/make_emoji.py` (PYTHON) | Magnitude: 0.01 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, branch: 3, safety: 2
- `tests/test_console.py` (PYTHON) | Magnitude: 344.08 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 689, test: 195, structural_boundaries: 169, sec_high_risk_execution: 131
- `tests/test_markup.py` (PYTHON) | Magnitude: 85.66 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 127, structural_boundaries: 90, test: 87, safety: 60
- `tests/test_live_render.py` (PYTHON) | Magnitude: 16.5 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 23, test: 15, safety: 8

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `rich/console.py` -> **Will McGugan** (100.0% isolated ownership) | Magnitude: 2334.52
- `rich/pretty.py` -> **Joel Ostblom** (100.0% isolated ownership) | Magnitude: 1521.62
- `rich/markdown.py` -> **Will McGugan** (100.0% isolated ownership) | Magnitude: 1165.72
- `rich/live.py` -> **Will McGugan** (100.0% isolated ownership) | Magnitude: 797.22
- `rich/style.py` -> **Will McGugan** (100.0% isolated ownership) | Magnitude: 764.46

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `rich/console.py` -> **Severity: 3.356** (Bridge: 0.0358 * Flux: 93.7856%)
- `rich/text.py` -> **Severity: 0.698** (Bridge: 0.0075 * Flux: 93.1368%)
- `rich/live.py` -> **Severity: 0.252** (Bridge: 0.0025 * Flux: 99.9819%)
- `rich/table.py` -> **Severity: 0.213** (Bridge: 0.003 * Flux: 71.6782%)
- `rich/align.py` -> **Severity: 0.17** (Bridge: 0.0018 * Flux: 92.3696%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `rich/jupyter.py` -> **Severity: 14.473** (Embedded: 0.1809 * Error Risk: 80.0%)
- `rich/_fileno.py` -> **Severity: 13.044** (Embedded: 0.163 * Error Risk: 80.0%)
- `rich/protocol.py` -> **Severity: 13.007** (Embedded: 0.1626 * Error Risk: 80.0%)
- `rich/_windows_renderer.py` -> **Severity: 12.926** (Embedded: 0.1616 * Error Risk: 80.0%)
- `rich/pager.py` -> **Severity: 12.845** (Embedded: 0.1606 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `rich/text.py` -> **Severity: 4417.7** (Blast Radius: 44.177 * Doc Risk: 100.0%)
- `rich/console.py` -> **Severity: 4401.063** (Blast Radius: 104.767 * Doc Risk: 42.0081%)
- `rich/style.py` -> **Severity: 3684.3** (Blast Radius: 36.843 * Doc Risk: 100.0%)
- `rich/segment.py` -> **Severity: 2613.3** (Blast Radius: 26.133 * Doc Risk: 100.0%)
- `rich/color.py` -> **Severity: 2498.969** (Blast Radius: 27.734 * Doc Risk: 90.1049%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
