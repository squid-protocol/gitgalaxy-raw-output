# ARCHITECTURAL_BRIEF: jinja2
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/jinja2` |
| **Timestamp** | `2026-08-03T21:21:51.667757+00:00` |
| **Scan Duration** | `0.46s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 49 malicious artifacts.

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
| Total Artifacts | 73 |
| Analyzed Artifacts (Scanned) | 54 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 19 |
| Total LOC | 14014 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 74.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2746 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1745 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 29.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.228 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 46 | 13998 | 85.2% |
| M4 | 3 | 9 | 5.6% |
| PLAINTEXT | 2 | 0 | 3.7% |
| HTML | 2 | 7 | 3.7% |
| MARKDOWN | 1 | 0 | 1.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.986`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 20 | 37.0% |
| file_cluster_8 | 13 | 24.1% |
| file_cluster_16 | 8 | 14.8% |
| file_cluster_2 | 8 | 14.8% |
| file_cluster_0 | 1 | 1.9% |
| file_cluster_17 | 1 | 1.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 5.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 19*

**Composition by Extension & Reason:**
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 152 LOC), 1x Excluded (Machine-Generated Source Code Signature: 29 LOC)
- `.py`: 1x Excluded (Saturation: Line 5 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 1207 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 2x Unsupported Format (.undeterminable)
- `.in`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.zip`: 1x Excluded (Explicitly Denied Extension: '.zip')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 52.5 | 11.2 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 25.0 | 0.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 20.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 25.4 | 0.2 | 0.0 |
| API Exposure | 0.0 | 13.6 | 6.3 | 6.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 13.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 24.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 17.8 | 2.3 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 85.6 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 36.4 | 0.8 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 69.0 | 99.9 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 31.4 | 0.6 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 64.7 | 100.0 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 3.9 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `jinja2-3.1.6/src/jinja2/loaders.py` (Hits: 47)
- `jinja2-3.1.6/src/jinja2/bccache.py` (Hits: 19)
- `jinja2-3.1.6/tests/test_loader.py` (Hits: 14)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **typing.in** (`jinja2-3.1.6/requirements/typing.in`) — 21 inbound connections
2. **exceptions.py** (`jinja2-3.1.6/src/jinja2/exceptions.py`) — 19 inbound connections
3. **environment.py** (`jinja2-3.1.6/src/jinja2/environment.py`) — 17 inbound connections
4. **runtime.py** (`jinja2-3.1.6/src/jinja2/runtime.py`) — 15 inbound connections
5. **utils.py** (`jinja2-3.1.6/src/jinja2/utils.py`) — 15 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **environment.py** (`jinja2-3.1.6/src/jinja2/environment.py`) — 25 outbound dependencies
2. **utils.py** (`jinja2-3.1.6/src/jinja2/utils.py`) — 20 outbound dependencies
3. **compiler.py** (`jinja2-3.1.6/src/jinja2/compiler.py`) — 19 outbound dependencies
4. **loaders.py** (`jinja2-3.1.6/src/jinja2/loaders.py`) — 18 outbound dependencies
5. **filters.py** (`jinja2-3.1.6/src/jinja2/filters.py`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `visit_For` (@ `jinja2-3.1.6/src/jinja2/compiler.py`) -> Impact: **258.9** | LOC: 138
- `__init__` (@ `jinja2-3.1.6/src/jinja2/bccache.py`) -> Impact: **226.8** | LOC: 135
- `parse` (@ `jinja2-3.1.6/src/jinja2/ext.py`) -> Impact: **188.0** | LOC: 122
- `url_quote` (@ `jinja2-3.1.6/src/jinja2/utils.py`) -> Impact: **187.9** | LOC: 279
- `visit_Output` (@ `jinja2-3.1.6/src/jinja2/compiler.py`) -> Impact: **159.9** | LOC: 78
- `do_filesizeformat` (@ `jinja2-3.1.6/src/jinja2/filters.py`) -> Impact: **135.6** | LOC: 28
- `test_env_async` (@ `jinja2-3.1.6/tests/test_async.py`) -> Impact: **125.8** | LOC: 438
- `test_comment_syntax` (@ `jinja2-3.1.6/tests/test_lexnparse.py`) -> Impact: **118.6** | LOC: 121
- `__call__` (@ `jinja2-3.1.6/src/jinja2/runtime.py`) -> Impact: **117.8** | LOC: 75
- `pop_assign_tracking` (@ `jinja2-3.1.6/src/jinja2/compiler.py`) -> Impact: **111.2** | LOC: 41

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `write` (@ `jinja2-3.1.6/src/jinja2/compiler.py`) -> **O(2^N) [Recursive]**
- `test_env_async` (@ `jinja2-3.1.6/tests/test_async.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `jinja2-3.1.6/src/jinja2/bccache.py`) -> **O(2^N) [Recursive]**
- `list_templates` (@ `jinja2-3.1.6/src/jinja2/loaders.py`) -> **O(2^N) [Recursive]**
- `enter_frame` (@ `jinja2-3.1.6/src/jinja2/meta.py`) -> **O(2^N) [Recursive]**
- `parse_condexpr` (@ `jinja2-3.1.6/src/jinja2/parser.py`) -> **O(2^N) [Recursive]**
- `_log_message` (@ `jinja2-3.1.6/src/jinja2/runtime.py`) -> **O(2^N) [Recursive]**
- `super` (@ `jinja2-3.1.6/src/jinja2/runtime.py`) -> **O(2^N) [Recursive]**
- `test_env` (@ `jinja2-3.1.6/tests/test_imports.py`) -> **O(2^N) [Recursive]**
- `getattr` (@ `jinja2-3.1.6/src/jinja2/environment.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `__init__` (@ `jinja2-3.1.6/src/jinja2/bccache.py`) -> DB Complexity: **54**
- `list_templates` (@ `jinja2-3.1.6/src/jinja2/loaders.py`) -> DB Complexity: **26**
- `url_quote` (@ `jinja2-3.1.6/src/jinja2/utils.py`) -> DB Complexity: **19**
- `test_import_as_with_context_deterministi` (@ `jinja2-3.1.6/tests/test_compile.py`) -> DB Complexity: **16**
- `split_template_path` (@ `jinja2-3.1.6/src/jinja2/loaders.py`) -> DB Complexity: **13**
- `list_templates` (@ `jinja2-3.1.6/src/jinja2/loaders.py`) -> DB Complexity: **12**
- `test_pep_451_import_hook` (@ `jinja2-3.1.6/tests/test_loader.py`) -> DB Complexity: **10**
- `teardown_method` (@ `jinja2-3.1.6/tests/test_loader.py`) -> DB Complexity: **9**
- `compile_down` (@ `jinja2-3.1.6/tests/test_loader.py`) -> DB Complexity: **7**
- `test_weak_references` (@ `jinja2-3.1.6/tests/test_loader.py`) -> DB Complexity: **7**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `jinja2-3.1.6/src/jinja2` | 23 | 7954.76 | 20.11% | 45.29% |
| `jinja2-3.1.6/tests` | 22 | 3480.0 | 3.66% | 0.0% |
| `jinja2-3.1.6/requirements` | 3 | 34.68 | 5.0% | 0.0% |
| `jinja2-3.1.6/tests/res/templates` | 3 | 24.64 | 3.33% | 0.0% |
| `jinja2-3.1.6/tests/res` | 1 | 10.52 | 5.0% | 0.0% |
| `jinja2-3.1.6` | 2 | 2.16 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `jinja2-3.1.6/src/jinja2/exceptions.py` -> **100.0%** Exposure
- `jinja2-3.1.6/src/jinja2/loaders.py` -> **100.0%** Exposure
- `jinja2-3.1.6/src/jinja2/runtime.py` -> **100.0%** Exposure
- `jinja2-3.1.6/src/jinja2/bccache.py` -> **99.9976%** Exposure
- `jinja2-3.1.6/src/jinja2/visitor.py` -> **99.9955%** Exposure
### Highest State Flux (Mutation/Volatility)
- `jinja2-3.1.6/src/jinja2/exceptions.py` -> **99.9951%** Exposure
- `jinja2-3.1.6/src/jinja2/runtime.py` -> **99.7572%** Exposure
- `jinja2-3.1.6/src/jinja2/loaders.py` -> **98.8931%** Exposure
- `jinja2-3.1.6/src/jinja2/visitor.py` -> **95.9865%** Exposure
- `jinja2-3.1.6/src/jinja2/parser.py` -> **95.7672%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `jinja2-3.1.6/tests/test_filters.py` -> **77** Orphaned Functions | **5** Duplicates
- `jinja2-3.1.6/src/jinja2/runtime.py` -> **0** Orphaned Functions | **44** Duplicates
- `jinja2-3.1.6/tests/test_lexnparse.py` -> **43** Orphaned Functions | **0** Duplicates
- `jinja2-3.1.6/tests/test_loader.py` -> **34** Orphaned Functions | **6** Duplicates
- `jinja2-3.1.6/tests/test_core_tags.py` -> **32** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`jinja2-3.1.6/src/jinja2/compiler.py`** -> AI Confidence: **99.31%**
2. **`jinja2-3.1.6/src/jinja2/ext.py`** -> AI Confidence: **99.24%**
3. **`jinja2-3.1.6/src/jinja2/filters.py`** -> AI Confidence: **99.24%**
4. **`jinja2-3.1.6/src/jinja2/lexer.py`** -> AI Confidence: **99.24%**
5. **`jinja2-3.1.6/src/jinja2/loaders.py`** -> AI Confidence: **99.24%**
6. **`jinja2-3.1.6/src/jinja2/nativetypes.py`** -> AI Confidence: **99.18%**
7. **`jinja2-3.1.6/src/jinja2/runtime.py`** -> AI Confidence: **99.18%**
8. **`jinja2-3.1.6/src/jinja2/bccache.py`** -> AI Confidence: **99.16%**
9. **`jinja2-3.1.6/src/jinja2/environment.py`** -> AI Confidence: **99.16%**
10. **`jinja2-3.1.6/src/jinja2/sandbox.py`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `jinja2-3.1.6/tests/test_api.py` -> **31.3907%** Exposure
### Exploit Generation Surface
- `jinja2-3.1.6/src/jinja2/bccache.py` -> **100.0%** Exposure
- `jinja2-3.1.6/src/jinja2/compiler.py` -> **100.0%** Exposure
- `jinja2-3.1.6/src/jinja2/environment.py` -> **100.0%** Exposure
- `jinja2-3.1.6/src/jinja2/ext.py` -> **100.0%** Exposure
- `jinja2-3.1.6/src/jinja2/filters.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `jinja2-3.1.6/src/jinja2/debug.py` -> **100.0%** Exposure
- `jinja2-3.1.6/tests/test_loader.py` -> **100.0%** Exposure
- `jinja2-3.1.6/tests/test_regression.py` -> **0.0008%** Exposure
### Algorithmic DoS Exposure
- `jinja2-3.1.6/src/jinja2/bccache.py` -> **100.0%** Exposure
- `jinja2-3.1.6/src/jinja2/compiler.py` -> **100.0%** Exposure
- `jinja2-3.1.6/src/jinja2/ext.py` -> **100.0%** Exposure
- `jinja2-3.1.6/src/jinja2/idtracking.py` -> **100.0%** Exposure
- `jinja2-3.1.6/src/jinja2/lexer.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `270` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `jinja2-3.1.6/src/jinja2/runtime.py` (PYTHON) -> Cumulative Risk: **962.02**
- **Archetype:** `file_cluster_13` (Distance: 12.732 IQR)
- **Magnitude:** 831.04 | **LOC:** 1063 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `__call__` (Impact: 117.8), `__anext__` (Impact: 24.6), `_log_message` (Impact: 21.3)

### 2. `jinja2-3.1.6/src/jinja2/visitor.py` (PYTHON) -> Cumulative Risk: **848.97**
- **Archetype:** `file_cluster_13` (Distance: 12.743 IQR)
- **Magnitude:** 125.98 | **LOC:** 93 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `generic_visit` (Impact: 79.3), `visit` (Impact: 9.4), `visit_list` (Impact: 9.4)

### 3. `jinja2-3.1.6/src/jinja2/exceptions.py` (PYTHON) -> Cumulative Risk: **841.88**
- **Archetype:** `file_cluster_13` (Distance: 14.474 IQR)
- **Magnitude:** 94.54 | **LOC:** 167 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Logic Bomb (99.9999%), State Flux (99.9951%)
- **Heaviest Functions:** `__str__` (Impact: 31.4), `message` (Impact: 7.9), `__init__` (Impact: 5.3)

### 4. `jinja2-3.1.6/src/jinja2/idtracking.py` (PYTHON) -> Cumulative Risk: **820.28**
- **Archetype:** `file_cluster_16` (Distance: 10.418 IQR)
- **Magnitude:** 384.38 | **LOC:** 319 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `branch_update` (Impact: 32.3), `store` (Impact: 21.6), `dump_stores` (Impact: 21.4)

### 5. `jinja2-3.1.6/src/jinja2/bccache.py` (PYTHON) -> Cumulative Risk: **806.31**
- **Archetype:** `file_cluster_13` (Distance: 12.784 IQR)
- **Magnitude:** 373.92 | **LOC:** 409 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9976%)
- **Heaviest Functions:** `__init__` (Impact: 226.8), `dump_bytecode` (Impact: 22.3), `load_bytecode` (Impact: 17.7)

### 6. `jinja2-3.1.6/src/jinja2/compiler.py` (PYTHON) -> Cumulative Risk: **786.71**
- **Archetype:** `file_cluster_16` (Distance: 12.211 IQR)
- **Magnitude:** 1961.5 | **LOC:** 1999 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.6765%)
- **Heaviest Functions:** `visit_For` (Impact: 258.9), `visit_Output` (Impact: 159.9), `pop_assign_tracking` (Impact: 111.2)

