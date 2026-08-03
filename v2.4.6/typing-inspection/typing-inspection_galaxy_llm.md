# ARCHITECTURAL_BRIEF: typing-inspection
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/typing-inspection` |
| **Timestamp** | `2026-08-03T21:26:00.796753+00:00` |
| **Scan Duration** | `0.16s` |
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
| Total Artifacts | 23 |
| Analyzed Artifacts (Scanned) | 13 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 10 |
| Total LOC | 924 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 56.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.5 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 10 | 894 | 76.9% |
| MARKDOWN | 2 | 0 | 15.4% |
| MAKEFILE | 1 | 30 | 7.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.164`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 5 | 38.5% |
| file_cluster_13 | 4 | 30.8% |
| file_cluster_16 | 1 | 7.7% |
| file_cluster_0 | 1 | 7.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 15.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 10*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 2.4 | 19.5 | 6.9 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 95.8 | 30.5 | 1.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 86.7 | 14.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 15.0 | 0.0 | 0.0 |
| API Exposure | 0.0 | 13.8 | 5.1 | 4.2 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 47.2 | 5.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 7.9 | 0.7 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 59.0 | 86.7 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 99.9 | 12.9 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 45.2 | 8.7 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 26.9 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 9.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `typing_inspection-0.4.2/tests/typing_objects/test_member_checks.py` (Hits: 6)
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` (Hits: 4)
- `typing_inspection-0.4.2/src/typing_inspection/introspection.py` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **introspection.py** (`typing_inspection-0.4.2/src/typing_inspection/introspection.py`) — 3 inbound connections
2. **HISTORY.md** (`typing_inspection-0.4.2/HISTORY.md`) — 0 inbound connections
3. **README.md** (`typing_inspection-0.4.2/README.md`) — 0 inbound connections
4. **Makefile** (`typing_inspection-0.4.2/Makefile`) — 0 inbound connections
5. **__init__.py** (`typing_inspection-0.4.2/src/typing_inspection/__init__.py`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **introspection.py** (`typing_inspection-0.4.2/src/typing_inspection/introspection.py`) — 10 outbound dependencies
2. **typing_objects.py** (`typing_inspection-0.4.2/src/typing_inspection/typing_objects.py`) — 9 outbound dependencies
3. **test_member_checks.py** (`typing_inspection-0.4.2/tests/typing_objects/test_member_checks.py`) — 9 outbound dependencies
4. **test_inspect_annotation.py** (`typing_inspection-0.4.2/tests/introspection/test_inspect_annotation.py`) — 7 outbound dependencies
5. **test_literal_values.py** (`typing_inspection-0.4.2/tests/introspection/test_literal_values.py`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_compile_identity_check_function` (@ `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py`) -> Impact: **39.1** | LOC: 19
- `_compile_isinstance_check_function` (@ `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py`) -> Impact: **35.6** | LOC: 19
- `allowed_qualifiers` (@ `typing_inspection-0.4.2/src/typing_inspection/introspection.py`) -> Impact: **28.6** | LOC: 18
- `test_annotation_source_invalid_qualifier` (@ `typing_inspection-0.4.2/tests/introspection/test_inspect_annotation.py`) -> Impact: **10.6** | LOC: 4
- `test_literal_values_type_check` (@ `typing_inspection-0.4.2/tests/introspection/test_literal_values.py`) -> Impact: **8.3** | LOC: 11
- `_literal_type_check` (@ `typing_inspection-0.4.2/src/typing_inspection/introspection.py`) -> Impact: **8.2** | LOC: 8
- `test_bare_qualifier` (@ `typing_inspection-0.4.2/tests/introspection/test_inspect_annotation.py`) -> Impact: **5.7** | LOC: 11
- `is_union_origin` (@ `typing_inspection-0.4.2/src/typing_inspection/introspection.py`) -> Impact: **5.4** | LOC: 4
- `is_namedtuple` (@ `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py`) -> Impact: **5.4** | LOC: 4
- `is_typealiastype` (@ `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py`) -> Impact: **5.3** | LOC: 2

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `allowed_qualifiers` (@ `typing_inspection-0.4.2/src/typing_inspection/introspection.py`) -> **O(N^3)**
- `_compile_identity_check_function` (@ `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py`) -> **O(N^3)**
- `_compile_isinstance_check_function` (@ `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py`) -> **O(N^3)**
- `test_annotation_source_invalid_qualifier` (@ `typing_inspection-0.4.2/tests/introspection/test_inspect_annotation.py`) -> **O(N^3)**

