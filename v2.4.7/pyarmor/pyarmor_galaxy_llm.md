# ARCHITECTURAL_BRIEF: pyarmor
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pyarmor` |
| **Timestamp** | `2026-08-07T05:21:03.343341+00:00` |
| **Scan Duration** | `0.65s` |
| **Git Branch** | `master` |
| **Git Commit** | `9e8858bcdf590491c0dd83f7539381d34ff356d5` |
| **Git Remote** | `https://github.com/dashingsoft/pyarmor.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 149 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 100.0 | 19.7 | 9.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 40.2 | 51.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 13.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 17.3 | 0.3 | 0.0 |
| API Exposure | 0.0 | 13.0 | 3.7 | 3.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 22.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 91.7 | 2.2 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 79.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.4 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 5.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 20.7 | 3.2 | 0.0 |
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

- `test` (@ `src/examples/pybench/Constructs.py`) -> Impact: **389.9** | LOC: 454
- `pytransform_bootstrap` (@ `src/utils.py`) -> Impact: **367.0** | LOC: 654
- `test` (@ `src/examples/pybench/Exceptions.py`) -> Impact: **294.6** | LOC: 626
- `_capsule` (@ `src/pyarmor.py`) -> Impact: **291.8** | LOC: 433
- `_import_pytransform` (@ `src/pyarmor-deprecated.py`) -> Impact: **289.2** | LOC: 484
- `_build` (@ `src/pyarmor.py`) -> Impact: **282.2** | LOC: 344
- `show_hd_info` (@ `src/utils.py`) -> Impact: **267.4** | LOC: 326
- `format_platform` (@ `src/cli/context.py`) -> Impact: **242.4** | LOC: 692
- `check_cross_platform` (@ `src/utils.py`) -> Impact: **219.7** | LOC: 353
- `parse_file` (@ `src/cli/project.py`) -> Impact: **219.1** | LOC: 606

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 24 | 20309.04 | 15.11% | 0.36% |
| `src/cli` | 20 | 5043.26 | 33.55% | 37.9% |
| `src/examples/pybench` | 20 | 2611.28 | 16.39% | 0.0% |
| `src/polyfills` | 2 | 1392.52 | 39.49% | 100.0% |
| `src/helper` | 9 | 650.74 | 16.61% | 4.93% |
| `src/examples/testmod` | 2 | 300.59 | 21.79% | 0.0% |
| `src/examples` | 12 | 297.48 | 26.79% | 0.0% |
| `plugins` | 9 | 277.64 | 17.43% | 30.94% |
| `__monolith__` | 7 | 202.56 | 4.46% | 6.52% |
| `tests.9` | 4 | 118.98 | 9.92% | 48.26% |

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
- `src/examples/pybench/Calls.py` -> **0** Orphaned Functions | **28** Duplicates
- `src/examples/pybench/Strings.py` -> **0** Orphaned Functions | **14** Duplicates
- `src/examples/pybench/With.py` -> **0** Orphaned Functions | **12** Duplicates
- `src/examples/pybench/Arithmetic.py` -> **0** Orphaned Functions | **10** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `548` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/cli/resource.py` (PYTHON) -> Cumulative Risk: **671.69**
- **Archetype:** `file_cluster_0` (Distance: 11.61 IQR)
- **Magnitude:** 272.68 | **LOC:** 266 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9763%), State Flux (99.9621%)
- **Heaviest Functions:** `__str__` (Impact: 43.9), `generate_output` (Impact: 23.7), `_get_encoding` (Impact: 22.3)

### 2. `src/cli/project.py` (PYTHON) -> Cumulative Risk: **582.36**
- **Archetype:** `file_cluster_0` (Distance: 13.458 IQR)
- **Magnitude:** 717.78 | **LOC:** 1282 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.997%), Documentation (88.3842%), Safety Score (87.0454%)
- **Heaviest Functions:** `parse_file` (Impact: 219.1), `preview_autofix_result` (Impact: 67.7), `search_item` (Impact: 25.3)

### 3. `src/cli/__init__.py` (PYTHON) -> Cumulative Risk: **575.56**
- **Archetype:** `file_cluster_8` (Distance: 11.247 IQR)
- **Magnitude:** 29.62 | **LOC:** 47 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Tech Debt (99.9994%), State Flux (94.6914%)
- **Heaviest Functions:** `__getattr__` (Impact: 11.1), `process` (Impact: 2.4), `trace` (Impact: 2.4)

### 4. `src/cli/context.py` (PYTHON) -> Cumulative Risk: **573.4**
- **Archetype:** `file_cluster_0` (Distance: 11.428 IQR)
- **Magnitude:** 587.92 | **LOC:** 791 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Cognitive Load (85.9133%), State Flux (84.142%)
- **Heaviest Functions:** `format_platform` (Impact: 242.4), `token_http_proxy` (Impact: 23.9), `runtime_interps` (Impact: 10.9)

### 5. `src/polyfills/argparse.py` (PYTHON) -> Cumulative Risk: **567.96**
- **Archetype:** `file_cluster_17` (Distance: 15.102 IQR)
- **Magnitude:** 1358.86 | **LOC:** 2361 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.399%), Verification (80.0%)
- **Heaviest Functions:** `_parse_known_args` (Impact: 182.1), `__call__` (Impact: 119.2), `_get_optional_kwargs` (Impact: 103.0)

### 6. `src/cli/shell.py` (PYTHON) -> Cumulative Risk: **565.26**
- **Archetype:** `file_cluster_0` (Distance: 12.096 IQR)
- **Magnitude:** 398.02 | **LOC:** 482 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9962%), Verification (80.0%)
- **Heaviest Functions:** `title` (Impact: 114.4), `do_push` (Impact: 15.0), `do_info` (Impact: 11.4)

### 7. `src/cli/model.py` (PYTHON) -> Cumulative Risk: **562.64**
- **Archetype:** `file_cluster_8` (Distance: 10.157 IQR)
- **Magnitude:** 143.3 | **LOC:** 461 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (96.7624%), Tech Debt (92.4142%), Documentation (91.1105%)
- **Heaviest Functions:** `usage` (Impact: 21.4), `check` (Impact: 18.9), `value` (Impact: 5.5)

### 8. `scripts/build-package.sh` (SHELL) -> Cumulative Risk: **535.82**
- **Archetype:** `file_cluster_17` (Distance: 15.497 IQR)
- **Magnitude:** 1.81 | **LOC:** 69 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9498%), Safety Score (99.8426%)
- **Heaviest Functions:** `__global_context__` (Impact: 5.2), `Anonymous_Block` (Impact: 1.6), `Anonymous_Block` (Impact: 1.4)

### 9. `src/cli/config.py` (PYTHON) -> Cumulative Risk: **534.86**
- **Archetype:** `file_cluster_8` (Distance: 12.213 IQR)
- **Magnitude:** 349.22 | **LOC:** 307 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (93.5498%), Documentation (86.2311%)
- **Heaviest Functions:** `list_sections` (Impact: 112.2), `run` (Impact: 52.6), `_parse_opt` (Impact: 19.8)

### 10. `src/cli/plugin.py` (PYTHON) -> Cumulative Risk: **490.9**
- **Archetype:** `file_cluster_13` (Distance: 10.912 IQR)
- **Magnitude:** 202.84 | **LOC:** 293 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Verification (80.0%), State Flux (57.46%)
- **Heaviest Functions:** `osx_merge_binary` (Impact: 60.0), `post_build` (Impact: 28.8), `install` (Impact: 19.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/product.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `src/utils.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.398 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.931 IQR)
- **Top Global Matches:** file_cluster_8: 11.398, file_cluster_13: 11.623, file_cluster_17: 11.64
- **Magnitude:** 1392.9 | **LOC:** 1872 | **CtrlFlow:** 66.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.9767%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pytransform_bootstrap` (Impact: 367.0)
  * `show_hd_info` (Impact: 267.4)
  * `check_cross_platform` (Impact: 219.7)
  * `_package_super_runtime` (Impact: 164.7)
  * `load_config` (Impact: 69.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 587`, `structural_boundaries: 295`, `args: 82`, `func_start: 82`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 1`, `state_mutation: 105`, `dead_code: 4`
* *Architecture:* `io: 247`, `api: 50`, `import: 23`
* *Defense:* `safety: 44`, `doc: 2`, `test: 2`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.759
  * `Choke Point (Betweenness):` 0.001889 | `Ripple Effect (Closeness):` 0.02381
  * `Imports (Out-Degree: 4):` subprocess, sppmode, config, re, os, codecs, time, logging...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/polyfills/argparse.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_17` (Drift: 15.102 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.697 IQR)
