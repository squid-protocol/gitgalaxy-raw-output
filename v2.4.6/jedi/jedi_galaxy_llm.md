# ARCHITECTURAL_BRIEF: jedi
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/jedi` |
| **Timestamp** | `2026-08-03T19:39:02.496714+00:00` |
| **Scan Duration** | `0.57s` |
| **Git Branch** | `master` |
| **Git Commit** | `76c1e03f07b351c07b54609df12615dfb9379a9a` |
| **Git Remote** | `https://github.com/davidhalter/jedi.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 93 malicious artifacts.

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
| Total Artifacts | 387 |
| Analyzed Artifacts (Scanned) | 99 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 288 |
| Total LOC | 13890 |
| Volatility Index | 0.03 |
| % Scanned of codebase = | 25.6% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2516 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1415 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 35.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2351 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 89 | 13854 | 89.9% |
| PLAINTEXT | 4 | 0 | 4.0% |
| MARKDOWN | 2 | 0 | 2.0% |
| SHELL | 2 | 34 | 2.0% |
| BINARY_THREAT | 2 | 2 | 2.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.973`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 63 | 63.6% |
| file_cluster_8 | 23 | 23.2% |
| file_cluster_0 | 2 | 2.0% |
| Unknown | 2 | 2.0% |
| file_cluster_17 | 1 | 1.0% |
| file_cluster_16 | 1 | 1.0% |
| file_cluster_7 | 1 | 1.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 6.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 288*

**Composition by Extension & Reason:**
- `.py`: 225x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 47 LOC), 1x Excluded (Machine-Generated Source Code Signature: 609 LOC)
- `.rst`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.rst')
- `.pyi`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable)
- `.png`: 4x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.egg-link`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zip`: 2x Excluded (Explicitly Denied Extension: '.zip')
- `.css`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.so`: 1x Excluded (Explicitly Denied Extension: '.so')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 98.7 | 21.6 | 16.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 16.9 | 5.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 34.1 | 12.5 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 51.4 | 80.0 | 80.0 |
| API Exposure | 0.0 | 11.5 | 3.5 | 3.2 | 0.0 |
| Concurrency Exposure | 0.0 | 94.4 | 3.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 43.1 | 33.6 | 0.0 |
| Commented Logic Exposure | 0.0 | 21.9 | 1.7 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 90.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.3 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 9.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 79.8 | 100.0 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 75.6 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 62.9 | 100.0 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `jedi/api/environment.py` (Hits: 38)
- `jedi/__main__.py` (Hits: 15)
- `jedi/inference/compiled/subprocess/__init__.py` (Hits: 14)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **base_value.py** (`jedi/inference/base_value.py`) — 38 inbound connections
2. **names.py** (`jedi/inference/names.py`) — 25 inbound connections
3. **cache.py** (`jedi/inference/cache.py`) — 22 inbound connections
4. **typing.py** (`jedi/inference/gradual/typing.py`) — 22 inbound connections
5. **helpers.py** (`jedi/inference/helpers.py`) — 20 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **imports.py** (`jedi/inference/imports.py`) — 31 outbound dependencies
2. **__init__.py** (`jedi/api/__init__.py`) — 28 outbound dependencies
3. **klass.py** (`jedi/inference/value/klass.py`) — 25 outbound dependencies
4. **completion.py** (`jedi/api/completion.py`) — 22 outbound dependencies
5. **names.py** (`jedi/inference/names.py`) — 21 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `infer_node` (@ `jedi/inference/syntax_tree.py`) -> Impact: **3216.5** | LOC: 798
- `__repr__` (@ `jedi/inference/compiled/access.py`) -> Impact: **1073.0** | LOC: 364
- `get_stack_at_position` (@ `jedi/api/helpers.py`) -> Impact: **908.3** | LOC: 322
- `get_type_hint` (@ `jedi/inference/value/function.py`) -> Impact: **804.6** | LOC: 331
- `goto` (@ `jedi/inference/context.py`) -> Impact: **571.0** | LOC: 220
- `process_params` (@ `jedi/inference/star_args.py`) -> Impact: **551.2** | LOC: 112
- `__repr__` (@ `jedi/api/__init__.py`) -> Impact: **540.8** | LOC: 390
- `_add_stderr_to_debug` (@ `jedi/inference/compiled/subprocess/__init__.py`) -> Impact: **540.0** | LOC: 374
- `_infer_field` (@ `jedi/plugins/django.py`) -> Impact: **510.1** | LOC: 122
- `_extract_string_while_in_string` (@ `jedi/api/completion.py`) -> Impact: **481.2** | LOC: 168

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `_get_subprocess` (@ `jedi/api/environment.py`) -> **O(2^N) [Recursive]**
- `infer` (@ `jedi/api/interpreter.py`) -> **O(2^N) [Recursive]**
- `_remove_unwanted_expression_nodes` (@ `jedi/api/refactoring/extract.py`) -> **O(2^N) [Recursive]**
- `goto` (@ `jedi/inference/base_value.py`) -> **O(2^N) [Recursive]**
- `__repr__` (@ `jedi/inference/compiled/access.py`) -> **O(2^N) [Recursive]**
- `_add_stderr_to_debug` (@ `jedi/inference/compiled/subprocess/__init__.py`) -> **O(2^N) [Recursive]**
- `goto` (@ `jedi/inference/context.py`) -> **O(2^N) [Recursive]**
- `create_context` (@ `jedi/inference/context.py`) -> **O(2^N) [Recursive]**
- `get_type_hint` (@ `jedi/inference/gradual/base.py`) -> **O(2^N) [Recursive]**
- `__repr__` (@ `jedi/inference/gradual/base.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `_get_subprocess` (@ `jedi/api/environment.py`) -> DB Complexity: **82**
- `_add_stderr_to_debug` (@ `jedi/inference/compiled/subprocess/__init__.py`) -> DB Complexity: **51**
- `infer_import` (@ `jedi/inference/imports.py`) -> DB Complexity: **32**
- `__init__` (@ `sith.py`) -> DB Complexity: **25**
  * *Intent:* --record=<file> Exceptions are recorded in here [default: record.json].
- `complete_file_name` (@ `jedi/api/file_name.py`) -> DB Complexity: **24**
- `_get_executable_path` (@ `jedi/api/environment.py`) -> DB Complexity: **21**
  * *Intent:* """ Ignores virtualenvs and returns the Python versions that were installed on your system. This might return nothing, if you're running Python e.g. f...
- `__init__` (@ `jedi/inference/__init__.py`) -> DB Complexity: **19**
- `_create_stub_map` (@ `jedi/inference/gradual/typeshed.py`) -> DB Complexity: **18**
  * *Intent:* """ Create a mapping of an importable name in Python to a stub file. """
- `_start_linter` (@ `jedi/__main__.py`) -> DB Complexity: **16**
  * *Intent:* """ This is a pre-alpha API. You're not supposed to use it at all, except for testing. It will very likely change. """
- `load_module` (@ `jedi/inference/compiled/access.py`) -> DB Complexity: **12**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `jedi/inference` | 25 | 13252.7 | 28.04% | 35.64% |
| `jedi/api` | 13 | 6128.38 | 17.95% | 20.1% |
| `jedi/inference/value` | 8 | 4002.84 | 15.31% | 63.87% |
| `jedi/inference/gradual` | 10 | 3342.96 | 20.35% | 57.94% |
| `jedi/inference/compiled` | 5 | 2854.98 | 36.63% | 44.72% |
| `jedi/api/refactoring` | 2 | 1498.46 | 16.11% | 28.8% |
| `jedi` | 10 | 1264.18 | 17.07% | 11.69% |
| `jedi/inference/compiled/subprocess` | 3 | 1024.16 | 30.41% | 7.91% |
| `test/examples/sample_venvs/pth_directory` | 2 | 1000.0 | 0.0% | 0.0% |
| `jedi/plugins` | 4 | 850.74 | 13.66% | 49.97% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `scripts/profiled_pytest.sh` -> **100.0%** Exposure
- `jedi/api/interpreter.py` -> **100.0%** Exposure
- `jedi/file_io.py` -> **100.0%** Exposure
- `jedi/inference/docstring_utils.py` -> **100.0%** Exposure
- `jedi/inference/filters.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `deploy-master.sh` -> **100.0%** Exposure
- `jedi/inference/compiled/subprocess/__main__.py` -> **99.995%** Exposure
- `jedi/inference/utils.py` -> **99.9928%** Exposure
- `jedi/inference/lazy_value.py` -> **99.9249%** Exposure
- `jedi/inference/gradual/type_var.py` -> **99.9201%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `jedi/inference/names.py` -> **0** Orphaned Functions | **54** Duplicates
- `jedi/inference/value/iterable.py` -> **0** Orphaned Functions | **34** Duplicates
- `jedi/inference/gradual/typing.py` -> **0** Orphaned Functions | **20** Duplicates
- `jedi/inference/compiled/value.py` -> **0** Orphaned Functions | **17** Duplicates
- `jedi/inference/signature.py` -> **0** Orphaned Functions | **14** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`jedi/__main__.py`** -> AI Confidence: **99.31%**
2. **`jedi/api/completion.py`** -> AI Confidence: **99.31%**
3. **`jedi/api/helpers.py`** -> AI Confidence: **99.31%**
4. **`jedi/api/refactoring/extract.py`** -> AI Confidence: **99.31%**
5. **`jedi/inference/docstrings.py`** -> AI Confidence: **99.31%**
6. **`jedi/inference/gradual/conversion.py`** -> AI Confidence: **99.31%**
7. **`jedi/inference/gradual/typeshed.py`** -> AI Confidence: **99.31%**
8. **`jedi/inference/imports.py`** -> AI Confidence: **99.31%**
9. **`jedi/inference/param.py`** -> AI Confidence: **99.31%**
10. **`jedi/inference/references.py`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `jedi/__main__.py` -> **100.0%** Exposure
- `jedi/api/__init__.py` -> **100.0%** Exposure
- `jedi/api/classes.py` -> **100.0%** Exposure
- `jedi/api/completion.py` -> **100.0%** Exposure
- `jedi/api/environment.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `jedi/inference/base_value.py` -> **100.0%** Exposure
- `jedi/inference/compiled/subprocess/__init__.py` -> **100.0%** Exposure
- `deploy-master.sh` -> **99.9999%** Exposure
- `jedi/api/classes.py` -> **36.2694%** Exposure
- `jedi/inference/compiled/value.py` -> **5.356%** Exposure
### Algorithmic DoS Exposure
- `jedi/__main__.py` -> **100.0%** Exposure
- `jedi/_compatibility.py` -> **100.0%** Exposure
- `jedi/api/__init__.py` -> **100.0%** Exposure
- `jedi/api/classes.py` -> **100.0%** Exposure
- `jedi/api/completion.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `746` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `jedi/inference/names.py` (PYTHON) -> Cumulative Risk: **870.36**
- **Archetype:** `file_cluster_13` (Distance: 10.499 IQR)
- **Magnitude:** 1331.38 | **LOC:** 674 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `goto` (Impact: 367.2), `get_qualified_names` (Impact: 97.7), `__repr__` (Impact: 86.3)

### 2. `jedi/inference/filters.py` (PYTHON) -> Cumulative Risk: **794.41**
- **Archetype:** `file_cluster_13` (Distance: 11.664 IQR)
- **Magnitude:** 522.0 | **LOC:** 371 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `__repr__` (Impact: 224.6), `__repr__` (Impact: 53.4), `_get_definition_names` (Impact: 32.9)

### 3. `jedi/inference/star_args.py` (PYTHON) -> Cumulative Risk: **776.57**
- **Archetype:** `file_cluster_13` (Distance: 9.844 IQR)
- **Magnitude:** 704.96 | **LOC:** 218 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `process_params` (Impact: 551.2), `_iter_nodes_for_param` (Impact: 50.1), `_remove_given_params` (Impact: 32.0)

### 4. `jedi/api/classes.py` (PYTHON) -> Cumulative Risk: **770.93**
- **Archetype:** `file_cluster_13` (Distance: 11.473 IQR)
- **Magnitude:** 888.9 | **LOC:** 894 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `description` (Impact: 456.0), `type` (Impact: 83.9), `docstring` (Impact: 28.7)

### 5. `jedi/inference/value/klass.py` (PYTHON) -> Cumulative Risk: **762.62**
- **Archetype:** `file_cluster_13` (Distance: 10.658 IQR)
- **Magnitude:** 1218.5 | **LOC:** 695 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `py__mro__` (Impact: 467.9), `is_typeddict` (Impact: 110.5), `get_metaclass_filters` (Impact: 85.0)

### 6. `jedi/inference/gradual/type_var.py` (PYTHON) -> Cumulative Risk: **758.06**
- **Archetype:** `file_cluster_13` (Distance: 11.096 IQR)
- **Magnitude:** 303.74 | **LOC:** 128 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 148.7), `py__call__` (Impact: 45.2), `infer_type_vars` (Impact: 21.3)

