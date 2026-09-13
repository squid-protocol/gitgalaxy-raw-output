# ARCHITECTURAL_BRIEF: poetry-core
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
| Total Artifacts | 501 |
| Analyzed Artifacts (Scanned) | 331 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 170 |
| Total LOC | 24622 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 66.1% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5641 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0654 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.5727 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 18 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 265 | 23350 | 80.1% |
| PLAINTEXT | 42 | 0 | 12.7% |
| JSON | 6 | 1113 | 1.8% |
| SHELL | 6 | 12 | 1.8% |
| C | 5 | 147 | 1.5% |
| MARKDOWN | 4 | 0 | 1.2% |
| XML | 3 | 0 | 0.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 285 | 86.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 46 | 13.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 170*

**Composition by Extension & Reason:**
- `.toml`: 87x Excluded (Unsupported Extension: '.toml')
- `.rst`: 41x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Unsupported Format (.undeterminable)
- `.py`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.typed`: 4x Excluded (Unsupported Extension: '.typed')
- `.json`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 3638 LOC)
- `.lark`: 2x Excluded (Unsupported Extension: '.lark')
- `.zip`: 1x Excluded (Explicitly Denied Extension: '.zip')
- `.whl`: 1x Excluded (Unsupported Extension: '.whl')
- `.gz`: 1x Excluded (Explicitly Denied Extension: '.gz')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 15.0 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.3 | 32.3 | 10.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 98.4 | 0.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.1 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 97.5 | 11.6 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 19.1 | 0.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 20.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 11.3 | 0.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 37.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 34.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 479 | 58 | 4 | `poetry_core-2.3.2/tests/version/test_markers.py` |
| cleanup | 2 | 1 | 0 | `poetry_core-2.3.2/src/poetry/core/masonry/builders/sdist.py` |
| guards | 2159 | 93 | 15 | `poetry_core-2.3.2/tests/test_factory.py` |
| danger | 424 | 69 | 4 | `poetry_core-2.3.2/src/poetry/core/factory.py` |
| concurrency | 32 | 10 | 0 | `poetry_core-2.3.2/src/poetry/core/version/markers.py` |
| connectivity | 1409 | 110 | 14 | `poetry_core-2.3.2/src/poetry/core/version/markers.py` |
| io | 220 | 58 | 1 | `poetry_core-2.3.2/tests/packages/test_main.py` |
| crypto | 3 | 3 | 0 | `poetry_core-2.3.2/src/poetry/core/masonry/builders/wheel.py` |
| ipc | 35 | 5 | 0 | `poetry_core-2.3.2/src/poetry/core/masonry/builders/wheel.py` |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 47 | 13 | 0 | `poetry_core-2.3.2/src/poetry/core/vcs/git.py` |
| events | 19 | 6 | 0 | `poetry_core-2.3.2/src/poetry/core/masonry/builders/wheel.py` |
| tests | 1152 | 50 | 10 | `poetry_core-2.3.2/tests/test_factory.py` |
| docs | 168 | 57 | 1 | `poetry_core-2.3.2/tests/test_factory.py` |
| debt | 39 | 12 | 0 | `poetry_core-2.3.2/src/poetry/core/version/markers.py` |
| mutation | 6716 | 142 | 52 | `poetry_core-2.3.2/tests/test_factory.py` |
| dead_code | 585 | 55 | 4 | `poetry_core-2.3.2/tests/version/test_markers.py` |
| credential | 5 | 3 | 0 | `poetry_core-2.3.2/src/poetry/core/vcs/git.py` |
| threat | 202 | 38 | 1 | `poetry_core-2.3.2/src/poetry/core/packages/package.py` |
| ml_ai | 168 | 19 | 0 | `poetry_core-2.3.2/tests/vcs/test_vcs.py` |
| ui | 2 | 1 | 0 | `poetry_core-2.3.2/tests/packages/test_main.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `poetry_core-2.3.2/tests/packages/test_main.py` (Hits: 29)
- `poetry_core-2.3.2/tests/test_factory.py` (Hits: 22)
- `poetry_core-2.3.2/tests/masonry/builders/test_sdist.py` (Hits: 19)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **utils.py** (`poetry_core-2.3.2/src/poetry/core/packages/utils/utils.py`) — 22 inbound connections
2. **dependency.py** (`poetry_core-2.3.2/src/poetry/core/packages/dependency.py`) — 18 inbound connections
3. **markers.py** (`poetry_core-2.3.2/src/poetry/core/version/markers.py`) — 12 inbound connections
4. **directory_dependency.py** (`poetry_core-2.3.2/src/poetry/core/packages/directory_dependency.py`) — 11 inbound connections
5. **vcs_dependency.py** (`poetry_core-2.3.2/src/poetry/core/packages/vcs_dependency.py`) — 10 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **wheel.py** (`poetry_core-2.3.2/src/poetry/core/masonry/builders/wheel.py`) — 30 outbound dependencies
2. **factory.py** (`poetry_core-2.3.2/src/poetry/core/factory.py`) — 25 outbound dependencies
3. **sdist.py** (`poetry_core-2.3.2/src/poetry/core/masonry/builders/sdist.py`) — 22 outbound dependencies
4. **dependency.py** (`poetry_core-2.3.2/src/poetry/core/packages/dependency.py`) — 22 outbound dependencies
5. **package.py** (`poetry_core-2.3.2/src/poetry/core/packages/package.py`) — 22 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_configure_package_metadata` (@ `poetry_core-2.3.2/src/poetry/core/factory.py`) -> Impact: **120.2** | LOC: 151
- `create_nested_marker` (@ `poetry_core-2.3.2/src/poetry/core/packages/utils/utils.py`) -> Impact: **85.1** | LOC: 109
- `_validate_legacy_vs_project` (@ `poetry_core-2.3.2/src/poetry/core/factory.py`) -> Impact: **84.4** | LOC: 128
- `create_from_pep_508` (@ `poetry_core-2.3.2/src/poetry/core/packages/dependency.py`) -> Impact: **76.3** | LOC: 140
- `_merge_single_markers` (@ `poetry_core-2.3.2/src/poetry/core/version/markers.py`) -> Impact: **75.0** | LOC: 99
- `__init__` (@ `poetry_core-2.3.2/src/poetry/core/version/markers.py`) -> Impact: **71.1** | LOC: 81
- `parse_single_constraint` (@ `poetry_core-2.3.2/src/poetry/core/constraints/version/parser.py`) -> Impact: **69.2** | LOC: 143
- `_validate_strict` (@ `poetry_core-2.3.2/src/poetry/core/factory.py`) -> Impact: **59.9** | LOC: 78
- `union` (@ `poetry_core-2.3.2/src/poetry/core/constraints/generic/union_constraint.py`) -> Impact: **59.3** | LOC: 77
- `create_dependency` (@ `poetry_core-2.3.2/src/poetry/core/factory.py`) -> Impact: **56.2** | LOC: 145

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `poetry_core-2.3.2/src/poetry/core/packages` | 11 | 1837.66 | 69.19% | 0.92% |
| `poetry_core-2.3.2/src/poetry/core/version` | 6 | 1689.74 | 37.91% | 16.4% |
| `poetry_core-2.3.2/src/poetry/core/constraints/version` | 11 | 1469.24 | 47.82% | 0.0% |
| `poetry_core-2.3.2/src/poetry/core` | 3 | 1335.36 | 65.22% | 0.0% |
| `poetry_core-2.3.2/tests/packages` | 10 | 1294.76 | 18.35% | 0.0% |
| `poetry_core-2.3.2/src/poetry/core/masonry/builders` | 4 | 1119.58 | 52.01% | 0.0% |
| `poetry_core-2.3.2/tests/version` | 3 | 1091.96 | 8.84% | 0.0% |
| `poetry_core-2.3.2/tests/masonry/builders` | 6 | 1010.96 | 19.31% | 0.0% |
| `poetry_core-2.3.2/tests` | 5 | 941.5 | 9.67% | 0.0% |
| `poetry_core-2.3.2/src/poetry/core/constraints/generic` | 8 | 875.6 | 42.94% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `poetry_core-2.3.2/src/poetry/core/version/markers.py` -> **98.4269%** Exposure
- `poetry_core-2.3.2/src/poetry/core/masonry/api.py` -> **97.1653%** Exposure
- `poetry_core-2.3.2/src/poetry/core/pyproject/tables.py` -> **37.7541%** Exposure
- `poetry_core-2.3.2/src/poetry/core/version/pep440/version.py` -> **11.0557%** Exposure
- `poetry_core-2.3.2/src/poetry/core/packages/package.py` -> **10.1057%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `poetry_core-2.3.2/src/poetry/core/constraints/generic/parser.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/constraints/generic/union_constraint.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/constraints/version/parser.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/constraints/version/util.py` -> **100.0%** Exposure
- `poetry_core-2.3.2/src/poetry/core/constraints/version/version_union.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `poetry_core-2.3.2/tests/version/test_markers.py` -> **87** Orphaned Functions | **0** Duplicates
- `poetry_core-2.3.2/tests/test_factory.py` -> **61** Orphaned Functions | **0** Duplicates
- `poetry_core-2.3.2/tests/packages/test_package.py` -> **47** Orphaned Functions | **0** Duplicates
- `poetry_core-2.3.2/tests/packages/test_dependency.py` -> **27** Orphaned Functions | **0** Duplicates
- `poetry_core-2.3.2/src/poetry/core/version/markers.py` -> **0** Orphaned Functions | **26** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `861` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `poetry_core-2.3.2/src/poetry/core/version/markers.py` (PYTHON) -> Cumulative Risk: **743.97**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1498.64 | **LOC:** 1396 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.4269%), Cognitive Load (95.7989%)
- **Heaviest Functions:** `_merge_single_markers` (Impact: 75.0), `__init__` (Impact: 71.1), `intersect_simplify` (Impact: 39.5)

