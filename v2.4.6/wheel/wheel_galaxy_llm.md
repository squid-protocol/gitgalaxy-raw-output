# ARCHITECTURAL_BRIEF: wheel
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/wheel` |
| **Timestamp** | `2026-08-03T21:26:21.744205+00:00` |
| **Scan Duration** | `0.19s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 23 malicious artifacts.

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
| Total Artifacts | 31 |
| Analyzed Artifacts (Scanned) | 25 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6 |
| Total LOC | 2320 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 80.6% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3923 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.278 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6023 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 23 | 2320 | 92.0% |
| PLAINTEXT | 2 | 0 | 8.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.614`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 13 | 52.0% |
| file_cluster_8 | 10 | 40.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 8.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6*

**Composition by Extension & Reason:**
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 39 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.whl`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 1.6 | 62.4 | 10.4 | 5.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 30.2 | 3.0 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 9.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 18.0 | 0.3 | 0.0 |
| API Exposure | 0.0 | 8.9 | 3.6 | 3.2 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 16.0 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 10.7 | 0.8 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 87.2 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 40.9 | 25.8 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 51.3 | 36.4 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 38.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `wheel-0.46.3/src/wheel/_bdist_wheel.py` (Hits: 39)
- `wheel-0.46.3/src/wheel/wheelfile.py` (Hits: 14)
- `wheel-0.46.3/src/wheel/macosx_libfile.py` (Hits: 10)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **wheelfile.py** (`wheel-0.46.3/src/wheel/wheelfile.py`) — 10 inbound connections
2. **_metadata.py** (`wheel-0.46.3/src/wheel/_metadata.py`) — 4 inbound connections
3. **util.py** (`wheel-0.46.3/tests/commands/util.py`) — 4 inbound connections
4. **convert.py** (`wheel-0.46.3/src/wheel/_commands/convert.py`) — 2 inbound connections
5. **tags.py** (`wheel-0.46.3/src/wheel/_commands/tags.py`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **_bdist_wheel.py** (`wheel-0.46.3/src/wheel/_bdist_wheel.py`) — 25 outbound dependencies
2. **convert.py** (`wheel-0.46.3/src/wheel/_commands/convert.py`) — 17 outbound dependencies
3. **wheelfile.py** (`wheel-0.46.3/src/wheel/wheelfile.py`) — 13 outbound dependencies
4. **_metadata.py** (`wheel-0.46.3/src/wheel/_metadata.py`) — 11 outbound dependencies
5. **test_convert.py** (`wheel-0.46.3/tests/commands/test_convert.py`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_nonblank` (@ `wheel-0.46.3/src/wheel/_metadata.py`) -> Impact: **293.2** | LOC: 104
- `bdist_wininst_path` (@ `wheel-0.46.3/tests/commands/test_convert.py`) -> Impact: **287.8** | LOC: 155
  * *Intent:* """.encode() @pytest.fixture( params=[ pytest.param(("py3.7", "win32"), id="win32"), pytest.param(("py3.7", "win_amd64"), id="amd64"), pytest.param((N...
- `calculate_macosx_platform_tag` (@ `wheel-0.46.3/src/wheel/macosx_libfile.py`) -> Impact: **173.6** | LOC: 77
- `__init__` (@ `wheel-0.46.3/src/wheel/_commands/convert.py`) -> Impact: **140.9** | LOC: 29
- `extract_macosx_min_system_version` (@ `wheel-0.46.3/src/wheel/macosx_libfile.py`) -> Impact: **121.8** | LOC: 57
- `pack` (@ `wheel-0.46.3/src/wheel/_commands/pack.py`) -> Impact: **103.1** | LOC: 62
  * *Intent:* """Repack a previously unpacked wheel directory into a new wheel file. The .dist-info/WHEEL file must contain one or more tags so that the target whee...
- `get_tag` (@ `wheel-0.46.3/src/wheel/_bdist_wheel.py`) -> Impact: **101.6** | LOC: 57
- `write_files` (@ `wheel-0.46.3/src/wheel/wheelfile.py`) -> Impact: **100.4** | LOC: 69
- `license_paths` (@ `wheel-0.46.3/src/wheel/_bdist_wheel.py`) -> Impact: **99.1** | LOC: 43
- `convert` (@ `wheel-0.46.3/src/wheel/_commands/convert.py`) -> Impact: **86.5** | LOC: 51

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `_nonblank` (@ `wheel-0.46.3/src/wheel/_metadata.py`) -> **O(2^N) [Recursive]**
- `close` (@ `wheel-0.46.3/src/wheel/wheelfile.py`) -> **O(2^N) [Recursive]**
- `bdist_wininst_path` (@ `wheel-0.46.3/tests/commands/test_convert.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """.encode() @pytest.fixture( params=[ pytest.param(("py3.7", "win32"), id="win32"), pytest.param(("py3.7", "win_amd64"), id="amd64"), pytest.param((N...
- `get_platform` (@ `wheel-0.46.3/src/wheel/_bdist_wheel.py`) -> **O(2^N) [Recursive]**
- `main` (@ `wheel-0.46.3/src/wheel/__main__.py`) -> **O(2^N) [Recursive]**
- `urlsafe_b64encode` (@ `wheel-0.46.3/src/wheel/wheelfile.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """urlsafe_b64encode without padding"""
- `urlsafe_b64decode` (@ `wheel-0.46.3/src/wheel/wheelfile.py`) -> **O(2^N) [Recursive]**
- `license_paths` (@ `wheel-0.46.3/src/wheel/_bdist_wheel.py`) -> **O(N^6)**
- `__init__` (@ `wheel-0.46.3/src/wheel/_commands/convert.py`) -> **O(N^6)**
- `convert` (@ `wheel-0.46.3/src/wheel/_commands/convert.py`) -> **O(N^6)**

### Highest Data Gravity (Database Complexity)
- `egg2dist` (@ `wheel-0.46.3/src/wheel/_bdist_wheel.py`) -> DB Complexity: **54**
- `run` (@ `wheel-0.46.3/src/wheel/_bdist_wheel.py`) -> DB Complexity: **36**
- `write_files` (@ `wheel-0.46.3/src/wheel/wheelfile.py`) -> DB Complexity: **25**
- `pack` (@ `wheel-0.46.3/src/wheel/_commands/pack.py`) -> DB Complexity: **21**
  * *Intent:* """Repack a previously unpacked wheel directory into a new wheel file. The .dist-info/WHEEL file must contain one or more tags so that the target whee...
- `calculate_macosx_platform_tag` (@ `wheel-0.46.3/src/wheel/macosx_libfile.py`) -> DB Complexity: **21**
- `main` (@ `wheel-0.46.3/src/wheel/__main__.py`) -> DB Complexity: **15**
- `__init__` (@ `wheel-0.46.3/src/wheel/_commands/convert.py`) -> DB Complexity: **14**
- `pkginfo_to_metadata` (@ `wheel-0.46.3/src/wheel/_metadata.py`) -> DB Complexity: **12**
- `initialize_options` (@ `wheel-0.46.3/src/wheel/_bdist_wheel.py`) -> DB Complexity: **10**
- `__init__` (@ `wheel-0.46.3/src/wheel/_commands/convert.py`) -> DB Complexity: **10**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `wheel-0.46.3/src/wheel` | 9 | 1624.86 | 11.9% | 12.64% |
| `wheel-0.46.3/src/wheel/_commands` | 5 | 842.24 | 18.49% | 19.64% |
| `wheel-0.46.3/tests/commands` | 6 | 462.22 | 4.73% | 0.0% |
| `wheel-0.46.3/tests` | 3 | 161.4 | 3.81% | 0.0% |
| `wheel-0.46.3` | 1 | 1.0 | 0.0% | 0.0% |
| `wheel-0.46.3/tests/testdata` | 1 | 0.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `wheel-0.46.3/src/wheel/_setuptools_logging.py` -> **99.9729%** Exposure
- `wheel-0.46.3/src/wheel/_commands/convert.py` -> **98.2235%** Exposure
- `wheel-0.46.3/src/wheel/_bdist_wheel.py` -> **13.7842%** Exposure
### Highest State Flux (Mutation/Volatility)
- `wheel-0.46.3/src/wheel/_commands/convert.py` -> **99.9996%** Exposure
- `wheel-0.46.3/src/wheel/wheelfile.py` -> **79.5168%** Exposure
- `wheel-0.46.3/src/wheel/_bdist_wheel.py` -> **69.659%** Exposure
- `wheel-0.46.3/src/wheel/_commands/tags.py` -> **54.2145%** Exposure
- `wheel-0.46.3/src/wheel/_metadata.py` -> **49.6038%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `wheel-0.46.3/tests/test_wheelfile.py` -> **11** Orphaned Functions | **0** Duplicates
- `wheel-0.46.3/tests/commands/test_tags.py` -> **10** Orphaned Functions | **0** Duplicates
- `wheel-0.46.3/src/wheel/_commands/convert.py` -> **0** Orphaned Functions | **6** Duplicates
- `wheel-0.46.3/tests/commands/test_unpack.py` -> **3** Orphaned Functions | **0** Duplicates
- `wheel-0.46.3/tests/commands/test_convert.py` -> **2** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`wheel-0.46.3/src/wheel/_bdist_wheel.py`** -> AI Confidence: **99.31%**
2. **`wheel-0.46.3/src/wheel/_commands/convert.py`** -> AI Confidence: **99.31%**
3. **`wheel-0.46.3/src/wheel/_commands/pack.py`** -> AI Confidence: **99.31%**
4. **`wheel-0.46.3/src/wheel/_commands/tags.py`** -> AI Confidence: **99.31%**
5. **`wheel-0.46.3/src/wheel/wheelfile.py`** -> AI Confidence: **99.31%**
6. **`wheel-0.46.3/src/wheel/_metadata.py`** -> AI Confidence: **99.24%**
7. **`wheel-0.46.3/src/wheel/_commands/__init__.py`** -> AI Confidence: **99.18%**
8. **`wheel-0.46.3/tests/commands/util.py`** -> AI Confidence: **99.18%**
9. **`wheel-0.46.3/tests/commands/test_convert.py`** -> AI Confidence: **99.16%**
10. **`wheel-0.46.3/tests/commands/test_pack.py`** -> AI Confidence: **99.15%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `wheel-0.46.3/src/wheel/_bdist_wheel.py` -> **100.0%** Exposure
- `wheel-0.46.3/src/wheel/_commands/convert.py` -> **100.0%** Exposure
- `wheel-0.46.3/src/wheel/_metadata.py` -> **100.0%** Exposure
- `wheel-0.46.3/src/wheel/macosx_libfile.py` -> **100.0%** Exposure
- `wheel-0.46.3/src/wheel/wheelfile.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `wheel-0.46.3/src/wheel/__main__.py` -> **100.0%** Exposure
- `wheel-0.46.3/src/wheel/_bdist_wheel.py` -> **100.0%** Exposure
- `wheel-0.46.3/src/wheel/_commands/convert.py` -> **100.0%** Exposure
- `wheel-0.46.3/src/wheel/_commands/pack.py` -> **100.0%** Exposure
- `wheel-0.46.3/src/wheel/_metadata.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `149` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `wheel-0.46.3/src/wheel/_commands/convert.py` (PYTHON) -> Cumulative Risk: **827.36**
- **Archetype:** `file_cluster_13` (Distance: 11.346 IQR)
- **Magnitude:** 624.26 | **LOC:** 338 | **CtrlFlow:** 55.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9996%)
- **Heaviest Functions:** `__init__` (Impact: 140.9), `convert` (Impact: 86.5), `generate_contents` (Impact: 56.2)

### 2. `wheel-0.46.3/src/wheel/wheelfile.py` (PYTHON) -> Cumulative Risk: **641.84**
- **Archetype:** `file_cluster_13` (Distance: 10.351 IQR)
- **Magnitude:** 219.24 | **LOC:** 242 | **CtrlFlow:** 51.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.3192%)
- **Heaviest Functions:** `write_files` (Impact: 100.4), `close` (Impact: 52.7), `_update_crc` (Impact: 20.3)

