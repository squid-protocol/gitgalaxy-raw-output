# ARCHITECTURAL_BRIEF: python-dateutil
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/python-dateutil` |
| **Timestamp** | `2026-08-03T21:24:13.861717+00:00` |
| **Scan Duration** | `0.26s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 15 malicious artifacts.

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
| Total Artifacts | 24 |
| Analyzed Artifacts (Scanned) | 18 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6 |
| Total LOC | 3760 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 75.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4609 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4432 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 11.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9048 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 15 | 3735 | 83.3% |
| PLAINTEXT | 2 | 0 | 11.1% |
| JSON | 1 | 25 | 5.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.418`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 10 | 55.6% |
| file_cluster_13 | 6 | 33.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 11.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')
- `.gz`: 1x Excluded (Explicitly Denied Extension: '.gz')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 2.6 | 75.7 | 24.1 | 18.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 19.9 | 7.1 | 0.0 |
| Tech Debt Exposure | 0.0 | 98.2 | 32.2 | 4.8 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 40.8 | 41.8 | 80.0 |
| API Exposure | 0.0 | 4.2 | 1.5 | 1.2 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 46.1 | 32.8 | 0.0 |
| Commented Logic Exposure | 0.0 | 11.7 | 2.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 79.6 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 6.7 | 100.0 | 53.4 | 37.2 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 57.0 | 99.2 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 50.0 | 49.8 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `python-dateutil-2.6.1/dateutil/tz/tz.py` (Hits: 14)
- `python-dateutil-2.6.1/updatezinfo.py` (Hits: 4)
- `python-dateutil-2.6.1/dateutil/zoneinfo/__init__.py` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **tz.py** (`python-dateutil-2.6.1/dateutil/tz/tz.py`) — 3 inbound connections
2. **_version.py** (`python-dateutil-2.6.1/dateutil/_version.py`) — 2 inbound connections
3. **win.py** (`python-dateutil-2.6.1/dateutil/tz/win.py`) — 2 inbound connections
4. **relativedelta.py** (`python-dateutil-2.6.1/dateutil/relativedelta.py`) — 1 inbound connections
5. **tzwin.py** (`python-dateutil-2.6.1/dateutil/tzwin.py`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **tz.py** (`python-dateutil-2.6.1/dateutil/tz/tz.py`) — 14 outbound dependencies
2. **rrule.py** (`python-dateutil-2.6.1/dateutil/rrule.py`) — 13 outbound dependencies
3. **parser.py** (`python-dateutil-2.6.1/dateutil/parser.py`) — 12 outbound dependencies
4. **relativedelta.py** (`python-dateutil-2.6.1/dateutil/relativedelta.py`) — 7 outbound dependencies
5. **win.py** (`python-dateutil-2.6.1/dateutil/tz/win.py`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__init__` (@ `python-dateutil-2.6.1/dateutil/rrule.py`) -> Impact: **3216.5** | LOC: 254
- `__init__` (@ `python-dateutil-2.6.1/dateutil/relativedelta.py`) -> Impact: **2523.3** | LOC: 445
- `__str__` (@ `python-dateutil-2.6.1/dateutil/rrule.py`) -> Impact: **1644.0** | LOC: 871
- `__repr__` (@ `python-dateutil-2.6.1/dateutil/tz/tz.py`) -> Impact: **1077.1** | LOC: 445
  * *Intent:* # the hour near to a change is DST or not. # # timestamp = time.mktime((dt.year, dt.month, dt.day, dt.hour, # dt.minute, dt.second, dt.weekday(), 0, -...
- `_parse_rfc` (@ `python-dateutil-2.6.1/dateutil/tz/tz.py`) -> Impact: **521.0** | LOC: 236
- `_fromutc` (@ `python-dateutil-2.6.1/dateutil/tz/_common.py`) -> Impact: **335.5** | LOC: 162
- `get_token` (@ `python-dateutil-2.6.1/dateutil/parser.py`) -> Impact: **259.5** | LOC: 97
- `__repr__` (@ `python-dateutil-2.6.1/dateutil/tz/tz.py`) -> Impact: **181.3** | LOC: 93
- `between` (@ `python-dateutil-2.6.1/dateutil/rrule.py`) -> Impact: **130.1** | LOC: 30
- `__init__` (@ `python-dateutil-2.6.1/dateutil/tz/tz.py`) -> Impact: **108.4** | LOC: 46

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `__init__` (@ `python-dateutil-2.6.1/dateutil/rrule.py`) -> **O(2^N) [Recursive]**
- `_fromutc` (@ `python-dateutil-2.6.1/dateutil/tz/_common.py`) -> **O(2^N) [Recursive]**
- `__repr__` (@ `python-dateutil-2.6.1/dateutil/tz/tz.py`) -> **O(2^N) [Recursive]**
  * *Intent:* # the hour near to a change is DST or not. # # timestamp = time.mktime((dt.year, dt.month, dt.day, dt.hour, # dt.minute, dt.second, dt.weekday(), 0, -...
