# ARCHITECTURAL_BRIEF: more-itertools
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/more-itertools` |
| **Timestamp** | `2026-08-03T21:22:25.151881+00:00` |
| **Scan Duration** | `0.75s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 10 malicious artifacts.

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
| Total Artifacts | 26 |
| Analyzed Artifacts (Scanned) | 15 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 11 |
| Total LOC | 10498 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 57.7% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 9 | 10467 | 60.0% |
| PLAINTEXT | 5 | 0 | 33.3% |
| MAKEFILE | 1 | 31 | 6.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.073`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 4 | 26.7% |
| file_cluster_13 | 2 | 13.3% |
| file_cluster_7 | 2 | 13.3% |
| file_cluster_16 | 2 | 13.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 33.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 11*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 22 LOC)
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 16.9 | 5.2 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 27.3 | 6.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 30.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 24.5 | 1.4 | 80.0 |
| API Exposure | 0.0 | 13.8 | 5.6 | 4.1 | 0.0 |
| Concurrency Exposure | 0.0 | 16.1 | 1.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 93.7 | 13.9 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 5.0 | 1.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 74.0 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 52.1 | 56.4 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 40.2 | 1.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 40.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `more_itertools-11.0.1/MANIFEST.in` (Hits: 0)
- `more_itertools-11.0.1/requirements/development.txt` (Hits: 0)
- `more_itertools-11.0.1/requirements/packaging.txt` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **MANIFEST.in** (`more_itertools-11.0.1/MANIFEST.in`) — 0 inbound connections
2. **development.txt** (`more_itertools-11.0.1/requirements/development.txt`) — 0 inbound connections
3. **packaging.txt** (`more_itertools-11.0.1/requirements/packaging.txt`) — 0 inbound connections
4. **testing.txt** (`more_itertools-11.0.1/requirements/testing.txt`) — 0 inbound connections
5. **typechecks.txt** (`more_itertools-11.0.1/requirements/typechecks.txt`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_more.py** (`more_itertools-11.0.1/tests/test_more.py`) — 25 outbound dependencies
2. **more.py** (`more_itertools-11.0.1/more_itertools/more.py`) — 23 outbound dependencies
3. **test_recipes.py** (`more_itertools-11.0.1/tests/test_recipes.py`) — 13 outbound dependencies
4. **recipes.py** (`more_itertools-11.0.1/more_itertools/recipes.py`) — 11 outbound dependencies
5. **more.pyi** (`more_itertools-11.0.1/more_itertools/more.pyi`) — 10 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `test_basic` (@ `more_itertools-11.0.1/tests/test_more.py`) -> Impact: **3148.3** | LOC: 4042
- `_islice_helper` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> Impact: **207.9** | LOC: 106
- `distinct_permutations` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> Impact: **187.3** | LOC: 108
  * *Intent:* # If either the start or stop index is negative, we'll need to cache # the rest of the iterable in order to slice from the right side. if (start < 0) ...
- `minmax` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> Impact: **169.9** | LOC: 43
- `set_partitions` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> Impact: **149.7** | LOC: 43
- `_get_slice` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> Impact: **79.2** | LOC: 25
- `collapse` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> Impact: **67.8** | LOC: 35
  * *Intent:* # If no such index exists, this permutation is the last one else: return # Find the largest index j greater than j such that A[i] < A[j] for j in rang...
- `replace` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> Impact: **63.1** | LOC: 37
  * *Intent:* """ iterator = iter(iterable) iterator_with_repeat = chain(iterator, repeat(fillvalue)) if n is None: return iterator_with_repeat elif n < 1: raise Va...
- `one` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> Impact: **60.6** | LOC: 13
- `interleave_evenly` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> Impact: **58.4** | LOC: 43

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `test_basic` (@ `more_itertools-11.0.1/tests/test_more.py`) -> **O(2^N) [Recursive]**
- `minmax` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> **O(2^N) [Recursive]**
- `one` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> **O(2^N) [Recursive]**
- `last` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> **O(2^N) [Recursive]**
- `result` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> **O(2^N) [Recursive]**
- `first` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> **O(2^N) [Recursive]**
- `__getitem__` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # Check if done iterating
- `done` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> **O(2^N) [Recursive]**
- `distinct_permutations` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> **O(N^6)**
  * *Intent:* # If either the start or stop index is negative, we'll need to cache # the rest of the iterable in order to slice from the right side. if (start < 0) ...
- `_get_values` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> **O(N^6)**

### Highest Data Gravity (Database Complexity)
- `test_basic` (@ `more_itertools-11.0.1/tests/test_more.py`) -> DB Complexity: **15**
- `__init__` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> DB Complexity: **8**
  * *Intent:* # If we've cached some items that match the target value, emit # the first one and evict it from the cache. if self._cache[value]: yield self._cache[v...
- `__init__` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> DB Complexity: **8**
- `__init__` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> DB Complexity: **6**
- `__init__` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> DB Complexity: **4**
- `__init__` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> DB Complexity: **4**
- `__init__` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> DB Complexity: **4**
- `zip_offset` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> DB Complexity: **3**
- `__next__` (@ `more_itertools-11.0.1/more_itertools/more.py`) -> DB Complexity: **3**
  * *Intent:* """ children = tee(iterable, len(offsets)) return zip_offset( *children, offsets=offsets, longest=longest, fillvalue=fillvalue ) def zip_offset(*itera...
- `__init__` (@ `more_itertools-11.0.1/tests/test_more.py`) -> DB Complexity: **3**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `more_itertools-11.0.1/tests` | 3 | 7010.82 | 3.23% | 0.0% |
| `more_itertools-11.0.1/more_itertools` | 6 | 5422.74 | 5.97% | 50.72% |
| `more_itertools-11.0.1` | 2 | 11.72 | 3.03% | 0.0% |
| `more_itertools-11.0.1/requirements` | 4 | 4.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `more_itertools-11.0.1/more_itertools/more.pyi` -> **99.9988%** Exposure
- `more_itertools-11.0.1/more_itertools/more.py` -> **99.8145%** Exposure
- `more_itertools-11.0.1/more_itertools/recipes.pyi` -> **93.691%** Exposure
- `more_itertools-11.0.1/more_itertools/recipes.py` -> **10.8042%** Exposure
### Highest State Flux (Mutation/Volatility)
- `more_itertools-11.0.1/more_itertools/more.py` -> **93.7087%** Exposure
- `more_itertools-11.0.1/more_itertools/recipes.py` -> **45.5411%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `more_itertools-11.0.1/tests/test_more.py` -> **140** Orphaned Functions | **94** Duplicates
- `more_itertools-11.0.1/tests/test_recipes.py` -> **92** Orphaned Functions | **49** Duplicates
- `more_itertools-11.0.1/more_itertools/more.pyi` -> **0** Orphaned Functions | **53** Duplicates
- `more_itertools-11.0.1/more_itertools/more.py` -> **0** Orphaned Functions | **49** Duplicates
- `more_itertools-11.0.1/more_itertools/recipes.pyi` -> **0** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`more_itertools-11.0.1/more_itertools/more.py`** -> AI Confidence: **99.31%**
2. **`more_itertools-11.0.1/more_itertools/recipes.py`** -> AI Confidence: **99.24%**
3. **`more_itertools-11.0.1/tests/test_more.py`** -> AI Confidence: **99.16%**
4. **`more_itertools-11.0.1/tests/test_recipes.py`** -> AI Confidence: **99.16%**
5. **`more_itertools-11.0.1/more_itertools/more.pyi`** -> AI Confidence: **99.09%**
6. **`more_itertools-11.0.1/Makefile`** -> AI Confidence: **98.84%**
7. **`more_itertools-11.0.1/more_itertools/__init__.py`** -> AI Confidence: **98.84%**
8. **`more_itertools-11.0.1/more_itertools/__init__.pyi`** -> AI Confidence: **98.84%**
9. **`more_itertools-11.0.1/more_itertools/recipes.pyi`** -> AI Confidence: **98.84%**
10. **`more_itertools-11.0.1/tests/__init__.py`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `more_itertools-11.0.1/more_itertools/more.py` -> **100.0%** Exposure
- `more_itertools-11.0.1/more_itertools/recipes.py` -> **100.0%** Exposure
- `more_itertools-11.0.1/tests/test_more.py` -> **100.0%** Exposure
- `more_itertools-11.0.1/tests/test_recipes.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `more_itertools-11.0.1/more_itertools/more.py` -> **100.0%** Exposure
- `more_itertools-11.0.1/more_itertools/recipes.py` -> **100.0%** Exposure
- `more_itertools-11.0.1/tests/test_more.py` -> **100.0%** Exposure
- `more_itertools-11.0.1/tests/test_recipes.py` -> **100.0%** Exposure
- `more_itertools-11.0.1/more_itertools/more.pyi` -> **1.9704%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `86` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `more_itertools-11.0.1/more_itertools/more.py` (PYTHON) -> Cumulative Risk: **772.18**
- **Archetype:** `file_cluster_7` (Distance: 12.625 IQR)
- **Magnitude:** 4230.66 | **LOC:** 5584 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.8145%)
- **Heaviest Functions:** `_islice_helper` (Impact: 207.9), `distinct_permutations` (Impact: 187.3), `minmax` (Impact: 169.9)