### Highest Data Gravity (Database Complexity)
- `__init__` (@ `typing_inspection-0.4.2/src/typing_inspection/introspection.py`) -> DB Complexity: **1**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `typing_inspection-0.4.2/src/typing_inspection` | 4 | 445.01 | 8.68% | 40.95% |
| `typing_inspection-0.4.2/tests/introspection` | 4 | 93.42 | 5.76% | 0.0% |
| `typing_inspection-0.4.2/tests/typing_objects` | 2 | 68.52 | 6.94% | 0.0% |
| `typing_inspection-0.4.2` | 3 | 44.6 | 1.4% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `typing_inspection-0.4.2/src/typing_inspection/introspection.py` -> **86.7036%** Exposure
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` -> **52.6634%** Exposure
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.pyi` -> **24.4136%** Exposure
### Highest State Flux (Mutation/Volatility)
- `typing_inspection-0.4.2/src/typing_inspection/introspection.py` -> **47.1697%** Exposure
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` -> **11.0031%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `typing_inspection-0.4.2/tests/typing_objects/test_member_checks.py` -> **12** Orphaned Functions | **0** Duplicates
- `typing_inspection-0.4.2/tests/introspection/test_inspect_annotation.py` -> **9** Orphaned Functions | **0** Duplicates
- `typing_inspection-0.4.2/tests/introspection/test_literal_values.py` -> **6** Orphaned Functions | **0** Duplicates
- `typing_inspection-0.4.2/src/typing_inspection/introspection.py` -> **0** Orphaned Functions | **2** Duplicates
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` -> **0** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`typing_inspection-0.4.2/src/typing_inspection/introspection.py`** -> AI Confidence: **99.31%**
2. **`typing_inspection-0.4.2/src/typing_inspection/typing_objects.py`** -> AI Confidence: **99.31%**
3. **`typing_inspection-0.4.2/tests/introspection/test_inspect_annotation.py`** -> AI Confidence: **99.07%**
4. **`typing_inspection-0.4.2/tests/introspection/test_literal_values.py`** -> AI Confidence: **99.07%**
5. **`typing_inspection-0.4.2/Makefile`** -> AI Confidence: **99.06%**
6. **`typing_inspection-0.4.2/tests/typing_objects/test_member_checks.py`** -> AI Confidence: **99.06%**
7. **`typing_inspection-0.4.2/src/typing_inspection/__init__.py`** -> AI Confidence: **98.84%**
8. **`typing_inspection-0.4.2/src/typing_inspection/typing_objects.pyi`** -> AI Confidence: **98.84%**
9. **`typing_inspection-0.4.2/tests/introspection/__init__.py`** -> AI Confidence: **98.84%**
10. **`typing_inspection-0.4.2/tests/introspection/test_is_union_origin.py`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `typing_inspection-0.4.2/src/typing_inspection/introspection.py` -> **100.0%** Exposure
- `typing_inspection-0.4.2/tests/introspection/test_inspect_annotation.py` -> **99.7161%** Exposure
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` -> **96.5881%** Exposure
### Weaponizable Injection Vectors
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `typing_inspection-0.4.2/src/typing_inspection/introspection.py` -> **45.2071%** Exposure
- `typing_inspection-0.4.2/tests/introspection/test_inspect_annotation.py` -> **33.1812%** Exposure
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` -> **11.007%** Exposure
- `typing_inspection-0.4.2/tests/introspection/test_literal_values.py` -> **6.2447%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `51` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `typing_inspection-0.4.2/src/typing_inspection/introspection.py` (PYTHON) -> Cumulative Risk: **616.79**
- **Archetype:** `file_cluster_13` (Distance: 10.891 IQR)
- **Magnitude:** 88.1 | **LOC:** 588 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Logic Bomb (100.0%), Tech Debt (86.7036%), Spec Match (86.6667%), Safety Score (80.0%)
- **Heaviest Functions:** `allowed_qualifiers` (Impact: 28.6), `_literal_type_check` (Impact: 8.2), `is_union_origin` (Impact: 5.4)

