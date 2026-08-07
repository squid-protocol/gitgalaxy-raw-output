# ARCHITECTURAL_BRIEF: filelock
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/filelock` |
| **Timestamp** | `2026-08-07T05:22:29.117942+00:00` |
| **Scan Duration** | `0.21s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 23 malicious artifacts.

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
| Total Artifacts | 31 |
| Analyzed Artifacts (Scanned) | 24 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7 |
| Total LOC | 3837 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 77.4% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.185 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4626 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 16.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0095 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 23 | 3837 | 95.8% |
| MARKDOWN | 1 | 0 | 4.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.233`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 12 | 50.0% |
| file_cluster_0 | 7 | 29.2% |
| file_cluster_8 | 2 | 8.3% |
| file_cluster_16 | 1 | 4.2% |
| file_cluster_4 | 1 | 4.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 4.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 2.9 | 49.3 | 16.5 | 7.9 | 7.5 |
| Error & Exception Exposure | 0.0 | 80.0 | 19.0 | 2.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 21.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.6 | 0.0 | 0.0 |
| API Exposure | 0.2 | 9.3 | 3.9 | 3.4 | 0.2 |
| Concurrency Exposure | 0.0 | 100.0 | 35.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 99.7 | 12.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 28.0 | 2.8 | 0.0 | 0.0 |
| Specification Exposure | 86.7 | 100.0 | 99.4 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 98.4 | 14.6 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `filelock-3.25.2/tests/test_filelock.py` (Hits: 63)
- `filelock-3.25.2/src/filelock/_soft.py` (Hits: 19)
- `filelock-3.25.2/tests/test_soft_stale.py` (Hits: 18)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **_api.py** (`filelock-3.25.2/src/filelock/_api.py`) — 7 inbound connections
2. **_read_write.py** (`filelock-3.25.2/src/filelock/_read_write.py`) — 6 inbound connections
3. **_error.py** (`filelock-3.25.2/src/filelock/_error.py`) — 4 inbound connections
4. **_soft.py** (`filelock-3.25.2/src/filelock/_soft.py`) — 3 inbound connections
5. **_util.py** (`filelock-3.25.2/src/filelock/_util.py`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **asyncio.py** (`filelock-3.25.2/src/filelock/asyncio.py`) — 20 outbound dependencies
2. **_api.py** (`filelock-3.25.2/src/filelock/_api.py`) — 19 outbound dependencies
3. **test_filelock.py** (`filelock-3.25.2/tests/test_filelock.py`) — 19 outbound dependencies
4. **_read_write.py** (`filelock-3.25.2/src/filelock/_read_write.py`) — 14 outbound dependencies
5. **__init__.py** (`filelock-3.25.2/src/filelock/__init__.py`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `timeout_for_sqlite` (@ `filelock-3.25.2/src/filelock/_read_write.py`) -> Impact: **137.2** | LOC: 239
- `_acquire` (@ `filelock-3.25.2/src/filelock/_read_write.py`) -> Impact: **35.9** | LOC: 32
- `test_non_blocking` (@ `filelock-3.25.2/tests/test_async_filelock.py`) -> Impact: **34.6** | LOC: 69
  * *Intent:* # raises Timeout error when the lock cannot be acquired lock_path = tmp_path / "a" lock_1, lock_2 = lock_type(str(lock_path)), lock_type(str(lock_path...
- `_acquire` (@ `filelock-3.25.2/src/filelock/_unix.py`) -> Impact: **30.1** | LOC: 48
- `test_write_non_starvation` (@ `filelock-3.25.2/tests/test_read_write.py`) -> Impact: **28.5** | LOC: 50
  * *Intent:* """ NUM_READERS = 7 chain_forward = [Event() for _ in range(NUM_READERS)] chain_backward = [Event() for _ in range(NUM_READERS)] writer_ready = Event(...
- `release` (@ `filelock-3.25.2/src/filelock/_read_write.py`) -> Impact: **17.0** | LOC: 20
- `_acquire` (@ `filelock-3.25.2/src/filelock/_soft.py`) -> Impact: **16.7** | LOC: 23
- `_acquire` (@ `filelock-3.25.2/src/filelock/_windows.py`) -> Impact: **15.3** | LOC: 28
- `raise_on_not_writable_file` (@ `filelock-3.25.2/src/filelock/_util.py`) -> Impact: **14.9** | LOC: 19
  * *Intent:* """ Raise an exception if attempting to open the file for writing would fail. This is done so files that will never be writable can be separated from ...
- `test_sequential_mode_switch` (@ `filelock-3.25.2/tests/test_read_write_unit.py`) -> Impact: **14.4** | LOC: 8

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `filelock-3.25.2/tests` | 12 | 1508.32 | 12.64% | 0.0% |
| `filelock-3.25.2/src/filelock` | 11 | 839.92 | 20.63% | 44.51% |
| `filelock-3.25.2` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `filelock-3.25.2/src/filelock/_api.py` -> **100.0%** Exposure
- `filelock-3.25.2/src/filelock/_windows.py` -> **99.9997%** Exposure
- `filelock-3.25.2/src/filelock/_unix.py` -> **99.9955%** Exposure
- `filelock-3.25.2/src/filelock/_async_read_write.py` -> **97.1913%** Exposure
- `filelock-3.25.2/src/filelock/asyncio.py` -> **92.4142%** Exposure
### Highest State Flux (Mutation/Volatility)
- `filelock-3.25.2/src/filelock/_read_write.py` -> **99.72%** Exposure
- `filelock-3.25.2/src/filelock/_error.py` -> **48.556%** Exposure
- `filelock-3.25.2/src/filelock/_async_read_write.py` -> **37.2441%** Exposure
- `filelock-3.25.2/src/filelock/_api.py` -> **36.0065%** Exposure
- `filelock-3.25.2/src/filelock/_unix.py` -> **29.9133%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `filelock-3.25.2/tests/test_read_write_unit.py` -> **45** Orphaned Functions | **5** Duplicates
- `filelock-3.25.2/tests/test_async_read_write.py` -> **23** Orphaned Functions | **0** Duplicates
- `filelock-3.25.2/tests/test_async_filelock.py` -> **17** Orphaned Functions | **0** Duplicates
- `filelock-3.25.2/tests/test_read_write.py` -> **17** Orphaned Functions | **0** Duplicates
- `filelock-3.25.2/src/filelock/_api.py` -> **0** Orphaned Functions | **15** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`filelock-3.25.2/src/filelock/_read_write.py`** -> AI Confidence: **99.31%**
2. **`filelock-3.25.2/src/filelock/_soft.py`** -> AI Confidence: **99.24%**
3. **`filelock-3.25.2/src/filelock/_unix.py`** -> AI Confidence: **99.24%**
4. **`filelock-3.25.2/src/filelock/__init__.py`** -> AI Confidence: **99.18%**
5. **`filelock-3.25.2/src/filelock/_windows.py`** -> AI Confidence: **99.18%**
6. **`filelock-3.25.2/src/filelock/asyncio.py`** -> AI Confidence: **99.18%**
7. **`filelock-3.25.2/tests/test_async_read_write.py`** -> AI Confidence: **99.18%**
8. **`filelock-3.25.2/tests/test_lock_expiry.py`** -> AI Confidence: **99.18%**
9. **`filelock-3.25.2/tests/test_soft_stale.py`** -> AI Confidence: **99.18%**
10. **`filelock-3.25.2/src/filelock/_api.py`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `204` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `filelock-3.25.2/src/filelock/_async_read_write.py` (PYTHON) -> Cumulative Risk: **503.72**
- **Archetype:** `file_cluster_13` (Distance: 11.777 IQR)
- **Magnitude:** 100.42 | **LOC:** 204 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9999%), Tech Debt (97.1913%), Stability (50.0%)
- **Heaviest Functions:** `read_lock` (Impact: 11.8), `write_lock` (Impact: 11.8), `_run` (Impact: 4.6)

### 2. `filelock-3.25.2/src/filelock/_read_write.py` (PYTHON) -> Cumulative Risk: **469.51**
- **Archetype:** `file_cluster_13` (Distance: 12.065 IQR)
- **Magnitude:** 314.62 | **LOC:** 365 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.72%), Concurrency (99.4829%), Safety Score (60.0111%)
- **Heaviest Functions:** `timeout_for_sqlite` (Impact: 137.2), `_acquire` (Impact: 35.9), `release` (Impact: 17.0)

### 3. `filelock-3.25.2/src/filelock/_unix.py` (PYTHON) -> Cumulative Risk: **465.44**
- **Archetype:** `file_cluster_13` (Distance: 10.76 IQR)
- **Magnitude:** 58.48 | **LOC:** 117 | **CtrlFlow:** 40.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9955%), Concurrency (92.8487%), Stability (50.0%)
- **Heaviest Functions:** `_acquire` (Impact: 30.1), `_release` (Impact: 5.6), `_fallback_to_soft_lock` (Impact: 5.5)

### 4. `filelock-3.25.2/src/filelock/_api.py` (PYTHON) -> Cumulative Risk: **459.09**
- **Archetype:** `file_cluster_13` (Distance: 10.871 IQR)
- **Magnitude:** 120.8 | **LOC:** 579 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Verification (80.0%), Safety Score (54.5474%)
- **Heaviest Functions:** `release` (Impact: 7.6), `_try_break_expired_lock` (Impact: 7.5), `mode` (Impact: 5.4)

### 5. `filelock-3.25.2/src/filelock/asyncio.py` (PYTHON) -> Cumulative Risk: **447.22**
- **Archetype:** `file_cluster_13` (Distance: 10.383 IQR)
- **Magnitude:** 66.7 | **LOC:** 377 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.704%), Tech Debt (92.4142%), Safety Score (50.5869%)
- **Heaviest Functions:** `__aenter__` (Impact: 2.1), `run_in_executor` (Impact: 1.9), `executor` (Impact: 1.9)

### 6. `filelock-3.25.2/src/filelock/_error.py` (PYTHON) -> Cumulative Risk: **393.75**
- **Archetype:** `file_cluster_16` (Distance: 10.551 IQR)
- **Magnitude:** 16.56 | **LOC:** 31 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (98.3735%), Safety Score (80.0%), Stability (50.0%)
- **Heaviest Functions:** `__init__` (Impact: 1.9), `lock_file` (Impact: 1.9), `__reduce__` (Impact: 1.8)

### 7. `filelock-3.25.2/src/filelock/_soft.py` (PYTHON) -> Cumulative Risk: **349.29**
- **Archetype:** `file_cluster_13` (Distance: 9.597 IQR)
- **Magnitude:** 70.7 | **LOC:** 128 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Stability (50.0%), Safety Score (38.2961%)
- **Heaviest Functions:** `_acquire` (Impact: 16.7), `_is_process_alive` (Impact: 12.9), `_windows_unlink_with_retry` (Impact: 11.1)

### 8. `filelock-3.25.2/tests/test_async_filelock.py` (PYTHON) -> Cumulative Risk: **334.33**
- **Archetype:** `file_cluster_0` (Distance: 14.421 IQR)
- **Magnitude:** 188.76 | **LOC:** 322 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Stability (50.0%), Cognitive Load (49.3268%)
- **Heaviest Functions:** `test_non_blocking` (Impact: 34.6), `test_thread_local_run_in_executor` (Impact: 6.9), `test_cancel_check_triggers` (Impact: 5.7)

### 9. `filelock-3.25.2/src/filelock/_windows.py` (PYTHON) -> Cumulative Risk: **323.15**
- **Archetype:** `file_cluster_13` (Distance: 9.62 IQR)
- **Magnitude:** 35.88 | **LOC:** 112 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9997%), Stability (50.0%), Safety Score (48.6015%)
- **Heaviest Functions:** `_acquire` (Impact: 15.3), `_is_reparse_point` (Impact: 8.7), `_release` (Impact: 3.9)

### 10. `filelock-3.25.2/tests/test_async_read_write.py` (PYTHON) -> Cumulative Risk: **301.75**
- **Archetype:** `file_cluster_4` (Distance: 12.617 IQR)
- **Magnitude:** 268.88 | **LOC:** 271 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Stability (50.0%), Cognitive Load (48.3136%)
- **Heaviest Functions:** `test_close` (Impact: 12.0), `test_non_blocking_read` (Impact: 9.4), `test_non_blocking_write` (Impact: 9.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `filelock-3.25.2/tests/test_read_write_unit.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.823 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.202 IQR)
- **Top Global Matches:** file_cluster_0: 11.823, file_cluster_16: 11.839, file_cluster_8: 11.879
- **Magnitude:** 347.86 | **LOC:** 575 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.6773%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_sequential_mode_switch` (Impact: 14.4)
  * `test_close_releases_lock_and_closes_conn` (Impact: 10.8)
  * `test_non_blocking_transaction_lock_timeo` (Impact: 10.8)
  * `test_non_blocking_with_timeout_no_value_` (Impact: 10.8)
  * `test_finite_timeout_transaction_lock` (Impact: 10.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 143`, `args: 54`, `func_start: 54`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 12`, `duplicate_logic: 5`, `orphaned_logic: 45`
* *Architecture:* `io: 1`, `api: 53`, `concurrency: 18`, `import: 10`
* *Defense:* `safety: 70`, `test: 165`, `sync_locks: 6`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` collections.abc, filelock._read_write, __future__, typing, filelock, pytest_mock, pytest, threading...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/src/filelock/_read_write.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.065 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.834 IQR)
- **Top Global Matches:** file_cluster_13: 12.065, file_cluster_4: 12.282, file_cluster_16: 12.368
- **Magnitude:** 314.62 | **LOC:** 365 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.1175%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `timeout_for_sqlite` (Impact: 137.2)
  * `_acquire` (Impact: 35.9)
  * `release` (Impact: 17.0)
  * `read_lock` (Impact: 11.8)
    * *Intent:* """ Acquire a shared read lock. If this instance already holds a read lock, the lock level is increm...
  * `write_lock` (Impact: 11.8)
    * *Intent:* """ return self._acquire("read", timeout, blocking=blocking) def acquire_write(self, timeout: float ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 57`, `args: 15`, `func_start: 15`, `class_start: 2`
* *Risk/State:* `state_mutation: 42`
* *Architecture:* `io: 8`, `api: 11`, `concurrency: 28`, `import: 14`
* *Defense:* `safety: 7`, `doc: 43`, `sync_locks: 5`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 151.435
  * `Choke Point (Betweenness):` 0.013834 | `Ripple Effect (Closeness):` 0.328804
  * `Imports (Out-Degree: 2):` atexit, collections.abc, __future__, typing, threading, contextlib, os, weakref...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `filelock-3.25.2/tests/test_async_read_write.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.617 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.911 IQR)