- **Top Global Matches:** file_cluster_17: 15.102, file_cluster_0: 15.319, file_cluster_9: 15.326
- **Magnitude:** 1358.86 | **LOC:** 2361 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.5343%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_parse_known_args` (Impact: 182.1)
  * `__call__` (Impact: 119.2)
  * `_get_optional_kwargs` (Impact: 103.0)
  * `take_action` (Impact: 72.5)
  * `_format_actions_usage` (Impact: 62.8)
    * *Intent:* # build full usage string
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 374`, `structural_boundaries: 298`, `args: 127`, `func_start: 127`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 273`, `dead_code: 54`, `duplicate_logic: 31`
* *Architecture:* `io: 4`, `api: 45`, `import: 9`
* *Defense:* `safety: 46`, `doc: 36`, `test: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 31.284
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.063713
  * `Imports (Out-Degree: 0):` copy, warnings, textwrap, gettext, sys, re, os
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/pyarmor.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.44%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.362 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.667 IQR)
- **Top Global Matches:** file_cluster_8: 10.362, file_cluster_7: 10.781, file_cluster_13: 10.816
- **Magnitude:** 977.78 | **LOC:** 1648 | **CtrlFlow:** 78.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.5456%), Tech Debt (8.7241%)
**Top Internal Functions/Classes:**
  * `_capsule` (Impact: 291.8)
  * `_build` (Impact: 282.2)
  * `_help` (Impact: 157.2)
  * `_format_entry` (Impact: 100.9)
  * `main` (Impact: 21.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 451`, `structural_boundaries: 125`, `args: 33`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 2`, `state_mutation: 57`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 130`, `api: 10`, `import: 16`
* *Defense:* `safety: 16`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.056
  * `Choke Point (Betweenness):` 0.002816 | `Ripple Effect (Closeness):` 0.021429
  * `Imports (Out-Degree: 4):` subprocess, register, sys, polyfills.argparse, .cli.__main__, project, webbrowser, config...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/cli/project.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.458 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.293 IQR)
- **Top Global Matches:** file_cluster_0: 13.458, file_cluster_13: 13.644, file_cluster_17: 13.739
- **Magnitude:** 717.78 | **LOC:** 1282 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.0245%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_file` (Impact: 219.1)
  * `preview_autofix_result` (Impact: 67.7)
  * `search_item` (Impact: 25.3)
  * `scan_path` (Impact: 25.2)
  * `get_external_type` (Impact: 12.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 165`, `args: 72`, `func_start: 72`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 2`, `state_mutation: 209`, `dead_code: 9`
* *Architecture:* `io: 15`, `api: 79`, `import: 14`
* *Defense:* `safety: 4`, `doc: 86`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.484
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` subprocess, textwrap, glob, abc, string, json, extension, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cli/register.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.105 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.075 IQR)
- **Top Global Matches:** file_cluster_8: 11.105, file_cluster_13: 11.265, file_cluster_17: 11.481
- **Magnitude:** 695.06 | **LOC:** 1091 | **CtrlFlow:** 57.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (19.3881%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_token` (Impact: 213.6)
  * `check_request_interval` (Impact: 89.9)
  * `request_device_regfile` (Impact: 66.6)
  * `register` (Impact: 45.5)
  * `register_regfile` (Impact: 28.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 231`, `structural_boundaries: 174`, `args: 40`, `func_start: 40`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 70`
* *Architecture:* `io: 33`, `api: 24`, `import: 24`
* *Defense:* `safety: 15`, `doc: 18`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.484
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` urllib.request, zipfile, string, json, struct, socket, http.client, base64...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cli/context.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.428 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.197 IQR)
- **Top Global Matches:** file_cluster_0: 11.428, file_cluster_13: 11.717, file_cluster_12: 11.858
- **Magnitude:** 587.92 | **LOC:** 791 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (85.9133%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `format_platform` (Impact: 242.4)
  * `token_http_proxy` (Impact: 23.9)
  * `runtime_interps` (Impact: 10.9)
    * *Intent:* # # runtime configuration #
  * `runtime_user_data` (Impact: 9.2)
  * `runtime_period` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 245`, `args: 101`, `func_start: 101`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 92`
* *Architecture:* `io: 53`, `api: 118`, `import: 16`
* *Defense:* `safety: 4`, `doc: 8`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.347
  * `Choke Point (Betweenness):` 0.000107 | `Ripple Effect (Closeness):` 0.029557
  * `Imports (Out-Degree: 1):` .plugin, urllib.request, shlex, struct, __pyarmor__, sys, ssl, json...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/packer.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.76 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.112 IQR)
- **Top Global Matches:** file_cluster_13: 10.76, file_cluster_8: 10.806, file_cluster_0: 10.993
- **Magnitude:** 523.46 | **LOC:** 721 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.9774%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `logaction` (Impact: 160.6)
  * `__obfuscate_dependency_pkgs` (Impact: 127.8)
  * `wrap` (Impact: 112.4)
  * `packer` (Impact: 33.7)
  * `_check_entry_script` (Impact: 14.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 96`, `args: 26`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 1`, `state_mutation: 37`, `dead_code: 2`
* *Architecture:* `io: 88`, `api: 14`, `import: 17`
* *Defense:* `safety: 16`, `doc: 10`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.046
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.017157
  * `Imports (Out-Degree: 1):` subprocess, shlex, glob, zipfile, pkg_resources, json, sys, polyfills.argparse...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/protect_code.pt` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `src/protect_code2.pt` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `src/cli/repack.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.974 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.821 IQR)
- **Top Global Matches:** file_cluster_13: 11.974, file_cluster_8: 12.149, file_cluster_17: 12.333
- **Magnitude:** 488.4 | **LOC:** 794 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.472%), Tech Debt (40.1312%)
**Top Internal Functions/Classes:**
  * `repack_executable` (Impact: 119.9)
  * `build` (Impact: 110.0)
  * `autoclean_output` (Impact: 50.4)
  * `_fixup_darwin_rtbinary` (Impact: 17.4)
  * `build` (Impact: 14.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 123`, `args: 32`, `func_start: 32`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 110`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 91`, `api: 32`, `import: 22`
* *Defense:* `safety: 19`, `doc: 20`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.484
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` subprocess, PyInstaller.archive.readers, os, PyInstaller.utils.win32, marshal, logging, struct, tempfile...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/examples/pybench/Constructs.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.903 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.551 IQR)
- **Top Global Matches:** file_cluster_8: 7.903, file_cluster_7: 8.752, file_cluster_1: 9.017
- **Magnitude:** 479.24 | **LOC:** 565 | **CtrlFlow:** 85.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.6361%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 389.9)
  * `test` (Impact: 49.7)
  * `test` (Impact: 9.2)
  * `calibrate` (Impact: 3.8)
  * `calibrate` (Impact: 3.7)
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
- **Global Archetype:** `file_cluster_8` (Drift: 11.348 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 4.86 IQR)
- **Top Global Matches:** file_cluster_8: 11.348, file_cluster_13: 11.566, file_cluster_7: 11.689
- **Magnitude:** 399.3 | **LOC:** 955 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.1288%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `calibrate` (Impact: 155.1)
    * *Intent:* # Init vars
  * `calibrate_test` (Impact: 46.2)
  * `load_tests` (Impact: 21.3)
  * `__init__` (Impact: 16.9)
    * *Intent:* # The number of abstract operations done in each round of the # measure. The benchmark will output t...
  * `get_timer` (Impact: 16.7)
    * *Intent:* # Allow skipping calibration ? # Timer types TIMER_TIME_TIME = 'time.time' TIMER_TIME_CLOCK = 'time....
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 71`, `args: 24`, `func_start: 22`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 83`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `io: 11`, `api: 23`, `import: 9`
* *Defense:* `safety: 22`, `doc: 26`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 57.179
  * `Choke Point (Betweenness):` 0.009053 | `Ripple Effect (Closeness):` 0.083705
  * `Imports (Out-Degree: 3):` CommandLine, gc, Setup, sys, systimes, cPickle, pickle, platform...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `src/cli/shell.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.096 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.01 IQR)
- **Top Global Matches:** file_cluster_0: 12.096, file_cluster_13: 12.225, file_cluster_17: 12.398
- **Magnitude:** 398.02 | **LOC:** 482 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (48.666%), Tech Debt (26.9479%)
**Top Internal Functions/Classes:**
  * `title` (Impact: 114.4)
  * `do_push` (Impact: 15.0)
  * `do_info` (Impact: 11.4)
  * `do_set` (Impact: 11.3)
  * `remove` (Impact: 10.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 114`, `args: 58`, `func_start: 58`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 114`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 61`, `import: 6`
* *Defense:* `safety: 6`, `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.828
  * `Choke Point (Betweenness):` 0.000321 | `Ripple Effect (Closeness):` 0.018544
  * `Imports (Out-Degree: 2):` shlex, .context, .model, cmd, os.path, configparser
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/cli/__main__.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.932 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.109 IQR)
- **Top Global Matches:** file_cluster_8: 9.932, file_cluster_13: 10.208, file_cluster_7: 10.473
- **Magnitude:** 351.96 | **LOC:** 813 | **CtrlFlow:** 60.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.1666%), Tech Debt (19.0276%)
**Top Internal Functions/Classes:**
  * `_cmd_gen_key` (Impact: 118.3)
  * `cmd_gen` (Impact: 68.5)
  * `main_entry` (Impact: 30.5)
  * `gen_parser` (Impact: 22.9)
    * *Intent:* '''generate obfuscated scripts and all required runtime files pyarmor gen <options> <scripts> genera...
  * `log_settings` (Impact: 11.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 95`, `args: 21`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 15`, `fragile_debt: 4`
* *Architecture:* `io: 27`, `api: 19`, `concurrency: 1`, `import: 24`
* *Defense:* `safety: 17`, `doc: 8`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.046
  * `Choke Point (Betweenness):` 0.002246 | `Ripple Effect (Closeness):` 0.017157
  * `Imports (Out-Degree: 8):` subprocess, pyarmor.man, webbrowser, .command, os, .register, argparse, time...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cli/config.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.213 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.686 IQR)
- **Top Global Matches:** file_cluster_8: 12.213, file_cluster_17: 12.279, file_cluster_13: 12.326
- **Magnitude:** 349.22 | **LOC:** 307 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (57.6407%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `list_sections` (Impact: 112.2)
  * `run` (Impact: 52.6)
  * `_parse_opt` (Impact: 19.8)
  * `reset` (Impact: 6.9)
  * `__init__` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 38`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 134`
* *Architecture:* `io: 8`, `api: 11`, `import: 4`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.484
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fnmatch, os, configparser, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/examples/pybench/Exceptions.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.75%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.923 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.219 IQR)
- **Top Global Matches:** file_cluster_8: 11.923, file_cluster_0: 12.562, file_cluster_7: 12.584
- **Magnitude:** 340.46 | **LOC:** 700 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.2126%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 294.6)
  * `test` (Impact: 19.2)
  * `calibrate` (Impact: 3.8)
  * `calibrate` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 319`, `args: 4`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 468`, `duplicate_logic: 4`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `safety: 316`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.679
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.031888
  * `Imports (Out-Degree: 1):` pybench, timeit
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/pyarmor-deprecated.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.935 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.117 IQR)
- **Top Global Matches:** file_cluster_13: 10.935, file_cluster_8: 11.05, file_cluster_0: 11.276
- **Magnitude:** 336.76 | **LOC:** 844 | **CtrlFlow:** 74.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.3978%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_import_pytransform` (Impact: 289.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 59`, `args: 18`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 27`, `dead_code: 1`
* *Architecture:* `io: 97`, `api: 11`, `import: 20`
* *Defense:* `safety: 22`, `doc: 18`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.484
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` config, distutils.text_file, os, distutils.util, time, logging, zipfile, tempfile...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/examples/pybench/CommandLine.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.507 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.059 IQR)
- **Top Global Matches:** file_cluster_8: 12.507, file_cluster_13: 12.596, file_cluster_7: 12.689
- **Magnitude:** 332.94 | **LOC:** 643 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.5717%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 75.2)
    * *Intent:* # The help layout looks like this: # [header] - defaults to '' # # [synopsis] - formatted as '<self....
  * `fileopen` (Impact: 16.9)
    * *Intent:* # long option
  * `__str__` (Impact: 16.6)
  * `print_options` (Impact: 14.5)
  * `_getopt_flags` (Impact: 13.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 68`, `args: 30`, `func_start: 30`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 79`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 17`, `api: 39`, `import: 4`
* *Defense:* `safety: 17`, `doc: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.686
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.047619
  * `Imports (Out-Degree: 0):` glob, sys, getpass, re, os, __future__, codecs, traceback...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cli/resource.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.61 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.998 IQR)
- **Top Global Matches:** file_cluster_0: 11.61, file_cluster_13: 11.715, file_cluster_17: 11.824
- **Magnitude:** 272.68 | **LOC:** 266 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (76.3021%), Tech Debt (99.9763%)
**Top Internal Functions/Classes:**
  * `__str__` (Impact: 43.9)
  * `generate_output` (Impact: 23.7)
  * `_get_encoding` (Impact: 22.3)
    * *Intent:* # Maybe: from tokenize import detect_encoding from codecs import BOM_UTF8 from re import search as r...
  * `find_encoding` (Impact: 11.2)
  * `readlines` (Impact: 9.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 84`, `args: 32`, `func_start: 32`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 48`, `dead_code: 1`, `duplicate_logic: 8`
* *Architecture:* `io: 15`, `api: 29`, `import: 9`
* *Defense:* `safety: 8`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 27.678
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.056247
  * `Imports (Out-Degree: 0):` string, importlib._bootstrap_external, tokenize, fnmatch, datetime, re, os, ast...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/cli/command.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.807 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.537 IQR)
- **Top Global Matches:** file_cluster_8: 8.807, file_cluster_13: 9.303, file_cluster_7: 9.419
- **Magnitude:** 217.44 | **LOC:** 564 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (10.5573%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `cmd_init` (Impact: 140.3)
  * `build_parser` (Impact: 23.0)
  * `init_parser` (Impact: 9.2)
  * `env_parser` (Impact: 7.1)
  * `run` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 54`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`
* *Architecture:* `io: 4`, `api: 11`, `concurrency: 2`, `import: 16`
* *Defense:* `safety: 2`, `doc: 6`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.126
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.015238
  * `Imports (Out-Degree: 5):` .plugin, shlex, .generate, .rftbuild, sys, .context, , logging.config...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cli/plugin.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.912 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.838 IQR)
- **Top Global Matches:** file_cluster_13: 10.912, file_cluster_0: 10.92, file_cluster_17: 11.147
- **Magnitude:** 202.84 | **LOC:** 293 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.8853%), Tech Debt (50.864%)
**Top Internal Functions/Classes:**
  * `osx_merge_binary` (Impact: 60.0)
  * `post_build` (Impact: 28.8)
  * `install` (Impact: 19.0)
  * `osx_sign_binary` (Impact: 18.1)
  * `post_key` (Impact: 12.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 65`, `args: 16`, `func_start: 16`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 14`, `duplicate_logic: 2`
* *Architecture:* `io: 34`, `api: 22`, `import: 11`
* *Defense:* `safety: 13`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.773
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.030483
  * `Imports (Out-Degree: 0):` subprocess, importlib.util, sys, , shutil, os, .pyarmor_runtime
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/pytransform.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.268 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.009 IQR)
- **Top Global Matches:** file_cluster_8: 9.268, file_cluster_0: 9.272, file_cluster_13: 9.552
- **Magnitude:** 200.34 | **LOC:** 484 | **CtrlFlow:** 43.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.2945%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_hd_info` (Impact: 140.3)
  * `init_pytransform` (Impact: 13.8)
  * `dllmethod` (Impact: 1.9)
  * `version_info` (Impact: 1.9)
  * `wrap` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 97`, `args: 38`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1`, `dead_code: 1`
* *Architecture:* `io: 32`, `api: 33`, `import: 7`
* *Defense:* `safety: 10`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 42.508
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.077143
  * `Imports (Out-Degree: 0):` anything, struct, sys, fnmatch, platform, os, time, ctypes
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

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
- `src/cli/core/__init__.py` (PYTHON) | Magnitude: 46.08 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 39, branch: 13, api: 13
- `src/cli/resource.py` (PYTHON) | Magnitude: 272.68 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 179, structural_boundaries: 84, branch: 59, state_mutation: 48
- `src/cli/shell.py` (PYTHON) | Magnitude: 398.02 | Delta: **0.129 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 355, structural_boundaries: 114, state_mutation: 114, encapsulation: 103
- `src/benchmark.py` (PYTHON) | Magnitude: 167.18 | Delta: **0.18 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 192, structural_boundaries: 76, args: 35, telemetry: 33
- `src/cli/project.py` (PYTHON) | Magnitude: 717.78 | Delta: **0.186 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 624, state_mutation: 209, branch: 186, structural_boundaries: 165

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/examples/pack-obfuscated-scripts.sh` (SHELL) | Magnitude: 29.8 | Delta: **0.142 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: state_mutation: 18, branch: 9, reflection_metaprogramming: 6, safety_bypasses: 4
- `src/examples/obfuscate-app.sh` (SHELL) | Magnitude: 33.66 | Delta: **0.229 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: state_mutation: 18, branch: 10, indent_spaces: 9, reflection_metaprogramming: 8
- `src/examples/obfuscate-pkg.sh` (SHELL) | Magnitude: 50.48 | Delta: **0.243 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: branch: 21, state_mutation: 21, indent_spaces: 13, reflection_metaprogramming: 11
- `src/examples/build-with-project.sh` (SHELL) | Magnitude: 75.58 | Delta: **0.295 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: branch: 37, indent_spaces: 30, state_mutation: 27, safety_bypasses: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/cli/plugin.py` (PYTHON) | Magnitude: 202.84 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 203, branch: 68, structural_boundaries: 65, io: 34
- `src/helper/buildext.py` (PYTHON) | Magnitude: 141.1 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 144, branch: 39, structural_boundaries: 31, telemetry: 17
- `plugins/check_docker.py` (PYTHON) | Magnitude: 17.62 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 12, branch: 7, import: 3
- `src/packer.py` (PYTHON) | Magnitude: 523.46 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 482, branch: 170, structural_boundaries: 96, io: 88
- `tests.8/samples/joker/__init__.py` (PYTHON) | Magnitude: 11.56 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, import: 2, encapsulation: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/cli/generate.py` (PYTHON) | Magnitude: 155.94 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 177, branch: 50, structural_boundaries: 38, state_mutation: 32
- `tests.9/Makefile` (MAKEFILE) | Magnitude: 16.76 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 41, indent_spaces: 31, branch: 27, indent_tabs: 24
- `scripts/build-package.sh` (SHELL) | Magnitude: 1.81 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 9, state_mutation: 8, safety_bypasses: 6
- `src/polyfills/argparse.py` (PYTHON) | Magnitude: 1358.86 | Delta: **0.217 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1434, encapsulation: 483, branch: 374, structural_boundaries: 298
- `tests/Makefile` (MAKEFILE) | Magnitude: 35.78 | Delta: **0.358 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 68, structural_boundaries: 29, indent_spaces: 29, indent_tabs: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/data/t_refcnt.py` (PYTHON) | Magnitude: 0.03 | Delta: **0.153 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 23, concurrency: 12, structural_boundaries: 9, debug_prints: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/cobuilder.py` (PYTHON) | Magnitude: 130.72 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 116, branch: 59, structural_boundaries: 36, safety: 23
- `src/pytransform.py` (PYTHON) | Magnitude: 200.34 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 265, structural_boundaries: 97, branch: 75, encapsulation: 55
- `tests.8/samples/joker/card.py` (PYTHON) | Magnitude: 2.98 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, debug_prints: 2, indent_spaces: 2, args: 1
- `src/cli/bug.py` (PYTHON) | Magnitude: 20.94 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 15, doc: 10, branch: 8
- `plugins/check_multiple_machine.py` (PYTHON) | Magnitude: 25.66 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 17, encapsulation: 8, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `plugins/assert_armored.py` (PYTHON) | Magnitude: 9.6 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 8, encapsulation: 4, args: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/cli/__init__.py` -> Churn: **100.0%** | Cog Load: 81.9968% | Debt: 99.9994%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/cli/project.py` -> **Jondy Zhao** (100.0% isolated ownership) | Magnitude: 717.78
- `src/cli/register.py` -> **Jondy Zhao** (100.0% isolated ownership) | Magnitude: 695.06
- `src/cli/context.py` -> **Jondy Zhao** (100.0% isolated ownership) | Magnitude: 587.92
- `src/cli/shell.py` -> **Jondy Zhao** (100.0% isolated ownership) | Magnitude: 398.02
- `src/cli/__main__.py` -> **Jondy Zhao** (100.0% isolated ownership) | Magnitude: 351.96

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

- `src/examples/pybench/pybench.py` -> **Severity: 5.005** (Embedded: 0.0837 * Error Risk: 59.7989%)
- `src/examples/pybench/Setup.py` -> **Severity: 4.569** (Embedded: 0.0462 * Error Risk: 98.9422%)
- `src/polyfills/argparse.py` -> **Severity: 4.5** (Embedded: 0.0637 * Error Risk: 70.626%)
- `src/cli/resource.py` -> **Severity: 4.232** (Embedded: 0.0562 * Error Risk: 75.2316%)
- `src/pytransform.py` -> **Severity: 3.758** (Embedded: 0.0771 * Error Risk: 48.7134%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/pytransform.py` -> **Severity: 2879.696** (Blast Radius: 42.508 * Doc Risk: 67.7448%)
- `src/cli/resource.py` -> **Severity: 2767.8** (Blast Radius: 27.678 * Doc Risk: 100.0%)
- `src/cli/plugin.py` -> **Severity: 1277.3** (Blast Radius: 12.773 * Doc Risk: 100.0%)
- `src/utils.py` -> **Severity: 950.387** (Blast Radius: 21.759 * Doc Risk: 43.6779%)
- `src/cli/context.py` -> **Severity: 934.7** (Blast Radius: 9.347 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