### 2. `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` (PYTHON) -> Cumulative Risk: **495.97**
- **Archetype:** `file_cluster_13` (Distance: 10.891 IQR)
- **Magnitude:** 106.72 | **LOC:** 608 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Injection Surface (100.0%), Logic Bomb (96.5881%), Verification (80.0%), Safety Score (75.0237%)
- **Heaviest Functions:** `_compile_identity_check_function` (Impact: 39.1), `_compile_isinstance_check_function` (Impact: 35.6), `is_namedtuple` (Impact: 5.4)

### 3. `typing_inspection-0.4.2/tests/introspection/test_inspect_annotation.py` (PYTHON) -> Cumulative Risk: **291.55**
- **Archetype:** `file_cluster_8` (Distance: 10.324 IQR)
- **Magnitude:** 48.2 | **LOC:** 207 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (99.7161%), Stability (50.0%), Algorithmic Dos (33.1812%)
- **Heaviest Functions:** `test_annotation_source_invalid_qualifier` (Impact: 10.6), `test_bare_qualifier` (Impact: 5.7), `test_annotation_source_valid_qualifiers` (Impact: 5.3)

### 4. `typing_inspection-0.4.2/Makefile` (MAKEFILE) -> Cumulative Risk: **270.2**
- **Archetype:** `file_cluster_8` (Distance: 7.371 IQR)
- **Magnitude:** 42.6 | **LOC:** 40 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9026%), Stability (50.0%), Api Exposure (13.8139%)

### 5. `typing_inspection-0.4.2/tests/introspection/test_is_union_origin.py` (PYTHON) -> Cumulative Risk: **246.64**
- **Archetype:** `file_cluster_13` (Distance: 10.37 IQR)
- **Magnitude:** 6.48 | **LOC:** 26 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (80.0%), Stability (50.0%), Cognitive Load (12.4378%)
- **Heaviest Functions:** `test_is_union_origin` (Impact: 2.1)

### 6. `typing_inspection-0.4.2/src/typing_inspection/typing_objects.pyi` (PYTHON) -> Cumulative Risk: **240.47**
- **Archetype:** `file_cluster_16` (Distance: 11.339 IQR)
- **Magnitude:** 239.67 | **LOC:** 418 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Safety Score (95.7501%), Stability (50.0%), Spec Match (41.9355%), Tech Debt (24.4136%)

### 7. `typing_inspection-0.4.2/tests/typing_objects/test_member_checks.py` (PYTHON) -> Cumulative Risk: **171.76**
- **Archetype:** `file_cluster_0` (Distance: 11.653 IQR)
- **Magnitude:** 58.0 | **LOC:** 210 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Api Exposure (10.12%), Cognitive Load (8.8753%)
- **Heaviest Functions:** `test_is_typealiastype` (Impact: 2.2), `test_identity_member_check` (Impact: 2.1), `test_is_namedtuple` (Impact: 2.1)

### 8. `typing_inspection-0.4.2/tests/introspection/test_literal_values.py` (PYTHON) -> Cumulative Risk: **169.71**
- **Archetype:** `file_cluster_13` (Distance: 11.066 IQR)
- **Magnitude:** 28.22 | **LOC:** 80 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Api Exposure (8.8562%), Algorithmic Dos (6.2447%)
- **Heaviest Functions:** `test_literal_values_type_check` (Impact: 8.3), `test_literal_values_skip_aliases_type_ch` (Impact: 5.3), `test_literal_values_unpack_type_aliases` (Impact: 2.1)

### 9. `typing_inspection-0.4.2/src/typing_inspection/__init__.py` (PYTHON) -> Cumulative Risk: **68.49**
- **Archetype:** `file_cluster_8` (Distance: 4.447 IQR)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (6.6667%), Documentation (6.6667%), Cognitive Load (5.0%)

