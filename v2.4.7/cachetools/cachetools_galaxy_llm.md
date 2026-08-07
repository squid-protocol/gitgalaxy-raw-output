# ARCHITECTURAL_BRIEF: cachetools
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/cachetools` |
| **Timestamp** | `2026-08-07T05:21:45.664882+00:00` |
| **Scan Duration** | `0.15s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 19 malicious artifacts.

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
| Total Artifacts | 27 |
| Analyzed Artifacts (Scanned) | 20 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7 |
| Total LOC | 3401 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 74.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.64 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6667 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3333 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 19 | 3401 | 95.0% |
| PLAINTEXT | 1 | 0 | 5.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `7.025`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 16 | 80.0% |
| file_cluster_13 | 3 | 15.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 5.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7*

**Composition by Extension & Reason:**
- `.rst`: 2x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 2.8 | 66.3 | 13.8 | 5.0 | 40.6 |
| Error & Exception Exposure | 0.0 | 70.4 | 37.4 | 46.1 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 15.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.6 | 0.0 | 0.0 |
| API Exposure | 1.8 | 11.3 | 6.6 | 7.0 | 1.8 |
| Concurrency Exposure | 0.0 | 60.2 | 3.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 19.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 33.3 | 100.0 | 96.5 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 89.0 | 20.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `cachetools-7.0.5/tests/__init__.py` (Hits: 1)
- `cachetools-7.0.5/MANIFEST.in` (Hits: 0)
- `cachetools-7.0.5/src/cachetools/__init__.py` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **keys.py** (`cachetools-7.0.5/src/cachetools/keys.py`) — 2 inbound connections
2. **_cached.py** (`cachetools-7.0.5/src/cachetools/_cached.py`) — 1 inbound connections
3. **_cachedmethod.py** (`cachetools-7.0.5/src/cachetools/_cachedmethod.py`) — 1 inbound connections
4. **func.py** (`cachetools-7.0.5/src/cachetools/func.py`) — 1 inbound connections
5. **MANIFEST.in** (`cachetools-7.0.5/MANIFEST.in`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`cachetools-7.0.5/src/cachetools/__init__.py`) — 9 outbound dependencies
2. **test_cachedmethod.py** (`cachetools-7.0.5/tests/test_cachedmethod.py`) — 8 outbound dependencies
3. **func.py** (`cachetools-7.0.5/src/cachetools/func.py`) — 6 outbound dependencies
4. **test_cached.py** (`cachetools-7.0.5/tests/test_cached.py`) — 5 outbound dependencies
5. **test_threading.py** (`cachetools-7.0.5/tests/test_threading.py`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `popitem` (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> Impact: **68.1** | LOC: 219
- `_wrapper` (@ `cachetools-7.0.5/src/cachetools/_cached.py`) -> Impact: **46.5** | LOC: 31
- `_wrapper` (@ `cachetools-7.0.5/src/cachetools/_cachedmethod.py`) -> Impact: **41.0** | LOC: 27
- `__repr__` (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> Impact: **39.6** | LOC: 134
- `_condition_info` (@ `cachetools-7.0.5/src/cachetools/_cachedmethod.py`) -> Impact: **28.8** | LOC: 46
- `_condition_info` (@ `cachetools-7.0.5/src/cachetools/_cached.py`) -> Impact: **28.6** | LOC: 42
- `popitem` (@ `cachetools-7.0.5/src/cachetools/__init__.py`) -> Impact: **28.0** | LOC: 76
- `_condition` (@ `cachetools-7.0.5/src/cachetools/_cachedmethod.py`) -> Impact: **24.5** | LOC: 49
- `__get__` (@ `cachetools-7.0.5/src/cachetools/_cachedmethod.py`) -> Impact: **23.9** | LOC: 39
  * *Intent:* # through the class to support class-level introspection, such # as for mocking with autospec=True in unittest.mock. pass elif self.__attrname is not ...
- `_condition` (@ `cachetools-7.0.5/src/cachetools/_cached.py`) -> Impact: **23.6** | LOC: 31

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `cachetools-7.0.5/src/cachetools` | 5 | 1350.46 | 34.78% | 59.99% |
| `cachetools-7.0.5/tests` | 14 | 975.76 | 6.25% | 0.0% |
| `cachetools-7.0.5` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `cachetools-7.0.5/src/cachetools/_cached.py` -> **100.0%** Exposure
- `cachetools-7.0.5/src/cachetools/_cachedmethod.py` -> **100.0%** Exposure
- `cachetools-7.0.5/src/cachetools/__init__.py` -> **99.9584%** Exposure
### Highest State Flux (Mutation/Volatility)
- `cachetools-7.0.5/src/cachetools/__init__.py` -> **99.9615%** Exposure
- `cachetools-7.0.5/src/cachetools/_cachedmethod.py` -> **99.7045%** Exposure
- `cachetools-7.0.5/src/cachetools/_cached.py` -> **99.6322%** Exposure
- `cachetools-7.0.5/src/cachetools/keys.py` -> **79.5168%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `cachetools-7.0.5/tests/test_cachedmethod.py` -> **31** Orphaned Functions | **15** Duplicates
- `cachetools-7.0.5/src/cachetools/_cachedmethod.py` -> **0** Orphaned Functions | **34** Duplicates
- `cachetools-7.0.5/tests/test_cached.py` -> **17** Orphaned Functions | **14** Duplicates
- `cachetools-7.0.5/tests/__init__.py` -> **20** Orphaned Functions | **4** Duplicates
- `cachetools-7.0.5/src/cachetools/__init__.py` -> **0** Orphaned Functions | **23** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`cachetools-7.0.5/src/cachetools/__init__.py`** -> AI Confidence: **99.15%**
2. **`cachetools-7.0.5/tests/test_cachedmethod.py`** -> AI Confidence: **99.07%**
3. **`cachetools-7.0.5/src/cachetools/_cached.py`** -> AI Confidence: **98.96%**
4. **`cachetools-7.0.5/src/cachetools/func.py`** -> AI Confidence: **98.93%**
5. **`cachetools-7.0.5/tests/test_threading.py`** -> AI Confidence: **98.93%**
6. **`cachetools-7.0.5/tests/test_keys.py`** -> AI Confidence: **98.92%**
7. **`cachetools-7.0.5/tests/test_lfu.py`** -> AI Confidence: **98.92%**
8. **`cachetools-7.0.5/src/cachetools/_cachedmethod.py`** -> AI Confidence: **98.89%**
9. **`cachetools-7.0.5/src/cachetools/keys.py`** -> AI Confidence: **98.89%**
10. **`cachetools-7.0.5/tests/__init__.py`** -> AI Confidence: **98.89%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `61` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `cachetools-7.0.5/src/cachetools/__init__.py` (PYTHON) -> Cumulative Risk: **606.7**
- **Archetype:** `file_cluster_13` (Distance: 12.642 IQR)
- **Magnitude:** 485.48 | **LOC:** 773 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9615%), Tech Debt (99.9584%), Verification (80.0%)
- **Heaviest Functions:** `popitem` (Impact: 68.1), `__repr__` (Impact: 39.6), `popitem` (Impact: 28.0)

### 2. `cachetools-7.0.5/src/cachetools/_cachedmethod.py` (PYTHON) -> Cumulative Risk: **563.31**
- **Archetype:** `file_cluster_8` (Distance: 12.278 IQR)
- **Magnitude:** 452.52 | **LOC:** 420 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.7045%), Documentation (88.97%)
- **Heaviest Functions:** `_wrapper` (Impact: 41.0), `_condition_info` (Impact: 28.8), `_condition` (Impact: 24.5)

### 3. `cachetools-7.0.5/src/cachetools/_cached.py` (PYTHON) -> Cumulative Risk: **519.62**
- **Archetype:** `file_cluster_8` (Distance: 11.989 IQR)
- **Magnitude:** 306.66 | **LOC:** 260 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.6322%), Documentation (79.784%)
- **Heaviest Functions:** `_wrapper` (Impact: 46.5), `_condition_info` (Impact: 28.6), `_condition` (Impact: 23.6)

