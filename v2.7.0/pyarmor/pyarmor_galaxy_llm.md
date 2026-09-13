# ARCHITECTURAL_BRIEF: pyarmor
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/dashingsoft/pyarmor.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. A high Structural Surface Profile reading (formerly called Risk Exposure; e.g., Complexity Load, formerly Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict. These are activity/content surface meters, not defect-probability estimates (gitgalaxy#2991, evidence in #2982) -- describe what is there, don't imply it predicts a bug.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates the Structural Surface Profile (Lower 0 - Higher Surface Presence 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws. These 13 vectors are activity/content surface meters -- they describe what is present in a file, not the probability of a defect. The temporal-crucible validation record (gitgalaxy#2982, ~3,550 scanned snapshots, two repositories, pre-registered) tested the per-file-standing-risk claim to exhaustion and found it does not hold; see docs/vectors.md for the full record and gitgalaxy#2991 for the rename this drove. `risk_*` names remain the underlying column/key names for schema compatibility -- see the 'formerly' aliases below.
> 
> 1. **Complexity Load** (formerly Cognitive Load Exposure)**:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Guard Balance** (formerly Error & Exception Risk Exposure)**:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Debt Markers** (formerly Tech Debt Exposure)**:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Test Surface** (formerly Verification Risk Exposure)**:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **Connectivity** (formerly API Risk Exposure)**:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Surface** (formerly Concurrency Risk Exposure)**:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **Mutation Surface** (formerly State Flux Risk Exposure)**:** Measures the frequency of data mutation and variable reassignment.
> 8. **Dead Code Surface** (formerly Commented Logic (dead code))**:** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Alignment** (formerly Spec Match Risk Exposure)**:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Historical Stability** (formerly Stability; predictive layer, promotion pending #2987)**:** Measures the recency of edits relative to the repository's entire lifespan. Part of the family the validation record actually supports as predictive -- currently ablated to zero in every scan (`GITGALAXY_DISABLE_GIT_HISTORY`, temporal-crucible#29).
> 11. **Historical Churn** (formerly Deep Churn; predictive layer, promotion pending #2987)**:** Measures the historical volatility and frequency of modification. Same predictive-layer status and ablation caveat as Historical Stability above.
> 12. **Documentation Surface** (formerly Documentation Risk Exposure)**:** Of the units extracted from a file, the weight-share a reader cannot recover from documentation -- public units count double, runtime-dynamic units count more, and a folder-level documentation umbrella shields the whole file. A ratio over units, not a density over lines; files with no extracted units have no value.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Credential Material** (formerly Secrets Risk Exposure)**:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 263 |
| Analyzed Artifacts (Scanned) | 193 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 70 |
| Total LOC | 28991 |
| Volatility Index | 0.016 |
| % Scanned of codebase = | 73.4% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7795 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5475 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 13.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.9878 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 15 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 137 | 23381 | 71.0% |
| SHELL | 19 | 4662 | 9.8% |
| MARKDOWN | 13 | 0 | 6.7% |
| PLAINTEXT | 11 | 3 | 5.7% |
| BATCH | 6 | 370 | 3.1% |
| MAKEFILE | 4 | 513 | 2.1% |
| BINARY_THREAT | 2 | 2 | 1.0% |
| C | 1 | 60 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.276`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 167 | 86.5% |
| Unknown | 5 | 2.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 21 | 10.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 70*

**Composition by Extension & Reason:**
- `.rst`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 18x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 287 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 2 exceeds 500 chars)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.8`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.9`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.02`: 1x Excluded (Unsupported Extension: '.02')
- `.cfg`: 1x Unsupported Format (.cfg)
- `.tri`: 1x Excluded (Binary Format Detected)
- `.zip`: 1x Excluded (Explicitly Denied Extension: '.zip')
- `.lic`: 1x Excluded (Binary Format Detected)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 97.8 | 34.3 | 32.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 67.3 | 87.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 11.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 82.0 | 18.2 | 7.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 39.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 91.7 | 2.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 71.6 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.4 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 56.1 | 63.4 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 68.3 | 0.5 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 241 | 52 | 4 | `src/utils.py` |
| cleanup | 121 | 32 | 2 | `src/examples/pybench/With.py` |
| guards | 1117 | 81 | 14 | `src/examples/pybench/Exceptions.py` |
| danger | 3216 | 105 | 30 | `tests/function-test.sh` |
| concurrency | 134 | 32 | 2 | `tests/function-test.sh` |
| connectivity | 1417 | 117 | 21 | `src/cli/context.py` |
| io | 3443 | 86 | 30 | `tests/function-test.sh` |
| crypto | 5 | 4 | 0 | `src/utils.py` |
| ipc | 48 | 25 | 1 | `tests.8/Makefile` |
| time | 22 | 9 | 0 | `src/examples/pybench/systimes.py` |
| serialization | 6 | 3 | 0 | `tests.8/Makefile` |
| regex | 58 | 14 | 0 | `tests/integration-test.sh` |
| events | 855 | 34 | 8 | `src/pyarmor.py` |
| tests | 229 | 25 | 1 | `tests/test-sppmode.py` |
| docs | 441 | 45 | 4 | `tests.9/script_factory.py` |
| debt | 1048 | 87 | 10 | `tests/function-test.sh` |
| mutation | 14676 | 142 | 213 | `src/examples/pybench/Arithmetic.py` |
| dead_code | 321 | 42 | 3 | `src/polyfills/argparse.py` |
| credential | 2 | 2 | 0 | `tests/function-test.sh` |
| threat | 300 | 42 | 3 | `src/cli/context.py` |
| ml_ai | 13 | 6 | 0 | `tests/test-header.sh` |
| ui | 20 | 2 | 0 | `tests/integration-test.sh` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/function-test.sh` (Hits: 814)
- `tests/integration-test.sh` (Hits: 468)
- `src/utils.py` (Hits: 248)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **pybench.py** (`src/examples/pybench/pybench.py`) — 15 inbound connections
2. **pytransform.py** (`src/pytransform.py`) — 13 inbound connections
3. **argparse.py** (`src/polyfills/argparse.py`) — 11 inbound connections
4. **test-header.sh** (`tests/test-header.sh`) — 9 inbound connections
5. **context.py** (`src/cli/context.py`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **utils.py** (`src/utils.py`) — 24 outbound dependencies
2. **__main__.py** (`src/cli/__main__.py`) — 23 outbound dependencies
3. **repack.py** (`src/cli/repack.py`) — 20 outbound dependencies
4. **pyarmor-deprecated.py** (`src/pyarmor-deprecated.py`) — 20 outbound dependencies
5. **context.py** (`src/cli/context.py`) — 18 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `test` (@ `src/examples/pybench/Constructs.py`) -> Impact: **322.5** | LOC: 454
- `encrypt_script` (@ `src/utils.py`) -> Impact: **239.5** | LOC: 89
- `__global_context__` (@ `tests/integration-test.sh`) -> Impact: **158.7** | LOC: 773
- `_build` (@ `src/pyarmor.py`) -> Impact: **131.2** | LOC: 192
  * *Intent:* '''Build project, obfuscate all scripts in the project.'''
- `_obfuscate` (@ `src/pyarmor.py`) -> Impact: **128.4** | LOC: 192
  * *Intent:* '''Obfuscate scripts without project.'''
- `__global_context__` (@ `tests/function-test.sh`) -> Impact: **124.0** | LOC: 1401
- `_parse_known_args` (@ `src/polyfills/argparse.py`) -> Impact: **105.7** | LOC: 234
  * *Intent:* # replace arg strings that are file references if self.fromfile_prefix_chars is not None: arg_strings = self._read_args_from_files(arg_strings) # map ...
- `_pyinstaller` (@ `src/packer.py`) -> Impact: **104.3** | LOC: 128
  * *Intent:* ''' Args: src: str - (absolute) or (relative to cwd) path for root; entry: str - (absolute) or (relative to cwd) path for entry script; output: str - ...
- `_patch_specfile` (@ `src/packer.py`) -> Impact: **101.1** | LOC: 98
- `do_encrypt` (@ `src/pyarmor-deprecated.py`) -> Impact: **81.0** | LOC: 235
  * *Intent:* '''Usage: pyarmor encrypt [OPTIONS] [File Patterns or @Filename] Encrpty the files list in the command line, you can use a specified pattern according...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 24 | 23475.16 | 37.27% | 0.8% |
| `src/cli` | 20 | 7480.88 | 61.76% | 27.64% |
| `src/examples/pybench` | 20 | 5920.78 | 44.16% | 0.0% |
| `tests` | 18 | 2762.2 | 22.85% | 0.0% |
| `src/polyfills` | 2 | 2440.32 | 78.89% | 50.0% |
| `src/helper` | 9 | 1004.0 | 51.54% | 3.0% |
| `tests.8` | 5 | 465.04 | 38.83% | 69.99% |
| `__monolith__` | 7 | 353.96 | 6.81% | 14.27% |
| `plugins` | 9 | 353.74 | 30.52% | 13.83% |
| `tests.9` | 5 | 286.38 | 29.61% | 46.19% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/cli/bug.py` -> **100.0%** Exposure
- `src/polyfills/__init__.py` -> **100.0%** Exposure
- `tests.8/test_pack.py` -> **99.992%** Exposure
- `tests.9/accept_test.py` -> **99.9877%** Exposure
- `tests.9/accept_test_nogil.py` -> **99.9828%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `gh.py` -> **100.0%** Exposure
- `plugins/check_multi_mac.py` -> **100.0%** Exposure
- `src/build_meta.py` -> **100.0%** Exposure
- `src/cli/bootstrap.py` -> **100.0%** Exposure
- `src/cli/bug.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/test-sppmode.py` -> **48** Orphaned Functions | **4** Duplicates
- `tests.8/accept_test.py` -> **35** Orphaned Functions | **0** Duplicates
- `tests/test-pyarmor.py` -> **24** Orphaned Functions | **0** Duplicates
- `gh.py` -> **14** Orphaned Functions | **0** Duplicates
- `src/examples/pybench/Calls.py` -> **0** Orphaned Functions | **14** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/system-test.sh` -> **68.2759%** Exposure
- `tests/function-test.sh` -> **13.9011%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `637` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/cli/generate.py` (PYTHON) -> Cumulative Risk: **660.49**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 297.24 | **LOC:** 257 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.0948%), Verification (80.0%)
- **Heaviest Functions:** `process_extra` (Impact: 17.8), `process` (Impact: 17.6), `async_obfuscate_scripts` (Impact: 17.6)

### 2. `src/cli/context.py` (PYTHON) -> Cumulative Risk: **650.05**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 751.82 | **LOC:** 791 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (97.0338%), Cognitive Load (92.3277%), State Flux (85.0%)
- **Heaviest Functions:** `format_platform` (Impact: 32.2), `__init__` (Impact: 31.3), `version_info` (Impact: 29.3)

### 3. `src/cli/resource.py` (PYTHON) -> Cumulative Risk: **636.84**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 337.38 | **LOC:** 266 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.7892%), Cognitive Load (88.8358%)
- **Heaviest Functions:** `rebuild` (Impact: 36.4), `generate_output` (Impact: 23.7), `_get_encoding` (Impact: 18.8)

### 4. `src/cli/__init__.py` (PYTHON) -> Cumulative Risk: **635.88**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 35.32 | **LOC:** 47 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Tech Debt (99.8499%), State Flux (99.6316%)
- **Heaviest Functions:** `__getattr__` (Impact: 11.1), `process` (Impact: 2.4), `trace` (Impact: 2.4)

### 5. `src/cli/shell.py` (PYTHON) -> Cumulative Risk: **632.15**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 527.92 | **LOC:** 482 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.5738%), Verification (80.0%)
- **Heaviest Functions:** `do_push` (Impact: 12.9), `do_cd` (Impact: 12.8), `get_sections` (Impact: 12.4)

### 6. `src/cli/register.py` (PYTHON) -> Cumulative Risk: **630.59**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1009.48 | **LOC:** 1091 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.4184%), Churn (80.72%)
- **Heaviest Functions:** `prepare` (Impact: 70.8), `_register_offline_license` (Impact: 36.1), `request_device_regfile` (Impact: 27.1)

### 7. `src/cli/__main__.py` (PYTHON) -> Cumulative Risk: **628.95**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 537.46 | **LOC:** 813 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9993%), Safety Score (88.6153%), Verification (80.0%)
- **Heaviest Functions:** `cmd_reg` (Impact: 52.8), `check_gen_context` (Impact: 47.5), `format_gen_args` (Impact: 44.7)

### 8. `src/polyfills/argparse.py` (PYTHON) -> Cumulative Risk: **621.22**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2391.66 | **LOC:** 2361 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.3519%), Documentation (98.0%)
- **Heaviest Functions:** `_parse_known_args` (Impact: 105.7), `_format_usage` (Impact: 63.3), `_format_actions_usage` (Impact: 60.8)

### 9. `src/polyfills/__init__.py` (PYTHON) -> Cumulative Risk: **614.14**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 48.66 | **LOC:** 63 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `get_platform` (Impact: 16.9)

### 10. `src/cli/command.py` (PYTHON) -> Cumulative Risk: **611.21**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 377.64 | **LOC:** 564 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Safety Score (90.8232%), Verification (80.0%)
- **Heaviest Functions:** `cmd_init` (Impact: 60.8), `cmd_build` (Impact: 47.9), `cmd_env` (Impact: 31.6)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.057
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.057
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/utils.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2759.24 | **LOC:** 1872 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.1843%), Tech Debt (10.5511%)
**Top Internal Functions/Classes:**
  * `encrypt_script` (Impact: 239.5)
  * `check_cross_platform` (Impact: 77.4)
  * `_check_code_object_for_super_mode` (Impact: 73.4)
  * `_patch_extension` (Impact: 65.1)
  * `make_runtime` (Impact: 58.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 402 instances
* *High Risk Execution (weighted view):* 2
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 1268
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 528`, `structural_boundaries: 348`, `args: 82`, `func_start: 82`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 3`, `state_mutation: 464`, `dead_code: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 248`, `api: 48`, `import: 23`
* *Defense:* `safety: 30`, `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.098
  * `Choke Point (Betweenness):` 0.001445 | `Ripple Effect (Closeness):` 0.020833
  * `Imports (Out-Degree: 4):` base64, cobuilder, codecs, config, dis, glob, hashlib, io...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/polyfills/argparse.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2391.66 | **LOC:** 2361 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.8865%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_parse_known_args` (Impact: 105.7)
    * *Intent:* # replace arg strings that are file references if self.fromfile_prefix_chars is not None: arg_string...
  * `_format_usage` (Impact: 63.3)
  * `_format_actions_usage` (Impact: 60.8)
    * *Intent:* # find group indices and identify actions in groups group_actions = set() inserts = {} for group in ...
  * `_get_values` (Impact: 48.4)
    * *Intent:* # ======================== # Value conversion methods # ======================== # for everything bu...
  * `__init__` (Impact: 44.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 351 instances
* *State Mutation (weighted view):* 1194
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 363`, `structural_boundaries: 304`, `args: 127`, `func_start: 127`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 492`, `dead_code: 54`
* *Architecture:* `io: 6`, `api: 51`, `import: 9`
* *Defense:* `safety: 35`, `doc: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 27.457
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.055748
  * `Imports (Out-Degree: 0):` copy, gettext, os, re, sys, textwrap, warnings
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/pyarmor.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1545.32 | **LOC:** 1648 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.4854%), Tech Debt (8.7223%)
**Top Internal Functions/Classes:**
  * `_build` (Impact: 131.2)
    * *Intent:* '''Build project, obfuscate all scripts in the project.'''
  * `_obfuscate` (Impact: 128.4)
    * *Intent:* '''Obfuscate scripts without project.'''
  * `_licenses` (Impact: 75.0)
    * *Intent:* '''Generate licenses for obfuscated scripts.'''
  * `_parser` (Impact: 54.7)
  * `licenses` (Impact: 46.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 3 instances
* *Amplified Cascading Flux:* 238 instances
* *High Risk Execution (weighted view):* 2
* *Sec Tainted Injection (weighted view):* 3
* *State Mutation (weighted view):* 747
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 436`, `structural_boundaries: 146`, `args: 33`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 3`, `state_mutation: 271`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 126`, `api: 9`, `import: 16`
* *Defense:* `safety: 11`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.582
  * `Choke Point (Betweenness):` 0.002154 | `Ripple Effect (Closeness):` 0.01875
  * `Imports (Out-Degree: 4):` .cli.__main__, config, logging, or, os, packer, polyfills.argparse, project...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/examples/pybench/Constructs.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1080.84 | **LOC:** 565 | **CtrlFlow:** 47.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.8041%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 322.5)
  * `test` (Impact: 41.1)
  * `test` (Impact: 7.6)
  * `calibrate` (Impact: 3.2)
  * `calibrate` (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 227 instances
* *State Mutation (weighted view):* 681
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 244`, `structural_boundaries: 40`, `args: 6`, `func_start: 6`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 227`
* *Architecture:* `api: 9`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.162
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.02963
  * `Imports (Out-Degree: 1):` pybench
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cli/project.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1041.18 | **LOC:** 1282 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.3698%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `load` (Impact: 45.5)
    * *Intent:* """Init project object with dict It equals: 1. map init data to ProjectItem 2. map ProjectItem to pr...
  * `search_item` (Impact: 25.3)
  * `scan_path` (Impact: 23.0)
  * `_preview_autofix_3` (Impact: 21.9)
  * `_preview_autofix_2` (Impact: 13.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 161 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 531
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 174`, `args: 72`, `func_start: 72`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 2`, `state_mutation: 209`, `dead_code: 9`
* *Architecture:* `io: 15`, `api: 68`, `import: 14`
* *Defense:* `safety: 4`, `doc: 43`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` abc, ast, builtins, collections, extension, fnmatch, glob, json...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cli/register.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1009.48 | **LOC:** 1091 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (66.0446%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `prepare` (Impact: 70.8)
  * `_register_offline_license` (Impact: 36.1)
  * `request_device_regfile` (Impact: 27.1)
  * `register_regfile` (Impact: 26.1)
  * `_group_license_helper` (Impact: 24.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 133 instances
* *State Mutation (weighted view):* 459
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 197`, `args: 40`, `func_start: 40`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 193`
* *Architecture:* `io: 34`, `api: 25`, `import: 24`
* *Defense:* `safety: 11`, `doc: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , base64, datetime, http.client, json, os, platform, pyarmor.cli.core...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cli/repack.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 763.1 | **LOC:** 794 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.8601%), Tech Debt (10.9097%)
**Top Internal Functions/Classes:**
  * `repack` (Impact: 33.8)
  * `repack_executable` (Impact: 27.0)
  * `repack_pyzarchive` (Impact: 26.9)
    * *Intent:* # logic_toc tuples: (name, src_path, typecode) # `name` is the name without suffix) # `src_path` is ...
  * `get_logical_toc` (Impact: 21.1)
  * `_fixup_darwin_rtbinary` (Impact: 15.3)
    * *Intent:* '''Unused since Pyarmor 8.3.0'''
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 118 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 410
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 141`, `args: 32`, `func_start: 32`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 1`, `state_mutation: 174`, `fragile_debt: 1`
* *Architecture:* `io: 93`, `api: 32`, `import: 22`
* *Defense:* `safety: 13`, `doc: 10`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PyInstaller, PyInstaller.archive.readers, PyInstaller.archive.writers, PyInstaller.compat, PyInstaller.config, PyInstaller.depend, PyInstaller.loader.pyimod01_archive, PyInstaller.loader.pyimod02_archive...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cli/context.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 751.82 | **LOC:** 791 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (92.3277%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `format_platform` (Impact: 32.2)
  * `__init__` (Impact: 31.3)
  * `version_info` (Impact: 29.3)
    * *Intent:* # 8.0.1 # 8.0.1 (trial) # 8.0.1 (basic), 002000 # 8.0.1 (group), 002002, Product # 8.0.1 (group), 00...
  * `get_res_options` (Impact: 14.8)
  * `_named_config` (Impact: 10.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 81 instances
* *State Mutation (weighted view):* 282
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 256`, `args: 101`, `func_start: 101`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 120`
* *Architecture:* `io: 53`, `api: 93`, `import: 16`
* *Defense:* `safety: 3`, `doc: 4`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.204
  * `Choke Point (Betweenness):` 8.2e-05 | `Ripple Effect (Closeness):` 0.025862
  * `Imports (Out-Degree: 1):` .plugin, .pyarmor_runtime, .register, __pyarmor__, base64, configparser, fnmatch, importlib.machinery...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/packer.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 751.26 | **LOC:** 721 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.5325%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_pyinstaller` (Impact: 104.3)
    * *Intent:* ''' Args: src: str - (absolute) or (relative to cwd) path for root; entry: str - (absolute) or (rela...
  * `_patch_specfile` (Impact: 101.1)
  * `packer` (Impact: 26.5)
  * `_packer` (Impact: 20.9)
  * `__obfuscate_dependency_pkgs` (Impact: 16.1)
    * *Intent:* ''' Args: package_names: List[str] - packages' distribution names obf_options: List[str] - obfuscati...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 105 instances
* *High Risk Execution (weighted view):* 1
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 333
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 114`, `args: 26`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 2`, `state_mutation: 123`, `dead_code: 2`
* *Architecture:* `io: 92`, `api: 14`, `import: 16`
* *Defense:* `safety: 13`, `doc: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.306
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.015012
  * `Imports (Out-Degree: 1):` PyInstaller.config, codecs, distutils.util, glob, json, logging, os, pkg_resources...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/examples/pybench/Arithmetic.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 718.92 | **LOC:** 778 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.6772%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 4.8)
  * `test` (Impact: 4.8)
  * `test` (Impact: 4.8)
  * `test` (Impact: 4.8)
  * `test` (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 653
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 22`, `args: 10`, `func_start: 10`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 565`, `duplicate_logic: 5`
* *Architecture:* `api: 15`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.162
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.02963
  * `Imports (Out-Degree: 1):` pybench
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/examples/pybench/pybench.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 698.1 | **LOC:** 955 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.9823%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `print_comparison` (Impact: 57.2)
    * *Intent:* # Check benchmark versions if compare_to.version != self.version: print('* Benchmark versions differ...
  * `main` (Impact: 34.0)
  * `__init__` (Impact: 22.5)
  * `load_tests` (Impact: 21.3)
    * *Intent:* # Add tests if self.verbose: print('Searching for tests ...') print('-------------------------------...
  * `__init__` (Impact: 16.9)
    * *Intent:* # Set parameters if warp is not None: self.rounds = int(self.rounds / warp) if self.rounds == 0: rai...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 115 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 398
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 80`, `args: 24`, `func_start: 22`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 2`, `state_mutation: 168`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 11`, `api: 23`, `import: 9`
* *Defense:* `safety: 19`, `doc: 13`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 53.423
  * `Choke Point (Betweenness):` 0.007444 | `Ripple Effect (Closeness):` 0.078431
  * `Imports (Out-Degree: 3):` CommandLine, Setup, __future__, cPickle, gc, operator, pickle, platform...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `src/examples/pybench/Lookups.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 667.5 | **LOC:** 946 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.481%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 5.8)
  * `test` (Impact: 5.8)
  * `test` (Impact: 5.8)
  * `test` (Impact: 5.8)
  * `test` (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 595
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 38`, `args: 10`, `func_start: 10`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 503`, `duplicate_logic: 4`
* *Architecture:* `api: 15`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.162
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.02963
  * `Imports (Out-Degree: 1):` pybench
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/pyarmor-deprecated.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 656.06 | **LOC:** 844 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.3131%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `do_encrypt` (Impact: 81.0)
    * *Intent:* '''Usage: pyarmor encrypt [OPTIONS] [File Patterns or @Filename] Encrpty the files list in the comma...
  * `do_license` (Impact: 48.4)
    * *Intent:* ''' Usage: pyarmor license [Options] [CODE] Generate a registration code for project capsule, save i...
  * `encrypt_files` (Impact: 31.0)
    * *Intent:* '''Encrypt all the files, all the encrypted scripts will be plused with a suffix 'e', for example, h...
  * `_parse_file_args` (Impact: 25.7)
  * `do_capsule` (Impact: 16.7)
    * *Intent:* '''Usage: pyarmor capsule [OPTIONS] [NAME] Generate a capsule which used to encrypt/decrypt python s...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 3 instances
* *Amplified Cascading Flux:* 119 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 3
* *State Mutation (weighted view):* 372
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 72`, `args: 18`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 3`, `state_mutation: 134`, `dead_code: 1`
* *Architecture:* `io: 85`, `api: 11`, `import: 18`
* *Defense:* `safety: 19`, `doc: 9`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` binascii, config, distutils.filelist, distutils.text_file, distutils.util, fnmatch, getopt, glob...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test-sppmode.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 612.2 | **LOC:** 741 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.2512%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_list_comp` (Impact: 21.9)
  * `test_set_comp` (Impact: 21.9)
  * `test_boolop` (Impact: 19.1)
  * `test_dict_comp` (Impact: 19.0)
  * `test_with_statement` (Impact: 12.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 203
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 218`, `args: 94`, `func_start: 93`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 111`, `fragile_debt: 3`, `duplicate_logic: 4`, `unreferenced_by_name: 48`
* *Architecture:* `io: 6`, `api: 80`, `import: 10`
* *Defense:* `safety: 45`, `doc: 1`, `test: 50`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` decimal, gc, os, os.path, sys, tempfile, unittest, weakref
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cli/config.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 550.92 | **LOC:** 307 | **CtrlFlow:** 39.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (58.1719%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 52.6)
  * `_set_option` (Impact: 44.5)
  * `_list_value` (Impact: 30.7)
  * `list_options` (Impact: 25.9)
  * `_remove` (Impact: 25.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 92 instances
* *State Mutation (weighted view):* 285
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 40`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 101`
* *Architecture:* `io: 8`, `api: 10`, `import: 4`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , configparser, fnmatch, os
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cli/__main__.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 537.46 | **LOC:** 813 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (65.1622%), Tech Debt (15.5652%)
**Top Internal Functions/Classes:**
  * `cmd_reg` (Impact: 52.8)
  * `check_gen_context` (Impact: 47.5)
  * `format_gen_args` (Impact: 44.7)
  * `gen_parser` (Impact: 19.1)
    * *Intent:* '''generate obfuscated scripts and all required runtime files pyarmor gen <options> <scripts> genera...
  * `main_entry` (Impact: 14.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 65 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 221
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 102`, `args: 21`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 91`, `fragile_debt: 3`
* *Architecture:* `io: 26`, `api: 19`, `concurrency: 1`, `import: 22`
* *Defense:* `safety: 12`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.306
  * `Choke Point (Betweenness):` 0.001718 | `Ripple Effect (Closeness):` 0.015012
  * `Imports (Out-Degree: 8):` , .bootstrap, .command, .config, .context, .generate, .plugin, .register...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cli/shell.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 527.92 | **LOC:** 482 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (63.1514%), Tech Debt (59.1182%)
**Top Internal Functions/Classes:**
  * `do_push` (Impact: 12.9)
    * *Intent:* """Append new value to option"""
  * `do_cd` (Impact: 12.8)
    * *Intent:* """Switch to section, .. to parent, blank to top"""
  * `get_sections` (Impact: 12.4)
  * `do_info` (Impact: 11.3)
    * *Intent:* """List sections, options, and all the values"""
  * `do_use` (Impact: 11.2)
    * *Intent:* """Switch domain: global, local, project"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 203
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 115`, `args: 58`, `func_start: 58`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 95`, `duplicate_logic: 4`
* *Architecture:* `io: 2`, `api: 56`, `import: 6`
* *Defense:* `safety: 4`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.237
  * `Choke Point (Betweenness):` 0.000245 | `Ripple Effect (Closeness):` 0.016226
  * `Imports (Out-Degree: 2):` .context, .model, cmd, configparser, os.path, shlex
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/examples/pybench/CommandLine.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 522.84 | **LOC:** 643 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.8837%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 27.7)
    * *Intent:* """ Parse the command line and fill in self.values and self.files. After having parsed the options, ...
  * `__init__` (Impact: 26.0)
    * *Intent:* # Setup application specs if argv is None: argv = sys.argv self.filename = os.path.split(argv[0])[1]...
  * `fileopen` (Impact: 17.3)
    * *Intent:* """ Open a file using mode. Default mode is 'wb' meaning to open the file for writing in binary mode...
  * `srange` (Impact: 13.3)
  * `print_options` (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Rce:* 3 instances
* *Amplified Cascading Flux:* 89 instances
* *High Risk Execution (weighted view):* 1
* *Sec Tainted Injection (weighted view):* 3
* *State Mutation (weighted view):* 294
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 69`, `args: 30`, `func_start: 30`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 3`, `state_mutation: 116`, `planned_debt: 1`
* *Architecture:* `io: 17`, `api: 30`, `import: 4`
* *Defense:* `safety: 15`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.196
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.044271
  * `Imports (Out-Degree: 0):` __future__, codecs, getopt, getpass, glob, os, re, sys...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/protect_code.pt` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/protect_code2.pt` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/pytransform.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 453.96 | **LOC:** 484 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.2781%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_load_library` (Impact: 76.8)
    * *Intent:* # Load _pytransform library
  * `format_platform` (Impact: 24.3)
  * `get_hd_info` (Impact: 12.7)
  * `get_license_info` (Impact: 10.2)
  * `pyarmor_runtime` (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 52 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 204
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 97`, `args: 38`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`, `state_mutation: 100`, `dead_code: 1`
* *Architecture:* `io: 31`, `api: 33`, `import: 7`
* *Defense:* `safety: 7`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 39.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.069637
  * `Imports (Out-Degree: 0):` anything, ctypes, fnmatch, os, platform, struct, sys, time
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `tests/function-test.sh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 418.2 | **LOC:** 2161 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.1341%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__global_context__` (Impact: 124.0)
  * `Anonymous_Block` (Impact: 21.9)
    * *Intent:* # ====================================================================== # # Super mode # # ========...
  * `Anonymous_Block` (Impact: 15.1)
  * `Anonymous_Block` (Impact: 8.8)
  * `Anonymous_Block` (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 145
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 313`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 901`, `state_mutation: 95`, `fragile_debt: 1`
* *Architecture:* `io: 814`, `concurrency: 5`, `import: 1`
* *Defense:* `test: 6`, `sync_locks: 22`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.057
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` test-header.sh
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/cli/__init__.py` -> Churn: **100.0%** | Cog Load: 71.5042% | Debt: 99.8499%
- `src/cli/register.py` -> Churn: **80.72%** | Cog Load: 66.0446% | Debt: 0.0%
- `src/cli/command.py` -> Churn: **61.71%** | Cog Load: 64.8334% | Debt: 0.0%
- `src/cli/__main__.py` -> Churn: **58.62%** | Cog Load: 65.1622% | Debt: 15.5652%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/cli/project.py` -> **Jondy Zhao** (100.0% isolated ownership) | Magnitude: 1041.18
- `src/cli/register.py` -> **Jondy Zhao** (100.0% isolated ownership) | Magnitude: 1009.48
- `src/cli/context.py` -> **Jondy Zhao** (100.0% isolated ownership) | Magnitude: 751.82
- `src/cli/config.py` -> **Jondy Zhao** (100.0% isolated ownership) | Magnitude: 550.92
- `src/cli/__main__.py` -> **Jondy Zhao** (100.0% isolated ownership) | Magnitude: 537.46

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/pyarmor.py` -> **Severity: 0.215** (Bridge: 0.0022 * Flux: 100.0%)
- `src/cli/__main__.py` -> **Severity: 0.172** (Bridge: 0.0017 * Flux: 99.9993%)
- `src/utils.py` -> **Severity: 0.145** (Bridge: 0.0014 * Flux: 100.0%)
- `src/sppmode.py` -> **Severity: 0.041** (Bridge: 0.0004 * Flux: 100.0%)
- `src/cli/generate.py` -> **Severity: 0.027** (Bridge: 0.0003 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/examples/pybench/pybench.py` -> **Severity: 7.62** (Embedded: 0.0784 * Error Risk: 97.1555%)
- `src/pytransform.py` -> **Severity: 6.768** (Embedded: 0.0696 * Error Risk: 97.1865%)
- `src/polyfills/argparse.py` -> **Severity: 5.539** (Embedded: 0.0557 * Error Risk: 99.3519%)
- `src/cli/resource.py` -> **Severity: 4.982** (Embedded: 0.051 * Error Risk: 97.7892%)
- `tests/test-header.sh` -> **Severity: 4.634** (Embedded: 0.0469 * Error Risk: 98.8638%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/examples/pybench/pybench.py` -> **Severity: 3205.38** (Blast Radius: 53.423 * Doc Risk: 60.0%)
- `tests/data/pub_foo.py` -> **Severity: 2962.8** (Blast Radius: 29.628 * Doc Risk: 100.0%)
- `src/polyfills/argparse.py` -> **Severity: 2690.786** (Blast Radius: 27.457 * Doc Risk: 98.0%)
- `tests/test-header.sh` -> **Severity: 2644.8** (Blast Radius: 26.448 * Doc Risk: 100.0%)
- `src/examples/pybench/systimes.py` -> **Severity: 1871.55** (Blast Radius: 20.795 * Doc Risk: 90.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
