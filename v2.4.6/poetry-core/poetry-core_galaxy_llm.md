# ARCHITECTURAL_BRIEF: poetry-core
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/poetry-core` |
| **Timestamp** | `2026-08-03T21:23:17.670556+00:00` |
| **Scan Duration** | `0.96s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 267 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 100.0 | 12.9 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 6.7 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 8.7 | 0.0 | 0.0 |
| API Exposure | 0.0 | 13.4 | 2.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 23.0 | 0.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 12.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 11.3 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 44.3 | 6.7 | 6.7 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 19.9 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 21.7 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 18.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `to_pep_508` (@ `poetry_core-2.3.2/src/poetry/core/packages/dependency.py`) -> Impact: **401.6** | LOC: 206
- `union` (@ `poetry_core-2.3.2/src/poetry/core/constraints/generic/union_constraint.py`) -> Impact: **391.8** | LOC: 77
- `test_validate_strict_fails_strict_and_no` (@ `poetry_core-2.3.2/tests/test_factory.py`) -> Impact: **375.2** | LOC: 853
- `difference` (@ `poetry_core-2.3.2/src/poetry/core/constraints/version/version_range.py`) -> Impact: **295.6** | LOC: 93
- `difference` (@ `poetry_core-2.3.2/src/poetry/core/constraints/version/version_union.py`) -> Impact: **258.7** | LOC: 82
- `intersect` (@ `poetry_core-2.3.2/src/poetry/core/constraints/generic/union_constraint.py`) -> Impact: **252.9** | LOC: 69
- `marker` (@ `poetry_core-2.3.2/src/poetry/core/packages/dependency.py`) -> Impact: **208.2** | LOC: 42
- `intersect` (@ `poetry_core-2.3.2/src/poetry/core/constraints/version/version_range.py`) -> Impact: **200.7** | LOC: 65
- `invert` (@ `poetry_core-2.3.2/src/poetry/core/version/markers.py`) -> Impact: **189.5** | LOC: 48
- `dependencies_for_locking` (@ `poetry_core-2.3.2/src/poetry/core/packages/dependency_group.py`) -> Impact: **184.0** | LOC: 42

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `union` (@ `poetry_core-2.3.2/src/poetry/core/constraints/generic/constraint.py`) -> **O(2^N) [Recursive]**
- `union` (@ `poetry_core-2.3.2/src/poetry/core/constraints/generic/union_constraint.py`) -> **O(2^N) [Recursive]**
- `difference` (@ `poetry_core-2.3.2/src/poetry/core/constraints/version/version_union.py`) -> **O(2^N) [Recursive]**
- `marker` (@ `poetry_core-2.3.2/src/poetry/core/packages/dependency.py`) -> **O(2^N) [Recursive]**
- `dependencies_for_locking` (@ `poetry_core-2.3.2/src/poetry/core/packages/dependency_group.py`) -> **O(2^N) [Recursive]**
- `allows_all` (@ `poetry_core-2.3.2/src/poetry/core/constraints/generic/constraint.py`) -> **O(2^N) [Recursive]**
- `union` (@ `poetry_core-2.3.2/src/poetry/core/constraints/generic/multi_constraint.py`) -> **O(2^N) [Recursive]**
- `intersect` (@ `poetry_core-2.3.2/src/poetry/core/constraints/generic/multi_constraint.py`) -> **O(2^N) [Recursive]**
- `intersect` (@ `poetry_core-2.3.2/src/poetry/core/constraints/generic/union_constraint.py`) -> **O(2^N) [Recursive]**
- `difference` (@ `poetry_core-2.3.2/src/poetry/core/constraints/version/version_range.py`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `test_dependency_from_pep_508_with_platfo` (@ `poetry_core-2.3.2/tests/packages/test_main.py`) -> DB Complexity: **36**
- `test_validate_strict_fails_strict_and_no` (@ `poetry_core-2.3.2/tests/test_factory.py`) -> DB Complexity: **21**
- `test_create_poetry` (@ `poetry_core-2.3.2/tests/test_factory.py`) -> DB Complexity: **21**
- `to_pep_508` (@ `poetry_core-2.3.2/src/poetry/core/packages/dependency.py`) -> DB Complexity: **15**
- `_build` (@ `poetry_core-2.3.2/src/poetry/core/masonry/builders/wheel.py`) -> DB Complexity: **12**
- `test_remove_dependency_does_not_leak_inc` (@ `poetry_core-2.3.2/tests/packages/test_dependency_group.py`) -> DB Complexity: **12**
  * *Intent:* """Removing a dep must not copy included-group deps into _dependencies."""
- `test_dependency_from_pep_508_with_extras` (@ `poetry_core-2.3.2/tests/packages/test_main.py`) -> DB Complexity: **12**
- `test_dependency_from_pep_508_with_python` (@ `poetry_core-2.3.2/tests/packages/test_main.py`) -> DB Complexity: **12**
- `prepare_metadata` (@ `poetry_core-2.3.2/src/poetry/core/masonry/builders/wheel.py`) -> DB Complexity: **9**
  * *Intent:* # Walk the files and compress them, # sorting everything so the order is stable. for file in sorted(to_add, key=lambda x: x.path): self._add_file(whee...
- `test_prepare_metadata_for_build_wheel` (@ `poetry_core-2.3.2/tests/masonry/test_api.py`) -> DB Complexity: **9**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `poetry_core-2.3.2/src/poetry/core/packages` | 11 | 2766.36 | 63.96% | 26.12% |
| `poetry_core-2.3.2/src/poetry/core/constraints/version` | 11 | 2413.84 | 23.52% | 0.0% |
| `poetry_core-2.3.2/src/poetry/core/constraints/generic` | 8 | 2401.3 | 32.51% | 24.94% |
| `poetry_core-2.3.2/src/poetry/core/version` | 6 | 2140.54 | 32.09% | 16.67% |
| `poetry_core-2.3.2/src/poetry/core/masonry/builders` | 3 | 986.28 | 24.4% | 12.2% |
| `poetry_core-2.3.2/src/poetry/core/version/pep440` | 4 | 932.2 | 47.7% | 49.68% |
| `poetry_core-2.3.2/tests` | 4 | 907.78 | 4.08% | 0.0% |
| `poetry_core-2.3.2/tests/packages` | 10 | 788.96 | 3.36% | 0.0% |
| `poetry_core-2.3.2/tests/version` | 3 | 695.76 | 5.45% | 0.0% |
| `poetry_core-2.3.2/tests/masonry/builders` | 4 | 628.28 | 3.75% | 0.0% |

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

### Exploit Generation Surface
- `poetry_core-2.3.2/src/poetry/core/constraints/generic/constraint.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/constraints/generic/multi_constraint.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/constraints/generic/union_constraint.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/constraints/version/version.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/constraints/version/version_constraint.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `poetry_core-2.3.2/tests/packages/test_directory_dependency.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/tests/packages/test_file_dependency.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `poetry_core-2.3.2/src/poetry/core/constraints/generic/constraint.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/constraints/generic/multi_constraint.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/constraints/generic/union_constraint.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/constraints/version/version.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/constraints/version/version_range.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `798` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `poetry_core-2.3.2/src/poetry/core/packages/project_package.py` (PYTHON) -> Cumulative Risk: **910.75**
- **Archetype:** `file_cluster_13` (Distance: 10.763 IQR)
- **Magnitude:** 112.94 | **LOC:** 126 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `python_versions` (Impact: 21.8), `all_classifiers` (Impact: 14.1), `to_dependency` (Impact: 5.5)

### 2. `poetry_core-2.3.2/src/poetry/core/version/markers.py` (PYTHON) -> Cumulative Risk: **829.03**
- **Archetype:** `file_cluster_13` (Distance: 12.251 IQR)
- **Magnitude:** 1887.44 | **LOC:** 1396 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `invert` (Impact: 189.5), `union_simplify` (Impact: 129.9), `intersect_simplify` (Impact: 129.9)

### 3. `poetry_core-2.3.2/src/poetry/core/packages/dependency.py` (PYTHON) -> Cumulative Risk: **822.14**
- **Archetype:** `file_cluster_13` (Distance: 11.092 IQR)
- **Magnitude:** 920.48 | **LOC:** 546 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.8209%)
- **Heaviest Functions:** `to_pep_508` (Impact: 401.6), `marker` (Impact: 208.2), `base_pep_508_name` (Impact: 42.9)

### 4. `poetry_core-2.3.2/src/poetry/core/masonry/utils/package_include.py` (PYTHON) -> Cumulative Risk: **809.89**
- **Archetype:** `file_cluster_13` (Distance: 11.812 IQR)
- **Magnitude:** 131.16 | **LOC:** 99 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `check_elements` (Impact: 40.4), `is_stub_only` (Impact: 21.2), `refresh` (Impact: 5.4)

### 5. `poetry_core-2.3.2/src/poetry/core/constraints/generic/constraint.py` (PYTHON) -> Cumulative Risk: **806.46**
- **Archetype:** `file_cluster_13` (Distance: 11.582 IQR)
- **Magnitude:** 755.92 | **LOC:** 259 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `union` (Impact: 159.3), `allows_all` (Impact: 126.0), `allows_any` (Impact: 105.2)

### 6. `poetry_core-2.3.2/src/poetry/core/packages/package.py` (PYTHON) -> Cumulative Risk: **805.83**
- **Archetype:** `file_cluster_13` (Distance: 11.391 IQR)
- **Magnitude:** 703.24 | **LOC:** 681 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9975%)
- **Heaviest Functions:** `all_classifiers` (Impact: 70.2), `license` (Impact: 52.6), `__repr__` (Impact: 43.0)

### 7. `poetry_core-2.3.2/src/poetry/core/version/pep440/segments.py` (PYTHON) -> Cumulative Risk: **796.5**
- **Archetype:** `file_cluster_16` (Distance: 10.48 IQR)
- **Magnitude:** 216.98 | **LOC:** 164 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9976%)
- **Heaviest Functions:** `__post_init__` (Impact: 44.2), `from_parts` (Impact: 21.3), `next_major` (Impact: 21.2)

### 8. `poetry_core-2.3.2/src/poetry/core/poetry.py` (PYTHON) -> Cumulative Risk: **785.99**
- **Archetype:** `file_cluster_13` (Distance: 10.608 IQR)
- **Magnitude:** 92.02 | **LOC:** 95 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9974%)
- **Heaviest Functions:** `build_system_dependencies` (Impact: 50.1), `get_project_config` (Impact: 3.1), `is_package_mode` (Impact: 2.8)

### 9. `poetry_core-2.3.2/src/poetry/core/vcs/git.py` (PYTHON) -> Cumulative Risk: **766.33**
- **Archetype:** `file_cluster_8` (Distance: 10.141 IQR)
- **Magnitude:** 178.42 | **LOC:** 296 | **CtrlFlow:** 44.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9999%), Documentation (96.2052%)
- **Heaviest Functions:** `normalize_url` (Impact: 90.5), `__init__` (Impact: 26.7), `get` (Impact: 6.1)

### 10. `poetry_core-2.3.2/src/poetry/core/packages/dependency_group.py` (PYTHON) -> Cumulative Risk: **762.58**
- **Archetype:** `file_cluster_13` (Distance: 10.757 IQR)
- **Magnitude:** 434.36 | **LOC:** 222 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9985%)
- **Heaviest Functions:** `dependencies_for_locking` (Impact: 184.0), `dependencies` (Impact: 105.0), `remove_dependency` (Impact: 22.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `poetry_core-2.3.2/src/poetry/core/version/markers.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.251 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.686 IQR)
- **Top Global Matches:** file_cluster_13: 12.251, file_cluster_0: 12.347, file_cluster_16: 12.369
- **Magnitude:** 1887.44 | **LOC:** 1396 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (61.6427%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `invert` (Impact: 189.5 | O(2^N) | DB: 8)
  * `union_simplify` (Impact: 129.9 | O(N^6))
  * `intersect_simplify` (Impact: 129.9 | O(N^6))
  * `of` (Impact: 124.6 | O(N^6) | DB: 1)
  * `of` (Impact: 112.1 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `structural_boundaries: 409`, `args: 120`, `func_start: 118`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 135`, `dead_code: 2`, `duplicate_logic: 101`
* *Architecture:* `io: 2`, `api: 93`, `concurrency: 2`, `import: 46`
* *Defense:* `safety: 80`, `doc: 20`, `test: 7`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 51.513
  * `Choke Point (Betweenness):` 0.003845 | `Ripple Effect (Closeness):` 0.071651
  * `Imports (Out-Degree: 4):` functools, poetry.core.constraints.generic.parser, collections.abc, collections, packaging.utils, poetry.core.constraints.version, lark, poetry.core.packages.utils.utils...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/constraints/version/version_range.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.937 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.186 IQR)
- **Top Global Matches:** file_cluster_13: 10.937, file_cluster_8: 11.039, file_cluster_16: 11.129
- **Magnitude:** 1082.86 | **LOC:** 473 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (44.3191%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `difference` (Impact: 295.6 | O(2^N) | DB: 3)
  * `intersect` (Impact: 200.7 | O(2^N))
  * `union` (Impact: 90.9 | O(N^5) | DB: 2)
  * `allows_any` (Impact: 87.8 | O(2^N))
  * `allows` (Impact: 80.2 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 152`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 31`
* *Architecture:* `api: 28`, `import: 16`
* *Defense:* `safety: 25`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.207
  * `Choke Point (Betweenness):` 0.000278 | `Ripple Effect (Closeness):` 0.021937
  * `Imports (Out-Degree: 5):` functools, contextlib, poetry.core.constraints.version.version_union, typing, poetry.core.constraints.version.version, poetry.core.constraints.version.version_constraint, poetry.core.constraints.version.empty_constraint, __future__...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/packages/dependency.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.092 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.524 IQR)
- **Top Global Matches:** file_cluster_13: 11.092, file_cluster_0: 11.478, file_cluster_16: 11.591
- **Magnitude:** 920.48 | **LOC:** 546 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (72.8499%), Tech Debt (93.7206%)
**Top Internal Functions/Classes:**
  * `to_pep_508` (Impact: 401.6 | O(N^6) | DB: 15)
  * `marker` (Impact: 208.2 | O(2^N) | DB: 7)
  * `base_pep_508_name` (Impact: 42.9 | O(N^5))
  * `__eq__` (Impact: 28.3 | O(2^N) | DB: 1)
  * `constraint` (Impact: 21.1 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 160`, `args: 35`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 80`, `dead_code: 1`, `duplicate_logic: 8`
* *Architecture:* `io: 4`, `api: 38`, `import: 46`
* *Defense:* `safety: 5`, `doc: 10`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.143
  * `Choke Point (Betweenness):` 0.003784 | `Ripple Effect (Closeness):` 0.06237
  * `Imports (Out-Degree: 12):` poetry.core.packages.utils.link, poetry.core.packages.dependency_group, re, poetry.core.packages.vcs_dependency, poetry.core.packages.directory_dependency, poetry.core.version.markers, contextlib, poetry.core.packages.file_dependency...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/tests/test_factory.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.996 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.272 IQR)
- **Top Global Matches:** file_cluster_8: 11.996, file_cluster_16: 12.116, file_cluster_0: 12.159
- **Magnitude:** 875.72 | **LOC:** 2109 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (2.7775%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_validate_strict_fails_strict_and_no` (Impact: 375.2 | O(N^5) | DB: 21)
  * `test_create_poetry` (Impact: 119.2 | O(N^3) | DB: 21)
  * `complete_legacy_duplicate_warnings` (Impact: 80.0 | O(N^3))
  * `test_create_poetry_with_groups` (Impact: 31.7 | O(N^4) | DB: 1)
  * `complete_legacy_warnings` (Impact: 30.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 329`, `args: 68`, `func_start: 64`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 27`, `orphaned_logic: 26`
* *Architecture:* `io: 22`, `api: 64`, `import: 21`
* *Defense:* `safety: 190`, `doc: 82`, `test: 302`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.839
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` shutil, poetry.core.version.markers, poetry.core.packages.dependency, poetry.core.factory, collections, packaging.utils, poetry.core.constraints.version, poetry.core.packages.dependency_group...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `poetry_core-2.3.2/src/poetry/core/constraints/generic/union_constraint.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.667 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.35 IQR)
- **Top Global Matches:** file_cluster_13: 11.667, file_cluster_16: 11.883, file_cluster_8: 11.894
- **Magnitude:** 859.96 | **LOC:** 219 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (87.0665%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `union` (Impact: 391.8 | O(2^N) | DB: 7)
  * `intersect` (Impact: 252.9 | O(2^N) | DB: 1)
  * `invert` (Impact: 61.2 | O(2^N))
  * `allows_any` (Impact: 43.8 | O(2^N))
  * `allows_all` (Impact: 43.7 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 63`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 28`
* *Architecture:* `api: 13`, `import: 9`
* *Defense:* `safety: 19`, `test: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.532
  * `Choke Point (Betweenness):` 0.000389 | `Ripple Effect (Closeness):` 0.044876
  * `Imports (Out-Degree: 4):` poetry.core.constraints.generic.base_constraint, itertools, poetry.core.constraints.generic.multi_constraint, __future__, poetry.core.constraints.generic.constraint, poetry.core.constraints.generic.empty_constraint, poetry.core.constraints.generic
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/constraints/generic/constraint.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.582 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.661 IQR)
- **Top Global Matches:** file_cluster_13: 11.582, file_cluster_16: 11.847, file_cluster_8: 11.962
- **Magnitude:** 755.92 | **LOC:** 259 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (64.7709%), Tech Debt (99.7679%)
**Top Internal Functions/Classes:**
  * `union` (Impact: 159.3 | O(2^N) | DB: 1)
  * `allows_all` (Impact: 126.0 | O(2^N) | DB: 3)
  * `allows_any` (Impact: 105.2 | O(2^N) | DB: 3)
  * `intersect` (Impact: 61.6 | O(2^N))
  * `allows` (Impact: 52.5 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 104`, `args: 20`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `state_mutation: 39`, `duplicate_logic: 6`
* *Architecture:* `api: 21`, `import: 15`
* *Defense:* `safety: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.056
  * `Choke Point (Betweenness):` 0.00048 | `Ripple Effect (Closeness):` 0.045577
  * `Imports (Out-Degree: 5):` poetry.core.constraints.generic.union_constraint, poetry.core.constraints.generic.base_constraint, poetry.core.constraints.generic.any_constraint, typing, operator, poetry.core.constraints.generic.multi_constraint, __future__, collections.abc...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/packages/package.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.391 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.833 IQR)
- **Top Global Matches:** file_cluster_13: 11.391, file_cluster_0: 11.594, file_cluster_16: 11.68
- **Magnitude:** 703.24 | **LOC:** 681 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (58.9593%), Tech Debt (93.6355%)
**Top Internal Functions/Classes:**
  * `all_classifiers` (Impact: 70.2 | O(N^5) | DB: 6)
  * `license` (Impact: 52.6 | O(2^N) | DB: 2)
  * `__repr__` (Impact: 43.0 | O(N^5) | DB: 8)
    * *Intent:* # The dependency specifies a source: this package matches if and only if it is
  * `to_dependency` (Impact: 42.4 | O(N^4) | DB: 7)
  * `full_pretty_version` (Impact: 28.6 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 189`, `args: 47`, `func_start: 46`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 79`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `io: 2`, `api: 59`, `import: 40`
* *Defense:* `safety: 13`, `doc: 16`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.613
  * `Choke Point (Betweenness):` 0.00056 | `Ripple Effect (Closeness):` 0.016983
  * `Imports (Out-Degree: 14):` poetry.core.packages.dependency_group, poetry.core.version.exceptions, poetry.core.packages.vcs_dependency, poetry.core.packages.directory_dependency, poetry.core.version.markers, poetry.core.spdx.license, poetry.core.packages.file_dependency, poetry.core.packages.dependency...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/tests/version/test_markers.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.601 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.686 IQR)
- **Top Global Matches:** file_cluster_8: 10.601, file_cluster_16: 11.238, file_cluster_7: 11.276
- **Magnitude:** 668.0 | **LOC:** 2764 | **CtrlFlow:** 77.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.2525%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_marker_union_union_duplicates` (Impact: 35.7 | O(N^3))
  * `test_marker_union_intersect_multi_marker` (Impact: 24.4 | O(N^2))
  * `test_multi_marker_union_with_union` (Impact: 24.2 | O(N^2))
  * `test_marker_union_intersect_marker_union` (Impact: 24.1 | O(N^2))
  * `test_multi_marker_intersect_multi_with_o` (Impact: 21.5 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 867`, `structural_boundaries: 255`, `args: 88`, `func_start: 88`
* *Risk/State:* `duplicate_logic: 8`, `orphaned_logic: 52`
* *Architecture:* `io: 4`, `api: 88`, `import: 20`
* *Defense:* `safety: 131`, `doc: 12`, `test: 239`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.839
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` poetry.core.version.markers, poetry.core.constraints.version, typing, pytest, os, __future__, poetry.core.constraints.generic
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `poetry_core-2.3.2/src/poetry/core/constraints/version/version_union.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.224 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.419 IQR)
- **Top Global Matches:** file_cluster_13: 11.224, file_cluster_16: 11.39, file_cluster_0: 11.46
- **Magnitude:** 661.56 | **LOC:** 325 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (49.6052%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `difference` (Impact: 258.7 | O(2^N) | DB: 4)
  * `of` (Impact: 67.3 | O(N^4) | DB: 2)
  * `intersect` (Impact: 53.0 | O(2^N) | DB: 1)
  * `allows_any` (Impact: 52.8 | O(2^N))
  * `allows_all` (Impact: 44.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 114`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 25`
* *Architecture:* `api: 23`, `import: 15`
* *Defense:* `safety: 21`, `doc: 4`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.97
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.017549
  * `Imports (Out-Degree: 5):` functools, typing, poetry.core.constraints.version.version, poetry.core.constraints.version.version_constraint, operator, poetry.core.constraints.version.empty_constraint, __future__, poetry.core.constraints.version.version_range_constraint...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/constraints/generic/multi_constraint.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.42 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.156 IQR)
- **Top Global Matches:** file_cluster_13: 10.42, file_cluster_17: 10.583, file_cluster_16: 10.649
- **Magnitude:** 562.8 | **LOC:** 179 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (34.2913%), Tech Debt (99.7268%)
**Top Internal Functions/Classes:**
  * `union` (Impact: 126.2 | O(2^N))
  * `union` (Impact: 122.7 | O(2^N))
  * `intersect` (Impact: 87.7 | O(2^N))
  * `intersect` (Impact: 63.0 | O(2^N))
  * `allows_any` (Impact: 61.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 72`, `args: 13`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`, `duplicate_logic: 4`
* *Architecture:* `api: 15`, `import: 11`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.082
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.036462
  * `Imports (Out-Degree: 2):` poetry.core.constraints.generic.base_constraint, typing, itertools, __future__, poetry.core.constraints.generic.constraint, poetry.core.constraints.generic
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/masonry/builders/builder.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.181 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.735 IQR)
- **Top Global Matches:** file_cluster_13: 11.181, file_cluster_16: 11.261, file_cluster_8: 11.452
- **Magnitude:** 553.04 | **LOC:** 391 | **CtrlFlow:** 53.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (50.1241%), Tech Debt (36.5947%)
**Top Internal Functions/Classes:**
  * `find_files_to_add` (Impact: 131.3 | O(N^6) | DB: 2)
  * `find_excluded_files` (Impact: 84.9 | O(N^5) | DB: 2)
  * `get_metadata_content` (Impact: 72.5 | O(N^4))
  * `convert_script_files` (Impact: 49.9 | O(N^6) | DB: 1)
  * `is_excluded` (Impact: 31.1 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 75`, `args: 23`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 53`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 26`, `import: 14`
* *Defense:* `safety: 6`, `doc: 12`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.948
  * `Choke Point (Betweenness):` 0.000183 | `Ripple Effect (Closeness):` 0.009735
  * `Imports (Out-Degree: 4):` sys, functools, poetry.core.masonry.metadata, poetry.core.masonry.utils.module, typing, logging, textwrap, poetry.core.masonry.utils.package_include...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/version/pep440/version.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.394 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.663 IQR)
- **Top Global Matches:** file_cluster_13: 10.394, file_cluster_16: 10.428, file_cluster_0: 10.437
- **Magnitude:** 472.52 | **LOC:** 331 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (40.8869%), Tech Debt (98.7213%)
**Top Internal Functions/Classes:**
  * `next_prerelease` (Impact: 96.2 | O(2^N))
  * `next_devrelease` (Impact: 51.0 | O(2^N))
  * `to_string` (Impact: 42.6 | O(2^N))
  * `next_minor` (Impact: 24.4 | O(2^N))
  * `next_patch` (Impact: 24.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 112`, `args: 36`, `func_start: 36`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 45`, `import: 15`
* *Defense:* `safety: 13`, `doc: 2`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.169
  * `Choke Point (Betweenness):` 0.00038 | `Ripple Effect (Closeness):` 0.018547
  * `Imports (Out-Degree: 2):` dataclasses, warnings, functools, poetry.core.version.pep440.parser, poetry.core.version.pep440.segments, typing, __future__, collections.abc
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/packages/dependency_group.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.757 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.862 IQR)
- **Top Global Matches:** file_cluster_13: 10.757, file_cluster_16: 10.902, file_cluster_8: 11.036
- **Magnitude:** 434.36 | **LOC:** 222 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (83.6165%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dependencies_for_locking` (Impact: 184.0 | O(2^N) | DB: 4)
  * `dependencies` (Impact: 105.0 | O(2^N))
  * `remove_dependency` (Impact: 22.6 | O(N^4) | DB: 4)
  * `__eq__` (Impact: 17.8 | O(N^3) | DB: 2)
  * `add_dependency` (Impact: 14.1 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 49`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 38`
* *Architecture:* `api: 17`, `import: 11`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.432
  * `Choke Point (Betweenness):` 6.5e-05 | `Ripple Effect (Closeness):` 0.043388
  * `Imports (Out-Degree: 5):` poetry.core.version.markers, poetry.core.packages.dependency, packaging.utils, collections, typing, __future__, poetry.core.packages.vcs_dependency, poetry.core.packages.directory_dependency
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/masonry/builders/wheel.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.963 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.658 IQR)
- **Top Global Matches:** file_cluster_13: 9.963, file_cluster_8: 10.233, file_cluster_16: 10.25
- **Magnitude:** 422.72 | **LOC:** 563 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (18.0832%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_build` (Impact: 93.3 | O(N^6) | DB: 12)
  * `tag` (Impact: 52.6 | O(2^N) | DB: 3)
  * `_zipfile_date_time` (Impact: 44.2 | O(N^5) | DB: 3)
  * `prepare_metadata` (Impact: 31.6 | O(N^4) | DB: 9)
    * *Intent:* # Walk the files and compress them, # sorting everything so the order is stable. for file in sorted(...
  * `_add_pth` (Impact: 31.1 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 121`, `args: 30`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 17`
* *Architecture:* `io: 15`, `api: 12`, `import: 33`
* *Defense:* `safety: 12`, `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.146
  * `Choke Point (Betweenness):` 0.00054 | `Ripple Effect (Closeness):` 0.009346
  * `Imports (Out-Degree: 6):` hashlib, tempfile, base64, poetry.core.masonry.builders.builder, contextlib, sys, functools, poetry.core.masonry.utils.package_include...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/packages/utils/utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.877 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.399 IQR)
- **Top Global Matches:** file_cluster_13: 10.877, file_cluster_8: 11.414, file_cluster_16: 11.433
- **Magnitude:** 299.06 | **LOC:** 434 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (38.5311%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `convert_markers` (Impact: 104.3 | O(N^5) | DB: 2)
  * `url_to_path` (Impact: 79.8 | O(N^5) | DB: 3)
  * `is_python_project` (Impact: 12.7 | O(N^2))
  * `strip_extras` (Impact: 12.5 | O(N^2))
  * `splitext` (Impact: 11.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 95`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 30`, `dead_code: 1`
* *Architecture:* `io: 2`, `api: 21`, `import: 32`
* *Defense:* `safety: 16`, `doc: 12`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 48.73
  * `Choke Point (Betweenness):` 0.001533 | `Ripple Effect (Closeness):` 0.085609
  * `Imports (Out-Degree: 1):` dataclasses, warnings, poetry.core.version.markers, sys, functools, contextlib, poetry.core.constraints.version, typing...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/packages/utils/link.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.448 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.406 IQR)
- **Top Global Matches:** file_cluster_0: 11.448, file_cluster_13: 11.585, file_cluster_16: 11.602
- **Magnitude:** 295.84 | **LOC:** 257 | **CtrlFlow:** 30.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (29.7252%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `metadata_hashes` (Impact: 47.2 | O(N^5))
  * `show_url` (Impact: 32.7 | O(N^4) | DB: 6)
  * `hashes` (Impact: 24.6 | O(N^3))
  * `subdirectory_fragment` (Impact: 17.6 | O(N^3))
  * `has_metadata` (Impact: 14.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 103`, `args: 33`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `io: 1`, `api: 39`, `import: 11`
* *Defense:* `safety: 13`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.917
  * `Choke Point (Betweenness):` 0.000117 | `Ripple Effect (Closeness):` 0.041883
  * `Imports (Out-Degree: 1):` datetime, sys, functools, poetry.core.packages.utils.utils, typing, re, urllib.parse, posixpath...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/tests/masonry/builders/test_wheel.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.958 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.233 IQR)
- **Top Global Matches:** file_cluster_8: 11.958, file_cluster_13: 11.984, file_cluster_16: 12.013
- **Magnitude:** 288.34 | **LOC:** 624 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (3.0306%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `clear_samples_build` (Impact: 17.7 | O(N^3))
  * `test_wheel_package_target_dir` (Impact: 16.4 | O(N^2))
  * `test_tag` (Impact: 13.7 | O(N^2) | DB: 3)
  * `clear_samples_dist` (Impact: 10.6 | O(N^3))
  * `test_wheel_include_formats` (Impact: 9.5 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 202`, `args: 35`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 3`, `fragile_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `io: 3`, `api: 64`, `import: 19`
* *Defense:* `safety: 108`, `doc: 12`, `test: 153`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.361
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003115
  * `Imports (Out-Degree: 2):` shutil, poetry.core.factory, importlib.machinery, typing, logging, re, tests.masonry.builders.test_sdist, pytest...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/tests/masonry/test_api.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.999 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.206 IQR)
- **Top Global Matches:** file_cluster_13: 10.999, file_cluster_8: 11.013, file_cluster_0: 11.061
- **Magnitude:** 279.72 | **LOC:** 518 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (2.459%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_prepare_metadata_for_build_wheel` (Impact: 25.6 | O(N^3) | DB: 9)
  * `cwd` (Impact: 22.4 | O(2^N) | DB: 6)
  * `test_build_editable_wheel_with_metadata_` (Impact: 21.6 | O(N^4))
  * `test_build_wheel_with_metadata_directory` (Impact: 21.4 | O(N^4))
  * `test_prepare_metadata_for_build_wheel_wi` (Impact: 18.9 | O(N^3) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 114`, `args: 23`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 2`, `duplicate_logic: 3`, `orphaned_logic: 19`
* *Architecture:* `io: 10`, `api: 23`, `import: 14`
* *Defense:* `safety: 36`, `doc: 14`, `test: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.839
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` contextlib, tempfile, collections.abc, tests.testutils, typing, poetry.core.masonry, pytest, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `poetry_core-2.3.2/src/poetry/core/constraints/version/version.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 9.571 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.549 IQR)
- **Top Global Matches:** file_cluster_16: 9.571, file_cluster_13: 9.59, file_cluster_8: 9.751
- **Magnitude:** 247.1 | **LOC:** 183 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (26.707%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__eq__` (Impact: 43.8 | O(2^N))
  * `intersect` (Impact: 35.2 | O(2^N))
  * `union` (Impact: 27.2 | O(N^5))
  * `next_breaking` (Impact: 17.7 | O(N^3))
  * `allows` (Impact: 14.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 80`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 31`, `import: 13`
* *Defense:* `safety: 6`, `doc: 2`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.296
  * `Choke Point (Betweenness):` 0.000531 | `Ripple Effect (Closeness):` 0.019499
  * `Imports (Out-Degree: 6):` dataclasses, poetry.core.constraints.version.version_union, poetry.core.version.pep440, poetry.core.version.pep440.version, typing, poetry.core.constraints.version.version_constraint, poetry.core.constraints.version.empty_constraint, __future__...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/packages/specification.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.88 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.104 IQR)
- **Top Global Matches:** file_cluster_13: 10.88, file_cluster_0: 10.897, file_cluster_16: 11.048
- **Magnitude:** 239.8 | **LOC:** 228 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (88.0717%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `is_same_source_as` (Impact: 98.0 | O(N^4) | DB: 2)
  * `__hash__` (Impact: 9.4 | O(N^4))
  * `complete_name` (Impact: 7.3 | O(N^3))
  * `complete_pretty_name` (Impact: 7.3 | O(N^3))
  * `with_features` (Impact: 7.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 71`, `args: 22`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 23`, `dead_code: 1`
* *Architecture:* `api: 27`, `import: 9`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.121
  * `Choke Point (Betweenness):` 0.000148 | `Ripple Effect (Closeness):` 0.042407
  * `Imports (Out-Degree: 2):` packaging.utils, typing, copy, __future__, collections.abc, poetry.core.vcs.git
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/version/pep440/parser.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.985 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.891 IQR)
- **Top Global Matches:** file_cluster_13: 8.985, file_cluster_8: 9.202, file_cluster_16: 9.221
- **Magnitude:** 228.58 | **LOC:** 85 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (80.4164%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 60.6 | O(N^3))
  * `_get_postrelease` (Impact: 42.0 | O(N^3))
  * `_get_prerelease` (Impact: 31.4 | O(N^3))
  * `_get_devrelease` (Impact: 31.4 | O(N^3))
  * `_get_local` (Impact: 28.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 42`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 4`, `import: 11`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.307
  * `Choke Point (Betweenness):` 9.7e-05 | `Ripple Effect (Closeness):` 0.01375
  * `Imports (Out-Degree: 2):` functools, poetry.core.version.pep440, poetry.core.version.pep440.version, typing, re, __future__, packaging.version, poetry.core.version.exceptions
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/tests/packages/test_package.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.643 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.872 IQR)
- **Top Global Matches:** file_cluster_8: 11.643, file_cluster_0: 11.884, file_cluster_16: 11.892
- **Magnitude:** 219.86 | **LOC:** 769 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.1214%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_python_versions_are_made_precise` (Impact: 10.9 | O(N^3))
  * `test_all_classifiers_no_license_classifi` (Impact: 9.3 | O(N^2))
  * `test_all_classifiers_with_license_classi` (Impact: 8.1 | O(N^2))
  * `test_package_author_names_invalid` (Impact: 6.3 | O(N^2))
  * `test_package_authors_invalid` (Impact: 5.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 238`, `args: 48`, `func_start: 48`
* *Risk/State:* `safety_bypasses: 5`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 47`
* *Architecture:* `io: 1`, `api: 48`, `import: 21`
* *Defense:* `safety: 144`, `test: 213`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.839
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` poetry.core.packages.dependency_group, poetry.core.version.exceptions, poetry.core.packages.vcs_dependency, poetry.core.packages.directory_dependency, poetry.core.packages.project_package, pytest, poetry.core.packages.file_dependency, poetry.core.packages.dependency...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `poetry_core-2.3.2/src/poetry/core/version/pep440/segments.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.48 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.349 IQR)
- **Top Global Matches:** file_cluster_16: 10.48, file_cluster_8: 10.488, file_cluster_13: 10.51
- **Magnitude:** 216.98 | **LOC:** 164 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (64.4969%), Tech Debt (99.9926%)
**Top Internal Functions/Classes:**
  * `__post_init__` (Impact: 44.2 | O(N^4))
  * `from_parts` (Impact: 21.3 | O(N^3))
  * `next_major` (Impact: 21.2 | O(N^3))
  * `next_minor` (Impact: 21.2 | O(N^3))
  * `next_patch` (Impact: 21.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 38`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `state_mutation: 15`, `duplicate_logic: 6`
* *Architecture:* `api: 15`, `import: 4`
* *Defense:* `safety: 2`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.016822
  * `Imports (Out-Degree: 0):` dataclasses, collections.abc, typing, __future__
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/factory.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.474 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.341 IQR)
- **Top Global Matches:** file_cluster_13: 11.474, file_cluster_8: 11.532, file_cluster_0: 11.704
- **Magnitude:** 211.2 | **LOC:** 1087 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (44.7491%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_package` (Impact: 3.2 | O(N^2))
  * `_configure_package_dependencies` (Impact: 1.9 | O(N^2))
  * `_add_package_pep735_group_dependencies` (Impact: 1.8 | O(N^2))
  * `_add_package_poetry_group_dependencies` (Impact: 1.8 | O(N^2))
  * `configure_package` (Impact: 1.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 132`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 155`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 8`, `import: 41`
* *Defense:* `safety: 31`, `doc: 6`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.93
  * `Choke Point (Betweenness):` 0.001444 | `Ripple Effect (Closeness):` 0.018692
  * `Imports (Out-Degree: 13):` poetry.core.utils.helpers, poetry.core.packages.dependency_group, itertools, poetry.core.packages.vcs_dependency, poetry.core.packages.directory_dependency, poetry.core.version.markers, poetry.core.packages.project_package, poetry.core.packages.file_dependency...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/masonry/metadata.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.355 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.245 IQR)
- **Top Global Matches:** file_cluster_13: 10.355, file_cluster_16: 10.511, file_cluster_17: 10.515
- **Magnitude:** 205.04 | **LOC:** 170 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (30.6164%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `from_package` (Impact: 106.9 | O(N^6) | DB: 1)
  * `_license_files_from_package` (Impact: 80.6 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 28`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 12`
* *Architecture:* `io: 1`, `api: 3`, `import: 7`
* *Defense:* `safety: 8`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.987
  * `Choke Point (Betweenness):` 0.000193 | `Ripple Effect (Closeness):` 0.010177
  * `Imports (Out-Degree: 4):` poetry.core.packages.project_package, packaging.utils, poetry.core.utils.helpers, typing, poetry.core.version.helpers, pathlib, __future__
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

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
- `poetry_core-2.3.2/tests/version/pep440/test_segments.py` (PYTHON) | Magnitude: 52.0 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 85, test: 48, structural_boundaries: 43, safety: 21
- `poetry_core-2.3.2/tests/packages/utils/test_utils_urls.py` (PYTHON) | Magnitude: 51.56 | Delta: **0.119 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 33, test: 29, safety: 13
- `poetry_core-2.3.2/src/poetry/core/packages/utils/link.py` (PYTHON) | Magnitude: 295.84 | Delta: **0.137 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 165, structural_boundaries: 103, branch: 46, encapsulation: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `poetry_core-2.3.2/src/poetry/core/masonry/utils/package_include.py` (PYTHON) | Magnitude: 131.16 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 63, state_mutation: 30, structural_boundaries: 28, encapsulation: 25
- `poetry_core-2.3.2/tests/integration/test_pep517.py` (PYTHON) | Magnitude: 19.04 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 32, test: 18, explicit_casts: 10
- `poetry_core-2.3.2/src/poetry/core/constraints/version/parser.py` (PYTHON) | Magnitude: 27.48 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 182, structural_boundaries: 78, branch: 55, encapsulation: 21
- `poetry_core-2.3.2/tests/masonry/test_api.py` (PYTHON) | Magnitude: 279.72 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 264, structural_boundaries: 114, test: 66, branch: 41
- `poetry_core-2.3.2/src/poetry/core/packages/specification.py` (PYTHON) | Magnitude: 239.8 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 143, structural_boundaries: 71, encapsulation: 50, branch: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `poetry_core-2.3.2/src/poetry/core/version/pep440/segments.py` (PYTHON) | Magnitude: 216.98 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 111, branch: 41, structural_boundaries: 38, test: 16
- `poetry_core-2.3.2/src/poetry/core/constraints/version/version.py` (PYTHON) | Magnitude: 247.1 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 123, structural_boundaries: 80, api: 31, branch: 27
- `poetry_core-2.3.2/tests/spdx/test_license.py` (PYTHON) | Magnitude: 36.36 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 20, test: 16, args: 8
- `poetry_core-2.3.2/src/poetry/core/packages/vcs_dependency.py` (PYTHON) | Magnitude: 127.2 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 100, structural_boundaries: 39, encapsulation: 35, branch: 18
- `poetry_core-2.3.2/tests/json/test_poetry_schema.py` (PYTHON) | Magnitude: 52.66 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 29, test: 25, generics: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `poetry_core-2.3.2/tests/masonry/builders/test_wheel.py` (PYTHON) | Magnitude: 288.34 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 359, structural_boundaries: 202, test: 153, safety: 108
- `poetry_core-2.3.2/src/poetry/core/constraints/version/__init__.py` (PYTHON) | Magnitude: 16.46 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 20, import: 10, indent_spaces: 10, encapsulation: 2
- `poetry_core-2.3.2/tests/packages/test_main.py` (PYTHON) | Magnitude: 117.6 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 216, structural_boundaries: 142, test: 132, safety: 102
- `poetry_core-2.3.2/tests/packages/utils/test_utils_link.py` (PYTHON) | Magnitude: 39.56 | Delta: **0.098 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 113, structural_boundaries: 66, test: 56, safety: 34
- `poetry_core-2.3.2/src/poetry/core/vcs/git.py` (PYTHON) | Magnitude: 178.42 | Delta: **0.113 IQR** | Secondary Pull: `file_cluster_13`
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
- `poetry_core-2.3.2/src/poetry/core/version/parser.py` -> **Severity: 3.79** (Embedded: 0.0502 * Error Risk: 75.4545%)
- `poetry_core-2.3.2/src/poetry/core/vcs/git.py` -> **Severity: 2.608** (Embedded: 0.0475 * Error Risk: 54.8963%)
- `poetry_core-2.3.2/src/poetry/core/pyproject/toml.py` -> **Severity: 2.562** (Embedded: 0.041 * Error Risk: 62.4675%)
- `poetry_core-2.3.2/src/poetry/core/pyproject/exceptions.py` -> **Severity: 2.454** (Embedded: 0.0307 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `poetry_core-2.3.2/src/poetry/core/version/markers.py` -> **Severity: 5149.106** (Blast Radius: 51.513 * Doc Risk: 99.9574%)
- `poetry_core-2.3.2/src/poetry/core/packages/utils/utils.py` -> **Severity: 4421.819** (Blast Radius: 48.73 * Doc Risk: 90.7412%)
- `poetry_core-2.3.2/src/poetry/core/constraints/version/version.py` -> **Severity: 2329.6** (Blast Radius: 23.296 * Doc Risk: 100.0%)
- `poetry_core-2.3.2/src/poetry/core/packages/dependency.py` -> **Severity: 2310.155** (Blast Radius: 23.143 * Doc Risk: 99.8209%)
- `poetry_core-2.3.2/src/poetry/core/constraints/version/version_constraint.py` -> **Severity: 1968.496** (Blast Radius: 19.685 * Doc Risk: 99.9998%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
