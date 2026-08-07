# ARCHITECTURAL_BRIEF: aiohappyeyeballs
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/aiohappyeyeballs` |
| **Timestamp** | `2026-08-07T05:21:06.898439+00:00` |
| **Scan Duration** | `0.18s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 13 malicious artifacts.

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
| Total Artifacts | 19 |
| Analyzed Artifacts (Scanned) | 14 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 2581 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 73.7% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.42 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5309 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.5333 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 13 | 2581 | 92.9% |
| MARKDOWN | 1 | 0 | 7.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.059`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 5 | 35.7% |
| file_cluster_4 | 3 | 21.4% |
| file_cluster_13 | 3 | 21.4% |
| file_cluster_16 | 2 | 14.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 7.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 42 exceeds 500 chars)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 1.6 | 48.9 | 19.8 | 16.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.5 | 23.5 | 6.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 2.3 | 0.6 | 0.0 | 0.0 |
| API Exposure | 0.0 | 9.5 | 4.3 | 5.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 46.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 22.5 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 77.9 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 49.8 | 9.9 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `aiohappyeyeballs-2.6.1/tests/test_impl.py` (Hits: 490)
- `aiohappyeyeballs-2.6.1/tests/test_utils.py` (Hits: 46)
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py` (Hits: 13)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **types.py** (`aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/types.py`) — 5 inbound connections
2. **_staggered.py** (`aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/_staggered.py`) — 3 inbound connections
3. **impl.py** (`aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py`) — 1 inbound connections
4. **utils.py** (`aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/utils.py`) — 1 inbound connections
5. **README.md** (`aiohappyeyeballs-2.6.1/README.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **impl.py** (`aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py`) — 9 outbound dependencies
2. **test_impl.py** (`aiohappyeyeballs-2.6.1/tests/test_impl.py`) — 7 outbound dependencies
3. **test_staggered.py** (`aiohappyeyeballs-2.6.1/tests/test_staggered.py`) — 7 outbound dependencies
4. **utils.py** (`aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/utils.py`) — 4 outbound dependencies
5. **test_staggered_cpython_eager_task_factory.py** (`aiohappyeyeballs-2.6.1/tests/test_staggered_cpython_eager_task_factory.py`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `mock_socket_module` (@ `aiohappyeyeballs-2.6.1/tests/test_impl.py`) -> Impact: **8.1** | LOC: 23
- `test_single_addr_info_errors` (@ `aiohappyeyeballs-2.6.1/tests/test_impl.py`) -> Impact: **7.8** | LOC: 21
- `set_event_loop` (@ `aiohappyeyeballs-2.6.1/tests/test_staggered_cpython_eager_task_factory.py`) -> Impact: **7.1** | LOC: 7
- `test_remove_addr_infos_slow_path` (@ `aiohappyeyeballs-2.6.1/tests/test_utils.py`) -> Impact: **7.1** | LOC: 39
- `test_none_successful` (@ `aiohappyeyeballs-2.6.1/tests/test_staggered_cpython.py`) -> Impact: **7.0** | LOC: 19
- `test_single_addr_success_passing_loop` (@ `aiohappyeyeballs-2.6.1/tests/test_impl.py`) -> Impact: **5.8** | LOC: 27
- `test_single_addr_success` (@ `aiohappyeyeballs-2.6.1/tests/test_impl.py`) -> Impact: **5.7** | LOC: 24
- `test_single_addr_socket_factory` (@ `aiohappyeyeballs-2.6.1/tests/test_impl.py`) -> Impact: **5.6** | LOC: 23
- `_socket` (@ `aiohappyeyeballs-2.6.1/tests/test_impl.py`) -> Impact: **5.5** | LOC: 6
- `_socket` (@ `aiohappyeyeballs-2.6.1/tests/test_impl.py`) -> Impact: **5.5** | LOC: 6

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `aiohappyeyeballs-2.6.1/tests` | 8 | 836.26 | 15.43% | 0.0% |
| `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs` | 5 | 193.78 | 26.75% | 0.0% |
| `aiohappyeyeballs-2.6.1` | 1 | 1.94 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest State Flux (Mutation/Volatility)
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/utils.py` -> **99.9615%** Exposure
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py` -> **99.6584%** Exposure
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/_staggered.py` -> **92.5532%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `aiohappyeyeballs-2.6.1/tests/test_impl.py` -> **30** Orphaned Functions | **48** Duplicates
- `aiohappyeyeballs-2.6.1/tests/test_staggered_cpython.py` -> **8** Orphaned Functions | **6** Duplicates
- `aiohappyeyeballs-2.6.1/tests/test_staggered_cpython_eager_task_factory.py` -> **4** Orphaned Functions | **4** Duplicates
- `aiohappyeyeballs-2.6.1/tests/test_staggered.py` -> **4** Orphaned Functions | **3** Duplicates
- `aiohappyeyeballs-2.6.1/tests/test_utils.py` -> **4** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py`** -> AI Confidence: **99.31%**
2. **`aiohappyeyeballs-2.6.1/tests/test_impl.py`** -> AI Confidence: **99.18%**
3. **`aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/_staggered.py`** -> AI Confidence: **99.09%**
4. **`aiohappyeyeballs-2.6.1/tests/test_staggered.py`** -> AI Confidence: **99.08%**
5. **`aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/utils.py`** -> AI Confidence: **99.06%**
6. **`aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/__init__.py`** -> AI Confidence: **98.88%**
7. **`aiohappyeyeballs-2.6.1/tests/test_types.py`** -> AI Confidence: **98.88%**
8. **`aiohappyeyeballs-2.6.1/tests/test_staggered_cpython.py`** -> AI Confidence: **98.87%**
9. **`aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/types.py`** -> AI Confidence: **98.84%**
10. **`aiohappyeyeballs-2.6.1/tests/__init__.py`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `44` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py` (PYTHON) -> Cumulative Risk: **470.03**
- **Archetype:** `file_cluster_13` (Distance: 12.237 IQR)
- **Magnitude:** 64.52 | **LOC:** 260 | **CtrlFlow:** 65.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.6584%), Concurrency (99.6084%), Safety Score (57.6922%)
- **Heaviest Functions:** `start_connection` (Impact: 1.4), `_connect_sock` (Impact: 1.4), `_interleave_addrinfos` (Impact: 1.1)

