# ARCHITECTURAL_BRIEF: mypy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/mypy` |
| **Timestamp** | `2026-08-03T19:39:13.161930+00:00` |
| **Scan Duration** | `2.6s` |
| **Git Branch** | `master` |
| **Git Commit** | `d7e3268ddd200ff390989d7359dd1e1b42bb94df` |
| **Git Remote** | `https://github.com/python/mypy.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 242 malicious artifacts.

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
| Total Artifacts | 1866 |
| Analyzed Artifacts (Scanned) | 266 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1600 |
| Total LOC | 87815 |
| Volatility Index | 0.011 |
| % Scanned of codebase = | 14.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4292 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2026 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 18.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.8716 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 15 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 225 | 84062 | 84.6% |
| PLAINTEXT | 12 | 0 | 4.5% |
| CPP | 11 | 3554 | 4.1% |
| MARKDOWN | 7 | 0 | 2.6% |
| SHELL | 3 | 14 | 1.1% |
| XML | 3 | 0 | 1.1% |
| YAML | 1 | 75 | 0.4% |
| DOCKERFILE | 1 | 8 | 0.4% |
| CSS | 1 | 70 | 0.4% |
| MAKEFILE | 1 | 8 | 0.4% |
| BATCH | 1 | 24 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.384`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 89 | 33.5% |
| file_cluster_8 | 84 | 31.6% |
| file_cluster_16 | 63 | 23.7% |
| file_cluster_11 | 6 | 2.3% |
| file_cluster_0 | 3 | 1.1% |
| file_cluster_17 | 1 | 0.4% |
| file_cluster_12 | 1 | 0.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 19 | 7.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1600*

**Composition by Extension & Reason:**
- `.pyi`: 855x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.test`: 261x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 214x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 211 LOC), 1x Excluded (Machine-Generated Source Code Signature: 403 LOC)
- `.c`: 80x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 22x Excluded (Unsupported Extension: '.rst')
- `.h`: 49x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.typed`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.typed')
- `no_extension`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4772 LOC)
- `.yml`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.patch`: 7x Excluded (Unsupported Extension: '.patch'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pump`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 94.0 | 19.2 | 13.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 86.6 | 20.0 | 5.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 34.3 | 13.1 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 47.1 | 80.0 | 80.0 |
| API Exposure | 0.0 | 17.0 | 5.4 | 4.9 | 0.0 |
| Concurrency Exposure | 0.0 | 94.8 | 1.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 42.5 | 27.3 | 0.0 |
| Commented Logic Exposure | 0.0 | 10.9 | 1.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 90.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 7.6 | 1.6 | 1.1 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 13.3 | 6.7 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 70.8 | 100.0 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 64.8 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 55.0 | 99.8 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.3 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `mypy/modulefinder.py` (Hits: 81)
- `mypy/report.py` (Hits: 53)
- `mypy/dmypy_server.py` (Hits: 51)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **nodes.py** (`mypy/nodes.py`) — 83 inbound connections
2. **types.py** (`mypy/types.py`) — 78 inbound connections
3. **options.py** (`mypy/options.py`) — 41 inbound connections
4. **ops.py** (`mypyc/ir/ops.py`) — 40 inbound connections
5. **util.py** (`mypy/util.py`) — 33 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **semanal.py** (`mypy/semanal.py`) — 55 outbound dependencies
2. **checker.py** (`mypy/checker.py`) — 50 outbound dependencies
3. **checkexpr.py** (`mypy/checkexpr.py`) — 45 outbound dependencies
4. **gtest.cc** (`mypyc/external/googletest/src/gtest.cc`) — 37 outbound dependencies
5. **stubutil.py** (`mypy/stubutil.py`) — 34 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `check_enum` (@ `mypy/checker.py`) -> Impact: **10705.7** | LOC: 6302
- `function_fullname` (@ `mypy/semanal.py`) -> Impact: **5512.8** | LOC: 1380
- `visit_op_expr` (@ `mypy/checkexpr.py`) -> Impact: **5085.2** | LOC: 3255
- `__repr__` (@ `mypy/nodes.py`) -> Impact: **3344.4** | LOC: 1658
  * *Intent:* # Is this TempNode used to indicate absence of a right hand side in an annotated assignment? # (e.g. for 'x: int' the rvalue is TempNode(AnyType(TypeO...
- `typeddict_key_must_be_string_literal` (@ `mypy/messages.py`) -> Impact: **2499.1** | LOC: 1262
- `error_message_templates` (@ `mypy/modulefinder.py`) -> Impact: **1302.9** | LOC: 840
  * *Intent:* # Stub PyPI package (typically types-pkgname) known to exist but not installed.
- `__repr__` (@ `mypyc/ir/rtypes.py`) -> Impact: **1130.0** | LOC: 950
  * *Intent:* # If True, error/undefined value overlaps with a valid value. To # detect an exception, PyErr_Occurred() must be used in addition # to checking for er...