- **Top Global Matches:** file_cluster_4: 12.617, file_cluster_0: 12.702, file_cluster_13: 13.009
- **Magnitude:** 268.88 | **LOC:** 271 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.3136%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_close` (Impact: 12.0)
  * `test_non_blocking_read` (Impact: 9.4)
  * `test_non_blocking_write` (Impact: 9.4)
  * `test_timeout_expires` (Impact: 9.4)
  * `test_sequential_mode_switch` (Impact: 9.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 126`, `args: 25`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 9`, `orphaned_logic: 23`
* *Architecture:* `io: 1`, `api: 24`, `concurrency: 95`, `import: 9`
* *Defense:* `safety: 57`, `test: 110`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` collections.abc, filelock._read_write, __future__, typing, concurrent.futures, filelock, pytest, sqlite3...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/tests/test_read_write.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.971 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.18 IQR)
- **Top Global Matches:** file_cluster_0: 11.971, file_cluster_13: 12.054, file_cluster_16: 12.099
- **Magnitude:** 219.8 | **LOC:** 562 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.8822%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_write_non_starvation` (Impact: 28.5)
    * *Intent:* """ NUM_READERS = 7 chain_forward = [Event() for _ in range(NUM_READERS)] chain_backward = [Event() ...
  * `test_write_lock_excludes_other_write_loc` (Impact: 9.5)
  * `cleanup_processes` (Impact: 8.3)
  * `recursive_read_lock` (Impact: 8.1)
  * `recursive_write_lock` (Impact: 8.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 122`, `args: 27`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 6`, `orphaned_logic: 17`
* *Architecture:* `io: 1`, `api: 27`, `concurrency: 3`, `import: 12`
* *Defense:* `safety: 69`, `doc: 34`, `test: 102`, `sync_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` collections.abc, filelock._read_write, __future__, typing, multiprocessing.synchronize, filelock, time, multiprocessing.sharedctypes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/tests/test_async_filelock.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.421 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.297 IQR)
- **Top Global Matches:** file_cluster_0: 14.421, file_cluster_4: 14.455, file_cluster_17: 14.726
- **Magnitude:** 188.76 | **LOC:** 322 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.3268%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_non_blocking` (Impact: 34.6)
    * *Intent:* # raises Timeout error when the lock cannot be acquired lock_path = tmp_path / "a" lock_1, lock_2 = ...
  * `test_thread_local_run_in_executor` (Impact: 6.9)
  * `test_cancel_check_triggers` (Impact: 5.7)
  * `test_non_executor` (Impact: 4.3)
  * `test_coroutine_function` (Impact: 3.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 142`, `args: 20`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`, `dead_code: 7`, `orphaned_logic: 17`
* *Architecture:* `io: 1`, `api: 17`, `concurrency: 89`, `import: 5`
* *Defense:* `safety: 59`, `test: 127`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, filelock, pytest, logging, pathlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/tests/test_filelock.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.978 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.223 IQR)
- **Top Global Matches:** file_cluster_0: 12.978, file_cluster_11: 13.385, file_cluster_13: 13.452
- **Magnitude:** 162.46 | **LOC:** 1148 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.5559%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_ro_folder` (Impact: 5.4)
  * `test_ro_file` (Impact: 5.4)
  * `tmp_path_ro` (Impact: 4.2)
  * `tmp_file_ro` (Impact: 4.2)
  * `make_ro` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 366`, `args: 85`, `func_start: 82`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 26`, `dead_code: 10`, `orphaned_logic: 3`
* *Architecture:* `io: 63`, `api: 83`, `concurrency: 14`, `import: 20`
* *Defense:* `safety: 173`, `doc: 2`, `test: 326`, `sync_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typing, weakref, logging, stat, collections.abc, __future__, inspect, pytest_mock...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/src/filelock/_api.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.871 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.155 IQR)
- **Top Global Matches:** file_cluster_13: 10.871, file_cluster_16: 10.904, file_cluster_0: 11.125
- **Magnitude:** 120.8 | **LOC:** 579 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.3759%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `release` (Impact: 7.6)
  * `_try_break_expired_lock` (Impact: 7.5)
    * *Intent:* """ :returns: the default polling interval, in seconds .. versionadded:: 3.24.0 """
  * `mode` (Impact: 5.4)
    * *Intent:* """ return self._context.blocking @blocking.setter def blocking(self, value: bool) -> None: """
  * `_open_mode` (Impact: 5.4)
    * *Intent:* """ self._context.blocking = value @property def poll_interval(self) -> float: """
  * `__init_subclass__` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 97`, `args: 32`, `func_start: 32`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 13`, `planned_debt: 1`, `duplicate_logic: 15`
