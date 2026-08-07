# ARCHITECTURAL_BRIEF: poetry-core
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/poetry-core` |
| **Timestamp** | `2026-08-07T05:24:49.160074+00:00` |
| **Scan Duration** | `0.82s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 267 malicious artifacts.

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
| Total Artifacts | 496 |
| Analyzed Artifacts (Scanned) | 322 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 174 |
| Total LOC | 23551 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 64.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5494 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0688 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.6166 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 18 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 258 | 22279 | 80.1% |
| PLAINTEXT | 42 | 0 | 13.0% |
| JSON | 6 | 1113 | 1.9% |
| SHELL | 6 | 12 | 1.9% |
| MARKDOWN | 4 | 0 | 1.2% |
| XML | 3 | 0 | 0.9% |
| C | 3 | 147 | 0.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.349`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 198 | 61.5% |
| file_cluster_13 | 56 | 17.4% |
| file_cluster_16 | 19 | 5.9% |
| file_cluster_0 | 3 | 0.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 46 | 14.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 174*

**Composition by Extension & Reason:**
- `.toml`: 86x Excluded (Unsupported Extension: '.toml')
- `.rst`: 41x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Unsupported Format (.undeterminable)
- `.py`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.typed`: 4x Excluded (Unsupported Extension: '.typed')
- `.json`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 3638 LOC)
- `.lark`: 2x Excluded (Unsupported Extension: '.lark')
- `.zip`: 1x Excluded (Explicitly Denied Extension: '.zip')
- `.whl`: 1x Excluded (Unsupported Extension: '.whl')
- `.gz`: 1x Excluded (Explicitly Denied Extension: '.gz')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 12.8 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 91.0 | 14.4 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 5.6 | 0.0 | 0.0 |
| API Exposure | 0.0 | 13.4 | 2.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 15.7 | 0.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 12.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 11.3 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 44.3 | 6.7 | 6.7 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 15.8 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `poetry_core-2.3.2/tests/packages/test_main.py` (Hits: 29)
- `poetry_core-2.3.2/tests/test_factory.py` (Hits: 22)
- `poetry_core-2.3.2/src/poetry/core/masonry/builders/wheel.py` (Hits: 15)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **utils.py** (`poetry_core-2.3.2/src/poetry/core/packages/utils/utils.py`) — 21 inbound connections
2. **dependency.py** (`poetry_core-2.3.2/src/poetry/core/packages/dependency.py`) — 16 inbound connections
3. **markers.py** (`poetry_core-2.3.2/src/poetry/core/version/markers.py`) — 12 inbound connections
4. **directory_dependency.py** (`poetry_core-2.3.2/src/poetry/core/packages/directory_dependency.py`) — 11 inbound connections
5. **file_dependency.py** (`poetry_core-2.3.2/src/poetry/core/packages/file_dependency.py`) — 9 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **wheel.py** (`poetry_core-2.3.2/src/poetry/core/masonry/builders/wheel.py`) — 30 outbound dependencies
2. **factory.py** (`poetry_core-2.3.2/src/poetry/core/factory.py`) — 25 outbound dependencies
3. **dependency.py** (`poetry_core-2.3.2/src/poetry/core/packages/dependency.py`) — 22 outbound dependencies
4. **package.py** (`poetry_core-2.3.2/src/poetry/core/packages/package.py`) — 22 outbound dependencies
5. **test_package.py** (`poetry_core-2.3.2/tests/packages/test_package.py`) — 20 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `test_validate_strict_fails_strict_and_no` (@ `poetry_core-2.3.2/tests/test_factory.py`) -> Impact: **153.5** | LOC: 853
- `to_pep_508` (@ `poetry_core-2.3.2/src/poetry/core/packages/dependency.py`) -> Impact: **122.1** | LOC: 206
- `test_create_poetry` (@ `poetry_core-2.3.2/tests/test_factory.py`) -> Impact: **63.2** | LOC: 144
- `union` (@ `poetry_core-2.3.2/src/poetry/core/constraints/generic/union_constraint.py`) -> Impact: **59.3** | LOC: 77
- `difference` (@ `poetry_core-2.3.2/src/poetry/core/constraints/version/version_range.py`) -> Impact: **53.1** | LOC: 93
- `intersect` (@ `poetry_core-2.3.2/src/poetry/core/constraints/generic/union_constraint.py`) -> Impact: **45.0** | LOC: 69
- `complete_legacy_duplicate_warnings` (@ `poetry_core-2.3.2/tests/test_factory.py`) -> Impact: **41.9** | LOC: 76
- `is_same_source_as` (@ `poetry_core-2.3.2/src/poetry/core/packages/specification.py`) -> Impact: **40.8** | LOC: 54
- `difference` (@ `poetry_core-2.3.2/src/poetry/core/constraints/version/version_union.py`) -> Impact: **40.5** | LOC: 82
- `find_files_to_add` (@ `poetry_core-2.3.2/src/poetry/core/masonry/builders/builder.py`) -> Impact: **40.3** | LOC: 79

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `poetry_core-2.3.2/src/poetry/core/packages` | 11 | 1309.36 | 63.96% | 26.12% |
| `poetry_core-2.3.2/src/poetry/core/constraints/version` | 11 | 1021.04 | 23.49% | 0.0% |
| `poetry_core-2.3.2/src/poetry/core/version` | 6 | 970.04 | 32.08% | 16.67% |
| `poetry_core-2.3.2/src/poetry/core/constraints/generic` | 8 | 743.0 | 29.16% | 24.94% |
| `poetry_core-2.3.2/tests/packages` | 10 | 655.36 | 3.36% | 0.0% |
| `poetry_core-2.3.2/tests/version` | 3 | 531.26 | 5.45% | 0.0% |
| `poetry_core-2.3.2/tests` | 4 | 517.78 | 4.08% | 0.0% |
| `poetry_core-2.3.2/src/poetry/core/masonry/builders` | 3 | 470.18 | 24.28% | 12.2% |
| `poetry_core-2.3.2/src/poetry/core/version/pep440` | 4 | 457.5 | 47.7% | 49.68% |
| `poetry_core-2.3.2/tests/masonry/builders` | 4 | 435.88 | 3.75% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `poetry_core-2.3.2/src/poetry/core/packages/project_package.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/version/markers.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/version/pep440/segments.py` -> **99.9926%** Exposure
- `poetry_core-2.3.2/src/poetry/core/constraints/generic/constraint.py` -> **99.7679%** Exposure
- `poetry_core-2.3.2/src/poetry/core/constraints/generic/multi_constraint.py` -> **99.7268%** Exposure
### Highest State Flux (Mutation/Volatility)
- `poetry_core-2.3.2/src/poetry/core/__init__.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/masonry/utils/include.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/masonry/utils/module.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/masonry/utils/package_include.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/packages/utils/link.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `poetry_core-2.3.2/src/poetry/core/version/markers.py` -> **0** Orphaned Functions | **101** Duplicates
- `poetry_core-2.3.2/tests/version/test_markers.py` -> **52** Orphaned Functions | **8** Duplicates
- `poetry_core-2.3.2/tests/packages/test_package.py` -> **47** Orphaned Functions | **0** Duplicates
- `poetry_core-2.3.2/tests/test_factory.py` -> **26** Orphaned Functions | **0** Duplicates
- `poetry_core-2.3.2/tests/version/pep440/test_version.py` -> **23** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`poetry_core-2.3.2/tests/version/test_markers.py`** -> AI Confidence: **99.39%**
2. **`poetry_core-2.3.2/src/poetry/core/constraints/generic/union_constraint.py`** -> AI Confidence: **99.31%**
3. **`poetry_core-2.3.2/src/poetry/core/constraints/version/version_range.py`** -> AI Confidence: **99.31%**
4. **`poetry_core-2.3.2/src/poetry/core/factory.py`** -> AI Confidence: **99.31%**
5. **`poetry_core-2.3.2/src/poetry/core/masonry/builders/builder.py`** -> AI Confidence: **99.31%**
6. **`poetry_core-2.3.2/src/poetry/core/masonry/metadata.py`** -> AI Confidence: **99.31%**
7. **`poetry_core-2.3.2/src/poetry/core/packages/dependency_group.py`** -> AI Confidence: **99.31%**
8. **`poetry_core-2.3.2/src/poetry/core/packages/utils/utils.py`** -> AI Confidence: **99.31%**
9. **`poetry_core-2.3.2/src/poetry/core/version/pep440/parser.py`** -> AI Confidence: **99.31%**
10. **`poetry_core-2.3.2/tests/packages/test_dependency_group.py`** -> AI Confidence: **99.31%**
11. **`poetry_core-2.3.2/tests/packages/utils/test_utils.py`** -> AI Confidence: **99.31%**
12. **`poetry_core-2.3.2/src/poetry/core/constraints/version/parser.py`** -> AI Confidence: **99.24%**
13. **`poetry_core-2.3.2/src/poetry/core/version/markers.py`** -> AI Confidence: **99.24%**
14. **`poetry_core-2.3.2/src/poetry/core/vcs/git.py`** -> AI Confidence: **99.23%**
15. **`poetry_core-2.3.2/src/poetry/core/constraints/version/version.py`** -> AI Confidence: **99.18%**
16. **`poetry_core-2.3.2/src/poetry/core/pyproject/toml.py`** -> AI Confidence: **99.18%**
17. **`poetry_core-2.3.2/src/poetry/core/spdx/helpers.py`** -> AI Confidence: **99.18%**
18. **`poetry_core-2.3.2/tests/masonry/builders/test_builder.py`** -> AI Confidence: **99.18%**
19. **`poetry_core-2.3.2/tests/masonry/test_api.py`** -> AI Confidence: **99.18%**
20. **`poetry_core-2.3.2/tests/packages/test_file_dependency.py`** -> AI Confidence: **99.18%**
21. **`poetry_core-2.3.2/tests/testutils.py`** -> AI Confidence: **99.18%**
22. **`poetry_core-2.3.2/src/poetry/core/masonry/builders/wheel.py`** -> AI Confidence: **99.16%**
23. **`poetry_core-2.3.2/src/poetry/core/packages/dependency.py`** -> AI Confidence: **99.16%**
24. **`poetry_core-2.3.2/src/poetry/core/packages/package.py`** -> AI Confidence: **99.16%**
25. **`poetry_core-2.3.2/src/poetry/core/version/requirements.py`** -> AI Confidence: **99.16%**
26. **`poetry_core-2.3.2/tests/test_factory.py`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `798` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `poetry_core-2.3.2/src/poetry/core/packages/dependency.py` (PYTHON) -> Cumulative Risk: **662.81**
- **Archetype:** `file_cluster_13` (Distance: 11.092 IQR)
- **Magnitude:** 361.88 | **LOC:** 546 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.663%), Tech Debt (93.7206%), Documentation (84.3505%)
- **Heaviest Functions:** `to_pep_508` (Impact: 122.1), `marker` (Impact: 31.5), `base_pep_508_name` (Impact: 15.2)

### 2. `poetry_core-2.3.2/src/poetry/core/packages/package.py` (PYTHON) -> Cumulative Risk: **650.22**
- **Archetype:** `file_cluster_13` (Distance: 11.391 IQR)
- **Magnitude:** 374.44 | **LOC:** 681 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.7191%), Tech Debt (93.6355%), Documentation (90.1238%)
- **Heaviest Functions:** `all_classifiers` (Impact: 25.2), `to_dependency` (Impact: 19.0), `__repr__` (Impact: 15.3)

### 3. `poetry_core-2.3.2/src/poetry/core/constraints/generic/constraint.py` (PYTHON) -> Cumulative Risk: **646.65**
- **Archetype:** `file_cluster_13` (Distance: 11.582 IQR)
- **Magnitude:** 217.02 | **LOC:** 259 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8237%), Tech Debt (99.7679%), Documentation (91.1835%)
- **Heaviest Functions:** `union` (Impact: 24.2), `allows_all` (Impact: 22.1), `allows_any` (Impact: 22.1)

### 4. `poetry_core-2.3.2/src/poetry/core/packages/project_package.py` (PYTHON) -> Cumulative Risk: **642.03**
- **Archetype:** `file_cluster_13` (Distance: 10.763 IQR)
- **Magnitude:** 68.34 | **LOC:** 126 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.7517%), Documentation (97.8627%)
- **Heaviest Functions:** `python_versions` (Impact: 8.0), `all_classifiers` (Impact: 3.7), `to_dependency` (Impact: 2.0)

### 5. `poetry_core-2.3.2/src/poetry/core/packages/specification.py` (PYTHON) -> Cumulative Risk: **594.87**
- **Archetype:** `file_cluster_13` (Distance: 10.88 IQR)
- **Magnitude:** 145.8 | **LOC:** 228 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (98.4097%), State Flux (96.933%), Cognitive Load (88.0717%)
- **Heaviest Functions:** `is_same_source_as` (Impact: 40.8), `__hash__` (Impact: 4.2), `complete_name` (Impact: 3.9)

### 6. `poetry_core-2.3.2/src/poetry/core/masonry/utils/package_include.py` (PYTHON) -> Cumulative Risk: **581.51**
- **Archetype:** `file_cluster_13` (Distance: 11.812 IQR)
- **Magnitude:** 87.16 | **LOC:** 99 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (97.6289%)
- **Heaviest Functions:** `check_elements` (Impact: 17.0), `is_stub_only` (Impact: 10.8), `has_modules` (Impact: 3.7)

### 7. `poetry_core-2.3.2/src/poetry/core/packages/dependency_group.py` (PYTHON) -> Cumulative Risk: **574.91**
- **Archetype:** `file_cluster_13` (Distance: 10.757 IQR)
- **Magnitude:** 152.76 | **LOC:** 222 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8091%), Cognitive Load (83.6165%), Documentation (81.4523%)
- **Heaviest Functions:** `dependencies_for_locking` (Impact: 28.1), `dependencies` (Impact: 21.9), `remove_dependency` (Impact: 9.6)

### 8. `poetry_core-2.3.2/src/poetry/core/version/markers.py` (PYTHON) -> Cumulative Risk: **565.78**
- **Archetype:** `file_cluster_13` (Distance: 12.249 IQR)
- **Magnitude:** 824.84 | **LOC:** 1396 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (95.9723%), Documentation (77.298%)
- **Heaviest Functions:** `intersect_simplify` (Impact: 39.0), `union_simplify` (Impact: 38.9), `of` (Impact: 38.0)

### 9. `poetry_core-2.3.2/src/poetry/core/packages/vcs_dependency.py` (PYTHON) -> Cumulative Risk: **563.89**
- **Archetype:** `file_cluster_16` (Distance: 10.016 IQR)
- **Magnitude:** 81.5 | **LOC:** 140 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (97.1022%), State Flux (87.1073%), Cognitive Load (83.0592%)
- **Heaviest Functions:** `_base_pep_508_name` (Impact: 15.0), `pretty_constraint` (Impact: 9.4), `reference` (Impact: 7.1)

### 10. `poetry_core-2.3.2/src/poetry/core/masonry/builders/builder.py` (PYTHON) -> Cumulative Risk: **560.11**
- **Archetype:** `file_cluster_13` (Distance: 11.181 IQR)
- **Magnitude:** 276.54 | **LOC:** 391 | **CtrlFlow:** 53.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.4716%), Verification (80.0%), Documentation (73.3159%)
- **Heaviest Functions:** `find_files_to_add` (Impact: 40.3), `get_metadata_content` (Impact: 30.9), `find_excluded_files` (Impact: 29.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `poetry_core-2.3.2/src/poetry/core/version/markers.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.249 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.686 IQR)
- **Top Global Matches:** file_cluster_13: 12.249, file_cluster_0: 12.345, file_cluster_16: 12.367
- **Magnitude:** 824.84 | **LOC:** 1396 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.5405%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `intersect_simplify` (Impact: 39.0)
  * `union_simplify` (Impact: 38.9)
  * `of` (Impact: 38.0)
  * `of` (Impact: 34.2)
  * `invert` (Impact: 33.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `structural_boundaries: 409`, `args: 120`, `func_start: 118`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 135`, `dead_code: 2`, `duplicate_logic: 101`
* *Architecture:* `io: 2`, `api: 93`, `concurrency: 2`, `import: 46`
* *Defense:* `safety: 80`, `doc: 20`, `test: 7`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 51.513
  * `Choke Point (Betweenness):` 0.003845 | `Ripple Effect (Closeness):` 0.071651
  * `Imports (Out-Degree: 4):` threading, __future__, abc, functools, packaging.utils, poetry.core.constraints.version, poetry.core.constraints.generic.parser, itertools...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/tests/version/test_markers.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.601 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.686 IQR)
- **Top Global Matches:** file_cluster_8: 10.601, file_cluster_16: 11.238, file_cluster_7: 11.276
- **Magnitude:** 506.4 | **LOC:** 2764 | **CtrlFlow:** 77.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.2525%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_marker_union_union_duplicates` (Impact: 18.4)
  * `test_marker_union_intersect_multi_marker` (Impact: 16.6)
  * `test_multi_marker_union_with_union` (Impact: 16.4)
  * `test_marker_union_intersect_marker_union` (Impact: 16.3)
  * `test_single_marker_union_with_union_dupl` (Impact: 12.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 867`, `structural_boundaries: 255`, `args: 88`, `func_start: 88`
* *Risk/State:* `duplicate_logic: 8`, `orphaned_logic: 52`
* *Architecture:* `io: 4`, `api: 88`, `import: 20`
* *Defense:* `safety: 131`, `doc: 12`, `test: 239`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.839
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, poetry.core.constraints.version, pytest, poetry.core.constraints.generic, poetry.core.version.markers, typing, os
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `poetry_core-2.3.2/tests/test_factory.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.996 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.272 IQR)
- **Top Global Matches:** file_cluster_8: 11.996, file_cluster_16: 12.116, file_cluster_0: 12.159
- **Magnitude:** 486.62 | **LOC:** 2109 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.7775%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_validate_strict_fails_strict_and_no` (Impact: 153.5)
  * `test_create_poetry` (Impact: 63.2)
  * `complete_legacy_duplicate_warnings` (Impact: 41.9)
  * `complete_legacy_warnings` (Impact: 16.4)
  * `test_create_poetry_with_groups` (Impact: 13.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 329`, `args: 68`, `func_start: 64`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 27`, `orphaned_logic: 26`
* *Architecture:* `io: 22`, `api: 64`, `import: 21`
* *Defense:* `safety: 190`, `doc: 82`, `test: 302`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.839
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` __future__, poetry.core.pyproject.tables, poetry.core.utils._compat, packaging.utils, poetry.core.constraints.version, pathlib, poetry.core.packages.dependency, poetry.core.packages.vcs_dependency...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `poetry_core-2.3.2/src/poetry/core/packages/package.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.391 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.833 IQR)
- **Top Global Matches:** file_cluster_13: 11.391, file_cluster_0: 11.594, file_cluster_16: 11.68
- **Magnitude:** 374.44 | **LOC:** 681 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.9593%), Tech Debt (93.6355%)
**Top Internal Functions/Classes:**
  * `all_classifiers` (Impact: 25.2)
  * `to_dependency` (Impact: 19.0)
  * `__repr__` (Impact: 15.3)
    * *Intent:* # The dependency specifies a source: this package matches if and only if it is
  * `full_pretty_version` (Impact: 14.8)
  * `source_satisfies` (Impact: 11.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 189`, `args: 47`, `func_start: 46`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 79`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `io: 2`, `api: 59`, `import: 40`
* *Defense:* `safety: 13`, `doc: 16`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.613
  * `Choke Point (Betweenness):` 0.00056 | `Ripple Effect (Closeness):` 0.016983
  * `Imports (Out-Degree: 14):` warnings, poetry.core.packages.utils.utils, poetry.core.spdx.helpers, poetry.core.packages.url_dependency, poetry.core.spdx.license, poetry.core.packages.dependency_group, typing, poetry.core.packages.specification...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/packages/dependency.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.092 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.524 IQR)
- **Top Global Matches:** file_cluster_13: 11.092, file_cluster_0: 11.478, file_cluster_16: 11.591
- **Magnitude:** 361.88 | **LOC:** 546 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.8499%), Tech Debt (93.7206%)
**Top Internal Functions/Classes:**
  * `to_pep_508` (Impact: 122.1)
  * `marker` (Impact: 31.5)
  * `base_pep_508_name` (Impact: 15.2)
  * `__eq__` (Impact: 7.5)
  * `__str__` (Impact: 7.3)
    * *Intent:* # "constraint" is implicitly given for direct origin dependencies and might not # be set yet ("*"). ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 160`, `args: 35`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 80`, `dead_code: 1`, `duplicate_logic: 8`
* *Architecture:* `io: 4`, `api: 38`, `import: 46`
* *Defense:* `safety: 5`, `doc: 10`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.143
  * `Choke Point (Betweenness):` 0.003784 | `Ripple Effect (Closeness):` 0.06237
  * `Imports (Out-Degree: 12):` poetry.core.version.requirements, poetry.core.packages.utils.link, poetry.core.packages.utils.utils, poetry.core.packages.url_dependency, poetry.core.packages.dependency_group, typing, poetry.core.packages.specification, pathlib...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/constraints/version/version_range.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.937 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.186 IQR)
- **Top Global Matches:** file_cluster_13: 10.937, file_cluster_8: 11.039, file_cluster_16: 11.129
- **Magnitude:** 359.16 | **LOC:** 473 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.3191%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `difference` (Impact: 53.1)
  * `intersect` (Impact: 36.2)
  * `allows` (Impact: 33.5)
  * `union` (Impact: 32.0)
  * `__str__` (Impact: 20.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 152`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 31`
* *Architecture:* `api: 28`, `import: 16`
* *Defense:* `safety: 25`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.207
  * `Choke Point (Betweenness):` 0.000278 | `Ripple Effect (Closeness):` 0.021937
  * `Imports (Out-Degree: 5):` __future__, functools, poetry.core.constraints.version.version_range_constraint, poetry.core.constraints.version.version_constraint, poetry.core.constraints.version.empty_constraint, poetry.core.constraints.version.version, poetry.core.constraints.version.version_union, contextlib...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/masonry/builders/builder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.181 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.735 IQR)
- **Top Global Matches:** file_cluster_13: 11.181, file_cluster_16: 11.261, file_cluster_8: 11.452
- **Magnitude:** 276.54 | **LOC:** 391 | **CtrlFlow:** 53.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.7646%), Tech Debt (36.5947%)
**Top Internal Functions/Classes:**
  * `find_files_to_add` (Impact: 40.3)
  * `get_metadata_content` (Impact: 30.9)
  * `find_excluded_files` (Impact: 29.5)
  * `convert_script_files` (Impact: 15.3)
  * `_module` (Impact: 13.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 75`, `args: 23`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 53`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 26`, `import: 14`
* *Defense:* `safety: 6`, `doc: 12`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.948
  * `Choke Point (Betweenness):` 0.000183 | `Ripple Effect (Closeness):` 0.009735
  * `Imports (Out-Degree: 4):` __future__, functools, poetry.core.masonry.utils.package_include, pathlib, sys, poetry.core.masonry.metadata, poetry.core.vcs, poetry.core.poetry...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/constraints/version/version_union.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.228 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.419 IQR)