- `visit_func_def` (@ `mypy/stats.py`) -> Impact: **997.1** | LOC: 301
- `format` (@ `mypyc/ir/pprint.py`) -> Impact: **864.0** | LOC: 200
- `get_prefix` (@ `mypy/config_parser.py`) -> Impact: **573.3** | LOC: 311

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `extract_callable_type` (@ `mypy/checker.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Check override validity after we analyzed current definition.
- `visit_union_type` (@ `mypy/erasetype.py`) -> **O(2^N) [Recursive]**
- `visit_tuple_type` (@ `mypy/erasetype.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Normalize Tuple[*Tuple[X, ...], ...] -> Tuple[X, ...]
- `__repr__` (@ `mypy/nodes.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Is this TempNode used to indicate absence of a right hand side in an annotated assignment? # (e.g. for 'x: int' the rvalue is TempNode(AnyType(TypeO...
- `function_fullname` (@ `mypy/semanal.py`) -> **O(2^N) [Recursive]**
- `find_fixed_callable_return` (@ `mypy/semanal_infer.py`) -> **O(2^N) [Recursive]**
- `visit_func_def` (@ `mypy/stats.py`) -> **O(2^N) [Recursive]**
- `visit_with_stmt` (@ `mypyc/annotate.py`) -> **O(2^N) [Recursive]**
- `format` (@ `mypyc/ir/pprint.py`) -> **O(2^N) [Recursive]**
- `analyze_type_type_callee` (@ `mypy/checkexpr.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `error_message_templates` (@ `mypy/modulefinder.py`) -> DB Complexity: **264**
  * *Intent:* # Stub PyPI package (typically types-pkgname) known to exist but not installed.
- `check_enum` (@ `mypy/checker.py`) -> DB Complexity: **145**
- `__init__` (@ `mypy/options.py`) -> DB Complexity: **106**
- `__repr__` (@ `mypy/nodes.py`) -> DB Complexity: **103**
  * *Intent:* # Is this TempNode used to indicate absence of a right hand side in an annotated assignment? # (e.g. for 'x: int' the rvalue is TempNode(AnyType(TypeO...
- `function_fullname` (@ `mypy/semanal.py`) -> DB Complexity: **70**
- `console_entry` (@ `mypy/__main__.py`) -> DB Complexity: **66**
- `_daemonize_cb` (@ `mypy/dmypy_server.py`) -> DB Complexity: **66**
- `indentation_level` (@ `mypy/report.py`) -> DB Complexity: **66**
- `visit_mypy_file` (@ `mypy/strconv.py`) -> DB Complexity: **66**
- `__init__` (@ `mypyc/ir/ops.py`) -> DB Complexity: **64**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `mypy` | 111 | 99321.56 | 21.6% | 42.75% |
| `mypyc/ir` | 7 | 6033.84 | 32.22% | 46.63% |
| `mypy/plugins` | 11 | 4843.6 | 14.39% | 25.97% |
| `mypy/server` | 10 | 2684.82 | 15.16% | 32.99% |
| `misc` | 20 | 2280.98 | 14.68% | 22.9% |
| `mypyc/analysis` | 6 | 2171.16 | 18.9% | 66.55% |
| `mypyc` | 12 | 1821.98 | 23.61% | 25.56% |
| `mypyc/transform` | 10 | 1271.94 | 23.23% | 78.17% |
| `mypy/typeshed/stubs/mypy-extensions` | 1 | 371.23 | 11.01% | 0.0% |
| `__monolith__` | 9 | 345.96 | 4.13% | 5.09% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `mypy/erasetype.py` -> **100.0%** Exposure
- `mypy/error_formatter.py` -> **100.0%** Exposure
- `mypy/evalexpr.py` -> **100.0%** Exposure
- `mypy/git.py` -> **100.0%** Exposure
- `mypy/indirection.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `mypy/strconv.py` -> **100.0%** Exposure
- `mypy/stubdoc.py` -> **100.0%** Exposure
- `mypyc/analysis/blockfreq.py` -> **100.0%** Exposure
- `mypyc/options.py` -> **100.0%** Exposure
- `misc/docker/run.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `mypy/nodes.py` -> **0** Orphaned Functions | **225** Duplicates
- `mypy/types.py` -> **0** Orphaned Functions | **220** Duplicates
- `mypy/traverser.py` -> **0** Orphaned Functions | **184** Duplicates
- `mypy/visitor.py` -> **0** Orphaned Functions | **162** Duplicates
- `mypy/type_visitor.py` -> **0** Orphaned Functions | **104** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`misc/diff-cache.py`** -> AI Confidence: **99.31%**
2. **`misc/incremental_checker.py`** -> AI Confidence: **99.31%**
3. **`mypy/argmap.py`** -> AI Confidence: **99.31%**
4. **`mypy/checker.py`** -> AI Confidence: **99.31%**
5. **`mypy/checkexpr.py`** -> AI Confidence: **99.31%**
6. **`mypy/checkmember.py`** -> AI Confidence: **99.31%**
7. **`mypy/checkpattern.py`** -> AI Confidence: **99.31%**
8. **`mypy/checkstrformat.py`** -> AI Confidence: **99.31%**
9. **`mypy/config_parser.py`** -> AI Confidence: **99.31%**
10. **`mypy/constraints.py`** -> AI Confidence: **99.31%**
11. **`mypy/dmypy_server.py`** -> AI Confidence: **99.31%**
12. **`mypy/errors.py`** -> AI Confidence: **99.31%**
13. **`mypy/fastparse.py`** -> AI Confidence: **99.31%**
14. **`mypy/fixup.py`** -> AI Confidence: **99.31%**
15. **`mypy/inspections.py`** -> AI Confidence: **99.31%**
16. **`mypy/ipc.py`** -> AI Confidence: **99.31%**
17. **`mypy/join.py`** -> AI Confidence: **99.31%**
18. **`mypy/main.py`** -> AI Confidence: **99.31%**
19. **`mypy/meet.py`** -> AI Confidence: **99.31%**
20. **`mypy/memprofile.py`** -> AI Confidence: **99.31%**
21. **`mypy/messages.py`** -> AI Confidence: **99.31%**
22. **`mypy/modulefinder.py`** -> AI Confidence: **99.31%**
23. **`mypy/nativeparse.py`** -> AI Confidence: **99.31%**
24. **`mypy/options.py`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `misc/analyze_cache.py` -> **100.0%** Exposure
- `misc/cherry-pick-typeshed.py` -> **100.0%** Exposure
- `misc/diff-cache.py` -> **100.0%** Exposure
- `misc/gen_blog_post_html.py` -> **100.0%** Exposure
- `misc/incremental_checker.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `misc/cherry-pick-typeshed.py` -> **100.0%** Exposure
- `misc/incremental_checker.py` -> **100.0%** Exposure
- `misc/perf_checker.py` -> **100.0%** Exposure
- `misc/perf_compare.py` -> **100.0%** Exposure
- `misc/profile_check.py` -> **100.0%** Exposure
### Raw Memory Manipulation
- `mypyc/external/googletest/src/gtest-printers.cc` -> **0.2884%** Exposure
- `mypyc/external/googletest/src/gtest.cc` -> **0.0832%** Exposure
- `mypyc/external/googletest/src/gtest-port.cc` -> **0.007%** Exposure
- `mypyc/external/googletest/src/gtest-death-test.cc` -> **0.0032%** Exposure
- `mypyc/external/googletest/src/gtest-internal-inl.h` -> **0.0005%** Exposure
### Algorithmic DoS Exposure
- `misc/analyze_cache.py` -> **100.0%** Exposure
- `misc/analyze_typeform_stats.py` -> **100.0%** Exposure
- `misc/cherry-pick-typeshed.py` -> **100.0%** Exposure
- `misc/convert-cache.py` -> **100.0%** Exposure
- `misc/diff-cache.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2067` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `mypy/metastore.py` (PYTHON) -> Cumulative Risk: **824.89**
- **Archetype:** `file_cluster_13` (Distance: 12.007 IQR)
- **Magnitude:** 294.46 | **LOC:** 243 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `write` (Impact: 56.9), `write` (Impact: 23.1), `read` (Impact: 21.2)

### 2. `mypy/fastparse.py` (PYTHON) -> Cumulative Risk: **822.74**
- **Archetype:** `file_cluster_16` (Distance: 12.616 IQR)
- **Magnitude:** 2189.24 | **LOC:** 2257 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 27.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `fix_function_overloads` (Impact: 286.2), `visit_Call` (Impact: 87.5), `translate_type_params` (Impact: 68.3)

### 3. `mypy/stubdoc.py` (PYTHON) -> Cumulative Risk: **806.98**
- **Archetype:** `file_cluster_13` (Distance: 12.813 IQR)
- **Magnitude:** 962.62 | **LOC:** 546 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `add_token` (Impact: 403.0), `parse_all_signatures` (Impact: 43.0), `parse_signature` (Impact: 41.6)

### 4. `mypy/stubgenc.py` (PYTHON) -> Cumulative Risk: **801.71**
- **Archetype:** `file_cluster_11` (Distance: 12.008 IQR)
- **Magnitude:** 1070.6 | **LOC:** 1047 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `generate_module` (Impact: 246.3), `get_default_function_sig` (Impact: 229.3), `_indent_docstring` (Impact: 61.5)

### 5. `mypy/types.py` (PYTHON) -> Cumulative Risk: **801.68**
- **Archetype:** `file_cluster_16` (Distance: 13.132 IQR)
- **Magnitude:** 3160.54 | **LOC:** 4453 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 47.2%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `read` (Impact: 123.6), `write` (Impact: 105.3), `with_normalized_var_args` (Impact: 82.1)

### 6. `mypyc/analysis/ircheck.py` (PYTHON) -> Cumulative Risk: **795.5**
- **Archetype:** `file_cluster_16` (Distance: 11.741 IQR)
- **Magnitude:** 807.98 | **LOC:** 499 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `check_op_sources_valid` (Impact: 99.9), `can_coerce_to` (Impact: 87.7), `check_tuple_items_valid_literals` (Impact: 67.4)

### 7. `mypy/nodes.py` (PYTHON) -> Cumulative Risk: **795.16**
- **Archetype:** `file_cluster_16` (Distance: 13.095 IQR)
- **Magnitude:** 5901.16 | **LOC:** 5368 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 64.3%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `__repr__` (Impact: 3344.4), `is_trivial_self` (Impact: 104.8), `deserialize` (Impact: 53.5)

### 8. `mypyc/ir/ops.py` (PYTHON) -> Cumulative Risk: **789.94**
- **Archetype:** `file_cluster_16` (Distance: 13.052 IQR)
- **Magnitude:** 1540.54 | **LOC:** 2107 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 293.6), `__repr__` (Impact: 194.6), `__init__` (Impact: 18.2)

### 9. `misc/profile_check.py` (PYTHON) -> Cumulative Risk: **787.39**
- **Archetype:** `file_cluster_13` (Distance: 10.682 IQR)
- **Magnitude:** 74.54 | **LOC:** 146 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `check_requirements` (Impact: 21.8), `_profile_type_check` (Impact: 18.2), `main` (Impact: 15.1)

### 10. `mypy/type_visitor.py` (PYTHON) -> Cumulative Risk: **786.44**
- **Archetype:** `file_cluster_16` (Distance: 10.938 IQR)
- **Magnitude:** 663.3 | **LOC:** 613 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `query_types` (Impact: 55.7), `visit_callable_type` (Impact: 20.4), `visit_union_type` (Impact: 16.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `mypy/checker.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.455 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.863 IQR)
- **Top Global Matches:** file_cluster_11: 14.455, file_cluster_16: 14.498, file_cluster_13: 14.562
- **Magnitude:** 14341.48 | **LOC:** 9583 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 44.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 145
- **Risk Profile:** Cognitive Load (31.78%), Tech Debt (21.6474%)
**Top Internal Functions/Classes:**
  * `check_enum` (Impact: 10705.7 | O(N^6) | DB: 145)
  * `extract_callable_type` (Impact: 240.8 | O(2^N) | DB: 1)
    * *Intent:* # Check override validity after we analyzed current definition.
  * `_visit_overloaded_func_def` (Impact: 217.2 | O(N^6) | DB: 1)
    * *Intent:* # If exit_condition is set, assume it must be False on exit from the loop: if exit_condition: _, els...
  * `visit_class_def` (Impact: 198.0 | O(N^6) | DB: 4)
  * `check_overlapping_overloads` (Impact: 188.0 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2371`, `structural_boundaries: 1549`, `args: 345`, `func_start: 341`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 100`, `state_mutation: 553`, `dead_code: 25`, `planned_debt: 70`, `fragile_debt: 9`, `duplicate_logic: 2`
* *Architecture:* `api: 337`, `concurrency: 2`, `import: 47`
* *Defense:* `safety: 727`, `doc: 334`, `test: 74`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.188
  * `Choke Point (Betweenness):` 0.00666 | `Ripple Effect (Closeness):` 0.038133
  * `Imports (Out-Degree: 40):` mypy.treetransform, unfollowed, mypy.patterns, mypy.plugin, mypy.erasetype, mypy.util, typing, mypy.scope...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `mypy/semanal.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.25 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.728 IQR)
- **Top Global Matches:** file_cluster_16: 14.25, file_cluster_11: 14.251, file_cluster_8: 14.274
- **Magnitude:** 10103.66 | **LOC:** 8436 | **CtrlFlow:** 61.0% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 70
- **Risk Profile:** Cognitive Load (33.4483%), Tech Debt (15.387%)
**Top Internal Functions/Classes:**
  * `function_fullname` (Impact: 5512.8 | O(2^N) | DB: 70)
  * `check_and_set_up_type_alias` (Impact: 363.3 | O(N^5))
  * `store_final_status` (Impact: 172.7 | O(N^6))
    * *Intent:* """Check if s defines a typed dict."""
  * `should_wait_rhs` (Impact: 157.0 | O(2^N))
  * `visit_import_from` (Impact: 156.2 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2220`, `structural_boundaries: 1422`, `args: 345`, `func_start: 342`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 69`, `state_mutation: 579`, `dead_code: 19`, `planned_debt: 42`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 350`, `concurrency: 10`, `import: 37`
* *Defense:* `safety: 648`, `doc: 276`, `test: 102`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.802
  * `Choke Point (Betweenness):` 0.002918 | `Ripple Effect (Closeness):` 0.035735
  * `Imports (Out-Degree: 27):` mypy.patterns, mypy.plugin, Y, x, somewhere, mypy.util, typing, mypy.tvar_scope...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `mypy/checkexpr.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.787 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.726 IQR)
- **Top Global Matches:** file_cluster_16: 13.787, file_cluster_8: 13.818, file_cluster_11: 13.82
- **Magnitude:** 7620.88 | **LOC:** 6998 | **CtrlFlow:** 60.3% | **Authorship Centralization:** 35.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 61
- **Risk Profile:** Cognitive Load (21.9869%), Tech Debt (17.6101%)
**Top Internal Functions/Classes:**
  * `visit_op_expr` (Impact: 5085.2 | O(N^6) | DB: 61)
  * `visit_call_expr_inner` (Impact: 441.5 | O(N^6) | DB: 1)
  * `analyze_type_type_callee` (Impact: 170.2 | O(2^N))
  * `defn_returns_none` (Impact: 125.8 | O(2^N))
  * `analyze_ref_expr` (Impact: 116.2 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1569`, `structural_boundaries: 1031`, `args: 223`, `func_start: 212`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 78`, `state_mutation: 297`, `dead_code: 26`, `planned_debt: 36`, `fragile_debt: 6`, `duplicate_logic: 2`
* *Architecture:* `api: 223`, `import: 44`
* *Defense:* `safety: 484`, `doc: 256`, `test: 50`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.436
  * `Choke Point (Betweenness):` 0.001845 | `Ripple Effect (Closeness):` 0.029373
  * `Imports (Out-Degree: 35):` mypy.lookup, mypy.plugin, mypy.erasetype, typing, mypy.tvar_scope, cycles., mypy.semanal_enum, mypy.checker...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mypy/nodes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.095 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.895 IQR)
- **Top Global Matches:** file_cluster_16: 13.095, file_cluster_0: 13.159, file_cluster_11: 13.224
- **Magnitude:** 5901.16 | **LOC:** 5368 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 64.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 103
- **Risk Profile:** Cognitive Load (29.6097%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 3344.4 | O(2^N) | DB: 103)
    * *Intent:* # Is this TempNode used to indicate absence of a right hand side in an annotated assignment? # (e.g....
  * `is_trivial_self` (Impact: 104.8 | O(2^N) | DB: 3)
    * *Intent:* # TODO: figure out how to reliably set end position (we don't know the impl here). self.set_line(ite...
  * `deserialize` (Impact: 53.5 | O(2^N))
  * `serialize` (Impact: 53.2 | O(2^N))
    * *Intent:* # the majority). In cases where self is not annotated and there are no Self # in the signature we ca...
  * `deserialize` (Impact: 44.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 382`, `structural_boundaries: 938`, `args: 328`, `func_start: 328`, `class_start: 99`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 615`, `dead_code: 15`, `planned_debt: 25`, `fragile_debt: 4`, `duplicate_logic: 225`
* *Architecture:* `io: 1`, `api: 343`, `import: 17`
* *Defense:* `safety: 126`, `doc: 202`, `test: 76`, `immutability_locks: 136`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 53.267
  * `Choke Point (Betweenness):` 0.031307 | `Ripple Effect (Closeness):` 0.341693
  * `Imports (Out-Degree: 9):` mypy_extensions, mypy.patterns, mypy.util, typing, m, mypy.types, mypy.visitor, nodes...
  * `Imported By (In-Degree: 83):` (Excluded from Brief to save tokens)

### `mypy/messages.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.029 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.764 IQR)
- **Top Global Matches:** file_cluster_8: 12.029, file_cluster_16: 12.03, file_cluster_13: 12.291
- **Magnitude:** 3379.86 | **LOC:** 3428 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 39.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (22.2977%), Tech Debt (8.793%)
**Top Internal Functions/Classes:**
  * `typeddict_key_must_be_string_literal` (Impact: 2499.1 | O(N^6) | DB: 22)
  * `dangerous_comparison` (Impact: 70.1 | O(N^6))
  * `requires_int_or_single_byte` (Impact: 35.8 | O(N^4))
  * `reveal_locals` (Impact: 34.1 | O(N^4))
  * `ignore_last_known_values` (Impact: 30.8 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 759`, `structural_boundaries: 624`, `args: 193`, `func_start: 191`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 110`, `dead_code: 2`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `api: 244`, `concurrency: 3`, `import: 21`
* *Defense:* `safety: 146`, `doc: 94`, `test: 13`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.125
  * `Choke Point (Betweenness):` 0.01016 | `Ripple Effect (Closeness):` 0.181764
  * `Imports (Out-Degree: 12):` mypy.erasetype, mypy.util, typing, mypy.typetraverser, mypy, mypy.errors, itertools, mypy.types...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `mypy/types.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.132 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.919 IQR)
- **Top Global Matches:** file_cluster_16: 13.132, file_cluster_0: 13.219, file_cluster_11: 13.3
- **Magnitude:** 3160.54 | **LOC:** 4453 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 47.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (38.8153%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `read` (Impact: 123.6 | O(2^N))
  * `write` (Impact: 105.3 | O(2^N))
    * *Intent:* # # Or more broadly, this field lets this Instance "remember" its original declaration # when applic...
  * `with_normalized_var_args` (Impact: 82.1 | O(N^6))
  * `deserialize` (Impact: 70.4 | O(2^N))
    * *Intent:* # Normalize also single item tuples like # *args: *Tuple[*tuple[X, ...]] -> *args: X # *args: *Tuple...
  * `serialize` (Impact: 56.5 | O(2^N))
    * *Intent:* # Boilerplate: var_arg_index = self.arg_kinds.index(ARG_STAR) types_prefix = self.arg_types[:var_arg...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 666`, `structural_boundaries: 1132`, `args: 385`, `func_start: 385`, `class_start: 45`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 470`, `dead_code: 4`, `planned_debt: 16`, `fragile_debt: 3`, `duplicate_logic: 220`
* *Architecture:* `io: 1`, `api: 350`, `import: 16`
* *Defense:* `safety: 195`, `doc: 130`, `test: 101`, `immutability_locks: 103`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 48.712
  * `Choke Point (Betweenness):` 0.023228 | `Ripple Effect (Closeness):` 0.305048
  * `Imports (Out-Degree: 9):` mypy.bogus_type, mypy.state, sys, mypy.expandtype, abc, typing_extensions, mypy.util, typing...
  * `Imported By (In-Degree: 78):` (Excluded from Brief to save tokens)

### `mypy/typeanal.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.438 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.712 IQR)
- **Top Global Matches:** file_cluster_8: 12.438, file_cluster_16: 12.486, file_cluster_11: 12.592
- **Magnitude:** 2715.94 | **LOC:** 2804 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 27.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (35.0373%), Tech Debt (89.1499%)
**Top Internal Functions/Classes:**
  * `visit_unbound_type_nonoptional` (Impact: 557.2 | O(N^6) | DB: 1)
    * *Intent:* # We don't need to worry about double-wrapping Optionals or # wrapping Anys: Union simplification wi...
  * `try_analyze_special_unbound_type` (Impact: 479.8 | O(N^6) | DB: 2)
  * `analyze_literal_param` (Impact: 272.5 | O(2^N) | DB: 1)
  * `validate_instance` (Impact: 206.7 | O(N^6))
  * `check_and_warn_deprecated` (Impact: 91.0 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 637`, `structural_boundaries: 609`, `args: 128`, `func_start: 127`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 205`, `dead_code: 2`, `planned_debt: 24`, `fragile_debt: 1`, `duplicate_logic: 22`
* *Architecture:* `api: 134`, `import: 20`
* *Defense:* `safety: 166`, `doc: 50`, `test: 30`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.82
  * `Choke Point (Betweenness):` 0.000517 | `Ripple Effect (Closeness):` 0.037781
  * `Imports (Out-Degree: 15):` mypy.plugin, typing, mypy.tvar_scope, was, mypy, mypy.types_utils, mypy.errors, itertools...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `mypy/subtypes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.472 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.825 IQR)
- **Top Global Matches:** file_cluster_8: 11.472, file_cluster_13: 11.649, file_cluster_16: 11.684
- **Magnitude:** 2583.62 | **LOC:** 2319 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (34.3128%), Tech Debt (40.0105%)
**Top Internal Functions/Classes:**
  * `visit_instance` (Impact: 414.5 | O(N^6))
    * *Intent:* # None is compatible with Hashable (and other similar protocols). This is # None is also compatible ...
  * `visit_callable_type` (Impact: 197.0 | O(N^6))
  * `restrict_subtype_away` (Impact: 175.9 | O(2^N))
  * `visit_overloaded` (Impact: 173.8 | O(N^6))
    * *Intent:* # Non-required key is not compatible with a required key since # indexing may fail unexpectedly if a...
  * `variadic_tuple_subtype` (Impact: 164.9 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 633`, `structural_boundaries: 522`, `args: 64`, `func_start: 64`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 37`, `dead_code: 7`, `planned_debt: 21`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 82`, `import: 21`
* *Defense:* `safety: 156`, `doc: 40`, `test: 33`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.028
  * `Choke Point (Betweenness):` 0.026523 | `Ripple Effect (Closeness):` 0.187262
  * `Imports (Out-Degree: 16):` mypy.erasetype, typing, mypy.applytype, mypy.checker_state, mypy.types_utils, mypy.types, mypy.solve, mypy.options...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `mypy/traverser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.037 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.89 IQR)
- **Top Global Matches:** file_cluster_16: 10.037, file_cluster_8: 10.261, file_cluster_13: 10.789
- **Magnitude:** 2331.68 | **LOC:** 1106 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (11.3394%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `visit_try_stmt` (Impact: 35.7 | O(N^4))
  * `visit_func` (Impact: 30.6 | O(N^5))
    * *Intent:* # Visit methods
  * `visit_template_str_expr` (Impact: 30.4 | O(N^5))
  * `visit_class_def` (Impact: 24.6 | O(N^3))
  * `visit_if_stmt` (Impact: 16.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 340`, `args: 198`, `func_start: 198`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 30`, `planned_debt: 1`, `duplicate_logic: 184`
* *Architecture:* `api: 210`, `import: 5`
* *Defense:* `safety: 3`, `doc: 8`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.749
  * `Choke Point (Betweenness):` 0.000311 | `Ripple Effect (Closeness):` 0.085763
  * `Imports (Out-Degree: 4):` mypy.patterns, mypy_extensions, mypy.visitor, __future__, mypy.nodes
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `mypy/fastparse.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.616 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.188 IQR)
- **Top Global Matches:** file_cluster_16: 12.616, file_cluster_8: 12.681, file_cluster_17: 12.729
- **Magnitude:** 2189.24 | **LOC:** 2257 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 27.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (36.375%), Tech Debt (96.6584%)
**Top Internal Functions/Classes:**
  * `fix_function_overloads` (Impact: 286.2 | O(N^6) | DB: 23)
  * `visit_Call` (Impact: 87.5 | O(N^6))
  * `translate_type_params` (Impact: 68.3 | O(N^6) | DB: 6)
  * `_strip_contents_from_if_stmt` (Impact: 52.5 | O(2^N))
    * *Intent:* # always False condition with no else
  * `_is_stripped_if_stmt` (Impact: 42.4 | O(2^N))
    * *Intent:* # body will be set unreachable if condition is always False # else_body can contain an IfStmt itself...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 451`, `structural_boundaries: 404`, `args: 142`, `func_start: 141`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 207`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 27`
* *Architecture:* `io: 8`, `api: 197`, `import: 19`
* *Defense:* `safety: 122`, `doc: 34`, `test: 15`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.076
  * `Choke Point (Betweenness):` 0.000921 | `Ripple Effect (Closeness):` 0.035734
  * `Imports (Out-Degree: 11):` mypy, ast, mypy.errors, mypy.patterns, mypy.types, sys, mypy.message_registry, warnings...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `mypy/constraints.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.375 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.208 IQR)
- **Top Global Matches:** file_cluster_11: 13.375, file_cluster_16: 13.403, file_cluster_13: 13.473
- **Magnitude:** 2115.36 | **LOC:** 1688 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (53.8571%), Tech Debt (46.7316%)
**Top Internal Functions/Classes:**
  * `visit_instance` (Impact: 510.8 | O(N^6) | DB: 38)
    * *Intent:* # Errors # We can't do anything useful with a partial type here. assert False, "Internal error" # No...
  * `any_constraints` (Impact: 266.4 | O(2^N) | DB: 1)
  * `visit_callable_type` (Impact: 250.5 | O(N^6) | DB: 8)
  * `visit_tuple_type` (Impact: 168.7 | O(N^6) | DB: 5)
  * `filter_satisfiable` (Impact: 56.0 | O(N^4) | DB: 2)
    * *Intent:* # All options have same structure. In this case we can merge-in trivial # TODO: More generally, if a...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 405`, `structural_boundaries: 321`, `args: 54`, `func_start: 54`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 261`, `dead_code: 2`, `planned_debt: 15`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `api: 72`, `import: 13`
* *Defense:* `safety: 170`, `doc: 48`, `test: 39`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.59
  * `Choke Point (Betweenness):` 0.002277 | `Ripple Effect (Closeness):` 0.147604
  * `Imports (Out-Degree: 10):` mypy.maptype, mypy.types_utils, mypy.argmap, mypy.typeops, mypy.types, mypy.infer, mypy.erasetype, mypy.subtypes...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `mypy/typeops.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.937 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.335 IQR)
