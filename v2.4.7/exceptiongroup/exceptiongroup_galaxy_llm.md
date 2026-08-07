# ARCHITECTURAL_BRIEF: exceptiongroup
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/exceptiongroup` |
| **Timestamp** | `2026-08-07T05:22:27.275949+00:00` |
| **Scan Duration** | `0.15s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 16 malicious artifacts.

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
| Total Artifacts | 23 |
| Analyzed Artifacts (Scanned) | 16 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7 |
| Total LOC | 2373 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 69.6% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.7746 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.4667 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 16 | 2373 | 100.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.686`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 8 | 50.0% |
| file_cluster_8 | 7 | 43.8% |
| file_cluster_16 | 1 | 6.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7*

**Composition by Extension & Reason:**
- `.rst`: 2x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 4.8 | 69.1 | 15.7 | 5.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 76.9 | 28.0 | 7.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 17.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 2.3 | 0.3 | 0.0 | 0.0 |
| API Exposure | 0.0 | 9.1 | 2.9 | 1.7 | 0.0 |
| Concurrency Exposure | 0.0 | 19.2 | 1.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 96.3 | 16.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 85.8 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 85.9 | 19.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `exceptiongroup-1.3.1/tests/test_formatting.py` (Hits: 61)
- `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py` (Hits: 13)
- `exceptiongroup-1.3.1/tests/test_apport_monkeypatching.py` (Hits: 7)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **_exceptions.py** (`exceptiongroup-1.3.1/src/exceptiongroup/_exceptions.py`) — 4 inbound connections
2. **_catch.py** (`exceptiongroup-1.3.1/src/exceptiongroup/_catch.py`) — 1 inbound connections
3. **_formatting.py** (`exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py`) — 1 inbound connections
4. **_suppress.py** (`exceptiongroup-1.3.1/src/exceptiongroup/_suppress.py`) — 1 inbound connections
5. **_version.py** (`exceptiongroup-1.3.1/src/exceptiongroup/_version.py`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_formatting.py** (`exceptiongroup-1.3.1/tests/test_formatting.py`) — 12 outbound dependencies
2. **__init__.py** (`exceptiongroup-1.3.1/src/exceptiongroup/__init__.py`) — 10 outbound dependencies
3. **_formatting.py** (`exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py`) — 10 outbound dependencies
4. **_catch.py** (`exceptiongroup-1.3.1/src/exceptiongroup/_catch.py`) — 8 outbound dependencies
5. **_exceptions.py** (`exceptiongroup-1.3.1/src/exceptiongroup/_exceptions.py`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `format` (@ `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py`) -> Impact: **95.0** | LOC: 88
- `split_exception_group` (@ `exceptiongroup-1.3.1/tests/test_exceptions.py`) -> Impact: **63.1** | LOC: 63
- `_levenshtein_distance` (@ `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py`) -> Impact: **47.0** | LOC: 59
- `test_split_by_type` (@ `exceptiongroup-1.3.1/tests/test_exceptions.py`) -> Impact: **43.1** | LOC: 100
- `test_split_ExceptionGroup_subclass_deriv` (@ `exceptiongroup-1.3.1/tests/test_exceptions.py`) -> Impact: **39.5** | LOC: 62
  * *Intent:* # Match KeyboardInterrupt match, rest = self.split_exception_group(eg, KeyboardInterrupt) self.assertMatchesTemplate(match, BaseExceptionGroup, [Keybo...
- `handle_exception` (@ `exceptiongroup-1.3.1/src/exceptiongroup/_catch.py`) -> Impact: **35.1** | LOC: 44
- `_compute_suggestion_error` (@ `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py`) -> Impact: **30.1** | LOC: 47
- `test_split_ExceptionGroup_subclass_no_de` (@ `exceptiongroup-1.3.1/tests/test_exceptions.py`) -> Impact: **24.7** | LOC: 43
  * *Intent:* # Match KeyboardInterrupts
- `create_simple_eg` (@ `exceptiongroup-1.3.1/tests/test_exceptions.py`) -> Impact: **22.3** | LOC: 30
- `test_format_nested` (@ `exceptiongroup-1.3.1/tests/test_formatting.py`) -> Impact: **21.9** | LOC: 37

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `exceptiongroup-1.3.1/tests` | 10 | 1090.76 | 5.87% | 0.0% |
| `exceptiongroup-1.3.1/src/exceptiongroup` | 6 | 524.52 | 32.1% | 46.31% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `exceptiongroup-1.3.1/src/exceptiongroup/_exceptions.py` -> **100.0%** Exposure
- `exceptiongroup-1.3.1/src/exceptiongroup/_suppress.py` -> **97.7023%** Exposure
- `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py` -> **80.1565%** Exposure
### Highest State Flux (Mutation/Volatility)
- `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py` -> **96.3071%** Exposure
- `exceptiongroup-1.3.1/src/exceptiongroup/_catch.py` -> **77.3604%** Exposure
- `exceptiongroup-1.3.1/src/exceptiongroup/_exceptions.py` -> **67.7342%** Exposure
- `exceptiongroup-1.3.1/src/exceptiongroup/_suppress.py` -> **26.3084%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `exceptiongroup-1.3.1/tests/test_exceptions.py` -> **46** Orphaned Functions | **4** Duplicates
- `exceptiongroup-1.3.1/src/exceptiongroup/_exceptions.py` -> **0** Orphaned Functions | **20** Duplicates
- `exceptiongroup-1.3.1/tests/test_catch.py` -> **14** Orphaned Functions | **4** Duplicates
- `exceptiongroup-1.3.1/tests/test_catch_py311.py` -> **10** Orphaned Functions | **0** Duplicates
- `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py` -> **0** Orphaned Functions | **7** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`exceptiongroup-1.3.1/src/exceptiongroup/_catch.py`** -> AI Confidence: **99.31%**
2. **`exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py`** -> AI Confidence: **99.31%**
3. **`exceptiongroup-1.3.1/src/exceptiongroup/__init__.py`** -> AI Confidence: **99.18%**
4. **`exceptiongroup-1.3.1/tests/test_formatting.py`** -> AI Confidence: **99.16%**
5. **`exceptiongroup-1.3.1/src/exceptiongroup/_exceptions.py`** -> AI Confidence: **99.15%**
6. **`exceptiongroup-1.3.1/tests/test_exceptions.py`** -> AI Confidence: **99.13%**
7. **`exceptiongroup-1.3.1/tests/test_apport_monkeypatching.py`** -> AI Confidence: **99.07%**
8. **`exceptiongroup-1.3.1/src/exceptiongroup/_suppress.py`** -> AI Confidence: **98.96%**
9. **`exceptiongroup-1.3.1/tests/test_catch_py311.py`** -> AI Confidence: **98.92%**
10. **`exceptiongroup-1.3.1/tests/dummyscript.py`** -> AI Confidence: **98.87%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `75` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `exceptiongroup-1.3.1/src/exceptiongroup/_exceptions.py` (PYTHON) -> Cumulative Risk: **499.87**
- **Archetype:** `file_cluster_16` (Distance: 10.308 IQR)
- **Magnitude:** 99.16 | **LOC:** 337 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (85.9039%), State Flux (67.7342%)
- **Heaviest Functions:** `add_note` (Impact: 5.7), `__str__` (Impact: 5.3), `_derive_and_copy_attributes` (Impact: 3.9)

### 2. `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py` (PYTHON) -> Cumulative Risk: **483.91**
- **Archetype:** `file_cluster_13` (Distance: 11.001 IQR)
- **Magnitude:** 323.34 | **LOC:** 603 | **CtrlFlow:** 60.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (96.3071%), Tech Debt (80.1565%), Cognitive Load (69.1031%)
- **Heaviest Functions:** `format` (Impact: 95.0), `_levenshtein_distance` (Impact: 47.0), `_compute_suggestion_error` (Impact: 30.1)

### 3. `exceptiongroup-1.3.1/src/exceptiongroup/_suppress.py` (PYTHON) -> Cumulative Risk: **434.28**
- **Archetype:** `file_cluster_13` (Distance: 9.58 IQR)
- **Magnitude:** 10.44 | **LOC:** 56 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (97.7023%), Safety Score (76.875%), Documentation (71.6236%)
- **Heaviest Functions:** `__init__` (Impact: 1.8), `__enter__` (Impact: 1.8), `__exit__` (Impact: 1.2)

### 4. `exceptiongroup-1.3.1/src/exceptiongroup/_catch.py` (PYTHON) -> Cumulative Risk: **403.79**
- **Archetype:** `file_cluster_13` (Distance: 11.159 IQR)
- **Magnitude:** 58.28 | **LOC:** 139 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (77.3604%), Safety Score (73.8596%), Cognitive Load (57.2297%)
- **Heaviest Functions:** `handle_exception` (Impact: 35.1), `__init__` (Impact: 1.8), `__enter__` (Impact: 1.8)

### 5. `exceptiongroup-1.3.1/tests/test_apport_monkeypatching.py` (PYTHON) -> Cumulative Risk: **225.68**
- **Archetype:** `file_cluster_13` (Distance: 10.212 IQR)
- **Magnitude:** 18.24 | **LOC:** 68 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (68.3747%), Stability (50.0%), Cognitive Load (5.5732%)
- **Heaviest Functions:** `run_script` (Impact: 7.2), `test_apport_excepthook_monkeypatch_inter` (Impact: 2.1)

### 6. `exceptiongroup-1.3.1/src/exceptiongroup/_version.py` (PYTHON) -> Cumulative Risk: **201.63**
- **Archetype:** `file_cluster_8` (Distance: 5.333 IQR)
- **Magnitude:** 16.52 | **LOC:** 35 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Documentation (40.5445%), Cognitive Load (8.4353%)

### 7. `exceptiongroup-1.3.1/src/exceptiongroup/__init__.py` (PYTHON) -> Cumulative Risk: **196.27**
- **Archetype:** `file_cluster_8` (Distance: 6.094 IQR)
- **Magnitude:** 16.78 | **LOC:** 47 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Documentation (34.4328%), Cognitive Load (9.262%)

### 8. `exceptiongroup-1.3.1/tests/test_exceptions.py` (PYTHON) -> Cumulative Risk: **196.11**
- **Archetype:** `file_cluster_8` (Distance: 11.643 IQR)
- **Magnitude:** 662.22 | **LOC:** 889 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Safety Score (26.5607%), Cognitive Load (11.4093%)
- **Heaviest Functions:** `split_exception_group` (Impact: 63.1), `test_split_by_type` (Impact: 43.1), `test_split_ExceptionGroup_subclass_deriv` (Impact: 39.5)

### 9. `exceptiongroup-1.3.1/tests/test_catch.py` (PYTHON) -> Cumulative Risk: **183.94**
- **Archetype:** `file_cluster_8` (Distance: 12.457 IQR)
- **Magnitude:** 123.48 | **LOC:** 223 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Concurrency (19.1857%), Api Exposure (9.146%)
- **Heaviest Functions:** `test_bare_raise_in_handler` (Impact: 9.8), `test_catch_exceptiongroup` (Impact: 8.9), `test_catch_handler_raises` (Impact: 7.7)

### 10. `exceptiongroup-1.3.1/tests/test_formatting.py` (PYTHON) -> Cumulative Risk: **173.36**
- **Archetype:** `file_cluster_13` (Distance: 12.264 IQR)
- **Magnitude:** 149.72 | **LOC:** 578 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Safety Score (14.7541%), Cognitive Load (5.8313%)
- **Heaviest Functions:** `test_format_nested` (Impact: 21.9), `test_formatting_syntax_error` (Impact: 15.0), `test_exceptionhook` (Impact: 12.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `exceptiongroup-1.3.1/tests/test_exceptions.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.643 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.108 IQR)
- **Top Global Matches:** file_cluster_8: 11.643, file_cluster_0: 11.972, file_cluster_13: 11.981
- **Magnitude:** 662.22 | **LOC:** 889 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.4093%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `split_exception_group` (Impact: 63.1)
  * `test_split_by_type` (Impact: 43.1)
  * `test_split_ExceptionGroup_subclass_deriv` (Impact: 39.5)
    * *Intent:* # Match KeyboardInterrupt match, rest = self.split_exception_group(eg, KeyboardInterrupt) self.asser...
  * `test_split_ExceptionGroup_subclass_no_de` (Impact: 24.7)
    * *Intent:* # Match KeyboardInterrupts
  * `create_simple_eg` (Impact: 22.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 161`, `args: 74`, `func_start: 68`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 35`, `duplicate_logic: 4`, `orphaned_logic: 46`
* *Architecture:* `io: 4`, `api: 87`, `import: 6`
* *Defense:* `safety: 75`, `doc: 4`, `test: 76`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pytest, collections.abc, sys, platform, unittest, exceptiongroup
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.001 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.48 IQR)
- **Top Global Matches:** file_cluster_13: 11.001, file_cluster_0: 11.169, file_cluster_8: 11.183
- **Magnitude:** 323.34 | **LOC:** 603 | **CtrlFlow:** 60.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.1031%), Tech Debt (80.1565%)
**Top Internal Functions/Classes:**
  * `format` (Impact: 95.0)
  * `_levenshtein_distance` (Impact: 47.0)
  * `_compute_suggestion_error` (Impact: 30.1)
  * `format_exception_only` (Impact: 20.5)
    * *Intent:* """Format the exception part of the traceback. The return value is a generator of strings, each endi...
  * `emit` (Impact: 12.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 91`, `args: 21`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 64`, `duplicate_logic: 7`
* *Architecture:* `io: 13`, `api: 11`, `import: 11`
* *Defense:* `safety: 28`, `doc: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 58.991
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.066667
  * `Imports (Out-Degree: 1):` functools, traceback, __future__, collections.abc, sys, types, typing, apport_python_hook...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `exceptiongroup-1.3.1/tests/test_formatting.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.264 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.912 IQR)
- **Top Global Matches:** file_cluster_13: 12.264, file_cluster_0: 12.499, file_cluster_8: 12.521
- **Magnitude:** 149.72 | **LOC:** 578 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.8313%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_format_nested` (Impact: 21.9)
  * `test_formatting_syntax_error` (Impact: 15.0)
  * `test_exceptionhook` (Impact: 12.8)
  * `test_exceptionhook_format_exception_only` (Impact: 12.8)
  * `test_exceptiongroup_loop` (Impact: 8.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 128`, `args: 28`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 12`, `orphaned_logic: 7`
* *Architecture:* `io: 61`, `api: 20`, `import: 20`
* *Defense:* `safety: 59`, `doc: 18`, `test: 45`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` _pytest.capture, traceback, urllib.error, pytest, pickle, subprocess, sys, typing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exceptiongroup-1.3.1/tests/test_catch.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.457 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.022 IQR)
- **Top Global Matches:** file_cluster_8: 12.457, file_cluster_0: 12.862, file_cluster_13: 12.934
- **Magnitude:** 123.48 | **LOC:** 223 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.8072%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_bare_raise_in_handler` (Impact: 9.8)
    * *Intent:* """Test that a bare "raise" "middle" ecxeption group gets discarded."""
  * `test_catch_exceptiongroup` (Impact: 8.9)
  * `test_catch_handler_raises` (Impact: 7.7)
  * `test_async_handler` (Impact: 7.5)
  * `test_catch_no_match` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 78`, `args: 24`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 13`, `duplicate_logic: 4`, `orphaned_logic: 14`
* *Architecture:* `api: 19`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 74`, `doc: 2`, `test: 73`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` exceptiongroup, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exceptiongroup-1.3.1/src/exceptiongroup/_exceptions.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.308 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.56 IQR)
- **Top Global Matches:** file_cluster_16: 10.308, file_cluster_0: 10.568, file_cluster_8: 10.704
- **Magnitude:** 99.16 | **LOC:** 337 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.4283%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `add_note` (Impact: 5.7)
  * `__str__` (Impact: 5.3)
  * `_derive_and_copy_attributes` (Impact: 3.9)
  * `message` (Impact: 1.8)
  * `__repr__` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 94`, `args: 29`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 21`, `duplicate_logic: 20`
* *Architecture:* `io: 1`, `api: 28`, `import: 7`
* *Defense:* `safety: 14`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 209.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.266667
  * `Imports (Out-Degree: 0):` functools, __future__, typing_extensions, collections.abc, sys, typing, inspect
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `exceptiongroup-1.3.1/tests/test_catch_py311.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.567 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.604 IQR)
- **Top Global Matches:** file_cluster_8: 13.567, file_cluster_13: 13.702, file_cluster_0: 13.706
- **Magnitude:** 84.0 | **LOC:** 191 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.9731%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_bare_raise_in_handler` (Impact: 8.0)
    * *Intent:* """Test that the "middle" ecxeption group gets discarded."""
  * `test_catch_handler_raises` (Impact: 7.6)
  * `test_catch_no_match` (Impact: 7.5)
  * `test_catch_single_no_match` (Impact: 7.4)
  * `test_catch_ungrouped` (Impact: 6.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 75`, `args: 10`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 11`, `orphaned_logic: 10`
* *Architecture:* `io: 1`, `api: 10`, `import: 3`
* *Defense:* `safety: 97`, `doc: 2`, `test: 60`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, pytest, exceptiongroup
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exceptiongroup-1.3.1/src/exceptiongroup/_catch.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.159 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.01 IQR)
- **Top Global Matches:** file_cluster_13: 11.159, file_cluster_8: 11.373, file_cluster_16: 11.376
- **Magnitude:** 58.28 | **LOC:** 139 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.2297%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handle_exception` (Impact: 35.1)
  * `__init__` (Impact: 1.8)
  * `__enter__` (Impact: 1.8)
  * `__exit__` (Impact: 1.2)
  * `catch` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 43`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 10`
* *Architecture:* `io: 1`, `api: 5`, `import: 8`
* *Defense:* `safety: 17`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 58.991
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.066667
  * `Imports (Out-Degree: 1):` __future__, collections.abc, sys, types, typing, contextlib, inspect, ._exceptions
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `exceptiongroup-1.3.1/tests/test_apport_monkeypatching.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.212 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 7.118 IQR)
- **Top Global Matches:** file_cluster_13: 10.212, file_cluster_0: 10.45, file_cluster_8: 10.847
- **Magnitude:** 18.24 | **LOC:** 68 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.5732%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_script` (Impact: 7.2)
  * `test_apport_excepthook_monkeypatch_inter` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 13`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 6`, `orphaned_logic: 1`
* *Architecture:* `io: 7`, `api: 2`, `import: 7`
* *Defense:* `safety: 1`, `doc: 2`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, os, pytest, subprocess, sys, exceptiongroup, pathlib
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exceptiongroup-1.3.1/src/exceptiongroup/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.094 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.678 IQR)
- **Top Global Matches:** file_cluster_8: 6.094, file_cluster_13: 6.371, file_cluster_7: 7.345
- **Magnitude:** 16.78 | **LOC:** 47 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.262%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 19`
* *Risk/State:* None
* *Architecture:* `io: 3`, `api: 1`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 50.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` traceback, os, sys, ._formatting, ._catch, contextlib, , ._version...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exceptiongroup-1.3.1/src/exceptiongroup/_version.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 58.991
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.066667
  * `Imports (Out-Degree: 0):` typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `exceptiongroup-1.3.1/tests/dummyscript.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.413 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.468 IQR)
- **Top Global Matches:** file_cluster_13: 10.413, file_cluster_8: 10.543, file_cluster_17: 11.317
- **Magnitude:** 14.68 | **LOC:** 13 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 6`
* *Risk/State:* None
* *Architecture:* `io: 2`, `import: 3`
* *Defense:* `safety: 3`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, traceback, pickle
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exceptiongroup-1.3.1/tests/apport_excepthook.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.31 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.288 IQR)
- **Top Global Matches:** file_cluster_13: 9.31, file_cluster_8: 9.871, file_cluster_7: 10.591
- **Magnitude:** 14.12 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 1`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` apport_python_hook, sys, it, exceptiongroup
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exceptiongroup-1.3.1/tests/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exceptiongroup-1.3.1/src/exceptiongroup/_suppress.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.58 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.86 IQR)
- **Top Global Matches:** file_cluster_13: 9.58, file_cluster_16: 9.867, file_cluster_8: 10.174
- **Magnitude:** 10.44 | **LOC:** 56 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.1213%), Tech Debt (97.7023%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 1.8)
  * `__enter__` (Impact: 1.8)
  * `__exit__` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 21`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 4`, `import: 6`
* *Defense:* `safety: 2`, `doc: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 58.991
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.066667
  * `Imports (Out-Degree: 1):` __future__, sys, types, typing, contextlib, ._exceptions
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `exceptiongroup-1.3.1/tests/check_types.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.539 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.304 IQR)
- **Top Global Matches:** file_cluster_8: 7.539, file_cluster_13: 8.1, file_cluster_16: 8.145
- **Magnitude:** 8.78 | **LOC:** 42 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.1392%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `value_key_err_handler` (Impact: 4.2)
    * *Intent:* # code snippets from the README
  * `runtime_err_handler` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 7`, `args: 2`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` exceptiongroup, typing_extensions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `exceptiongroup-1.3.1/tests/test_suppress.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.545 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.065 IQR)
- **Top Global Matches:** file_cluster_13: 11.545, file_cluster_8: 11.92, file_cluster_0: 12.451
- **Magnitude:** 5.0 | **LOC:** 17 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_suppress_exception` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 10`, `args: 1`, `func_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 4`
* *Defense:* `safety: 3`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 50.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, pytest, exceptiongroup
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `exceptiongroup-1.3.1/tests/dummyscript.py` (PYTHON) | Magnitude: 14.68 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, safety: 3, import: 3, indent_spaces: 3
- `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py` (PYTHON) | Magnitude: 323.34 | Delta: **0.168 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 407, encapsulation: 151, branch: 140, structural_boundaries: 91
- `exceptiongroup-1.3.1/src/exceptiongroup/_catch.py` (PYTHON) | Magnitude: 58.28 | Delta: **0.214 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 102, structural_boundaries: 43, branch: 40, encapsulation: 18
- `exceptiongroup-1.3.1/tests/test_formatting.py` (PYTHON) | Magnitude: 149.72 | Delta: **0.235 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 284, bitwise_ops: 143, structural_boundaries: 128, branch: 76
- `exceptiongroup-1.3.1/tests/test_apport_monkeypatching.py` (PYTHON) | Magnitude: 18.24 | Delta: **0.238 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 13, io: 7, import: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `exceptiongroup-1.3.1/src/exceptiongroup/_exceptions.py` (PYTHON) | Magnitude: 99.16 | Delta: **0.26 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 256, encapsulation: 173, structural_boundaries: 94, generics: 80

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `exceptiongroup-1.3.1/tests/test_catch_py311.py` (PYTHON) | Magnitude: 84.0 | Delta: **0.135 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 140, safety: 97, structural_boundaries: 75, test: 60
- `exceptiongroup-1.3.1/src/exceptiongroup/__init__.py` (PYTHON) | Magnitude: 16.78 | Delta: **0.277 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 19, encapsulation: 12, import: 10
- `exceptiongroup-1.3.1/tests/test_exceptions.py` (PYTHON) | Magnitude: 662.22 | Delta: **0.329 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 639, branch: 186, structural_boundaries: 161, api: 87
- `exceptiongroup-1.3.1/tests/test_catch.py` (PYTHON) | Magnitude: 123.48 | Delta: **0.405 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 156, structural_boundaries: 78, safety: 74, test: 73
- `exceptiongroup-1.3.1/tests/check_types.py` (PYTHON) | Magnitude: 8.78 | Delta: **0.561 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 6, branch: 3, args: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `exceptiongroup-1.3.1/src/exceptiongroup/_exceptions.py` -> **Severity: 14.719** (Embedded: 0.2667 * Error Risk: 55.1959%)
- `exceptiongroup-1.3.1/src/exceptiongroup/_suppress.py` -> **Severity: 5.125** (Embedded: 0.0667 * Error Risk: 76.875%)
- `exceptiongroup-1.3.1/src/exceptiongroup/_catch.py` -> **Severity: 4.924** (Embedded: 0.0667 * Error Risk: 73.8596%)
- `exceptiongroup-1.3.1/src/exceptiongroup/_formatting.py` -> **Severity: 4.05** (Embedded: 0.0667 * Error Risk: 60.7557%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `exceptiongroup-1.3.1/src/exceptiongroup/_exceptions.py` -> **Severity: 17989.651** (Blast Radius: 209.416 * Doc Risk: 85.9039%)
- `exceptiongroup-1.3.1/src/exceptiongroup/_suppress.py` -> **Severity: 4225.148** (Blast Radius: 58.991 * Doc Risk: 71.6236%)
- `exceptiongroup-1.3.1/src/exceptiongroup/_catch.py` -> **Severity: 2581.57** (Blast Radius: 58.991 * Doc Risk: 43.7621%)
- `exceptiongroup-1.3.1/src/exceptiongroup/_version.py` -> **Severity: 2391.761** (Blast Radius: 58.991 * Doc Risk: 40.5445%)
- `exceptiongroup-1.3.1/src/exceptiongroup/__init__.py` -> **Severity: 1736.102** (Blast Radius: 50.42 * Doc Risk: 34.4328%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
