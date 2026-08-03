# ARCHITECTURAL_BRIEF: sniffio
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/sniffio` |
| **Timestamp** | `2026-08-03T21:25:20.700766+00:00` |
| **Scan Duration** | `0.12s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 6 malicious artifacts.

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
| Total Artifacts | 27 |
| Analyzed Artifacts (Scanned) | 10 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 17 |
| Total LOC | 148 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 37.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3333 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 5 | 109 | 50.0% |
| MARKDOWN | 2 | 0 | 20.0% |
| PLAINTEXT | 2 | 0 | 20.0% |
| SHELL | 1 | 39 | 10.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.517`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 4 | 40.0% |
| file_cluster_13 | 1 | 10.0% |
| file_cluster_4 | 1 | 10.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 40.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 17*

**Composition by Extension & Reason:**
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rst`: 3x Excluded (Unsupported Extension: '.rst')
- `.ini`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yapf`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.apache2`: 1x Excluded (Unsupported Extension: '.APACHE2')
- `.mit`: 1x Excluded (Unsupported Extension: '.MIT')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 98.5 | 38.5 | 22.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 57.0 | 12.5 | 0.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 99.5 | 32.6 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 2.7 | 1.6 | 2.2 | 0.2 |
| API Exposure | 0.0 | 8.7 | 2.2 | 0.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 33.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 98.3 | 30.8 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 66.7 | 93.3 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 6.7 | 93.9 | 38.3 | 20.8 | 6.7 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 27.0 | 4.6 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `sniffio-1.3.1/ci.sh` (Hits: 8)
- `sniffio-1.3.1/sniffio/_impl.py` (Hits: 2)
- `sniffio-1.3.1/sniffio/_tests/test_sniffio.py` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **_impl.py** (`sniffio-1.3.1/sniffio/_impl.py`) — 1 inbound connections
2. **_version.py** (`sniffio-1.3.1/sniffio/_version.py`) — 1 inbound connections
3. **CODE_OF_CONDUCT.md** (`sniffio-1.3.1/CODE_OF_CONDUCT.md`) — 0 inbound connections
4. **CONTRIBUTING.md** (`sniffio-1.3.1/CONTRIBUTING.md`) — 0 inbound connections
5. **MANIFEST.in** (`sniffio-1.3.1/MANIFEST.in`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **_impl.py** (`sniffio-1.3.1/sniffio/_impl.py`) — 8 outbound dependencies
2. **test_sniffio.py** (`sniffio-1.3.1/sniffio/_tests/test_sniffio.py`) — 6 outbound dependencies
3. **__init__.py** (`sniffio-1.3.1/sniffio/__init__.py`) — 2 outbound dependencies
4. **CODE_OF_CONDUCT.md** (`sniffio-1.3.1/CODE_OF_CONDUCT.md`) — 0 outbound dependencies
5. **CONTRIBUTING.md** (`sniffio-1.3.1/CONTRIBUTING.md`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `current_async_library` (@ `sniffio-1.3.1/sniffio/_impl.py`) -> Impact: **45.0** | LOC: 33
  * *Intent:* """Detect which async library is currently running. The following libraries are currently supported: ================ =========== ====================...
- `test_basics_cvar` (@ `sniffio-1.3.1/sniffio/_tests/test_sniffio.py`) -> Impact: **13.6** | LOC: 12
- `test_basics_tlocal` (@ `sniffio-1.3.1/sniffio/_tests/test_sniffio.py`) -> Impact: **13.6** | LOC: 12
- `Anonymous_Block` (@ `sniffio-1.3.1/ci.sh`) -> Impact: **12.2** | LOC: 34
- `test_asyncio` (@ `sniffio-1.3.1/sniffio/_tests/test_sniffio.py`) -> Impact: **8.7** | LOC: 19
- `test_curio` (@ `sniffio-1.3.1/sniffio/_tests/test_sniffio.py`) -> Impact: **8.7** | LOC: 19
- `__global_context__` (@ `sniffio-1.3.1/ci.sh`) -> Impact: **2.1** | LOC: 22

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `current_async_library` (@ `sniffio-1.3.1/sniffio/_impl.py`) -> **O(N^4)**
  * *Intent:* """Detect which async library is currently running. The following libraries are currently supported: ================ =========== ====================...

### Highest Data Gravity (Database Complexity)
- `Anonymous_Block` (@ `sniffio-1.3.1/ci.sh`) -> DB Complexity: **18**
- `current_async_library` (@ `sniffio-1.3.1/sniffio/_impl.py`) -> DB Complexity: **6**
  * *Intent:* """Detect which async library is currently running. The following libraries are currently supported: ================ =========== ====================...
- `test_asyncio` (@ `sniffio-1.3.1/sniffio/_tests/test_sniffio.py`) -> DB Complexity: **1**
- `test_curio` (@ `sniffio-1.3.1/sniffio/_tests/test_sniffio.py`) -> DB Complexity: **1**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `sniffio-1.3.1/sniffio/_tests` | 2 | 94.28 | 51.74% | 49.74% |
| `sniffio-1.3.1/sniffio` | 3 | 84.52 | 16.88% | 0.0% |
| `sniffio-1.3.1` | 4 | 25.08 | 19.24% | 24.08% |
| `sniffio-1.3.1/ci` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `sniffio-1.3.1/sniffio/_tests/test_sniffio.py` -> **99.4824%** Exposure
- `sniffio-1.3.1/ci.sh` -> **96.3358%** Exposure
### Highest State Flux (Mutation/Volatility)
- `sniffio-1.3.1/ci.sh` -> **98.2941%** Exposure
- `sniffio-1.3.1/sniffio/_tests/test_sniffio.py` -> **86.5056%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `sniffio-1.3.1/sniffio/_tests/test_sniffio.py` -> **4** Orphaned Functions | **0** Duplicates
- `sniffio-1.3.1/ci.sh` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`sniffio-1.3.1/sniffio/_impl.py`** -> AI Confidence: **99.15%**
2. **`sniffio-1.3.1/ci.sh`** -> AI Confidence: **99.06%**
3. **`sniffio-1.3.1/sniffio/_tests/test_sniffio.py`** -> AI Confidence: **98.93%**
4. **`sniffio-1.3.1/sniffio/__init__.py`** -> AI Confidence: **98.84%**
5. **`sniffio-1.3.1/sniffio/_tests/__init__.py`** -> AI Confidence: **98.84%**
6. **`sniffio-1.3.1/sniffio/_version.py`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `sniffio-1.3.1/sniffio/_impl.py` -> **0.0051%** Exposure
### Algorithmic DoS Exposure
- `sniffio-1.3.1/sniffio/_impl.py` -> **100.0%** Exposure
- `sniffio-1.3.1/sniffio/_tests/test_sniffio.py` -> **52.8814%** Exposure
- `sniffio-1.3.1/ci.sh` -> **9.298%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `13` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `sniffio-1.3.1/sniffio/_tests/test_sniffio.py` (PYTHON) -> Cumulative Risk: **693.2**
- **Archetype:** `file_cluster_4` (Distance: 12.176 IQR)
- **Magnitude:** 83.76 | **LOC:** 85 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.4824%), Cognitive Load (98.4819%)
- **Heaviest Functions:** `test_basics_cvar` (Impact: 13.6), `test_basics_tlocal` (Impact: 13.6), `test_asyncio` (Impact: 8.7)

### 2. `sniffio-1.3.1/sniffio/_impl.py` (PYTHON) -> Cumulative Risk: **483.64**
- **Archetype:** `file_cluster_13` (Distance: 9.831 IQR)
- **Magnitude:** 57.74 | **LOC:** 96 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Safety Score (57.027%)
- **Heaviest Functions:** `current_async_library` (Impact: 45.0)

### 3. `sniffio-1.3.1/ci.sh` (SHELL) -> Cumulative Risk: **462.65**
- **Archetype:** `file_cluster_8` (Distance: 9.516 IQR)
- **Magnitude:** 22.08 | **LOC:** 57 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.2941%), Tech Debt (96.3358%), Cognitive Load (76.9436%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 12.2), `__global_context__` (Impact: 2.1)

### 4. `sniffio-1.3.1/sniffio/__init__.py` (PYTHON) -> Cumulative Risk: **225.44**
- **Archetype:** `file_cluster_8` (Distance: 6.881 IQR)
- **Magnitude:** 16.26 | **LOC:** 18 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (86.6667%), Documentation (80.8419%), Stability (50.0%), Cognitive Load (5.0%)

### 5. `sniffio-1.3.1/sniffio/_tests/__init__.py` (PYTHON) -> Cumulative Risk: **68.49**
- **Archetype:** `file_cluster_8` (Distance: 4.447 IQR)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (6.6667%), Documentation (6.6667%), Cognitive Load (5.0%)

### 6. `sniffio-1.3.1/sniffio/_version.py` (PYTHON) -> Cumulative Risk: **68.49**
- **Archetype:** `file_cluster_8` (Distance: 3.628 IQR)
- **Magnitude:** 10.52 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (6.6667%), Documentation (6.6667%), Cognitive Load (5.0%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `sniffio-1.3.1/sniffio/_tests/test_sniffio.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.176 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.918 IQR)
- **Top Global Matches:** file_cluster_4: 12.176, file_cluster_13: 12.577, file_cluster_0: 12.85
- **Magnitude:** 83.76 | **LOC:** 85 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (98.4819%), Tech Debt (99.4824%)
**Top Internal Functions/Classes:**
  * `test_basics_cvar` (Impact: 13.6 | O(N^2))
  * `test_basics_tlocal` (Impact: 13.6 | O(N^2))
  * `test_asyncio` (Impact: 8.7 | O(N^2) | DB: 1)
  * `test_curio` (Impact: 8.7 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 21`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`, `orphaned_logic: 4`
* *Architecture:* `io: 1`, `api: 6`, `concurrency: 26`, `import: 6`
* *Defense:* `safety: 12`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 92.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` curio, .., os, sys, pytest, asyncio
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sniffio-1.3.1/sniffio/_impl.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.831 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.809 IQR)
- **Top Global Matches:** file_cluster_13: 9.831, file_cluster_4: 10.06, file_cluster_8: 10.065
- **Magnitude:** 57.74 | **LOC:** 96 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (40.6366%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `current_async_library` (Impact: 45.0 | O(N^4) | DB: 6)
    * *Intent:* """Detect which async library is currently running. The following libraries are currently supported:...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 18`, `args: 1`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `io: 2`, `api: 3`, `concurrency: 9`, `import: 6`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 131.337
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 0):` sniffio, trio, curio.meta, typing, sys, contextvars, threading, asyncio
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `sniffio-1.3.1/ci.sh` (SHELL | Tier 0 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.516 IQR)
- **Top Global Matches:** file_cluster_8: 9.516, file_cluster_4: 10.2, file_cluster_12: 10.204
- **Magnitude:** 22.08 | **LOC:** 57 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (76.9436%), Tech Debt (96.3358%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 12.2 | O(N^2) | DB: 18)
  * `__global_context__` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 6`
* *Risk/State:* `state_mutation: 6`, `orphaned_logic: 1`
* *Architecture:* `io: 8`, `concurrency: 1`
* *Defense:* `safety: 1`, `test: 1`, `sync_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 92.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sniffio-1.3.1/sniffio/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.881 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.019 IQR)
- **Top Global Matches:** file_cluster_8: 6.881, file_cluster_13: 7.297, file_cluster_7: 7.424
- **Magnitude:** 16.26 | **LOC:** 18 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 92.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ._impl, ._version
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sniffio-1.3.1/sniffio/_tests/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 92.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sniffio-1.3.1/sniffio/_version.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 3.628 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.821 IQR)
- **Top Global Matches:** file_cluster_8: 3.628, file_cluster_7: 5.597, file_cluster_1: 5.652
- **Magnitude:** 10.52 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 131.337
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.111111
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `sniffio-1.3.1/CODE_OF_CONDUCT.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 92.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sniffio-1.3.1/CONTRIBUTING.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 92.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sniffio-1.3.1/MANIFEST.in` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 92.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sniffio-1.3.1/ci/rtd-requirements.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 92.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `sniffio-1.3.1/sniffio/_version.py` (PYTHON) | **Drift Ratio: 1.6x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.628 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.821 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `sniffio-1.3.1/sniffio/_impl.py` (PYTHON) | Magnitude: 57.74 | Delta: **0.229 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 18, branch: 9, concurrency: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `sniffio-1.3.1/sniffio/_tests/test_sniffio.py` (PYTHON) | Magnitude: 83.76 | Delta: **0.401 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, concurrency: 26, test: 22, structural_boundaries: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `sniffio-1.3.1/sniffio/__init__.py` (PYTHON) | Magnitude: 16.26 | Delta: **0.416 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 4, encapsulation: 4, doc: 2
- `sniffio-1.3.1/ci.sh` (SHELL) | Magnitude: 22.08 | Delta: **0.684 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 13, io: 8, branch: 6, structural_boundaries: 6

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `sniffio-1.3.1/sniffio/_impl.py` -> **Severity: 6.336** (Embedded: 0.1111 * Error Risk: 57.027%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `sniffio-1.3.1/sniffio/_tests/test_sniffio.py` -> **Severity: 8652.756** (Blast Radius: 92.166 * Doc Risk: 93.8823%)
- `sniffio-1.3.1/sniffio/__init__.py` -> **Severity: 7450.875** (Blast Radius: 92.166 * Doc Risk: 80.8419%)
- `sniffio-1.3.1/sniffio/_impl.py` -> **Severity: 3893.315** (Blast Radius: 131.337 * Doc Risk: 29.6437%)
- `sniffio-1.3.1/ci.sh` -> **Severity: 1098.646** (Blast Radius: 92.166 * Doc Risk: 11.9203%)
- `sniffio-1.3.1/sniffio/_version.py` -> **Severity: 875.584** (Blast Radius: 131.337 * Doc Risk: 6.6667%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
