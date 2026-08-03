# ARCHITECTURAL_BRIEF: markupsafe
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/markupsafe` |
| **Timestamp** | `2026-08-03T21:22:16.099946+00:00` |
| **Scan Duration** | `0.15s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 11 malicious artifacts.

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
| Total Artifacts | 21 |
| Analyzed Artifacts (Scanned) | 14 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7 |
| Total LOC | 695 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 66.7% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 10 | 518 | 71.4% |
| PLAINTEXT | 2 | 0 | 14.3% |
| MARKDOWN | 1 | 0 | 7.1% |
| C | 1 | 177 | 7.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.071`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 5 | 35.7% |
| file_cluster_8 | 4 | 28.6% |
| file_cluster_16 | 2 | 14.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 21.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7*

**Composition by Extension & Reason:**
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 2.5 | 74.3 | 13.6 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.3 | 22.8 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 99.9 | 9.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 14.9 | 0.0 | 0.0 |
| API Exposure | 0.0 | 11.1 | 3.1 | 2.8 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 13.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 75.8 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 32.5 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 26.6 | 2.3 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 9.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 2.3 | 0.2 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `markupsafe-3.0.3/tests/test_ext_init.py` (Hits: 3)
- `markupsafe-3.0.3/setup.py` (Hits: 2)
- `markupsafe-3.0.3/LICENSE.txt` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **_native.py** (`markupsafe-3.0.3/src/markupsafe/_native.py`) — 1 inbound connections
2. **LICENSE.txt** (`markupsafe-3.0.3/LICENSE.txt`) — 0 inbound connections
3. **MANIFEST.in** (`markupsafe-3.0.3/MANIFEST.in`) — 0 inbound connections
4. **README.md** (`markupsafe-3.0.3/README.md`) — 0 inbound connections
5. **setup.py** (`markupsafe-3.0.3/setup.py`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`markupsafe-3.0.3/src/markupsafe/__init__.py`) — 10 outbound dependencies
2. **setup.py** (`markupsafe-3.0.3/setup.py`) — 6 outbound dependencies
3. **test_escape.py** (`markupsafe-3.0.3/tests/test_escape.py`) — 4 outbound dependencies
4. **test_ext_init.py** (`markupsafe-3.0.3/tests/test_ext_init.py`) — 4 outbound dependencies
5. **test_leak.py** (`markupsafe-3.0.3/tests/test_leak.py`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `format_field` (@ `markupsafe-3.0.3/src/markupsafe/__init__.py`) -> Impact: **72.8** | LOC: 16
- `__mod__` (@ `markupsafe-3.0.3/src/markupsafe/__init__.py`) -> Impact: **48.6** | LOC: 12
- `build_extension` (@ `markupsafe-3.0.3/setup.py`) -> Impact: **26.5** | LOC: 10
- `__add__` (@ `markupsafe-3.0.3/src/markupsafe/__init__.py`) -> Impact: **24.2** | LOC: 5
- `striptags` (@ `markupsafe-3.0.3/src/markupsafe/__init__.py`) -> Impact: **23.0** | LOC: 26
- `__getattr__` (@ `markupsafe-3.0.3/src/markupsafe/__init__.py`) -> Impact: **16.8** | LOC: 15
- `escape` (@ `markupsafe-3.0.3/src/markupsafe/__init__.py`) -> Impact: **16.4** | LOC: 9
- `run` (@ `markupsafe-3.0.3/setup.py`) -> Impact: **14.1** | LOC: 5
- `test_ext_init` (@ `markupsafe-3.0.3/tests/test_ext_init.py`) -> Impact: **13.6** | LOC: 13
  * *Intent:* """Test that the extension module uses multi-phase init by checking that uncached imports result in different module objects. """
- `__radd__` (@ `markupsafe-3.0.3/src/markupsafe/__init__.py`) -> Impact: **12.2** | LOC: 5
  * *Intent:* """A string that is ready to be safely inserted into an HTML or XML document, either because it was escaped or because it was marked safe. Passing an ...

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `format_field` (@ `markupsafe-3.0.3/src/markupsafe/__init__.py`) -> **O(2^N) [Recursive]**
- `build_extension` (@ `markupsafe-3.0.3/setup.py`) -> **O(2^N) [Recursive]**
- `run` (@ `markupsafe-3.0.3/setup.py`) -> **O(2^N) [Recursive]**
- `__mod__` (@ `markupsafe-3.0.3/src/markupsafe/__init__.py`) -> **O(2^N) [Recursive]**
- `__add__` (@ `markupsafe-3.0.3/src/markupsafe/__init__.py`) -> **O(2^N) [Recursive]**
- `escape` (@ `markupsafe-3.0.3/src/markupsafe/__init__.py`) -> **O(2^N) [Recursive]**
- `replace` (@ `markupsafe-3.0.3/src/markupsafe/__init__.py`) -> **O(2^N) [Recursive]**
- `ljust` (@ `markupsafe-3.0.3/src/markupsafe/__init__.py`) -> **O(2^N) [Recursive]**
  * *Intent:* """ from html import unescape return unescape(str(self)) def striptags(self, /) -> str: """:meth:`unescape` the markup, remove tags, and normalize whi...
- `rjust` (@ `markupsafe-3.0.3/src/markupsafe/__init__.py`) -> **O(2^N) [Recursive]**
- `center` (@ `markupsafe-3.0.3/src/markupsafe/__init__.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `test_ext_init` (@ `markupsafe-3.0.3/tests/test_ext_init.py`) -> DB Complexity: **6**
  * *Intent:* """Test that the extension module uses multi-phase init by checking that uncached imports result in different module objects. """