### 2. `poetry_core-2.3.2/src/poetry/core/version/pep440/version.py` (PYTHON) -> Cumulative Risk: **705.35**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 237.92 | **LOC:** 331 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9963%)
- **Heaviest Functions:** `next_prerelease` (Impact: 18.2), `to_string` (Impact: 9.5), `next_postrelease` (Impact: 7.7)

### 3. `poetry_core-2.3.2/src/poetry/core/constraints/version/version_constraint.py` (PYTHON) -> Cumulative Risk: **688.56**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 122.6 | **LOC:** 131 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9932%), Cognitive Load (97.4954%)
- **Heaviest Functions:** `_is_wildcard_candidate` (Impact: 40.0), `_single_wildcard_range_string` (Impact: 11.2), `allows` (Impact: 1.8)

### 4. `poetry_core-2.3.2/src/poetry/core/packages/specification.py` (PYTHON) -> Cumulative Risk: **676.0**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 180.0 | **LOC:** 228 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), State Flux (99.9988%), Documentation (95.3488%)
- **Heaviest Functions:** `is_same_source_as` (Impact: 40.8), `__init__` (Impact: 10.3), `_normalize_source_url` (Impact: 7.4)

### 5. `poetry_core-2.3.2/src/poetry/core/constraints/version/version_union.py` (PYTHON) -> Cumulative Risk: **675.21**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 316.36 | **LOC:** 325 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (97.7778%), Cognitive Load (95.2547%)
- **Heaviest Functions:** `difference` (Impact: 40.5), `of` (Impact: 28.3), `excludes_single_wildcard_range` (Impact: 15.1)

