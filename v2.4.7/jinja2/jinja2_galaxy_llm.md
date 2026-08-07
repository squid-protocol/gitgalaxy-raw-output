# ARCHITECTURAL_BRIEF: jinja2
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/jinja2` |
| **Timestamp** | `2026-08-07T05:23:33.375238+00:00` |
| **Scan Duration** | `0.38s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 49 malicious artifacts.

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
| Total Artifacts | 73 |
| Analyzed Artifacts (Scanned) | 54 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 19 |
| Total LOC | 14014 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 74.0% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2746 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1745 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 29.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.228 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 46 | 13998 | 85.2% |
| M4 | 3 | 9 | 5.6% |
| PLAINTEXT | 2 | 0 | 3.7% |
| HTML | 2 | 7 | 3.7% |
| MARKDOWN | 1 | 0 | 1.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.986`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 20 | 37.0% |
| file_cluster_8 | 13 | 24.1% |
| file_cluster_16 | 8 | 14.8% |
| file_cluster_2 | 8 | 14.8% |
| file_cluster_0 | 1 | 1.9% |
| file_cluster_17 | 1 | 1.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 5.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 19*

**Composition by Extension & Reason:**
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 152 LOC), 1x Excluded (Machine-Generated Source Code Signature: 29 LOC)
- `.py`: 1x Excluded (Saturation: Line 5 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 1207 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 2x Unsupported Format (.undeterminable)
- `.in`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.zip`: 1x Excluded (Explicitly Denied Extension: '.zip')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 46.8 | 10.8 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 92.3 | 33.2 | 11.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 22.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 14.8 | 0.2 | 0.0 |
| API Exposure | 0.0 | 13.6 | 6.3 | 6.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 11.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 24.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 17.8 | 2.3 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 85.6 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 99.3 | 21.9 | 0.8 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `jinja2-3.1.6/src/jinja2/loaders.py` (Hits: 47)
- `jinja2-3.1.6/src/jinja2/bccache.py` (Hits: 19)
- `jinja2-3.1.6/tests/test_loader.py` (Hits: 14)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **typing.in** (`jinja2-3.1.6/requirements/typing.in`) — 21 inbound connections
2. **exceptions.py** (`jinja2-3.1.6/src/jinja2/exceptions.py`) — 19 inbound connections
3. **environment.py** (`jinja2-3.1.6/src/jinja2/environment.py`) — 17 inbound connections
4. **runtime.py** (`jinja2-3.1.6/src/jinja2/runtime.py`) — 15 inbound connections
5. **utils.py** (`jinja2-3.1.6/src/jinja2/utils.py`) — 15 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **environment.py** (`jinja2-3.1.6/src/jinja2/environment.py`) — 25 outbound dependencies
2. **utils.py** (`jinja2-3.1.6/src/jinja2/utils.py`) — 20 outbound dependencies
3. **compiler.py** (`jinja2-3.1.6/src/jinja2/compiler.py`) — 19 outbound dependencies
4. **loaders.py** (`jinja2-3.1.6/src/jinja2/loaders.py`) — 18 outbound dependencies
5. **filters.py** (`jinja2-3.1.6/src/jinja2/filters.py`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `visit_For` (@ `jinja2-3.1.6/src/jinja2/compiler.py`) -> Impact: **90.9** | LOC: 138
- `url_quote` (@ `jinja2-3.1.6/src/jinja2/utils.py`) -> Impact: **72.0** | LOC: 279
- `parse` (@ `jinja2-3.1.6/src/jinja2/ext.py`) -> Impact: **58.1** | LOC: 122
- `visit_Output` (@ `jinja2-3.1.6/src/jinja2/compiler.py`) -> Impact: **55.9** | LOC: 78
- `test_comment_syntax` (@ `jinja2-3.1.6/tests/test_lexnparse.py`) -> Impact: **51.1** | LOC: 121
- `__init__` (@ `jinja2-3.1.6/src/jinja2/bccache.py`) -> Impact: **50.8** | LOC: 135
- `do_filesizeformat` (@ `jinja2-3.1.6/src/jinja2/filters.py`) -> Impact: **43.0** | LOC: 28
- `__call__` (@ `jinja2-3.1.6/src/jinja2/runtime.py`) -> Impact: **41.8** | LOC: 75
- `test_env_async` (@ `jinja2-3.1.6/tests/test_async.py`) -> Impact: **39.2** | LOC: 438
- `pop_assign_tracking` (@ `jinja2-3.1.6/src/jinja2/compiler.py`) -> Impact: **38.4** | LOC: 41

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `jinja2-3.1.6/src/jinja2` | 23 | 4604.16 | 19.16% | 50.77% |
| `jinja2-3.1.6/tests` | 22 | 2438.9 | 3.66% | 0.0% |
| `jinja2-3.1.6/requirements` | 3 | 34.68 | 5.0% | 0.0% |
| `jinja2-3.1.6/tests/res/templates` | 3 | 24.64 | 3.33% | 0.0% |
| `jinja2-3.1.6/tests/res` | 1 | 10.52 | 5.0% | 0.0% |
| `jinja2-3.1.6` | 2 | 2.16 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `jinja2-3.1.6/src/jinja2/exceptions.py` -> **100.0%** Exposure
- `jinja2-3.1.6/src/jinja2/loaders.py` -> **100.0%** Exposure
- `jinja2-3.1.6/src/jinja2/runtime.py` -> **100.0%** Exposure
- `jinja2-3.1.6/src/jinja2/bccache.py` -> **99.9976%** Exposure
- `jinja2-3.1.6/src/jinja2/visitor.py` -> **99.9955%** Exposure
### Highest State Flux (Mutation/Volatility)
- `jinja2-3.1.6/src/jinja2/exceptions.py` -> **99.9951%** Exposure
- `jinja2-3.1.6/src/jinja2/runtime.py` -> **99.7572%** Exposure
- `jinja2-3.1.6/src/jinja2/loaders.py` -> **98.8931%** Exposure
- `jinja2-3.1.6/src/jinja2/visitor.py` -> **95.9865%** Exposure
- `jinja2-3.1.6/src/jinja2/parser.py` -> **95.7672%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `jinja2-3.1.6/tests/test_filters.py` -> **77** Orphaned Functions | **5** Duplicates
- `jinja2-3.1.6/src/jinja2/runtime.py` -> **0** Orphaned Functions | **48** Duplicates
- `jinja2-3.1.6/tests/test_lexnparse.py` -> **43** Orphaned Functions | **0** Duplicates
- `jinja2-3.1.6/tests/test_loader.py` -> **36** Orphaned Functions | **6** Duplicates
- `jinja2-3.1.6/tests/test_core_tags.py` -> **32** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`jinja2-3.1.6/src/jinja2/compiler.py`** -> AI Confidence: **99.31%**
2. **`jinja2-3.1.6/src/jinja2/ext.py`** -> AI Confidence: **99.24%**
3. **`jinja2-3.1.6/src/jinja2/filters.py`** -> AI Confidence: **99.24%**
4. **`jinja2-3.1.6/src/jinja2/lexer.py`** -> AI Confidence: **99.24%**
5. **`jinja2-3.1.6/src/jinja2/loaders.py`** -> AI Confidence: **99.24%**
6. **`jinja2-3.1.6/src/jinja2/nativetypes.py`** -> AI Confidence: **99.18%**
7. **`jinja2-3.1.6/src/jinja2/runtime.py`** -> AI Confidence: **99.18%**
8. **`jinja2-3.1.6/src/jinja2/bccache.py`** -> AI Confidence: **99.16%**
9. **`jinja2-3.1.6/src/jinja2/environment.py`** -> AI Confidence: **99.16%**
10. **`jinja2-3.1.6/src/jinja2/sandbox.py`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `270` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `jinja2-3.1.6/src/jinja2/runtime.py` (PYTHON) -> Cumulative Risk: **695.99**
- **Archetype:** `file_cluster_13` (Distance: 12.732 IQR)
- **Magnitude:** 536.04 | **LOC:** 1063 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.7572%), Concurrency (98.6155%)
- **Heaviest Functions:** `__call__` (Impact: 41.8), `length` (Impact: 8.6), `_undefined_message` (Impact: 7.9)