### 7. `jinja2-3.1.6/src/jinja2/async_utils.py` (PYTHON) -> Cumulative Risk: **769.75**
- **Archetype:** `file_cluster_13` (Distance: 9.508 IQR)
- **Magnitude:** 72.36 | **LOC:** 100 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (99.9998%), Algorithmic Dos (99.9998%)
- **Heaviest Functions:** `async_variant` (Impact: 28.1), `auto_await` (Impact: 8.2), `__anext__` (Impact: 8.2)

### 8. `jinja2-3.1.6/src/jinja2/utils.py` (PYTHON) -> Cumulative Risk: **764.9**
- **Archetype:** `file_cluster_13` (Distance: 12.215 IQR)
- **Magnitude:** 384.84 | **LOC:** 767 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (94.8503%)
- **Heaviest Functions:** `url_quote` (Impact: 187.9), `import_string` (Impact: 21.5), `object_type_repr` (Impact: 12.7)

### 9. `jinja2-3.1.6/src/jinja2/filters.py` (PYTHON) -> Cumulative Risk: **759.55**
- **Archetype:** `file_cluster_16` (Distance: 11.325 IQR)
- **Magnitude:** 548.14 | **LOC:** 1874 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (96.6067%), Safety Score (80.0%)
- **Heaviest Functions:** `do_filesizeformat` (Impact: 135.6), `attrgetter` (Impact: 25.6), `attrgetter` (Impact: 20.8)