### 6. `poetry_core-2.3.2/src/poetry/core/constraints/generic/union_constraint.py` (PYTHON) -> Cumulative Risk: **670.75**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 255.56 | **LOC:** 219 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (94.5235%)
- **Heaviest Functions:** `union` (Impact: 59.3), `intersect` (Impact: 45.0), `invert` (Impact: 10.4)

### 7. `poetry_core-2.3.2/src/poetry/core/packages/vcs_dependency.py` (PYTHON) -> Cumulative Risk: **669.46**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 118.7 | **LOC:** 140 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9997%), Cognitive Load (98.8272%)
- **Heaviest Functions:** `__init__` (Impact: 20.7), `_base_pep_508_name` (Impact: 13.1), `pretty_constraint` (Impact: 7.8)

### 8. `poetry_core-2.3.2/src/poetry/core/masonry/utils/module.py` (PYTHON) -> Cumulative Risk: **665.18**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 112.5 | **LOC:** 118 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `__init__` (Impact: 45.1), `file` (Impact: 4.5), `name` (Impact: 1.5)

### 9. `poetry_core-2.3.2/src/poetry/core/vcs/git.py` (PYTHON) -> Cumulative Risk: **664.55**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 234.92 | **LOC:** 296 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.9859%)
- **Heaviest Functions:** `normalize_url` (Impact: 24.0), `url` (Impact: 11.6), `get_ignored_files` (Impact: 11.2)