- **Top Global Matches:** file_cluster_13: 12.937, file_cluster_11: 12.961, file_cluster_17: 12.978
- **Magnitude:** 1935.64 | **LOC:** 1345 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 44.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (13.8501%), Tech Debt (13.671%)
**Top Internal Functions/Classes:**
  * `type_object_type` (Impact: 292.6 | O(2^N))
  * `false_only` (Impact: 242.1 | O(2^N))
    * *Intent:* # If deleted subtypes had more general truthiness, use that
  * `custom_special_method` (Impact: 161.4 | O(2^N))
    * *Intent:* # Non-empty enums cannot subclass each other so simply removing duplicates is enough. items = [ try_...
  * `_remove_redundant_union_items` (Impact: 149.3 | O(N^6) | DB: 1)
  * `true_only` (Impact: 89.3 | O(2^N))
    * *Intent:* # This is an optimisation for unions with many LiteralType # the LiteralType must be a super type of...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 306`, `args: 52`, `func_start: 52`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 33`, `dead_code: 9`, `planned_debt: 10`
* *Architecture:* `api: 68`, `import: 18`
* *Defense:* `safety: 114`, `doc: 62`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.99
  * `Choke Point (Betweenness):` 0.014847 | `Ripple Effect (Closeness):` 0.193459
  * `Imports (Out-Degree: 12):` mypy.maptype, itertools, mypy.state, mypy.types, mypy.expandtype, mypy.copytype, mypy.infer, mypy.subtypes...
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `mypy/meet.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.635 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.853 IQR)
- **Top Global Matches:** file_cluster_8: 12.635, file_cluster_11: 12.679, file_cluster_13: 12.687
- **Magnitude:** 1829.3 | **LOC:** 1276 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (21.8292%), Tech Debt (16.0124%)
**Top Internal Functions/Classes:**
  * `narrow_declared_type` (Impact: 474.0 | O(2^N))
  * `visit_instance` (Impact: 216.4 | O(N^6) | DB: 2)
  * `meet_tuples` (Impact: 135.6 | O(N^5) | DB: 6)
    * *Intent:* # TODO: Implement a better algorithm that covers at least the same cases # as TypeJoinVisitor.visit_...
  * `meet_types` (Impact: 106.0 | O(N^5))
  * `visit_callable_type` (Impact: 70.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 382`, `structural_boundaries: 368`, `args: 47`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 50`, `dead_code: 3`, `planned_debt: 11`, `fragile_debt: 1`
* *Architecture:* `api: 69`, `import: 11`
* *Defense:* `safety: 187`, `doc: 32`, `test: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.037
  * `Choke Point (Betweenness):` 0.001465 | `Ripple Effect (Closeness):` 0.151864
  * `Imports (Out-Degree: 8):` mypy, mypy.maptype, mypy.state, mypy.typeops, mypy.types, mypy.erasetype, mypy.subtypes, __future__...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `mypy/nativeparse.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.479 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.398 IQR)
- **Top Global Matches:** file_cluster_8: 11.479, file_cluster_16: 11.828, file_cluster_13: 11.838
- **Magnitude:** 1813.26 | **LOC:** 2095 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (20.0967%), Tech Debt (8.6846%)
**Top Internal Functions/Classes:**
  * `read_statement` (Impact: 525.3 | O(2^N) | DB: 13)
  * `read_type` (Impact: 379.5 | O(2^N) | DB: 1)
  * `read_pattern` (Impact: 178.4 | O(2^N) | DB: 4)
    * *Intent:* # Process keyword arguments for kw_name, kw_value in kwargs: if kw_name == "name": # MULTIPLE_VALUES...
  * `read_call_type` (Impact: 109.3 | O(N^5) | DB: 1)
  * `read_func_def` (Impact: 89.3 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 417`, `structural_boundaries: 221`, `args: 38`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 192`, `planned_debt: 4`
* *Architecture:* `io: 1`, `api: 39`, `import: 15`
* *Defense:* `safety: 53`, `doc: 38`, `test: 21`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.496
  * `Choke Point (Betweenness):` 0.000175 | `Ripple Effect (Closeness):` 0.019211
  * `Imports (Out-Degree: 10):` mypy, mypy.patterns, mypy.types, statement., dependencies, ast_serialize, os, mypy.util...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mypy/join.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 12.691 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.034 IQR)
- **Top Global Matches:** file_cluster_11: 12.691, file_cluster_13: 12.765, file_cluster_16: 12.837
- **Magnitude:** 1709.4 | **LOC:** 917 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (31.8618%), Tech Debt (75.7011%)
**Top Internal Functions/Classes:**
  * `join_tuples` (Impact: 236.1 | O(N^6) | DB: 9)
  * `join_instances` (Impact: 207.8 | O(N^6) | DB: 7)
  * `object_or_any_from_type` (Impact: 145.1 | O(2^N))
    * *Intent:* """ num_args = len(t.arg_types) new_names = [] for i in range(num_args): t_name = t.arg_names[i] s_n...
  * `visit_instance` (Impact: 100.4 | O(N^5) | DB: 1)
  * `visit_callable_type` (Impact: 95.4 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 280`, `args: 46`, `func_start: 46`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 87`, `dead_code: 2`, `planned_debt: 11`, `duplicate_logic: 4`
* *Architecture:* `api: 67`, `import: 12`
* *Defense:* `safety: 110`, `doc: 16`, `test: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.996
  * `Choke Point (Betweenness):` 5.7e-05 | `Ripple Effect (Closeness):` 0.124399
  * `Imports (Out-Degree: 8):` mypy.maptype, mypy.state, mypy.typeops, mypy.types, mypy.expandtype, mypy.subtypes, mypy.meet, typing...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `mypyc/ir/rtypes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.027 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.992 IQR)
- **Top Global Matches:** file_cluster_0: 13.027, file_cluster_16: 13.035, file_cluster_11: 13.203
- **Magnitude:** 1621.58 | **LOC:** 1445 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 64.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 52
- **Risk Profile:** Cognitive Load (38.1377%), Tech Debt (99.9685%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 1130.0 | O(2^N) | DB: 52)
    * *Intent:* # If True, error/undefined value overlaps with a valid value. To # detect an exception, PyErr_Occurr...
  * `flatten_nested_unions` (Impact: 48.5 | O(2^N) | DB: 2)
  * `optional_value_type` (Impact: 20.4 | O(N^3))
  * `make_simplified_union` (Impact: 12.6 | O(N^3))
  * `__eq__` (Impact: 10.7 | O(N^3) | DB: 2)
    * *Intent:* # We compare based on the set because order in a union doesn't matter def __eq__(self, other: object...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 335`, `args: 136`, `func_start: 136`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 162`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 25`
