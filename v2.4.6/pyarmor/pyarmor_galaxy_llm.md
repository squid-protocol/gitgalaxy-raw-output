# ARCHITECTURAL_BRIEF: pyarmor
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pyarmor` |
| **Timestamp** | `2026-08-03T21:19:01.708461+00:00` |
| **Scan Duration** | `0.74s` |
| **Git Branch** | `master` |
| **Git Commit** | `9e8858bcdf590491c0dd83f7539381d34ff356d5` |
| **Git Remote** | `https://github.com/dashingsoft/pyarmor.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 149 malicious artifacts.

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
| Total Artifacts | 263 |
| Analyzed Artifacts (Scanned) | 169 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 94 |
| Total LOC | 22926 |
| Volatility Index | 0.018 |
| % Scanned of codebase = | 64.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6881 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5085 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 14.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.8451 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 11 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 132 | 21883 | 78.1% |
| MARKDOWN | 11 | 0 | 6.5% |
| PLAINTEXT | 9 | 3 | 5.3% |
| BATCH | 6 | 507 | 3.6% |
| SHELL | 5 | 139 | 3.0% |
| MAKEFILE | 3 | 332 | 1.8% |
| BINARY_THREAT | 2 | 2 | 1.2% |
| C | 1 | 60 | 0.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.068`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 100 | 59.2% |
| file_cluster_13 | 29 | 17.2% |
| file_cluster_0 | 7 | 4.1% |
| Unknown | 5 | 3.0% |
| file_cluster_17 | 5 | 3.0% |
| file_cluster_11 | 4 | 2.4% |
| file_cluster_9 | 1 | 0.6% |
| file_cluster_4 | 1 | 0.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 17 | 10.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 94*

**Composition by Extension & Reason:**
- `.rst`: 50x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 2 exceeds 500 chars)
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.8`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.9`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.02`: 1x Excluded (Unsupported Extension: '.02')
- `.cfg`: 1x Unsupported Format (.cfg)
- `.tri`: 1x Excluded (Binary Format Detected)
- `.zip`: 1x Excluded (Explicitly Denied Extension: '.zip')
- `.lic`: 1x Excluded (Binary Format Detected)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 20.2 | 9.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.6 | 18.8 | 5.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 12.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 26.1 | 0.3 | 0.0 |
| API Exposure | 0.0 | 13.0 | 3.7 | 3.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 22.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 91.7 | 2.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 79.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.4 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 5.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 35.0 | 6.4 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 49.7 | 39.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 43.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 3.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/utils.py` (Hits: 247)
- `src/pyarmor.py` (Hits: 130)
- `src/pyarmor-deprecated.py` (Hits: 97)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **pybench.py** (`src/examples/pybench/pybench.py`) — 14 inbound connections
2. **pytransform.py** (`src/pytransform.py`) — 13 inbound connections
3. **argparse.py** (`src/polyfills/argparse.py`) — 11 inbound connections
4. **context.py** (`src/cli/context.py`) — 5 inbound connections
5. **bootstrap.py** (`src/cli/bootstrap.py`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **utils.py** (`src/utils.py`) — 24 outbound dependencies
2. **__main__.py** (`src/cli/__main__.py`) — 23 outbound dependencies
3. **repack.py** (`src/cli/repack.py`) — 20 outbound dependencies
4. **pyarmor-deprecated.py** (`src/pyarmor-deprecated.py`) — 20 outbound dependencies
5. **context.py** (`src/cli/context.py`) — 18 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `pytransform_bootstrap` (@ `src/utils.py`) -> Impact: **2372.7** | LOC: 654
- `show_hd_info` (@ `src/utils.py`) -> Impact: **1774.3** | LOC: 326
- `format_platform` (@ `src/cli/context.py`) -> Impact: **1489.5** | LOC: 692
- `parse_token` (@ `src/cli/register.py`) -> Impact: **1367.1** | LOC: 426
- `test` (@ `src/examples/pybench/Constructs.py`) -> Impact: **1307.9** | LOC: 454
- `logaction` (@ `src/packer.py`) -> Impact: **1033.5** | LOC: 302
- `_capsule` (@ `src/pyarmor.py`) -> Impact: **967.3** | LOC: 433
- `calibrate` (@ `src/examples/pybench/pybench.py`) -> Impact: **955.3** | LOC: 434
  * *Intent:* # Init vars
- `_import_pytransform` (@ `src/pyarmor-deprecated.py`) -> Impact: **951.7** | LOC: 484
- `_build` (@ `src/pyarmor.py`) -> Impact: **944.7** | LOC: 344

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `call_query` (@ `gh.py`) -> **O(2^N) [Recursive]**
- `main` (@ `src/benchmark.py`) -> **O(2^N) [Recursive]**
- `format_platform` (@ `src/cli/context.py`) -> **O(2^N) [Recursive]**
- `main_entry` (@ `src/cli/docker.py`) -> **O(2^N) [Recursive]**
- `_build_resource` (@ `src/cli/generate.py`) -> **O(2^N) [Recursive]**
- `process` (@ `src/cli/generate.py`) -> **O(2^N) [Recursive]**
- `merge_scripts` (@ `src/cli/merge.py`) -> **O(2^N) [Recursive]**
- `_reform_value` (@ `src/cli/mixer.py`) -> **O(2^N) [Recursive]**
- `visit` (@ `src/cli/mixer.py`) -> **O(2^N) [Recursive]**
- `osx_merge_binary` (@ `src/cli/plugin.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `pytransform_bootstrap` (@ `src/utils.py`) -> DB Complexity: **386**
- `_import_pytransform` (@ `src/pyarmor-deprecated.py`) -> DB Complexity: **243**
- `format_platform` (@ `src/cli/context.py`) -> DB Complexity: **203**
- `logaction` (@ `src/packer.py`) -> DB Complexity: **140**
- `_capsule` (@ `src/pyarmor.py`) -> DB Complexity: **139**
- `show_hd_info` (@ `src/utils.py`) -> DB Complexity: **134**
- `build` (@ `src/cli/repack.py`) -> DB Complexity: **126**
- `_build` (@ `src/pyarmor.py`) -> DB Complexity: **99**
- `__obfuscate_dependency_pkgs` (@ `src/packer.py`) -> DB Complexity: **98**
- `get_hd_info` (@ `src/pytransform.py`) -> DB Complexity: **91**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 24 | 32127.14 | 15.23% | 0.36% |
| `src/cli` | 20 | 14907.16 | 34.55% | 36.44% |
| `src/examples/pybench` | 20 | 5905.98 | 17.59% | 0.0% |
| `src/polyfills` | 2 | 3781.52 | 39.58% | 100.0% |
| `src/helper` | 9 | 2031.54 | 17.0% | 4.93% |
| `__monolith__` | 7 | 689.06 | 3.2% | 4.57% |
| `plugins` | 9 | 506.84 | 17.43% | 30.94% |
| `src/cli/core` | 4 | 379.96 | 27.59% | 25.0% |
| `src/examples/testmod` | 2 | 374.89 | 21.79% | 0.0% |
| `src/examples` | 12 | 311.28 | 26.79% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/cli/bug.py` -> **100.0%** Exposure
- `src/polyfills/__init__.py` -> **100.0%** Exposure
- `src/polyfills/argparse.py` -> **100.0%** Exposure
- `scripts/build-package.sh` -> **100.0%** Exposure
- `src/cli/core/features.py` -> **99.9995%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/cli/config.py` -> **100.0%** Exposure
- `src/helper/merge.py` -> **100.0%** Exposure
- `src/pyimcore.py` -> **100.0%** Exposure
- `tests.8/samples/benchmark.py` -> **100.0%** Exposure
- `plugins/extra_hdinfo.c` -> **99.9999%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/polyfills/argparse.py` -> **0** Orphaned Functions | **31** Duplicates
- `src/examples/pybench/Strings.py` -> **0** Orphaned Functions | **14** Duplicates
- `src/examples/pybench/With.py` -> **0** Orphaned Functions | **12** Duplicates
- `src/examples/pybench/Arithmetic.py` -> **0** Orphaned Functions | **10** Duplicates
- `src/examples/pybench/Calls.py` -> **0** Orphaned Functions | **10** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/pyarmor.py`** -> AI Confidence: **99.44%**
2. **`src/pyarmor-deprecated.py`** -> AI Confidence: **99.39%**
3. **`gh.py`** -> AI Confidence: **99.31%**
4. **`src/cli/__main__.py`** -> AI Confidence: **99.31%**
5. **`src/cli/bootstrap.py`** -> AI Confidence: **99.31%**
6. **`src/cli/command.py`** -> AI Confidence: **99.31%**
7. **`src/cli/plugin.py`** -> AI Confidence: **99.31%**
8. **`src/cli/project.py`** -> AI Confidence: **99.31%**
9. **`src/cli/register.py`** -> AI Confidence: **99.31%**
10. **`src/cli/repack.py`** -> AI Confidence: **99.31%**
11. **`src/helper/buildext.py`** -> AI Confidence: **99.31%**
12. **`src/helper/merge.py`** -> AI Confidence: **99.31%**
13. **`src/helper/repack.py`** -> AI Confidence: **99.31%**
14. **`tests/data/gbk.py`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `gh.py` -> **100.0%** Exposure
- `plugins/check_ntp_time.py` -> **100.0%** Exposure
- `src/benchmark.py` -> **100.0%** Exposure
- `src/build_meta.py` -> **100.0%** Exposure
- `src/cli/__main__.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `src/cli/merge.py` -> **100.0%** Exposure
- `src/examples/pybench/pybench.py` -> **100.0%** Exposure
- `src/helper/merge.py` -> **100.0%** Exposure
- `src/packer.py` -> **100.0%** Exposure
- `tests/Makefile` -> **99.9754%** Exposure
### Algorithmic DoS Exposure
- `gh.py` -> **100.0%** Exposure
- `src/benchmark.py` -> **100.0%** Exposure
- `src/build_meta.py` -> **100.0%** Exposure
- `src/cli/__main__.py` -> **100.0%** Exposure
- `src/cli/bootstrap.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `548` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/cli/resource.py` (PYTHON) -> Cumulative Risk: **835.01**
- **Archetype:** `file_cluster_0` (Distance: 11.613 IQR)
- **Magnitude:** 575.58 | **LOC:** 266 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__str__` (Impact: 147.8), `generate_output` (Impact: 80.2), `_get_encoding` (Impact: 74.2)