### 10. `poetry_core-2.3.2/src/poetry/core/packages/dependency_group.py` (PYTHON) -> Cumulative Risk: **663.74**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 244.66 | **LOC:** 222 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.136%)
- **Heaviest Functions:** `dependencies_for_locking` (Impact: 23.3), `_enrich_dependency` (Impact: 21.8), `dependencies` (Impact: 18.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `poetry_core-2.3.2/src/poetry/core/version/markers.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1498.64 | **LOC:** 1396 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.7989%), Tech Debt (98.4269%)
**Top Internal Functions/Classes:**
  * `_merge_single_markers` (Impact: 75.0)
  * `__init__` (Impact: 71.1)
  * `intersect_simplify` (Impact: 39.5)
    * *Intent:* """ Finds a couple of easy simplifications for intersection on MarkerUnions: - intersection with any...
  * `union_simplify` (Impact: 39.4)
    * *Intent:* """ Finds a couple of easy simplifications for union on MultiMarkers: - union with any marker that a...
  * `_compact_markers` (Impact: 38.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 200 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 616
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 293`, `structural_boundaries: 409`, `args: 120`, `func_start: 118`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 216`, `dead_code: 2`, `duplicate_logic: 26`
* *Architecture:* `io: 2`, `api: 93`, `concurrency: 2`, `import: 46`
* *Defense:* `safety: 80`, `doc: 10`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 51.557
  * `Choke Point (Betweenness):` 0.00387 | `Ripple Effect (Closeness):` 0.074242
  * `Imports (Out-Degree: 4):` __future__, abc, collections, collections.abc, functools, itertools, lark, packaging.utils...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/factory.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1247.1 | **LOC:** 1087 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.4403%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_configure_package_metadata` (Impact: 120.2)
  * `_validate_legacy_vs_project` (Impact: 84.4)
  * `_validate_strict` (Impact: 59.9)
  * `create_dependency` (Impact: 56.2)
  * `_configure_package_dependencies` (Impact: 52.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 196 instances
* *State Mutation (weighted view):* 615
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 132`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 223`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 7`, `import: 41`
* *Defense:* `safety: 31`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.837
  * `Choke Point (Betweenness):` 0.001666 | `Ripple Effect (Closeness):` 0.024242
  * `Imports (Out-Degree: 13):` __future__, collections, collections.abc, itertools, logging, packaging.licenses, packaging.utils, pathlib...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/tests/version/test_markers.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1057.4 | **LOC:** 2764 | **CtrlFlow:** 35.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.6098%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_complex_intersection_with_itertools_product_duplicates` (Impact: 42.8)
    * *Intent:* """ Real-world example from https://github.com/python-poetry/poetry/issues/10250. (Only occurs if th...
  * `test_complex_union_is_deterministic` (Impact: 33.4)
    * *Intent:* """ This test might fail sporadically if marker operations are not deterministic! """
  * `test_intersection_avoids_combinatorial_explosion` (Impact: 26.5)
    * *Intent:* """ combinatorial explosion without AtomicMultiMarker and AtomicMarkerUnion based gevent constraint ...
  * `test_merging_python_version_and_python_full_version` (Impact: 19.4)
  * `test_complex_union` (Impact: 18.6)
    * *Intent:* """ real world example on the way to get mutually exclusive markers for numpy(>=1.21.2) of https://p...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 130 instances
* *State Mutation (weighted view):* 434
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 866`, `structural_boundaries: 256`, `args: 88`, `func_start: 88`
* *Risk/State:* `state_mutation: 174`, `unreferenced_by_name: 87`
* *Architecture:* `io: 4`, `api: 88`, `import: 20`
* *Defense:* `safety: 131`, `doc: 6`, `test: 113`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, os, poetry.core.constraints.generic, poetry.core.constraints.version, poetry.core.version.markers, pytest, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `poetry_core-2.3.2/tests/test_factory.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 818.32 | **LOC:** 2109 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.6259%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_create_poetry` (Impact: 46.8)
  * `test_create_poetry_with_license_type` (Impact: 41.1)
  * `complete_legacy_duplicate_warnings` (Impact: 25.8)
  * `test_create_poetry_with_nested_dependency_groups` (Impact: 16.9)
  * `test_validate_with_license_type` (Impact: 15.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 368
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 355`, `args: 68`, `func_start: 64`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 204`, `unreferenced_by_name: 61`
* *Architecture:* `io: 22`, `api: 64`, `import: 21`
* *Defense:* `safety: 190`, `doc: 41`, `test: 116`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` __future__, collections, packaging.utils, pathlib, poetry.core.constraints.version, poetry.core.factory, poetry.core.packages.dependency, poetry.core.packages.dependency_group...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `poetry_core-2.3.2/src/poetry/core/packages/dependency.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 563.98 | **LOC:** 546 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.2373%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create_from_pep_508` (Impact: 76.3)
  * `to_pep_508` (Impact: 36.2)
  * `marker` (Impact: 31.5)
  * `_make_file_or_dir_dep` (Impact: 20.4)
  * `__init__` (Impact: 13.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 85 instances
* *State Mutation (weighted view):* 263
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 161`, `args: 35`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 93`, `dead_code: 1`
* *Architecture:* `io: 4`, `api: 35`, `import: 46`
* *Defense:* `safety: 5`, `doc: 5`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 24.301
  * `Choke Point (Betweenness):` 0.003937 | `Ripple Effect (Closeness):` 0.067366
  * `Imports (Out-Degree: 12):` __future__, collections.abc, contextlib, os, packaging.utils, pathlib, poetry.core.constraints.generic, poetry.core.constraints.version...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/packages/utils/utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 500.96 | **LOC:** 434 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.603%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create_nested_marker` (Impact: 85.1)
  * `normalize_python_version_markers` (Impact: 40.4)
  * `convert_markers` (Impact: 26.3)
  * `url_to_path` (Impact: 20.4)
    * *Intent:* """ Convert an RFC8089 file URI to path. The logic used here is borrowed from pip https://github.com...
  * `add_constraint` (Impact: 8.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 85 instances
* *State Mutation (weighted view):* 264
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 97`, `args: 14`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 94`, `dead_code: 1`
* *Architecture:* `io: 2`, `api: 14`, `import: 32`
* *Defense:* `safety: 16`, `doc: 6`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 48.9
  * `Choke Point (Betweenness):` 0.001479 | `Ripple Effect (Closeness):` 0.088729
  * `Imports (Out-Degree: 1):` __future__, bz2, contextlib, dataclasses, functools, lzma, pathlib, poetry.core.constraints.generic...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/packages/package.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 496.24 | **LOC:** 681 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.9296%), Tech Debt (10.1057%)
**Top Internal Functions/Classes:**
  * `all_classifiers` (Impact: 21.0)
  * `to_dependency` (Impact: 16.2)
  * `with_dependency_groups` (Impact: 13.1)
  * `__repr__` (Impact: 12.7)
  * `full_pretty_version` (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 207
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 189`, `args: 47`, `func_start: 46`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 81`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 2`, `api: 45`, `import: 40`
* *Defense:* `safety: 13`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.874
  * `Choke Point (Betweenness):` 0.000595 | `Ripple Effect (Closeness):` 0.020415
  * `Imports (Out-Degree: 14):` __future__, collections.abc, packaging.licenses, packaging.utils, pathlib, poetry.core.constraints.version, poetry.core.constraints.version.exceptions, poetry.core.packages.dependency...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/constraints/version/version_range.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 442.26 | **LOC:** 473 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.739%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `difference` (Impact: 53.1)
  * `intersect` (Impact: 36.2)
  * `allows` (Impact: 33.5)
  * `union` (Impact: 32.0)
  * `allows_any` (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 153`, `args: 26`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 45`
* *Architecture:* `api: 24`, `import: 16`
* *Defense:* `safety: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.849
  * `Choke Point (Betweenness):` 0.000263 | `Ripple Effect (Closeness):` 0.021338
  * `Imports (Out-Degree: 5):` __future__, contextlib, functools, poetry.core.constraints.version.empty_constraint, poetry.core.constraints.version.version, poetry.core.constraints.version.version_constraint, poetry.core.constraints.version.version_range_constraint, poetry.core.constraints.version.version_union...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/masonry/builders/sdist.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 434.9 | **LOC:** 433 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.9513%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `find_packages` (Impact: 43.6)
  * `build_setup` (Impact: 43.3)
  * `convert_dependencies` (Impact: 34.8)
  * `build` (Impact: 14.5)
  * `find_files_to_add` (Impact: 8.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 77 instances
* *State Mutation (weighted view):* 252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 85`, `args: 12`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 98`
* *Architecture:* `io: 7`, `api: 11`, `import: 25`
* *Defense:* `safety: 5`, `doc: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.358
  * `Choke Point (Betweenness):` 0.000263 | `Ripple Effect (Closeness):` 0.012626
  * `Imports (Out-Degree: 5):` __future__, collections, collections.abc, contextlib, copy, functools, gzip, io...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/tests/masonry/builders/test_sdist.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 432.52 | **LOC:** 883 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.9875%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_package_target_dir` (Impact: 9.4)
  * `test_make_setup` (Impact: 8.7)
  * `test_convert_dependencies` (Impact: 8.2)
  * `test_sdist_members_mtime_default` (Impact: 8.0)
  * `test_default_with_excluded_data` (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 12 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 41 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 250`, `args: 39`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 12`, `state_mutation: 170`
* *Architecture:* `io: 19`, `api: 39`, `import: 23`
* *Defense:* `safety: 137`, `doc: 2`, `test: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.397
  * `Choke Point (Betweenness):` 6.4e-05 | `Ripple Effect (Closeness):` 0.00404
  * `Imports (Out-Degree: 7):` __future__, ast, collections.abc, email.parser, gzip, hashlib, logging, packaging.utils...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/masonry/builders/builder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 353.44 | **LOC:** 391 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.9252%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `find_files_to_add` (Impact: 40.4)
    * *Intent:* """ Finds all files to add to the tarball """
  * `find_excluded_files` (Impact: 29.5)
  * `get_metadata_content` (Impact: 25.8)
  * `__init__` (Impact: 13.4)
  * `is_excluded` (Impact: 12.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 75`, `args: 23`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 47`
* *Architecture:* `io: 2`, `api: 19`, `import: 14`
* *Defense:* `safety: 6`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.258
  * `Choke Point (Betweenness):` 0.000261 | `Ripple Effect (Closeness):` 0.013499
  * `Imports (Out-Degree: 4):` __future__, functools, logging, pathlib, poetry.core.masonry.metadata, poetry.core.masonry.utils.module, poetry.core.masonry.utils.package_include, poetry.core.poetry...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/masonry/builders/wheel.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 320.72 | **LOC:** 563 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.1491%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_build` (Impact: 19.7)
  * `build` (Impact: 18.1)
  * `_add_pth` (Impact: 11.2)
  * `_add_file` (Impact: 10.6)
  * `tag` (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 130`, `args: 30`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 68`
* *Architecture:* `io: 14`, `api: 12`, `import: 33`
* *Defense:* `safety: 12`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.281
  * `Choke Point (Betweenness):` 0.000438 | `Ripple Effect (Closeness):` 0.009091
  * `Imports (Out-Degree: 7):` __future__, base64, collections.abc, contextlib, csv, functools, hashlib, importlib.util...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/constraints/version/version_union.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 316.36 | **LOC:** 325 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.2547%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `difference` (Impact: 40.5)
  * `of` (Impact: 28.3)
  * `excludes_single_wildcard_range` (Impact: 15.1)
  * `intersect` (Impact: 11.4)
  * `allows_any` (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 114`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 49`
* *Architecture:* `api: 22`, `import: 15`
* *Defense:* `safety: 21`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.712
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.017071
  * `Imports (Out-Degree: 5):` __future__, functools, operator, poetry.core.constraints.version.empty_constraint, poetry.core.constraints.version.version, poetry.core.constraints.version.version_constraint, poetry.core.constraints.version.version_range, poetry.core.constraints.version.version_range_constraint...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/tests/packages/test_package.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 295.66 | **LOC:** 769 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.8808%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_package_satisfies_on_repositories` (Impact: 10.8)
  * `test_package_authors_valid` (Impact: 5.5)
  * `test_all_classifiers_no_license_classifiers_if_spdx` (Impact: 4.5)
  * `test_all_classifiers_with_license_classifiers_if_no_spdx` (Impact: 3.4)
  * `test_package_url_groups_optional` (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 245`, `args: 48`, `func_start: 48`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 109`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 47`
* *Architecture:* `io: 1`, `api: 48`, `import: 21`
* *Defense:* `safety: 144`, `test: 69`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` __future__, packaging.licenses, packaging.utils, pathlib, poetry.core.constraints.version, poetry.core.constraints.version.exceptions, poetry.core.factory, poetry.core.packages.dependency...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `poetry_core-2.3.2/src/poetry/core/constraints/generic/union_constraint.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 255.56 | **LOC:** 219 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.5235%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `union` (Impact: 59.3)
  * `intersect` (Impact: 45.0)
  * `invert` (Impact: 10.4)
  * `allows_any` (Impact: 9.1)
  * `allows_all` (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 82
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 63`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 28`
* *Architecture:* `api: 13`, `import: 9`
* *Defense:* `safety: 19`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.422
  * `Choke Point (Betweenness):` 0.000391 | `Ripple Effect (Closeness):` 0.045908
  * `Imports (Out-Degree: 4):` __future__, itertools, poetry.core.constraints.generic, poetry.core.constraints.generic.base_constraint, poetry.core.constraints.generic.constraint, poetry.core.constraints.generic.empty_constraint, poetry.core.constraints.generic.multi_constraint
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/constraints/version/parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 252.78 | **LOC:** 259 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.0893%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_single_constraint` (Impact: 69.2)
  * `_parse_constraint` (Impact: 24.6)
  * `_make_x_constraint_range` (Impact: 19.5)
  * `parse_marker_version_constraint` (Impact: 2.0)
  * `parse_constraint` (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 78`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 43`
* *Architecture:* `api: 3`, `import: 20`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.973
  * `Choke Point (Betweenness):` 2.8e-05 | `Ripple Effect (Closeness):` 0.00303
  * `Imports (Out-Degree: 7):` __future__, functools, poetry.core.constraints.version.exceptions, poetry.core.constraints.version.patterns, poetry.core.constraints.version.version, poetry.core.constraints.version.version_constraint, poetry.core.constraints.version.version_range, poetry.core.constraints.version.version_union...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/packages/dependency_group.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 244.66 | **LOC:** 222 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.6396%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dependencies_for_locking` (Impact: 23.3)
  * `_enrich_dependency` (Impact: 21.8)
  * `dependencies` (Impact: 18.1)
  * `remove_dependency` (Impact: 9.6)
  * `_resolve_included_dependency_groups` (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 51`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 43`
* *Architecture:* `api: 13`, `import: 11`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.444
  * `Choke Point (Betweenness):` 6.3e-05 | `Ripple Effect (Closeness):` 0.046707
  * `Imports (Out-Degree: 5):` __future__, collections, packaging.utils, poetry.core.packages.dependency, poetry.core.packages.directory_dependency, poetry.core.packages.vcs_dependency, poetry.core.version.markers, typing
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/tests/masonry/builders/test_wheel.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 243.94 | **LOC:** 624 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.8444%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_wheel_includes_licenses_in_correct_paths` (Impact: 10.9)
  * `test_wheel_package_target_dir` (Impact: 9.5)
  * `test_tag` (Impact: 9.5)
    * *Intent:* """Tests that tag returns a valid tag if a build script is used, no matter if poetry-core lives insi...
  * `test_dist_info_date_time_default_value` (Impact: 6.4)
  * `clear_samples_build` (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 230`, `args: 35`, `func_start: 35`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 83`, `fragile_debt: 1`
* *Architecture:* `io: 3`, `api: 35`, `import: 19`
* *Defense:* `safety: 108`, `doc: 6`, `test: 45`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.163
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.00303
  * `Imports (Out-Degree: 3):` __future__, collections.abc, importlib.machinery, logging, os, pathlib, poetry.core.factory, poetry.core.masonry.builders.wheel...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/version/pep440/version.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 237.92 | **LOC:** 331 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (11.0557%)
**Top Internal Functions/Classes:**
  * `next_prerelease` (Impact: 18.2)
  * `to_string` (Impact: 9.5)
  * `next_postrelease` (Impact: 7.7)
  * `next_devrelease` (Impact: 6.7)
  * `__post_init__` (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 114`, `args: 36`, `func_start: 36`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 28`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 35`, `import: 15`
* *Defense:* `safety: 11`, `doc: 1`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.887
  * `Choke Point (Betweenness):` 0.000359 | `Ripple Effect (Closeness):` 0.018041
  * `Imports (Out-Degree: 2):` __future__, collections.abc, dataclasses, functools, poetry.core.version.pep440.parser, poetry.core.version.pep440.segments, typing, warnings
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/vcs/git.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 234.92 | **LOC:** 296 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.743%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `normalize_url` (Impact: 24.0)
  * `url` (Impact: 11.6)
  * `get_ignored_files` (Impact: 11.2)
  * `parse` (Impact: 9.5)
  * `executable` (Impact: 8.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 30 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 51`, `args: 16`, `func_start: 16`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 1`, `state_mutation: 57`
* *Architecture:* `io: 1`, `api: 17`, `import: 7`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.324
  * `Choke Point (Betweenness):` 0.000184 | `Ripple Effect (Closeness):` 0.051212
  * `Imports (Out-Degree: 1):` __future__, collections, pathlib, poetry.core.utils._compat, re, subprocess, typing
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/packages/utils/link.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 224.94 | **LOC:** 257 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.8295%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 17.9)
  * `metadata_hashes` (Impact: 13.2)
  * `hashes` (Impact: 10.2)
  * `egg_fragment` (Impact: 7.3)
  * `subdirectory_fragment` (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 103`, `args: 33`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `io: 1`, `api: 34`, `import: 11`
* *Defense:* `safety: 13`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.889
  * `Choke Point (Betweenness):` 0.000111 | `Ripple Effect (Closeness):` 0.044628
  * `Imports (Out-Degree: 1):` __future__, collections.abc, datetime, functools, poetry.core.packages.utils.utils, posixpath, re, sys...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/src/poetry/core/constraints/generic/constraint.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 224.62 | **LOC:** 259 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.4661%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `union` (Impact: 24.2)
  * `allows_all` (Impact: 22.1)
  * `allows_any` (Impact: 22.1)
  * `intersect` (Impact: 13.1)
  * `intersect` (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 105`, `args: 20`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `state_mutation: 21`
* *Architecture:* `api: 20`, `import: 15`
* *Defense:* `safety: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.851
  * `Choke Point (Betweenness):` 0.000477 | `Ripple Effect (Closeness):` 0.046583
  * `Imports (Out-Degree: 5):` __future__, collections.abc, operator, poetry.core.constraints.generic, poetry.core.constraints.generic.any_constraint, poetry.core.constraints.generic.base_constraint, poetry.core.constraints.generic.empty_constraint, poetry.core.constraints.generic.multi_constraint...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `poetry_core-2.3.2/tests/packages/test_dependency_group.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 218.54 | **LOC:** 686 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.5673%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_dependencies_for_locking` (Impact: 37.5)
  * `create_dependency` (Impact: 20.4)
  * `test_include_dependency_groups` (Impact: 16.2)
  * `test_add_dependency_adds_to_correct_list` (Impact: 12.1)
  * `test_dependencies` (Impact: 11.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 68`, `args: 13`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 39`, `unreferenced_by_name: 12`
* *Architecture:* `io: 5`, `api: 13`, `import: 8`
* *Defense:* `safety: 38`, `doc: 1`, `test: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` __future__, packaging.utils, pathlib, poetry.core.packages.dependency, poetry.core.packages.dependency_group, poetry.core.packages.directory_dependency, poetry.core.packages.vcs_dependency, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `poetry_core-2.3.2/tests/packages/test_main.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 193.5 | **LOC:** 344 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.4921%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_dependency_from_pep_508_complex` (Impact: 9.9)
  * `test_dependency_from_pep_508_with_python_full_version` (Impact: 6.8)
  * `test_dependency_from_pep_508_with_python_version_union_of_multi` (Impact: 5.7)
  * `test_dependency_from_pep_508_with_not_in_op_marker` (Impact: 3.7)
  * `test_dependency_from_pep_508_with_python_version` (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 142`, `args: 25`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 55`, `unreferenced_by_name: 25`
* *Architecture:* `io: 29`, `api: 25`, `import: 8`
* *Defense:* `safety: 102`, `test: 30`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.784
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` __future__, poetry.core.constraints.version, poetry.core.packages.dependency, poetry.core.packages.url_dependency, poetry.core.packages.vcs_dependency, pytest, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `poetry_core-2.3.2/src/poetry/core/packages/specification.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 180.0 | **LOC:** 228 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `is_same_source_as` (Impact: 40.8)
  * `__init__` (Impact: 10.3)
  * `_normalize_source_url` (Impact: 7.4)
  * `provides` (Impact: 4.0)
    * *Intent:* """ Helper method to determine if this package provides the given specification. This determination ...
  * `with_features` (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 71`, `args: 22`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 21`, `dead_code: 1`
* *Architecture:* `api: 22`, `import: 9`
* *Defense:* `safety: 1`, `doc: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.109
  * `Choke Point (Betweenness):` 0.00014 | `Ripple Effect (Closeness):` 0.045141
  * `Imports (Out-Degree: 2):` __future__, collections.abc, copy, packaging.utils, poetry.core.vcs.git, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `poetry_core-2.3.2/src/poetry/core/packages/dependency.py` -> **Severity: 0.394** (Bridge: 0.0039 * Flux: 100.0%)
- `poetry_core-2.3.2/src/poetry/core/version/markers.py` -> **Severity: 0.387** (Bridge: 0.0039 * Flux: 100.0%)
- `poetry_core-2.3.2/src/poetry/core/constraints/generic/parser.py` -> **Severity: 0.279** (Bridge: 0.0028 * Flux: 100.0%)
- `poetry_core-2.3.2/src/poetry/core/factory.py` -> **Severity: 0.167** (Bridge: 0.0017 * Flux: 100.0%)
- `poetry_core-2.3.2/src/poetry/core/packages/utils/utils.py` -> **Severity: 0.148** (Bridge: 0.0015 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `poetry_core-2.3.2/src/poetry/core/packages/utils/utils.py` -> **Severity: 8.797** (Embedded: 0.0887 * Error Risk: 99.1431%)
- `poetry_core-2.3.2/src/poetry/core/version/markers.py` -> **Severity: 7.105** (Embedded: 0.0742 * Error Risk: 95.7069%)
- `poetry_core-2.3.2/src/poetry/core/packages/dependency.py` -> **Severity: 6.595** (Embedded: 0.0674 * Error Risk: 97.8971%)
- `poetry_core-2.3.2/src/poetry/core/constraints/generic/parser.py` -> **Severity: 5.407** (Embedded: 0.0546 * Error Risk: 98.979%)
- `poetry_core-2.3.2/src/poetry/core/vcs/git.py` -> **Severity: 4.967** (Embedded: 0.0512 * Error Risk: 96.9859%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `poetry_core-2.3.2/src/poetry/core/version/markers.py` -> **Severity: 4844.801** (Blast Radius: 51.557 * Doc Risk: 93.9698%)
- `poetry_core-2.3.2/src/poetry/core/packages/utils/utils.py` -> **Severity: 2794.288** (Blast Radius: 48.9 * Doc Risk: 57.1429%)
- `poetry_core-2.3.2/src/poetry/core/constraints/version/version.py` -> **Severity: 2239.2** (Blast Radius: 22.392 * Doc Risk: 100.0%)
- `poetry_core-2.3.2/src/poetry/core/packages/dependency.py` -> **Severity: 2218.786** (Blast Radius: 24.301 * Doc Risk: 91.3043%)
- `poetry_core-2.3.2/src/poetry/core/constraints/version/version_constraint.py` -> **Severity: 1887.9** (Blast Radius: 18.879 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