* *Architecture:* `api: 113`, `import: 8`
* *Defense:* `safety: 106`, `doc: 42`, `test: 18`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 25.435
  * `Choke Point (Betweenness):` 0.007949 | `Ripple Effect (Closeness):` 0.199321
  * `Imports (Out-Degree: 3):` mypyc.common, mypyc.namegen, abc, mypyc.ir.deps, typing, __future__, mypyc.ir.ops, mypyc.ir.class_ir
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `mypyc/ir/ops.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.052 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.079 IQR)
- **Top Global Matches:** file_cluster_16: 13.052, file_cluster_0: 13.197, file_cluster_13: 13.498
- **Magnitude:** 1540.54 | **LOC:** 2107 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 57.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 64
- **Risk Profile:** Cognitive Load (30.9501%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 293.6 | O(2^N) | DB: 64)
  * `__repr__` (Impact: 194.6 | O(2^N) | DB: 49)
  * `__init__` (Impact: 18.2 | O(N^3) | DB: 4)
  * `__init__` (Impact: 16.2 | O(2^N) | DB: 3)
  * `unique_sources` (Impact: 13.3 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 575`, `args: 250`, `func_start: 250`, `class_start: 54`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 297`, `planned_debt: 5`, `fragile_debt: 1`, `duplicate_logic: 81`
* *Architecture:* `api: 254`, `import: 11`
* *Defense:* `safety: 52`, `doc: 122`, `test: 35`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 36.899
  * `Choke Point (Betweenness):` 0.018058 | `Ripple Effect (Closeness):` 0.201999
  * `Imports (Out-Degree: 6):` mypy_extensions, mypyc.common, mypyc.ir.func_ir, abc, mypyc.codegen.literals, mypyc.ir.deps, typing, __future__...
  * `Imported By (In-Degree: 40):` (Excluded from Brief to save tokens)

### `mypy/modulefinder.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_11` (Drift: 11.92 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.342 IQR)
- **Top Global Matches:** file_cluster_11: 11.92, file_cluster_13: 11.927, file_cluster_16: 12.022
- **Magnitude:** 1525.36 | **LOC:** 1003 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(N^6) | **DB Complexity:** 264
- **Risk Profile:** Cognitive Load (39.7222%), Tech Debt (40.4106%)
**Top Internal Functions/Classes:**
  * `error_message_templates` (Impact: 1302.9 | O(N^6) | DB: 264)
    * *Intent:* # Stub PyPI package (typically types-pkgname) known to exist but not installed.
  * `load_stdlib_py_versions` (Impact: 50.3 | O(N^4) | DB: 9)
    * *Intent:* # If provided, insert the caller-supplied extra module path to the # beginning (highest priority) of...
  * `asdict` (Impact: 3.8 | O(N^3))
    * *Intent:* # paths in typeshed
  * `typeshed_py_version` (Impact: 2.3 | O(N^1))
  * `__init__` (Impact: 1.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 150`, `args: 32`, `func_start: 32`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 122`, `dead_code: 2`, `planned_debt: 15`, `fragile_debt: 4`
* *Architecture:* `io: 81`, `api: 29`, `import: 19`
* *Defense:* `safety: 17`, `doc: 34`, `test: 4`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.637
  * `Choke Point (Betweenness):` 0.004697 | `Ripple Effect (Closeness):` 0.038593
  * `Imports (Out-Degree: 8):` mypy.util, subprocess, typing, pathspec.patterns.gitignore, mypy, mypy.errors, os, mypy.options...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `mypy/suggestions.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.795 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.916 IQR)
