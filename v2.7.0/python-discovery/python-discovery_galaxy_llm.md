# ARCHITECTURAL_BRIEF: python-discovery
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
| Total Artifacts | 37 |
| Analyzed Artifacts (Scanned) | 26 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 11 |
| Total LOC | 4051 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 70.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4067 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0966 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7095 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 8 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 24 | 4051 | 92.3% |
| MARKDOWN | 2 | 0 | 7.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 24 | 92.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 7.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 11*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.py`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 64.4 | 29.0 | 33.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 1.7 | 98.7 | 59.4 | 61.2 | 52.1 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 12.8 | 0.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.7 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 75.9 | 21.6 | 12.6 | 25.7 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 34.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 9.9 | 0.8 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 87.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 81.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 193 | 16 | 18 | `python_discovery-1.2.1/tests/test_discovery.py` |
| cleanup | 1 | 1 | 0 | `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py` |
| guards | 551 | 20 | 46 | `python_discovery-1.2.1/tests/test_py_info_extra.py` |
| danger | 66 | 16 | 4 | `python_discovery-1.2.1/src/python_discovery/_py_info.py` |
| concurrency | 62 | 9 | 5 | `python_discovery-1.2.1/src/python_discovery/_discovery.py` |
| connectivity | 361 | 23 | 31 | `python_discovery-1.2.1/tests/test_py_info_extra.py` |
| io | 165 | 17 | 17 | `python_discovery-1.2.1/src/python_discovery/_py_info.py` |
| crypto | 2 | 2 | 0 | `python_discovery-1.2.1/src/python_discovery/_cache.py` |
| ipc | 12 | 3 | 0 | `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 6 | 3 | 0 | `python_discovery-1.2.1/src/python_discovery/_windows/_pep514.py` |
| events | 0 | 0 | 0 | - |
| tests | 530 | 13 | 69 | `python_discovery-1.2.1/tests/test_py_info_extra.py` |
| docs | 80 | 13 | 9 | `python_discovery-1.2.1/src/python_discovery/_py_info.py` |
| debt | 3 | 2 | 0 | `python_discovery-1.2.1/tests/test_cached_py_info.py` |
| mutation | 1938 | 24 | 179 | `python_discovery-1.2.1/src/python_discovery/_py_info.py` |
| dead_code | 255 | 15 | 28 | `python_discovery-1.2.1/tests/test_py_info_extra.py` |
| credential | 1 | 1 | 0 | `python_discovery-1.2.1/tests/windows/test_windows_pep514.py` |
| threat | 49 | 5 | 2 | `python_discovery-1.2.1/src/python_discovery/_py_info.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.7647**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `python_discovery-1.2.1/src/python_discovery/_py_info.py` (Hits: 49)
- `python_discovery-1.2.1/src/python_discovery/_discovery.py` (Hits: 21)
- `python_discovery-1.2.1/tests/test_discovery.py` (Hits: 18)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **_py_info.py** (`python_discovery-1.2.1/src/python_discovery/_py_info.py`) — 8 inbound connections
2. **_cache.py** (`python_discovery-1.2.1/src/python_discovery/_cache.py`) — 6 inbound connections
3. **_discovery.py** (`python_discovery-1.2.1/src/python_discovery/_discovery.py`) — 4 inbound connections
4. **_cached_py_info.py** (`python_discovery-1.2.1/src/python_discovery/_cached_py_info.py`) — 3 inbound connections
5. **_compat.py** (`python_discovery-1.2.1/src/python_discovery/_compat.py`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **_py_info.py** (`python_discovery-1.2.1/src/python_discovery/_py_info.py`) — 23 outbound dependencies
2. **_cached_py_info.py** (`python_discovery-1.2.1/src/python_discovery/_cached_py_info.py`) — 18 outbound dependencies
3. **test_py_info.py** (`python_discovery-1.2.1/tests/py_info/test_py_info.py`) — 16 outbound dependencies
4. **_discovery.py** (`python_discovery-1.2.1/src/python_discovery/_discovery.py`) — 14 outbound dependencies
5. **test_discovery.py** (`python_discovery-1.2.1/tests/test_discovery.py`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `test_discovery_via_path` (@ `python_discovery-1.2.1/tests/test_discovery.py`) -> Impact: **52.3** | LOC: 40
- `_get_via_file_cache` (@ `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py`) -> Impact: **41.8** | LOC: 52
- `_mock_pyinfo` (@ `python_discovery-1.2.1/tests/windows/conftest.py`) -> Impact: **35.6** | LOC: 26
- `satisfies` (@ `python_discovery-1.2.1/src/python_discovery/_py_info.py`) -> Impact: **33.1** | LOC: 23
  * *Intent:* """ Check if a given specification can be satisfied by this python interpreter instance. :param spec: the specification to check against. :param impl_...
- `from_string` (@ `python_discovery-1.2.1/src/python_discovery/_specifier.py`) -> Impact: **32.3** | LOC: 22
  * *Intent:* """ Parse a PEP 440 version string (e.g. ``3.12.1``). :param version_str: the version string to parse. """
- `discover_exe` (@ `python_discovery-1.2.1/src/python_discovery/_py_info.py`) -> Impact: **31.3** | LOC: 39
- `_run_subprocess` (@ `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py`) -> Impact: **30.8** | LOC: 56
- `_check_exe` (@ `python_discovery-1.2.1/src/python_discovery/_py_info.py`) -> Impact: **29.8** | LOC: 30
- `_find_interpreter` (@ `python_discovery-1.2.1/src/python_discovery/_discovery.py`) -> Impact: **25.7** | LOC: 25
- `propose_interpreters` (@ `python_discovery-1.2.1/src/python_discovery/_windows/_propose.py`) -> Impact: **23.1** | LOC: 23

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `python_discovery-1.2.1/src/python_discovery` | 7 | 1970.82 | 33.46% | 0.0% |
| `python_discovery-1.2.1/tests` | 8 | 1386.3 | 31.01% | 0.0% |
| `python_discovery-1.2.1/tests/py_info` | 2 | 390.14 | 31.24% | 0.0% |
| `python_discovery-1.2.1/tests/windows` | 4 | 267.4 | 10.1% | 0.0% |
| `python_discovery-1.2.1/src/python_discovery/_windows` | 3 | 257.26 | 37.1% | 4.28% |
| `python_discovery-1.2.1` | 2 | 2.22 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `python_discovery-1.2.1/src/python_discovery/_windows/_pep514.py` -> **12.8397%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py` -> **100.0%** Exposure
- `python_discovery-1.2.1/src/python_discovery/_discovery.py` -> **100.0%** Exposure
- `python_discovery-1.2.1/src/python_discovery/_py_info.py` -> **100.0%** Exposure
- `python_discovery-1.2.1/src/python_discovery/_specifier.py` -> **100.0%** Exposure
- `python_discovery-1.2.1/src/python_discovery/_windows/_pep514.py` -> **99.9997%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `python_discovery-1.2.1/tests/test_py_info_extra.py` -> **59** Orphaned Functions | **0** Duplicates
- `python_discovery-1.2.1/tests/test_specifier.py` -> **39** Orphaned Functions | **0** Duplicates
- `python_discovery-1.2.1/tests/py_info/test_py_info.py` -> **29** Orphaned Functions | **0** Duplicates
- `python_discovery-1.2.1/tests/test_discovery_extra.py` -> **28** Orphaned Functions | **0** Duplicates
- `python_discovery-1.2.1/tests/test_discovery.py` -> **24** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `199` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `python_discovery-1.2.1/src/python_discovery/_windows/_pep514.py` (PYTHON) -> Cumulative Risk: **659.72**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 195.72 | **LOC:** 223 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9997%), Safety Score (92.3293%)
- **Heaviest Functions:** `parse_version` (Impact: 19.0), `load_exe` (Impact: 18.8), `load_threaded` (Impact: 13.9)