### 4. `cachetools-7.0.5/src/cachetools/keys.py` (PYTHON) -> Cumulative Risk: **393.58**
- **Archetype:** `file_cluster_8` (Distance: 10.693 IQR)
- **Magnitude:** 39.66 | **LOC:** 67 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (81.4287%), State Flux (79.5168%), Safety Score (58.9862%)
- **Heaviest Functions:** `typedkey` (Impact: 9.3), `hashkey` (Impact: 5.6), `__hash__` (Impact: 3.7)

### 5. `cachetools-7.0.5/src/cachetools/func.py` (PYTHON) -> Cumulative Risk: **306.72**
- **Archetype:** `file_cluster_13` (Distance: 9.008 IQR)
- **Magnitude:** 66.14 | **LOC:** 106 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Documentation (61.6889%), Stability (50.0%)
- **Heaviest Functions:** `ttl_cache` (Impact: 9.4), `rr_cache` (Impact: 8.4), `fifo_cache` (Impact: 7.4)

### 6. `cachetools-7.0.5/tests/__init__.py` (PYTHON) -> Cumulative Risk: **247.31**
- **Archetype:** `file_cluster_8` (Distance: 10.545 IQR)
- **Magnitude:** 195.46 | **LOC:** 384 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (70.4007%), Stability (50.0%), Cognitive Load (19.8946%)
- **Heaviest Functions:** `test_missing` (Impact: 20.2), `test_pickle` (Impact: 8.1), `test_pop` (Impact: 7.9)