- **Top Global Matches:** file_cluster_13: 12.795, file_cluster_16: 12.828, file_cluster_11: 12.879
- **Magnitude:** 1355.4 | **LOC:** 1069 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (19.4897%), Tech Debt (91.8864%)
**Top Internal Functions/Classes:**
  * `refine_type` (Impact: 89.8 | O(2^N))
    * *Intent:* # Note: for default arguments, we just assume that they # are required. This isn't right, but neithe...
  * `extract_from_decorator` (Impact: 84.6 | O(N^5) | DB: 1)
  * `find_node` (Impact: 74.6 | O(N^5) | DB: 3)
  * `visit_instance` (Impact: 66.5 | O(N^4))
  * `score_type` (Impact: 65.9 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 241`, `args: 66`, `func_start: 64`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 91`, `dead_code: 3`, `planned_debt: 6`, `fragile_debt: 1`, `duplicate_logic: 7`
* *Architecture:* `io: 3`, `api: 80`, `import: 25`
* *Defense:* `safety: 59`, `doc: 74`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.389
  * `Choke Point (Betweenness):` 0.001015 | `Ripple Effect (Closeness):` 0.006709
  * `Imports (Out-Degree: 16):` mypy.plugin, json, mypy.util, typing, mypy.checkexpr, mypy.build, mypy.types_utils, itertools...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mypy/strconv.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.979 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.124 IQR)