### 2. `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/_staggered.py` (PYTHON) -> Cumulative Risk: **461.2**
- **Archetype:** `file_cluster_4` (Distance: 11.408 IQR)
- **Magnitude:** 67.9 | **LOC:** 208 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (92.5532%), Safety Score (57.1262%)
- **Heaviest Functions:** `_set_result` (Impact: 4.2), `_on_completion` (Impact: 4.2), `staggered_race` (Impact: 1.2)

### 3. `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/utils.py` (PYTHON) -> Cumulative Risk: **408.24**
- **Archetype:** `file_cluster_16` (Distance: 10.885 IQR)
- **Magnitude:** 29.92 | **LOC:** 98 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9615%), Safety Score (80.5476%), Stability (50.0%)
- **Heaviest Functions:** `addr_to_addr_infos` (Impact: 1.2), `pop_addr_infos_interleave` (Impact: 1.1), `_addr_tuple_to_ip_address` (Impact: 1.1)

### 4. `aiohappyeyeballs-2.6.1/tests/test_staggered_cpython_eager_task_factory.py` (PYTHON) -> Cumulative Risk: **338.74**
- **Archetype:** `file_cluster_4` (Distance: 10.637 IQR)
- **Magnitude:** 84.36 | **LOC:** 97 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Stability (50.0%), Safety Score (42.3226%)
- **Heaviest Functions:** `set_event_loop` (Impact: 7.1), `setUp` (Impact: 3.9), `test_staggered_race_with_eager_tasks` (Impact: 2.9)

### 5. `aiohappyeyeballs-2.6.1/tests/test_impl.py` (PYTHON) -> Cumulative Risk: **306.92**
- **Archetype:** `file_cluster_8` (Distance: 10.282 IQR)
- **Magnitude:** 480.98 | **LOC:** 2017 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.5246%), Stability (50.0%), Safety Score (38.4349%)
- **Heaviest Functions:** `mock_socket_module` (Impact: 8.1), `test_single_addr_info_errors` (Impact: 7.8), `test_single_addr_success_passing_loop` (Impact: 5.8)

### 6. `aiohappyeyeballs-2.6.1/tests/test_staggered.py` (PYTHON) -> Cumulative Risk: **290.13**
- **Archetype:** `file_cluster_4` (Distance: 12.407 IQR)
- **Magnitude:** 126.1 | **LOC:** 102 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Stability (50.0%), Cognitive Load (24.9999%)
- **Heaviest Functions:** `test_multiple_winners` (Impact: 5.2), `test_one_winners` (Impact: 5.0), `test_multiple_winners_eager_task_factory` (Impact: 5.0)