### 2. `src/polyfills/argparse.py` (PYTHON) -> Cumulative Risk: **789.14**
- **Archetype:** `file_cluster_17` (Distance: 15.103 IQR)
- **Magnitude:** 3677.76 | **LOC:** 2361 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__call__` (Impact: 645.8), `_parse_known_args` (Impact: 592.0), `_get_optional_kwargs` (Impact: 322.9)

### 3. `src/helper/merge.py` (PYTHON) -> Cumulative Risk: **773.37**
- **Archetype:** `file_cluster_8` (Distance: 10.459 IQR)
- **Magnitude:** 410.96 | **LOC:** 299 | **CtrlFlow:** 63.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `merge_scripts` (Impact: 207.7), `main` (Impact: 81.3), `parse_script` (Impact: 40.6)

### 4. `src/cli/__init__.py` (PYTHON) -> Cumulative Risk: **762.19**
- **Archetype:** `file_cluster_8` (Distance: 11.238 IQR)
- **Magnitude:** 50.72 | **LOC:** 47 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Documentation (100.0%), Tech Debt (99.9994%)
- **Heaviest Functions:** `__getattr__` (Impact: 31.9), `trace` (Impact: 3.5), `resoptions` (Impact: 2.9)

### 5. `src/cli/project.py` (PYTHON) -> Cumulative Risk: **760.7**
- **Archetype:** `file_cluster_0` (Distance: 13.458 IQR)
- **Magnitude:** 1513.48 | **LOC:** 1282 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `parse_file` (Impact: 691.1), `preview_autofix_result` (Impact: 219.3), `scan_path` (Impact: 62.1)

### 6. `src/cli/model.py` (PYTHON) -> Cumulative Risk: **750.91**
- **Archetype:** `file_cluster_8` (Distance: 10.157 IQR)
- **Magnitude:** 198.5 | **LOC:** 461 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `usage` (Impact: 38.7), `check` (Impact: 26.7), `value` (Impact: 26.3)

### 7. `src/cli/config.py` (PYTHON) -> Cumulative Risk: **719.81**
- **Archetype:** `file_cluster_8` (Distance: 12.213 IQR)
- **Magnitude:** 792.82 | **LOC:** 307 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `list_sections` (Impact: 372.2), `run` (Impact: 175.6), `_parse_opt` (Impact: 67.4)

### 8. `src/cli/shell.py` (PYTHON) -> Cumulative Risk: **710.46**
- **Archetype:** `file_cluster_0` (Distance: 12.096 IQR)
- **Magnitude:** 932.42 | **LOC:** 482 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `title` (Impact: 516.2), `do_push` (Impact: 43.0), `remove` (Impact: 30.4)

### 9. `src/cli/context.py` (PYTHON) -> Cumulative Risk: **705.23**
- **Archetype:** `file_cluster_0` (Distance: 11.409 IQR)
- **Magnitude:** 1684.22 | **LOC:** 791 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `format_platform` (Impact: 1489.5)

### 10. `src/cli/merge.py` (PYTHON) -> Cumulative Risk: **684.49**
- **Archetype:** `file_cluster_8` (Distance: 9.455 IQR)
- **Magnitude:** 528.7 | **LOC:** 233 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `merge_scripts` (Impact: 425.0), `main` (Impact: 38.7), `parse_script` (Impact: 17.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/utils.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.398 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.931 IQR)
- **Top Global Matches:** file_cluster_8: 11.398, file_cluster_13: 11.623, file_cluster_17: 11.64
- **Magnitude:** 6152.0 | **LOC:** 1872 | **CtrlFlow:** 66.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 386
- **Risk Profile:** Cognitive Load (31.2582%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pytransform_bootstrap` (Impact: 2372.7 | O(2^N) | DB: 386)
  * `show_hd_info` (Impact: 1774.3 | O(2^N) | DB: 134)
  * `check_cross_platform` (Impact: 724.6 | O(N^6) | DB: 64)
  * `_package_super_runtime` (Impact: 550.5 | O(N^6) | DB: 49)
  * `load_config` (Impact: 234.2 | O(N^6) | DB: 42)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 587`, `structural_boundaries: 295`, `args: 82`, `func_start: 82`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 1`, `state_mutation: 105`, `dead_code: 4`