- **Top Global Matches:** file_cluster_13: 11.228, file_cluster_16: 11.394, file_cluster_0: 11.464
- **Magnitude:** 233.16 | **LOC:** 325 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.179%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `difference` (Impact: 40.5)
  * `of` (Impact: 28.3)
  * `excludes_single_wildcard_range` (Impact: 18.3)
  * `intersect` (Impact: 11.4)
  * `allows_any` (Impact: 11.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 114`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 25`
* *Architecture:* `api: 23`, `import: 15`
* *Defense:* `safety: 21`, `doc: 4`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.97
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.017549
  * `Imports (Out-Degree: 5):` __future__, functools, poetry.core.constraints.version.version_range, poetry.core.constraints.version.version_range_constraint, poetry.core.constraints.version.version_constraint, poetry.core.constraints.version.empty_constraint, operator, poetry.core.constraints.version.version...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/tests/masonry/builders/test_wheel.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.958 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.233 IQR)
- **Top Global Matches:** file_cluster_8: 11.958, file_cluster_13: 11.985, file_cluster_16: 12.013
- **Magnitude:** 220.84 | **LOC:** 624 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.0306%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_wheel_package_target_dir` (Impact: 11.2)
  * `test_tag` (Impact: 9.4)
  * `clear_samples_build` (Impact: 9.0)
  * `test_wheel_include_formats` (Impact: 6.9)
  * `test_extended_editable_wheel_build` (Impact: 5.8)
    * *Intent:* """Tests that an editable wheel made from a project with extensions includes the .pth, but does not ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 202`, `args: 35`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 3`, `fragile_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `io: 3`, `api: 64`, `import: 19`