### 7. `aiohappyeyeballs-2.6.1/tests/test_staggered_cpython.py` (PYTHON) -> Cumulative Risk: **287.54**
- **Archetype:** `file_cluster_8` (Distance: 9.004 IQR)
- **Magnitude:** 102.1 | **LOC:** 147 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Stability (50.0%), Cognitive Load (27.9893%)
- **Heaviest Functions:** `test_none_successful` (Impact: 7.0), `test_long_delay_early_failure` (Impact: 5.1), `test_first_error_second_successful` (Impact: 5.0)

### 8. `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/__init__.py` (PYTHON) -> Cumulative Risk: **188.3**
- **Archetype:** `file_cluster_8` (Distance: 5.884 IQR)
- **Magnitude:** 16.24 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (80.0%), Stability (50.0%), Documentation (49.7967%), Cognitive Load (5.0%)

### 9. `aiohappyeyeballs-2.6.1/tests/test_utils.py` (PYTHON) -> Cumulative Risk: **179.89**
- **Archetype:** `file_cluster_8` (Distance: 8.98 IQR)
- **Magnitude:** 26.22 | **LOC:** 186 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Safety Score (22.1244%), Api Exposure (6.1533%)
- **Heaviest Functions:** `test_remove_addr_infos_slow_path` (Impact: 7.1), `test_addr_to_addr_infos` (Impact: 4.7), `test_pop_addr_infos_interleave` (Impact: 3.5)