### 3. `wheel-0.46.3/src/wheel/_bdist_wheel.py` (PYTHON) -> Cumulative Risk: **561.11**
- **Archetype:** `file_cluster_13` (Distance: 10.344 IQR)
- **Magnitude:** 657.3 | **LOC:** 617 | **CtrlFlow:** 53.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.0238%)
- **Heaviest Functions:** `get_tag` (Impact: 101.6), `license_paths` (Impact: 99.1), `egg2dist` (Impact: 81.6)

### 4. `wheel-0.46.3/src/wheel/macosx_libfile.py` (PYTHON) -> Cumulative Risk: **543.94**
- **Archetype:** `file_cluster_8` (Distance: 9.532 IQR)
- **Magnitude:** 329.12 | **LOC:** 487 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Verification (80.0%)
- **Heaviest Functions:** `calculate_macosx_platform_tag` (Impact: 173.6), `extract_macosx_min_system_version` (Impact: 121.8), `swap32` (Impact: 3.4)

### 5. `wheel-0.46.3/src/wheel/_metadata.py` (PYTHON) -> Cumulative Risk: **536.85**
- **Archetype:** `file_cluster_13` (Distance: 10.417 IQR)
- **Magnitude:** 358.92 | **LOC:** 185 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.6323%)
- **Heaviest Functions:** `_nonblank` (Impact: 293.2), `pkginfo_to_metadata` (Impact: 48.6)