* *Defense:* `safety: 108`, `doc: 12`, `test: 153`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.361
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003115
  * `Imports (Out-Degree: 2):` __future__, typing, re, pathlib, poetry.core.masonry.builders.wheel, importlib.machinery, tests.masonry.builders.test_sdist, pytest...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/constraints/generic/constraint.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.582 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.661 IQR)
- **Top Global Matches:** file_cluster_13: 11.582, file_cluster_16: 11.847, file_cluster_8: 11.962
- **Magnitude:** 217.02 | **LOC:** 259 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.7709%), Tech Debt (99.7679%)
**Top Internal Functions/Classes:**
  * `union` (Impact: 24.2)
  * `allows_all` (Impact: 22.1)
  * `allows_any` (Impact: 22.1)
  * `intersect` (Impact: 13.1)
  * `allows` (Impact: 10.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 104`, `args: 20`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `state_mutation: 39`, `duplicate_logic: 6`
* *Architecture:* `api: 21`, `import: 15`
* *Defense:* `safety: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.056
  * `Choke Point (Betweenness):` 0.00048 | `Ripple Effect (Closeness):` 0.045577
  * `Imports (Out-Degree: 5):` __future__, poetry.core.constraints.generic.union_constraint, poetry.core.constraints.generic.base_constraint, poetry.core.constraints.generic.empty_constraint, collections.abc, poetry.core.constraints.generic, poetry.core.constraints.generic.multi_constraint, operator...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/constraints/generic/union_constraint.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.67 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.35 IQR)