### 7. `jedi/inference/gradual/stub_value.py` (PYTHON) -> Cumulative Risk: **753.7**
- **Archetype:** `file_cluster_13` (Distance: 11.063 IQR)
- **Magnitude:** 169.72 | **LOC:** 103 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9985%)
- **Heaviest Functions:** `_is_name_reachable` (Impact: 70.1), `sub_modules_dict` (Impact: 35.3), `__init__` (Impact: 6.9)

### 8. `jedi/inference/base_value.py` (PYTHON) -> Cumulative Risk: **745.25**
- **Archetype:** `file_cluster_13` (Distance: 10.639 IQR)
- **Magnitude:** 909.3 | **LOC:** 559 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `_getitem` (Impact: 358.1), `goto` (Impact: 157.8), `is_sub_class_of` (Impact: 39.2)

### 9. `jedi/inference/analysis.py` (PYTHON) -> Cumulative Risk: **742.43**
- **Archetype:** `file_cluster_13` (Distance: 12.195 IQR)
- **Magnitude:** 348.5 | **LOC:** 214 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9297%)
- **Heaviest Functions:** `add_attribute_error` (Impact: 242.9), `_check_for_setattr` (Impact: 21.7), `__str__` (Impact: 19.1)

### 10. `jedi/inference/__init__.py` (PYTHON) -> Cumulative Risk: **734.41**
- **Archetype:** `file_cluster_13` (Distance: 11.054 IQR)
- **Magnitude:** 236.68 | **LOC:** 200 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9822%)
- **Heaviest Functions:** `infer` (Impact: 91.8), `parse_and_get_code` (Impact: 56.3), `execute` (Impact: 14.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `jedi/inference/syntax_tree.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.049 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.937 IQR)
- **Top Global Matches:** file_cluster_8: 10.049, file_cluster_13: 10.104, file_cluster_7: 10.373
- **Magnitude:** 3267.98 | **LOC:** 906 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (18.5116%), Tech Debt (12.9371%)
**Top Internal Functions/Classes:**
  * `infer_node` (Impact: 3216.5 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 266`, `structural_boundaries: 230`, `args: 28`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 18`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `api: 14`, `concurrency: 6`, `import: 25`
* *Defense:* `safety: 27`, `doc: 21`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 24.917
  * `Choke Point (Betweenness):` 0.018301 | `Ripple Effect (Closeness):` 0.281255
  * `Imports (Out-Degree: 11):` jedi.inference.context, jedi.inference.helpers, jedi.inference.names, itertools, jedi.inference.base_value, jedi.inference.value.dynamic_arrays, jedi.inference.compiled.access, jedi.inference.gradual...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `jedi/api/completion.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.986 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.61 IQR)