### 6. `wheel-0.46.3/src/wheel/_commands/pack.py` (PYTHON) -> Cumulative Risk: **460.51**
- **Archetype:** `file_cluster_13` (Distance: 9.128 IQR)
- **Magnitude:** 107.1 | **LOC:** 85 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (89.5243%), Verification (80.0%)
- **Heaviest Functions:** `pack` (Impact: 103.1)

### 7. `wheel-0.46.3/src/wheel/_commands/__init__.py` (PYTHON) -> Cumulative Risk: **440.82**
- **Archetype:** `file_cluster_8` (Distance: 8.681 IQR)
- **Magnitude:** 76.06 | **LOC:** 154 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.6677%), Documentation (98.8985%), Verification (80.0%)
- **Heaviest Functions:** `parse_build_tag` (Impact: 15.3), `main` (Impact: 14.5), `parser` (Impact: 13.5)

### 8. `wheel-0.46.3/src/wheel/_setuptools_logging.py` (PYTHON) -> Cumulative Risk: **394.45**
- **Archetype:** `file_cluster_13` (Distance: 8.799 IQR)
- **Magnitude:** 6.48 | **LOC:** 27 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (99.9729%), Spec Match (93.3333%), Algorithmic Dos (72.8654%), Documentation (69.9805%)
- **Heaviest Functions:** `configure` (Impact: 3.1), `_not_warning` (Impact: 2.1)