### 7. `cachetools-7.0.5/tests/test_threading.py` (PYTHON) -> Cumulative Risk: **234.03**
- **Archetype:** `file_cluster_8` (Distance: 9.158 IQR)
- **Magnitude:** 33.32 | **LOC:** 63 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (60.1932%), Stability (50.0%), Cognitive Load (15.2237%)
- **Heaviest Functions:** `test_cached_stampede` (Impact: 7.5), `test_cachedmethod_stampede` (Impact: 7.5), `func` (Impact: 5.5)

### 8. `cachetools-7.0.5/tests/test_keys.py` (PYTHON) -> Cumulative Risk: **215.36**
- **Archetype:** `file_cluster_8` (Distance: 7.353 IQR)
- **Magnitude:** 31.72 | **LOC:** 93 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (52.1081%), Stability (50.0%), Cognitive Load (6.8401%)
- **Heaviest Functions:** `test_hashkey` (Impact: 4.3), `test_methodkey` (Impact: 4.3), `test_typedmethodkey` (Impact: 4.3)

### 9. `cachetools-7.0.5/tests/test_classmethod.py` (PYTHON) -> Cumulative Risk: **214.44**
- **Archetype:** `file_cluster_8` (Distance: 8.36 IQR)
- **Magnitude:** 60.02 | **LOC:** 152 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Safety Score (46.0017%), Api Exposure (10.4924%)
- **Heaviest Functions:** `test` (Impact: 6.4), `test_typed` (Impact: 6.3), `test_locked` (Impact: 4.1)