- `escape_unicode_kind1` (@ `markupsafe-3.0.3/src/markupsafe/_speedups.c`) -> DB Complexity: **6**
- `escape_unicode_kind2` (@ `markupsafe-3.0.3/src/markupsafe/_speedups.c`) -> DB Complexity: **6**
- `escape_unicode_kind4` (@ `markupsafe-3.0.3/src/markupsafe/_speedups.c`) -> DB Complexity: **6**
- `striptags` (@ `markupsafe-3.0.3/src/markupsafe/__init__.py`) -> DB Complexity: **4**
- `build_extension` (@ `markupsafe-3.0.3/setup.py`) -> DB Complexity: **3**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `markupsafe-3.0.3/src/markupsafe` | 4 | 814.62 | 25.78% | 24.98% |
| `markupsafe-3.0.3/tests` | 6 | 111.92 | 6.79% | 0.0% |
| `markupsafe-3.0.3` | 4 | 64.32 | 1.36% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `markupsafe-3.0.3/src/markupsafe/__init__.py` -> **99.9362%** Exposure
### Highest State Flux (Mutation/Volatility)
- `markupsafe-3.0.3/src/markupsafe/_speedups.c` -> **100.0%** Exposure
- `markupsafe-3.0.3/src/markupsafe/__init__.py` -> **50.6923%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `markupsafe-3.0.3/src/markupsafe/__init__.py` -> **0** Orphaned Functions | **8** Duplicates
- `markupsafe-3.0.3/tests/test_exception_custom_html.py` -> **2** Orphaned Functions | **0** Duplicates
- `markupsafe-3.0.3/tests/test_ext_init.py` -> **1** Orphaned Functions | **0** Duplicates
- `markupsafe-3.0.3/tests/test_leak.py` -> **1** Orphaned Functions | **0** Duplicates
- `markupsafe-3.0.3/tests/test_markupsafe.py` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`markupsafe-3.0.3/src/markupsafe/__init__.py`** -> AI Confidence: **99.07%**
2. **`markupsafe-3.0.3/src/markupsafe/_speedups.c`** -> AI Confidence: **99.06%**
3. **`markupsafe-3.0.3/setup.py`** -> AI Confidence: **98.93%**
4. **`markupsafe-3.0.3/tests/test_exception_custom_html.py`** -> AI Confidence: **98.87%**
5. **`markupsafe-3.0.3/tests/test_ext_init.py`** -> AI Confidence: **98.85%**
6. **`markupsafe-3.0.3/src/markupsafe/_native.py`** -> AI Confidence: **98.84%**
7. **`markupsafe-3.0.3/src/markupsafe/_speedups.pyi`** -> AI Confidence: **98.84%**
8. **`markupsafe-3.0.3/tests/__init__.py`** -> AI Confidence: **98.84%**
9. **`markupsafe-3.0.3/tests/test_escape.py`** -> AI Confidence: **98.84%**
10. **`markupsafe-3.0.3/tests/test_markupsafe.py`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `markupsafe-3.0.3/tests/test_escape.py` -> **0.0001%** Exposure
### Exploit Generation Surface
- `markupsafe-3.0.3/src/markupsafe/__init__.py` -> **100.0%** Exposure
- `markupsafe-3.0.3/setup.py` -> **7.1334%** Exposure
### Raw Memory Manipulation
- `markupsafe-3.0.3/src/markupsafe/_speedups.c` -> **2.3169%** Exposure
### Algorithmic DoS Exposure
- `markupsafe-3.0.3/src/markupsafe/__init__.py` -> **100.0%** Exposure
- `markupsafe-3.0.3/setup.py` -> **99.9365%** Exposure
- `markupsafe-3.0.3/tests/test_ext_init.py` -> **77.7041%** Exposure
- `markupsafe-3.0.3/tests/test_exception_custom_html.py` -> **6.7547%** Exposure
- `markupsafe-3.0.3/tests/test_leak.py` -> **5.348%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `34` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `markupsafe-3.0.3/src/markupsafe/__init__.py` (PYTHON) -> Cumulative Risk: **769.33**
- **Archetype:** `file_cluster_16` (Distance: 11.245 IQR)
- **Magnitude:** 490.86 | **LOC:** 397 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9995%)
- **Heaviest Functions:** `format_field` (Impact: 72.8), `__mod__` (Impact: 48.6), `__add__` (Impact: 24.2)