- **Top Global Matches:** file_cluster_16: 12.979, file_cluster_13: 13.119, file_cluster_11: 13.277
- **Magnitude:** 1335.58 | **LOC:** 708 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 66
- **Risk Profile:** Cognitive Load (76.841%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `visit_mypy_file` (Impact: 388.1 | O(N^5) | DB: 66)
  * `dump_tagged` (Impact: 101.3 | O(2^N) | DB: 6)
  * `func_helper` (Impact: 49.1 | O(N^4) | DB: 10)
  * `visit_call_expr` (Impact: 42.5 | O(N^5) | DB: 4)
  * `visit_template_str_expr` (Impact: 32.1 | O(N^5) | DB: 4)
    * *Intent:* # REVEAL_LOCALS
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 238`, `args: 98`, `func_start: 96`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 267`
* *Architecture:* `io: 3`, `api: 148`, `import: 16`
* *Defense:* `safety: 9`, `doc: 12`, `test: 2`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.347
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.222029
  * `Imports (Out-Degree: 6):` mypy.patterns, mypy.types, mypy.visitor, os, mypy.util, typing, mypy.options, re...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mypyc/ir/pprint.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.178 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.537 IQR)
- **Top Global Matches:** file_cluster_16: 12.178, file_cluster_13: 12.306, file_cluster_11: 12.413
- **Magnitude:** 1279.38 | **LOC:** 531 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (54.7964%), Tech Debt (16.3329%)
**Top Internal Functions/Classes:**
  * `format` (Impact: 864.0 | O(2^N) | DB: 29)
  * `visit_unbox` (Impact: 31.0 | O(N^4))
  * `visit_set_element` (Impact: 22.3 | O(N^4))
  * `visit_dec_ref` (Impact: 18.4 | O(N^3))
  * `visit_branch` (Impact: 18.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 144`, `args: 48`, `func_start: 48`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 88`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 70`, `import: 9`
* *Defense:* `safety: 24`, `doc: 10`, `test: 5`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.138
  * `Choke Point (Betweenness):` 0.012696 | `Ripple Effect (Closeness):` 0.192047
  * `Imports (Out-Degree: 5):` mypyc.ir.module_ir, mypyc.common, mypyc.ir.func_ir, collections, typing, __future__, mypyc.ir.rtypes, mypyc.ir.ops...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `mypy/checkpattern.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.777 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.933 IQR)