- **Top Global Matches:** file_cluster_13: 11.67, file_cluster_16: 11.886, file_cluster_8: 11.897
- **Magnitude:** 205.96 | **LOC:** 219 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.2223%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `union` (Impact: 59.3)
  * `intersect` (Impact: 45.0)
  * `invert` (Impact: 12.7)
  * `add_unseen_constraint` (Impact: 12.6)
  * `allows_any` (Impact: 9.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 63`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 28`
* *Architecture:* `api: 13`, `import: 9`
* *Defense:* `safety: 19`, `test: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.532
  * `Choke Point (Betweenness):` 0.000389 | `Ripple Effect (Closeness):` 0.044876
  * `Imports (Out-Degree: 4):` __future__, poetry.core.constraints.generic.constraint, itertools, poetry.core.constraints.generic.base_constraint, poetry.core.constraints.generic.empty_constraint, poetry.core.constraints.generic, poetry.core.constraints.generic.multi_constraint
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/factory.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.474 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.341 IQR)
- **Top Global Matches:** file_cluster_13: 11.474, file_cluster_8: 11.532, file_cluster_0: 11.704
- **Magnitude:** 201.8 | **LOC:** 1087 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.7491%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_package` (Impact: 2.2)
  * `_configure_package_dependencies` (Impact: 1.4)
  * `configure_package` (Impact: 1.3)
  * `_configure_package_metadata` (Impact: 1.3)
  * `create_dependency` (Impact: 1.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 132`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 155`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 8`, `import: 41`
* *Defense:* `safety: 31`, `doc: 6`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.93
  * `Choke Point (Betweenness):` 0.001444 | `Ripple Effect (Closeness):` 0.018692
  * `Imports (Out-Degree: 13):` poetry.core.packages.utils.utils, poetry.core.spdx.helpers, poetry.core.packages.url_dependency, poetry.core.packages.dependency_group, logging, typing, pathlib, packaging.licenses...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/version/pep440/version.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.394 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.663 IQR)
- **Top Global Matches:** file_cluster_13: 10.394, file_cluster_16: 10.428, file_cluster_0: 10.437
- **Magnitude:** 200.22 | **LOC:** 331 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.8869%), Tech Debt (98.7213%)
**Top Internal Functions/Classes:**
  * `next_prerelease` (Impact: 20.0)
  * `to_string` (Impact: 11.4)
  * `next_devrelease` (Impact: 11.0)
  * `next_postrelease` (Impact: 10.6)
  * `__post_init__` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 112`, `args: 36`, `func_start: 36`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 45`, `import: 15`
* *Defense:* `safety: 13`, `doc: 2`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.169
  * `Choke Point (Betweenness):` 0.00038 | `Ripple Effect (Closeness):` 0.018547
  * `Imports (Out-Degree: 2):` __future__, functools, dataclasses, warnings, poetry.core.version.pep440.segments, collections.abc, poetry.core.version.pep440.parser, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/tests/packages/test_package.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.643 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.872 IQR)
- **Top Global Matches:** file_cluster_8: 11.643, file_cluster_0: 11.884, file_cluster_16: 11.892
- **Magnitude:** 186.16 | **LOC:** 769 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.1214%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_all_classifiers_no_license_classifi` (Impact: 6.3)
  * `test_python_versions_are_made_precise` (Impact: 5.7)
  * `test_package_authors_valid` (Impact: 5.5)
  * `test_all_classifiers_with_license_classi` (Impact: 5.5)
  * `test_package_author_names_invalid` (Impact: 4.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 238`, `args: 48`, `func_start: 48`
* *Risk/State:* `safety_bypasses: 5`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 47`
* *Architecture:* `io: 1`, `api: 48`, `import: 21`
* *Defense:* `safety: 144`, `test: 213`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.839
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` poetry.core.spdx.helpers, poetry.core.packages.url_dependency, pytest, poetry.core.packages.dependency_group, poetry.core.packages.package, typing, poetry.core.version.exceptions, pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `poetry_core-2.3.2/src/poetry/core/masonry/builders/wheel.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.963 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.658 IQR)
- **Top Global Matches:** file_cluster_13: 9.963, file_cluster_8: 10.233, file_cluster_16: 10.25
- **Magnitude:** 183.12 | **LOC:** 563 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.0832%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_build` (Impact: 28.4)
  * `_zipfile_date_time` (Impact: 16.5)
  * `prepare_metadata` (Impact: 13.4)
    * *Intent:* # Walk the files and compress them, # sorting everything so the order is stable. for file in sorted(...
  * `_add_pth` (Impact: 12.9)
  * `tag` (Impact: 11.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 121`, `args: 30`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 17`
* *Architecture:* `io: 15`, `api: 12`, `import: 33`
* *Defense:* `safety: 12`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.146
  * `Choke Point (Betweenness):` 0.00054 | `Ripple Effect (Closeness):` 0.009346
  * `Imports (Out-Degree: 6):` sys, csv, poetry.core.masonry.builders.builder, poetry.core, poetry.core.masonry.builders.sdist, base64, hashlib, typing...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/packages/utils/link.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.448 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.406 IQR)
- **Top Global Matches:** file_cluster_0: 11.448, file_cluster_13: 11.585, file_cluster_16: 11.602
- **Magnitude:** 177.74 | **LOC:** 257 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.7252%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `metadata_hashes` (Impact: 16.0)
  * `show_url` (Impact: 14.5)
  * `hashes` (Impact: 12.5)
  * `subdirectory_fragment` (Impact: 8.9)
  * `has_metadata` (Impact: 7.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 103`, `args: 33`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `io: 1`, `api: 39`, `import: 11`
* *Defense:* `safety: 13`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.917
  * `Choke Point (Betweenness):` 0.000117 | `Ripple Effect (Closeness):` 0.041883
  * `Imports (Out-Degree: 1):` __future__, functools, posixpath, re, sys, poetry.core.packages.utils.utils, collections.abc, datetime...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/packages/utils/utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.871 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.399 IQR)
- **Top Global Matches:** file_cluster_13: 10.871, file_cluster_8: 11.408, file_cluster_16: 11.427
- **Magnitude:** 166.46 | **LOC:** 434 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.9088%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `convert_markers` (Impact: 36.3)
  * `url_to_path` (Impact: 27.8)
  * `is_python_project` (Impact: 8.7)
  * `strip_extras` (Impact: 8.5)
  * `splitext` (Impact: 7.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 95`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 30`, `dead_code: 1`
* *Architecture:* `io: 2`, `api: 21`, `import: 32`
* *Defense:* `safety: 16`, `doc: 12`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 48.73
  * `Choke Point (Betweenness):` 0.001533 | `Ripple Effect (Closeness):` 0.085609
  * `Imports (Out-Degree: 1):` __future__, functools, dataclasses, warnings, poetry.core.constraints.version, lzma, re, pathlib...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/tests/masonry/test_api.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.999 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.206 IQR)
- **Top Global Matches:** file_cluster_13: 10.999, file_cluster_8: 11.013, file_cluster_0: 11.061
- **Magnitude:** 161.42 | **LOC:** 518 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.459%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_prepare_metadata_for_build_wheel` (Impact: 13.7)
  * `test_prepare_metadata_for_build_wheel_wi` (Impact: 10.3)
  * `test_build_editable_wheel_with_metadata_` (Impact: 9.6)
  * `test_build_wheel_with_metadata_directory` (Impact: 9.4)
  * `cwd` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 114`, `args: 23`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 2`, `duplicate_logic: 3`, `orphaned_logic: 19`
* *Architecture:* `io: 10`, `api: 23`, `import: 14`
* *Defense:* `safety: 36`, `doc: 14`, `test: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.839
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, pathlib, tests.testutils, collections.abc, pytest, tempfile, zipfile, poetry.core...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `poetry_core-2.3.2/src/poetry/core/packages/dependency_group.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.757 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.862 IQR)
- **Top Global Matches:** file_cluster_13: 10.757, file_cluster_16: 10.902, file_cluster_8: 11.036
- **Magnitude:** 152.76 | **LOC:** 222 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.6165%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dependencies_for_locking` (Impact: 28.1)
  * `dependencies` (Impact: 21.9)
  * `remove_dependency` (Impact: 9.6)
  * `__eq__` (Impact: 9.2)
  * `add_dependency` (Impact: 7.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 49`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 38`
* *Architecture:* `api: 17`, `import: 11`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.432
  * `Choke Point (Betweenness):` 6.5e-05 | `Ripple Effect (Closeness):` 0.043388
  * `Imports (Out-Degree: 5):` __future__, packaging.utils, poetry.core.packages.dependency, poetry.core.packages.vcs_dependency, poetry.core.version.markers, collections, poetry.core.packages.directory_dependency, typing
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/packages/specification.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.88 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.104 IQR)
- **Top Global Matches:** file_cluster_13: 10.88, file_cluster_0: 10.897, file_cluster_16: 11.048
- **Magnitude:** 145.8 | **LOC:** 228 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0717%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `is_same_source_as` (Impact: 40.8)
  * `__hash__` (Impact: 4.2)
  * `complete_name` (Impact: 3.9)
  * `complete_pretty_name` (Impact: 3.9)
  * `with_features` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 71`, `args: 22`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 23`, `dead_code: 1`
* *Architecture:* `api: 27`, `import: 9`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.121
  * `Choke Point (Betweenness):` 0.000148 | `Ripple Effect (Closeness):` 0.042407
  * `Imports (Out-Degree: 2):` __future__, packaging.utils, copy, collections.abc, poetry.core.vcs.git, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/constraints/generic/multi_constraint.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.42 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.156 IQR)