### 2. `python_discovery-1.2.1/src/python_discovery/_windows/_propose.py` (PYTHON) -> Cumulative Risk: **533.02**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 44.86 | **LOC:** 54 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9994%), Safety Score (86.6293%)
- **Heaviest Functions:** `propose_interpreters` (Impact: 23.1)

### 3. `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py` (PYTHON) -> Cumulative Risk: **525.79**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 269.88 | **LOC:** 265 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (93.75%), Safety Score (92.0429%)
- **Heaviest Functions:** `_get_via_file_cache` (Impact: 41.8), `_run_subprocess` (Impact: 30.8), `from_exe` (Impact: 14.1)

### 4. `python_discovery-1.2.1/src/python_discovery/_py_info.py` (PYTHON) -> Cumulative Risk: **501.63**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 922.5 | **LOC:** 814 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.675%), Documentation (51.0417%)
- **Heaviest Functions:** `satisfies` (Impact: 33.1), `discover_exe` (Impact: 31.3), `_check_exe` (Impact: 29.8)

### 5. `python_discovery-1.2.1/src/python_discovery/_specifier.py` (PYTHON) -> Cumulative Risk: **499.1**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 267.42 | **LOC:** 312 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (90.009%), Documentation (71.4286%)
- **Heaviest Functions:** `from_string` (Impact: 32.3), `__lt__` (Impact: 18.0), `from_string` (Impact: 13.6)