### 9. `wheel-0.46.3/tests/test_wheelfile.py` (PYTHON) -> Cumulative Risk: **362.37**
- **Archetype:** `file_cluster_8` (Distance: 10.337 IQR)
- **Magnitude:** 135.94 | **LOC:** 205 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (98.6544%), Stability (50.0%)
- **Heaviest Functions:** `test_testzip_bad_hash` (Impact: 20.6), `test_attributes` (Impact: 18.4), `test_testzip_missing_hash` (Impact: 15.4)

### 10. `wheel-0.46.3/tests/commands/test_convert.py` (PYTHON) -> Cumulative Risk: **358.59**
- **Archetype:** `file_cluster_13` (Distance: 10.663 IQR)
- **Magnitude:** 324.02 | **LOC:** 292 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9995%), Stability (50.0%)
- **Heaviest Functions:** `bdist_wininst_path` (Impact: 287.8), `expected_wheelfile` (Impact: 9.6), `pyver_arch` (Impact: 2.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `wheel-0.46.3/src/wheel/_bdist_wheel.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.344 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.578 IQR)
- **Top Global Matches:** file_cluster_13: 10.344, file_cluster_8: 10.602, file_cluster_16: 10.804
- **Magnitude:** 657.3 | **LOC:** 617 | **CtrlFlow:** 53.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 54
- **Risk Profile:** Cognitive Load (16.4005%), Tech Debt (13.7842%)
**Top Internal Functions/Classes:**
  * `get_tag` (Impact: 101.6 | O(N^5))
  * `license_paths` (Impact: 99.1 | O(N^6) | DB: 3)
  * `egg2dist` (Impact: 81.6 | O(N^5) | DB: 54)
  * `run` (Impact: 77.2 | O(N^5) | DB: 36)
  * `get_abi_tag` (Impact: 71.2 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 95`, `args: 22`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 35`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 39`, `api: 22`, `import: 30`
* *Defense:* `safety: 11`, `doc: 18`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 62.778
  * `Choke Point (Betweenness):` 0.01087 | `Ripple Effect (Closeness):` 0.055556
  * `Imports (Out-Degree: 3):` sysconfig, struct, email.policy, , sys, collections.abc, setuptools.logging, packaging...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wheel-0.46.3/src/wheel/_commands/convert.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.346 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.89 IQR)
- **Top Global Matches:** file_cluster_13: 11.346, file_cluster_16: 11.769, file_cluster_8: 11.83
- **Magnitude:** 624.26 | **LOC:** 338 | **CtrlFlow:** 55.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (62.4336%), Tech Debt (98.2235%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 140.9 | O(N^6) | DB: 14)
  * `convert` (Impact: 86.5 | O(N^6))
  * `generate_contents` (Impact: 56.2 | O(N^6))
  * `convert_pkg_info` (Impact: 56.0 | O(N^6))
  * `generate_contents` (Impact: 55.9 | O(N^6) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 63`, `args: 12`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 87`, `duplicate_logic: 6`
* *Architecture:* `io: 3`, `api: 14`, `import: 17`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 35.466
  * `Choke Point (Betweenness):` 0.005435 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 3):` collections.abc, ..wheelfile, re, packaging.tags, email.policy, .., .._metadata, os.path...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `wheel-0.46.3/src/wheel/_metadata.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.417 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.095 IQR)