### 10. `jinja2-3.1.6/src/jinja2/debug.py` (PYTHON) -> Cumulative Risk: **756.36**
- **Archetype:** `file_cluster_13` (Distance: 10.372 IQR)
- **Magnitude:** 111.12 | **LOC:** 192 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), Logic Bomb (99.9943%), Algorithmic Dos (99.8972%)
- **Heaviest Functions:** `rewrite_traceback_stack` (Impact: 51.6), `get_template_locals` (Impact: 40.2), `fake_traceback` (Impact: 1.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `jinja2-3.1.6/src/jinja2/compiler.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.211 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.699 IQR)
- **Top Global Matches:** file_cluster_16: 12.211, file_cluster_13: 12.261, file_cluster_0: 12.368
- **Magnitude:** 1961.5 | **LOC:** 1999 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (25.431%), Tech Debt (39.559%)
**Top Internal Functions/Classes:**
  * `visit_For` (Impact: 258.9 | O(N^5))
  * `visit_Output` (Impact: 159.9 | O(N^5) | DB: 5)
  * `pop_assign_tracking` (Impact: 111.2 | O(N^5) | DB: 5)
  * `visit_Include` (Impact: 87.9 | O(N^4))
  * `visit_FromImport` (Impact: 86.8 | O(N^5) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 388`, `structural_boundaries: 262`, `args: 118`, `func_start: 118`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 156`, `dead_code: 11`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 7`
* *Architecture:* `api: 132`, `concurrency: 14`, `import: 25`
* *Defense:* `safety: 41`, `doc: 100`, `test: 1`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.341
  * `Choke Point (Betweenness):` 0.039399 | `Ripple Effect (Closeness):` 0.278472
  * `Imports (Out-Degree: 8):` .nodes, typing, contextlib, .optimizer, markupsafe, functools, .visitor, keyword...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/src/jinja2/parser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.89 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.253 IQR)
- **Top Global Matches:** file_cluster_16: 10.89, file_cluster_8: 11.008, file_cluster_13: 11.221
- **Magnitude:** 1103.84 | **LOC:** 1050 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (20.9136%), Tech Debt (33.6094%)
**Top Internal Functions/Classes:**
  * `parse_from` (Impact: 105.1 | O(N^6) | DB: 2)
  * `parse_primary` (Impact: 62.7 | O(N^4) | DB: 1)
  * `parse_test` (Impact: 62.5 | O(N^4))
    * *Intent:* # needs to be recorded before the stream is advanced. token = self.stream.current args, kwargs, dyn_...
  * `parse_block` (Impact: 53.5 | O(N^5))
  * `parse_condexpr` (Impact: 52.7 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 231`, `structural_boundaries: 218`, `args: 58`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 116`, `dead_code: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 70`, `import: 9`
* *Defense:* `safety: 10`, `doc: 34`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.56
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.265669
  * `Imports (Out-Degree: 4):` typing_extensions, , .exceptions, .lexer, .environment, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/src/jinja2/runtime.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.732 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.835 IQR)