### 2. `more_itertools-11.0.1/more_itertools/recipes.py` (PYTHON) -> Cumulative Risk: **599.35**
- **Archetype:** `file_cluster_7` (Distance: 11.018 IQR)
- **Magnitude:** 722.28 | **LOC:** 1477 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (93.0221%)
- **Heaviest Functions:** `iter_index` (Impact: 56.8), `factor` (Impact: 35.8), `partition` (Impact: 35.7)

### 3. `more_itertools-11.0.1/more_itertools/more.pyi` (PYTHON) -> Cumulative Risk: **479.72**
- **Archetype:** `file_cluster_16` (Distance: 7.756 IQR)
- **Magnitude:** 359.06 | **LOC:** 1006 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9988%), Documentation (99.6799%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Impact: 1.8), `__init__` (Impact: 1.8), `__exit__` (Impact: 1.8)

### 4. `more_itertools-11.0.1/more_itertools/recipes.pyi` (PYTHON) -> Cumulative Risk: **400.11**
- **Archetype:** `file_cluster_16` (Distance: 7.701 IQR)
- **Magnitude:** 88.14 | **LOC:** 212 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9896%), Tech Debt (93.691%), Stability (50.0%)
- **Heaviest Functions:** `grouper` (Impact: 1.2), `unique` (Impact: 1.2), `iter_except` (Impact: 1.2)

