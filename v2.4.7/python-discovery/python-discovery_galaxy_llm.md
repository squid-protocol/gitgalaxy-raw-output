# ARCHITECTURAL_BRIEF: python-discovery
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/python-discovery` |
| **Timestamp** | `2026-08-07T05:25:40.662093+00:00` |
| **Scan Duration** | `0.19s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 22 malicious artifacts.

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
| Total Artifacts | 37 |
| Analyzed Artifacts (Scanned) | 24 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 13 |
| Total LOC | 3893 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 64.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4024 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.1298 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 8.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7316 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 8 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 22 | 3893 | 91.7% |
| MARKDOWN | 2 | 0 | 8.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.059`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 12 | 50.0% |
| file_cluster_8 | 6 | 25.0% |
| file_cluster_16 | 4 | 16.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 8.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 13*

**Composition by Extension & Reason:**
- `.py`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 41.2 | 10.7 | 5.0 | 3.4 |
| Error & Exception Exposure | 0.0 | 68.0 | 20.3 | 3.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 9.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.0 | 0.0 | 0.0 |
| API Exposure | 0.0 | 11.1 | 4.0 | 3.2 | 0.4 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 99.8 | 20.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 9.9 | 0.9 | 0.0 | 0.0 |
| Specification Exposure | 60.0 | 100.0 | 98.2 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 98.2 | 21.2 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `python_discovery-1.2.1/src/python_discovery/_py_info.py` (Hits: 57)
- `python_discovery-1.2.1/tests/test_cached_py_info.py` (Hits: 30)
- `python_discovery-1.2.1/src/python_discovery/_discovery.py` (Hits: 23)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **_py_info.py** (`python_discovery-1.2.1/src/python_discovery/_py_info.py`) — 7 inbound connections
2. **_cache.py** (`python_discovery-1.2.1/src/python_discovery/_cache.py`) — 6 inbound connections
3. **_discovery.py** (`python_discovery-1.2.1/src/python_discovery/_discovery.py`) — 4 inbound connections
4. **_compat.py** (`python_discovery-1.2.1/src/python_discovery/_compat.py`) — 3 inbound connections
5. **_specifier.py** (`python_discovery-1.2.1/src/python_discovery/_specifier.py`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **_py_info.py** (`python_discovery-1.2.1/src/python_discovery/_py_info.py`) — 23 outbound dependencies
2. **_cached_py_info.py** (`python_discovery-1.2.1/src/python_discovery/_cached_py_info.py`) — 18 outbound dependencies
3. **test_py_info.py** (`python_discovery-1.2.1/tests/py_info/test_py_info.py`) — 16 outbound dependencies
4. **_discovery.py** (`python_discovery-1.2.1/src/python_discovery/_discovery.py`) — 14 outbound dependencies
5. **test_discovery.py** (`python_discovery-1.2.1/tests/test_discovery.py`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__repr__` (@ `python_discovery-1.2.1/src/python_discovery/_discovery.py`) -> Impact: **70.9** | LOC: 101
- `satisfies` (@ `python_discovery-1.2.1/src/python_discovery/_py_info.py`) -> Impact: **36.7** | LOC: 19
- `from_string` (@ `python_discovery-1.2.1/src/python_discovery/_specifier.py`) -> Impact: **32.1** | LOC: 19
- `_init_sysconfig` (@ `python_discovery-1.2.1/src/python_discovery/_py_info.py`) -> Impact: **27.5** | LOC: 31
- `parse_version` (@ `python_discovery-1.2.1/src/python_discovery/_windows/_pep514.py`) -> Impact: **26.6** | LOC: 13
- `load_exe` (@ `python_discovery-1.2.1/src/python_discovery/_windows/_pep514.py`) -> Impact: **25.5** | LOC: 19
- `_satisfies_version_specifier` (@ `python_discovery-1.2.1/src/python_discovery/_py_info.py`) -> Impact: **20.2** | LOC: 22
- `__lt__` (@ `python_discovery-1.2.1/src/python_discovery/_specifier.py`) -> Impact: **18.0** | LOC: 14
- `test_pep514_parse_functions` (@ `python_discovery-1.2.1/tests/windows/test_windows_pep514.py`) -> Impact: **16.4** | LOC: 17
- `_fast_get_system_executable` (@ `python_discovery-1.2.1/src/python_discovery/_py_info.py`) -> Impact: **15.2** | LOC: 26
  * *Intent:* # note we must choose the original and not the pure executable as shim scripts might throw us off if not (self.real_prefix or (self.base_prefix is not...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `python_discovery-1.2.1/src/python_discovery` | 7 | 1120.52 | 23.34% | 28.57% |