- **Top Global Matches:** file_cluster_13: 10.417, file_cluster_16: 10.767, file_cluster_0: 10.968
- **Magnitude:** 358.92 | **LOC:** 185 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (10.6924%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_nonblank` (Impact: 293.2 | O(2^N) | DB: 2)
  * `pkginfo_to_metadata` (Impact: 48.6 | O(N^5) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 41`, `args: 11`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 6`, `dead_code: 1`
* *Architecture:* `io: 5`, `api: 9`, `import: 11`
* *Defense:* `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 93.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.205128
  * `Imports (Out-Degree: 0):` functools, collections.abc, itertools, re, typing, os.path, email.message, textwrap...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `wheel-0.46.3/src/wheel/macosx_libfile.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.532 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.314 IQR)
- **Top Global Matches:** file_cluster_8: 9.532, file_cluster_13: 9.695, file_cluster_16: 9.779
- **Magnitude:** 329.12 | **LOC:** 487 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (8.5284%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `calculate_macosx_platform_tag` (Impact: 173.6 | O(N^6) | DB: 21)
  * `extract_macosx_min_system_version` (Impact: 121.8 | O(N^6) | DB: 4)
  * `swap32` (Impact: 3.4 | O(N^2))
  * `parse_version` (Impact: 2.2 | O(N^1))
  * `read_data` (Impact: 1.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 46`, `args: 7`, `func_start: 7`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`, `dead_code: 1`
* *Architecture:* `io: 10`, `api: 16`, `import: 7`
* *Defense:* `safety: 6`, `doc: 31`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 42.19
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0625
  * `Imports (Out-Degree: 0):` os, typing, sys, ctypes, __future__, io
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wheel-0.46.3/tests/commands/test_convert.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.663 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.003 IQR)
- **Top Global Matches:** file_cluster_13: 10.663, file_cluster_8: 10.765, file_cluster_16: 10.816
- **Magnitude:** 324.02 | **LOC:** 292 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (2.8407%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bdist_wininst_path` (Impact: 287.8 | O(2^N) | DB: 3)
    * *Intent:* """.encode() @pytest.fixture( params=[ pytest.param(("py3.7", "win32"), id="win32"), pytest.param(("...
  * `expected_wheelfile` (Impact: 9.6 | O(N^2))
  * `pyver_arch` (Impact: 2.1 | O(N^1))
  * `test_convert_pkg_info_with_empty_descrip` (Impact: 2.1 | O(N^1))
  * `test_convert_pkg_info_with_one_line_desc` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 70`, `args: 13`, `func_start: 13`
* *Risk/State:* `orphaned_logic: 2`
* *Architecture:* `io: 2`, `api: 13`, `import: 12`
* *Defense:* `safety: 21`, `doc: 14`, `test: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.403
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` pytest, wheel.wheelfile, wheel._commands.convert, wheel, _pytest.fixtures, email.message, textwrap, commands.util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/src/wheel/wheelfile.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.351 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.49 IQR)
- **Top Global Matches:** file_cluster_13: 10.351, file_cluster_8: 10.604, file_cluster_16: 10.674
- **Magnitude:** 219.24 | **LOC:** 242 | **CtrlFlow:** 51.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (21.5853%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `write_files` (Impact: 100.4 | O(N^6) | DB: 25)
  * `close` (Impact: 52.7 | O(2^N) | DB: 1)
  * `_update_crc` (Impact: 20.3 | O(N^4) | DB: 1)
  * `urlsafe_b64encode` (Impact: 4.2 | O(2^N))
    * *Intent:* """urlsafe_b64encode without padding"""
  * `urlsafe_b64decode` (Impact: 4.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 40`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 17`
* *Architecture:* `io: 14`, `api: 12`, `import: 13`
* *Defense:* `safety: 8`, `doc: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 186.136
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.4
  * `Imports (Out-Degree: 0):` stat, csv, zipfile, logging, re, typing, os.path, _typeshed...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `wheel-0.46.3/tests/test_wheelfile.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.337 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.446 IQR)
- **Top Global Matches:** file_cluster_8: 10.337, file_cluster_13: 10.546, file_cluster_0: 10.557
- **Magnitude:** 135.94 | **LOC:** 205 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.8296%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_testzip_bad_hash` (Impact: 20.6 | O(N^3))
  * `test_attributes` (Impact: 18.4 | O(N^3))
    * *Intent:* # With the change from ZipFile.write() to .writestr(), we need to manually # set member attributes. ...
  * `test_testzip_missing_hash` (Impact: 15.4 | O(N^2))
  * `test_write_str` (Impact: 13.0 | O(N^3))
  * `test_unsupported_hash_algorithm` (Impact: 12.5 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 55`, `args: 12`, `func_start: 12`
* *Risk/State:* `orphaned_logic: 11`
* *Architecture:* `io: 2`, `api: 12`, `import: 8`
* *Defense:* `safety: 13`, `test: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.403
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stat, pytest, wheel.wheelfile, sys, pathlib, zipfile, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/src/wheel/_commands/pack.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.128 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 6.123 IQR)
- **Top Global Matches:** file_cluster_13: 9.128, file_cluster_8: 9.257, file_cluster_16: 9.433
- **Magnitude:** 107.1 | **LOC:** 85 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (10.5409%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pack` (Impact: 103.1 | O(N^4) | DB: 21)
    * *Intent:* """Repack a previously unpacked wheel directory into a new wheel file. The .dist-info/WHEEL file mus...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 19`, `args: 2`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `io: 8`, `api: 3`, `import: 7`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.041667
  * `Imports (Out-Degree: 1):` email.generator, re, email.policy, os.path, email.parser, ..wheelfile, __future__
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wheel-0.46.3/tests/commands/test_tags.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.46 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.287 IQR)
- **Top Global Matches:** file_cluster_8: 10.46, file_cluster_13: 10.762, file_cluster_16: 10.89
- **Magnitude:** 85.0 | **LOC:** 233 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.1417%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_permission_bits` (Impact: 26.1 | O(N^4))
  * `test_multi_tags` (Impact: 7.3 | O(N^2))
  * `test_python_tags` (Impact: 7.0 | O(N^2))
  * `test_invalid_build_tag` (Impact: 6.3 | O(N^2))
  * `test_plat_tags` (Impact: 5.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 68`, `args: 11`, `func_start: 11`
* *Risk/State:* `orphaned_logic: 10`
* *Architecture:* `io: 1`, `api: 11`, `import: 8`
* *Defense:* `safety: 35`, `test: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.403
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pytest, wheel.wheelfile, pathlib, __future__, zipfile, .util, shutil, subprocess
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/src/wheel/_commands/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.681 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.082 IQR)
- **Top Global Matches:** file_cluster_8: 8.681, file_cluster_13: 8.804, file_cluster_16: 9.021
- **Magnitude:** 76.06 | **LOC:** 154 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (5.2873%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_build_tag` (Impact: 15.3 | O(N^2))
  * `main` (Impact: 14.5 | O(N^3) | DB: 3)
  * `parser` (Impact: 13.5 | O(N^2) | DB: 6)
  * `tags_f` (Impact: 12.8 | O(N^3))
  * `unpack_f` (Impact: 2.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 33`, `args: 9`, `func_start: 8`
* *Risk/State:* None
* *Architecture:* `io: 3`, `api: 9`, `import: 11`
* *Defense:* `safety: 3`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.403
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` os, .unpack, .convert, .pack, .tags, .., sys, ..wheelfile...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/tests/commands/test_unpack.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.523 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.492 IQR)
- **Top Global Matches:** file_cluster_8: 9.523, file_cluster_13: 9.548, file_cluster_0: 9.925
- **Magnitude:** 29.08 | **LOC:** 80 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.1857%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_unpack` (Impact: 9.2 | O(N^3))
  * `test_chmod_outside_unpack_tree` (Impact: 8.9 | O(N^3))
  * `test_unpack_executable_bit` (Impact: 6.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 26`, `args: 3`, `func_start: 3`
* *Risk/State:* `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 3`, `import: 8`
* *Defense:* `safety: 7`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.403
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` stat, pytest, wheel.wheelfile, pathlib, platform, .util, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/src/wheel/_commands/tags.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.381 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.286 IQR)
- **Top Global Matches:** file_cluster_8: 9.381, file_cluster_13: 9.388, file_cluster_16: 9.811
- **Magnitude:** 21.36 | **LOC:** 141 | **CtrlFlow:** 47.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.1976%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_compute_tags` (Impact: 11.0 | O(N^2))
    * *Intent:* """Add or replace tags. Supports dot-separated tags"""
  * `tags` (Impact: 1.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 25`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 6`, `api: 1`, `import: 7`
* *Defense:* `safety: 1`, `doc: 10`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 38.601
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.09375
  * `Imports (Out-Degree: 1):` os, collections.abc, itertools, email.policy, email.parser, ..wheelfile, __future__
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `wheel-0.46.3/tests/test_metadata.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.007 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.154 IQR)
- **Top Global Matches:** file_cluster_8: 9.007, file_cluster_13: 9.071, file_cluster_16: 9.446
- **Magnitude:** 16.48 | **LOC:** 97 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (1.6139%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_metadata_deprecated` (Impact: 8.0 | O(N^2))
  * `test_pkginfo_to_metadata` (Impact: 5.5 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 13`, `args: 2`, `func_start: 2`
* *Risk/State:* `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 2`, `import: 5`
* *Defense:* `safety: 3`, `doc: 4`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.403
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` wheel._metadata, pytest, wheel, pathlib, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/src/wheel/bdist_wheel.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.33 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.119 IQR)
- **Top Global Matches:** file_cluster_8: 8.33, file_cluster_13: 8.363, file_cluster_7: 9.437
- **Magnitude:** 15.32 | **LOC:** 27 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (22.27%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 12`
* *Risk/State:* None
* *Architecture:* `import: 5`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 45.146
  * `Choke Point (Betweenness):` 0.007246 | `Ripple Effect (Closeness):` 0.041667
  * `Imports (Out-Degree: 1):` warnings, ._bdist_wheel, typing, setuptools.command.bdist_wheel
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wheel-0.46.3/src/wheel/metadata.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 6.0 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.343 IQR)
- **Top Global Matches:** file_cluster_13: 6.0, file_cluster_8: 6.057, file_cluster_7: 7.404
- **Magnitude:** 15.3 | **LOC:** 18 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (12.6382%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 26`
* *Risk/State:* None
* *Architecture:* `import: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.403
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` warnings, ._metadata, it
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/src/wheel/_commands/unpack.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.86%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.275 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 6.547 IQR)
- **Top Global Matches:** file_cluster_13: 9.275, file_cluster_8: 9.563, file_cluster_16: 9.661
- **Magnitude:** 13.46 | **LOC:** 31 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `unpack` (Impact: 11.2 | O(N^3))
    * *Intent:* """Unpack a wheel. Wheel content will be unpacked to {dest}/{name}-{ver}, where {name} is the packag...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 8`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 2`, `import: 3`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.041667
  * `Imports (Out-Degree: 1):` ..wheelfile, __future__, pathlib
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wheel-0.46.3/src/wheel/__main__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.392 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.69 IQR)
- **Top Global Matches:** file_cluster_13: 8.392, file_cluster_8: 8.981, file_cluster_16: 9.056
- **Magnitude:** 12.14 | **LOC:** 26 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 10.9 | O(2^N) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 10`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 5`, `api: 1`, `import: 5`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.403
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ._commands, typing, os.path, sys, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/src/wheel/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.008 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.596 IQR)
- **Top Global Matches:** file_cluster_8: 6.008, file_cluster_13: 6.182, file_cluster_7: 7.305
- **Magnitude:** 11.04 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.403
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/tests/commands/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.581 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.403
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/tests/commands/test_pack.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.18 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.517 IQR)
- **Top Global Matches:** file_cluster_13: 9.18, file_cluster_8: 9.473, file_cluster_0: 9.649
- **Magnitude:** 9.8 | **LOC:** 93 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.6823%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_pack` (Impact: 1.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 22`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 6`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 9`
* *Defense:* `safety: 4`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.403
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` os, pytest, email.policy, email.parser, email.message, zipfile, .util, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/tests/test_bdist_wheel.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.588 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.946 IQR)
- **Top Global Matches:** file_cluster_13: 9.588, file_cluster_16: 9.959, file_cluster_8: 10.049
- **Magnitude:** 8.98 | **LOC:** 7 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_import_bdist_wheel` (Impact: 7.9 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 24.403
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` wheel.bdist_wheel, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/src/wheel/_setuptools_logging.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.799 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.383 IQR)
- **Top Global Matches:** file_cluster_13: 8.799, file_cluster_16: 8.863, file_cluster_8: 8.902
- **Magnitude:** 6.48 | **LOC:** 27 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (99.9729%)
**Top Internal Functions/Classes:**
  * `configure` (Impact: 3.1 | O(N^2) | DB: 3)
    * *Intent:* """ Configure logging to emit warning and above to stderr and everything else to stdout. This behavi...
  * `_not_warning` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 2`, `func_start: 2`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 3`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.403
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` logging, sys, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/tests/commands/util.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.556 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.416 IQR)
- **Top Global Matches:** file_cluster_13: 8.556, file_cluster_8: 8.559, file_cluster_16: 9.457
- **Magnitude:** 3.8 | **LOC:** 44 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.5247%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_command` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 19`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `safety: 2`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 72.803
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.166667
  * `Imports (Out-Degree: 0):` os, pytest, unittest.mock, io, wheel._commands, sys, __future__, subprocess
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `wheel-0.46.3/tests/testdata/eggnames.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.76 | **LOC:** 88 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.403
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wheel-0.46.3/LICENSE.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 22 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 24.403
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `wheel-0.46.3/tests/commands/util.py` (PYTHON) | Magnitude: 3.8 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 19, import: 8, test: 7
- `wheel-0.46.3/src/wheel/metadata.py` (PYTHON) | Magnitude: 15.3 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 26, import: 9, encapsulation: 8, indent_spaces: 5
- `wheel-0.46.3/src/wheel/_setuptools_logging.py` (PYTHON) | Magnitude: 6.48 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 7, import: 3, encapsulation: 3
- `wheel-0.46.3/tests/commands/test_convert.py` (PYTHON) | Magnitude: 324.02 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 145, structural_boundaries: 70, test: 46, branch: 29
- `wheel-0.46.3/src/wheel/_commands/pack.py` (PYTHON) | Magnitude: 107.1 | Delta: **0.129 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, branch: 19, structural_boundaries: 19, io: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `wheel-0.46.3/src/wheel/_commands/tags.py` (PYTHON) | Magnitude: 21.36 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 88, structural_boundaries: 25, branch: 23, doc: 10
- `wheel-0.46.3/tests/commands/test_unpack.py` (PYTHON) | Magnitude: 29.08 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 26, test: 14, sec_high_risk_execution: 11
- `wheel-0.46.3/src/wheel/bdist_wheel.py` (PYTHON) | Magnitude: 15.32 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 10, branch: 5, import: 5
- `wheel-0.46.3/tests/test_metadata.py` (PYTHON) | Magnitude: 16.48 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 13, test: 8, import: 5
- `wheel-0.46.3/src/wheel/_commands/__init__.py` (PYTHON) | Magnitude: 76.06 | Delta: **0.123 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 93, structural_boundaries: 33, branch: 12, import: 11

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `wheel-0.46.3/src/wheel/_bdist_wheel.py` -> **Severity: 0.757** (Bridge: 0.0109 * Flux: 69.659%)
- `wheel-0.46.3/src/wheel/_commands/convert.py` -> **Severity: 0.543** (Bridge: 0.0054 * Flux: 99.9996%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `wheel-0.46.3/src/wheel/wheelfile.py` -> **Severity: 3.357** (Embedded: 0.4 * Error Risk: 8.3927%)
- `wheel-0.46.3/src/wheel/_commands/convert.py` -> **Severity: 2.517** (Embedded: 0.0833 * Error Risk: 30.2025%)
- `wheel-0.46.3/src/wheel/_metadata.py` -> **Severity: 1.972** (Embedded: 0.2051 * Error Risk: 9.6133%)
- `wheel-0.46.3/src/wheel/_commands/tags.py` -> **Severity: 0.586** (Embedded: 0.0938 * Error Risk: 6.2525%)
- `wheel-0.46.3/src/wheel/_bdist_wheel.py` -> **Severity: 0.358** (Embedded: 0.0556 * Error Risk: 6.4412%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `wheel-0.46.3/src/wheel/wheelfile.py` -> **Severity: 18486.879** (Blast Radius: 186.136 * Doc Risk: 99.3192%)
- `wheel-0.46.3/src/wheel/_metadata.py` -> **Severity: 9337.938** (Blast Radius: 93.724 * Doc Risk: 99.6323%)
- `wheel-0.46.3/src/wheel/_bdist_wheel.py` -> **Severity: 6216.516** (Blast Radius: 62.778 * Doc Risk: 99.0238%)
- `wheel-0.46.3/src/wheel/_commands/convert.py` -> **Severity: 3546.515** (Blast Radius: 35.466 * Doc Risk: 99.9976%)
- `wheel-0.46.3/src/wheel/macosx_libfile.py` -> **Severity: 3087.211** (Blast Radius: 42.19 * Doc Risk: 73.174%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