### 5. `more_itertools-11.0.1/tests/test_more.py` (PYTHON) -> Cumulative Risk: **373.84**
- **Archetype:** `file_cluster_8` (Distance: 11.345 IQR)
- **Magnitude:** 5628.92 | **LOC:** 6892 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Stability (50.0%)
- **Heaviest Functions:** `test_basic` (Impact: 3148.3), `test_concurrent_consumers` (Impact: 54.2), `test_concurrent_calls` (Impact: 36.3)

### 6. `more_itertools-11.0.1/tests/test_recipes.py` (PYTHON) -> Cumulative Risk: **367.95**
- **Archetype:** `file_cluster_8` (Distance: 10.81 IQR)
- **Magnitude:** 1371.38 | **LOC:** 1658 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Stability (50.0%)
- **Heaviest Functions:** `test_basic` (Impact: 38.8), `test_start` (Impact: 37.3), `test_vs_statistics_median_windowed` (Impact: 33.1)

### 7. `more_itertools-11.0.1/Makefile` (MAKEFILE) -> Cumulative Risk: **266.8**
- **Archetype:** `file_cluster_8` (Distance: 6.107 IQR)
- **Magnitude:** 10.72 | **LOC:** 39 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (95.9351%), Stability (50.0%), Api Exposure (12.4839%)
- **Heaviest Functions:** `test` (Impact: 1.1)

### 8. `more_itertools-11.0.1/more_itertools/__init__.py` (PYTHON) -> Cumulative Risk: **175.28**
- **Archetype:** `file_cluster_13` (Distance: 8.75 IQR)
- **Magnitude:** 11.56 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Safety Score (80.0%), Stability (50.0%), Spec Match (20.0%), Documentation (19.8253%)

### 9. `more_itertools-11.0.1/more_itertools/__init__.pyi` (PYTHON) -> Cumulative Risk: **161.97**
- **Archetype:** `file_cluster_13` (Distance: 6.786 IQR)
- **Magnitude:** 11.04 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Safety Score (80.0%), Stability (50.0%), Spec Match (13.3333%), Documentation (13.3333%)