| `python_discovery-1.2.1/tests` | 7 | 791.7 | 4.04% | 0.0% |
| `python_discovery-1.2.1/src/python_discovery/_windows` | 3 | 167.66 | 8.77% | 4.28% |
| `python_discovery-1.2.1/tests/py_info` | 2 | 115.94 | 5.74% | 0.0% |
| `python_discovery-1.2.1/tests/windows` | 3 | 56.14 | 2.2% | 0.0% |
| `python_discovery-1.2.1` | 2 | 2.22 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `python_discovery-1.2.1/src/python_discovery/_cache.py` -> **100.0%** Exposure
- `python_discovery-1.2.1/src/python_discovery/_specifier.py` -> **100.0%** Exposure
- `python_discovery-1.2.1/src/python_discovery/_windows/_pep514.py` -> **12.8397%** Exposure
### Highest State Flux (Mutation/Volatility)
- `python_discovery-1.2.1/src/python_discovery/_py_info.py` -> **99.8253%** Exposure
- `python_discovery-1.2.1/src/python_discovery/_discovery.py` -> **99.0289%** Exposure
- `python_discovery-1.2.1/src/python_discovery/_specifier.py` -> **98.69%** Exposure
- `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py` -> **94.6487%** Exposure
- `python_discovery-1.2.1/src/python_discovery/_cache.py` -> **39.0517%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `python_discovery-1.2.1/tests/test_py_info_extra.py` -> **59** Orphaned Functions | **0** Duplicates
- `python_discovery-1.2.1/tests/test_specifier.py` -> **39** Orphaned Functions | **0** Duplicates
- `python_discovery-1.2.1/tests/test_discovery.py` -> **24** Orphaned Functions | **0** Duplicates
- `python_discovery-1.2.1/src/python_discovery/_cache.py` -> **0** Orphaned Functions | **22** Duplicates
- `python_discovery-1.2.1/tests/test_cached_py_info.py` -> **22** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`python_discovery-1.2.1/src/python_discovery/_cached_py_info.py`** -> AI Confidence: **99.31%**
2. **`python_discovery-1.2.1/src/python_discovery/_discovery.py`** -> AI Confidence: **99.31%**
3. **`python_discovery-1.2.1/src/python_discovery/_py_info.py`** -> AI Confidence: **99.31%**
4. **`python_discovery-1.2.1/src/python_discovery/_windows/_pep514.py`** -> AI Confidence: **99.31%**
5. **`python_discovery-1.2.1/src/python_discovery/_windows/_propose.py`** -> AI Confidence: **99.24%**
6. **`python_discovery-1.2.1/src/python_discovery/_specifier.py`** -> AI Confidence: **99.23%**
7. **`python_discovery-1.2.1/tests/py_info/test_py_info.py`** -> AI Confidence: **99.18%**
8. **`python_discovery-1.2.1/tests/test_discovery.py`** -> AI Confidence: **99.16%**
9. **`python_discovery-1.2.1/tests/py_info/test_py_info_exe_based_of.py`** -> AI Confidence: **99.15%**
10. **`python_discovery-1.2.1/tests/test_cached_py_info.py`** -> AI Confidence: **99.09%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `180` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `python_discovery-1.2.1/src/python_discovery/_cache.py` (PYTHON) -> Cumulative Risk: **459.38**
- **Archetype:** `file_cluster_16` (Distance: 10.978 IQR)
- **Magnitude:** 99.58 | **LOC:** 186 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (98.2213%), Safety Score (53.5174%)
- **Heaviest Functions:** `read` (Impact: 9.4), `py_info_clear` (Impact: 9.1), `write` (Impact: 3.9)