* *Architecture:* `io: 247`, `api: 50`, `import: 23`
* *Defense:* `safety: 44`, `doc: 2`, `test: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.759
  * `Choke Point (Betweenness):` 0.001889 | `Ripple Effect (Closeness):` 0.02381
  * `Imports (Out-Degree: 4):` shutil, pyarmor, dis, logging, urllib2, ssl, zipfile, cobuilder...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/product.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.484
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/public.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.484
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/pyshield.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.484
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/pyarmor.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.44%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.362 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.667 IQR)
- **Top Global Matches:** file_cluster_8: 10.362, file_cluster_7: 10.781, file_cluster_13: 10.816
- **Magnitude:** 3688.08 | **LOC:** 1648 | **CtrlFlow:** 78.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 139
- **Risk Profile:** Cognitive Load (18.986%), Tech Debt (8.7241%)
**Top Internal Functions/Classes:**
  * `_capsule` (Impact: 967.3 | O(N^6) | DB: 139)
  * `_build` (Impact: 944.7 | O(N^6) | DB: 99)
  * `_help` (Impact: 926.3 | O(2^N) | DB: 61)
  * `_format_entry` (Impact: 662.1 | O(2^N) | DB: 80)
  * `main` (Impact: 59.3 | O(2^N) | DB: 24)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 451`, `structural_boundaries: 125`, `args: 33`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 2`, `state_mutation: 57`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 130`, `api: 10`, `import: 16`