* *Architecture:* `io: 12`, `api: 26`, `concurrency: 1`, `import: 20`
* *Defense:* `safety: 4`, `doc: 96`, `sync_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 148.061
  * `Choke Point (Betweenness):` 0.016798 | `Ripple Effect (Closeness):` 0.350725
  * `Imports (Out-Degree: 2):` typing, warnings, weakref, logging, collections.abc, __future__, inspect, pathlib...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `filelock-3.25.2/src/filelock/_async_read_write.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.777 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.448 IQR)
- **Top Global Matches:** file_cluster_13: 11.777, file_cluster_16: 11.876, file_cluster_4: 11.981
- **Magnitude:** 100.42 | **LOC:** 204 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.2249%), Tech Debt (97.1913%)
**Top Internal Functions/Classes:**
  * `read_lock` (Impact: 11.8)
  * `write_lock` (Impact: 11.8)
  * `_run` (Impact: 4.6)
  * `acquire_read` (Impact: 2.5)
    * *Intent:* """:returns: the executor (or ``None`` for the default)."""
  * `acquire_write` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 55`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `state_mutation: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 18`, `concurrency: 23`, `import: 10`
* *Defense:* `safety: 4`, `doc: 55`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.57
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.043478
  * `Imports (Out-Degree: 2):` collections.abc, concurrent, __future__, typing, ._read_write, os, types, contextlib...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `filelock-3.25.2/tests/test_self_deadlock.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.036 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.992 IQR)