### 2. `markupsafe-3.0.3/src/markupsafe/_speedups.c` (C) -> Cumulative Risk: **539.14**
- **Archetype:** `file_cluster_8` (Distance: 13.551 IQR)
- **Magnitude:** 304.94 | **LOC:** 201 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.7251%), Safety Score (99.3464%)
- **Heaviest Functions:** `escape_unicode` (Impact: 8.1), `escape_unicode_kind1` (Impact: 5.2), `escape_unicode_kind2` (Impact: 4.2)

### 3. `markupsafe-3.0.3/setup.py` (PYTHON) -> Cumulative Risk: **450.53**
- **Archetype:** `file_cluster_13` (Distance: 9.722 IQR)
- **Magnitude:** 61.3 | **LOC:** 83 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9365%), Documentation (97.3418%), Verification (80.0%)
- **Heaviest Functions:** `build_extension` (Impact: 26.5), `run` (Impact: 14.1), `run_setup` (Impact: 8.0)

### 4. `markupsafe-3.0.3/tests/test_ext_init.py` (PYTHON) -> Cumulative Risk: **247.36**
- **Archetype:** `file_cluster_13` (Distance: 11.526 IQR)
- **Magnitude:** 14.94 | **LOC:** 29 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (77.7041%), Stability (50.0%), Cognitive Load (19.3686%)
- **Heaviest Functions:** `test_ext_init` (Impact: 13.6)

### 5. `markupsafe-3.0.3/tests/test_markupsafe.py` (PYTHON) -> Cumulative Risk: **234.21**
- **Archetype:** `file_cluster_8` (Distance: 6.762 IQR)
- **Magnitude:** 5.76 | **LOC:** 209 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (80.0%), Stability (50.0%), Cognitive Load (2.9103%)
- **Heaviest Functions:** `test_adding` (Impact: 1.8)

### 6. `markupsafe-3.0.3/src/markupsafe/_native.py` (PYTHON) -> Cumulative Risk: **168.15**
- **Archetype:** `file_cluster_8` (Distance: 6.591 IQR)
- **Magnitude:** 4.16 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (53.3333%), Documentation (53.3154%), Stability (50.0%), Cognitive Load (5.0%)
- **Heaviest Functions:** `_escape_inner` (Impact: 3.0)

### 7. `markupsafe-3.0.3/tests/test_leak.py` (PYTHON) -> Cumulative Risk: **163.35**
- **Archetype:** `file_cluster_13` (Distance: 8.876 IQR)
- **Magnitude:** 12.62 | **LOC:** 29 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Cognitive Load (5.9601%), Algorithmic Dos (5.348%)
- **Heaviest Functions:** `test_markup_leaks` (Impact: 11.3)

### 8. `markupsafe-3.0.3/tests/test_escape.py` (PYTHON) -> Cumulative Risk: **156.83**
- **Archetype:** `file_cluster_13` (Distance: 11.348 IQR)
- **Magnitude:** 57.68 | **LOC:** 69 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Api Exposure (2.8116%), Cognitive Load (2.4938%)

### 9. `markupsafe-3.0.3/tests/test_exception_custom_html.py` (PYTHON) -> Cumulative Risk: **131.83**
- **Archetype:** `file_cluster_13` (Distance: 10.246 IQR)
- **Magnitude:** 10.4 | **LOC:** 24 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (66.6667%), Stability (50.0%), Algorithmic Dos (6.7547%), Cognitive Load (5.0%)
- **Heaviest Functions:** `test_exception_custom_html` (Impact: 5.5), `__html__` (Impact: 2.7)