### 2. `jinja2-3.1.6/src/jinja2/idtracking.py` (PYTHON) -> Cumulative Risk: **626.7**
- **Archetype:** `file_cluster_16` (Distance: 10.419 IQR)
- **Magnitude:** 213.38 | **LOC:** 319 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.994%), Documentation (99.3203%), State Flux (87.1259%)
- **Heaviest Functions:** `branch_update` (Impact: 11.5), `visit_FromImport` (Impact: 8.4), `store` (Impact: 7.8)

### 3. `jinja2-3.1.6/src/jinja2/compiler.py` (PYTHON) -> Cumulative Risk: **582.17**
- **Archetype:** `file_cluster_16` (Distance: 12.21 IQR)
- **Magnitude:** 1012.7 | **LOC:** 1999 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (88.3345%), Verification (80.0%), Documentation (69.4682%)
- **Heaviest Functions:** `visit_For` (Impact: 90.9), `visit_Output` (Impact: 55.9), `pop_assign_tracking` (Impact: 38.4)

### 4. `jinja2-3.1.6/src/jinja2/async_utils.py` (PYTHON) -> Cumulative Risk: **576.68**
- **Archetype:** `file_cluster_13` (Distance: 9.491 IQR)
- **Magnitude:** 69.66 | **LOC:** 100 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.8035%), Documentation (98.9829%), Concurrency (93.7348%)
- **Heaviest Functions:** `async_variant` (Impact: 12.5), `decorator` (Impact: 12.3), `wrapper` (Impact: 5.7)

### 5. `jinja2-3.1.6/src/jinja2/visitor.py` (PYTHON) -> Cumulative Risk: **559.18**
- **Archetype:** `file_cluster_13` (Distance: 12.743 IQR)
- **Magnitude:** 55.68 | **LOC:** 93 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9955%), State Flux (95.9865%), Safety Score (92.2505%)
- **Heaviest Functions:** `generic_visit` (Impact: 23.4), `visit` (Impact: 4.9), `visit_list` (Impact: 4.9)

### 6. `jinja2-3.1.6/src/jinja2/exceptions.py` (PYTHON) -> Cumulative Risk: **548.2**
- **Archetype:** `file_cluster_13` (Distance: 14.471 IQR)
- **Magnitude:** 66.14 | **LOC:** 167 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9951%), Safety Score (77.3613%)
- **Heaviest Functions:** `__str__` (Impact: 13.2), `message` (Impact: 5.3), `__reduce__` (Impact: 2.0)