### 10. `typing_inspection-0.4.2/tests/introspection/__init__.py` (PYTHON) -> Cumulative Risk: **61.67**
- **Archetype:** `file_cluster_8` (Distance: 4.447 IQR)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Spec Match (6.6667%), Cognitive Load (5.0%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `typing_inspection-0.4.2/src/typing_inspection/typing_objects.pyi` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.339 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.846 IQR)
- **Top Global Matches:** file_cluster_16: 11.339, file_cluster_7: 11.986, file_cluster_13: 12.005
- **Magnitude:** 239.67 | **LOC:** 418 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.9185%), Tech Debt (24.4136%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 40`, `args: 31`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 34`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 32`, `import: 4`
* *Defense:* `doc: 66`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 64.309
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, typing_extensions, types, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.891 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.834 IQR)
- **Top Global Matches:** file_cluster_13: 10.891, file_cluster_7: 11.004, file_cluster_16: 11.066
- **Magnitude:** 106.72 | **LOC:** 608 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (7.291%), Tech Debt (52.6634%)
**Top Internal Functions/Classes:**
  * `_compile_identity_check_function` (Impact: 39.1 | O(N^3))
  * `_compile_isinstance_check_function` (Impact: 35.6 | O(N^3))
  * `is_namedtuple` (Impact: 5.4 | O(N^1))
  * `is_typealiastype` (Impact: 5.3 | O(N^2))
  * `is_newtype` (Impact: 2.7 | O(N^2))
    * *Intent:* """ # Unlikely to have a different version in `typing-extensions`, but keep it consistent. # Also no...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 36`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `api: 6`, `import: 12`
* *Defense:* `safety: 20`, `doc: 74`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 64.309
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, warnings, contextlib, re, textwrap, typing_extensions, types, typing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/src/typing_inspection/introspection.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.891 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.548 IQR)
- **Top Global Matches:** file_cluster_13: 10.891, file_cluster_16: 11.025, file_cluster_7: 11.244
- **Magnitude:** 88.1 | **LOC:** 588 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (19.5005%), Tech Debt (86.7036%)
**Top Internal Functions/Classes:**
  * `allowed_qualifiers` (Impact: 28.6 | O(N^3))
  * `_literal_type_check` (Impact: 8.2 | O(N^2))
  * `is_union_origin` (Impact: 5.4 | O(N^2))
  * `__init__` (Impact: 3.1 | O(N^2) | DB: 1)
  * `is_union_origin` (Impact: 2.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 63`, `args: 11`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 13`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 12`, `import: 9`
* *Defense:* `safety: 12`, `doc: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 228.295
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.25
  * `Imports (Out-Degree: 0):` sys, enum, , typing_inspection, dataclasses, __future__, types, typing_extensions...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `typing_inspection-0.4.2/tests/typing_objects/test_member_checks.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.653 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.651 IQR)
- **Top Global Matches:** file_cluster_0: 11.653, file_cluster_13: 11.774, file_cluster_16: 12.04
- **Magnitude:** 58.0 | **LOC:** 210 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.8753%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_is_typealiastype` (Impact: 2.2 | O(N^1))
  * `test_identity_member_check` (Impact: 2.1 | O(N^1))
  * `test_is_namedtuple` (Impact: 2.1 | O(N^1))
  * `test_is_newtype` (Impact: 2.1 | O(N^1))
  * `test_is_paramspec` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 45`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 16`, `orphaned_logic: 12`
* *Architecture:* `io: 6`, `api: 14`, `import: 11`
* *Defense:* `safety: 18`, `test: 38`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 64.309
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, warnings, typing_inspection, collections, pytest, typing_extensions, types, typing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/tests/introspection/test_inspect_annotation.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.324 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.983 IQR)
- **Top Global Matches:** file_cluster_8: 10.324, file_cluster_13: 10.418, file_cluster_0: 10.429
- **Magnitude:** 48.2 | **LOC:** 207 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.4131%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_annotation_source_invalid_qualifier` (Impact: 10.6 | O(N^3))
  * `test_bare_qualifier` (Impact: 5.7 | O(N^2))
  * `test_annotation_source_valid_qualifiers` (Impact: 5.3 | O(N^2))
  * `test_unpack_type_aliases` (Impact: 3.1 | O(N^2))
  * `test_nested_metadata_and_qualifiers` (Impact: 3.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 57`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `orphaned_logic: 9`