### 6. `python_discovery-1.2.1/src/python_discovery/_discovery.py` (PYTHON) -> Cumulative Risk: **494.88**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 379.34 | **LOC:** 336 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.4125%), Documentation (72.0%)
- **Heaviest Functions:** `_find_interpreter` (Impact: 25.7), `_read_python_version_file` (Impact: 19.8), `propose_interpreters` (Impact: 19.2)

### 7. `python_discovery-1.2.1/src/python_discovery/_cache.py` (PYTHON) -> Cumulative Risk: **473.79**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 96.38 | **LOC:** 186 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (95.7082%), Api Exposure (75.8736%), Safety Score (71.5232%)
- **Heaviest Functions:** `py_info_clear` (Impact: 6.1), `read` (Impact: 5.0), `write` (Impact: 2.1)

### 8. `python_discovery-1.2.1/src/python_discovery/_compat.py` (PYTHON) -> Cumulative Risk: **462.6**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 16.88 | **LOC:** 30 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (83.2018%), Safety Score (69.8465%)
- **Heaviest Functions:** `fs_path_id` (Impact: 4.3), `fs_is_case_sensitive` (Impact: 3.2)

### 9. `python_discovery-1.2.1/tests/py_info/test_py_info_exe_based_of.py` (PYTHON) -> Cumulative Risk: **377.7**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 76.74 | **LOC:** 83 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (92.2924%), Stability (50.0%)
- **Heaviest Functions:** `test_discover_ok` (Impact: 19.9), `_discover_base_folders` (Impact: 3.5), `test_discover_empty_folder` (Impact: 1.9)