### 7. `jinja2-3.1.6/src/jinja2/ext.py` (PYTHON) -> Cumulative Risk: **547.33**
- **Archetype:** `file_cluster_16` (Distance: 11.02 IQR)
- **Magnitude:** 273.66 | **LOC:** 871 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.961%), State Flux (88.2992%), Verification (80.0%)
- **Heaviest Functions:** `parse` (Impact: 58.1), `_install_null` (Impact: 13.5), `find_backwards` (Impact: 12.9)

### 8. `jinja2-3.1.6/src/jinja2/parser.py` (PYTHON) -> Cumulative Risk: **532.03**
- **Archetype:** `file_cluster_16` (Distance: 10.891 IQR)
- **Magnitude:** 581.34 | **LOC:** 1050 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (95.7672%), Verification (80.0%), Safety Score (70.6932%)
- **Heaviest Functions:** `parse_from` (Impact: 31.5), `parse_primary` (Impact: 26.3), `parse_test` (Impact: 26.1)

### 9. `jinja2-3.1.6/src/jinja2/utils.py` (PYTHON) -> Cumulative Risk: **530.05**
- **Archetype:** `file_cluster_13` (Distance: 12.215 IQR)
- **Magnitude:** 235.54 | **LOC:** 767 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (94.8503%), Safety Score (83.7656%), Verification (80.0%)
- **Heaviest Functions:** `url_quote` (Impact: 72.0), `import_string` (Impact: 11.1), `object_type_repr` (Impact: 8.7)

### 10. `jinja2-3.1.6/src/jinja2/filters.py` (PYTHON) -> Cumulative Risk: **506.09**
- **Archetype:** `file_cluster_16` (Distance: 11.322 IQR)
- **Magnitude:** 361.34 | **LOC:** 1874 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (80.0%), Verification (80.0%), Tech Debt (66.2533%)
- **Heaviest Functions:** `do_filesizeformat` (Impact: 43.0), `attrgetter` (Impact: 10.6), `attrgetter` (Impact: 8.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `jinja2-3.1.6/src/jinja2/compiler.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.21 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.693 IQR)
- **Top Global Matches:** file_cluster_16: 12.21, file_cluster_13: 12.259, file_cluster_0: 12.365
- **Magnitude:** 1012.7 | **LOC:** 1999 | **CtrlFlow:** 59.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.5098%), Tech Debt (64.8895%)
**Top Internal Functions/Classes:**
  * `visit_For` (Impact: 90.9)
  * `visit_Output` (Impact: 55.9)
  * `pop_assign_tracking` (Impact: 38.4)
  * `visit_Include` (Impact: 36.9)
  * `visit_Block` (Impact: 32.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 388`, `structural_boundaries: 262`, `args: 118`, `func_start: 118`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 156`, `dead_code: 11`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 11`
* *Architecture:* `api: 132`, `concurrency: 14`, `import: 25`
* *Defense:* `safety: 41`, `doc: 100`, `test: 1`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.341
  * `Choke Point (Betweenness):` 0.039399 | `Ripple Effect (Closeness):` 0.278472
  * `Imports (Out-Degree: 8):` typing, .visitor, .utils, keyword, them, typing_extensions, .idtracking, .runtime...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/src/jinja2/parser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.891 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.253 IQR)
- **Top Global Matches:** file_cluster_16: 10.891, file_cluster_8: 11.008, file_cluster_13: 11.221
- **Magnitude:** 581.34 | **LOC:** 1050 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.9136%), Tech Debt (33.6094%)
**Top Internal Functions/Classes:**
  * `parse_from` (Impact: 31.5)
  * `parse_primary` (Impact: 26.3)
  * `parse_test` (Impact: 26.1)
    * *Intent:* # needs to be recorded before the stream is advanced. token = self.stream.current args, kwargs, dyn_...
  * `parse_subscribed` (Impact: 20.6)
  * `parse_block` (Impact: 18.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 231`, `structural_boundaries: 218`, `args: 58`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 116`, `dead_code: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 70`, `import: 9`
* *Defense:* `safety: 10`, `doc: 34`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.56
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.265669
  * `Imports (Out-Degree: 4):` typing, .environment, .lexer, .exceptions, typing_extensions, 
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/src/jinja2/runtime.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.732 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.838 IQR)
- **Top Global Matches:** file_cluster_13: 12.732, file_cluster_16: 12.777, file_cluster_0: 12.785
- **Magnitude:** 536.04 | **LOC:** 1063 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.8405%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__call__` (Impact: 41.8)
  * `length` (Impact: 8.6)
  * `_undefined_message` (Impact: 7.9)
  * `__str__` (Impact: 7.6)
  * `markup_join` (Impact: 6.5)
    * *Intent:* """Concatenation that escapes if necessary and converts to string."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 252`, `args: 82`, `func_start: 82`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 128`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 48`