### 10. `cachetools-7.0.5/tests/test_ttl.py` (PYTHON) -> Cumulative Risk: **211.79**
- **Archetype:** `file_cluster_8` (Distance: 8.32 IQR)
- **Magnitude:** 66.72 | **LOC:** 246 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Safety Score (49.7569%), Api Exposure (6.9834%)
- **Heaviest Functions:** `test_ttl` (Impact: 9.7), `test_ttl_expire` (Impact: 6.0), `test_ttl_tuple_key` (Impact: 4.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `cachetools-7.0.5/src/cachetools/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.642 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.928 IQR)
- **Top Global Matches:** file_cluster_13: 12.642, file_cluster_8: 12.665, file_cluster_0: 12.751
- **Magnitude:** 485.48 | **LOC:** 773 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.5596%), Tech Debt (99.9584%)
**Top Internal Functions/Classes:**
  * `popitem` (Impact: 68.1)
  * `__repr__` (Impact: 39.6)
  * `popitem` (Impact: 28.0)
  * `popitem` (Impact: 17.2)
  * `expire` (Impact: 16.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 212`, `args: 99`, `func_start: 98`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 143`, `duplicate_logic: 23`
* *Architecture:* `api: 51`, `import: 9`
* *Defense:* `safety: 31`, `doc: 58`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` random, , functools, time, ._cached, ._cachedmethod, collections.abc, collections...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/src/cachetools/_cachedmethod.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.278 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.923 IQR)
- **Top Global Matches:** file_cluster_8: 12.278, file_cluster_0: 12.391, file_cluster_13: 12.417
- **Magnitude:** 452.52 | **LOC:** 420 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.3085%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_wrapper` (Impact: 41.0)
  * `_condition_info` (Impact: 28.8)
  * `_condition` (Impact: 24.5)
  * `__get__` (Impact: 23.9)
    * *Intent:* # through the class to support class-level introspection, such # as for mocking with autospec=True i...
  * `_locked_info` (Impact: 19.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 123`, `args: 53`, `func_start: 51`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 64`, `duplicate_logic: 34`
* *Architecture:* `api: 37`, `import: 3`
* *Defense:* `safety: 32`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 60.897
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.052632
  * `Imports (Out-Degree: 0):` functools, weakref, warnings
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cachetools-7.0.5/src/cachetools/_cached.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.989 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.929 IQR)
- **Top Global Matches:** file_cluster_8: 11.989, file_cluster_13: 12.329, file_cluster_0: 12.382
- **Magnitude:** 306.66 | **LOC:** 260 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.9279%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_wrapper` (Impact: 46.5)
  * `_condition_info` (Impact: 28.6)
  * `_condition` (Impact: 23.6)
  * `_locked_info` (Impact: 18.9)
  * `wrapper` (Impact: 15.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 69`, `args: 31`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 40`, `duplicate_logic: 17`
* *Architecture:* `api: 19`, `import: 1`
* *Defense:* `safety: 28`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 60.897
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.052632
  * `Imports (Out-Degree: 0):` functools
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cachetools-7.0.5/tests/test_cachedmethod.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.806 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.07 IQR)
- **Top Global Matches:** file_cluster_8: 8.806, file_cluster_0: 9.451, file_cluster_7: 9.51
- **Magnitude:** 243.34 | **LOC:** 698 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.8615%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_decorator_cond_info` (Impact: 7.7)
  * `test_decorator_lock_cond_info` (Impact: 7.7)
  * `test_decorator_lock_info` (Impact: 7.2)
  * `test_decorator_immutable_dict` (Impact: 7.0)
  * `test_decorator_slots` (Impact: 6.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 103`, `args: 81`, `func_start: 55`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 12`, `duplicate_logic: 15`, `orphaned_logic: 31`
* *Architecture:* `api: 62`, `import: 8`
* *Defense:* `safety: 4`, `doc: 2`, `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, cachetools, fractions, , warnings, gc, weakref, unittest.mock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.545 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.768 IQR)
- **Top Global Matches:** file_cluster_8: 10.545, file_cluster_13: 10.93, file_cluster_0: 11.151
- **Magnitude:** 195.46 | **LOC:** 384 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.8946%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_missing` (Impact: 20.2)
  * `test_pickle` (Impact: 8.1)
  * `test_pop` (Impact: 7.9)
  * `test_insert` (Impact: 7.8)
  * `_test_getsizeof` (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 46`, `args: 29`, `func_start: 26`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 3`, `state_mutation: 55`, `duplicate_logic: 4`, `orphaned_logic: 20`
* *Architecture:* `io: 1`, `api: 25`, `import: 4`
* *Defense:* `safety: 5`, `test: 18`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, pickle, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_cached.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.371 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.996 IQR)
- **Top Global Matches:** file_cluster_8: 7.371, file_cluster_7: 8.361, file_cluster_1: 8.587
- **Magnitude:** 120.38 | **LOC:** 399 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.8066%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `func` (Impact: 6.3)
  * `test_decorator_typed` (Impact: 3.2)
  * `test_decorator` (Impact: 3.0)
  * `test_decorator_lock_condition_info` (Impact: 3.0)
  * `test_decorator_lock_info` (Impact: 2.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 45`, `args: 31`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `state_mutation: 3`, `duplicate_logic: 14`, `orphaned_logic: 17`