### 10. `markupsafe-3.0.3/src/markupsafe/_speedups.pyi` (PYTHON) -> Cumulative Risk: **68.49**
- **Archetype:** `file_cluster_16` (Distance: 8.768 IQR)
- **Magnitude:** 14.66 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (6.6667%), Documentation (6.6667%), Cognitive Load (5.0%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `markupsafe-3.0.3/src/markupsafe/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.245 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.742 IQR)
- **Top Global Matches:** file_cluster_16: 11.245, file_cluster_13: 11.528, file_cluster_8: 11.768
- **Magnitude:** 490.86 | **LOC:** 397 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (18.8051%), Tech Debt (99.9362%)
**Top Internal Functions/Classes:**
  * `format_field` (Impact: 72.8 | O(2^N))
  * `__mod__` (Impact: 48.6 | O(2^N))
  * `__add__` (Impact: 24.2 | O(2^N))
  * `striptags` (Impact: 23.0 | O(N^4) | DB: 4)
  * `__getattr__` (Impact: 16.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 138`, `args: 53`, `func_start: 53`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 12`, `duplicate_logic: 8`
* *Architecture:* `api: 45`, `import: 10`
* *Defense:* `safety: 14`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ._native, string, __future__, html, collections.abc, ._speedups, warnings, typing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `markupsafe-3.0.3/src/markupsafe/_speedups.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.551 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.222 IQR)
- **Top Global Matches:** file_cluster_8: 13.551, file_cluster_13: 13.776, file_cluster_0: 13.899
- **Magnitude:** 304.94 | **LOC:** 201 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (74.3101%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `escape_unicode` (Impact: 8.1 | O(N^1))
  * `escape_unicode_kind1` (Impact: 5.2 | O(N^1) | DB: 6)
  * `escape_unicode_kind2` (Impact: 4.2 | O(N^1) | DB: 6)
  * `escape_unicode_kind4` (Impact: 4.2 | O(N^1) | DB: 6)
  * `PyInit__speedups` (Impact: 1.7 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 18`, `args: 1`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 244`
* *Architecture:* `api: 34`, `import: 1`
* *Defense:* `safety: 1`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Python.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `markupsafe-3.0.3/setup.py` (PYTHON | Tier 1 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.722 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.224 IQR)
- **Top Global Matches:** file_cluster_13: 9.722, file_cluster_8: 9.759, file_cluster_7: 10.356
- **Magnitude:** 61.3 | **LOC:** 83 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (5.4491%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `build_extension` (Impact: 26.5 | O(2^N) | DB: 3)
  * `run` (Impact: 14.1 | O(2^N))
  * `run_setup` (Impact: 8.0 | O(N^2))
  * `show_message` (Impact: 5.4 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 28`, `args: 4`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `io: 2`, `api: 6`, `import: 9`
* *Defense:* `safety: 7`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` setuptools.command.build_ext, sys, setuptools, platform, setuptools.errors, os
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `markupsafe-3.0.3/tests/test_escape.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.348 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.267 IQR)
- **Top Global Matches:** file_cluster_13: 11.348, file_cluster_16: 11.368, file_cluster_0: 11.69
- **Magnitude:** 57.68 | **LOC:** 69 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.4938%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 28`, `args: 7`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `safety: 8`, `doc: 4`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` markupsafe, typing, pytest, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `markupsafe-3.0.3/tests/test_ext_init.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.526 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.807 IQR)
- **Top Global Matches:** file_cluster_13: 11.526, file_cluster_0: 11.867, file_cluster_17: 12.213
- **Magnitude:** 14.94 | **LOC:** 29 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (19.3686%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_ext_init` (Impact: 13.6 | O(N^2) | DB: 6)
    * *Intent:* """Test that the extension module uses multi-phase init by checking that uncached imports result in ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 11`, `args: 1`, `func_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 1`, `import: 5`
* *Defense:* `safety: 4`, `doc: 2`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` markupsafe._speedups, markupsafe, sys, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `markupsafe-3.0.3/src/markupsafe/_speedups.pyi` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_16` (Drift: 8.768 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.873 IQR)
- **Top Global Matches:** file_cluster_16: 8.768, file_cluster_8: 9.171, file_cluster_7: 10.072
- **Magnitude:** 14.66 | **LOC:** 2 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `markupsafe-3.0.3/tests/test_leak.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.876 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.05 IQR)
- **Top Global Matches:** file_cluster_13: 8.876, file_cluster_8: 9.185, file_cluster_0: 9.403
- **Magnitude:** 12.62 | **LOC:** 29 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.9601%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_markup_leaks` (Impact: 11.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 8`, `args: 1`, `func_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 1`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` gc, markupsafe, pytest, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `markupsafe-3.0.3/tests/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `markupsafe-3.0.3/tests/test_exception_custom_html.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.246 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.719 IQR)
- **Top Global Matches:** file_cluster_13: 10.246, file_cluster_16: 10.343, file_cluster_8: 10.592
- **Magnitude:** 10.4 | **LOC:** 24 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_exception_custom_html` (Impact: 5.5 | O(N^2))
    * *Intent:* """Checks whether exceptions in custom __html__ implementations are propagated correctly. There was ...
  * `__html__` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 8`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `fragile_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `doc: 2`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` markupsafe, pytest, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `markupsafe-3.0.3/tests/test_markupsafe.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.762 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.955 IQR)
- **Top Global Matches:** file_cluster_8: 6.762, file_cluster_13: 7.627, file_cluster_1: 7.754
- **Magnitude:** 5.76 | **LOC:** 209 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.9103%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_adding` (Impact: 1.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 32`, `args: 1`, `func_start: 3`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `test: 59`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` markupsafe, typing, pytest, __future__
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `markupsafe-3.0.3/src/markupsafe/_native.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.591 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.635 IQR)
- **Top Global Matches:** file_cluster_8: 6.591, file_cluster_16: 7.112, file_cluster_7: 7.711
- **Magnitude:** 4.16 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_escape_inner` (Impact: 3.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 124.579
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.076923
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `markupsafe-3.0.3/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.02 | **LOC:** 51 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `markupsafe-3.0.3/LICENSE.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 29 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `markupsafe-3.0.3/MANIFEST.in` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 67.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `markupsafe-3.0.3/tests/test_escape.py` (PYTHON) | Magnitude: 57.68 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 28, sec_reflection_metaprogramming: 12, test: 11
- `markupsafe-3.0.3/setup.py` (PYTHON) | Magnitude: 61.3 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 28, branch: 12, import: 9
- `markupsafe-3.0.3/tests/test_exception_custom_html.py` (PYTHON) | Magnitude: 10.4 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 5, test: 3, import: 3
- `markupsafe-3.0.3/tests/test_leak.py` (PYTHON) | Magnitude: 12.62 | Delta: **0.309 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 8, test: 4, import: 4
- `markupsafe-3.0.3/tests/test_ext_init.py` (PYTHON) | Magnitude: 14.94 | Delta: **0.341 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: encapsulation: 13, structural_boundaries: 11, indent_spaces: 9, test: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `markupsafe-3.0.3/src/markupsafe/__init__.py` (PYTHON) | Magnitude: 490.86 | Delta: **0.283 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 192, structural_boundaries: 138, encapsulation: 105, generics: 61
- `markupsafe-3.0.3/src/markupsafe/_speedups.pyi` (PYTHON) | Magnitude: 14.66 | Delta: **0.403 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, args: 1, func_start: 1, generics: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `markupsafe-3.0.3/src/markupsafe/_speedups.c` (C) | Magnitude: 304.94 | Delta: **0.225 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 244, indent_tabs: 144, pointers: 49, branch: 35
- `markupsafe-3.0.3/src/markupsafe/_native.py` (PYTHON) | Magnitude: 4.16 | Delta: **0.521 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 2, args: 1, func_start: 1
- `markupsafe-3.0.3/tests/test_markupsafe.py` (PYTHON) | Magnitude: 5.76 | Delta: **0.865 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 118, test: 59, sec_high_risk_execution: 38, structural_boundaries: 32

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `markupsafe-3.0.3/src/markupsafe/__init__.py` -> **Severity: 6733.966** (Blast Radius: 67.34 * Doc Risk: 99.9995%)
- `markupsafe-3.0.3/src/markupsafe/_speedups.c` -> **Severity: 6715.488** (Blast Radius: 67.34 * Doc Risk: 99.7251%)
- `markupsafe-3.0.3/src/markupsafe/_native.py` -> **Severity: 6641.979** (Blast Radius: 124.579 * Doc Risk: 53.3154%)
- `markupsafe-3.0.3/setup.py` -> **Severity: 6554.997** (Blast Radius: 67.34 * Doc Risk: 97.3418%)
- `markupsafe-3.0.3/src/markupsafe/_speedups.pyi` -> **Severity: 448.936** (Blast Radius: 67.34 * Doc Risk: 6.6667%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