* *Architecture:* `io: 1`, `api: 51`, `concurrency: 49`, `import: 25`
* *Defense:* `safety: 20`, `doc: 94`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 89.579
  * `Choke Point (Betweenness):` 0.043572 | `Ripple Effect (Closeness):` 0.405495
  * `Imports (Out-Degree: 5):` typing, .environment, .nodes, .async_utils, .utils, logging, itertools, .exceptions...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/tests/test_lexnparse.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_2` (Drift: 12.293 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.586 IQR)
- **Top Global Matches:** file_cluster_2: 12.293, file_cluster_17: 12.336, file_cluster_8: 12.446
- **Magnitude:** 369.94 | **LOC:** 1031 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (1.8674%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_comment_syntax` (Impact: 51.1)
  * `test_balancing` (Impact: 33.7)
  * `test_tuple_expr` (Impact: 18.4)
  * `test_function_calls` (Impact: 9.9)
  * `test_grouping` (Impact: 8.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 272`, `args: 110`, `func_start: 109`, `class_start: 7`
* *Risk/State:* `dead_code: 4`, `fragile_debt: 1`, `orphaned_logic: 43`
* *Architecture:* `api: 115`, `import: 13`
* *Defense:* `safety: 125`, `doc: 88`, `test: 244`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` jinja2, pprint, pytest, jinja2.lexer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/src/jinja2/filters.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.322 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.757 IQR)
- **Top Global Matches:** file_cluster_16: 11.322, file_cluster_13: 11.512, file_cluster_0: 11.527
- **Magnitude:** 361.34 | **LOC:** 1874 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.5193%), Tech Debt (66.2533%)
**Top Internal Functions/Classes:**
  * `do_filesizeformat` (Impact: 43.0)
  * `attrgetter` (Impact: 10.6)
  * `attrgetter` (Impact: 8.8)
  * `do_int` (Impact: 8.7)
  * `do_format` (Impact: 8.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 259`, `args: 94`, `func_start: 85`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 111`, `state_mutation: 21`, `dead_code: 2`, `duplicate_logic: 11`
* *Architecture:* `api: 82`, `concurrency: 24`, `import: 31`
* *Defense:* `safety: 55`, `doc: 130`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.593
  * `Choke Point (Betweenness):` 0.016147 | `Ripple Effect (Closeness):` 0.195875
  * `Imports (Out-Degree: 7):` typing, .environment, .nodes, .async_utils, .runtime, .utils, math, inspect...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/tests/test_filters.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_2` (Drift: 11.85 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.782 IQR)
- **Top Global Matches:** file_cluster_2: 11.85, file_cluster_8: 12.024, file_cluster_13: 12.223
- **Magnitude:** 343.94 | **LOC:** 884 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (1.5692%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_filter_undefined_in_condexpr` (Impact: 16.1)
  * `test_filter_undefined_in_if` (Impact: 13.2)
  * `test_format` (Impact: 7.4)
  * `test_random` (Impact: 6.8)
    * *Intent:* # ensures that filter result is not constant folded random.seed("jinja") t = env.from_string('{{ "12...
  * `test_xmlattr_key_invalid` (Impact: 6.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 267`, `args: 111`, `func_start: 107`, `class_start: 5`
* *Risk/State:* `state_mutation: 3`, `duplicate_logic: 5`, `orphaned_logic: 77`
* *Architecture:* `api: 105`, `import: 10`
* *Defense:* `safety: 131`, `doc: 76`, `test: 250`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` jinja2.exceptions, pprint, jinja2, pytest, markupsafe, collections, random
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/src/jinja2/ext.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.02 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.327 IQR)
- **Top Global Matches:** file_cluster_16: 11.02, file_cluster_13: 11.172, file_cluster_8: 11.395
- **Magnitude:** 273.66 | **LOC:** 871 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.4502%), Tech Debt (99.961%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 58.1)
  * `_install_null` (Impact: 13.5)
  * `find_backwards` (Impact: 12.9)
  * `find_comments` (Impact: 9.0)
    * *Intent:* * ``message`` is the string, or a tuple of strings for functions
  * `npgettext` (Impact: 6.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 140`, `args: 43`, `func_start: 43`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 60`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 15`
* *Architecture:* `api: 34`, `import: 19`
* *Defense:* `safety: 17`, `doc: 41`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.751
  * `Choke Point (Betweenness):` 0.003205 | `Ripple Effect (Closeness):` 0.265669
  * `Imports (Out-Degree: 7):` gettext, typing, pprint, .environment, .lexer, jinja2, .runtime, .utils...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/src/jinja2/utils.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.215 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.088 IQR)
- **Top Global Matches:** file_cluster_13: 12.215, file_cluster_16: 12.22, file_cluster_11: 12.652
- **Magnitude:** 235.54 | **LOC:** 767 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.1091%), Tech Debt (27.276%)
**Top Internal Functions/Classes:**
  * `url_quote` (Impact: 72.0)
  * `import_string` (Impact: 11.1)
  * `object_type_repr` (Impact: 8.7)
  * `consume` (Impact: 4.2)
  * `trim_url` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 155`, `args: 52`, `func_start: 52`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 47`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 49`, `concurrency: 1`, `import: 21`
* *Defense:* `safety: 17`, `doc: 89`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 78.333
  * `Choke Point (Betweenness):` 0.04206 | `Ripple Effect (Closeness):` 0.398504
  * `Imports (Out-Degree: 5):` typing, pprint, types, paths, typing_extensions, os, .lexer, json...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/tests/test_async.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_2` (Drift: 11.799 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.26 IQR)
- **Top Global Matches:** file_cluster_2: 11.799, file_cluster_8: 11.823, file_cluster_13: 11.971
- **Magnitude:** 233.12 | **LOC:** 735 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.9396%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_env_async` (Impact: 39.2)
  * `test_chainable_undefined_aiter` (Impact: 12.0)
    * *Intent:* """ ) sm = t.render( this="/foo", site={"root": {"url": "/", "children": [{"url": "/foo"}, {"url": "...
  * `test_blocks_generate_async` (Impact: 10.2)
  * `_test` (Impact: 8.7)
  * `func` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 215`, `args: 86`, `func_start: 82`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `fragile_debt: 1`, `duplicate_logic: 3`, `orphaned_logic: 6`
* *Architecture:* `api: 80`, `concurrency: 35`, `import: 12`
* *Defense:* `safety: 84`, `doc: 34`, `test: 147`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` jinja2.exceptions, asyncio, jinja2.async_utils, jinja2, pytest, test, with, bar...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/src/jinja2/lexer.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.107 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.576 IQR)
- **Top Global Matches:** file_cluster_16: 11.107, file_cluster_13: 11.177, file_cluster_8: 11.22
- **Magnitude:** 224.14 | **LOC:** 869 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.7947%), Tech Debt (72.369%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 11.4)
    * *Intent:* """A special tuple for marking a point in the state that can have lstrip applied. """
  * `compile_rules` (Impact: 10.0)
  * `describe_token_expr` (Impact: 8.6)
  * `__next__` (Impact: 7.6)
  * `expect` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 115`, `args: 34`, `func_start: 33`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 61`, `dead_code: 4`, `duplicate_logic: 8`
* *Architecture:* `api: 35`, `import: 10`
* *Defense:* `safety: 9`, `doc: 56`, `test: 3`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 38.897
  * `Choke Point (Betweenness):` 0.01022 | `Ripple Effect (Closeness):` 0.308176
  * `Imports (Out-Degree: 4):` typing, ._identifier, .utils, sys, .exceptions, re, typing_extensions, collections...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/src/jinja2/environment.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.851 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.78 IQR)
- **Top Global Matches:** file_cluster_13: 11.851, file_cluster_16: 11.879, file_cluster_0: 12.204
- **Magnitude:** 222.7 | **LOC:** 1673 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.9421%), Tech Debt (9.2475%)
**Top Internal Functions/Classes:**
  * `_environment_config_check` (Impact: 6.8)
  * `getattr` (Impact: 6.5)
  * `extend` (Impact: 5.5)
  * `__init__` (Impact: 5.1)
  * `get_spontaneous_environment` (Impact: 2.0)
    * *Intent:* # for direct template usage we have up to ten living environments
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 300`, `args: 75`, `func_start: 73`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 78`, `high_risk_execution: 2`, `state_mutation: 68`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `io: 6`, `api: 60`, `concurrency: 35`, `import: 61`
* *Defense:* `safety: 64`, `doc: 124`, `test: 6`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 81.539
  * `Choke Point (Betweenness):` 0.151306 | `Ripple Effect (Closeness):` 0.42024
  * `Imports (Out-Degree: 12):` typing, weakref, without, .loaders, .utils, types, .defaults, paths...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/tests/test_loader.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.337 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.319 IQR)
- **Top Global Matches:** file_cluster_13: 12.337, file_cluster_0: 12.497, file_cluster_17: 12.669
- **Magnitude:** 218.56 | **LOC:** 437 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.9884%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_pep_451_import_hook` (Impact: 8.4)
  * `teardown_method` (Impact: 7.3)
  * `test_error_includes_paths` (Impact: 6.8)
  * `compile_down` (Impact: 6.5)
  * `test_package_loader_no_dir` (Impact: 5.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 148`, `args: 49`, `func_start: 48`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 33`, `duplicate_logic: 6`, `orphaned_logic: 36`
* *Architecture:* `io: 14`, `api: 51`, `import: 17`
* *Defense:* `safety: 64`, `doc: 4`, `test: 119`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` jinja2.exceptions, time, weakref, jinja2.loaders, pathlib, jinja2, pytest, importlib.abc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/src/jinja2/idtracking.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.419 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.35 IQR)
- **Top Global Matches:** file_cluster_16: 10.419, file_cluster_8: 10.856, file_cluster_13: 10.946
- **Magnitude:** 213.38 | **LOC:** 319 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.8807%), Tech Debt (99.994%)
**Top Internal Functions/Classes:**
  * `branch_update` (Impact: 11.5)
  * `visit_FromImport` (Impact: 8.4)
  * `store` (Impact: 7.8)
  * `dump_stores` (Impact: 7.5)
  * `dump_param_targets` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 71`, `args: 40`, `func_start: 40`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 24`, `duplicate_logic: 11`
* *Architecture:* `api: 47`, `import: 4`
* *Defense:* `safety: 2`, `doc: 16`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.765
  * `Choke Point (Betweenness):` 0.000726 | `Ripple Effect (Closeness):` 0.215252
  * `Imports (Out-Degree: 2):` typing_extensions, typing, .visitor, 
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/src/jinja2/loaders.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.652 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.985 IQR)
- **Top Global Matches:** file_cluster_13: 12.652, file_cluster_11: 12.758, file_cluster_0: 12.8
- **Magnitude:** 206.56 | **LOC:** 694 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.9223%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `split_template_path` (Impact: 16.7)
  * `list_templates` (Impact: 15.4)
  * `list_templates` (Impact: 11.2)
  * `list_templates` (Impact: 5.5)
  * `_get_zipimporter_files` (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 116`, `args: 34`, `func_start: 32`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 64`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 26`
* *Architecture:* `io: 47`, `api: 32`, `import: 19`
* *Defense:* `safety: 29`, `doc: 34`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.686
  * `Choke Point (Betweenness):` 0.006894 | `Ripple Effect (Closeness):` 0.275157
  * `Imports (Out-Degree: 4):` typing, weakref, os.path, jinja2, .utils, hashlib, zipimport, posixpath...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/tests/test_core_tags.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_2` (Drift: 12.132 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.164 IQR)
- **Top Global Matches:** file_cluster_2: 12.132, file_cluster_8: 12.247, file_cluster_17: 12.484
- **Magnitude:** 180.02 | **LOC:** 604 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (1.3884%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_context_vars` (Impact: 18.7)
  * `test_block_filtered` (Impact: 5.5)
  * `test_intended_scoping_with_set` (Impact: 5.3)
  * `test_loop_unassignable` (Impact: 4.2)
    * *Intent:* %}{{ loop }}{% endfor %}"""
  * `test_namespace_block` (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 171`, `args: 65`, `func_start: 65`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `fragile_debt: 6`, `duplicate_logic: 2`, `orphaned_logic: 32`
* *Architecture:* `api: 69`, `import: 6`
* *Defense:* `safety: 88`, `doc: 58`, `test: 162`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jinja2, test, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/tests/test_ext.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_2` (Drift: 10.861 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.569 IQR)
- **Top Global Matches:** file_cluster_2: 10.861, file_cluster_13: 10.991, file_cluster_8: 11.01
- **Magnitude:** 161.48 | **LOC:** 740 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (1.779%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_extension_nodes` (Impact: 9.8)
    * *Intent:* """ {%- set items = [] %} {%- for char in "foo" %} {%- do items.append(loop.index0 ~ char) %} {%- en...
  * `test_trimmed_vars` (Impact: 9.8)
  * `test_complex_plural` (Impact: 8.7)
  * `test_basic_scope_behavior` (Impact: 6.5)
  * `parse` (Impact: 5.9)
    * *Intent:* """ ) assert list(babel_extract(source, ("pgettext", "npgettext", "_"), [], {})) == [ (2, "pgettext"...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 205`, `args: 68`, `func_start: 65`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `duplicate_logic: 8`, `orphaned_logic: 9`
* *Architecture:* `api: 76`, `import: 17`
* *Defense:* `safety: 72`, `doc: 28`, `test: 127`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` jinja2.exceptions, jinja2, pytest, io, re, jinja2.ext, jinja2.lexer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/src/jinja2/bccache.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.784 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.901 IQR)
- **Top Global Matches:** file_cluster_13: 12.784, file_cluster_16: 13.077, file_cluster_11: 13.126
- **Magnitude:** 154.82 | **LOC:** 409 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.4356%), Tech Debt (99.9976%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 50.8)
  * `dump_bytecode` (Impact: 9.3)
  * `load_bytecode` (Impact: 7.9)
  * `load_bytecode` (Impact: 7.3)
  * `write_bytecode` (Impact: 3.9)
    * *Intent:* # if marshal_load fails then we need to reload try: self.code = marshal.load(f) except (EOFError, Va...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 68`, `args: 26`, `func_start: 26`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 26`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 7`
* *Architecture:* `io: 19`, `api: 26`, `import: 15`
* *Defense:* `safety: 22`, `doc: 34`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.732
  * `Choke Point (Betweenness):` 0.005322 | `Ripple Effect (Closeness):` 0.268758
  * `Imports (Out-Degree: 2):` fnmatch, typing, pickle, errno, marshal, types, io, tempfile...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/tests/test_async_filters.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.522 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.743 IQR)
- **Top Global Matches:** file_cluster_0: 11.522, file_cluster_4: 11.589, file_cluster_13: 11.596
- **Magnitude:** 149.72 | **LOC:** 322 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.1676%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_join_string_list` (Impact: 15.4)
  * `closing_factory` (Impact: 8.7)
  * `closing` (Impact: 5.6)
  * `test_first` (Impact: 4.4)
  * `make_aiter` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 100`, `args: 57`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `orphaned_logic: 7`
* *Architecture:* `api: 40`, `concurrency: 37`, `import: 8`
* *Defense:* `safety: 27`, `doc: 16`, `test: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` asyncio, jinja2.async_utils, jinja2, pytest, trio, contextlib, markupsafe, collections
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/tests/test_regression.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_2` (Drift: 12.337 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.449 IQR)
- **Top Global Matches:** file_cluster_2: 12.337, file_cluster_17: 12.349, file_cluster_13: 12.355
- **Magnitude:** 142.34 | **LOC:** 768 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (1.5514%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_double_caller` (Impact: 21.5)
  * `test_extends_output_bugs` (Impact: 17.9)
  * `test_nested_for_else` (Impact: 6.7)
  * `test_recursive_loop_bug` (Impact: 6.7)
  * `test_loop_include` (Impact: 3.3)
    * *Intent:* """, "c.html": """
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 167`, `args: 62`, `func_start: 58`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `dead_code: 4`, `orphaned_logic: 11`
* *Architecture:* `api: 62`, `import: 13`
* *Defense:* `safety: 68`, `doc: 58`, `test: 130`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` jinja2, jinja2.filters, jinja2.runtime, pytest, jinja2.utils, markupsafe
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/tests/test_inheritance.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.357 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.09 IQR)
- **Top Global Matches:** file_cluster_8: 10.357, file_cluster_2: 10.389, file_cluster_13: 10.766
- **Magnitude:** 95.1 | **LOC:** 411 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (1.6327%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_level2_required` (Impact: 28.3)
  * `test_double_extends` (Impact: 5.4)
  * `test_dynamic_inheritance` (Impact: 5.1)
  * `test_super` (Impact: 3.6)
  * `test_scoped_block` (Impact: 3.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 75`, `args: 23`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `orphaned_logic: 13`
* *Architecture:* `api: 25`, `import: 5`
* *Defense:* `safety: 25`, `doc: 28`, `test: 56`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jinja2, pytest, foo
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/src/jinja2/tests.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.672 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.597 IQR)
- **Top Global Matches:** file_cluster_16: 11.672, file_cluster_13: 11.917, file_cluster_8: 12.097
- **Magnitude:** 84.82 | **LOC:** 257 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.5564%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_integer` (Impact: 6.2)
  * `test_sequence` (Impact: 4.5)
    * *Intent:* # NOTE: The existing 'number' test matches booleans and integers def test_float(value: t.Any) -> boo...
  * `test_iterable` (Impact: 4.5)
  * `test_boolean` (Impact: 4.2)
  * `test_odd` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 61`, `args: 23`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 19`
* *Architecture:* `api: 23`, `import: 7`
* *Defense:* `safety: 12`, `doc: 48`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` operator, typing, numbers, .runtime, .utils, collections, .environment
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/src/jinja2/sandbox.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.02 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.93 IQR)
- **Top Global Matches:** file_cluster_16: 11.02, file_cluster_13: 11.071, file_cluster_8: 11.163
- **Magnitude:** 79.82 | **LOC:** 437 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.5371%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `is_internal_attribute` (Impact: 30.7)
  * `modifies_known_mutable` (Impact: 5.5)
  * `is_safe_attribute` (Impact: 4.7)
  * `safe_range` (Impact: 4.6)
  * `unsafe` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 90`, `args: 18`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 3`