### 2. `python_discovery-1.2.1/src/python_discovery/_specifier.py` (PYTHON) -> Cumulative Risk: **443.5**
- **Archetype:** `file_cluster_13` (Distance: 12.257 IQR)
- **Magnitude:** 212.92 | **LOC:** 312 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (98.69%), Safety Score (50.8694%)
- **Heaviest Functions:** `from_string` (Impact: 32.1), `__lt__` (Impact: 18.0), `from_string` (Impact: 15.2)

### 3. `python_discovery-1.2.1/src/python_discovery/_windows/_pep514.py` (PYTHON) -> Cumulative Risk: **414.65**
- **Archetype:** `file_cluster_13` (Distance: 10.446 IQR)
- **Magnitude:** 147.02 | **LOC:** 223 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Safety Score (68.0117%), Documentation (58.7982%)
- **Heaviest Functions:** `parse_version` (Impact: 26.6), `load_exe` (Impact: 25.5), `parse_arch` (Impact: 14.4)

### 4. `python_discovery-1.2.1/src/python_discovery/_py_info.py` (PYTHON) -> Cumulative Risk: **392.06**
- **Archetype:** `file_cluster_13` (Distance: 12.878 IQR)
- **Magnitude:** 560.0 | **LOC:** 814 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8253%), Safety Score (61.8745%), Stability (50.0%)
- **Heaviest Functions:** `satisfies` (Impact: 36.7), `_init_sysconfig` (Impact: 27.5), `_satisfies_version_specifier` (Impact: 20.2)

### 5. `python_discovery-1.2.1/src/python_discovery/_discovery.py` (PYTHON) -> Cumulative Risk: **379.88**
- **Archetype:** `file_cluster_13` (Distance: 11.341 IQR)
- **Magnitude:** 148.94 | **LOC:** 336 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.0289%), Safety Score (63.2377%), Stability (50.0%)
- **Heaviest Functions:** `__repr__` (Impact: 70.9), `get_paths` (Impact: 11.9), `__init__` (Impact: 2.4)

### 6. `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py` (PYTHON) -> Cumulative Risk: **360.18**
- **Archetype:** `file_cluster_13` (Distance: 10.898 IQR)
- **Magnitude:** 71.68 | **LOC:** 265 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (94.6487%), Safety Score (50.3735%), Stability (50.0%)
- **Heaviest Functions:** `_resolve_py_info_script` (Impact: 14.7), `_extract_between_cookies` (Impact: 10.8), `gen_cookie` (Impact: 1.8)

### 7. `python_discovery-1.2.1/src/python_discovery/_compat.py` (PYTHON) -> Cumulative Risk: **244.83**
- **Archetype:** `file_cluster_13` (Distance: 8.06 IQR)
- **Magnitude:** 10.98 | **LOC:** 30 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (83.1282%), Stability (50.0%), Cognitive Load (6.242%)
- **Heaviest Functions:** `fs_is_case_sensitive` (Impact: 7.6)

### 8. `python_discovery-1.2.1/src/python_discovery/_windows/_propose.py` (PYTHON) -> Cumulative Risk: **223.52**
- **Archetype:** `file_cluster_13` (Distance: 7.662 IQR)
- **Magnitude:** 4.96 | **LOC:** 54 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (60.2802%), Stability (50.0%), Cognitive Load (9.0418%)
- **Heaviest Functions:** `propose_interpreters` (Impact: 1.2)

### 9. `python_discovery-1.2.1/tests/windows/test_windows.py` (PYTHON) -> Cumulative Risk: **196.97**
- **Archetype:** `file_cluster_13` (Distance: 7.938 IQR)
- **Magnitude:** 3.58 | **LOC:** 36 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Safety Score (42.7055%), Cognitive Load (3.5016%)
- **Heaviest Functions:** `test_propose_interpreters` (Impact: 2.0)