### 10. `python_discovery-1.2.1/tests/test_discovery.py` (PYTHON) -> Cumulative Risk: **370.46**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 403.48 | **LOC:** 447 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (66.2353%), Stability (50.0%)
- **Heaviest Functions:** `test_discovery_via_path` (Impact: 52.3), `test_shim_resolved_to_real_binary` (Impact: 21.2), `test_discovery_absolute_path_with_try_first` (Impact: 9.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `python_discovery-1.2.1/src/python_discovery/_py_info.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 922.5 | **LOC:** 814 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.4675%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `satisfies` (Impact: 33.1)
    * *Intent:* """ Check if a given specification can be satisfied by this python interpreter instance. :param spec...
  * `discover_exe` (Impact: 31.3)
  * `_check_exe` (Impact: 29.8)
  * `_init_sysconfig` (Impact: 22.8)
  * `_satisfies_version_specifier` (Impact: 20.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Rce:* 3 instances
* *Amplified Cascading Flux:* 142 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 3
* *State Mutation (weighted view):* 461
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 163`, `args: 47`, `func_start: 47`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 3`, `state_mutation: 177`, `dead_code: 3`
* *Architecture:* `io: 49`, `api: 31`, `import: 23`
* *Defense:* `safety: 17`, `doc: 30`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 133.486
  * `Choke Point (Betweenness):` 0.0325 | `Ripple Effect (Closeness):` 0.36
  * `Imports (Out-Degree: 3):` ._cache, ._cached_py_info, ._compat, ._py_spec, Distribution, __future__, collections, collections.abc...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/tests/test_discovery.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 403.48 | **LOC:** 447 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.2008%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_discovery_via_path` (Impact: 52.3)
  * `test_shim_resolved_to_real_binary` (Impact: 21.2)
  * `test_discovery_absolute_path_with_try_first` (Impact: 9.8)
  * `test_uv_python` (Impact: 8.9)
  * `_create_versioned_binary` (Impact: 7.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 195
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 122`, `args: 32`, `func_start: 28`
* *Risk/State:* `state_mutation: 95`, `unreferenced_by_name: 24`
* *Architecture:* `io: 18`, `api: 26`, `import: 14`
* *Defense:* `safety: 44`, `test: 69`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 19.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, logging, os, pathlib, pytest, pytest_mock, python_discovery, python_discovery._discovery...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/test_py_info_extra.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 400.32 | **LOC:** 517 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.1637%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_possible_base_case_sensitive` (Impact: 7.6)
  * `test_check_exe_mismatch_not_exact` (Impact: 5.7)
  * `test_check_exe_mismatch_exact` (Impact: 5.7)
  * `test_resolve_to_system_circle` (Impact: 4.5)
  * `test_resolve_to_system_single_prefix_self_link` (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 216
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 157`, `args: 60`, `func_start: 59`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 166`, `unreferenced_by_name: 59`
* *Architecture:* `io: 12`, `api: 59`, `import: 13`
* *Defense:* `safety: 86`, `test: 106`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 19.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, copy, logging, os, pathlib, pytest, pytest_mock, python_discovery...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/src/python_discovery/_discovery.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 379.34 | **LOC:** 336 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.5351%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_find_interpreter` (Impact: 25.7)
  * `_read_python_version_file` (Impact: 19.8)
    * *Intent:* """Read a ``.python-version`` file, optionally searching parent directories."""
  * `propose_interpreters` (Impact: 19.2)
  * `get_interpreter` (Impact: 16.0)
  * `_propose_explicit` (Impact: 15.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 86`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 53`
* *Architecture:* `io: 21`, `api: 10`, `import: 14`
* *Defense:* `safety: 6`, `doc: 9`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 63.632
  * `Choke Point (Betweenness):` 0.015 | `Ripple Effect (Closeness):` 0.16
  * `Imports (Out-Degree: 3):` ._cache, ._compat, ._py_info, ._py_spec, ._windows, __future__, collections.abc, contextlib...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/tests/py_info/test_py_info.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 313.4 | **LOC:** 455 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.5607%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_system_executable_no_exact_match` (Impact: 19.9)
  * `test_bad_exe_py_info_no_raise` (Impact: 7.7)
  * `test_select_most_likely_prefers_machine_match` (Impact: 6.6)
  * `_generate_not_match_current_interpreter_version` (Impact: 6.5)
  * `test_py_info_cache_clear` (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 169
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 128`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 83`, `unreferenced_by_name: 29`
* *Architecture:* `io: 12`, `api: 31`, `import: 17`
* *Defense:* `safety: 64`, `doc: 1`, `test: 69`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 19.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, copy, itertools, json, logging, os, pathlib, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 269.88 | **LOC:** 265 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.3834%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_get_via_file_cache` (Impact: 41.8)
  * `_run_subprocess` (Impact: 30.8)
  * `from_exe` (Impact: 14.1)
  * `_get_from_cache` (Impact: 13.1)
  * `_extract_between_cookies` (Impact: 10.7)
    * *Intent:* """Extract payload between reversed cookie markers, forwarding any surrounding output to stdout."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 68`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 55`
* *Architecture:* `io: 6`, `api: 7`, `import: 20`
* *Defense:* `safety: 15`, `doc: 2`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 83.117
  * `Choke Point (Betweenness):` 0.005833 | `Ripple Effect (Closeness):` 0.24
  * `Imports (Out-Degree: 2):` ._cache, ._py_info, __future__, collections, collections.abc, contextlib, hashlib, json...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/src/python_discovery/_specifier.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 267.42 | **LOC:** 312 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.8425%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `from_string` (Impact: 32.3)
    * *Intent:* """ Parse a PEP 440 version string (e.g. ``3.12.1``). :param version_str: the version string to pars...
  * `__lt__` (Impact: 18.0)
  * `from_string` (Impact: 13.6)
    * *Intent:* """ Parse a single PEP 440 specifier (e.g. ``>=3.10``). :param spec_str: the specifier string to par...
  * `_check_standard` (Impact: 9.6)
  * `contains` (Impact: 9.4)
    * *Intent:* """ Check if a version string satisfies this specifier. :param version_str: the version string to te...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 90`, `args: 25`, `func_start: 25`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 34`
* *Architecture:* `io: 1`, `api: 14`, `import: 8`
* *Defense:* `safety: 10`, `doc: 11`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 57.99
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.12
  * `Imports (Out-Degree: 0):` __future__, collections.abc, contextlib, dataclasses, operator, re, sys, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/tests/windows/conftest.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 207.96 | **LOC:** 176 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.3616%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_mock_pyinfo` (Impact: 35.6)
  * `satisfies` (Impact: 17.8)
  * `_make_open_key_ex` (Impact: 16.4)
  * `_open_key_ex` (Impact: 13.4)
  * `_mock_registry` (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 59`, `args: 16`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 34`, `unreferenced_by_name: 5`
* *Architecture:* `io: 5`, `api: 1`, `import: 14`
* *Defense:* `safety: 8`, `doc: 2`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 19.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` __future__, collections.abc, contextlib, os, pathlib, pytest, python_discovery._cached_py_info, python_discovery._py_info...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/src/python_discovery/_windows/_pep514.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 195.72 | **LOC:** 223 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.7881%), Tech Debt (12.8397%)
**Top Internal Functions/Classes:**
  * `parse_version` (Impact: 19.0)
  * `load_exe` (Impact: 18.8)
  * `load_threaded` (Impact: 13.9)
  * `process_tag` (Impact: 10.5)
  * `parse_arch` (Impact: 10.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 59`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 23`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 13`, `import: 9`
* *Defense:* `safety: 15`, `doc: 4`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 53.336
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.12
  * `Imports (Out-Degree: 0):` __future__, collections.abc, logging, os, re, sys, typing, winreg
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/tests/test_discovery_extra.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 182.88 | **LOC:** 242 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.7114%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_propose_interpreters_relative_path` (Impact: 6.7)
  * `test_propose_interpreters_try_first_with_duplicate` (Impact: 6.1)
  * `test_propose_interpreters_relative_spec_is_abs` (Impact: 5.5)
  * `test_propose_interpreters_try_first_with_missing` (Impact: 3.3)
  * `test_active_versions_global_version_file` (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 81`, `args: 28`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 61`, `unreferenced_by_name: 28`
* *Architecture:* `io: 12`, `api: 28`, `import: 12`
* *Defense:* `safety: 31`, `test: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 19.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, os, pathlib, pytest, pytest_mock, python_discovery, python_discovery._discovery, python_discovery._py_spec...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/test_cached_py_info.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 124.48 | **LOC:** 241 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.0986%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_from_exe_retry_on_first_failure` (Impact: 4.7)
  * `test_resolve_py_info_script_pkgutil_returns_none` (Impact: 3.1)
  * `test_run_subprocess_with_cookies` (Impact: 2.3)
  * `test_get_via_file_cache_stale_hash` (Impact: 2.2)
  * `test_get_via_file_cache_py_info_none` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 94`, `args: 22`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 58`, `unreferenced_by_name: 22`
* *Architecture:* `io: 17`, `api: 22`, `import: 13`
* *Defense:* `safety: 54`, `test: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 19.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, json, logging, os, pathlib, pytest, pytest_mock, python_discovery...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/test_specifier.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 115.72 | **LOC:** 300 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.0593%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_version_parse` (Impact: 2.7)
  * `test_version_invalid_raises` (Impact: 2.1)
  * `test_version_lt` (Impact: 2.1)
  * `test_specifier_invalid_raises` (Impact: 2.1)
    * *Intent:* # --- SimpleSpecifier ---
  * `test_specifier_contains` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 92`, `args: 39`, `func_start: 39`
* *Risk/State:* `state_mutation: 21`, `unreferenced_by_name: 39`
* *Architecture:* `api: 39`, `import: 3`
* *Defense:* `safety: 45`, `test: 92`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 19.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, pytest, python_discovery._specifier
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/src/python_discovery/_cache.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 96.38 | **LOC:** 186 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.8114%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `py_info_clear` (Impact: 6.1)
    * *Intent:* """Remove all cached interpreter information."""
  * `read` (Impact: 5.0)
  * `write` (Impact: 2.1)
    * *Intent:* """ Persist *content* to the store. :param content: interpreter metadata to cache. """
  * `py_info` (Impact: 2.1)
    * *Intent:* """ Return the content store for the interpreter at *path*. :param path: absolute path to a Python e...
  * `__init__` (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 64`, `args: 25`, `func_start: 25`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 10`
* *Architecture:* `io: 1`, `api: 28`, `import: 9`
* *Defense:* `safety: 3`, `doc: 16`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 140.278
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.356364
  * `Imports (Out-Degree: 0):` __future__, collections.abc, contextlib, filelock, hashlib, json, logging, pathlib...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/tests/py_info/test_py_info_exe_based_of.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 76.74 | **LOC:** 83 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.9261%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_discover_ok` (Impact: 19.9)
  * `_discover_base_folders` (Impact: 3.5)
  * `test_discover_empty_folder` (Impact: 1.9)
  * `_fs_supports_symlink` (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 25`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 17`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 2`, `import: 8`
* *Defense:* `safety: 3`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 19.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, logging, pathlib, pytest, python_discovery, python_discovery._compat, python_discovery._discovery, python_discovery._py_info
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/test_py_spec_extra.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 74.08 | **LOC:** 131 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.5352%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_specifier_with_invalid_inner` (Impact: 3.1)
  * `test_get_required_precision_none` (Impact: 1.6)
  * `test_get_required_precision_attribute_error` (Impact: 1.6)
  * `test_specifier_parse_failure_fallback` (Impact: 1.2)
  * `test_version_specifier_satisfies_micro` (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 53`, `args: 18`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 28`, `unreferenced_by_name: 18`
* *Architecture:* `api: 18`, `import: 6`
* *Defense:* `safety: 23`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 19.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, python_discovery, python_discovery._specifier, unittest.mock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/test_cache.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 70.34 | **LOC:** 116 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.22%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_disk_cache_py_info_clear_skips_non_json` (Impact: 3.3)
  * `test_disk_cache_py_info_clear` (Impact: 1.8)
  * `test_disk_content_store_read_valid_json` (Impact: 1.7)
  * `test_disk_content_store_read_invalid_json` (Impact: 1.7)
  * `test_disk_content_store_remove` (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 44`, `args: 18`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 21`, `unreferenced_by_name: 18`
* *Architecture:* `io: 1`, `api: 18`, `import: 3`
* *Defense:* `safety: 19`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 19.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, pathlib, python_discovery._cache
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/src/python_discovery/_windows/_propose.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 44.86 | **LOC:** 54 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.5083%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `propose_interpreters` (Impact: 23.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 16`, `args: 2`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 3`, `import: 7`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.373
  * `Choke Point (Betweenness):` 0.006667 | `Ripple Effect (Closeness):` 0.04
  * `Imports (Out-Degree: 3):` ._pep514, __future__, collections.abc, python_discovery._cache, python_discovery._py_info, python_discovery._py_spec, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/tests/windows/test_windows_pep514.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 31.48 | **LOC:** 157 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0285%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_pep514_parse_functions` (Impact: 5.8)
  * `test_pep514` (Impact: 3.5)
  * `test_pep514_discovers_interpreters` (Impact: 2.5)
  * `test_pep514_run` (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 36`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 7`, `unreferenced_by_name: 4`
* *Architecture:* `io: 2`, `api: 4`, `import: 8`
* *Defense:* `safety: 13`, `doc: 1`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 19.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, pytest, python_discovery._windows, python_discovery._windows._pep514, sys, textwrap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/windows/winreg_mock_values.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 22.38 | **LOC:** 171 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/src/python_discovery/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 18.42 | **LOC:** 28 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 14`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 19.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ._cache, ._discovery, ._py_info, ._py_spec, ._specifier, __future__, importlib.metadata
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/src/python_discovery/_compat.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 16.88 | **LOC:** 30 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.1497%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fs_path_id` (Impact: 4.3)
  * `fs_is_case_sensitive` (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 14`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 2`, `api: 3`, `import: 6`
* *Defense:* `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 81.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.2704
  * `Imports (Out-Degree: 0):` __future__, functools, logging, pathlib, tempfile, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/src/python_discovery/_windows/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 16.68 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 19.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ._pep514, ._propose, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/conftest.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 15.0 | **LOC:** 31 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.0926%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_skip_if_test_in_system` (Impact: 4.5)
  * `_ensure_py_info_cache_empty` (Impact: 1.6)
  * `session_cache` (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 13`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, collections.abc, pytest, python_discovery, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/windows/test_windows.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5.58 | **LOC:** 36 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_propose_interpreters` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 5`
* *Defense:* `safety: 1`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, pytest, python_discovery, python_discovery._windows, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/CODE_OF_CONDUCT.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.22 | **LOC:** 61 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 19.91
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `python_discovery-1.2.1/src/python_discovery/_py_info.py` -> **Severity: 3.25** (Bridge: 0.0325 * Flux: 100.0%)
- `python_discovery-1.2.1/src/python_discovery/_discovery.py` -> **Severity: 1.5** (Bridge: 0.015 * Flux: 100.0%)
- `python_discovery-1.2.1/src/python_discovery/_windows/_propose.py` -> **Severity: 0.667** (Bridge: 0.0067 * Flux: 99.9994%)
- `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py` -> **Severity: 0.583** (Bridge: 0.0058 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `python_discovery-1.2.1/src/python_discovery/_py_info.py` -> **Severity: 35.523** (Embedded: 0.36 * Error Risk: 98.675%)
- `python_discovery-1.2.1/src/python_discovery/_cache.py` -> **Severity: 25.488** (Embedded: 0.3564 * Error Risk: 71.5232%)
- `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py` -> **Severity: 22.09** (Embedded: 0.24 * Error Risk: 92.0429%)
- `python_discovery-1.2.1/src/python_discovery/_compat.py` -> **Severity: 18.886** (Embedded: 0.2704 * Error Risk: 69.8465%)
- `python_discovery-1.2.1/src/python_discovery/_discovery.py` -> **Severity: 15.426** (Embedded: 0.16 * Error Risk: 96.4125%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `python_discovery-1.2.1/src/python_discovery/_cache.py` -> **Severity: 8538.666** (Blast Radius: 140.278 * Doc Risk: 60.8696%)
- `python_discovery-1.2.1/src/python_discovery/_compat.py` -> **Severity: 8140.0** (Blast Radius: 81.4 * Doc Risk: 100.0%)
- `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py` -> **Severity: 7792.219** (Blast Radius: 83.117 * Doc Risk: 93.75%)
- `python_discovery-1.2.1/src/python_discovery/_py_info.py` -> **Severity: 6813.352** (Blast Radius: 133.486 * Doc Risk: 51.0417%)
- `python_discovery-1.2.1/src/python_discovery/_windows/_pep514.py` -> **Severity: 5333.6** (Blast Radius: 53.336 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