- **Top Global Matches:** file_cluster_0: 11.036, file_cluster_13: 11.245, file_cluster_16: 11.286
- **Magnitude:** 75.62 | **LOC:** 140 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.9108%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_symlink_same_canonical_path` (Impact: 7.4)
  * `test_same_thread_different_instances_rai` (Impact: 7.3)
  * `test_force_release_cleans_registry` (Impact: 5.7)
  * `test_singleton_avoids_deadlock` (Impact: 5.6)
  * `test_finite_timeout_gives_timeout_not_de` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 46`, `args: 11`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `orphaned_logic: 10`
* *Architecture:* `io: 2`, `api: 11`, `concurrency: 1`, `import: 7`
* *Defense:* `safety: 14`, `test: 37`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, typing, sys, filelock, pytest, threading, pathlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/tests/test_lock_expiry.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.035 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.566 IQR)
- **Top Global Matches:** file_cluster_13: 11.035, file_cluster_0: 11.076, file_cluster_16: 11.136
- **Magnitude:** 73.78 | **LOC:** 145 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.9435%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_lifetime_singleton_mismatch` (Impact: 6.3)
  * `test_lock_mtime_updated_on_acquire` (Impact: 5.5)
  * `test_async_expired_lock_is_broken` (Impact: 5.0)
  * `test_async_soft_non_expired_lock_not_bro` (Impact: 4.9)
  * `test_soft_lifetime_none_no_expiry` (Impact: 4.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 47`, `args: 13`, `func_start: 13`