- **Top Global Matches:** file_cluster_13: 12.732, file_cluster_16: 12.777, file_cluster_0: 12.785
- **Magnitude:** 831.04 | **LOC:** 1063 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (46.7554%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__call__` (Impact: 117.8 | O(N^5) | DB: 6)
  * `__anext__` (Impact: 24.6 | O(2^N) | DB: 3)
  * `_log_message` (Impact: 21.3 | O(2^N))
  * `_undefined_message` (Impact: 18.3 | O(N^4))
  * `__str__` (Impact: 18.0 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 252`, `args: 82`, `func_start: 82`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 128`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 44`
* *Architecture:* `io: 1`, `api: 51`, `concurrency: 49`, `import: 25`
* *Defense:* `safety: 20`, `doc: 94`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 89.579
  * `Choke Point (Betweenness):` 0.043572 | `Ripple Effect (Closeness):` 0.405495
  * `Imports (Out-Degree: 5):` typing_extensions, .utils, itertools, .exceptions, collections, .nodes, markupsafe, .environment...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/tests/test_lexnparse.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_2` (Drift: 12.293 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.586 IQR)
- **Top Global Matches:** file_cluster_2: 12.293, file_cluster_17: 12.336, file_cluster_8: 12.446
- **Magnitude:** 594.24 | **LOC:** 1031 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (1.8674%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_comment_syntax` (Impact: 118.6 | O(N^4))
  * `test_balancing` (Impact: 75.3 | O(N^4))
  * `test_tuple_expr` (Impact: 34.0 | O(N^4))
  * `test_function_calls` (Impact: 27.2 | O(N^5))
  * `test_grouping` (Impact: 17.6 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 272`, `args: 110`, `func_start: 109`, `class_start: 7`
* *Risk/State:* `dead_code: 4`, `fragile_debt: 1`, `orphaned_logic: 43`
* *Architecture:* `api: 115`, `import: 13`
* *Defense:* `safety: 125`, `doc: 88`, `test: 244`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` jinja2, pytest, jinja2.lexer, pprint
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/src/jinja2/filters.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.325 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.757 IQR)
- **Top Global Matches:** file_cluster_16: 11.325, file_cluster_13: 11.515, file_cluster_0: 11.53
- **Magnitude:** 548.14 | **LOC:** 1874 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (13.5193%), Tech Debt (66.2533%)
**Top Internal Functions/Classes:**
  * `do_filesizeformat` (Impact: 135.6 | O(N^4))
  * `attrgetter` (Impact: 25.6 | O(N^4))
  * `attrgetter` (Impact: 20.8 | O(N^4))
  * `do_int` (Impact: 16.7 | O(N^3))
  * `do_format` (Impact: 16.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 259`, `args: 94`, `func_start: 85`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 111`, `state_mutation: 21`, `dead_code: 2`, `duplicate_logic: 11`
* *Architecture:* `api: 82`, `concurrency: 24`, `import: 31`
* *Defense:* `safety: 55`, `doc: 130`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.593
  * `Choke Point (Betweenness):` 0.016147 | `Ripple Effect (Closeness):` 0.195875
  * `Imports (Out-Degree: 7):` typing_extensions, .runtime, random, inspect, .utils, re, itertools, .exceptions...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/tests/test_filters.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_2` (Drift: 11.848 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.781 IQR)
- **Top Global Matches:** file_cluster_2: 11.848, file_cluster_8: 12.022, file_cluster_13: 12.222
- **Magnitude:** 496.24 | **LOC:** 884 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (1.5691%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_filter_undefined_in_condexpr` (Impact: 31.7 | O(N^3))
  * `test_filter_undefined_in_if` (Impact: 25.3 | O(N^3))
  * `test_xmlattr_key_invalid` (Impact: 15.2 | O(N^4))
  * `test_random` (Impact: 12.8 | O(N^3))
    * *Intent:* # ensures that filter result is not constant folded random.seed("jinja") t = env.from_string('{{ "12...
  * `test_format` (Impact: 12.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 267`, `args: 110`, `func_start: 107`, `class_start: 5`
* *Risk/State:* `state_mutation: 3`, `duplicate_logic: 5`, `orphaned_logic: 77`
* *Architecture:* `api: 105`, `import: 10`
* *Defense:* `safety: 131`, `doc: 76`, `test: 250`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` random, jinja2.exceptions, collections, pprint, markupsafe, pytest, jinja2
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/src/jinja2/ext.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.023 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.325 IQR)
- **Top Global Matches:** file_cluster_16: 11.023, file_cluster_13: 11.179, file_cluster_8: 11.398
- **Magnitude:** 495.36 | **LOC:** 871 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (22.5258%), Tech Debt (98.8896%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 188.0 | O(N^6) | DB: 2)
  * `find_backwards` (Impact: 43.2 | O(N^6) | DB: 1)
  * `_install_null` (Impact: 31.7 | O(N^4))
  * `find_comments` (Impact: 22.0 | O(N^4))
    * *Intent:* * ``message`` is the string, or a tuple of strings for functions
  * `_make_new_ngettext` (Impact: 9.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 140`, `args: 43`, `func_start: 43`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 60`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 10`
* *Architecture:* `api: 34`, `import: 19`
* *Defense:* `safety: 17`, `doc: 41`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.751
  * `Choke Point (Betweenness):` 0.003205 | `Ripple Effect (Closeness):` 0.265669
  * `Imports (Out-Degree: 7):` typing_extensions, , .runtime, .utils, name., re, .exceptions, gettext...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/src/jinja2/utils.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.215 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.088 IQR)
- **Top Global Matches:** file_cluster_13: 12.215, file_cluster_16: 12.22, file_cluster_11: 12.652
- **Magnitude:** 384.84 | **LOC:** 767 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (32.1091%), Tech Debt (27.276%)
**Top Internal Functions/Classes:**
  * `url_quote` (Impact: 187.9 | O(N^5) | DB: 19)
  * `import_string` (Impact: 21.5 | O(N^3))
  * `object_type_repr` (Impact: 12.7 | O(N^2) | DB: 1)
  * `trim_url` (Impact: 10.2 | O(N^4))
  * `from_obj` (Impact: 7.2 | O(N^3))
    * *Intent:* """ f.jinja_pass_arg = _PassArg.eval_context # type: ignore return f def pass_environment(f: F) -> F...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 155`, `args: 52`, `func_start: 52`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 47`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 49`, `concurrency: 1`, `import: 21`
* *Defense:* `safety: 17`, `doc: 89`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 78.333
  * `Choke Point (Betweenness):` 0.04206 | `Ripple Effect (Closeness):` 0.398504
  * `Imports (Out-Degree: 5):` .constants, urllib.parse, collections, pprint, typing, re, markupsafe, threading...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/src/jinja2/idtracking.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.418 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.35 IQR)
- **Top Global Matches:** file_cluster_16: 10.418, file_cluster_8: 10.855, file_cluster_13: 10.945
- **Magnitude:** 384.38 | **LOC:** 319 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (13.8807%), Tech Debt (99.994%)
**Top Internal Functions/Classes:**
  * `branch_update` (Impact: 32.3 | O(N^5) | DB: 4)
  * `store` (Impact: 21.6 | O(N^5))
  * `dump_stores` (Impact: 21.4 | O(N^5))
  * `dump_param_targets` (Impact: 21.4 | O(N^5))
  * `find_load` (Impact: 21.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 71`, `args: 40`, `func_start: 40`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 24`, `duplicate_logic: 11`
* *Architecture:* `api: 47`, `import: 4`
* *Defense:* `safety: 2`, `doc: 16`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.765
  * `Choke Point (Betweenness):` 0.000726 | `Ripple Effect (Closeness):` 0.215252
  * `Imports (Out-Degree: 2):` typing_extensions, , typing, .visitor
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/src/jinja2/bccache.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.784 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.901 IQR)
- **Top Global Matches:** file_cluster_13: 12.784, file_cluster_16: 13.077, file_cluster_11: 13.126
- **Magnitude:** 373.92 | **LOC:** 409 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 54
- **Risk Profile:** Cognitive Load (17.4356%), Tech Debt (99.9976%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 226.8 | O(2^N) | DB: 54)
  * `dump_bytecode` (Impact: 22.3 | O(N^4))
  * `load_bytecode` (Impact: 17.7 | O(N^4))
  * `load_bytecode` (Impact: 14.8 | O(N^3) | DB: 5)
  * `write_bytecode` (Impact: 7.3 | O(N^3))
    * *Intent:* # if marshal_load fails then we need to reload try: self.code = marshal.load(f) except (EOFError, Va...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 68`, `args: 26`, `func_start: 26`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 26`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 7`
* *Architecture:* `io: 19`, `api: 26`, `import: 15`
* *Defense:* `safety: 22`, `doc: 34`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.732
  * `Choke Point (Betweenness):` 0.005322 | `Ripple Effect (Closeness):` 0.268758
  * `Imports (Out-Degree: 2):` typing_extensions, fnmatch, tempfile, os, errno, hashlib, io, types...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/src/jinja2/loaders.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.648 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.984 IQR)
- **Top Global Matches:** file_cluster_13: 12.648, file_cluster_11: 12.754, file_cluster_0: 12.796
- **Magnitude:** 350.16 | **LOC:** 694 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (30.9223%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `list_templates` (Impact: 43.1 | O(N^5) | DB: 26)
  * `list_templates` (Impact: 37.2 | O(N^6) | DB: 12)
  * `split_template_path` (Impact: 32.7 | O(N^3) | DB: 13)
  * `list_templates` (Impact: 26.3 | O(2^N) | DB: 1)
  * `list_templates` (Impact: 14.1 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 116`, `args: 33`, `func_start: 32`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 64`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 26`
* *Architecture:* `io: 47`, `api: 32`, `import: 19`
* *Defense:* `safety: 29`, `doc: 34`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.686
  * `Choke Point (Betweenness):` 0.006894 | `Ripple Effect (Closeness):` 0.275157
  * `Imports (Out-Degree: 4):` posixpath, weakref, .utils, spec, does, os, .exceptions, os.path...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/src/jinja2/lexer.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.106 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.576 IQR)
- **Top Global Matches:** file_cluster_16: 11.106, file_cluster_13: 11.176, file_cluster_8: 11.219
- **Magnitude:** 321.94 | **LOC:** 869 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (9.7947%), Tech Debt (72.369%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 28.7 | O(N^6) | DB: 3)
    * *Intent:* """A special tuple for marking a point in the state that can have lstrip applied. """
  * `compile_rules` (Impact: 22.0 | O(N^4) | DB: 2)
  * `__next__` (Impact: 18.0 | O(N^4) | DB: 2)
  * `expect` (Impact: 16.7 | O(N^5))
  * `describe_token_expr` (Impact: 16.6 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 115`, `args: 34`, `func_start: 33`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 61`, `dead_code: 4`, `duplicate_logic: 8`
* *Architecture:* `api: 35`, `import: 10`
* *Defense:* `safety: 9`, `doc: 56`, `test: 3`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 38.897
  * `Choke Point (Betweenness):` 0.01022 | `Ripple Effect (Closeness):` 0.308176
  * `Imports (Out-Degree: 4):` typing_extensions, ._identifier, .utils, re, .exceptions, collections, ast, .environment...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/tests/test_async.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_2` (Drift: 11.794 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.282 IQR)
- **Top Global Matches:** file_cluster_2: 11.794, file_cluster_8: 11.815, file_cluster_13: 11.97
- **Magnitude:** 321.72 | **LOC:** 735 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.9396%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_env_async` (Impact: 125.8 | O(2^N))
  * `test_chainable_undefined_aiter` (Impact: 20.6 | O(N^3))
    * *Intent:* """ ) sm = t.render( this="/foo", site={"root": {"url": "/", "children": [{"url": "/foo"}, {"url": "...
  * `test_blocks_generate_async` (Impact: 18.8 | O(N^3))
  * `test_include_generate_async` (Impact: 11.0 | O(N^3))
  * `test_async_iteration_in_templates` (Impact: 7.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 215`, `args: 86`, `func_start: 82`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `fragile_debt: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 80`, `concurrency: 35`, `import: 12`
* *Defense:* `safety: 84`, `doc: 34`, `test: 147`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` trio, bar, jinja2.exceptions, jinja2.nativetypes, baz, context, pytest, test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/tests/test_loader.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.322 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.301 IQR)
- **Top Global Matches:** file_cluster_13: 12.322, file_cluster_0: 12.482, file_cluster_17: 12.654
- **Magnitude:** 276.66 | **LOC:** 437 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (7.9966%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_pep_451_import_hook` (Impact: 18.8 | O(N^4) | DB: 10)
  * `teardown_method` (Impact: 17.7 | O(N^4) | DB: 9)
  * `test_error_includes_paths` (Impact: 12.8 | O(N^3) | DB: 1)
  * `compile_down` (Impact: 12.6 | O(N^3) | DB: 7)
  * `test_weak_references` (Impact: 7.9 | O(N^3) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 148`, `args: 48`, `func_start: 48`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 33`, `duplicate_logic: 6`, `orphaned_logic: 34`
* *Architecture:* `io: 14`, `api: 51`, `import: 17`
* *Defense:* `safety: 64`, `doc: 4`, `test: 119`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` weakref, pathlib, jinja2.exceptions, tempfile, shutil, os, gc, importlib.machinery...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/tests/test_core_tags.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_2` (Drift: 12.132 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.164 IQR)
- **Top Global Matches:** file_cluster_2: 12.132, file_cluster_8: 12.247, file_cluster_17: 12.484
- **Magnitude:** 259.82 | **LOC:** 604 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (1.3884%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_context_vars` (Impact: 42.1 | O(N^4))
  * `test_block_filtered` (Impact: 9.0 | O(N^3))
  * `test_intended_scoping_with_set` (Impact: 8.7 | O(N^3))
  * `test_loop_unassignable` (Impact: 6.0 | O(N^3))
    * *Intent:* %}{{ loop }}{% endfor %}"""
  * `test_recursive` (Impact: 5.9 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 171`, `args: 65`, `func_start: 65`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `fragile_debt: 6`, `duplicate_logic: 2`, `orphaned_logic: 32`
* *Architecture:* `api: 69`, `import: 6`
* *Defense:* `safety: 88`, `doc: 58`, `test: 162`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jinja2, pytest, test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/src/jinja2/environment.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.858 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.78 IQR)
- **Top Global Matches:** file_cluster_13: 11.858, file_cluster_16: 11.887, file_cluster_0: 12.211
- **Magnitude:** 259.6 | **LOC:** 1673 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (17.4716%), Tech Debt (9.2475%)
**Top Internal Functions/Classes:**
  * `getattr` (Impact: 24.6 | O(2^N))
  * `extend` (Impact: 13.3 | O(N^4))
  * `_environment_config_check` (Impact: 9.8 | O(N^2))
  * `__init__` (Impact: 7.6 | O(N^2))
  * `add_extension` (Impact: 3.2 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 300`, `args: 75`, `func_start: 73`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 78`, `high_risk_execution: 2`, `state_mutation: 68`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `io: 6`, `api: 60`, `concurrency: 35`, `import: 61`
* *Defense:* `safety: 64`, `doc: 124`, `test: 6`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 81.539
  * `Choke Point (Betweenness):` 0.151306 | `Ripple Effect (Closeness):` 0.42024
  * `Imports (Out-Degree: 12):` weakref, .compiler, collections, .nodes, typing, without, zipfile, markupsafe...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/tests/test_regression.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_2` (Drift: 12.33 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_2: 12.33, file_cluster_17: 12.342, file_cluster_13: 12.349
- **Magnitude:** 217.74 | **LOC:** 768 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (1.5495%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_double_caller` (Impact: 56.2 | O(N^5))
  * `test_extends_output_bugs` (Impact: 43.9 | O(N^6))
  * `test_nested_for_else` (Impact: 10.2 | O(N^5))
  * `test_recursive_loop_bug` (Impact: 9.3 | O(N^4))
  * `test_loop_include` (Impact: 6.8 | O(N^5))
    * *Intent:* """, "c.html": """
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 167`, `args: 60`, `func_start: 58`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `dead_code: 4`, `orphaned_logic: 11`
* *Architecture:* `api: 62`, `import: 13`
* *Defense:* `safety: 68`, `doc: 58`, `test: 130`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` jinja2.filters, jinja2.runtime, jinja2.utils, markupsafe, pytest, jinja2
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/tests/test_ext.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_2` (Drift: 10.862 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.571 IQR)
- **Top Global Matches:** file_cluster_2: 10.862, file_cluster_13: 10.994, file_cluster_8: 11.01
- **Magnitude:** 195.68 | **LOC:** 740 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (1.7812%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_extension_nodes` (Impact: 20.2 | O(N^4))
    * *Intent:* """ {%- set items = [] %} {%- for char in "foo" %} {%- do items.append(loop.index0 ~ char) %} {%- en...
  * `test_basic_scope_behavior` (Impact: 19.5 | O(N^6) | DB: 1)
  * `test_trimmed_vars` (Impact: 15.0 | O(N^3))
  * `test_complex_plural` (Impact: 10.4 | O(N^3))
  * `test_overlay_scopes` (Impact: 6.3 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 205`, `args: 68`, `func_start: 65`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `duplicate_logic: 6`, `orphaned_logic: 9`
* *Architecture:* `api: 76`, `import: 17`
* *Defense:* `safety: 72`, `doc: 28`, `test: 127`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` jinja2.exceptions, re, jinja2.lexer, io, pytest, jinja2.ext, jinja2
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/tests/test_inheritance.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.357 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.09 IQR)
- **Top Global Matches:** file_cluster_8: 10.357, file_cluster_2: 10.389, file_cluster_13: 10.766
- **Magnitude:** 182.3 | **LOC:** 411 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (1.6327%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_level2_required` (Impact: 73.3 | O(N^5))
  * `test_dynamic_inheritance` (Impact: 13.7 | O(N^6))
  * `test_double_extends` (Impact: 10.6 | O(N^3))
  * `test_super` (Impact: 7.1 | O(N^5))
  * `test_scoped_block` (Impact: 6.6 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 75`, `args: 23`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `orphaned_logic: 13`
* *Architecture:* `api: 25`, `import: 5`
* *Defense:* `safety: 25`, `doc: 28`, `test: 56`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jinja2, pytest, foo
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/tests/test_async_filters.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.438 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.722 IQR)
- **Top Global Matches:** file_cluster_0: 11.438, file_cluster_4: 11.505, file_cluster_13: 11.512
- **Magnitude:** 171.52 | **LOC:** 322 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (12.4887%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_join_string_list` (Impact: 25.8 | O(N^4) | DB: 1)
  * `closing_factory` (Impact: 20.6 | O(N^4))
  * `test_first` (Impact: 8.4 | O(N^3))
  * `make_aiter` (Impact: 6.2 | O(N^2))
  * `mark_dualiter` (Impact: 3.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 100`, `args: 41`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `orphaned_logic: 7`
* *Architecture:* `api: 40`, `concurrency: 37`, `import: 8`
* *Defense:* `safety: 27`, `doc: 16`, `test: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` trio, contextlib, collections, markupsafe, pytest, jinja2, jinja2.async_utils, asyncio
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/src/jinja2/meta.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.28 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.369 IQR)
- **Top Global Matches:** file_cluster_13: 11.28, file_cluster_16: 11.288, file_cluster_7: 11.653
- **Magnitude:** 155.54 | **LOC:** 113 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.7262%), Tech Debt (94.3702%)
**Top Internal Functions/Classes:**
  * `find_referenced_templates` (Impact: 107.0 | O(N^6))
  * `enter_frame` (Impact: 35.0 | O(2^N))
  * `__init__` (Impact: 5.3 | O(2^N))
  * `find_undeclared_variables` (Impact: 2.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 18`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `safety: 8`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` , .compiler, .environment, jinja2, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/src/jinja2/sandbox.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.02 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.93 IQR)
- **Top Global Matches:** file_cluster_16: 11.02, file_cluster_13: 11.071, file_cluster_8: 11.163
- **Magnitude:** 136.52 | **LOC:** 437 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (12.5371%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `is_internal_attribute` (Impact: 60.2 | O(N^3))
  * `is_safe_attribute` (Impact: 18.1 | O(2^N))
  * `modifies_known_mutable` (Impact: 10.7 | O(N^3))
  * `safe_range` (Impact: 8.6 | O(N^3))
  * `__init__` (Impact: 6.2 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 90`, `args: 18`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 3`
* *Architecture:* `api: 21`, `import: 14`
* *Defense:* `safety: 30`, `doc: 32`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.981
  * `Choke Point (Betweenness):` 0.006682 | `Ripple Effect (Closeness):` 0.162769
  * `Imports (Out-Degree: 4):` .runtime, operator, .exceptions, collections, types, markupsafe, _string, functools...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/tests/test_imports.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_2` (Drift: 11.137 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.596 IQR)
- **Top Global Matches:** file_cluster_2: 11.137, file_cluster_8: 11.218, file_cluster_13: 11.271
- **Magnitude:** 135.72 | **LOC:** 206 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.5405%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_env` (Impact: 83.2 | O(2^N))
  * `test_context_include` (Impact: 23.6 | O(N^5))
  * `test_import_from_with_context` (Impact: 3.9 | O(N^3))
    * *Intent:* """ {% macro outer(o) %} {% macro inner() %} {% include "o_printer" %} {% endmacro %} {{ inner() }} ...
  * `test_unoptimized_scopes` (Impact: 2.9 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 60`, `args: 17`, `func_start: 17`, `class_start: 2`
* *Risk/State:* `orphaned_logic: 3`
* *Architecture:* `api: 19`, `import: 7`
* *Defense:* `safety: 28`, `doc: 4`, `test: 56`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` bar, jinja2.exceptions, baz, context, jinja2.environment, nothing, x, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/src/jinja2/visitor.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.743 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.192 IQR)
- **Top Global Matches:** file_cluster_13: 12.743, file_cluster_16: 12.781, file_cluster_11: 13.179
- **Magnitude:** 125.98 | **LOC:** 93 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (34.6925%), Tech Debt (99.9955%)
**Top Internal Functions/Classes:**
  * `generic_visit` (Impact: 79.3 | O(N^6) | DB: 2)
  * `visit` (Impact: 9.4 | O(N^3))
  * `visit_list` (Impact: 9.4 | O(N^3))
  * `generic_visit` (Impact: 9.2 | O(N^3))
  * `get_visitor` (Impact: 2.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 24`, `args: 6`, `func_start: 6`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 6`, `duplicate_logic: 2`
* *Architecture:* `api: 9`, `import: 3`
* *Defense:* `safety: 6`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.595
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.227044
  * `Imports (Out-Degree: 1):` typing_extensions, typing, .nodes
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/tests/test_security.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.907 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.281 IQR)
- **Top Global Matches:** file_cluster_13: 10.907, file_cluster_2: 10.913, file_cluster_8: 11.165
- **Magnitude:** 111.78 | **LOC:** 203 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (3.2009%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_template_data` (Impact: 25.0 | O(N^4))
  * `test_safe_format_all_okay` (Impact: 7.9 | O(N^3))
  * `test_attr_filter` (Impact: 7.4 | O(N^3))
  * `test_unsafe` (Impact: 4.4 | O(N^3))
  * `test_restricted` (Impact: 4.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 78`, `args: 26`, `func_start: 26`, `class_start: 5`
* *Risk/State:* `state_mutation: 4`, `duplicate_logic: 6`, `orphaned_logic: 4`
* *Architecture:* `api: 28`, `import: 10`
* *Defense:* `safety: 21`, `doc: 4`, `test: 53`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` jinja2.exceptions, markupsafe, pytest, jinja2, jinja2.sandbox, jinja2.nodes
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `jinja2-3.1.6/tests/test_async_filters.py` (PYTHON) | Magnitude: 171.52 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 165, structural_boundaries: 100, test: 57, args: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `jinja2-3.1.6/src/jinja2/utils.py` (PYTHON) | Magnitude: 384.84 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 313, structural_boundaries: 155, encapsulation: 102, branch: 92
- `jinja2-3.1.6/tests/test_security.py` (PYTHON) | Magnitude: 111.78 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 144, structural_boundaries: 78, test: 53, ui_framework: 36
- `jinja2-3.1.6/src/jinja2/meta.py` (PYTHON) | Magnitude: 155.54 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 37, branch: 18, structural_boundaries: 18, doc: 12
- `jinja2-3.1.6/src/jinja2/environment.py` (PYTHON) | Magnitude: 259.6 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 859, structural_boundaries: 300, generics: 184, branch: 147
- `jinja2-3.1.6/src/jinja2/visitor.py` (PYTHON) | Magnitude: 125.98 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 24, safety_bypasses: 14, doc: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `jinja2-3.1.6/src/jinja2/compiler.py` (PYTHON) | Magnitude: 1961.5 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1405, branch: 388, structural_boundaries: 262, generics: 163
- `jinja2-3.1.6/src/jinja2/sandbox.py` (PYTHON) | Magnitude: 136.52 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 215, structural_boundaries: 90, branch: 47, safety_bypasses: 46
- `jinja2-3.1.6/src/jinja2/lexer.py` (PYTHON) | Magnitude: 321.94 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 500, structural_boundaries: 115, branch: 91, state_mutation: 61
- `jinja2-3.1.6/src/jinja2/parser.py` (PYTHON) | Magnitude: 1103.84 | Delta: **0.118 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 836, branch: 231, structural_boundaries: 218, state_mutation: 116
- `jinja2-3.1.6/src/jinja2/ext.py` (PYTHON) | Magnitude: 495.36 | Delta: **0.156 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 516, structural_boundaries: 140, branch: 112, generics: 100

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `jinja2-3.1.6/tests/test_compile.py` (PYTHON) | Magnitude: 64.82 | Delta: **0.249 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 21, state_mutation: 15, test: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `jinja2-3.1.6/tests/test_nativetypes.py` (PYTHON) | Magnitude: 59.92 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 89, structural_boundaries: 73, test: 61, safety: 51
- `jinja2-3.1.6/tests/test_regression.py` (PYTHON) | Magnitude: 217.74 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 403, structural_boundaries: 167, test: 130, ui_framework: 69
- `jinja2-3.1.6/tests/test_async.py` (PYTHON) | Magnitude: 321.72 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 476, structural_boundaries: 215, test: 147, args: 86
- `jinja2-3.1.6/tests/test_lexnparse.py` (PYTHON) | Magnitude: 594.24 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 762, structural_boundaries: 272, test: 244, safety: 125
- `jinja2-3.1.6/tests/test_imports.py` (PYTHON) | Magnitude: 135.72 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 145, structural_boundaries: 60, test: 56, ui_framework: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `jinja2-3.1.6/tests/test_inheritance.py` (PYTHON) | Magnitude: 182.3 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 268, structural_boundaries: 75, test: 56, ui_framework: 36
- `jinja2-3.1.6/tests/test_api.py` (PYTHON) | Magnitude: 48.44 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 324, test: 95, sec_high_risk_execution: 85, structural_boundaries: 82
- `jinja2-3.1.6/tests/test_tests.py` (PYTHON) | Magnitude: 93.8 | Delta: **0.176 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 191, structural_boundaries: 54, test: 45, api: 22
- `jinja2-3.1.6/src/jinja2/constants.py` (PYTHON) | Magnitude: 10.52 | Delta: **0.184 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 2
- `jinja2-3.1.6/src/jinja2/defaults.py` (PYTHON) | Magnitude: 15.78 | Delta: **0.419 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 18, indent_spaces: 15, import: 8, generics: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `jinja2-3.1.6/src/jinja2/environment.py` -> **Severity: 9.903** (Bridge: 0.1513 * Flux: 65.4509%)
- `jinja2-3.1.6/src/jinja2/runtime.py` -> **Severity: 4.347** (Bridge: 0.0436 * Flux: 99.7572%)
- `jinja2-3.1.6/src/jinja2/utils.py` -> **Severity: 3.989** (Bridge: 0.0421 * Flux: 94.8503%)
- `jinja2-3.1.6/src/jinja2/compiler.py` -> **Severity: 3.48** (Bridge: 0.0394 * Flux: 88.3345%)
- `jinja2-3.1.6/src/jinja2/exceptions.py` -> **Severity: 1.276** (Bridge: 0.0128 * Flux: 99.9951%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `jinja2-3.1.6/src/jinja2/utils.py` -> **Severity: 31.88** (Embedded: 0.3985 * Error Risk: 80.0%)
- `jinja2-3.1.6/src/jinja2/environment.py` -> **Severity: 30.78** (Embedded: 0.4202 * Error Risk: 73.2432%)
- `jinja2-3.1.6/src/jinja2/runtime.py` -> **Severity: 30.238** (Embedded: 0.4055 * Error Risk: 74.5705%)
- `jinja2-3.1.6/src/jinja2/exceptions.py` -> **Severity: 22.857** (Embedded: 0.4202 * Error Risk: 54.3902%)
- `jinja2-3.1.6/src/jinja2/async_utils.py` -> **Severity: 21.615** (Embedded: 0.2785 * Error Risk: 77.619%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `jinja2-3.1.6/src/jinja2/runtime.py` -> **Severity: 8950.178** (Blast Radius: 89.579 * Doc Risk: 99.9138%)
- `jinja2-3.1.6/src/jinja2/exceptions.py` -> **Severity: 7668.185** (Blast Radius: 78.994 * Doc Risk: 97.073%)
- `jinja2-3.1.6/src/jinja2/utils.py` -> **Severity: 6986.904** (Blast Radius: 78.333 * Doc Risk: 89.1949%)
- `jinja2-3.1.6/src/jinja2/async_utils.py` -> **Severity: 3167.694** (Blast Radius: 31.677 * Doc Risk: 99.9998%)
- `jinja2-3.1.6/src/jinja2/lexer.py` -> **Severity: 2785.675** (Blast Radius: 38.897 * Doc Risk: 71.6167%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