- `__init__` (@ `python-dateutil-2.6.1/dateutil/tz/tz.py`) -> **O(2^N) [Recursive]**
- `__repr__` (@ `python-dateutil-2.6.1/dateutil/tz/tz.py`) -> **O(2^N) [Recursive]**
- `__repr__` (@ `python-dateutil-2.6.1/dateutil/tz/win.py`) -> **O(2^N) [Recursive]**
- `__repr__` (@ `python-dateutil-2.6.1/dateutil/tz/tz.py`) -> **O(2^N) [Recursive]**
- `get` (@ `python-dateutil-2.6.1/dateutil/tz/tz.py`) -> **O(2^N) [Recursive]**
- `gettz` (@ `python-dateutil-2.6.1/dateutil/zoneinfo/__init__.py`) -> **O(2^N) [Recursive]**
- `gettz_db_metadata` (@ `python-dateutil-2.6.1/dateutil/zoneinfo/__init__.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `__init__` (@ `python-dateutil-2.6.1/dateutil/relativedelta.py`) -> DB Complexity: **69**
- `__str__` (@ `python-dateutil-2.6.1/dateutil/rrule.py`) -> DB Complexity: **67**
- `__init__` (@ `python-dateutil-2.6.1/dateutil/rrule.py`) -> DB Complexity: **55**
- `_parse_rfc` (@ `python-dateutil-2.6.1/dateutil/tz/tz.py`) -> DB Complexity: **36**
- `__repr__` (@ `python-dateutil-2.6.1/dateutil/tz/tz.py`) -> DB Complexity: **24**
  * *Intent:* # the hour near to a change is DST or not. # # timestamp = time.mktime((dt.year, dt.month, dt.day, dt.hour, # dt.minute, dt.second, dt.weekday(), 0, -...
- `__repr__` (@ `python-dateutil-2.6.1/dateutil/tz/tz.py`) -> DB Complexity: **14**
- `__init__` (@ `python-dateutil-2.6.1/dateutil/tz/tz.py`) -> DB Complexity: **14**
- `main` (@ `python-dateutil-2.6.1/updatezinfo.py`) -> DB Complexity: **13**
- `__eq__` (@ `python-dateutil-2.6.1/dateutil/tz/win.py`) -> DB Complexity: **12**
- `__repr__` (@ `python-dateutil-2.6.1/dateutil/tz/win.py`) -> DB Complexity: **10**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `python-dateutil-2.6.1/dateutil` | 8 | 9188.96 | 26.91% | 6.58% |
| `python-dateutil-2.6.1/dateutil/tz` | 4 | 3452.32 | 25.53% | 70.29% |
| `python-dateutil-2.6.1/dateutil/zoneinfo` | 1 | 211.68 | 35.46% | 90.29% |
| `python-dateutil-2.6.1` | 5 | 102.74 | 6.65% | 18.3% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `python-dateutil-2.6.1/dateutil/tz/tz.py` -> **98.2208%** Exposure
- `python-dateutil-2.6.1/dateutil/tz/_common.py` -> **97.121%** Exposure
- `python-dateutil-2.6.1/setup.py` -> **91.5138%** Exposure
- `python-dateutil-2.6.1/dateutil/zoneinfo/__init__.py` -> **90.2888%** Exposure
- `python-dateutil-2.6.1/dateutil/tz/win.py` -> **85.828%** Exposure
### Highest State Flux (Mutation/Volatility)
- `python-dateutil-2.6.1/dateutil/relativedelta.py` -> **99.9999%** Exposure
- `python-dateutil-2.6.1/dateutil/tz/win.py` -> **99.9996%** Exposure
- `python-dateutil-2.6.1/dateutil/rrule.py` -> **99.999%** Exposure
- `python-dateutil-2.6.1/dateutil/zoneinfo/__init__.py` -> **99.9933%** Exposure
- `python-dateutil-2.6.1/dateutil/tz/tz.py` -> **99.9771%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `python-dateutil-2.6.1/dateutil/tz/tz.py` -> **0** Orphaned Functions | **21** Duplicates
- `python-dateutil-2.6.1/dateutil/rrule.py` -> **0** Orphaned Functions | **3** Duplicates
- `python-dateutil-2.6.1/dateutil/tz/win.py` -> **0** Orphaned Functions | **3** Duplicates
- `python-dateutil-2.6.1/dateutil/parser.py` -> **0** Orphaned Functions | **2** Duplicates
- `python-dateutil-2.6.1/dateutil/tz/_common.py` -> **0** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`python-dateutil-2.6.1/dateutil/parser.py`** -> AI Confidence: **99.39%**
2. **`python-dateutil-2.6.1/dateutil/relativedelta.py`** -> AI Confidence: **99.39%**
3. **`python-dateutil-2.6.1/dateutil/rrule.py`** -> AI Confidence: **99.39%**
4. **`python-dateutil-2.6.1/dateutil/tz/tz.py`** -> AI Confidence: **99.31%**
5. **`python-dateutil-2.6.1/dateutil/zoneinfo/__init__.py`** -> AI Confidence: **99.24%**
6. **`python-dateutil-2.6.1/dateutil/tz/win.py`** -> AI Confidence: **99.15%**
7. **`python-dateutil-2.6.1/dateutil/easter.py`** -> AI Confidence: **99.06%**
8. **`python-dateutil-2.6.1/updatezinfo.py`** -> AI Confidence: **98.93%**
9. **`python-dateutil-2.6.1/dateutil/tz/_common.py`** -> AI Confidence: **98.89%**
10. **`python-dateutil-2.6.1/dateutil/_common.py`** -> AI Confidence: **98.85%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `python-dateutil-2.6.1/dateutil/parser.py` -> **100.0%** Exposure
- `python-dateutil-2.6.1/dateutil/relativedelta.py` -> **100.0%** Exposure
- `python-dateutil-2.6.1/dateutil/rrule.py` -> **100.0%** Exposure
- `python-dateutil-2.6.1/dateutil/tz/_common.py` -> **100.0%** Exposure
- `python-dateutil-2.6.1/dateutil/tz/tz.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `python-dateutil-2.6.1/dateutil/parser.py` -> **100.0%** Exposure
- `python-dateutil-2.6.1/dateutil/relativedelta.py` -> **100.0%** Exposure
- `python-dateutil-2.6.1/dateutil/rrule.py` -> **100.0%** Exposure
- `python-dateutil-2.6.1/dateutil/tz/_common.py` -> **100.0%** Exposure
- `python-dateutil-2.6.1/dateutil/tz/tz.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `70` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `python-dateutil-2.6.1/dateutil/tz/tz.py` (PYTHON) -> Cumulative Risk: **827.92**
- **Archetype:** `file_cluster_13` (Distance: 12.835 IQR)
- **Magnitude:** 2671.88 | **LOC:** 1512 | **CtrlFlow:** 52.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9771%)
- **Heaviest Functions:** `__repr__` (Impact: 1077.1), `_parse_rfc` (Impact: 521.0), `__repr__` (Impact: 181.3)

### 2. `python-dateutil-2.6.1/dateutil/tz/win.py` (PYTHON) -> Cumulative Risk: **783.22**
- **Archetype:** `file_cluster_13` (Distance: 12.522 IQR)
- **Magnitude:** 346.12 | **LOC:** 333 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9996%)
- **Heaviest Functions:** `__repr__` (Impact: 63.6), `__eq__` (Impact: 57.1), `valuestodict` (Impact: 35.9)

### 3. `python-dateutil-2.6.1/dateutil/zoneinfo/__init__.py` (PYTHON) -> Cumulative Risk: **781.86**
- **Archetype:** `file_cluster_13` (Distance: 14.756 IQR)
- **Magnitude:** 211.68 | **LOC:** 184 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.999%)
- **Heaviest Functions:** `__init__` (Impact: 68.2), `gettz` (Impact: 35.2), `gettz_db_metadata` (Impact: 35.2)

### 4. `python-dateutil-2.6.1/dateutil/rrule.py` (PYTHON) -> Cumulative Risk: **720.58**
- **Archetype:** `file_cluster_8` (Distance: 12.863 IQR)
- **Magnitude:** 5856.3 | **LOC:** 1611 | **CtrlFlow:** 74.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.999%)
- **Heaviest Functions:** `__init__` (Impact: 3216.5), `__str__` (Impact: 1644.0), `between` (Impact: 130.1)

### 5. `python-dateutil-2.6.1/dateutil/relativedelta.py` (PYTHON) -> Cumulative Risk: **677.13**
- **Archetype:** `file_cluster_8` (Distance: 12.596 IQR)
- **Magnitude:** 2700.1 | **LOC:** 550 | **CtrlFlow:** 72.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `__init__` (Impact: 2523.3), `_sign` (Impact: 1.8)

### 6. `python-dateutil-2.6.1/dateutil/tz/_common.py` (PYTHON) -> Cumulative Risk: **649.66**
- **Archetype:** `file_cluster_8` (Distance: 10.416 IQR)
- **Magnitude:** 421.24 | **LOC:** 395 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (98.889%)
- **Heaviest Functions:** `_fromutc` (Impact: 335.5), `enfold` (Impact: 14.5), `_fold_status` (Impact: 12.5)

### 7. `python-dateutil-2.6.1/dateutil/parser.py` (PYTHON) -> Cumulative Risk: **641.71**
- **Archetype:** `file_cluster_8` (Distance: 11.966 IQR)
- **Magnitude:** 518.7 | **LOC:** 1375 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (97.7992%)
- **Heaviest Functions:** `get_token` (Impact: 259.5), `__init__` (Impact: 31.1), `_repr` (Impact: 13.3)

### 8. `python-dateutil-2.6.1/updatezinfo.py` (PYTHON) -> Cumulative Risk: **534.29**
- **Archetype:** `file_cluster_13` (Distance: 9.452 IQR)
- **Magnitude:** 61.22 | **LOC:** 56 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.6399%), Verification (80.0%)
- **Heaviest Functions:** `main` (Impact: 56.4)

### 9. `python-dateutil-2.6.1/dateutil/_common.py` (PYTHON) -> Cumulative Risk: **461.75**
- **Archetype:** `file_cluster_8` (Distance: 10.524 IQR)
- **Magnitude:** 49.58 | **LOC:** 35 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (98.4026%), State Flux (74.1414%)
- **Heaviest Functions:** `__eq__` (Impact: 17.7), `__repr__` (Impact: 10.7), `__call__` (Impact: 10.6)

### 10. `python-dateutil-2.6.1/dateutil/easter.py` (PYTHON) -> Cumulative Risk: **276.37**
- **Archetype:** `file_cluster_8` (Distance: 7.759 IQR)
- **Magnitude:** 30.64 | **LOC:** 90 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.5572%), Stability (50.0%), Algorithmic Dos (14.3301%)
- **Heaviest Functions:** `easter` (Impact: 28.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `python-dateutil-2.6.1/dateutil/rrule.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.863 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.933 IQR)
- **Top Global Matches:** file_cluster_8: 12.863, file_cluster_13: 12.924, file_cluster_7: 13.013
- **Magnitude:** 5856.3 | **LOC:** 1611 | **CtrlFlow:** 74.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 67
- **Risk Profile:** Cognitive Load (50.2051%), Tech Debt (19.9973%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 3216.5 | O(2^N) | DB: 55)
  * `__str__` (Impact: 1644.0 | O(N^6) | DB: 67)
  * `between` (Impact: 130.1 | O(N^6) | DB: 4)
  * `__getitem__` (Impact: 79.9 | O(N^6) | DB: 3)
  * `xafter` (Impact: 71.7 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 441`, `structural_boundaries: 154`, `args: 52`, `func_start: 50`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 394`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `io: 1`, `api: 30`, `import: 15`
* *Defense:* `safety: 35`, `doc: 64`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` itertools, datetime, heapq, dateutil, fractions, calendar, six, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/relativedelta.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.596 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.491 IQR)
- **Top Global Matches:** file_cluster_8: 12.596, file_cluster_13: 12.73, file_cluster_0: 12.958
- **Magnitude:** 2700.1 | **LOC:** 550 | **CtrlFlow:** 72.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 69
- **Risk Profile:** Cognitive Load (75.686%), Tech Debt (9.5349%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 2523.3 | O(N^6) | DB: 69)
  * `_sign` (Impact: 1.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 57`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 161`, `planned_debt: 1`
* *Architecture:* `api: 6`, `import: 7`
* *Defense:* `safety: 21`, `doc: 5`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 55.564
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.134454
  * `Imports (Out-Degree: 0):` datetime, operator, calendar, six, math, ._common, warnings
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/dateutil/tz/tz.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.835 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.923 IQR)
- **Top Global Matches:** file_cluster_13: 12.835, file_cluster_8: 12.965, file_cluster_0: 12.998
- **Magnitude:** 2671.88 | **LOC:** 1512 | **CtrlFlow:** 52.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 36
- **Risk Profile:** Cognitive Load (45.3586%), Tech Debt (98.2208%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 1077.1 | O(2^N) | DB: 24)
    * *Intent:* # the hour near to a change is DST or not. # # timestamp = time.mktime((dt.year, dt.month, dt.day, d...
  * `_parse_rfc` (Impact: 521.0 | O(N^6) | DB: 36)
  * `__repr__` (Impact: 181.3 | O(2^N) | DB: 14)
  * `__init__` (Impact: 108.4 | O(N^4) | DB: 14)
  * `__init__` (Impact: 99.5 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 263`, `structural_boundaries: 242`, `args: 79`, `func_start: 79`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 217`, `dead_code: 2`, `duplicate_logic: 21`
* *Architecture:* `io: 14`, `api: 39`, `import: 16`
* *Defense:* `safety: 41`, `doc: 82`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 78.626
  * `Choke Point (Betweenness):` 0.033088 | `Ripple Effect (Closeness):` 0.176471
  * `Imports (Out-Degree: 2):` datetime, dateutil.relativedelta, .win, bisect, dateutil, os, struct, six...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/dateutil/parser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.966 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.187 IQR)
- **Top Global Matches:** file_cluster_8: 11.966, file_cluster_13: 12.161, file_cluster_7: 12.251
- **Magnitude:** 518.7 | **LOC:** 1375 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (43.2712%), Tech Debt (23.0817%)
**Top Internal Functions/Classes:**
  * `get_token` (Impact: 259.5 | O(N^6) | DB: 8)
  * `__init__` (Impact: 31.1 | O(N^6) | DB: 4)
  * `_repr` (Impact: 13.3 | O(N^4) | DB: 1)
  * `__len__` (Impact: 10.5 | O(N^5))
  * `__next__` (Impact: 7.2 | O(N^3))
    * *Intent:* # If we've seen some letters and a dot separator, continue # parsing, and the tokens will be broken ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 365`, `structural_boundaries: 151`, `args: 41`, `func_start: 41`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 123`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 29`, `import: 11`
* *Defense:* `safety: 43`, `doc: 50`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 22.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` , datetime, string, io, __future__, re, calendar, collections...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/tz/_common.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.416 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.835 IQR)
- **Top Global Matches:** file_cluster_8: 10.416, file_cluster_7: 10.582, file_cluster_0: 10.604
- **Magnitude:** 421.24 | **LOC:** 395 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (15.6218%), Tech Debt (97.121%)
**Top Internal Functions/Classes:**
  * `_fromutc` (Impact: 335.5 | O(2^N))
  * `enfold` (Impact: 14.5 | O(N^3))
  * `_fold_status` (Impact: 12.5 | O(N^3))
  * `_validate_fromutc_inputs` (Impact: 11.0 | O(N^3))
    * *Intent:* """ __slots__ = () @property def fold(self): return 1 def enfold(dt, fold=1): """
  * `tzname_in_python2` (Impact: 10.9 | O(N^3))
    * *Intent:* """Change unicode output into bytestrings in Python 2 tzname() API changed in Python 3. It used to r...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 70`, `args: 24`, `func_start: 24`, `class_start: 3`
* *Risk/State:* `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 15`, `import: 3`
* *Defense:* `safety: 6`, `doc: 38`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` six, datetime, functools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/tz/win.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.522 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.449 IQR)
- **Top Global Matches:** file_cluster_13: 12.522, file_cluster_0: 12.808, file_cluster_8: 12.842
- **Magnitude:** 346.12 | **LOC:** 333 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (36.1259%), Tech Debt (85.828%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 63.6 | O(2^N) | DB: 10)
  * `__eq__` (Impact: 57.1 | O(N^4) | DB: 12)
  * `valuestodict` (Impact: 35.9 | O(N^4))
  * `list` (Impact: 24.6 | O(N^6))
  * `__init__` (Impact: 14.8 | O(N^4) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 62`, `args: 20`, `func_start: 20`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 69`, `dead_code: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 16`, `import: 7`
* *Defense:* `safety: 9`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 268.077
  * `Choke Point (Betweenness):` 0.014706 | `Ripple Effect (Closeness):` 0.183824
  * `Imports (Out-Degree: 1):` datetime, ctypes, dateutil.tzwin, struct, six, ._common, six.moves
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/dateutil/zoneinfo/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.756 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.565 IQR)
- **Top Global Matches:** file_cluster_13: 14.756, file_cluster_11: 14.904, file_cluster_6: 14.93
- **Magnitude:** 211.68 | **LOC:** 184 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (35.464%), Tech Debt (90.2888%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 68.2 | O(N^6) | DB: 6)
  * `gettz` (Impact: 35.2 | O(2^N) | DB: 1)
  * `gettz_db_metadata` (Impact: 35.2 | O(2^N) | DB: 1)
  * `get_zonefile_instance` (Impact: 21.5 | O(2^N))
    * *Intent:* # The current API has gettz as a module function, although in fact it taps into # a stateful class. ...
  * `get` (Impact: 6.2 | O(2^N))
    * *Intent:* """ Wrapper for :func:`ZoneInfoFile.zones.get`. This is a convenience method for retrieving zones fr...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 32`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `state_mutation: 22`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 11`, `import: 7`
* *Defense:* `safety: 6`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 22.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` tarfile, contextlib, json, io, dateutil.tz, warnings, pkgutil
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/updatezinfo.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.452 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.842 IQR)
- **Top Global Matches:** file_cluster_13: 9.452, file_cluster_8: 9.731, file_cluster_17: 10.402
- **Magnitude:** 61.22 | **LOC:** 56 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (20.727%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 56.4 | O(N^6) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 19`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 4`, `api: 1`, `import: 7`
* *Defense:* `safety: 3`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` hashlib, json, six.moves.urllib, io, os, dateutil.zoneinfo
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/_common.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.524 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.129 IQR)
- **Top Global Matches:** file_cluster_8: 10.524, file_cluster_7: 10.901, file_cluster_13: 11.168
- **Magnitude:** 49.58 | **LOC:** 35 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (25.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__eq__` (Impact: 17.7 | O(N^4))
  * `__repr__` (Impact: 10.7 | O(N^3))
  * `__call__` (Impact: 10.6 | O(N^3))
  * `__init__` (Impact: 3.1 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 12`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 5`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/easter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.759 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.283 IQR)
- **Top Global Matches:** file_cluster_8: 7.759, file_cluster_7: 8.219, file_cluster_1: 8.475
- **Magnitude:** 30.64 | **LOC:** 90 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.1573%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `easter` (Impact: 28.1 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 3`, `args: 1`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` datetime
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/setup.py` (PYTHON | Tier 1 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.134 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.601 IQR)
- **Top Global Matches:** file_cluster_8: 6.134, file_cluster_13: 6.668, file_cluster_7: 7.01
- **Magnitude:** 15.82 | **LOC:** 48 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.5627%), Tech Debt (91.5138%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 9`
* *Risk/State:* `fragile_debt: 1`
* *Architecture:* `io: 2`, `import: 6`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 22.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` codecs, dateutil._version, re, os, os.path, setuptools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/zonefile_metadata.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.5 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.975%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/tz/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.102 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.365 IQR)
- **Top Global Matches:** file_cluster_8: 6.102, file_cluster_13: 6.249, file_cluster_7: 7.187
- **Magnitude:** 13.08 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 22.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .tz
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/_version.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.242 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.601 IQR)
- **Top Global Matches:** file_cluster_8: 7.242, file_cluster_7: 7.789, file_cluster_1: 7.88
- **Magnitude:** 12.6 | **LOC:** 11 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 59.8
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.117647
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/dateutil/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 6.432 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.582 IQR)
- **Top Global Matches:** file_cluster_13: 6.432, file_cluster_8: 6.762, file_cluster_7: 7.915
- **Magnitude:** 10.52 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* None
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 22.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ._version
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/dateutil/tzwin.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 6.737 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.717 IQR)
- **Top Global Matches:** file_cluster_13: 6.737, file_cluster_8: 7.285, file_cluster_7: 8.376
- **Magnitude:** 10.52 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 250.007
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.122549
  * `Imports (Out-Degree: 1):` .tz.win
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `python-dateutil-2.6.1/NEWS` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 9.2 | **LOC:** 460 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `python-dateutil-2.6.1/MANIFEST.in` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.148
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `python-dateutil-2.6.1/dateutil/tz/tz.py` (PYTHON) | Magnitude: 2671.88 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 781, branch: 263, encapsulation: 262, structural_boundaries: 242
- `python-dateutil-2.6.1/dateutil/zoneinfo/__init__.py` (PYTHON) | Magnitude: 211.68 | Delta: **0.148 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 32, state_mutation: 22, branch: 21
- `python-dateutil-2.6.1/updatezinfo.py` (PYTHON) | Magnitude: 61.22 | Delta: **0.279 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 19, branch: 9, import: 7
- `python-dateutil-2.6.1/dateutil/tz/win.py` (PYTHON) | Magnitude: 346.12 | Delta: **0.286 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 166, encapsulation: 103, state_mutation: 69, structural_boundaries: 62
- `python-dateutil-2.6.1/dateutil/__init__.py` (PYTHON) | Magnitude: 10.52 | Delta: **0.33 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, encapsulation: 2, import: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `python-dateutil-2.6.1/dateutil/rrule.py` (PYTHON) | Magnitude: 5856.3 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1100, branch: 441, state_mutation: 394, encapsulation: 345
- `python-dateutil-2.6.1/dateutil/relativedelta.py` (PYTHON) | Magnitude: 2700.1 | Delta: **0.134 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 389, state_mutation: 161, branch: 149, structural_boundaries: 57
- `python-dateutil-2.6.1/dateutil/tz/__init__.py` (PYTHON) | Magnitude: 13.08 | Delta: **0.147 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, indent_spaces: 2, safety_bypasses: 1, api: 1
- `python-dateutil-2.6.1/dateutil/tz/_common.py` (PYTHON) | Magnitude: 421.24 | Delta: **0.166 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 149, structural_boundaries: 70, encapsulation: 50, branch: 38
- `python-dateutil-2.6.1/dateutil/parser.py` (PYTHON) | Magnitude: 518.7 | Delta: **0.195 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 787, branch: 365, structural_boundaries: 151, state_mutation: 123

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `python-dateutil-2.6.1/dateutil/tz/tz.py` -> **Severity: 3.308** (Bridge: 0.0331 * Flux: 99.9771%)
- `python-dateutil-2.6.1/dateutil/tz/win.py` -> **Severity: 1.471** (Bridge: 0.0147 * Flux: 99.9996%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `python-dateutil-2.6.1/dateutil/tzwin.py` -> **Severity: 9.804** (Embedded: 0.1225 * Error Risk: 80.0%)
- `python-dateutil-2.6.1/dateutil/tz/tz.py` -> **Severity: 9.196** (Embedded: 0.1765 * Error Risk: 52.113%)
- `python-dateutil-2.6.1/dateutil/tz/win.py` -> **Severity: 4.383** (Embedded: 0.1838 * Error Risk: 23.8438%)
- `python-dateutil-2.6.1/dateutil/relativedelta.py` -> **Severity: 3.272** (Embedded: 0.1345 * Error Risk: 24.3371%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `python-dateutil-2.6.1/dateutil/tz/win.py` -> **Severity: 26805.421** (Blast Radius: 268.077 * Doc Risk: 99.9915%)
- `python-dateutil-2.6.1/dateutil/tz/tz.py` -> **Severity: 7518.989** (Blast Radius: 78.626 * Doc Risk: 95.6298%)
- `python-dateutil-2.6.1/dateutil/_common.py` -> **Severity: 2214.8** (Blast Radius: 22.148 * Doc Risk: 100.0%)
- `python-dateutil-2.6.1/dateutil/zoneinfo/__init__.py` -> **Severity: 2214.778** (Blast Radius: 22.148 * Doc Risk: 99.999%)
- `python-dateutil-2.6.1/dateutil/easter.py` -> **Severity: 2204.993** (Blast Radius: 22.148 * Doc Risk: 99.5572%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