- **Top Global Matches:** file_cluster_13: 9.986, file_cluster_8: 10.043, file_cluster_7: 10.367
- **Magnitude:** 1381.1 | **LOC:** 697 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (39.3815%), Tech Debt (9.1123%)
**Top Internal Functions/Classes:**
  * `_extract_string_while_in_string` (Impact: 481.2 | O(N^6) | DB: 3)
  * `_complete_python` (Impact: 354.9 | O(N^6) | DB: 5)
  * `_complete_trailer` (Impact: 175.0 | O(N^6))
  * `filter_names` (Impact: 120.2 | O(N^6))
  * `complete` (Impact: 69.0 | O(N^6) | DB: 1)
    * *Intent:* # Return list of completions in this order: # - Beginning with what user is typing # - Public (alpha...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 162`, `args: 31`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 29`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 15`, `import: 24`
* *Defense:* `safety: 10`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.208
  * `Choke Point (Betweenness):` 0.003361 | `Ripple Effect (Closeness):` 0.022959
  * `Imports (Out-Degree: 10):` inspect, jedi.inference.docstring_utils, jedi.inference.context, textwrap, jedi.inference.helpers, jedi.inference.names, jedi.inference.base_value, jedi.inference.gradual.conversion...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `jedi/inference/names.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.499 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.407 IQR)
- **Top Global Matches:** file_cluster_13: 10.499, file_cluster_8: 10.623, file_cluster_0: 10.73
- **Magnitude:** 1331.38 | **LOC:** 674 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (48.7166%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `goto` (Impact: 367.2 | O(2^N) | DB: 2)
  * `get_qualified_names` (Impact: 97.7 | O(2^N))
  * `__repr__` (Impact: 86.3 | O(2^N) | DB: 4)
  * `get_kind` (Impact: 74.1 | O(N^6))
  * `assignment_indexes` (Impact: 56.0 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 276`, `args: 77`, `func_start: 77`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 40`, `planned_debt: 1`, `duplicate_logic: 54`
* *Architecture:* `api: 78`, `concurrency: 6`, `import: 25`
* *Defense:* `safety: 3`, `doc: 10`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 43.816
  * `Choke Point (Betweenness):` 0.072446 | `Ripple Effect (Closeness):` 0.383529
  * `Imports (Out-Degree: 15):` inspect, or, nodes, jedi.inference.value.iterable, jedi.inference.helpers, jedi.inference.syntax_tree, jedi.cache, jedi.inference.param...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `jedi/inference/compiled/access.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.142 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.966 IQR)