* *Risk/State:* `orphaned_logic: 13`
* *Architecture:* `io: 7`, `api: 13`, `concurrency: 6`, `import: 10`
* *Defense:* `safety: 12`, `test: 41`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, typing, os, filelock, pytest_mock, time, pytest, pathlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/src/filelock/_soft.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.597 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.046 IQR)
- **Top Global Matches:** file_cluster_13: 9.597, file_cluster_8: 9.952, file_cluster_0: 10.108
- **Magnitude:** 70.7 | **LOC:** 128 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.6754%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_acquire` (Impact: 16.7)
  * `_is_process_alive` (Impact: 12.9)
  * `_windows_unlink_with_retry` (Impact: 11.1)
  * `_try_break_stale_lock` (Impact: 9.4)
  * `_release` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 39`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 19`, `api: 4`, `import: 11`
* *Defense:* `safety: 8`, `doc: 2`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 36.833
  * `Choke Point (Betweenness):` 0.001976 | `Ripple Effect (Closeness):` 0.13913
  * `Imports (Out-Degree: 2):` socket, __future__, ._util, sys, os, ctypes, errno, time...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `filelock-3.25.2/src/filelock/asyncio.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.383 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.157 IQR)
- **Top Global Matches:** file_cluster_13: 10.383, file_cluster_16: 10.509, file_cluster_8: 10.656
- **Magnitude:** 66.7 | **LOC:** 377 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.7442%), Tech Debt (92.4142%)
**Top Internal Functions/Classes:**
  * `__aenter__` (Impact: 2.1)
  * `run_in_executor` (Impact: 1.9)
    * *Intent:* """ self._is_thread_local = thread_local self._is_singleton = is_singleton # Create the context. Not...
  * `executor` (Impact: 1.9)
    * *Intent:* # Create the context. Note that external code should not work with the context directly and should i...
  * `executor` (Impact: 1.9)
  * `loop` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 78`, `args: 16`, `func_start: 16`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 3`, `duplicate_logic: 4`
* *Architecture:* `io: 4`, `api: 15`, `concurrency: 27`, `import: 21`
* *Defense:* `safety: 4`, `doc: 65`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 40.043
  * `Choke Point (Betweenness):` 0.012846 | `Ripple Effect (Closeness):` 0.130435
  * `Imports (Out-Degree: 5):` typing, logging, ._api, collections.abc, concurrent, __future__, inspect, dataclasses...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `filelock-3.25.2/src/filelock/_unix.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.76 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.748 IQR)
- **Top Global Matches:** file_cluster_13: 10.76, file_cluster_8: 11.279, file_cluster_4: 11.313
- **Magnitude:** 58.48 | **LOC:** 117 | **CtrlFlow:** 40.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.4802%), Tech Debt (99.9955%)
**Top Internal Functions/Classes:**
  * `_acquire` (Impact: 30.1)
  * `_release` (Impact: 5.6)
  * `_fallback_to_soft_lock` (Impact: 5.5)
  * `_acquire` (Impact: 1.8)
  * `_release` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 34`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 3`, `duplicate_logic: 4`
* *Architecture:* `io: 15`, `api: 3`, `concurrency: 6`, `import: 13`
* *Defense:* `safety: 11`, `doc: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 30.378
  * `Choke Point (Betweenness):` 0.001976 | `Ripple Effect (Closeness):` 0.097826
  * `Imports (Out-Degree: 4):` __future__, typing, fcntl, ._util, sys, os, warnings, errno...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `filelock-3.25.2/tests/test_soft_stale.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.714 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.616 IQR)
- **Top Global Matches:** file_cluster_13: 9.714, file_cluster_0: 9.72, file_cluster_8: 9.859
- **Magnitude:** 58.28 | **LOC:** 143 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.0296%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_stale_lock_not_broken_different_hos` (Impact: 4.4)
  * `test_lock_writes_pid_and_hostname` (Impact: 4.3)
  * `test_stale_lock_not_broken_when_process_` (Impact: 4.3)
  * `test_stale_lock_empty_file_ignored` (Impact: 4.3)
  * `test_stale_lock_malformed_content_ignore` (Impact: 4.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 33`, `args: 11`, `func_start: 11`
* *Risk/State:* `orphaned_logic: 11`
* *Architecture:* `io: 18`, `api: 11`, `import: 11`
* *Defense:* `safety: 4`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` socket, __future__, typing, sys, os, errno, filelock, pytest_mock...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/tests/test_default_mode.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.781 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.45 IQR)
- **Top Global Matches:** file_cluster_0: 11.781, file_cluster_13: 11.923, file_cluster_16: 11.975
- **Magnitude:** 56.98 | **LOC:** 140 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.8157%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_explicit_mode_overrides_umask` (Impact: 6.8)
  * `test_singleton_default_vs_explicit_mode_` (Impact: 6.3)
  * `test_default_mode_respects_umask` (Impact: 5.9)
  * `test_default_mode_skips_fchmod` (Impact: 2.2)
  * `test_explicit_mode_calls_fchmod` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 55`, `args: 14`, `func_start: 14`
* *Risk/State:* `orphaned_logic: 14`
* *Architecture:* `io: 10`, `api: 14`, `import: 10`
* *Defense:* `safety: 20`, `test: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` filelock._api, __future__, typing, sys, os, filelock, pytest, stat...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/tests/test_unix_fallback.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.431 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.989 IQR)
- **Top Global Matches:** file_cluster_0: 10.431, file_cluster_13: 10.517, file_cluster_8: 10.762
- **Magnitude:** 40.36 | **LOC:** 114 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.73%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_fallback_reentrant_locking` (Impact: 5.6)
  * `test_fallback_emits_warning` (Impact: 5.5)
  * `test_release_suppresses_eio_on_close` (Impact: 4.2)
  * `_close_eio` (Impact: 4.2)
  * `test_fallback_writes_pid_and_hostname` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 35`, `args: 8`, `func_start: 8`
* *Risk/State:* `orphaned_logic: 7`
* *Architecture:* `io: 7`, `api: 7`, `import: 11`
* *Defense:* `safety: 10`, `test: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` socket, __future__, typing, sys, os, errno, filelock, pytest_mock...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/src/filelock/_windows.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.62 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.636 IQR)
- **Top Global Matches:** file_cluster_13: 9.62, file_cluster_8: 9.967, file_cluster_16: 10.102
- **Magnitude:** 35.88 | **LOC:** 112 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.3087%), Tech Debt (99.9997%)
**Top Internal Functions/Classes:**
  * `_acquire` (Impact: 15.3)
  * `_is_reparse_point` (Impact: 8.7)
    * *Intent:* """ Check if a path is a reparse point (symlink, junction, etc.) on Windows. :param path: Path to ch...
  * `_release` (Impact: 3.9)
  * `_acquire` (Impact: 1.8)
  * `_release` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 33`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 8`, `api: 3`, `import: 12`