* *Architecture:* `api: 35`, `import: 5`
* *Defense:* `safety: 1`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unittest, cachetools, cachetools.keys, , warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_tlru.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.256 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.099 IQR)
- **Top Global Matches:** file_cluster_8: 8.256, file_cluster_7: 9.124, file_cluster_13: 9.283
- **Magnitude:** 79.24 | **LOC:** 330 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.2508%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_ttu` (Impact: 10.7)
  * `test_ttu_expire` (Impact: 5.9)
  * `test_ttu_heap_cleanup` (Impact: 4.9)
  * `test_ttu_tuple_key` (Impact: 3.9)
  * `__call__` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 28`, `args: 23`, `func_start: 14`, `class_start: 3`
* *Risk/State:* `state_mutation: 8`, `duplicate_logic: 2`, `orphaned_logic: 10`
* *Architecture:* `api: 14`, `import: 4`
* *Defense:* `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, cachetools, math, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_ttl.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.32 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.99 IQR)
- **Top Global Matches:** file_cluster_8: 8.32, file_cluster_13: 9.141, file_cluster_7: 9.17
- **Magnitude:** 66.72 | **LOC:** 246 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0497%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_ttl` (Impact: 9.7)
  * `test_ttl_expire` (Impact: 6.0)
  * `test_ttl_tuple_key` (Impact: 4.0)
  * `__call__` (Impact: 3.7)
  * `test_ttl_lru` (Impact: 3.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 27`, `args: 12`, `func_start: 12`, `class_start: 3`
* *Risk/State:* `state_mutation: 8`, `duplicate_logic: 2`, `orphaned_logic: 9`
* *Architecture:* `api: 12`, `import: 5`
* *Defense:* `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, cachetools, math, , datetime
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/src/cachetools/func.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.008 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.505 IQR)
- **Top Global Matches:** file_cluster_13: 9.008, file_cluster_8: 9.073, file_cluster_7: 9.306
- **Magnitude:** 66.14 | **LOC:** 106 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.4378%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ttl_cache` (Impact: 9.4)
    * *Intent:* """ if maxsize is None: return _cache({}, None, typed) elif callable(maxsize): return _cache(RRCache...
  * `rr_cache` (Impact: 8.4)
  * `fifo_cache` (Impact: 7.4)
  * `lfu_cache` (Impact: 7.4)
  * `lru_cache` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 40`, `args: 10`, `func_start: 9`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 8`, `concurrency: 1`, `import: 8`
* *Defense:* `doc: 12`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 79.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.052632
  * `Imports (Out-Degree: 0):` math, random, , functools, time, threading
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cachetools-7.0.5/tests/test_classmethod.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.36 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.189 IQR)
- **Top Global Matches:** file_cluster_8: 8.36, file_cluster_0: 8.844, file_cluster_13: 8.957
- **Magnitude:** 60.02 | **LOC:** 152 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.9435%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 6.4)
  * `test_typed` (Impact: 6.3)
  * `test_locked` (Impact: 4.1)
  * `test_condition` (Impact: 4.1)
  * `test_clear` (Impact: 4.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 26`, `args: 17`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `state_mutation: 1`, `orphaned_logic: 7`
* *Architecture:* `api: 13`, `concurrency: 3`, `import: 4`
* *Defense:* `test: 9`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, cachetools, warnings, threading
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_func.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.985 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.763 IQR)
- **Top Global Matches:** file_cluster_8: 8.985, file_cluster_7: 9.577, file_cluster_13: 9.681
- **Magnitude:** 48.32 | **LOC:** 125 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.6426%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_decorator_needs_rlock` (Impact: 4.7)
    * *Intent:* """This will deadlock on a cache that uses a regular lock. https://github.com/python/cpython/blob/3....
  * `__eq__` (Impact: 3.8)
  * `test_decorator_typed` (Impact: 2.3)
  * `test_decorator` (Impact: 2.2)
  * `test_decorator_clear` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 23`, `args: 18`, `func_start: 11`, `class_start: 7`