- **Top Global Matches:** file_cluster_13: 11.142, file_cluster_8: 11.24, file_cluster_12: 11.505
- **Magnitude:** 1236.3 | **LOC:** 563 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (60.1729%), Tech Debt (56.9001%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 1073.0 | O(2^N) | DB: 7)
  * `get_api_type` (Impact: 24.7 | O(N^3))
  * `safe_getattr` (Impact: 20.9 | O(N^3))
  * `_is_class_instance` (Impact: 13.5 | O(N^2))
  * `load_module` (Impact: 13.3 | O(N^3) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 189`, `args: 53`, `func_start: 53`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 7`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 7`, `api: 49`, `import: 16`
* *Defense:* `safety: 60`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.222
  * `Choke Point (Betweenness):` 0.006711 | `Ripple Effect (Closeness):` 0.246554
  * `Imports (Out-Degree: 2):` types, pathlib, inspect, collections, traceback, operator, warnings, builtins...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `jedi/api/helpers.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.318 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.354 IQR)
- **Top Global Matches:** file_cluster_13: 9.318, file_cluster_8: 9.473, file_cluster_7: 9.569
- **Magnitude:** 1222.92 | **LOC:** 523 | **CtrlFlow:** 49.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (35.363%), Tech Debt (13.8698%)
**Top Internal Functions/Classes:**
  * `get_stack_at_position` (Impact: 908.3 | O(N^6) | DB: 4)
  * `_get_code_for_stack` (Impact: 66.9 | O(N^4))
  * `validate_line_column` (Impact: 55.6 | O(N^6))
  * `get_module_names` (Impact: 51.5 | O(N^4))
  * `sorted_definitions` (Impact: 24.5 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 157`, `args: 32`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 8`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 32`, `import: 14`
* *Defense:* `safety: 5`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.69
  * `Choke Point (Betweenness):` 0.002435 | `Ripple Effect (Closeness):` 0.05
  * `Imports (Out-Degree: 5):` jedi.inference.syntax_tree, jedi.cache, itertools, collections, functools, inspect, jedi.inference.base_value, jedi.parser_utils...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `jedi/inference/value/klass.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.658 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.786 IQR)