### 10. `python_discovery-1.2.1/src/python_discovery/__init__.py` (PYTHON) -> Cumulative Risk: **193.11**
- **Archetype:** `file_cluster_8` (Distance: 7.095 IQR)
- **Magnitude:** 16.42 | **LOC:** 28 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Documentation (37.009%), Cognitive Load (3.3961%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `python_discovery-1.2.1/src/python_discovery/_py_info.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.878 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.665 IQR)
- **Top Global Matches:** file_cluster_13: 12.878, file_cluster_0: 12.928, file_cluster_11: 12.965
- **Magnitude:** 560.0 | **LOC:** 814 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.3265%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `satisfies` (Impact: 36.7)
  * `_init_sysconfig` (Impact: 27.5)
  * `_satisfies_version_specifier` (Impact: 20.2)
  * `_fast_get_system_executable` (Impact: 15.2)
    * *Intent:* # note we must choose the original and not the pure executable as shim scripts might throw us off if...
  * `__str__` (Impact: 15.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 161`, `args: 47`, `func_start: 47`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 134`, `dead_code: 3`
* *Architecture:* `io: 57`, `api: 40`, `import: 23`
* *Defense:* `safety: 33`, `doc: 83`, `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 130.036
  * `Choke Point (Betweenness):` 0.035573 | `Ripple Effect (Closeness):` 0.350725
  * `Imports (Out-Degree: 3):` ._compat, platform, venv, collections.abc, ._cache, typing, json, os...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/tests/test_py_info_extra.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.185 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.348 IQR)
- **Top Global Matches:** file_cluster_8: 12.185, file_cluster_16: 12.191, file_cluster_13: 12.387
- **Magnitude:** 237.02 | **LOC:** 517 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.5437%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_possible_base_case_sensitive` (Impact: 10.5)
  * `test_current_returns_none_raises` (Impact: 6.3)
  * `test_current_system_returns_none_raises` (Impact: 6.3)
  * `test_resolve_to_system_circle` (Impact: 6.2)
  * `test_check_exe_mismatch_not_exact` (Impact: 5.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 154`, `args: 60`, `func_start: 59`
* *Risk/State:* `safety_bypasses: 2`, `orphaned_logic: 59`
* *Architecture:* `io: 17`, `api: 59`, `import: 13`
* *Defense:* `safety: 86`, `test: 179`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sys, typing, os, python_discovery, pytest, pytest_mock, __future__, unittest.mock...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/src/python_discovery/_specifier.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.257 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.644 IQR)
- **Top Global Matches:** file_cluster_13: 12.257, file_cluster_16: 12.263, file_cluster_0: 12.461
- **Magnitude:** 212.92 | **LOC:** 312 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.8786%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `from_string` (Impact: 32.1)
  * `__lt__` (Impact: 18.0)
  * `from_string` (Impact: 15.2)
  * `contains` (Impact: 11.0)
  * `_check_standard` (Impact: 9.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 89`, `args: 25`, `func_start: 25`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 36`, `duplicate_logic: 17`
* *Architecture:* `io: 1`, `api: 14`, `import: 8`
* *Defense:* `safety: 14`, `doc: 42`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 62.957
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.130435
  * `Imports (Out-Degree: 0):` dataclasses, sys, contextlib, typing, operator, __future__, re, collections.abc
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/src/python_discovery/_discovery.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.341 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.62 IQR)
- **Top Global Matches:** file_cluster_13: 11.341, file_cluster_16: 11.359, file_cluster_7: 11.794
- **Magnitude:** 148.94 | **LOC:** 336 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.2745%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 70.9)
  * `get_paths` (Impact: 11.9)
  * `__init__` (Impact: 2.4)
  * `get_interpreter` (Impact: 1.3)
  * `_find_interpreter` (Impact: 1.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 83`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 45`
* *Architecture:* `io: 23`, `api: 10`, `import: 14`
* *Defense:* `safety: 7`, `doc: 28`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 69.081
  * `Choke Point (Betweenness):` 0.017787 | `Ripple Effect (Closeness):` 0.173913
  * `Imports (Out-Degree: 3):` ._py_info, ._cache, ._compat, contextlib, sys, typing, os, ._windows...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/src/python_discovery/_windows/_pep514.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.446 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.643 IQR)