- **Top Global Matches:** file_cluster_13: 11.777, file_cluster_8: 11.78, file_cluster_16: 11.865
- **Magnitude:** 1249.06 | **LOC:** 880 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 38.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (34.0283%), Tech Debt (10.6355%)
**Top Internal Functions/Classes:**
  * `visit_sequence_pattern` (Impact: 317.4 | O(N^6) | DB: 6)
  * `visit_class_pattern` (Impact: 219.6 | O(N^6) | DB: 2)
  * `get_class_pattern_type_ranges` (Impact: 145.9 | O(2^N) | DB: 1)
  * `construct_sequence_child` (Impact: 91.3 | O(2^N))
    * *Intent:* # expressions, as suggested in the TODO above it's definition already_captured = {literal_hash(expr)...
  * `visit_mapping_pattern` (Impact: 69.9 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 155`, `args: 25`, `func_start: 25`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 66`, `planned_debt: 4`
* *Architecture:* `api: 35`, `import: 21`
* *Defense:* `safety: 51`, `doc: 12`, `test: 8`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.362
  * `Choke Point (Betweenness):` 6.4e-05 | `Ripple Effect (Closeness):` 0.028762
  * `Imports (Out-Degree: 18):` mypy.patterns, mypy.plugin, typing, mypy, mypy.types, mypy.messages, mypy.subtypes, mypy.options...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mypy/plugins/dataclasses.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.274 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.874 IQR)
- **Top Global Matches:** file_cluster_13: 11.274, file_cluster_8: 11.302, file_cluster_16: 11.362
- **Magnitude:** 1172.36 | **LOC:** 1140 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (14.5311%), Tech Debt (28.6549%)
**Top Internal Functions/Classes:**
  * `collect_attributes` (Impact: 338.3 | O(N^6))
  * `transform` (Impact: 287.5 | O(N^6) | DB: 1)
  * `reset_init_only_vars` (Impact: 70.8 | O(N^6))
  * `_collect_field_args` (Impact: 56.1 | O(N^6))
    * *Intent:* # For `dataclasses`, use the type `dict[str, Field[Any]]` for accuracy. For dataclass # transforms, ...
  * `_meet_replace_sigs` (Impact: 46.3 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 221`, `structural_boundaries: 202`, `args: 37`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 25`, `dead_code: 5`, `planned_debt: 6`, `duplicate_logic: 2`
* *Architecture:* `api: 26`, `import: 17`
* *Defense:* `safety: 68`, `doc: 40`, `test: 14`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.386
  * `Choke Point (Betweenness):` 0.000264 | `Ripple Effect (Closeness):` 0.003774
  * `Imports (Out-Degree: 14):` mypy, mypy.state, mypy.typeops, mypy.plugin, mypy.types, mypy.checker, mypy.expandtype, mypy.messages...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mypy/stats.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.597 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.674 IQR)