- **Top Global Matches:** file_cluster_13: 10.658, file_cluster_0: 10.98, file_cluster_11: 11.056
- **Magnitude:** 1218.5 | **LOC:** 695 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (21.4761%), Tech Debt (99.8651%)
**Top Internal Functions/Classes:**
  * `py__mro__` (Impact: 467.9 | O(2^N) | DB: 2)
    * *Intent:* """ param_names = [] filter_ = cls.as_context().get_global_filter() for name in sorted(filter_.value...
  * `is_typeddict` (Impact: 110.5 | O(2^N))
    * *Intent:* # If dataclass_transform is applied to a class, dataclass-like semantics # will be assumed for any c...
  * `get_metaclass_filters` (Impact: 85.0 | O(N^6))
  * `init_mode_from_new` (Impact: 42.7 | O(N^5))
  * `get_dataclass_param_names` (Impact: 35.9 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 200`, `args: 48`, `func_start: 47`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 28`, `dead_code: 1`, `planned_debt: 5`, `duplicate_logic: 9`
* *Architecture:* `api: 47`, `import: 29`
* *Defense:* `safety: 15`, `doc: 28`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.113
  * `Choke Point (Betweenness):` 0.011911 | `Ripple Effect (Closeness):` 0.241843
  * `Imports (Out-Degree: 17):` inspect, jedi.inference.context, jedi.inference.gradual.base, system., jedi.inference.names, jedi.inference.syntax_tree, jedi.inference.base_value, jedi.inference.gradual.annotation...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `jedi/inference/value/function.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.598 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.376 IQR)
- **Top Global Matches:** file_cluster_13: 9.598, file_cluster_8: 9.822, file_cluster_0: 9.976
- **Magnitude:** 1064.12 | **LOC:** 460 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (34.2539%), Tech Debt (12.4992%)
**Top Internal Functions/Classes:**
  * `get_type_hint` (Impact: 804.6 | O(2^N) | DB: 8)
  * `_find_overload_functions` (Impact: 80.0 | O(N^5))
  * `get_qualified_names` (Impact: 43.9 | O(2^N))
  * `get_filters` (Impact: 14.1 | O(2^N))
  * `name` (Impact: 14.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 171`, `args: 46`, `func_start: 46`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 18`, `planned_debt: 3`
* *Architecture:* `api: 49`, `import: 20`
* *Defense:* `safety: 4`, `doc: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.496
  * `Choke Point (Betweenness):` 0.009578 | `Ripple Effect (Closeness):` 0.224671
  * `Imports (Out-Degree: 13):` jedi.inference.names, jedi.inference.filters, jedi.inference.base_value, jedi.inference, jedi.inference.value, jedi.inference.gradual.annotation, jedi.inference.value.instance, jedi.inference.signature...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `jedi/inference/value/iterable.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.174 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.034 IQR)
- **Top Global Matches:** file_cluster_0: 11.174, file_cluster_13: 11.177, file_cluster_11: 11.583
- **Magnitude:** 1024.32 | **LOC:** 648 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (24.067%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 186.8 | O(2^N) | DB: 3)
  * `__repr__` (Impact: 186.2 | O(2^N) | DB: 1)
  * `get_tree_entries` (Impact: 111.3 | O(N^6) | DB: 2)
  * `__repr__` (Impact: 94.3 | O(N^6) | DB: 8)
  * `__init__` (Impact: 27.3 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 230`, `args: 76`, `func_start: 76`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 55`, `dead_code: 3`, `planned_debt: 3`, `duplicate_logic: 34`
* *Architecture:* `api: 62`, `import: 14`
* *Defense:* `safety: 12`, `doc: 22`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.815
  * `Choke Point (Betweenness):` 0.005035 | `Ripple Effect (Closeness):` 0.251453
  * `Imports (Out-Degree: 11):` jedi.inference.filters, jedi.inference.base_value, jedi.inference, jedi.parser_utils, jedi.inference.utils, jedi.inference.value.dynamic_arrays, jedi.inference.context, jedi.inference.gradual.generics...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `jedi/inference/compiled/value.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.545 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.334 IQR)
- **Top Global Matches:** file_cluster_13: 10.545, file_cluster_0: 10.68, file_cluster_8: 10.777
- **Magnitude:** 989.52 | **LOC:** 627 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (29.4392%), Tech Debt (99.9995%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 332.4 | O(2^N) | DB: 5)
  * `_parse_function_doc` (Impact: 93.6 | O(N^6))
  * `_get` (Impact: 68.6 | O(N^4))
  * `py__call__` (Impact: 63.4 | O(2^N))
  * `values` (Impact: 44.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 228`, `args: 82`, `func_start: 78`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 29`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 17`
* *Architecture:* `io: 1`, `api: 69`, `import: 21`
* *Defense:* `safety: 19`, `doc: 12`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.386
  * `Choke Point (Betweenness):` 0.033485 | `Ripple Effect (Closeness):` 0.336012
  * `Imports (Out-Degree: 12):` inspect, jedi.inference.context, jedi.inference.helpers, jedi.inference.names, jedi.cache, functools, jedi.inference.base_value, jedi.inference.compiled.access...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `jedi/inference/context.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.834 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.421 IQR)
- **Top Global Matches:** file_cluster_13: 9.834, file_cluster_0: 10.063, file_cluster_8: 10.063
- **Magnitude:** 988.36 | **LOC:** 499 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (19.6684%), Tech Debt (55.0503%)
**Top Internal Functions/Classes:**
  * `goto` (Impact: 571.0 | O(2^N) | DB: 2)
  * `create_context` (Impact: 249.4 | O(2^N) | DB: 2)
  * `_get_global_filters_for_name` (Impact: 49.0 | O(N^5))
  * `get_global_filters` (Impact: 13.1 | O(N^3))
  * `get_filters` (Impact: 6.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 197`, `args: 65`, `func_start: 65`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 68`, `import: 18`
* *Defense:* `safety: 12`, `doc: 11`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.316
  * `Choke Point (Betweenness):` 0.017972 | `Ripple Effect (Closeness):` 0.283354
  * `Imports (Out-Degree: 8):` jedi.inference.names, jedi.inference.syntax_tree, jedi.inference.finder, pathlib, contextlib, typing, jedi.inference.filters, jedi.inference.base_value...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `jedi/api/refactoring/extract.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.955 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.26 IQR)
- **Top Global Matches:** file_cluster_8: 8.955, file_cluster_7: 9.29, file_cluster_13: 9.337
- **Magnitude:** 952.34 | **LOC:** 387 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (16.4499%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `extract_function` (Impact: 263.5 | O(N^6))
  * `_remove_unwanted_expression_nodes` (Impact: 183.6 | O(2^N))
  * `_find_nodes` (Impact: 87.5 | O(N^4))
  * `_check_for_non_extractables` (Impact: 73.3 | O(2^N))
  * `_find_non_global_names` (Impact: 61.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 86`, `args: 19`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 9`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `safety: 5`, `doc: 12`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.757
  * `Choke Point (Betweenness):` 0.000158 | `Ripple Effect (Closeness):` 0.010204
  * `Imports (Out-Degree: 3):` jedi.api.exceptions, jedi.parser_utils, parso, jedi, jedi.common, textwrap, jedi.api.refactoring
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `jedi/inference/base_value.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.639 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.654 IQR)
- **Top Global Matches:** file_cluster_13: 10.639, file_cluster_8: 10.905, file_cluster_0: 10.93
- **Magnitude:** 909.3 | **LOC:** 559 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (22.78%), Tech Debt (92.4142%)
**Top Internal Functions/Classes:**
  * `_getitem` (Impact: 358.1 | O(2^N) | DB: 4)
  * `goto` (Impact: 157.8 | O(2^N))
  * `is_sub_class_of` (Impact: 39.2 | O(N^6) | DB: 2)
  * `_get_value_filters` (Impact: 22.1 | O(N^4))
  * `name` (Impact: 21.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 241`, `args: 90`, `func_start: 90`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 18`, `planned_debt: 4`, `duplicate_logic: 4`
* *Architecture:* `api: 95`, `import: 21`
* *Defense:* `safety: 16`, `doc: 17`, `test: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 89.898
  * `Choke Point (Betweenness):` 0.044796 | `Ripple Effect (Closeness):` 0.441505
  * `Imports (Out-Degree: 10):` jedi.inference.arguments, jedi.inference.names, jedi.cache, functools, itertools, jedi.parser_utils, operator, jedi.inference.utils...
  * `Imported By (In-Degree: 38):` (Excluded from Brief to save tokens)

### `jedi/api/classes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.473 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.261 IQR)
- **Top Global Matches:** file_cluster_13: 11.473, file_cluster_0: 11.602, file_cluster_8: 11.729
- **Magnitude:** 888.9 | **LOC:** 894 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (28.4307%), Tech Debt (99.8167%)
**Top Internal Functions/Classes:**
  * `description` (Impact: 456.0 | O(2^N) | DB: 6)
  * `type` (Impact: 83.9 | O(2^N))
    * *Intent:* """ Shows the file path of a module. e.g. ``/usr/lib/python3.9/os.py`` """
  * `docstring` (Impact: 28.7 | O(N^3))
  * `get_definition_end_position` (Impact: 22.4 | O(N^4))
  * `defined_names` (Impact: 21.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 199`, `args: 60`, `func_start: 58`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 25`, `planned_debt: 3`, `duplicate_logic: 8`
* *Architecture:* `io: 8`, `api: 54`, `import: 15`
* *Defense:* `safety: 10`, `doc: 108`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.675
  * `Choke Point (Betweenness):` 0.002371 | `Ripple Effect (Closeness):` 0.02449
  * `Imports (Out-Degree: 11):` jedi.api.keywords, a, json, jedi.inference.names, jedi.cache, jedi.inference.base_value, foo, jedi.api.helpers...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `jedi/inference/imports.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.878 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.526 IQR)
- **Top Global Matches:** file_cluster_13: 10.878, file_cluster_0: 11.242, file_cluster_8: 11.271
- **Magnitude:** 857.58 | **LOC:** 592 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (21.7932%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `infer_import` (Impact: 408.9 | O(N^6) | DB: 32)
  * `load_module_from_path` (Impact: 102.7 | O(2^N))
  * `import_module_by_names` (Impact: 87.1 | O(N^6))
  * `import_module` (Impact: 65.6 | O(N^3) | DB: 1)
  * `iter_module_names` (Impact: 59.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 120`, `args: 22`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 35`, `dead_code: 3`
* *Architecture:* `io: 8`, `api: 17`, `import: 24`
* *Defense:* `safety: 11`, `doc: 20`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.979
  * `Choke Point (Betweenness):` 0.030027 | `Ripple Effect (Closeness):` 0.281255
  * `Imports (Out-Degree: 12):` statements, jedi.inference.gradual.typeshed, does, a, for, .....foo, jedi.inference.names, in...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `jedi/inference/references.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.912 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.951 IQR)
- **Top Global Matches:** file_cluster_13: 9.912, file_cluster_8: 9.964, file_cluster_7: 10.144
- **Magnitude:** 810.58 | **LOC:** 320 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (19.0293%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `gitignored_paths` (Impact: 479.5 | O(2^N) | DB: 6)
  * `find_references` (Impact: 177.6 | O(N^6) | DB: 4)
  * `_resolve_names` (Impact: 35.3 | O(2^N))
  * `_find_defining_names` (Impact: 26.9 | O(N^4))
  * `_find_global_variables` (Impact: 26.7 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 64`, `args: 17`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 12`
* *Architecture:* `io: 2`, `api: 8`, `import: 9`
* *Defense:* `safety: 9`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.725
  * `Choke Point (Betweenness):` 0.008101 | `Ripple Effect (Closeness):` 0.182545
  * `Imports (Out-Degree: 6):` jedi.inference.names, os, jedi.inference.filters, jedi.inference.imports, parso, jedi.file_io, jedi.inference.gradual.conversion, re...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `jedi/plugins/django.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.337 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.62 IQR)
- **Top Global Matches:** file_cluster_13: 9.337, file_cluster_8: 9.511, file_cluster_0: 9.776
- **Magnitude:** 763.76 | **LOC:** 297 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (23.35%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_infer_field` (Impact: 510.1 | O(2^N) | DB: 2)
  * `_get_foreign_key_values` (Impact: 55.3 | O(N^6))
  * `py__get__` (Impact: 28.1 | O(2^N))
  * `_infer_scalar_field` (Impact: 20.9 | O(N^2))
  * `py__getitem__` (Impact: 20.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 100`, `args: 31`, `func_start: 31`, `class_start: 9`
* *Risk/State:* `state_mutation: 6`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 8`, `orphaned_logic: 4`
* *Architecture:* `api: 27`, `import: 12`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` jedi.inference.names, jedi.inference.filters, inspect, jedi.inference.base_value, jedi.inference.value.klass, jedi.inference.value.instance, jedi.inference.signature, jedi.inference.compiled.value...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jedi/api/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.539 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.158 IQR)
- **Top Global Matches:** file_cluster_13: 10.539, file_cluster_8: 10.788, file_cluster_7: 10.927
- **Magnitude:** 728.68 | **LOC:** 799 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (12.3963%), Tech Debt (14.8284%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 540.8 | O(N^6) | DB: 2)
  * `__init__` (Impact: 81.2 | O(N^4) | DB: 8)
    * *Intent:* # Jedi uses lots and lots of recursion. By setting this a little bit higher, we
  * `_get_module` (Impact: 45.4 | O(N^4))
  * `set_debug_function` (Impact: 7.1 | O(N^5))
  * `preload_module` (Impact: 5.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 143`, `args: 30`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 15`, `planned_debt: 5`
* *Architecture:* `io: 3`, `api: 23`, `import: 33`
* *Defense:* `safety: 7`, `doc: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` jedi.api.errors, jedi.api.refactoring.extract, jedi.api.completion, jedi.api.project, jedi.api.keywords, sys, jedi.inference.value.iterable, jedi.inference.helpers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jedi/inference/gradual/base.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.64 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.122 IQR)
- **Top Global Matches:** file_cluster_13: 10.64, file_cluster_0: 10.81, file_cluster_11: 11.06
- **Magnitude:** 725.86 | **LOC:** 435 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (35.384%), Tech Debt (99.9998%)
**Top Internal Functions/Classes:**
  * `get_type_hint` (Impact: 297.3 | O(2^N) | DB: 3)
  * `__repr__` (Impact: 199.7 | O(2^N) | DB: 4)
  * `py__stop_iteration_returns` (Impact: 52.5 | O(2^N))
  * `infer` (Impact: 21.3 | O(N^5))
  * `__repr__` (Impact: 13.7 | O(2^N) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 158`, `args: 58`, `func_start: 58`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 33`, `dead_code: 1`, `planned_debt: 4`, `duplicate_logic: 11`
* *Architecture:* `api: 39`, `import: 13`
* *Defense:* `safety: 9`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.349
  * `Choke Point (Betweenness):` 0.006565 | `Ripple Effect (Closeness):` 0.263676
  * `Imports (Out-Degree: 10):` jedi.inference.names, jedi.inference.base_value, jedi.inference.utils, jedi.inference.value.klass, jedi.inference.gradual.type_var, jedi.inference.gradual.annotation, jedi.inference.context, jedi.inference.gradual.generics...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `jedi/inference/star_args.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.844 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.604 IQR)
- **Top Global Matches:** file_cluster_13: 9.844, file_cluster_8: 9.962, file_cluster_7: 10.102
- **Magnitude:** 704.96 | **LOC:** 218 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (44.4055%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `process_params` (Impact: 551.2 | O(2^N) | DB: 9)
  * `_iter_nodes_for_param` (Impact: 50.1 | O(N^6))
  * `_remove_given_params` (Impact: 32.0 | O(N^3))
    * *Intent:* # Infer atom first values = context.infer_node(atom_expr.children[index]) for trailer2 in atom_expr....
  * `_goes_to_param_name` (Impact: 16.4 | O(N^3))
  * `_to_callables` (Impact: 11.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 35`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 28`
* *Architecture:* `api: 3`, `concurrency: 1`, `import: 7`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.549
  * `Choke Point (Betweenness):` 0.001802 | `Ripple Effect (Closeness):` 0.171807
  * `Imports (Out-Degree: 5):` jedi.inference.names, jedi.inference.arguments, jedi.inference.syntax_tree, inspect, jedi.inference.utils, jedi.inference.helpers
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `jedi/api/environment.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.36 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.659 IQR)
- **Top Global Matches:** file_cluster_13: 11.36, file_cluster_0: 11.65, file_cluster_7: 11.783
- **Magnitude:** 652.0 | **LOC:** 481 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 82
- **Risk Profile:** Cognitive Load (13.9355%), Tech Debt (13.1501%)
**Top Internal Functions/Classes:**
  * `_get_subprocess` (Impact: 473.0 | O(2^N) | DB: 82)
  * `_get_executable_path` (Impact: 81.1 | O(N^6) | DB: 21)
    * *Intent:* """ Ignores virtualenvs and returns the Python versions that were installed on your system. This mig...
  * `_is_safe` (Impact: 18.6 | O(N^3) | DB: 3)
  * `_is_unix_safe_simple` (Impact: 8.6 | O(N^2) | DB: 3)
  * `_sha256` (Impact: 7.2 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 101`, `args: 27`, `func_start: 27`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 25`, `planned_debt: 2`
* *Architecture:* `io: 38`, `api: 15`, `import: 12`
* *Defense:* `safety: 18`, `doc: 37`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.227
  * `Choke Point (Betweenness):` 0.002298 | `Ripple Effect (Closeness):` 0.030612
  * `Imports (Out-Degree: 2):` jedi.inference.compiled.subprocess, os, jedi.cache, collections, filecmp, typing, jedi.inference, parso...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `jedi/inference/arguments.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.526 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.737 IQR)
- **Top Global Matches:** file_cluster_13: 10.526, file_cluster_0: 10.814, file_cluster_8: 10.914
- **Magnitude:** 621.88 | **LOC:** 336 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (21.2344%), Tech Debt (13.1787%)
**Top Internal Functions/Classes:**
  * `iterate_argument_clinic` (Impact: 474.7 | O(N^6) | DB: 9)
  * `try_iter_content` (Impact: 52.8 | O(2^N))
    * *Intent:* """Helper method for static analysis."""
  * `_star_star_dict` (Impact: 32.0 | O(N^3))
  * `repack_with_argument_clinic` (Impact: 16.5 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 105`, `args: 28`, `func_start: 28`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 17`, `planned_debt: 2`
* *Architecture:* `api: 24`, `import: 12`
* *Defense:* `safety: 14`, `doc: 9`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.21
  * `Choke Point (Betweenness):` 0.005574 | `Ripple Effect (Closeness):` 0.313797
  * `Imports (Out-Degree: 6):` jedi.inference.names, itertools, jedi.inference.base_value, jedi.inference, jedi.inference.utils, jedi.inference.value, jedi.inference.value.instance, jedi...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `jedi/inference/compiled/subprocess/__init__.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.946 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.598 IQR)