- **Top Global Matches:** file_cluster_13: 10.446, file_cluster_16: 10.695, file_cluster_11: 10.894
- **Magnitude:** 147.02 | **LOC:** 223 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.277%), Tech Debt (12.8397%)
**Top Internal Functions/Classes:**
  * `parse_version` (Impact: 26.6)
  * `load_exe` (Impact: 25.5)
  * `parse_arch` (Impact: 14.4)
  * `load_threaded` (Impact: 13.9)
  * `process_tag` (Impact: 13.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 54`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 6`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 13`, `import: 9`
* *Defense:* `safety: 15`, `doc: 8`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 57.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.130435
  * `Imports (Out-Degree: 0):` winreg, sys, typing, os, collections.abc, __future__, re, logging
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/tests/test_discovery.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.224 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.996 IQR)
- **Top Global Matches:** file_cluster_8: 11.224, file_cluster_13: 11.386, file_cluster_0: 11.408
- **Magnitude:** 135.68 | **LOC:** 447 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.5294%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_shim_pyenv_version_env_takes_priori` (Impact: 7.8)
  * `test_shim_uses_global_version_file` (Impact: 7.8)
  * `test_shim_not_resolved_without_version_m` (Impact: 7.7)
  * `test_shim_uses_python_version_file` (Impact: 7.7)
  * `test_shim_falls_through_when_binary_miss` (Impact: 7.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 112`, `args: 32`, `func_start: 28`
* *Risk/State:* `state_mutation: 3`, `orphaned_logic: 24`
* *Architecture:* `io: 20`, `api: 26`, `import: 14`
* *Defense:* `safety: 45`, `test: 113`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stat, sys, python_discovery._discovery, typing, os, python_discovery, pytest, pytest_mock...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/test_specifier.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.911 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.958 IQR)
- **Top Global Matches:** file_cluster_16: 11.911, file_cluster_8: 11.918, file_cluster_0: 12.19
- **Magnitude:** 123.92 | **LOC:** 300 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.005%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_version_invalid_raises` (Impact: 5.3)
  * `test_specifier_invalid_raises` (Impact: 5.3)
    * *Intent:* # --- SimpleSpecifier ---
  * `test_specifier_contains_version_none` (Impact: 2.2)
  * `test_specifier_wildcard_version_none` (Impact: 2.2)
  * `test_specifier_compatible_release_versio` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 90`, `args: 39`, `func_start: 39`
* *Risk/State:* `orphaned_logic: 39`
* *Architecture:* `api: 39`, `import: 3`
* *Defense:* `safety: 45`, `test: 137`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, pytest, python_discovery._specifier
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/src/python_discovery/_cache.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.978 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.636 IQR)
- **Top Global Matches:** file_cluster_16: 10.978, file_cluster_13: 10.988, file_cluster_0: 11.259
- **Magnitude:** 99.58 | **LOC:** 186 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.0398%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `read` (Impact: 9.4)
  * `py_info_clear` (Impact: 9.1)
  * `write` (Impact: 3.9)
  * `locked` (Impact: 3.8)
  * `__init__` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 60`, `args: 25`, `func_start: 25`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 6`, `duplicate_logic: 22`
* *Architecture:* `io: 1`, `api: 28`, `import: 9`
* *Defense:* `safety: 3`, `doc: 36`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 142.38
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.367391
  * `Imports (Out-Degree: 0):` contextlib, hashlib, typing, json, filelock, collections.abc, __future__, pathlib...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/tests/py_info/test_py_info.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.587 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.512 IQR)
- **Top Global Matches:** file_cluster_13: 11.587, file_cluster_8: 11.598, file_cluster_0: 11.625
- **Magnitude:** 97.1 | **LOC:** 455 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.0555%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_generate_not_match_current_interpreter_` (Impact: 10.9)
  * `test_py_info_cached_error` (Impact: 6.3)
  * `test_py_info_cache_clear` (Impact: 5.8)
  * `test_satisfy_not_arch` (Impact: 5.5)
  * `test_satisfy_not_threaded` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 125`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 6`, `orphaned_logic: 12`
* *Architecture:* `io: 12`, `api: 31`, `import: 17`
* *Defense:* `safety: 64`, `doc: 2`, `test: 130`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` textwrap, setuptools.dist, itertools, sys, typing, json, os, python_discovery...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/test_discovery_extra.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.673 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.926 IQR)
- **Top Global Matches:** file_cluster_13: 11.673, file_cluster_16: 11.71, file_cluster_8: 11.783
- **Magnitude:** 87.28 | **LOC:** 242 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.0295%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_read_python_version_file_found` (Impact: 10.4)
  * `test_propose_interpreters_try_first_with` (Impact: 8.4)
  * `test_propose_interpreters_try_first_with` (Impact: 4.5)
  * `test_lazy_path_dump_basic` (Impact: 4.2)
  * `test_lazy_path_dump_debug_with_dir` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 80`, `args: 28`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 3`, `duplicate_logic: 3`, `orphaned_logic: 13`
* *Architecture:* `io: 19`, `api: 28`, `import: 12`
* *Defense:* `safety: 31`, `test: 69`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` python_discovery._py_spec, sys, python_discovery._discovery, typing, os, python_discovery, pytest, __future__...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/test_cached_py_info.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.248 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 7.052 IQR)
- **Top Global Matches:** file_cluster_8: 12.248, file_cluster_13: 12.285, file_cluster_16: 12.343
- **Magnitude:** 83.78 | **LOC:** 241 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.0854%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_resolve_py_info_script_pkgutil_retu` (Impact: 6.2)
  * `test_run_subprocess_with_cookies` (Impact: 4.9)
  * `test_resolve_py_info_script_fallback_to_` (Impact: 4.4)
  * `test_resolve_py_info_script_file_exists` (Impact: 3.7)
  * `test_get_via_file_cache_stale_hash` (Impact: 2.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 90`, `args: 22`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 1`, `orphaned_logic: 22`
* *Architecture:* `io: 30`, `api: 22`, `import: 13`
* *Defense:* `safety: 54`, `test: 85`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sys, typing, json, os, python_discovery, pytest, pytest_mock, subprocess...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.898 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.869 IQR)
- **Top Global Matches:** file_cluster_13: 10.898, file_cluster_16: 11.237, file_cluster_8: 11.32
- **Magnitude:** 71.68 | **LOC:** 265 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.2388%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_resolve_py_info_script` (Impact: 14.7)
  * `_extract_between_cookies` (Impact: 10.8)
  * `gen_cookie` (Impact: 1.8)
  * `from_exe` (Impact: 1.4)
  * `_load_cached_py_info` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 65`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 31`
* *Architecture:* `io: 7`, `api: 5`, `import: 20`
* *Defense:* `safety: 16`, `doc: 4`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 76.832
  * `Choke Point (Betweenness):` 0.005929 | `Ripple Effect (Closeness):` 0.228733
  * `Imports (Out-Degree: 2):` ._cache, ._py_info, sys, hashlib, contextlib, shlex, json, os...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/tests/test_cache.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.277 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.998 IQR)
- **Top Global Matches:** file_cluster_16: 12.277, file_cluster_8: 12.443, file_cluster_13: 12.469
- **Magnitude:** 65.64 | **LOC:** 116 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0304%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_disk_cache_py_info_clear_skips_non_` (Impact: 4.5)
  * `test_disk_content_store_locked` (Impact: 4.2)
  * `test_noop_content_store_locked` (Impact: 3.6)
  * `test_disk_cache_py_info_clear` (Impact: 2.4)
  * `test_disk_content_store_read_invalid_jso` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 42`, `args: 18`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `orphaned_logic: 18`
* *Architecture:* `io: 1`, `api: 18`, `import: 3`
* *Defense:* `safety: 19`, `test: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, python_discovery._cache, pathlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/test_py_spec_extra.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.78 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.394 IQR)
- **Top Global Matches:** file_cluster_16: 11.78, file_cluster_8: 11.823, file_cluster_13: 11.957
- **Magnitude:** 58.38 | **LOC:** 131 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.046%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_specifier_with_invalid_inner` (Impact: 5.3)
  * `test_get_required_precision_attribute_er` (Impact: 2.4)
  * `test_get_required_precision_none` (Impact: 2.3)
  * `test_get_required_precision_normal` (Impact: 2.0)
  * `test_specifier_parse_failure_fallback` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 53`, `args: 18`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `orphaned_logic: 18`
* *Architecture:* `api: 18`, `import: 6`
* *Defense:* `safety: 23`, `test: 42`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, python_discovery._specifier, unittest.mock, python_discovery
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/windows/test_windows_pep514.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.387 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.008 IQR)
- **Top Global Matches:** file_cluster_8: 9.387, file_cluster_13: 9.585, file_cluster_0: 9.715
- **Magnitude:** 34.18 | **LOC:** 157 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.0981%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_pep514_parse_functions` (Impact: 16.4)
  * `test_pep514` (Impact: 5.2)
  * `test_pep514_discovers_interpreters` (Impact: 3.9)
  * `test_pep514_run` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 31`, `args: 4`, `func_start: 4`