- **Top Global Matches:** file_cluster_13: 11.597, file_cluster_16: 11.634, file_cluster_11: 11.724
- **Magnitude:** 1171.82 | **LOC:** 495 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (36.8708%), Tech Debt (91.353%)
**Top Internal Functions/Classes:**
  * `visit_func_def` (Impact: 997.1 | O(2^N) | DB: 11)
  * `process_import` (Impact: 14.3 | O(N^3))
  * `visit_import` (Impact: 14.2 | O(N^3))
  * `get_original_any` (Impact: 6.3 | O(N^2))
  * `visit_mypy_file` (Impact: 5.4 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 118`, `args: 50`, `func_start: 49`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 44`, `dead_code: 1`, `planned_debt: 4`, `duplicate_logic: 2`, `orphaned_logic: 5`
* *Architecture:* `io: 1`, `api: 50`, `import: 14`
* *Defense:* `safety: 24`, `doc: 6`, `test: 5`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` mypy, mypy.argmap, mypy.types, os, collections, mypy.util, typing, contextlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mypy/partially_defined.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.52 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.992 IQR)
- **Top Global Matches:** file_cluster_16: 11.52, file_cluster_8: 11.737, file_cluster_13: 11.755
- **Magnitude:** 1099.08 | **LOC:** 704 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (16.7899%), Tech Debt (99.9994%)
**Top Internal Functions/Classes:**
  * `visit_name_expr` (Impact: 88.0 | O(2^N))
  * `visit_break_stmt` (Impact: 52.6 | O(2^N))
  * `visit_import` (Impact: 52.6 | O(2^N))
  * `process_lvalue` (Impact: 43.7 | O(2^N))
  * `process_try_stmt` (Impact: 42.9 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 142`, `args: 69`, `func_start: 69`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 62`, `duplicate_logic: 26`, `orphaned_logic: 9`
* *Architecture:* `api: 69`, `import: 10`
* *Defense:* `safety: 28`, `doc: 16`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.316
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` mypy, mypy.patterns, mypy.types, mypy.messages, mypy.options, mypy.traverser, enum, __future__...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `mypy/expandtype.py` (PYTHON) | Magnitude: 848.88 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 417, structural_boundaries: 194, branch: 125, generics: 70
- `mypyc/ir/rtypes.py` (PYTHON) | Magnitude: 1621.58 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 732, structural_boundaries: 335, state_mutation: 162, generics: 155
- `mypy/semanal_shared.py` (PYTHON) | Magnitude: 453.54 | Delta: **0.239 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 288, structural_boundaries: 96, api: 76, generics: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `mypy/modulefinder.py` (PYTHON) | Magnitude: 1525.36 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 615, branch: 214, structural_boundaries: 150, state_mutation: 122
- `misc/analyze_cache.py` (PYTHON) | Magnitude: 213.82 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 115, structural_boundaries: 50, branch: 34, generics: 18
- `mypy/constraints.py` (PYTHON) | Magnitude: 2115.36 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 1152, branch: 405, structural_boundaries: 321, state_mutation: 261
- `mypy/checker.py` (PYTHON) | Magnitude: 14341.48 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 6535, branch: 2371, structural_boundaries: 1549, safety: 727
- `mypy/join.py` (PYTHON) | Magnitude: 1709.4 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 623, structural_boundaries: 280, branch: 243, safety: 110

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `misc/docker/run.sh` (SHELL) | Magnitude: 0.97 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 6, structural_boundaries: 3, safety: 2, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `mypy/checkpattern.py` (PYTHON) | Magnitude: 1249.06 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 640, branch: 188, structural_boundaries: 155, state_mutation: 66
- `mypy/stubdoc.py` (PYTHON) | Magnitude: 962.62 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 359, state_mutation: 198, branch: 145, structural_boundaries: 107
- `mypyc/external/googletest/src/gtest-filepath.cc` (CPP) | Magnitude: 0.35 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 117, indent_spaces: 77, branch: 38, macros: 29
- `mypy/find_sources.py` (PYTHON) | Magnitude: 363.12 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 127, structural_boundaries: 57, branch: 45, generics: 21
- `mypy/options.py` (PYTHON) | Magnitude: 385.98 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 312, state_mutation: 121, structural_boundaries: 49, generics: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `mypy/semanal.py` (PYTHON) | Magnitude: 10103.66 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 6147, branch: 2220, structural_boundaries: 1422, safety: 648
- `mypyc/ir/func_ir.py` (PYTHON) | Magnitude: 685.96 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 330, structural_boundaries: 127, branch: 69, state_mutation: 67
- `mypy/fixup.py` (PYTHON) | Magnitude: 694.92 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 338, branch: 107, structural_boundaries: 93, api: 70
- `mypy/config_parser.py` (PYTHON) | Magnitude: 925.0 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 488, branch: 183, structural_boundaries: 118, state_mutation: 73
- `mypy/checkexpr.py` (PYTHON) | Magnitude: 7620.88 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 4998, branch: 1569, structural_boundaries: 1031, safety: 484

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `mypy/solve.py` (PYTHON) | Magnitude: 375.26 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 333, branch: 176, structural_boundaries: 102, state_mutation: 55

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `mypyc/external/googletest/src/gtest-typed-test.cc` (CPP) | Magnitude: 0.12 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 53, state_mutation: 51, branch: 15, args: 8
- `mypy/messages.py` (PYTHON) | Magnitude: 3379.86 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 2714, branch: 759, structural_boundaries: 624, generics: 258
- `misc/gen_blog_post_html.py` (PYTHON) | Magnitude: 203.32 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 105, branch: 30, state_mutation: 27, regex_execution: 22
- `mypy/server/mergecheck.py` (PYTHON) | Magnitude: 96.64 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 22, branch: 20, debug_prints: 7
- `mypy/semanal_typeddict.py` (PYTHON) | Magnitude: 105.9 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 489, branch: 155, structural_boundaries: 114, safety: 55

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `mypy/types.py` -> Churn: **67.64%** | Cog Load: 38.8153% | Debt: 100.0%
- `mypy/nodes.py` -> Churn: **66.46%** | Cog Load: 29.6097% | Debt: 100.0%
- `mypyc/ir/ops.py` -> Churn: **57.76%** | Cog Load: 30.9501% | Debt: 100.0%
- `mypy/fastparse.py` -> Churn: **54.68%** | Cog Load: 36.375% | Debt: 96.6584%
- `mypy/typeanal.py` -> Churn: **53.21%** | Cog Load: 35.0373% | Debt: 89.1499%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `mypy/nativeparse.py` -> **Ivan Levkivskyi** (83.3% isolated ownership) | Magnitude: 1813.26
- `mypy/suggestions.py` -> **Marc Mueller** (100.0% isolated ownership) | Magnitude: 1355.4
- `mypy/plugins/dataclasses.py` -> **Shantanu** (100.0% isolated ownership) | Magnitude: 1172.36
- `mypy/stats.py` -> **Ivan Levkivskyi** (100.0% isolated ownership) | Magnitude: 1171.82
- `mypyc/annotate.py` -> **BobTheBuidler** (100.0% isolated ownership) | Magnitude: 1010.1

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `mypy/plugins/ctypes.py` -> **Severity: 4.912** (Bridge: 0.0522 * Flux: 94.1446%)
- `mypy/util.py` -> **Severity: 4.832** (Bridge: 0.0534 * Flux: 90.4011%)
- `mypy/nodes.py` -> **Severity: 3.063** (Bridge: 0.0313 * Flux: 97.8503%)
- `mypy/types.py` -> **Severity: 2.219** (Bridge: 0.0232 * Flux: 95.5418%)
- `mypy/options.py` -> **Severity: 1.987** (Bridge: 0.0199 * Flux: 99.9983%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `mypy/visitor.py` -> **Severity: 19.399** (Embedded: 0.2425 * Error Risk: 80.0%)
- `mypy/options.py` -> **Severity: 17.383** (Embedded: 0.2719 * Error Risk: 63.9233%)
- `mypy/typeshed/stubs/mypy-extensions/mypy_extensions.pyi` -> **Severity: 16.898** (Embedded: 0.314 * Error Risk: 53.8095%)
- `mypy/bogus_type.py` -> **Severity: 16.609** (Embedded: 0.2076 * Error Risk: 80.0%)
- `mypy/strconv.py` -> **Severity: 16.355** (Embedded: 0.222 * Error Risk: 73.6615%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `mypy/typeshed/stubs/mypy-extensions/mypy_extensions.pyi` -> **Severity: 6958.3** (Blast Radius: 69.583 * Doc Risk: 100.0%)
- `mypy/nodes.py` -> **Severity: 5326.7** (Blast Radius: 53.267 * Doc Risk: 100.0%)
- `mypy/types.py` -> **Severity: 4871.2** (Blast Radius: 48.712 * Doc Risk: 100.0%)
- `mypy/util.py` -> **Severity: 4367.9** (Blast Radius: 43.679 * Doc Risk: 100.0%)
- `mypyc/ir/ops.py` -> **Severity: 3689.9** (Blast Radius: 36.899 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