* *Risk/State:* `state_mutation: 4`, `orphaned_logic: 10`
* *Architecture:* `api: 15`, `import: 2`
* *Defense:* `doc: 2`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unittest, cachetools.func
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/src/cachetools/keys.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.693 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.646 IQR)
- **Top Global Matches:** file_cluster_8: 10.693, file_cluster_7: 10.811, file_cluster_1: 11.08
- **Magnitude:** 39.66 | **LOC:** 67 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.6867%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `typedkey` (Impact: 9.3)
  * `hashkey` (Impact: 5.6)
    * *Intent:* # A sentinel for separating args from kwargs. Using the class itself # ensures uniqueness and preser...
  * `__hash__` (Impact: 3.7)
  * `methodkey` (Impact: 2.2)
  * `typedmethodkey` (Impact: 2.2)
    * *Intent:* """Return a typed cache key for use with cached methods."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 20`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 7`
* *Defense:* `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 115.385
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.105263
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `cachetools-7.0.5/tests/test_threading.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.158 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.073 IQR)
- **Top Global Matches:** file_cluster_8: 9.158, file_cluster_13: 9.197, file_cluster_0: 9.431
- **Magnitude:** 33.32 | **LOC:** 63 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.2237%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_cached_stampede` (Impact: 7.5)
  * `test_cachedmethod_stampede` (Impact: 7.5)
  * `func` (Impact: 5.5)
  * `meth` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 14`, `args: 6`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 2`
* *Architecture:* `api: 5`, `concurrency: 5`, `import: 5`
* *Defense:* `safety: 1`, `test: 6`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, cachetools, time, os, threading
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_keys.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.353 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.652 IQR)
- **Top Global Matches:** file_cluster_8: 7.353, file_cluster_13: 8.296, file_cluster_7: 8.375
- **Magnitude:** 31.72 | **LOC:** 93 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.8401%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_hashkey` (Impact: 4.3)
  * `test_methodkey` (Impact: 4.3)
    * *Intent:* # similar to hashkey(), but ignores its first positional argument self.assertEqual(key("x"), key("y"...
  * `test_typedmethodkey` (Impact: 4.3)
    * *Intent:* # similar to typedkey(), but ignores its first positional argument self.assertEqual(key("x"), key("y...
  * `test_typedkey` (Impact: 4.2)
  * `test_pickle` (Impact: 4.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 13`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `orphaned_logic: 6`
* *Architecture:* `api: 7`, `import: 3`
* *Defense:* `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` unittest, cachetools.keys, pickle
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_rr.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.528 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.728 IQR)
- **Top Global Matches:** file_cluster_8: 7.528, file_cluster_13: 8.386, file_cluster_7: 8.548
- **Magnitude:** 25.94 | **LOC:** 89 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.9729%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_rr_getsizeof` (Impact: 4.5)
  * `test_rr_bad_choice` (Impact: 4.2)
  * `test_rr` (Impact: 2.9)
  * `test_rr_update_existing` (Impact: 2.3)
  * `test_rr_default_choice` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 13`, `args: 7`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 5`
* *Architecture:* `api: 7`, `import: 4`
* *Defense:* `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, cachetools, random, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_lfu.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.485 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.451 IQR)
- **Top Global Matches:** file_cluster_8: 7.485, file_cluster_13: 8.283, file_cluster_7: 8.474
- **Magnitude:** 23.3 | **LOC:** 91 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.5573%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_lfu` (Impact: 6.3)
  * `test_lfu_getsizeof` (Impact: 4.5)
  * `test_lfu_clear` (Impact: 2.9)
  * `test_lfu_update_existing` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 10`, `args: 5`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, cachetools, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_lru.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.3 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.45 IQR)
- **Top Global Matches:** file_cluster_8: 7.3, file_cluster_13: 8.16, file_cluster_7: 8.325
- **Magnitude:** 19.7 | **LOC:** 90 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.5319%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_lru_getsizeof` (Impact: 4.5)
  * `test_lru` (Impact: 2.9)
  * `test_lru_clear` (Impact: 2.7)
  * `test_lru_update_existing` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 10`, `args: 5`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, cachetools, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_fifo.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.086 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.596 IQR)
- **Top Global Matches:** file_cluster_8: 7.086, file_cluster_13: 8.029, file_cluster_7: 8.175
- **Magnitude:** 14.7 | **LOC:** 69 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.9762%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_fifo_getsizeof` (Impact: 4.5)
  * `test_fifo` (Impact: 2.9)
  * `test_fifo_update_existing` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 9`, `args: 4`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 3`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, cachetools, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/tests/test_cache.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.177 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.267 IQR)
- **Top Global Matches:** file_cluster_13: 8.177, file_cluster_8: 8.447, file_cluster_7: 9.347
- **Magnitude:** 13.6 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` unittest, cachetools, 
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cachetools-7.0.5/MANIFEST.in` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 42.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `cachetools-7.0.5/src/cachetools/__init__.py` (PYTHON) | Magnitude: 485.48 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 541, encapsulation: 280, structural_boundaries: 212, state_mutation: 143
- `cachetools-7.0.5/src/cachetools/func.py` (PYTHON) | Magnitude: 66.14 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 40, encapsulation: 21, branch: 17
- `cachetools-7.0.5/tests/test_cache.py` (PYTHON) | Magnitude: 13.6 | Delta: **0.27 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, test: 3, import: 3, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `cachetools-7.0.5/tests/test_threading.py` (PYTHON) | Magnitude: 33.32 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 14, branch: 8, args: 6
- `cachetools-7.0.5/src/cachetools/_cachedmethod.py` (PYTHON) | Magnitude: 452.52 | Delta: **0.113 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 299, encapsulation: 145, structural_boundaries: 123, branch: 65
- `cachetools-7.0.5/src/cachetools/keys.py` (PYTHON) | Magnitude: 39.66 | Delta: **0.118 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 26, encapsulation: 22, structural_boundaries: 20, doc: 12
- `cachetools-7.0.5/src/cachetools/_cached.py` (PYTHON) | Magnitude: 306.66 | Delta: **0.34 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 192, structural_boundaries: 69, branch: 48, state_mutation: 40
- `cachetools-7.0.5/tests/__init__.py` (PYTHON) | Magnitude: 195.46 | Delta: **0.385 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 289, state_mutation: 55, structural_boundaries: 46, args: 29

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `cachetools-7.0.5/src/cachetools/keys.py` -> **Severity: 6.209** (Embedded: 0.1053 * Error Risk: 58.9862%)
- `cachetools-7.0.5/src/cachetools/_cachedmethod.py` -> **Severity: 2.941** (Embedded: 0.0526 * Error Risk: 55.8833%)
- `cachetools-7.0.5/src/cachetools/_cached.py` -> **Severity: 2.581** (Embedded: 0.0526 * Error Risk: 49.0315%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cachetools-7.0.5/src/cachetools/keys.py` -> **Severity: 9395.651** (Blast Radius: 115.385 * Doc Risk: 81.4287%)
- `cachetools-7.0.5/src/cachetools/_cachedmethod.py` -> **Severity: 5418.006** (Blast Radius: 60.897 * Doc Risk: 88.97%)
- `cachetools-7.0.5/src/cachetools/func.py` -> **Severity: 4877.124** (Blast Radius: 79.06 * Doc Risk: 61.6889%)
- `cachetools-7.0.5/src/cachetools/_cached.py` -> **Severity: 4858.606** (Blast Radius: 60.897 * Doc Risk: 79.784%)
- `cachetools-7.0.5/src/cachetools/__init__.py` -> **Severity: 2889.365** (Blast Radius: 42.735 * Doc Risk: 67.6112%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