### 10. `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/types.py` (PYTHON) -> Cumulative Risk: **135.22**
- **Archetype:** `file_cluster_16` (Distance: 8.19 IQR)
- **Magnitude:** 15.2 | **LOC:** 18 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (66.6667%), Stability (50.0%), Documentation (12.0248%), Cognitive Load (5.0%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `aiohappyeyeballs-2.6.1/tests/test_impl.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.282 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.959 IQR)
- **Top Global Matches:** file_cluster_8: 10.282, file_cluster_0: 10.464, file_cluster_4: 10.591
- **Magnitude:** 480.98 | **LOC:** 2017 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.4074%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mock_socket_module` (Impact: 8.1)
  * `test_single_addr_info_errors` (Impact: 7.8)
  * `test_single_addr_success_passing_loop` (Impact: 5.8)
  * `test_single_addr_success` (Impact: 5.7)
  * `test_single_addr_socket_factory` (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 265`, `args: 82`, `func_start: 82`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 57`, `duplicate_logic: 48`, `orphaned_logic: 30`
* *Architecture:* `io: 490`, `api: 36`, `concurrency: 162`, `import: 7`
* *Defense:* `safety: 56`, `doc: 18`, `test: 160`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 46.989
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` socket, aiohappyeyeballs, asyncio, types, unittest, pytest, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohappyeyeballs-2.6.1/tests/test_staggered.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.407 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.934 IQR)
- **Top Global Matches:** file_cluster_4: 12.407, file_cluster_13: 13.003, file_cluster_0: 13.208
- **Magnitude:** 126.1 | **LOC:** 102 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.9999%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_multiple_winners` (Impact: 5.2)
  * `test_one_winners` (Impact: 5.0)
    * *Intent:* """Test that there is only one winner when there is no await in the coro."""
  * `test_multiple_winners_eager_task_factory` (Impact: 5.0)
  * `run` (Impact: 5.0)
  * `coro` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 48`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`, `duplicate_logic: 3`, `orphaned_logic: 4`
* *Architecture:* `io: 1`, `api: 8`, `concurrency: 85`, `import: 7`
* *Defense:* `safety: 17`, `doc: 8`, `test: 25`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 46.989
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` functools, asyncio, collections.abc, sys, pytest, aiohappyeyeballs._staggered, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohappyeyeballs-2.6.1/tests/test_staggered_cpython.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.004 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.671 IQR)
- **Top Global Matches:** file_cluster_8: 9.004, file_cluster_4: 9.512, file_cluster_7: 9.655
- **Magnitude:** 102.1 | **LOC:** 147 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.9893%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_none_successful` (Impact: 7.0)
  * `test_long_delay_early_failure` (Impact: 5.1)
  * `test_first_error_second_successful` (Impact: 5.0)
  * `test_first_timeout_second_successful` (Impact: 5.0)
  * `coro` (Impact: 4.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 35`, `args: 25`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `duplicate_logic: 6`, `orphaned_logic: 8`
* *Architecture:* `api: 16`, `concurrency: 31`, `import: 3`
* *Defense:* `doc: 2`, `test: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 46.989
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unittest, asyncio, aiohappyeyeballs._staggered
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohappyeyeballs-2.6.1/tests/test_staggered_cpython_eager_task_factory.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.637 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.753 IQR)
- **Top Global Matches:** file_cluster_4: 10.637, file_cluster_8: 11.068, file_cluster_13: 11.069
- **Magnitude:** 84.36 | **LOC:** 97 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.4676%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `set_event_loop` (Impact: 7.1)
  * `setUp` (Impact: 3.9)
  * `test_staggered_race_with_eager_tasks` (Impact: 2.9)
  * `run` (Impact: 2.8)
    * *Intent:* # See https://github.com/python/cpython/issues/124309
  * `test_staggered_race_with_eager_tasks_no_` (Impact: 2.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 22`, `args: 17`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`, `duplicate_logic: 4`, `orphaned_logic: 4`
* *Architecture:* `io: 2`, `api: 12`, `concurrency: 35`, `import: 4`
* *Defense:* `safety: 2`, `doc: 2`, `test: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 46.989
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unittest, sys, asyncio, aiohappyeyeballs._staggered
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/_staggered.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.408 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.649 IQR)
- **Top Global Matches:** file_cluster_4: 11.408, file_cluster_16: 11.418, file_cluster_8: 11.679
- **Magnitude:** 67.9 | **LOC:** 208 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.8623%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_set_result` (Impact: 4.2)
    * *Intent:* """Set the result of a future if it is not already done."""
  * `_on_completion` (Impact: 4.2)
  * `staggered_race` (Impact: 1.2)
  * `run_one_coro` (Impact: 1.2)
  * `_wait_one` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 22`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 12`
* *Architecture:* `api: 3`, `concurrency: 39`, `import: 3`
* *Defense:* `safety: 9`, `doc: 8`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 166.811
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.230769
  * `Imports (Out-Degree: 0):` contextlib, typing, asyncio
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.237 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.1 IQR)
- **Top Global Matches:** file_cluster_13: 12.237, file_cluster_4: 12.303, file_cluster_16: 12.404
- **Magnitude:** 64.52 | **LOC:** 260 | **CtrlFlow:** 65.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.9674%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `start_connection` (Impact: 1.4)
  * `_connect_sock` (Impact: 1.4)
    * *Intent:* # Raise a combined exception so the user can see all # the various error messages.
  * `_interleave_addrinfos` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 31`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 36`
* *Architecture:* `io: 13`, `api: 2`, `concurrency: 19`, `import: 9`
* *Defense:* `safety: 20`, `doc: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 60.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.076923
  * `Imports (Out-Degree: 1):` functools, socket, collections, asyncio, itertools, , .types, contextlib...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.885 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.77 IQR)
- **Top Global Matches:** file_cluster_16: 10.885, file_cluster_13: 11.142, file_cluster_8: 11.374
- **Magnitude:** 29.92 | **LOC:** 98 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.9328%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addr_to_addr_infos` (Impact: 1.2)
  * `pop_addr_infos_interleave` (Impact: 1.1)
    * *Intent:* """ Pop addr_info from the list of addr_infos by family up to interleave times. The interleave param...
  * `_addr_tuple_to_ip_address` (Impact: 1.1)
  * `remove_addr_infos` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 15`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 18`
* *Architecture:* `io: 5`, `api: 6`, `import: 4`
* *Defense:* `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 60.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.076923
  * `Imports (Out-Degree: 1):` typing, ipaddress, .types, socket
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `aiohappyeyeballs-2.6.1/tests/test_utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.98 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.432 IQR)
- **Top Global Matches:** file_cluster_8: 8.98, file_cluster_13: 9.642, file_cluster_7: 9.647
- **Magnitude:** 26.22 | **LOC:** 186 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (1.6139%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_remove_addr_infos_slow_path` (Impact: 7.1)
  * `test_addr_to_addr_infos` (Impact: 4.7)
  * `test_pop_addr_infos_interleave` (Impact: 3.5)
    * *Intent:* """Test pop_addr_infos_interleave."""
  * `test_remove_addr_infos` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 27`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `orphaned_logic: 4`
* *Architecture:* `io: 46`, `api: 4`, `import: 4`
* *Defense:* `safety: 17`, `doc: 8`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 46.989
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typing, pytest, socket, aiohappyeyeballs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 5.884 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.934 IQR)
- **Top Global Matches:** file_cluster_8: 5.884, file_cluster_13: 6.281, file_cluster_7: 7.12
- **Magnitude:** 16.24 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 46.989
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .types, .utils, .impl
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/types.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_16` (Drift: 8.19 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.815 IQR)
- **Top Global Matches:** file_cluster_16: 8.19, file_cluster_13: 8.405, file_cluster_8: 8.427
- **Magnitude:** 15.2 | **LOC:** 18 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* None
* *Architecture:* `io: 5`, `import: 2`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 242.698
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.384615
  * `Imports (Out-Degree: 0):` typing, socket
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `aiohappyeyeballs-2.6.1/tests/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.581 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 46.989
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohappyeyeballs-2.6.1/tests/test_types.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.094 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.614 IQR)
- **Top Global Matches:** file_cluster_13: 13.094, file_cluster_8: 13.6, file_cluster_7: 13.858
- **Magnitude:** 3.12 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_callable_import_from_typing` (Impact: 2.0)
    * *Intent:* """ Test that Callable is imported from typing. PY3.9: https://github.com/python/cpython/issues/8713...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `args: 1`, `func_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 2`, `doc: 2`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 46.989
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` collections.abc, typing, aiohappyeyeballs.types
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohappyeyeballs-2.6.1/tests/test_init.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.669 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.775 IQR)
- **Top Global Matches:** file_cluster_13: 12.669, file_cluster_8: 12.927, file_cluster_0: 13.483
- **Magnitude:** 2.86 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_init` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`, `args: 1`, `func_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `safety: 1`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 46.989
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` aiohappyeyeballs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aiohappyeyeballs-2.6.1/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.94 | **LOC:** 97 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 46.989
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py` (PYTHON) | Magnitude: 64.52 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 166, branch: 59, state_mutation: 36, structural_boundaries: 31
- `aiohappyeyeballs-2.6.1/tests/test_init.py` (PYTHON) | Magnitude: 2.86 | Delta: **0.258 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, test: 2, args: 1, func_start: 1
- `aiohappyeyeballs-2.6.1/tests/test_types.py` (PYTHON) | Magnitude: 3.12 | Delta: **0.506 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 11, test: 3, import: 3, safety: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/types.py` (PYTHON) | Magnitude: 15.2 | Delta: **0.215 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: io: 5, indent_spaces: 5, structural_boundaries: 3, generics: 3
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/utils.py` (PYTHON) | Magnitude: 29.92 | Delta: **0.257 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 58, generics: 20, branch: 18, state_mutation: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/_staggered.py` (PYTHON) | Magnitude: 67.9 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 89, concurrency: 39, branch: 26, structural_boundaries: 22
- `aiohappyeyeballs-2.6.1/tests/test_staggered_cpython_eager_task_factory.py` (PYTHON) | Magnitude: 84.36 | Delta: **0.431 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 61, concurrency: 35, structural_boundaries: 22, args: 17
- `aiohappyeyeballs-2.6.1/tests/test_staggered.py` (PYTHON) | Magnitude: 126.1 | Delta: **0.596 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: concurrency: 85, indent_spaces: 56, structural_boundaries: 48, test: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `aiohappyeyeballs-2.6.1/tests/test_impl.py` (PYTHON) | Magnitude: 480.98 | Delta: **0.182 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1649, io: 490, structural_boundaries: 265, concurrency: 162
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/__init__.py` (PYTHON) | Magnitude: 16.24 | Delta: **0.397 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 6, import: 3, encapsulation: 2
- `aiohappyeyeballs-2.6.1/tests/test_staggered_cpython.py` (PYTHON) | Magnitude: 102.1 | Delta: **0.508 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 104, structural_boundaries: 35, concurrency: 31, args: 25
- `aiohappyeyeballs-2.6.1/tests/test_utils.py` (PYTHON) | Magnitude: 26.22 | Delta: **0.662 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 162, io: 46, structural_boundaries: 27, test: 23

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/_staggered.py` -> **Severity: 13.183** (Embedded: 0.2308 * Error Risk: 57.1262%)
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/utils.py` -> **Severity: 6.196** (Embedded: 0.0769 * Error Risk: 80.5476%)
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py` -> **Severity: 4.438** (Embedded: 0.0769 * Error Risk: 57.6922%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/types.py` -> **Severity: 2918.395** (Blast Radius: 242.698 * Doc Risk: 12.0248%)
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/utils.py` -> **Severity: 2582.897** (Blast Radius: 60.302 * Doc Risk: 42.8327%)
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/__init__.py` -> **Severity: 2339.897** (Blast Radius: 46.989 * Doc Risk: 49.7967%)
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/_staggered.py` -> **Severity: 1988.437** (Blast Radius: 166.811 * Doc Risk: 11.9203%)
- `aiohappyeyeballs-2.6.1/src/aiohappyeyeballs/impl.py` -> **Severity: 718.818** (Blast Radius: 60.302 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