* *Risk/State:* `orphaned_logic: 4`
* *Architecture:* `io: 2`, `api: 4`, `import: 8`
* *Defense:* `safety: 13`, `doc: 2`, `test: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` textwrap, python_discovery._windows._pep514, sys, pytest, __future__, python_discovery._windows
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/py_info/test_py_info_exe_based_of.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.672 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.449 IQR)
- **Top Global Matches:** file_cluster_13: 9.672, file_cluster_0: 9.819, file_cluster_8: 10.01
- **Magnitude:** 18.84 | **LOC:** 83 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.4259%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_discover_base_folders` (Impact: 5.6)
  * `test_discover_empty_folder` (Impact: 3.6)
  * `_fs_supports_symlink` (Impact: 1.8)
  * `test_discover_ok` (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 23`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 2`, `import: 8`
* *Defense:* `safety: 3`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` python_discovery._discovery, pathlib, pytest, __future__, python_discovery._py_info, python_discovery, python_discovery._compat, logging
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/tests/windows/winreg_mock_values.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.404 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.308 IQR)
- **Top Global Matches:** file_cluster_8: 4.404, file_cluster_7: 6.195, file_cluster_1: 6.273
- **Magnitude:** 18.38 | **LOC:** 171 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/src/python_discovery/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.095 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.673 IQR)
- **Top Global Matches:** file_cluster_8: 7.095, file_cluster_13: 7.111, file_cluster_7: 7.71
- **Magnitude:** 16.42 | **LOC:** 28 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.3961%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 14`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ._discovery, ._cache, ._py_info, ._specifier, __future__, importlib.metadata, ._py_spec
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/src/python_discovery/_windows/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 7.654 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.986 IQR)
- **Top Global Matches:** file_cluster_13: 7.654, file_cluster_8: 7.756, file_cluster_7: 8.142
- **Magnitude:** 15.68 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ._pep514, __future__, ._propose
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/src/python_discovery/_compat.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.06 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.689 IQR)
- **Top Global Matches:** file_cluster_13: 8.06, file_cluster_16: 8.61, file_cluster_8: 8.724
- **Magnitude:** 10.98 | **LOC:** 30 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.242%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fs_is_case_sensitive` (Impact: 7.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 13`, `args: 2`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 3`, `import: 6`
* *Defense:* `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 84.156
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.272212
  * `Imports (Out-Degree: 0):` logging, functools, typing, __future__, pathlib, tempfile
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/src/python_discovery/_windows/_propose.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 7.662 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.332 IQR)
- **Top Global Matches:** file_cluster_13: 7.662, file_cluster_8: 8.001, file_cluster_16: 8.094
- **Magnitude:** 4.96 | **LOC:** 54 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.0418%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `propose_interpreters` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 16`, `args: 2`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 3`, `import: 7`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 30.803
  * `Choke Point (Betweenness):` 0.007905 | `Ripple Effect (Closeness):` 0.043478
  * `Imports (Out-Degree: 3):` python_discovery._py_spec, ._pep514, python_discovery._cache, typing, __future__, python_discovery._py_info, collections.abc
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `python_discovery-1.2.1/tests/windows/test_windows.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 7.938 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.944 IQR)
- **Top Global Matches:** file_cluster_13: 7.938, file_cluster_0: 8.096, file_cluster_8: 8.096
- **Magnitude:** 3.58 | **LOC:** 36 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.5016%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_propose_interpreters` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 10`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 5`
* *Defense:* `safety: 1`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, pytest, __future__, python_discovery, python_discovery._windows
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python_discovery-1.2.1/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 44 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.616
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `python_discovery-1.2.1/src/python_discovery/_specifier.py` (PYTHON) | Magnitude: 212.92 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 182, structural_boundaries: 89, branch: 65, doc: 42
- `python_discovery-1.2.1/tests/py_info/test_py_info.py` (PYTHON) | Magnitude: 97.1 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 295, test: 130, structural_boundaries: 125, safety: 64
- `python_discovery-1.2.1/src/python_discovery/_discovery.py` (PYTHON) | Magnitude: 148.94 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 210, branch: 88, structural_boundaries: 83, generics: 49
- `python_discovery-1.2.1/tests/test_discovery_extra.py` (PYTHON) | Magnitude: 87.28 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 138, structural_boundaries: 80, test: 69, explicit_casts: 36
- `python_discovery-1.2.1/src/python_discovery/_py_info.py` (PYTHON) | Magnitude: 560.0 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 577, branch: 191, structural_boundaries: 161, state_mutation: 134

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `python_discovery-1.2.1/tests/test_specifier.py` (PYTHON) | Magnitude: 123.92 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 160, test: 137, structural_boundaries: 90, safety: 45
- `python_discovery-1.2.1/src/python_discovery/_cache.py` (PYTHON) | Magnitude: 99.58 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 91, structural_boundaries: 60, doc: 36, api: 28
- `python_discovery-1.2.1/tests/test_py_spec_extra.py` (PYTHON) | Magnitude: 58.38 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 53, test: 42, safety: 23
- `python_discovery-1.2.1/tests/test_cache.py` (PYTHON) | Magnitude: 65.64 | Delta: **0.166 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 42, test: 35, safety: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `python_discovery-1.2.1/tests/test_py_info_extra.py` (PYTHON) | Magnitude: 237.02 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 303, test: 179, structural_boundaries: 154, safety: 86
- `python_discovery-1.2.1/src/python_discovery/__init__.py` (PYTHON) | Magnitude: 16.42 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 11, encapsulation: 9, import: 7
- `python_discovery-1.2.1/tests/test_cached_py_info.py` (PYTHON) | Magnitude: 83.78 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 147, structural_boundaries: 90, test: 85, safety: 54
- `python_discovery-1.2.1/tests/test_discovery.py` (PYTHON) | Magnitude: 135.68 | Delta: **0.162 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 300, test: 113, structural_boundaries: 112, branch: 63
- `python_discovery-1.2.1/tests/windows/test_windows_pep514.py` (PYTHON) | Magnitude: 34.18 | Delta: **0.198 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 114, structural_boundaries: 31, test: 30, encapsulation: 14

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `python_discovery-1.2.1/src/python_discovery/_py_info.py` -> **Severity: 3.551** (Bridge: 0.0356 * Flux: 99.8253%)
- `python_discovery-1.2.1/src/python_discovery/_discovery.py` -> **Severity: 1.761** (Bridge: 0.0178 * Flux: 99.0289%)
- `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py` -> **Severity: 0.561** (Bridge: 0.0059 * Flux: 94.6487%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `python_discovery-1.2.1/src/python_discovery/_py_info.py` -> **Severity: 21.701** (Embedded: 0.3507 * Error Risk: 61.8745%)
- `python_discovery-1.2.1/src/python_discovery/_cache.py` -> **Severity: 19.662** (Embedded: 0.3674 * Error Risk: 53.5174%)
- `python_discovery-1.2.1/src/python_discovery/_cached_py_info.py` -> **Severity: 11.522** (Embedded: 0.2287 * Error Risk: 50.3735%)
- `python_discovery-1.2.1/src/python_discovery/_discovery.py` -> **Severity: 10.998** (Embedded: 0.1739 * Error Risk: 63.2377%)
- `python_discovery-1.2.1/src/python_discovery/_windows/_pep514.py` -> **Severity: 8.871** (Embedded: 0.1304 * Error Risk: 68.0117%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `python_discovery-1.2.1/src/python_discovery/_cache.py` -> **Severity: 13984.749** (Blast Radius: 142.38 * Doc Risk: 98.2213%)
- `python_discovery-1.2.1/src/python_discovery/_compat.py` -> **Severity: 6995.737** (Blast Radius: 84.156 * Doc Risk: 83.1282%)
- `python_discovery-1.2.1/src/python_discovery/_py_info.py` -> **Severity: 3675.975** (Blast Radius: 130.036 * Doc Risk: 28.2689%)
- `python_discovery-1.2.1/src/python_discovery/_windows/_pep514.py` -> **Severity: 3404.651** (Blast Radius: 57.904 * Doc Risk: 58.7982%)
- `python_discovery-1.2.1/src/python_discovery/_discovery.py` -> **Severity: 2063.035** (Blast Radius: 69.081 * Doc Risk: 29.864%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