* *Defense:* `safety: 4`, `doc: 9`, `sync_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 30.378
  * `Choke Point (Betweenness):` 0.001976 | `Ripple Effect (Closeness):` 0.115942
  * `Imports (Out-Degree: 2):` __future__, typing, msvcrt, ._util, sys, os, ctypes, errno...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `filelock-3.25.2/src/filelock/_util.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.172 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.42 IQR)
- **Top Global Matches:** file_cluster_13: 14.172, file_cluster_0: 14.778, file_cluster_16: 14.825
- **Magnitude:** 21.0 | **LOC:** 54 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.5936%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `raise_on_not_writable_file` (Impact: 14.9)
    * *Intent:* """ Raise an exception if attempting to open the file for writing would fail. This is done so files ...
  * `ensure_directory_exists` (Impact: 2.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 12`, `args: 2`, `func_start: 2`
* *Risk/State:* `dead_code: 1`
* *Architecture:* `io: 3`, `api: 3`, `import: 6`
* *Defense:* `safety: 2`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 56.557
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.156522
  * `Imports (Out-Degree: 0):` __future__, sys, os, errno, stat, pathlib
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `filelock-3.25.2/src/filelock/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.565 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.829 IQR)
- **Top Global Matches:** file_cluster_8: 7.565, file_cluster_13: 7.583, file_cluster_16: 8.144
- **Magnitude:** 18.24 | **LOC:** 83 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.4962%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 28`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 1`, `import: 13`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 21.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` __future__, typing, ._read_write, ._soft, sys, warnings, ._windows, .asyncio...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/src/filelock/_error.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.551 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.04 IQR)
- **Top Global Matches:** file_cluster_16: 10.551, file_cluster_13: 10.844, file_cluster_8: 11.236
- **Magnitude:** 16.56 | **LOC:** 31 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.4471%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 1.9)
  * `lock_file` (Impact: 1.9)
  * `__reduce__` (Impact: 1.8)
  * `__str__` (Impact: 1.8)
  * `__repr__` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 14`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 157.664
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.313043
  * `Imports (Out-Degree: 0):` typing, __future__
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `filelock-3.25.2/src/filelock/version.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.333 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.501 IQR)
- **Top Global Matches:** file_cluster_8: 5.333, file_cluster_16: 6.278, file_cluster_13: 6.407
- **Magnitude:** 16.52 | **LOC:** 35 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.4353%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 4`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.57
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.043478
  * `Imports (Out-Degree: 0):` typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `filelock-3.25.2/tests/test_error.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.886 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.53 IQR)
- **Top Global Matches:** file_cluster_13: 12.886, file_cluster_16: 12.946, file_cluster_8: 13.036
- **Magnitude:** 12.18 | **LOC:** 31 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.5253%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_timeout_pickle` (Impact: 2.1)
  * `test_timeout_str` (Impact: 1.9)
  * `test_timeout_repr` (Impact: 1.9)
  * `test_timeout_lock_file` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 16`, `args: 4`, `func_start: 4`
* *Risk/State:* `orphaned_logic: 4`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 7`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pickle, filelock, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/tests/test_virtualenv.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.537 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.236 IQR)
- **Top Global Matches:** file_cluster_13: 9.537, file_cluster_0: 10.135, file_cluster_8: 10.193
- **Magnitude:** 3.36 | **LOC:** 19 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_virtualenv` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 11`, `args: 1`, `func_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 6`
* *Defense:* `safety: 1`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, typing, virtualenv, sys, pytest, pathlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `filelock-3.25.2/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 21.536
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `filelock-3.25.2/tests/test_read_write_unit.py` (PYTHON) | Magnitude: 347.86 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 369, test: 165, structural_boundaries: 143, encapsulation: 91
- `filelock-3.25.2/tests/test_async_filelock.py` (PYTHON) | Magnitude: 188.76 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 187, structural_boundaries: 142, test: 127, concurrency: 89
- `filelock-3.25.2/tests/test_read_write.py` (PYTHON) | Magnitude: 219.8 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 312, structural_boundaries: 122, test: 102, safety: 69
- `filelock-3.25.2/tests/test_unix_fallback.py` (PYTHON) | Magnitude: 40.36 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 35, test: 32, encapsulation: 20
- `filelock-3.25.2/tests/test_default_mode.py` (PYTHON) | Magnitude: 56.98 | Delta: **0.142 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 65, structural_boundaries: 55, test: 45, generics: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `filelock-3.25.2/tests/test_soft_stale.py` (PYTHON) | Magnitude: 58.28 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 33, test: 33, io: 18
- `filelock-3.25.2/src/filelock/_api.py` (PYTHON) | Magnitude: 120.8 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 276, structural_boundaries: 97, doc: 96, encapsulation: 94
- `filelock-3.25.2/tests/test_lock_expiry.py` (PYTHON) | Magnitude: 73.78 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 73, structural_boundaries: 47, test: 41, generics: 17
- `filelock-3.25.2/tests/test_error.py` (PYTHON) | Magnitude: 12.18 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 16, indent_spaces: 12, test: 11, safety: 7
- `filelock-3.25.2/src/filelock/_async_read_write.py` (PYTHON) | Magnitude: 100.42 | Delta: **0.099 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 55, doc: 55, encapsulation: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `filelock-3.25.2/src/filelock/_error.py` (PYTHON) | Magnitude: 16.56 | Delta: **0.293 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 14, encapsulation: 14, indent_spaces: 13, api: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `filelock-3.25.2/tests/test_async_read_write.py` (PYTHON) | Magnitude: 268.88 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 156, structural_boundaries: 126, test: 110, encapsulation: 96

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `filelock-3.25.2/src/filelock/__init__.py` (PYTHON) | Magnitude: 18.24 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 28, encapsulation: 19, import: 13

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `filelock-3.25.2/src/filelock/_read_write.py` -> **Severity: 1.38** (Bridge: 0.0138 * Flux: 99.72%)
- `filelock-3.25.2/src/filelock/_api.py` -> **Severity: 0.605** (Bridge: 0.0168 * Flux: 36.0065%)
- `filelock-3.25.2/src/filelock/asyncio.py` -> **Severity: 0.197** (Bridge: 0.0128 * Flux: 15.3349%)
- `filelock-3.25.2/src/filelock/_unix.py` -> **Severity: 0.059** (Bridge: 0.002 * Flux: 29.9133%)
- `filelock-3.25.2/src/filelock/_soft.py` -> **Severity: 0.05** (Bridge: 0.002 * Flux: 25.3506%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `filelock-3.25.2/src/filelock/_error.py` -> **Severity: 25.043** (Embedded: 0.313 * Error Risk: 80.0%)
- `filelock-3.25.2/src/filelock/_read_write.py` -> **Severity: 19.732** (Embedded: 0.3288 * Error Risk: 60.0111%)
- `filelock-3.25.2/src/filelock/_api.py` -> **Severity: 19.131** (Embedded: 0.3507 * Error Risk: 54.5474%)
- `filelock-3.25.2/src/filelock/asyncio.py` -> **Severity: 6.598** (Embedded: 0.1304 * Error Risk: 50.5869%)
- `filelock-3.25.2/src/filelock/_windows.py` -> **Severity: 5.635** (Embedded: 0.1159 * Error Risk: 48.6015%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `filelock-3.25.2/src/filelock/_error.py` -> **Severity: 15509.96** (Blast Radius: 157.664 * Doc Risk: 98.3735%)
- `filelock-3.25.2/src/filelock/_read_write.py` -> **Severity: 2450.264** (Blast Radius: 151.435 * Doc Risk: 16.1803%)
- `filelock-3.25.2/src/filelock/_util.py` -> **Severity: 2033.92** (Blast Radius: 56.557 * Doc Risk: 35.9623%)
- `filelock-3.25.2/src/filelock/_api.py` -> **Severity: 1764.932** (Blast Radius: 148.061 * Doc Risk: 11.9203%)
- `filelock-3.25.2/src/filelock/_soft.py` -> **Severity: 1215.029** (Blast Radius: 36.833 * Doc Risk: 32.9875%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