* *Defense:* `safety: 16`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.056
  * `Choke Point (Betweenness):` 0.002816 | `Ripple Effect (Closeness):` 0.021429
  * `Imports (Out-Degree: 4):` shutil, polyfills.argparse, .cli.__main__, time, register, utils, os, or...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/polyfills/argparse.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.103 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.697 IQR)
- **Top Global Matches:** file_cluster_17: 15.103, file_cluster_0: 15.32, file_cluster_9: 15.327
- **Magnitude:** 3677.76 | **LOC:** 2361 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 36
- **Risk Profile:** Cognitive Load (59.7157%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__call__` (Impact: 645.8 | O(2^N) | DB: 27)
  * `_parse_known_args` (Impact: 592.0 | O(N^6) | DB: 18)
  * `_get_optional_kwargs` (Impact: 322.9 | O(N^6) | DB: 36)
  * `format_help` (Impact: 295.9 | O(2^N) | DB: 5)
  * `_format_actions_usage` (Impact: 207.8 | O(N^6) | DB: 8)
    * *Intent:* # build full usage string
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 374`, `structural_boundaries: 298`, `args: 127`, `func_start: 127`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 273`, `dead_code: 54`, `duplicate_logic: 31`
* *Architecture:* `io: 4`, `api: 45`, `import: 9`
* *Defense:* `safety: 46`, `doc: 36`, `test: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 31.284
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.063713
  * `Imports (Out-Degree: 0):` re, textwrap, os, copy, gettext, warnings, sys
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/cli/register.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.106 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.076 IQR)
- **Top Global Matches:** file_cluster_8: 11.106, file_cluster_13: 11.268, file_cluster_17: 11.482
- **Magnitude:** 2696.16 | **LOC:** 1091 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 50
- **Risk Profile:** Cognitive Load (30.3685%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_token` (Impact: 1367.1 | O(2^N) | DB: 50)
  * `request_device_regfile` (Impact: 426.6 | O(2^N) | DB: 30)
  * `check_request_interval` (Impact: 299.9 | O(N^6) | DB: 30)
  * `register` (Impact: 253.7 | O(2^N) | DB: 9)
  * `_group_license_helper` (Impact: 81.0 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 231`, `structural_boundaries: 174`, `args: 40`, `func_start: 40`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 70`
* *Architecture:* `io: 33`, `api: 23`, `import: 24`
* *Defense:* `safety: 15`, `doc: 18`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.484
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` struct, datetime, urllib.request, time, string, platform, os, ssl...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/packer.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.768 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.109 IQR)
- **Top Global Matches:** file_cluster_13: 10.768, file_cluster_8: 10.806, file_cluster_0: 11.01
- **Magnitude:** 2113.16 | **LOC:** 721 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 140
- **Risk Profile:** Cognitive Load (20.9774%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `logaction` (Impact: 1033.5 | O(2^N) | DB: 140)
  * `__obfuscate_dependency_pkgs` (Impact: 835.9 | O(2^N) | DB: 98)
  * `packer` (Impact: 111.6 | O(N^6) | DB: 27)
  * `_check_entry_script` (Impact: 42.3 | O(N^5) | DB: 3)
  * `add_arguments` (Impact: 19.7 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 96`, `args: 26`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 37`, `dead_code: 2`
* *Architecture:* `io: 88`, `api: 14`, `import: 17`
* *Defense:* `safety: 16`, `doc: 10`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.017157
  * `Imports (Out-Degree: 1):` shutil, re, polyfills.argparse, shlex, py_compile, os, codecs, logging...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cli/repack.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.99 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.84 IQR)
- **Top Global Matches:** file_cluster_13: 11.99, file_cluster_8: 12.16, file_cluster_17: 12.35
- **Magnitude:** 1804.1 | **LOC:** 794 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 126
- **Risk Profile:** Cognitive Load (32.472%), Tech Debt (10.9097%)
**Top Internal Functions/Classes:**
  * `build` (Impact: 681.5 | O(2^N) | DB: 126)
  * `repack_executable` (Impact: 671.0 | O(2^N) | DB: 85)
  * `autoclean_output` (Impact: 266.9 | O(2^N) | DB: 89)
  * `repack_carchive` (Impact: 11.5 | O(N^2) | DB: 4)
  * `__init__` (Impact: 11.4 | O(N^2) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 123`, `args: 32`, `func_start: 32`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 110`, `fragile_debt: 1`
* *Architecture:* `io: 91`, `api: 31`, `import: 22`
* *Defense:* `safety: 19`, `doc: 20`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.484
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` shutil, importlib._bootstrap_external, logging, PyInstaller.depend, PyInstaller.archive.writers, PyInstaller.utils.osx, PyInstaller.utils.win32, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cli/context.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.409 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.182 IQR)
- **Top Global Matches:** file_cluster_0: 11.409, file_cluster_13: 11.693, file_cluster_12: 11.834
- **Magnitude:** 1684.22 | **LOC:** 791 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 203
- **Risk Profile:** Cognitive Load (75.8347%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `format_platform` (Impact: 1489.5 | O(2^N) | DB: 203)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 245`, `args: 101`, `func_start: 101`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 92`
* *Architecture:* `io: 53`, `api: 92`, `import: 16`
* *Defense:* `safety: 4`, `doc: 8`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.347
  * `Choke Point (Betweenness):` 0.000107 | `Ripple Effect (Closeness):` 0.029557
  * `Imports (Out-Degree: 1):` __pyarmor__, struct, shutil, shlex, .pyarmor_runtime, configparser, importlib.machinery, .plugin...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/cli/project.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.458 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.293 IQR)
- **Top Global Matches:** file_cluster_0: 13.458, file_cluster_13: 13.644, file_cluster_17: 13.739
- **Magnitude:** 1513.48 | **LOC:** 1282 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 75
- **Risk Profile:** Cognitive Load (49.1032%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_file` (Impact: 691.1 | O(N^6) | DB: 75)
  * `preview_autofix_result` (Impact: 219.3 | O(N^6) | DB: 21)
  * `scan_path` (Impact: 62.1 | O(N^4) | DB: 5)
  * `search_item` (Impact: 49.9 | O(N^3) | DB: 7)
  * `get_external_type` (Impact: 30.6 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 165`, `args: 72`, `func_start: 72`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 2`, `state_mutation: 209`, `dead_code: 9`
* *Architecture:* `io: 15`, `api: 79`, `import: 14`
* *Defense:* `safety: 4`, `doc: 86`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.484
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os.path, collections, string, textwrap, os, extension, logging, abc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/examples/pybench/Constructs.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.903 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.551 IQR)
- **Top Global Matches:** file_cluster_8: 7.903, file_cluster_7: 8.752, file_cluster_1: 9.017
- **Magnitude:** 1499.44 | **LOC:** 565 | **CtrlFlow:** 85.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (41.6361%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 1307.9 | O(N^6))
  * `test` (Impact: 119.8 | O(N^4))
  * `test` (Impact: 30.8 | O(N^6))
  * `calibrate` (Impact: 7.3 | O(N^3))
  * `calibrate` (Impact: 7.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 244`, `structural_boundaries: 40`, `args: 6`, `func_start: 6`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 29`, `duplicate_logic: 6`
* *Architecture:* `api: 9`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.679
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.031888
  * `Imports (Out-Degree: 1):` pybench
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/examples/pybench/pybench.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.339 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.864 IQR)
- **Top Global Matches:** file_cluster_8: 11.339, file_cluster_13: 11.557, file_cluster_7: 11.68
- **Magnitude:** 1408.7 | **LOC:** 955 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (17.1288%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `calibrate` (Impact: 955.3 | O(2^N) | DB: 30)
    * *Intent:* # Init vars
  * `calibrate_test` (Impact: 141.5 | O(N^6) | DB: 15)
  * `get_timer` (Impact: 51.3 | O(N^6) | DB: 6)
    * *Intent:* # Allow skipping calibration ? # Timer types TIMER_TIME_TIME = 'time.time' TIMER_TIME_CLOCK = 'time....
  * `load_tests` (Impact: 51.3 | O(N^4))
  * `__init__` (Impact: 40.4 | O(N^4) | DB: 10)
    * *Intent:* # The number of abstract operations done in each round of the # measure. The benchmark will output t...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 71`, `args: 22`, `func_start: 22`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 83`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `io: 11`, `api: 23`, `import: 9`
* *Defense:* `safety: 22`, `doc: 26`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 57.179
  * `Choke Point (Betweenness):` 0.009053 | `Ripple Effect (Closeness):` 0.083705
  * `Imports (Out-Degree: 3):` systimes, subclasses, pickle, Setup, gc, time, CommandLine, __future__...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `src/pyarmor-deprecated.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.929 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.117 IQR)
- **Top Global Matches:** file_cluster_13: 10.929, file_cluster_8: 11.044, file_cluster_0: 11.27
- **Magnitude:** 999.26 | **LOC:** 844 | **CtrlFlow:** 74.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 243
- **Risk Profile:** Cognitive Load (18.3978%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_import_pytransform` (Impact: 951.7 | O(N^6) | DB: 243)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 59`, `args: 17`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 27`, `dead_code: 1`
* *Architecture:* `io: 97`, `api: 11`, `import: 20`
* *Defense:* `safety: 22`, `doc: 18`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.484
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` shutil, pyarmor, imp, logging, distutils.text_file, distutils.util, zipfile, glob...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cli/shell.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.096 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.01 IQR)
- **Top Global Matches:** file_cluster_0: 12.096, file_cluster_13: 12.225, file_cluster_17: 12.398
- **Magnitude:** 932.42 | **LOC:** 482 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (48.666%), Tech Debt (26.9479%)
**Top Internal Functions/Classes:**
  * `title` (Impact: 516.2 | O(2^N) | DB: 35)
  * `do_push` (Impact: 43.0 | O(N^5))
  * `remove` (Impact: 30.4 | O(N^5))
  * `do_info` (Impact: 27.0 | O(N^4))
  * `do_set` (Impact: 26.9 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 114`, `args: 58`, `func_start: 58`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 114`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 61`, `import: 6`
* *Defense:* `safety: 6`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.828
  * `Choke Point (Betweenness):` 0.000321 | `Ripple Effect (Closeness):` 0.018544
  * `Imports (Out-Degree: 2):` shlex, configparser, .model, .context, cmd, os.path
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/cli/__main__.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.932 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.109 IQR)
- **Top Global Matches:** file_cluster_8: 9.932, file_cluster_13: 10.208, file_cluster_7: 10.473
- **Magnitude:** 899.16 | **LOC:** 813 | **CtrlFlow:** 60.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (13.1666%), Tech Debt (19.0276%)
**Top Internal Functions/Classes:**
  * `_cmd_gen_key` (Impact: 391.1 | O(N^6) | DB: 38)
  * `main_entry` (Impact: 141.3 | O(2^N) | DB: 9)
  * `cmd_gen` (Impact: 130.8 | O(N^3) | DB: 4)
  * `gen_parser` (Impact: 54.1 | O(2^N))
    * *Intent:* '''generate obfuscated scripts and all required runtime files pyarmor gen <options> <scripts> genera...
  * `cmd_man` (Impact: 31.6 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 95`, `args: 21`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 15`, `fragile_debt: 4`
* *Architecture:* `io: 27`, `api: 19`, `concurrency: 1`, `import: 24`
* *Defense:* `safety: 17`, `doc: 8`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.046
  * `Choke Point (Betweenness):` 0.002246 | `Ripple Effect (Closeness):` 0.017157
  * `Imports (Out-Degree: 8):` .config, logging, logging.config, sys, pyarmor.cli, argparse, .generate, .plugin...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cli/plugin.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.912 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.838 IQR)
- **Top Global Matches:** file_cluster_13: 10.912, file_cluster_0: 10.92, file_cluster_17: 11.147
- **Magnitude:** 853.14 | **LOC:** 293 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 49
- **Risk Profile:** Cognitive Load (31.8853%), Tech Debt (50.864%)
**Top Internal Functions/Classes:**
  * `osx_merge_binary` (Impact: 395.9 | O(2^N) | DB: 49)
  * `install` (Impact: 105.6 | O(2^N) | DB: 8)
  * `osx_sign_binary` (Impact: 96.0 | O(2^N) | DB: 9)
  * `post_build` (Impact: 82.4 | O(N^5) | DB: 28)
  * `post_bcc` (Impact: 50.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 65`, `args: 16`, `func_start: 16`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 14`, `duplicate_logic: 2`
* *Architecture:* `io: 34`, `api: 22`, `import: 11`
* *Defense:* `safety: 13`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.773
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.030483
  * `Imports (Out-Degree: 0):` shutil, importlib.util, .pyarmor_runtime, os, subprocess, , sys
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/pytransform.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.268 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.009 IQR)
- **Top Global Matches:** file_cluster_8: 9.268, file_cluster_0: 9.272, file_cluster_13: 9.552
- **Magnitude:** 826.54 | **LOC:** 484 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 91
- **Risk Profile:** Cognitive Load (12.9951%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_hd_info` (Impact: 755.2 | O(2^N) | DB: 91)
  * `init_pytransform` (Impact: 24.2 | O(N^3) | DB: 6)
  * `version_info` (Impact: 3.7 | O(2^N))
  * `dllmethod` (Impact: 2.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 97`, `args: 38`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1`, `dead_code: 1`
* *Architecture:* `io: 32`, `api: 33`, `import: 7`
* *Defense:* `safety: 10`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 42.508
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.077143
  * `Imports (Out-Degree: 0):` struct, anything, time, ctypes, os, fnmatch, platform, sys
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `src/cli/config.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.213 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.686 IQR)
- **Top Global Matches:** file_cluster_8: 12.213, file_cluster_17: 12.279, file_cluster_13: 12.326
- **Magnitude:** 792.82 | **LOC:** 307 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 45
- **Risk Profile:** Cognitive Load (57.6407%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `list_sections` (Impact: 372.2 | O(N^6) | DB: 45)
  * `run` (Impact: 175.6 | O(N^6) | DB: 24)
  * `_parse_opt` (Impact: 67.4 | O(N^6) | DB: 1)
  * `reset` (Impact: 17.0 | O(N^4))
  * `__init__` (Impact: 6.2 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 38`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 134`
* *Architecture:* `io: 8`, `api: 11`, `import: 4`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.484
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , os, fnmatch, configparser
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/examples/pybench/Exceptions.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.75%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.923 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.219 IQR)
- **Top Global Matches:** file_cluster_8: 11.923, file_cluster_0: 12.562, file_cluster_7: 12.584
- **Magnitude:** 768.16 | **LOC:** 700 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (16.2126%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 689.5 | O(N^4))
  * `test` (Impact: 45.2 | O(N^4))
  * `calibrate` (Impact: 7.2 | O(N^3))
  * `calibrate` (Impact: 7.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 319`, `args: 4`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 468`, `duplicate_logic: 4`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `safety: 316`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.679
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.031888
  * `Imports (Out-Degree: 1):` timeit, pybench
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cobuilder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.05%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.526 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.197 IQR)
- **Top Global Matches:** file_cluster_8: 11.526, file_cluster_13: 11.53, file_cluster_17: 11.554
- **Magnitude:** 754.32 | **LOC:** 155 | **CtrlFlow:** 62.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (53.5654%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_check_inline_option` (Impact: 734.8 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 36`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`
* *Architecture:* `io: 1`, `api: 8`, `import: 6`
* *Defense:* `safety: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.108
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.016484
  * `Imports (Out-Degree: 1):` mixins, sppmode, random, logging, ast, sys
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cli/generate.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.092 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.825 IQR)
- **Top Global Matches:** file_cluster_17: 11.092, file_cluster_8: 11.121, file_cluster_13: 11.16
- **Magnitude:** 729.44 | **LOC:** 257 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 50
- **Risk Profile:** Cognitive Load (37.3152%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_build_resource` (Impact: 394.3 | O(2^N) | DB: 50)
  * `process` (Impact: 284.7 | O(2^N) | DB: 27)
  * `__init__` (Impact: 2.7 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 38`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 32`
* *Architecture:* `io: 22`, `api: 12`, `import: 6`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.815
  * `Choke Point (Betweenness):` 0.000356 | `Ripple Effect (Closeness):` 0.022046
  * `Imports (Out-Degree: 1):` shutil, os, concurrent.futures, .resource, pyarmor.cli.core, 
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `gh.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.798 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.88 IQR)
- **Top Global Matches:** file_cluster_8: 11.798, file_cluster_13: 11.807, file_cluster_7: 11.936
- **Magnitude:** 658.16 | **LOC:** 512 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (16.3594%), Tech Debt (31.9556%)
**Top Internal Functions/Classes:**
  * `call_query` (Impact: 581.6 | O(2^N) | DB: 18)
  * `parse` (Impact: 3.6 | O(N^1))
  * `call_cmd` (Impact: 1.8 | O(N^1))
    * *Intent:* ''') cmd_view_discussion = Template('''
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 45`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 46`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 20`, `import: 7`
* *Defense:* `safety: 5`, `doc: 54`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.484
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` datetime, shlex, configparser, string, cmd, subprocess, json
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/helper/repack.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.03 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.785 IQR)
- **Top Global Matches:** file_cluster_13: 10.03, file_cluster_8: 10.128, file_cluster_7: 10.639
- **Magnitude:** 657.3 | **LOC:** 396 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (17.613%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `repack_exe` (Impact: 357.7 | O(2^N) | DB: 43)
  * `checkmagic` (Impact: 163.8 | O(N^6) | DB: 28)
  * `repack_pyz` (Impact: 68.9 | O(N^4) | DB: 12)
  * `main` (Impact: 25.4 | O(N^6) | DB: 6)
  * `excepthook` (Impact: 6.3 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 59`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 15`
* *Architecture:* `io: 31`, `api: 15`, `import: 20`
* *Defense:* `safety: 7`, `doc: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.484
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` shutil, struct, PyInstaller.utils.win32, PyInstaller.loader.pyimod02_archive, argparse, PyInstaller.archive.readers, PyInstaller.loader.pyimod01_archive, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/examples/pybench/CommandLine.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.509 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.065 IQR)
- **Top Global Matches:** file_cluster_8: 12.509, file_cluster_13: 12.601, file_cluster_7: 12.691
- **Magnitude:** 625.64 | **LOC:** 643 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (35.3994%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 239.7 | O(N^6) | DB: 34)
    * *Intent:* # The help layout looks like this: # [header] - defaults to '' # # [synopsis] - formatted as '<self....
  * `__str__` (Impact: 46.9 | O(N^6) | DB: 5)
  * `fileopen` (Impact: 33.0 | O(N^3) | DB: 18)
    * *Intent:* # long option
  * `_getopt_flags` (Impact: 31.3 | O(N^4) | DB: 4)
  * `print_options` (Impact: 28.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 68`, `args: 30`, `func_start: 30`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 79`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 17`, `api: 39`, `import: 4`
* *Defense:* `safety: 17`, `doc: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.686
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.047619
  * `Imports (Out-Degree: 0):` re, getopt, os, codecs, traceback, getpass, __future__, glob...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `tests/data/gbk.py` (PYTHON) | **Drift Ratio: 1.63x**
  * **Global Archetype:** `file_cluster_8` (Drift: 5.125 IQR)
  * **Local Reality:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 8.335 IQR)
- `tests/data/utf8bom.py` (PYTHON) | **Drift Ratio: 1.59x**
  * **Global Archetype:** `file_cluster_8` (Drift: 4.918 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.796 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/cli/core/__init__.py` (PYTHON) | Magnitude: 152.68 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 39, branch: 13, api: 13
- `src/cli/resource.py` (PYTHON) | Magnitude: 575.58 | Delta: **0.104 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 179, structural_boundaries: 84, branch: 59, state_mutation: 48
- `src/cli/shell.py` (PYTHON) | Magnitude: 932.42 | Delta: **0.129 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 355, structural_boundaries: 114, state_mutation: 114, encapsulation: 103
- `src/benchmark.py` (PYTHON) | Magnitude: 396.08 | Delta: **0.18 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 192, structural_boundaries: 76, args: 35, telemetry: 33
- `src/cli/project.py` (PYTHON) | Magnitude: 1513.48 | Delta: **0.186 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 624, state_mutation: 209, branch: 186, structural_boundaries: 165

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/examples/pack-obfuscated-scripts.sh` (SHELL) | Magnitude: 29.8 | Delta: **0.142 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: state_mutation: 18, branch: 9, reflection_metaprogramming: 6, safety_bypasses: 4
- `src/examples/obfuscate-app.sh` (SHELL) | Magnitude: 33.66 | Delta: **0.243 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: state_mutation: 18, branch: 10, indent_spaces: 9, reflection_metaprogramming: 8
- `src/examples/obfuscate-pkg.sh` (SHELL) | Magnitude: 50.78 | Delta: **0.254 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: branch: 21, state_mutation: 21, indent_spaces: 13, reflection_metaprogramming: 11
- `src/examples/build-with-project.sh` (SHELL) | Magnitude: 89.08 | Delta: **0.309 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: branch: 37, indent_spaces: 30, state_mutation: 27, safety_bypasses: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/cli/plugin.py` (PYTHON) | Magnitude: 853.14 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 203, branch: 68, structural_boundaries: 65, io: 34
- `src/helper/buildext.py` (PYTHON) | Magnitude: 571.5 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 144, branch: 39, structural_boundaries: 31, telemetry: 17
- `plugins/check_docker.py` (PYTHON) | Magnitude: 73.02 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 12, branch: 7, import: 3
- `src/packer.py` (PYTHON) | Magnitude: 2113.16 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 482, branch: 170, structural_boundaries: 96, io: 88
- `tests.8/samples/joker/__init__.py` (PYTHON) | Magnitude: 11.56 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, import: 2, encapsulation: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/cli/generate.py` (PYTHON) | Magnitude: 729.44 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 177, branch: 50, structural_boundaries: 38, state_mutation: 32
- `tests.9/Makefile` (MAKEFILE) | Magnitude: 16.76 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 41, indent_spaces: 31, branch: 27, indent_tabs: 24
- `scripts/build-package.sh` (SHELL) | Magnitude: 1.81 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 11, state_mutation: 8, safety_bypasses: 6
- `src/polyfills/argparse.py` (PYTHON) | Magnitude: 3677.76 | Delta: **0.217 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1434, encapsulation: 483, branch: 374, structural_boundaries: 298
- `tests/Makefile` (MAKEFILE) | Magnitude: 63.78 | Delta: **0.358 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 68, structural_boundaries: 29, indent_spaces: 29, indent_tabs: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/data/t_refcnt.py` (PYTHON) | Magnitude: 0.03 | Delta: **0.153 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 23, concurrency: 12, structural_boundaries: 9, debug_prints: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/cobuilder.py` (PYTHON) | Magnitude: 754.32 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 116, branch: 59, structural_boundaries: 36, safety: 23
- `src/pytransform.py` (PYTHON) | Magnitude: 826.54 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 265, structural_boundaries: 97, branch: 75, encapsulation: 55
- `tests.8/samples/joker/card.py` (PYTHON) | Magnitude: 4.68 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, debug_prints: 2, indent_spaces: 2, args: 1
- `src/cli/bug.py` (PYTHON) | Magnitude: 84.94 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 15, doc: 10, branch: 8
- `plugins/check_multiple_machine.py` (PYTHON) | Magnitude: 24.06 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 17, encapsulation: 8, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `plugins/assert_armored.py` (PYTHON) | Magnitude: 10.1 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 8, encapsulation: 4, args: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/cli/__init__.py` -> Churn: **100.0%** | Cog Load: 80.7754% | Debt: 99.9994%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/cli/register.py` -> **Jondy Zhao** (100.0% isolated ownership) | Magnitude: 2696.16
- `src/cli/context.py` -> **Jondy Zhao** (100.0% isolated ownership) | Magnitude: 1684.22
- `src/cli/project.py` -> **Jondy Zhao** (100.0% isolated ownership) | Magnitude: 1513.48
- `src/cli/shell.py` -> **Jondy Zhao** (100.0% isolated ownership) | Magnitude: 932.42
- `src/cli/__main__.py` -> **Jondy Zhao** (100.0% isolated ownership) | Magnitude: 899.16

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/utils.py` -> **Severity: 0.117** (Bridge: 0.0019 * Flux: 62.0643%)
- `src/pyarmor.py` -> **Severity: 0.103** (Bridge: 0.0028 * Flux: 36.7062%)
- `src/cli/__main__.py` -> **Severity: 0.048** (Bridge: 0.0022 * Flux: 21.2633%)
- `src/cli/generate.py` -> **Severity: 0.035** (Bridge: 0.0004 * Flux: 98.9697%)
- `src/sppmode.py` -> **Severity: 0.034** (Bridge: 0.0005 * Flux: 63.2633%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/examples/pybench/Setup.py` -> **Severity: 4.481** (Embedded: 0.0462 * Error Risk: 97.0261%)
- `src/examples/pybench/Exceptions.py` -> **Severity: 3.16** (Embedded: 0.0319 * Error Risk: 99.1042%)
- `src/examples/pybench/With.py` -> **Severity: 2.551** (Embedded: 0.0319 * Error Risk: 80.0%)
- `src/examples/pybench/Dict.py` -> **Severity: 2.449** (Embedded: 0.0319 * Error Risk: 76.798%)
- `src/examples/pybench/Instances.py` -> **Severity: 2.413** (Embedded: 0.0319 * Error Risk: 75.6785%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/pytransform.py` -> **Severity: 3826.791** (Blast Radius: 42.508 * Doc Risk: 90.0252%)
- `src/cli/bootstrap.py` -> **Severity: 3058.881** (Blast Radius: 32.751 * Doc Risk: 93.3981%)
- `src/polyfills/argparse.py` -> **Severity: 3044.703** (Blast Radius: 31.284 * Doc Risk: 97.3246%)
- `src/cli/resource.py` -> **Severity: 2767.8** (Blast Radius: 27.678 * Doc Risk: 100.0%)
- `src/cli/core/runtime.py` -> **Severity: 2355.214** (Blast Radius: 31.939 * Doc Risk: 73.741%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