### 10. `more_itertools-11.0.1/tests/__init__.py` (PYTHON) -> Cumulative Risk: **61.67**
- **Archetype:** `file_cluster_8` (Distance: 4.447 IQR)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (6.6667%), Cognitive Load (5.0%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `more_itertools-11.0.1/tests/test_more.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.345 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.141 IQR)
- **Top Global Matches:** file_cluster_8: 11.345, file_cluster_7: 11.62, file_cluster_1: 11.891
- **Magnitude:** 5628.92 | **LOC:** 6892 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (2.7429%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_basic` (Impact: 3148.3 | O(2^N) | DB: 15)
  * `test_concurrent_consumers` (Impact: 54.2 | O(N^5) | DB: 1)
  * `test_concurrent_calls` (Impact: 36.3 | O(N^4))
  * `test_concurrent_calls` (Impact: 31.7 | O(N^4) | DB: 1)
  * `test_many_iters` (Impact: 26.9 | O(N^4) | DB: 1)
    * *Intent:* # smoke test with many iterables: create iterables with a random # number of elements starting with ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 410`, `structural_boundaries: 868`, `args: 774`, `func_start: 634`, `class_start: 126`
* *Risk/State:* `safety_bypasses: 71`, `state_mutation: 52`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 94`, `orphaned_logic: 140`
* *Architecture:* `api: 727`, `concurrency: 1`, `import: 25`
* *Defense:* `safety: 14`, `doc: 212`, `test: 719`, `sync_locks: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` time, pickle, logging, string, collections, datetime, __future__, more_itertools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/more_itertools/more.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_7` (Drift: 12.625 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.635 IQR)
- **Top Global Matches:** file_cluster_7: 12.625, file_cluster_13: 12.664, file_cluster_8: 12.682
- **Magnitude:** 4230.66 | **LOC:** 5584 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (16.9055%), Tech Debt (99.8145%)
**Top Internal Functions/Classes:**
  * `_islice_helper` (Impact: 207.9 | O(N^5) | DB: 1)
  * `distinct_permutations` (Impact: 187.3 | O(N^6) | DB: 1)
    * *Intent:* # If either the start or stop index is negative, we'll need to cache # the rest of the iterable in o...
  * `minmax` (Impact: 169.9 | O(2^N))
  * `set_partitions` (Impact: 149.7 | O(N^5))
  * `_get_slice` (Impact: 79.2 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 648`, `structural_boundaries: 540`, `args: 217`, `func_start: 206`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 263`, `dead_code: 4`, `planned_debt: 1`, `duplicate_logic: 49`
* *Architecture:* `api: 159`, `concurrency: 7`, `import: 19`
* *Defense:* `safety: 91`, `doc: 248`, `sync_locks: 3`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` time, collections, datetime, .recipes, more_itertools, itertools, operator, heapq...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/tests/test_recipes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.81 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.256 IQR)
- **Top Global Matches:** file_cluster_8: 10.81, file_cluster_7: 11.102, file_cluster_1: 11.36
- **Magnitude:** 1371.38 | **LOC:** 1658 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (1.9448%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_basic` (Impact: 38.8 | O(N^5))
  * `test_start` (Impact: 37.3 | O(N^6) | DB: 1)
  * `test_vs_statistics_median_windowed` (Impact: 33.1 | O(N^5))
  * `test_multidimensional` (Impact: 32.9 | O(N^4))
    * *Intent:* # Empty input self.assertEqual(list(reshape([[]], shape=(1,))), []) # Non-uniform input: scalar wher...
  * `test_vs_statistics_median` (Impact: 32.1 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 245`, `args: 156`, `func_start: 146`, `class_start: 54`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 7`, `duplicate_logic: 49`, `orphaned_logic: 92`
* *Architecture:* `api: 197`, `import: 14`
* *Defense:* `safety: 7`, `doc: 140`, `test: 197`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collections, statistics, unittest.mock, doctest, math, decimal, functools, more_itertools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/more_itertools/recipes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_7` (Drift: 11.018 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.476 IQR)
- **Top Global Matches:** file_cluster_7: 11.018, file_cluster_13: 11.021, file_cluster_8: 11.064
- **Magnitude:** 722.28 | **LOC:** 1477 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (8.9057%), Tech Debt (10.8042%)
**Top Internal Functions/Classes:**
  * `iter_index` (Impact: 56.8 | O(N^4) | DB: 1)
  * `factor` (Impact: 35.8 | O(N^3) | DB: 1)
  * `partition` (Impact: 35.7 | O(N^4) | DB: 1)
  * `grouper` (Impact: 32.0 | O(N^3))
  * `is_prime` (Impact: 32.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 178`, `args: 64`, `func_start: 64`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 27`, `planned_debt: 3`
* *Architecture:* `api: 53`, `import: 14`
* *Defense:* `safety: 15`, `doc: 104`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collections, contextlib, math, functools, more_itertools, bisect, random, itertools...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/more_itertools/more.pyi` (PYTHON | Tier 0 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_16` (Drift: 7.756 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.258 IQR)
- **Top Global Matches:** file_cluster_16: 7.756, file_cluster_8: 8.466, file_cluster_0: 8.531
- **Magnitude:** 359.06 | **LOC:** 1006 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (99.9988%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 1.8 | O(N^2))
  * `__init__` (Impact: 1.8 | O(N^2))
  * `__exit__` (Impact: 1.8 | O(N^2))
  * `__reduce__` (Impact: 1.6 | O(N^2))
  * `__init__` (Impact: 1.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 282`, `args: 227`, `func_start: 227`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 29`, `duplicate_logic: 53`
* *Architecture:* `api: 186`, `concurrency: 1`, `import: 10`
* *Defense:* `safety: 2`, `doc: 2`, `sync_locks: 2`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` contextlib, typing_extensions, decimal, __future__, typing, types, dataclasses, threading...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/more_itertools/recipes.pyi` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_16` (Drift: 7.701 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.568 IQR)
- **Top Global Matches:** file_cluster_16: 7.701, file_cluster_8: 8.627, file_cluster_7: 8.729
- **Magnitude:** 88.14 | **LOC:** 212 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (93.691%)
**Top Internal Functions/Classes:**
  * `grouper` (Impact: 1.2 | O(N^1))
  * `unique` (Impact: 1.2 | O(N^1))
  * `iter_except` (Impact: 1.2 | O(N^1))
  * `iter_except` (Impact: 1.2 | O(N^1))
  * `first_true` (Impact: 1.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 74`, `args: 60`, `func_start: 60`
* *Risk/State:* `safety_bypasses: 8`, `duplicate_logic: 4`
* *Architecture:* `api: 56`, `import: 5`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` decimal, __future__, typing, collections.abc, fractions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/more_itertools/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.75 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.373 IQR)
- **Top Global Matches:** file_cluster_13: 8.75, file_cluster_8: 9.206, file_cluster_7: 9.411
- **Magnitude:** 11.56 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `import: 2`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .recipes, .more
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/more_itertools/__init__.pyi` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 6.786 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.717 IQR)
- **Top Global Matches:** file_cluster_13: 6.786, file_cluster_8: 7.333, file_cluster_7: 8.416
- **Magnitude:** 11.04 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .recipes, .more
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.107 IQR)
- **Top Global Matches:** file_cluster_8: 6.107, file_cluster_7: 7.344, file_cluster_1: 7.559
- **Magnitude:** 10.72 | **LOC:** 39 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.0677%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 8`
* *Risk/State:* None
* *Architecture:* `api: 9`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/tests/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/MANIFEST.in` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/requirements/development.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/requirements/packaging.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 5 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/requirements/testing.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `more_itertools-11.0.1/requirements/typechecks.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 66.667
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `more_itertools-11.0.1/more_itertools/__init__.py` (PYTHON) | Magnitude: 11.56 | Delta: **0.456 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, safety_bypasses: 2, doc: 2, import: 2
- `more_itertools-11.0.1/more_itertools/__init__.pyi` (PYTHON) | Magnitude: 11.04 | Delta: **0.547 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, safety_bypasses: 2, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `more_itertools-11.0.1/more_itertools/more.pyi` (PYTHON) | Magnitude: 359.06 | Delta: **0.71 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: encapsulation: 748, indent_spaces: 574, generics: 415, structural_boundaries: 282

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `more_itertools-11.0.1/more_itertools/recipes.py` (PYTHON) | Magnitude: 722.28 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 424, structural_boundaries: 178, branch: 128, doc: 104
- `more_itertools-11.0.1/more_itertools/more.py` (PYTHON) | Magnitude: 4230.66 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1948, branch: 648, structural_boundaries: 540, encapsulation: 326

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `more_itertools-11.0.1/tests/test_more.py` (PYTHON) | Magnitude: 5628.92 | Delta: **0.275 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 5301, structural_boundaries: 868, args: 774, api: 727
- `more_itertools-11.0.1/tests/test_recipes.py` (PYTHON) | Magnitude: 1371.38 | Delta: **0.292 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 1161, structural_boundaries: 245, api: 197, test: 197

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `more_itertools-11.0.1/more_itertools/recipes.pyi` -> **Severity: 6666.007** (Blast Radius: 66.667 * Doc Risk: 99.9896%)
- `more_itertools-11.0.1/more_itertools/more.pyi` -> **Severity: 6645.36** (Blast Radius: 66.667 * Doc Risk: 99.6799%)
- `more_itertools-11.0.1/more_itertools/more.py` -> **Severity: 6623.08** (Blast Radius: 66.667 * Doc Risk: 99.3457%)
- `more_itertools-11.0.1/Makefile` -> **Severity: 6395.705** (Blast Radius: 66.667 * Doc Risk: 95.9351%)
- `more_itertools-11.0.1/more_itertools/recipes.py` -> **Severity: 6201.504** (Blast Radius: 66.667 * Doc Risk: 93.0221%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