* *Architecture:* `api: 21`, `import: 14`
* *Defense:* `safety: 30`, `doc: 32`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.981
  * `Choke Point (Betweenness):` 0.006682 | `Ripple Effect (Closeness):` 0.162769
  * `Imports (Out-Degree: 4):` operator, typing, .environment, string, .runtime, types, _string, .exceptions...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `jinja2-3.1.6/tests/test_security.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.917 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.283 IQR)
- **Top Global Matches:** file_cluster_13: 10.917, file_cluster_2: 10.922, file_cluster_8: 11.174
- **Magnitude:** 79.48 | **LOC:** 203 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.2009%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_template_data` (Impact: 12.0)
  * `test_safe_format_all_okay` (Impact: 4.5)
  * `test_attr_filter` (Impact: 3.9)
  * `test_unsafe` (Impact: 2.7)
  * `test_restricted` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 78`, `args: 27`, `func_start: 26`, `class_start: 5`
* *Risk/State:* `state_mutation: 4`, `duplicate_logic: 6`, `orphaned_logic: 4`
* *Architecture:* `api: 28`, `import: 10`
* *Defense:* `safety: 21`, `doc: 4`, `test: 53`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` jinja2.exceptions, jinja2, pytest, markupsafe, jinja2.sandbox, jinja2.nodes
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/tests/test_tests.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.046 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.144 IQR)
- **Top Global Matches:** file_cluster_8: 10.046, file_cluster_2: 10.222, file_cluster_13: 10.368
- **Magnitude:** 73.1 | **LOC:** 234 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.2585%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_name_undefined_in_if` (Impact: 6.0)
  * `test_name_undefined` (Impact: 5.3)
  * `test_multiple_tests` (Impact: 4.4)
  * `test_equalto` (Impact: 2.5)
  * `test_types` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 54`, `args: 20`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`, `orphaned_logic: 17`
* *Architecture:* `api: 22`, `import: 5`
* *Defense:* `safety: 21`, `doc: 6`, `test: 45`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 6.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` jinja2, pytest, markupsafe
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jinja2-3.1.6/src/jinja2/async_utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.491 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.112 IQR)
- **Top Global Matches:** file_cluster_13: 9.491, file_cluster_16: 9.652, file_cluster_0: 9.901
- **Magnitude:** 69.66 | **LOC:** 100 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.8653%), Tech Debt (99.8035%)
**Top Internal Functions/Classes:**
  * `async_variant` (Impact: 12.5)
  * `decorator` (Impact: 12.3)
  * `wrapper` (Impact: 5.7)
  * `auto_await` (Impact: 4.7)
    * *Intent:* # Avoid a costly call to isawaitable if type(value) in _common_primitives: return t.cast("V", value)...
  * `__anext__` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 44`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 13`, `concurrency: 5`, `import: 7`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 31.677
  * `Choke Point (Betweenness):` 0.007922 | `Ripple Effect (Closeness):` 0.278472
  * `Imports (Out-Degree: 2):` typing, .utils, inspect, typing_extensions, functools
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `jinja2-3.1.6/tests/test_async_filters.py` (PYTHON) | Magnitude: 149.72 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 165, structural_boundaries: 100, args: 57, test: 57

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `jinja2-3.1.6/src/jinja2/utils.py` (PYTHON) | Magnitude: 235.54 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 313, structural_boundaries: 155, encapsulation: 102, branch: 92
- `jinja2-3.1.6/tests/test_security.py` (PYTHON) | Magnitude: 79.48 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 144, structural_boundaries: 78, test: 53, ui_framework: 36
- `jinja2-3.1.6/src/jinja2/meta.py` (PYTHON) | Magnitude: 49.34 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 37, branch: 18, structural_boundaries: 18, doc: 12
- `jinja2-3.1.6/src/jinja2/environment.py` (PYTHON) | Magnitude: 222.7 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 859, structural_boundaries: 300, generics: 184, branch: 147
- `jinja2-3.1.6/src/jinja2/visitor.py` (PYTHON) | Magnitude: 55.68 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 24, safety_bypasses: 14, doc: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `jinja2-3.1.6/src/jinja2/compiler.py` (PYTHON) | Magnitude: 1012.7 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1405, branch: 388, structural_boundaries: 262, generics: 163
- `jinja2-3.1.6/src/jinja2/sandbox.py` (PYTHON) | Magnitude: 79.82 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 215, structural_boundaries: 90, branch: 47, safety_bypasses: 46
- `jinja2-3.1.6/src/jinja2/lexer.py` (PYTHON) | Magnitude: 224.14 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 500, structural_boundaries: 115, branch: 91, state_mutation: 61
- `jinja2-3.1.6/src/jinja2/parser.py` (PYTHON) | Magnitude: 581.34 | Delta: **0.117 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 836, branch: 231, structural_boundaries: 218, state_mutation: 116
- `jinja2-3.1.6/src/jinja2/ext.py` (PYTHON) | Magnitude: 273.66 | Delta: **0.152 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 516, structural_boundaries: 140, branch: 112, generics: 100

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `jinja2-3.1.6/tests/test_compile.py` (PYTHON) | Magnitude: 46.62 | Delta: **0.248 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 21, state_mutation: 15, test: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `jinja2-3.1.6/tests/test_nativetypes.py` (PYTHON) | Magnitude: 56.52 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 89, structural_boundaries: 73, test: 61, safety: 51
- `jinja2-3.1.6/tests/test_regression.py` (PYTHON) | Magnitude: 142.34 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 403, structural_boundaries: 167, test: 130, ui_framework: 69
- `jinja2-3.1.6/tests/test_async.py` (PYTHON) | Magnitude: 233.12 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 476, structural_boundaries: 215, test: 147, args: 86
- `jinja2-3.1.6/tests/test_lexnparse.py` (PYTHON) | Magnitude: 369.94 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 762, structural_boundaries: 272, test: 244, safety: 125
- `jinja2-3.1.6/tests/test_imports.py` (PYTHON) | Magnitude: 63.22 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 145, structural_boundaries: 60, test: 56, ui_framework: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `jinja2-3.1.6/tests/test_inheritance.py` (PYTHON) | Magnitude: 95.1 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 268, structural_boundaries: 75, test: 56, ui_framework: 36
- `jinja2-3.1.6/tests/test_api.py` (PYTHON) | Magnitude: 35.84 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 324, test: 95, sec_high_risk_execution: 85, structural_boundaries: 82
- `jinja2-3.1.6/tests/test_tests.py` (PYTHON) | Magnitude: 73.1 | Delta: **0.176 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 191, structural_boundaries: 54, test: 45, api: 22
- `jinja2-3.1.6/src/jinja2/constants.py` (PYTHON) | Magnitude: 10.52 | Delta: **0.184 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 2
- `jinja2-3.1.6/src/jinja2/defaults.py` (PYTHON) | Magnitude: 15.78 | Delta: **0.419 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 18, indent_spaces: 15, import: 8, generics: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `jinja2-3.1.6/src/jinja2/environment.py` -> **Severity: 9.903** (Bridge: 0.1513 * Flux: 65.4509%)
- `jinja2-3.1.6/src/jinja2/runtime.py` -> **Severity: 4.347** (Bridge: 0.0436 * Flux: 99.7572%)
- `jinja2-3.1.6/src/jinja2/utils.py` -> **Severity: 3.989** (Bridge: 0.0421 * Flux: 94.8503%)
- `jinja2-3.1.6/src/jinja2/compiler.py` -> **Severity: 3.48** (Bridge: 0.0394 * Flux: 88.3345%)
- `jinja2-3.1.6/src/jinja2/exceptions.py` -> **Severity: 1.276** (Bridge: 0.0128 * Flux: 99.9951%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `jinja2-3.1.6/src/jinja2/runtime.py` -> **Severity: 33.892** (Embedded: 0.4055 * Error Risk: 83.5806%)
- `jinja2-3.1.6/src/jinja2/utils.py` -> **Severity: 33.381** (Embedded: 0.3985 * Error Risk: 83.7656%)
- `jinja2-3.1.6/src/jinja2/exceptions.py` -> **Severity: 32.51** (Embedded: 0.4202 * Error Risk: 77.3613%)
- `jinja2-3.1.6/src/jinja2/environment.py` -> **Severity: 30.78** (Embedded: 0.4202 * Error Risk: 73.2432%)
- `jinja2-3.1.6/src/jinja2/debug.py` -> **Severity: 21.873** (Embedded: 0.2688 * Error Risk: 81.3857%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `jinja2-3.1.6/src/jinja2/exceptions.py` -> **Severity: 4104.418** (Blast Radius: 78.994 * Doc Risk: 51.9586%)
- `jinja2-3.1.6/src/jinja2/utils.py` -> **Severity: 3962.475** (Blast Radius: 78.333 * Doc Risk: 50.585%)
- `jinja2-3.1.6/src/jinja2/async_utils.py` -> **Severity: 3135.481** (Blast Radius: 31.677 * Doc Risk: 98.9829%)
- `jinja2-3.1.6/src/jinja2/runtime.py` -> **Severity: 2344.488** (Blast Radius: 89.579 * Doc Risk: 26.1723%)
- `jinja2-3.1.6/src/jinja2/idtracking.py` -> **Severity: 1466.464** (Blast Radius: 14.765 * Doc Risk: 99.3203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