* *Architecture:* `io: 2`, `api: 9`, `import: 8`
* *Defense:* `safety: 22`, `doc: 4`, `test: 43`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 64.309
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sys, typing_inspection.introspection, textwrap, pytest, dataclasses, typing_extensions, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.371 IQR)
- **Top Global Matches:** file_cluster_8: 7.371, file_cluster_7: 7.995, file_cluster_1: 8.297
- **Magnitude:** 42.6 | **LOC:** 40 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.1895%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 1`, `func_start: 9`
* *Risk/State:* None
* *Architecture:* `api: 12`
* *Defense:* `doc: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 64.309
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/tests/introspection/test_literal_values.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.066 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.581 IQR)
- **Top Global Matches:** file_cluster_13: 11.066, file_cluster_16: 11.324, file_cluster_0: 11.42
- **Magnitude:** 28.22 | **LOC:** 80 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.1705%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_literal_values_type_check` (Impact: 8.3 | O(N^2))
  * `test_literal_values_skip_aliases_type_ch` (Impact: 5.3 | O(N^2))
  * `test_literal_values_unpack_type_aliases` (Impact: 2.1 | O(N^1))
  * `test_literal_values_skip_aliases_no_type` (Impact: 1.9 | O(N^1))
  * `test_literal_values_unpack_type_aliases_` (Impact: 1.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 27`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `orphaned_logic: 6`
* *Architecture:* `io: 1`, `api: 6`, `import: 8`
* *Defense:* `safety: 6`, `doc: 2`, `test: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 64.309
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sys, typing_inspection, typing_inspection.introspection, textwrap, pytest, typing_extensions, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/src/typing_inspection/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 64.309
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/tests/introspection/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 64.309
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/tests/typing_objects/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 64.309
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/tests/introspection/test_is_union_origin.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.37 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.172 IQR)
- **Top Global Matches:** file_cluster_13: 10.37, file_cluster_0: 10.928, file_cluster_16: 11.229
- **Magnitude:** 6.48 | **LOC:** 26 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (12.4378%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_is_union_origin` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 11`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 7`
* *Defense:* `safety: 1`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 64.309
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sys, typing_inspection.introspection, pytest, typing_extensions, types, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/HISTORY.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 39 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 64.309
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 21 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 64.309
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `typing_inspection-0.4.2/tests/typing_objects/test_member_checks.py` (PYTHON) | Magnitude: 58.0 | Delta: **0.121 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 45, test: 38, generics: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` (PYTHON) | Magnitude: 106.72 | Delta: **0.113 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 123, doc: 74, encapsulation: 71, structural_boundaries: 36
- `typing_inspection-0.4.2/src/typing_inspection/introspection.py` (PYTHON) | Magnitude: 88.1 | Delta: **0.134 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 210, branch: 75, structural_boundaries: 63, doc: 50
- `typing_inspection-0.4.2/tests/introspection/test_literal_values.py` (PYTHON) | Magnitude: 28.22 | Delta: **0.258 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 27, test: 20, explicit_casts: 11
- `typing_inspection-0.4.2/tests/introspection/test_is_union_origin.py` (PYTHON) | Magnitude: 6.48 | Delta: **0.558 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 11, import: 7, indent_spaces: 6, test: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.pyi` (PYTHON) | Magnitude: 239.67 | Delta: **0.647 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 66, structural_boundaries: 40, safety_bypasses: 34, indent_spaces: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `typing_inspection-0.4.2/tests/introspection/test_inspect_annotation.py` (PYTHON) | Magnitude: 48.2 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 109, structural_boundaries: 57, test: 43, safety: 22
- `typing_inspection-0.4.2/Makefile` (MAKEFILE) | Magnitude: 42.6 | Delta: **0.624 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: api: 12, indent_tabs: 11, func_start: 9, doc: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `typing_inspection-0.4.2/src/typing_inspection/introspection.py` -> **Severity: 20.0** (Embedded: 0.25 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `typing_inspection-0.4.2/Makefile` -> **Severity: 6424.636** (Blast Radius: 64.309 * Doc Risk: 99.9026%)
- `typing_inspection-0.4.2/src/typing_inspection/introspection.py` -> **Severity: 2721.345** (Blast Radius: 228.295 * Doc Risk: 11.9203%)
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` -> **Severity: 766.583** (Blast Radius: 64.309 * Doc Risk: 11.9203%)
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.pyi` -> **Severity: 766.583** (Blast Radius: 64.309 * Doc Risk: 11.9203%)
- `typing_inspection-0.4.2/src/typing_inspection/__init__.py` -> **Severity: 428.729** (Blast Radius: 64.309 * Doc Risk: 6.6667%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
