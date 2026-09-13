# ARCHITECTURAL_BRIEF: typing-inspection
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. A high Structural Surface Profile reading (formerly called Risk Exposure; e.g., Complexity Load, formerly Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict. These are activity/content surface meters, not defect-probability estimates (gitgalaxy#2991, evidence in #2982) -- describe what is there, don't imply it predicts a bug.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates the Structural Surface Profile (Lower 0 - Higher Surface Presence 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws. These 13 vectors are activity/content surface meters -- they describe what is present in a file, not the probability of a defect. The temporal-crucible validation record (gitgalaxy#2982, ~3,550 scanned snapshots, two repositories, pre-registered) tested the per-file-standing-risk claim to exhaustion and found it does not hold; see docs/vectors.md for the full record and gitgalaxy#2991 for the rename this drove. `risk_*` names remain the underlying column/key names for schema compatibility -- see the 'formerly' aliases below.
> 
> 1. **Complexity Load** (formerly Cognitive Load Exposure)**:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Guard Balance** (formerly Error & Exception Risk Exposure)**:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Debt Markers** (formerly Tech Debt Exposure)**:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Test Surface** (formerly Verification Risk Exposure)**:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **Connectivity** (formerly API Risk Exposure)**:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Surface** (formerly Concurrency Risk Exposure)**:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **Mutation Surface** (formerly State Flux Risk Exposure)**:** Measures the frequency of data mutation and variable reassignment.
> 8. **Dead Code Surface** (formerly Commented Logic (dead code))**:** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Alignment** (formerly Spec Match Risk Exposure)**:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Historical Stability** (formerly Stability; predictive layer, promotion pending #2987)**:** Measures the recency of edits relative to the repository's entire lifespan. Part of the family the validation record actually supports as predictive -- currently ablated to zero in every scan (`GITGALAXY_DISABLE_GIT_HISTORY`, temporal-crucible#29).
> 11. **Historical Churn** (formerly Deep Churn; predictive layer, promotion pending #2987)**:** Measures the historical volatility and frequency of modification. Same predictive-layer status and ablation caveat as Historical Stability above.
> 12. **Documentation Surface** (formerly Documentation Risk Exposure)**:** Of the units extracted from a file, the weight-share a reader cannot recover from documentation -- public units count double, runtime-dynamic units count more, and a folder-level documentation umbrella shields the whole file. A ratio over units, not a density over lines; files with no extracted units have no value.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Credential Material** (formerly Secrets Risk Exposure)**:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 23 |
| Analyzed Artifacts (Scanned) | 14 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 9 |
| Total LOC | 981 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 60.9% |
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
| PYTHON | 11 | 951 | 78.6% |
| MARKDOWN | 2 | 0 | 14.3% |
| MAKEFILE | 1 | 30 | 7.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 12 | 85.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 14.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 9*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.yml`: 1x Zero-Density Threshold (LOC: 97, Signals: 0)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 38.9 | 11.9 | 4.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 49.4 | 52.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 83.3 | 8.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.6 | 1.0 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 38.5 | 8.4 | 6.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 19.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 7.9 | 0.7 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 60.7 | 93.3 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 53.9 | 56.6 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 21 | 5 | 6 | `typing_inspection-0.4.2/tests/introspection/test_literal_values.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 98 | 8 | 22 | `typing_inspection-0.4.2/tests/introspection/test_inspect_annotation.py` |
| danger | 113 | 8 | 34 | `typing_inspection-0.4.2/src/typing_inspection/introspection.py` |
| concurrency | 14 | 2 | 6 | `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` |
| connectivity | 132 | 9 | 24 | `typing_inspection-0.4.2/src/typing_inspection/typing_objects.pyi` |
| io | 19 | 8 | 4 | `typing_inspection-0.4.2/tests/typing_objects/test_member_checks.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 1 | 1 | 0 | `typing_inspection-0.4.2/tests/conftest.py` |
| events | 0 | 0 | 0 | - |
| tests | 68 | 6 | 21 | `typing_inspection-0.4.2/tests/typing_objects/test_member_checks.py` |
| docs | 101 | 7 | 33 | `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` |
| debt | 4 | 2 | 1 | `typing_inspection-0.4.2/src/typing_inspection/introspection.py` |
| mutation | 371 | 8 | 87 | `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` |
| dead_code | 31 | 7 | 9 | `typing_inspection-0.4.2/tests/typing_objects/test_member_checks.py` |
| credential | 0 | 0 | 0 | - |
| threat | 9 | 4 | 2 | `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.1535**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

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

1. **conftest.py** (`typing_inspection-0.4.2/tests/conftest.py`) — 12 outbound dependencies
2. **introspection.py** (`typing_inspection-0.4.2/src/typing_inspection/introspection.py`) — 10 outbound dependencies
3. **typing_objects.py** (`typing_inspection-0.4.2/src/typing_inspection/typing_objects.py`) — 9 outbound dependencies
4. **test_member_checks.py** (`typing_inspection-0.4.2/tests/typing_objects/test_member_checks.py`) — 9 outbound dependencies
5. **test_inspect_annotation.py** (`typing_inspection-0.4.2/tests/introspection/test_inspect_annotation.py`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `inspect_annotation` (@ `typing_inspection-0.4.2/src/typing_inspection/introspection.py`) -> Impact: **54.1** | LOC: 122
- `get_literal_values` (@ `typing_inspection-0.4.2/src/typing_inspection/introspection.py`) -> Impact: **49.5** | LOC: 110
- `_unpack_annotated_inner` (@ `typing_inspection-0.4.2/src/typing_inspection/introspection.py`) -> Impact: **25.2** | LOC: 64
- `_compile_identity_check_function` (@ `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py`) -> Impact: **20.8** | LOC: 35
  * *Intent:* """Create a function checking that the function argument is the (unparameterized) typing `member`. The function will make sure to check against both t...
- `_compile_isinstance_check_function` (@ `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py`) -> Impact: **18.4** | LOC: 22
  * *Intent:* """Create a function checking that the function is an instance of the typing `member`. The function will make sure to check against both the `typing` ...
- `run` (@ `typing_inspection-0.4.2/tests/conftest.py`) -> Impact: **13.7** | LOC: 33
- `create_module` (@ `typing_inspection-0.4.2/tests/conftest.py`) -> Impact: **12.3** | LOC: 38
- `allowed_qualifiers` (@ `typing_inspection-0.4.2/src/typing_inspection/introspection.py`) -> Impact: **12.2** | LOC: 17
  * *Intent:* """The allowed [type qualifiers][type qualifier] for this annotation source."""
- `_extract_source_code_from_function` (@ `typing_inspection-0.4.2/tests/conftest.py`) -> Impact: **7.8** | LOC: 14
- `_unpack_annotated` (@ `typing_inspection-0.4.2/src/typing_inspection/introspection.py`) -> Impact: **7.4** | LOC: 10
  * *Intent:* # This could eventually be made public:

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `typing_inspection-0.4.2/src/typing_inspection` | 4 | 593.3 | 20.04% | 24.81% |
| `typing_inspection-0.4.2/tests/introspection` | 4 | 91.92 | 2.83% | 0.0% |
| `typing_inspection-0.4.2/tests/typing_objects` | 2 | 81.92 | 9.32% | 0.0% |
| `typing_inspection-0.4.2/tests` | 1 | 73.44 | 30.0% | 0.0% |
| `typing_inspection-0.4.2` | 3 | 26.3 | 0.74% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.pyi` -> **83.3354%** Exposure
- `typing_inspection-0.4.2/src/typing_inspection/introspection.py` -> **15.8869%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` -> **100.0%** Exposure
- `typing_inspection-0.4.2/src/typing_inspection/introspection.py` -> **99.9999%** Exposure
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.pyi` -> **31.948%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `typing_inspection-0.4.2/tests/typing_objects/test_member_checks.py` -> **12** Orphaned Functions | **0** Duplicates
- `typing_inspection-0.4.2/tests/introspection/test_inspect_annotation.py` -> **9** Orphaned Functions | **0** Duplicates
- `typing_inspection-0.4.2/tests/introspection/test_literal_values.py` -> **6** Orphaned Functions | **0** Duplicates
- `typing_inspection-0.4.2/src/typing_inspection/typing_objects.pyi` -> **1** Orphaned Functions | **0** Duplicates
- `typing_inspection-0.4.2/tests/conftest.py` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `63` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `typing_inspection-0.4.2/src/typing_inspection/introspection.py` (PYTHON) -> Cumulative Risk: **500.36**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 281.8 | **LOC:** 588 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (99.9999%), Safety Score (96.7463%), Spec Match (86.6667%), Documentation (63.1579%)
- **Heaviest Functions:** `inspect_annotation` (Impact: 54.1), `get_literal_values` (Impact: 49.5), `_unpack_annotated_inner` (Impact: 25.2)

### 2. `typing_inspection-0.4.2/tests/conftest.py` (PYTHON) -> Cumulative Risk: **374.73**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 73.44 | **LOC:** 83 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (92.258%), Stability (50.0%)
- **Heaviest Functions:** `run` (Impact: 13.7), `create_module` (Impact: 12.3), `_extract_source_code_from_function` (Impact: 7.8)

### 3. `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` (PYTHON) -> Cumulative Risk: **342.42**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 217.02 | **LOC:** 608 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Safety Score (99.0905%), Stability (50.0%), Documentation (50.0%)
- **Heaviest Functions:** `_compile_identity_check_function` (Impact: 20.8), `_compile_isinstance_check_function` (Impact: 18.4), `is_namedtuple` (Impact: 5.2)

### 4. `typing_inspection-0.4.2/tests/typing_objects/test_member_checks.py` (PYTHON) -> Cumulative Risk: **339.2**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 71.4 | **LOC:** 210 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (60.4327%), Stability (50.0%)
- **Heaviest Functions:** `test_identity_member_check` (Impact: 2.1), `test_is_typealiastype` (Impact: 1.7), `test_is_namedtuple` (Impact: 1.5)

### 5. `typing_inspection-0.4.2/tests/introspection/test_is_union_origin.py` (PYTHON) -> Cumulative Risk: **329.5**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 5.88 | **LOC:** 26 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (71.9676%), Stability (50.0%)
- **Heaviest Functions:** `test_is_union_origin` (Impact: 1.5)

### 6. `typing_inspection-0.4.2/src/typing_inspection/typing_objects.pyi` (PYTHON) -> Cumulative Risk: **325.16**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 83.96 | **LOC:** 418 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Safety Score (99.8734%), Tech Debt (83.3354%), Stability (50.0%), Spec Match (41.9355%)
- **Heaviest Functions:** `is_annotated` (Impact: 1.5), `is_any` (Impact: 1.5), `is_classvar` (Impact: 1.5)

### 7. `typing_inspection-0.4.2/tests/introspection/test_literal_values.py` (PYTHON) -> Cumulative Risk: **304.22**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 26.62 | **LOC:** 80 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Stability (50.0%), Safety Score (45.3655%)
- **Heaviest Functions:** `test_literal_values_skip_aliases_no_type_check` (Impact: 1.9), `test_literal_values_type_check` (Impact: 1.6), `test_literal_values_unpack_type_aliases_undefined` (Impact: 1.5)

### 8. `typing_inspection-0.4.2/tests/introspection/test_inspect_annotation.py` (PYTHON) -> Cumulative Risk: **292.8**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 48.9 | **LOC:** 207 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Stability (50.0%), Safety Score (26.8479%)
- **Heaviest Functions:** `test_annotation_source_invalid_qualifiers` (Impact: 3.7), `test_annotation_source_valid_qualifiers` (Impact: 3.6), `test_bare_qualifier` (Impact: 2.3)

### 9. `typing_inspection-0.4.2/Makefile` (MAKEFILE) -> Cumulative Risk: **200.98**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 24.3 | **LOC:** 40 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Documentation (33.3333%), Api Exposure (13.0471%)
- **Heaviest Functions:** `.uv` (Impact: 2.2), `install` (Impact: 1.2), `test` (Impact: 1.2)

### 10. `typing_inspection-0.4.2/src/typing_inspection/__init__.py` (PYTHON) -> Cumulative Risk: **52.3**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Stability (50.0%), Verification (2.2977%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `typing_inspection-0.4.2/src/typing_inspection/introspection.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 281.8 | **LOC:** 588 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.865%), Tech Debt (15.8869%)
**Top Internal Functions/Classes:**
  * `inspect_annotation` (Impact: 54.1)
  * `get_literal_values` (Impact: 49.5)
  * `_unpack_annotated_inner` (Impact: 25.2)
  * `allowed_qualifiers` (Impact: 12.2)
    * *Intent:* """The allowed [type qualifiers][type qualifier] for this annotation source."""
  * `_unpack_annotated` (Impact: 7.4)
    * *Intent:* # This could eventually be made public:
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 63`, `args: 11`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 40`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `io: 2`, `api: 12`, `import: 9`
* *Defense:* `safety: 12`, `doc: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 202.28
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.214286
  * `Imports (Out-Degree: 0):` , __future__, collections.abc, dataclasses, enum, sys, types, typing...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `typing_inspection-0.4.2/src/typing_inspection/typing_objects.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 217.02 | **LOC:** 608 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.3301%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_compile_identity_check_function` (Impact: 20.8)
    * *Intent:* """Create a function checking that the function argument is the (unparameterized) typing `member`. T...
  * `_compile_isinstance_check_function` (Impact: 18.4)
    * *Intent:* """Create a function checking that the function is an instance of the typing `member`. The function ...
  * `is_namedtuple` (Impact: 5.2)
    * *Intent:* """Return whether the argument is a named tuple type. This includes [`NamedTuple`][typing.NamedTuple...
  * `is_typealiastype` (Impact: 2.9)
    * *Intent:* # Parameterized PEP 695 type aliases are instances of `types.GenericAlias` in typing_extensions>=4.1...
  * `is_newtype` (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 37 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 36`, `args: 7`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 2`, `state_mutation: 81`
* *Architecture:* `io: 4`, `api: 6`, `import: 12`
* *Defense:* `safety: 14`, `doc: 37`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 56.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collections.abc, contextlib, re, sys, textwrap, types, typing, typing_extensions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/src/typing_inspection/typing_objects.pyi` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 83.96 | **LOC:** 418 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.9644%), Tech Debt (83.3354%)
**Top Internal Functions/Classes:**
  * `is_annotated` (Impact: 1.5)
    * *Intent:* """ Return whether the argument is the [`Annotated`][typing.Annotated] [special form][]. ```pycon >>...
  * `is_any` (Impact: 1.5)
    * *Intent:* """ Return whether the argument is the [`Any`][typing.Any] [special form][]. ```pycon >>> is_any(Any...
  * `is_classvar` (Impact: 1.5)
    * *Intent:* """ Return whether the argument is the [`ClassVar`][typing.ClassVar] [type qualifier][]. ```pycon >>...
  * `is_concatenate` (Impact: 1.5)
    * *Intent:* """ Return whether the argument is the [`Concatenate`][typing.Concatenate] [special form][]. ```pyco...
  * `is_final` (Impact: 1.5)
    * *Intent:* """ Return whether the argument is the [`Final`][typing.Final] [type qualifier][]. ```pycon >>> is_f...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 40`, `args: 31`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 2`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 32`, `import: 4`
* *Defense:* `doc: 33`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 56.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sys, types, typing, typing_extensions
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/tests/conftest.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 73.44 | **LOC:** 83 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.9973%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 13.7)
  * `create_module` (Impact: 12.3)
  * `_extract_source_code_from_function` (Impact: 7.8)
  * `_create_module_file` (Impact: 2.5)
    * *Intent:* # Max path length in Windows is 260. Leaving some buffer here max_name_len = 240 - len(str(tmp_path)...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 27`, `args: 4`, `func_start: 4`
* *Risk/State:* `state_mutation: 14`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 2`, `import: 12`
* *Defense:* `safety: 1`, `doc: 1`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 56.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, _pytest.assertion.rewrite, collections.abc, importlib.util, inspect, pathlib, pytest, re...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/tests/typing_objects/test_member_checks.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 71.4 | **LOC:** 210 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.6426%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_identity_member_check` (Impact: 2.1)
  * `test_is_typealiastype` (Impact: 1.7)
  * `test_is_namedtuple` (Impact: 1.5)
  * `test_is_newtype` (Impact: 1.5)
  * `test_is_paramspec` (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 45`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 18`, `unreferenced_by_name: 12`
* *Architecture:* `io: 6`, `api: 14`, `import: 11`
* *Defense:* `safety: 15`, `test: 25`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 56.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collections, collections.abc, pytest, sys, types, typing, typing_extensions, typing_inspection...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/tests/introspection/test_inspect_annotation.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 48.9 | **LOC:** 207 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.3242%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_annotation_source_invalid_qualifiers` (Impact: 3.7)
  * `test_annotation_source_valid_qualifiers` (Impact: 3.6)
  * `test_bare_qualifier` (Impact: 2.3)
  * `test_unpack_type_aliases` (Impact: 1.9)
  * `test_unpack_type_aliases_generic` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 61`, `args: 9`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 18`, `unreferenced_by_name: 9`
* *Architecture:* `io: 2`, `api: 9`, `import: 8`
* *Defense:* `safety: 22`, `doc: 2`, `test: 21`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 56.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dataclasses, pytest, sys, textwrap, typing, typing_extensions, typing_inspection.introspection
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/tests/introspection/test_literal_values.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 26.62 | **LOC:** 80 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_literal_values_skip_aliases_no_type_check` (Impact: 1.9)
  * `test_literal_values_type_check` (Impact: 1.6)
  * `test_literal_values_unpack_type_aliases_undefined` (Impact: 1.5)
  * `test_literal_values_unpack_type_aliases` (Impact: 1.4)
  * `test_literal_values_skip_aliases_type_check` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 32`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 11`, `unreferenced_by_name: 6`
* *Architecture:* `io: 1`, `api: 6`, `import: 8`
* *Defense:* `safety: 6`, `doc: 1`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 56.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pytest, sys, textwrap, typing, typing_extensions, typing_inspection, typing_inspection.introspection
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 24.3 | **LOC:** 40 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.223%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `.uv` (Impact: 2.2)
  * `install` (Impact: 1.2)
  * `test` (Impact: 1.2)
  * `format` (Impact: 1.2)
  * `format-diff` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 1`, `func_start: 9`
* *Risk/State:* None
* *Architecture:* `api: 12`
* *Defense:* `doc: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 56.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/src/typing_inspection/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 56.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/tests/introspection/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 56.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/tests/typing_objects/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 56.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/tests/introspection/test_is_union_origin.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5.88 | **LOC:** 26 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.0086%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_is_union_origin` (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 11`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 7`
* *Defense:* `safety: 1`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 56.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pytest, sys, types, typing, typing_extensions, typing_inspection.introspection
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/HISTORY.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 39 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 56.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `typing_inspection-0.4.2/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 21 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 56.98
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `typing_inspection-0.4.2/src/typing_inspection/introspection.py` -> **Severity: 20.731** (Embedded: 0.2143 * Error Risk: 96.7463%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `typing_inspection-0.4.2/src/typing_inspection/introspection.py` -> **Severity: 12775.58** (Blast Radius: 202.28 * Doc Risk: 63.1579%)
- `typing_inspection-0.4.2/tests/conftest.py` -> **Severity: 5698.0** (Blast Radius: 56.98 * Doc Risk: 100.0%)
- `typing_inspection-0.4.2/tests/introspection/test_inspect_annotation.py` -> **Severity: 5698.0** (Blast Radius: 56.98 * Doc Risk: 100.0%)
- `typing_inspection-0.4.2/tests/introspection/test_is_union_origin.py` -> **Severity: 5698.0** (Blast Radius: 56.98 * Doc Risk: 100.0%)
- `typing_inspection-0.4.2/tests/introspection/test_literal_values.py` -> **Severity: 5698.0** (Blast Radius: 56.98 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