- **Top Global Matches:** file_cluster_13: 11.946, file_cluster_0: 12.3, file_cluster_8: 12.359
- **Magnitude:** 608.0 | **LOC:** 513 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 51
- **Risk Profile:** Cognitive Load (14.952%), Tech Debt (10.4413%)
**Top Internal Functions/Classes:**
  * `_add_stderr_to_debug` (Impact: 540.0 | O(2^N) | DB: 51)
  * `_GeneralizedPopen` (Impact: 11.0 | O(N^3) | DB: 6)
  * `_enqueue_output` (Impact: 5.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 108`, `args: 35`, `func_start: 35`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 31`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 14`, `api: 14`, `concurrency: 1`, `import: 19`
* *Defense:* `safety: 38`, `doc: 14`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` jedi.inference.compiled.subprocess, os, functools, collections, typing, queue, traceback, jedi.cache...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jedi/parser_utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.659 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.842 IQR)
- **Top Global Matches:** file_cluster_13: 10.659, file_cluster_8: 10.731, file_cluster_7: 10.901
- **Magnitude:** 577.4 | **LOC:** 346 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (13.8075%), Tech Debt (16.9256%)
**Top Internal Functions/Classes:**
  * `get_executable_nodes` (Impact: 140.3 | O(2^N) | DB: 3)
    * *Intent:* """ For static analysis. """
  * `get_parent_scope` (Impact: 98.4 | O(N^6))
  * `get_signature` (Impact: 56.3 | O(N^4))
  * `expr_is_dotted` (Impact: 56.2 | O(2^N))
  * `get_following_comment_same_line` (Impact: 32.5 | O(N^3))
    * *Intent:* """ Move the `Node` start_pos. """
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 100`, `args: 23`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 9`, `planned_debt: 3`
* *Architecture:* `api: 27`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 15`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 29.454
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.3375
  * `Imports (Out-Degree: 0):` inspect, parso.cache, parso, weakref, ast, textwrap, re, parso.python
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `jedi/api/project.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.768 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.207 IQR)
- **Top Global Matches:** file_cluster_13: 11.768, file_cluster_0: 11.979, file_cluster_8: 12.197
- **Magnitude:** 553.02 | **LOC:** 449 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (36.6928%), Tech Debt (10.5488%)
**Top Internal Functions/Classes:**
  * `_search_func` (Impact: 129.3 | O(N^6) | DB: 1)
  * `__repr__` (Impact: 103.2 | O(N^4) | DB: 3)
  * `_get_sys_path` (Impact: 96.1 | O(N^6) | DB: 3)
  * `load` (Impact: 44.0 | O(2^N) | DB: 3)
  * `_try_to_skip_duplicates` (Impact: 37.1 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 95`, `args: 23`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 46`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 17`, `import: 14`
* *Defense:* `safety: 16`, `doc: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.776
  * `Choke Point (Betweenness):` 0.004195 | `Ripple Effect (Closeness):` 0.020408
  * `Imports (Out-Degree: 9):` pathlib, itertools, jedi.api.exceptions, jedi.inference.imports, jedi.api.completion, jedi.api.helpers, jedi.inference.references, jedi.file_io...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `jedi/api/refactoring/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.733 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.041 IQR)
- **Top Global Matches:** file_cluster_8: 9.733, file_cluster_13: 9.948, file_cluster_7: 10.209
- **Magnitude:** 546.12 | **LOC:** 265 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (15.7677%), Tech Debt (57.5939%)
**Top Internal Functions/Classes:**
  * `inline` (Impact: 307.4 | O(2^N))
  * `rename` (Impact: 51.1 | O(N^4))
  * `__repr__` (Impact: 44.0 | O(N^5) | DB: 3)
  * `get_diff` (Impact: 41.0 | O(N^4))
  * `apply` (Impact: 35.0 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 58`, `args: 17`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 8`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 14`, `import: 6`
* *Defense:* `safety: 7`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` jedi.api.exceptions, difflib, typing, pathlib, parso, jedi.inference.value.namespace
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `jedi/inference/value/iterable.py` (PYTHON) | Magnitude: 1024.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 423, structural_boundaries: 230, encapsulation: 136, branch: 92
- `jedi/inference/signature.py` (PYTHON) | Magnitude: 338.28 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 110, structural_boundaries: 60, encapsulation: 30, branch: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `jedi/inference/analysis.py` (PYTHON) | Magnitude: 348.5 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 139, structural_boundaries: 80, branch: 42, state_mutation: 25
- `jedi/plugins/__init__.py` (PYTHON) | Magnitude: 53.24 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 29, encapsulation: 16, structural_boundaries: 14, listeners: 9
- `jedi/file_io.py` (PYTHON) | Magnitude: 139.68 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 34, api: 19, args: 14
- `jedi/inference/cache.py` (PYTHON) | Magnitude: 143.18 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 34, branch: 15, api: 15
- `jedi/api/replstartup.py` (PYTHON) | Magnitude: 12.6 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, doc: 2, import: 2, encapsulation: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `jedi/api/completion_cache.py` (PYTHON) | Magnitude: 16.14 | Delta: **0.148 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, encapsulation: 10, structural_boundaries: 8, generics: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `deploy-master.sh` (SHELL) | Magnitude: 42.26 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 21, safety_bypasses: 17, branch: 11, structural_boundaries: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `jedi/api/exceptions.py` (PYTHON) | Magnitude: 15.6 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 5, class_start: 4, encapsulation: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `jedi/inference/param.py` (PYTHON) | Magnitude: 278.14 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 159, branch: 46, structural_boundaries: 46, state_mutation: 28
- `jedi/inference/gradual/utils.py` (PYTHON) | Magnitude: 28.38 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 9, branch: 4, safety: 3
- `jedi/inference/syntax_tree.py` (PYTHON) | Magnitude: 3267.98 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 613, branch: 266, structural_boundaries: 230, encapsulation: 63
- `jedi/inference/gradual/annotation.py` (PYTHON) | Magnitude: 502.96 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 267, structural_boundaries: 112, branch: 90, args: 24
- `jedi/inference/compiled/__init__.py` (PYTHON) | Magnitude: 52.98 | Delta: **0.121 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 25, args: 8, func_start: 8

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `jedi/inference/value/klass.py` -> Churn: **82.04%** | Cog Load: 21.4761% | Debt: 99.8651%
- `jedi/api/classes.py` -> Churn: **58.68%** | Cog Load: 28.4307% | Debt: 99.8167%
- `jedi/inference/context.py` -> Churn: **58.68%** | Cog Load: 19.6684% | Debt: 55.0503%
- `jedi/inference/filters.py` -> Churn: **58.68%** | Cog Load: 41.4767% | Debt: 100.0%
- `jedi/inference/names.py` -> Churn: **58.68%** | Cog Load: 48.7166% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `jedi/api/completion.py` -> **Dave Halter** (100.0% isolated ownership) | Magnitude: 1381.1
- `jedi/inference/names.py` -> **Dave Halter** (100.0% isolated ownership) | Magnitude: 1331.38
- `jedi/inference/compiled/access.py` -> **Mark Diekhans** (100.0% isolated ownership) | Magnitude: 1236.3
- `jedi/inference/value/klass.py` -> **Eric Masseran** (100.0% isolated ownership) | Magnitude: 1218.5
- `jedi/inference/value/function.py` -> **Dave Halter** (100.0% isolated ownership) | Magnitude: 1064.12

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `jedi/inference/names.py` -> **Severity: 5.285** (Bridge: 0.0724 * Flux: 72.948%)
- `jedi/inference/imports.py` -> **Severity: 2.3** (Bridge: 0.03 * Flux: 76.5908%)
- `jedi/inference/compiled/value.py` -> **Severity: 1.849** (Bridge: 0.0335 * Flux: 55.2127%)
- `jedi/inference/base_value.py` -> **Severity: 1.67** (Bridge: 0.0448 * Flux: 37.2852%)
- `jedi/inference/gradual/typing.py` -> **Severity: 1.572** (Bridge: 0.0666 * Flux: 23.589%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `jedi/cache.py` -> **Severity: 25.104** (Embedded: 0.3138 * Error Risk: 80.0%)
- `jedi/inference/cache.py` -> **Severity: 17.103** (Embedded: 0.3491 * Error Risk: 48.9873%)
- `jedi/inference/helpers.py` -> **Severity: 15.372** (Embedded: 0.336 * Error Risk: 45.748%)
- `jedi/inference/gradual/stub_value.py` -> **Severity: 13.117** (Embedded: 0.2566 * Error Risk: 51.1268%)
- `jedi/inference/param.py` -> **Severity: 12.577** (Embedded: 0.2498 * Error Risk: 50.3488%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `jedi/inference/base_value.py` -> **Severity: 8989.791** (Blast Radius: 89.898 * Doc Risk: 99.9999%)
- `jedi/inference/gradual/typing.py` -> **Severity: 6491.381** (Blast Radius: 64.914 * Doc Risk: 99.9997%)
- `jedi/inference/names.py` -> **Severity: 4381.6** (Blast Radius: 43.816 * Doc Risk: 100.0%)
- `jedi/inference/cache.py` -> **Severity: 3687.593** (Blast Radius: 36.886 * Doc Risk: 99.9727%)
- `jedi/inference/utils.py` -> **Severity: 3379.4** (Blast Radius: 33.794 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