- **Top Global Matches:** file_cluster_13: 10.42, file_cluster_17: 10.583, file_cluster_16: 10.649
- **Magnitude:** 142.7 | **LOC:** 179 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.2913%), Tech Debt (99.7268%)
**Top Internal Functions/Classes:**
  * `union` (Impact: 25.7)
  * `union` (Impact: 22.3)
  * `intersect` (Impact: 18.4)
  * `allows_any` (Impact: 12.9)
  * `intersect` (Impact: 11.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 72`, `args: 13`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`, `duplicate_logic: 4`
* *Architecture:* `api: 15`, `import: 11`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.036462
  * `Imports (Out-Degree: 2):` __future__, poetry.core.constraints.generic.constraint, itertools, poetry.core.constraints.generic.base_constraint, poetry.core.constraints.generic, typing
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/version/pep440/segments.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.48 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.349 IQR)
- **Top Global Matches:** file_cluster_16: 10.48, file_cluster_8: 10.488, file_cluster_13: 10.51
- **Magnitude:** 124.18 | **LOC:** 164 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.4969%), Tech Debt (99.9926%)
**Top Internal Functions/Classes:**
  * `__post_init__` (Impact: 18.2)
  * `from_parts` (Impact: 10.9)
  * `next_major` (Impact: 10.8)
  * `next_minor` (Impact: 10.8)
  * `next_patch` (Impact: 10.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 38`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `state_mutation: 15`, `duplicate_logic: 6`
* *Architecture:* `api: 15`, `import: 4`
* *Defense:* `safety: 2`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.016822
  * `Imports (Out-Degree: 0):` __future__, collections.abc, dataclasses, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/constraints/version/version.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.569 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.549 IQR)
- **Top Global Matches:** file_cluster_16: 9.569, file_cluster_13: 9.588, file_cluster_8: 9.749
- **Magnitude:** 119.6 | **LOC:** 183 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.707%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `union` (Impact: 9.9)
  * `__eq__` (Impact: 9.2)
  * `next_breaking` (Impact: 9.1)
  * `allows` (Impact: 7.5)
  * `intersect` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 80`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 31`, `import: 13`
* *Defense:* `safety: 6`, `doc: 2`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.296
  * `Choke Point (Betweenness):` 0.000531 | `Ripple Effect (Closeness):` 0.019499
  * `Imports (Out-Degree: 6):` __future__, dataclasses, poetry.core.constraints.version.version_range, poetry.core.constraints.version.version_range_constraint, poetry.core.constraints.version.version_constraint, poetry.core.version.pep440, poetry.core.constraints.version.empty_constraint, poetry.core.version.pep440.version...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/version/pep440/parser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.985 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.891 IQR)
- **Top Global Matches:** file_cluster_13: 8.985, file_cluster_8: 9.202, file_cluster_16: 9.221
- **Magnitude:** 118.98 | **LOC:** 85 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.4164%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 30.6)
  * `_get_postrelease` (Impact: 21.2)
  * `_get_prerelease` (Impact: 15.8)
  * `_get_devrelease` (Impact: 15.8)
  * `_get_local` (Impact: 14.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 42`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 4`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.307
  * `Choke Point (Betweenness):` 9.7e-05 | `Ripple Effect (Closeness):` 0.01375
  * `Imports (Out-Degree: 2):` __future__, poetry.core.version.exceptions, functools, re, poetry.core.version.pep440, poetry.core.version.pep440.version, packaging.version, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/tests/masonry/builders/test_builder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.395 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.783 IQR)
- **Top Global Matches:** file_cluster_8: 10.395, file_cluster_13: 10.678, file_cluster_0: 10.686
- **Magnitude:** 116.6 | **LOC:** 412 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.2822%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_metadata_license_type_file` (Impact: 32.6)
  * `test_get_metadata_content` (Impact: 15.4)
  * `test_invalid_script_files_definition` (Impact: 4.1)
  * `test_missing_script_files_throws_error` (Impact: 4.0)
  * `test_building_not_possible_in_non_packag` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 84`, `args: 18`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 3`, `orphaned_logic: 18`
* *Architecture:* `io: 4`, `api: 18`, `import: 10`
* *Defense:* `safety: 42`, `test: 81`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.839
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, pathlib, sys, pytest, pytest_mock, poetry.core.masonry.builders.builder, email.parser, poetry.core.factory...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### 🚨 Severe Anti-Patterns (Language Convention Violations)
- `poetry_core-2.3.2/tests/masonry/builders/fixtures/case_sensitive_exclusions/my_package/__init__.py` (PYTHON) | **Drift Ratio: 1.6x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.628 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.821 IQR)
- `poetry_core-2.3.2/tests/masonry/builders/fixtures/complete/my_package/__init__.py` (PYTHON) | **Drift Ratio: 1.6x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.628 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.821 IQR)
- `poetry_core-2.3.2/tests/masonry/builders/fixtures/complete_dynamic/my_package/__init__.py` (PYTHON) | **Drift Ratio: 1.6x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.628 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.821 IQR)
- `poetry_core-2.3.2/tests/masonry/builders/fixtures/complete_new/my_package/__init__.py` (PYTHON) | **Drift Ratio: 1.6x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.628 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.821 IQR)
- `poetry_core-2.3.2/tests/masonry/builders/fixtures/excluded_subpackage/example/__init__.py` (PYTHON) | **Drift Ratio: 1.6x**
  * **Global Archetype:** `file_cluster_8` (Drift: 3.628 IQR)
  * **Local Reality:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.821 IQR)

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `poetry_core-2.3.2/tests/version/pep440/test_segments.py` (PYTHON) | Magnitude: 49.2 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 85, test: 48, structural_boundaries: 43, safety: 21
- `poetry_core-2.3.2/tests/packages/utils/test_utils_urls.py` (PYTHON) | Magnitude: 35.26 | Delta: **0.119 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 33, test: 29, safety: 13
- `poetry_core-2.3.2/src/poetry/core/packages/utils/link.py` (PYTHON) | Magnitude: 177.74 | Delta: **0.137 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 165, structural_boundaries: 103, branch: 46, encapsulation: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `poetry_core-2.3.2/src/poetry/core/masonry/utils/package_include.py` (PYTHON) | Magnitude: 87.16 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 63, state_mutation: 30, structural_boundaries: 28, encapsulation: 25
- `poetry_core-2.3.2/tests/integration/test_pep517.py` (PYTHON) | Magnitude: 17.44 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 32, test: 18, explicit_casts: 10
- `poetry_core-2.3.2/src/poetry/core/constraints/version/parser.py` (PYTHON) | Magnitude: 27.48 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 182, structural_boundaries: 78, branch: 55, encapsulation: 21
- `poetry_core-2.3.2/tests/masonry/test_api.py` (PYTHON) | Magnitude: 161.42 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 264, structural_boundaries: 114, test: 66, branch: 41
- `poetry_core-2.3.2/src/poetry/core/packages/specification.py` (PYTHON) | Magnitude: 145.8 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 143, structural_boundaries: 71, encapsulation: 50, branch: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `poetry_core-2.3.2/src/poetry/core/version/pep440/segments.py` (PYTHON) | Magnitude: 124.18 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 111, branch: 41, structural_boundaries: 38, test: 16
- `poetry_core-2.3.2/src/poetry/core/constraints/version/version.py` (PYTHON) | Magnitude: 119.6 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 123, structural_boundaries: 80, api: 31, branch: 27
- `poetry_core-2.3.2/tests/spdx/test_license.py` (PYTHON) | Magnitude: 31.16 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 20, test: 16, args: 8
- `poetry_core-2.3.2/src/poetry/core/packages/vcs_dependency.py` (PYTHON) | Magnitude: 81.5 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 100, structural_boundaries: 39, encapsulation: 35, branch: 18
- `poetry_core-2.3.2/tests/json/test_poetry_schema.py` (PYTHON) | Magnitude: 25.86 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 29, test: 25, generics: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `poetry_core-2.3.2/tests/masonry/builders/test_wheel.py` (PYTHON) | Magnitude: 220.84 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 359, structural_boundaries: 202, test: 153, safety: 108
- `poetry_core-2.3.2/src/poetry/core/constraints/version/__init__.py` (PYTHON) | Magnitude: 16.46 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 20, import: 10, indent_spaces: 10, encapsulation: 2
- `poetry_core-2.3.2/tests/packages/test_main.py` (PYTHON) | Magnitude: 99.4 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 216, structural_boundaries: 142, test: 132, safety: 102
- `poetry_core-2.3.2/tests/packages/utils/test_utils_link.py` (PYTHON) | Magnitude: 39.56 | Delta: **0.098 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 113, structural_boundaries: 66, test: 56, safety: 34
- `poetry_core-2.3.2/src/poetry/core/vcs/git.py` (PYTHON) | Magnitude: 103.42 | Delta: **0.113 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 212, structural_boundaries: 51, branch: 41, encapsulation: 30

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `poetry_core-2.3.2/src/poetry/core/packages/dependency.py` -> **Severity: 0.377** (Bridge: 0.0038 * Flux: 99.663%)
- `poetry_core-2.3.2/src/poetry/core/version/markers.py` -> **Severity: 0.369** (Bridge: 0.0038 * Flux: 95.9723%)
- `poetry_core-2.3.2/src/poetry/core/constraints/generic/parser.py` -> **Severity: 0.278** (Bridge: 0.0028 * Flux: 99.9043%)
- `poetry_core-2.3.2/src/poetry/core/packages/utils/utils.py` -> **Severity: 0.15** (Bridge: 0.0015 * Flux: 97.9288%)
- `poetry_core-2.3.2/src/poetry/core/factory.py` -> **Severity: 0.143** (Bridge: 0.0014 * Flux: 99.1553%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `poetry_core-2.3.2/src/poetry/core/constraints/version/exceptions.py` -> **Severity: 5.0** (Embedded: 0.0625 * Error Risk: 80.0%)
- `poetry_core-2.3.2/src/poetry/core/packages/utils/utils.py` -> **Severity: 4.559** (Embedded: 0.0856 * Error Risk: 53.2548%)
- `poetry_core-2.3.2/src/poetry/core/packages/dependency.py` -> **Severity: 4.386** (Embedded: 0.0624 * Error Risk: 70.3296%)
- `poetry_core-2.3.2/src/poetry/core/version/parser.py` -> **Severity: 4.257** (Embedded: 0.0502 * Error Risk: 84.7391%)
- `poetry_core-2.3.2/src/poetry/core/constraints/generic/parser.py` -> **Severity: 4.168** (Embedded: 0.053 * Error Risk: 78.5756%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `poetry_core-2.3.2/src/poetry/core/version/markers.py` -> **Severity: 3981.852** (Blast Radius: 51.513 * Doc Risk: 77.298%)
- `poetry_core-2.3.2/src/poetry/core/packages/utils/utils.py` -> **Severity: 2389.48** (Blast Radius: 48.73 * Doc Risk: 49.0351%)
- `poetry_core-2.3.2/src/poetry/core/constraints/version/version.py` -> **Severity: 2324.261** (Blast Radius: 23.296 * Doc Risk: 99.7708%)
- `poetry_core-2.3.2/src/poetry/core/constraints/version/version_constraint.py` -> **Severity: 1968.205** (Blast Radius: 19.685 * Doc Risk: 99.985%)
- `poetry_core-2.3.2/src/poetry/core/packages/dependency.py` -> **Severity: 1952.124** (Blast Radius: 23.143 * Doc Risk: 84.3505%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
