# ARCHITECTURAL_BRIEF: pytest
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
| Total Artifacts | 514 |
| Analyzed Artifacts (Scanned) | 213 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 301 |
| Total LOC | 61159 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 41.4% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2909 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.163 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 11.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.545 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 18 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 190 | 61086 | 89.2% |
| XML | 12 | 0 | 5.6% |
| PLAINTEXT | 4 | 0 | 1.9% |
| YAML | 2 | 15 | 0.9% |
| MARKDOWN | 1 | 0 | 0.5% |
| MAKEFILE | 1 | 27 | 0.5% |
| CSS | 1 | 18 | 0.5% |
| HTML | 1 | 7 | 0.5% |
| JSON | 1 | 6 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Typed Library` (z +0.10; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 24%, Generic / Templated Code Files 23%, Data / Markup / Trivial 22%, Defensive Guards Files 14%, Tests & Verification Files 5%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 208 | 97.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 2.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 301*

**Composition by Extension & Reason:**
- `.rst`: 265x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable)
- `.png`: 8x Excluded (Explicitly Denied Extension: '.png')
- `.py`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 4x Excluded (Unsupported Extension: '.ini')
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 2x Excluded (Unsupported Extension: '.typed')
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')
- `.feature`: 1x Excluded (Unsupported Extension: '.feature')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.2 | 20.5 | 10.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.6 | 50.2 | 55.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 11.8 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 87.0 | 22.0 | 11.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 33.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 30.8 | 1.4 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 83.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 66.9 | 83.6 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1082 | 98 | 18 | `pytest-9.0.2/testing/_py/test_local.py` |
| cleanup | 51 | 17 | 0 | `pytest-9.0.2/src/_pytest/capture.py` |
| guards | 6963 | 147 | 101 | `pytest-9.0.2/testing/_py/test_local.py` |
| danger | 1768 | 129 | 27 | `pytest-9.0.2/testing/python/raises_group.py` |
| concurrency | 352 | 63 | 5 | `pytest-9.0.2/src/_pytest/capture.py` |
| connectivity | 5540 | 178 | 78 | `pytest-9.0.2/testing/python/fixtures.py` |
| io | 1120 | 98 | 12 | `pytest-9.0.2/src/_pytest/_py/path.py` |
| crypto | 3 | 2 | 0 | `pytest-9.0.2/testing/_py/test_local.py` |
| ipc | 58 | 14 | 0 | `pytest-9.0.2/src/_pytest/pytester.py` |
| time | 16 | 6 | 0 | `pytest-9.0.2/testing/_py/test_local.py` |
| serialization | 5 | 4 | 0 | `pytest-9.0.2/src/_pytest/assertion/rewrite.py` |
| regex | 48 | 23 | 1 | `pytest-9.0.2/src/_pytest/pytester.py` |
| events | 84 | 7 | 0 | `pytest-9.0.2/testing/logging/test_fixture.py` |
| tests | 5672 | 158 | 93 | `pytest-9.0.2/testing/test_config.py` |
| docs | 3794 | 138 | 61 | `pytest-9.0.2/testing/python/fixtures.py` |
| debt | 419 | 78 | 5 | `pytest-9.0.2/src/_pytest/hookspec.py` |
| mutation | 23204 | 173 | 339 | `pytest-9.0.2/testing/_py/test_local.py` |
| dead_code | 2841 | 123 | 49 | `pytest-9.0.2/testing/_py/test_local.py` |
| credential | 0 | 0 | 0 | - |
| threat | 714 | 91 | 9 | `pytest-9.0.2/src/_pytest/python.py` |
| ml_ai | 12 | 6 | 0 | `pytest-9.0.2/src/_pytest/python.py` |
| ui | 7 | 2 | 0 | `pytest-9.0.2/testing/code/test_excinfo.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.5714**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pytest-9.0.2/src/_pytest/_py/path.py` (Hits: 96)
- `pytest-9.0.2/testing/test_capture.py` (Hits: 75)
- `pytest-9.0.2/src/_pytest/config/__init__.py` (Hits: 69)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **pytester.py** (`pytest-9.0.2/src/_pytest/pytester.py`) — 54 inbound connections
2. **pathlib.py** (`pytest-9.0.2/src/_pytest/pathlib.py`) — 46 inbound connections
3. **warnings.py** (`pytest-9.0.2/src/_pytest/warnings.py`) — 35 inbound connections
4. **monkeypatch.py** (`pytest-9.0.2/src/_pytest/monkeypatch.py`) — 31 inbound connections
5. **argparsing.py** (`pytest-9.0.2/src/_pytest/config/argparsing.py`) — 27 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_assertrewrite.py** (`pytest-9.0.2/testing/test_assertrewrite.py`) — 49 outbound dependencies
2. **__init__.py** (`pytest-9.0.2/src/_pytest/config/__init__.py`) — 48 outbound dependencies
3. **pytester.py** (`pytest-9.0.2/src/_pytest/pytester.py`) — 39 outbound dependencies
4. **test_pathlib.py** (`pytest-9.0.2/testing/test_pathlib.py`) — 39 outbound dependencies
5. **rewrite.py** (`pytest-9.0.2/src/_pytest/assertion/rewrite.py`) — 36 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_check_exceptions` **(Many-Argument Workhorses)** (@ `pytest-9.0.2/src/_pytest/raises.py`) -> Impact: **97.1** | LOC: 142
- `parametrize` **(Many-Argument Workhorses)** (@ `pytest-9.0.2/src/_pytest/python.py`) -> Impact: **83.0** | LOC: 189
- `__init__` **(Defensive Guards)** (@ `pytest-9.0.2/src/_pytest/raises.py`) -> Impact: **72.5** | LOC: 51
- `_getini_toml` **(Many-Argument Workhorses)** (@ `pytest-9.0.2/src/_pytest/config/__init__.py`) -> Impact: **70.3** | LOC: 83
- `matches` **(Many-Argument Workhorses)** (@ `pytest-9.0.2/src/_pytest/raises.py`) -> Impact: **70.2** | LOC: 122
- `__init__` **(Many-Argument Workhorses)** (@ `pytest-9.0.2/src/_pytest/raises.py`) -> Impact: **68.2** | LOC: 62
- `assertrepr_compare` **(Many-Argument Workhorses)** (@ `pytest-9.0.2/src/_pytest/assertion/util.py`) -> Impact: **67.1** | LOC: 68
- `_getini_ini` **(Many-Argument Workhorses)** (@ `pytest-9.0.2/src/_pytest/config/__init__.py`) -> Impact: **66.5** | LOC: 60
- `make_numbered_dir` **(Many-Argument Workhorses)** (@ `pytest-9.0.2/src/_pytest/_py/path.py`) -> Impact: **57.0** | LOC: 160
- `_safe_repr` **(Many-Argument Workhorses)** (@ `pytest-9.0.2/src/_pytest/_io/pprint.py`) -> Impact: **56.7** | LOC: 57

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pytest-9.0.2/src/_pytest` | 48 | 17267.38 | 44.52% | 20.34% |
| `pytest-9.0.2/testing` | 54 | 15013.94 | 10.78% | 0.0% |
| `pytest-9.0.2/testing/python` | 7 | 3790.88 | 9.7% | 0.0% |
| `pytest-9.0.2/src/_pytest/config` | 5 | 2288.06 | 30.1% | 1.72% |
| `pytest-9.0.2/src/_pytest/assertion` | 4 | 2012.56 | 51.99% | 14.47% |
| `pytest-9.0.2/src/_pytest/_code` | 3 | 1561.7 | 33.35% | 4.99% |
| `pytest-9.0.2/src/_pytest/_py` | 3 | 1555.04 | 37.06% | 4.48% |
| `pytest-9.0.2/testing/code` | 3 | 1538.38 | 25.9% | 0.0% |
| `pytest-9.0.2/testing/_py` | 1 | 1198.0 | 41.66% | 0.0% |
| `pytest-9.0.2/src/_pytest/_io` | 5 | 912.52 | 39.92% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `pytest-9.0.2/src/_pytest/hookspec.py` -> **99.9743%** Exposure
- `pytest-9.0.2/src/_pytest/threadexception.py` -> **99.6604%** Exposure
- `pytest-9.0.2/src/_pytest/setupplan.py` -> **98.9013%** Exposure
- `pytest-9.0.2/src/_pytest/setuponly.py` -> **96.5913%** Exposure
- `pytest-9.0.2/src/_pytest/pastebin.py` -> **94.2357%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `pytest-9.0.2/extra/get_issues.py` -> **100.0%** Exposure
- `pytest-9.0.2/src/_pytest/_argcomplete.py` -> **100.0%** Exposure
- `pytest-9.0.2/src/_pytest/_code/code.py` -> **100.0%** Exposure
- `pytest-9.0.2/src/_pytest/_code/source.py` -> **100.0%** Exposure
- `pytest-9.0.2/src/_pytest/_io/saferepr.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pytest-9.0.2/testing/_py/test_local.py` -> **173** Orphaned Functions | **0** Duplicates
- `pytest-9.0.2/testing/test_terminal.py` -> **154** Orphaned Functions | **0** Duplicates
- `pytest-9.0.2/testing/test_config.py` -> **143** Orphaned Functions | **4** Duplicates
- `pytest-9.0.2/testing/python/metafunc.py` -> **109** Orphaned Functions | **29** Duplicates
- `pytest-9.0.2/testing/test_assertion.py` -> **122** Orphaned Functions | **2** Duplicates

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
- **Unknown Dependencies:** `2027` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `pytest-9.0.2/src/_pytest/threadexception.py` (PYTHON) -> Cumulative Risk: **735.92**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.67)
- **Magnitude:** 100.2 | **LOC:** 153 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9998%), Concurrency (99.9971%)
- **Heaviest Functions:** `collect_thread_exception` (Defensive Guards, Impact: 10.3), `thread_exception_hook` (Many-Argument Workhorses, Impact: 7.1), `cleanup` (Defensive Guards, Impact: 2.4)

### 2. `pytest-9.0.2/src/_pytest/terminal.py` (PYTHON) -> Cumulative Risk: **655.75**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +1.35)
- **Magnitude:** 1767.64 | **LOC:** 1764 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (95.8541%), Documentation (90.9574%)
- **Heaviest Functions:** `pytest_runtest_logreport` (Many-Argument Workhorses, Impact: 52.2), `short_test_summary` (Compute Cores, Impact: 37.9), `report_collect` (Compute Cores, Impact: 31.2)

### 3. `pytest-9.0.2/src/_pytest/mark/structures.py` (PYTHON) -> Cumulative Risk: **655.75**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.51)
- **Magnitude:** 382.28 | **LOC:** 665 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9954%), Safety Score (87.9403%), Verification (80.0%)
- **Heaviest Functions:** `param` (Defensive Guards, Impact: 21.3), `get_unpacked_marks` (Defensive Guards, Impact: 20.6), `__getattr__` (Compute Cores, Impact: 19.5)

### 4. `pytest-9.0.2/src/_pytest/fixtures.py` (PYTHON) -> Cumulative Risk: **655.34**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +1.54)
- **Magnitude:** 1417.64 | **LOC:** 2048 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (93.912%), Verification (80.0%)
- **Heaviest Functions:** `reorder_items_atscope` (Many-Argument Workhorses, Impact: 47.9), `_showfixtures_main` (Compute Cores, Impact: 28.7), `_get_active_fixturedef` (Many-Argument Workhorses, Impact: 26.3)

### 5. `pytest-9.0.2/src/_pytest/mark/expression.py` (PYTHON) -> Cumulative Risk: **655.33**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z -0.15)
- **Magnitude:** 289.96 | **LOC:** 354 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.949%), Documentation (90.2439%)
- **Heaviest Functions:** `lex` (Compute Cores, Impact: 42.4), `single_kwarg` (Compute Cores, Impact: 15.7), `not_expr` (Compute Cores, Impact: 9.4)

### 6. `pytest-9.0.2/src/_pytest/stepwise.py` (PYTHON) -> Cumulative Risk: **647.67**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.10)
- **Magnitude:** 154.5 | **LOC:** 210 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (91.6827%)
- **Heaviest Functions:** `pytest_collection_modifyitems` (Many-Argument Workhorses, Impact: 20.2), `pytest_runtest_logreport` (Compute Cores, Impact: 15.0), `pytest_configure` (Generic / Templated Code, Impact: 6.0)

### 7. `pytest-9.0.2/src/_pytest/mark/__init__.py` (PYTHON) -> Cumulative Risk: **647.49**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.34)
- **Magnitude:** 207.1 | **LOC:** 302 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (92.9376%)
- **Heaviest Functions:** `pytest_addoption` (Compute Cores, Impact: 21.8), `from_item` (Defensive Guards, Impact: 13.6), `deselect_by_keyword` (Generic / Templated Code, Impact: 11.3)

### 8. `pytest-9.0.2/src/_pytest/python.py` (PYTHON) -> Cumulative Risk: **640.36**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.00)
- **Magnitude:** 1350.78 | **LOC:** 1773 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (91.6296%), Verification (80.0%)
- **Heaviest Functions:** `parametrize` (Many-Argument Workhorses, Impact: 83.0), `collect` (Defensive Guards, Impact: 26.5), `__init__` (Many-Argument Workhorses, Impact: 25.7)

### 9. `pytest-9.0.2/src/_pytest/reports.py` (PYTHON) -> Cumulative Risk: **639.69**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.54)
- **Magnitude:** 542.74 | **LOC:** 695 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (95.94%), Verification (80.0%)
- **Heaviest Functions:** `from_item_and_call` (Many-Argument Workhorses, Impact: 29.5), `_report_kwargs_from_json` (Compute Cores, Impact: 28.1), `_report_to_json` (Defensive Guards, Impact: 27.6)

### 10. `pytest-9.0.2/src/_pytest/main.py` (PYTHON) -> Cumulative Risk: **639.09**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +1.85)
- **Magnitude:** 838.94 | **LOC:** 1204 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Documentation (92.4051%), Safety Score (92.1036%)
- **Heaviest Functions:** `collect` (Compute Cores, Impact: 51.4), `resolve_collection_argument` (Many-Argument Workhorses, Impact: 43.0), `perform_collect` (Many-Argument Workhorses, Impact: 38.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pytest-9.0.2/src/_pytest/terminal.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1767.64 | **LOC:** 1764 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.2731%), Tech Debt (10.134%)
**Top Internal Functions/Classes:**
  * `pytest_runtest_logreport` **(Many-Argument Workhorses)** (Impact: 52.2)
  * `short_test_summary` **(Compute Cores)** (Impact: 37.9)
  * `report_collect` **(Compute Cores)** (Impact: 31.2)
  * `summary_warnings` **(Compute Cores)** (Impact: 30.9)
  * `_printcollecteditems` **(Compute Cores)** (Impact: 29.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 246 instances
* *State Mutation (weighted view):* 791
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 347`, `structural_boundaries: 315`, `args: 105`, `func_start: 105`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 299`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `io: 8`, `api: 78`, `import: 48`
* *Defense:* `safety: 42`, `doc: 19`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 30.078
  * `Choke Point (Betweenness):` 0.010603 | `Ripple Effect (Closeness):` 0.239266
  * `Imports (Out-Degree: 10):` __future__, _pytest, _pytest._code, _pytest._code.code, _pytest._io, _pytest._io.wcwidth, _pytest._version, _pytest.compat...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/src/_pytest/config/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1501.86 | **LOC:** 2198 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.3007%), Tech Debt (8.5942%)
**Top Internal Functions/Classes:**
  * `_getini_toml` **(Many-Argument Workhorses)** (Impact: 70.3)
  * `_getini_ini` **(Many-Argument Workhorses)** (Impact: 66.5)
  * `_decide_args` **(Many-Argument Workhorses)** (Impact: 39.0)
  * `parse` **(Many-Argument Workhorses)** (Impact: 33.4)
    * *Intent:* # Parse given cmdline arguments into this config object. assert self.args == [], ( "can only parse c...
  * `_set_initial_conftests` **(Many-Argument Workhorses)** (Impact: 24.6)
    * *Intent:* # # Internal API for local conftest plugin handling. #
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 176 instances
* *State Mutation (weighted view):* 596
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 276`, `structural_boundaries: 455`, `args: 97`, `func_start: 95`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 244`, `fragile_debt: 1`
* *Architecture:* `io: 69`, `api: 61`, `import: 85`
* *Defense:* `safety: 113`, `doc: 61`, `test: 22`, `immutability_locks: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` .compat, .exceptions, .findpaths, __future__, _pytest, _pytest._code, _pytest._code.code, _pytest._io...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/src/_pytest/_py/path.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1478.68 | **LOC:** 1476 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.2129%), Tech Debt (13.4456%)
**Top Internal Functions/Classes:**
  * `make_numbered_dir` **(Many-Argument Workhorses)** (Impact: 57.0)
  * `pyimport` **(Many-Argument Workhorses)** (Impact: 40.4)
    * *Intent:* """Return path as an imported python module. If modname is None, look for the containing package and...
  * `sysfind` **(Many-Argument Workhorses)** (Impact: 40.3)
    * *Intent:* """Return a path object found by looking at the systems underlying PATH specification. If the checke...
  * `copy` **(Many-Argument Workhorses)** (Impact: 28.6)
    * *Intent:* """Copy path to target. If mode is True, will copy permission from path to target. If stat is True, ...
  * `_evaluate` **(Defensive Guards)** (Impact: 26.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 188 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 601
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 369`, `args: 122`, `func_start: 119`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 2`, `state_mutation: 225`, `dead_code: 2`, `fragile_debt: 4`
* *Architecture:* `io: 96`, `api: 112`, `import: 47`
* *Defense:* `safety: 100`, `doc: 71`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.308
  * `Choke Point (Betweenness):` 0.004417 | `Ripple Effect (Closeness):` 0.256754
  * `Imports (Out-Degree: 3):` , .._code.source, __future__, atexit, collections.abc, contextlib, fnmatch, grp...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/src/_pytest/fixtures.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1417.64 | **LOC:** 2048 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.7878%), Tech Debt (19.5624%)
**Top Internal Functions/Classes:**
  * `reorder_items_atscope` **(Many-Argument Workhorses)** (Impact: 47.9)
  * `_showfixtures_main` **(Compute Cores)** (Impact: 28.7)
  * `_get_active_fixturedef` **(Many-Argument Workhorses)** (Impact: 26.3)
  * `getfixtureclosure` **(Many-Argument Workhorses)** (Impact: 25.6)
  * `parsefactories` **(Many-Argument Workhorses)** (Impact: 25.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 176 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 586
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 399`, `args: 107`, `func_start: 105`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 234`, `dead_code: 4`, `planned_debt: 5`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 8`, `api: 78`, `concurrency: 2`, `import: 78`
* *Defense:* `safety: 54`, `doc: 48`, `test: 30`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.22
  * `Choke Point (Betweenness):` 0.010868 | `Ripple Effect (Closeness):` 0.277996
  * `Imports (Out-Degree: 12):` __future__, _pytest, _pytest._code, _pytest._code.code, _pytest._io, _pytest.compat, _pytest.config, _pytest.config.argparsing...
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/src/_pytest/python.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1350.78 | **LOC:** 1773 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.4198%), Tech Debt (14.8924%)
**Top Internal Functions/Classes:**
  * `parametrize` **(Many-Argument Workhorses)** (Impact: 83.0)
  * `collect` **(Defensive Guards)** (Impact: 26.5)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 25.7)
  * `_genfunctions` **(Many-Argument Workhorses)** (Impact: 24.4)
  * `_validate_if_using_arg_names` **(Many-Argument Workhorses)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 167 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 534
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 272`, `structural_boundaries: 402`, `args: 85`, `func_start: 85`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 200`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 4`
* *Architecture:* `io: 8`, `api: 62`, `concurrency: 3`, `import: 74`
* *Defense:* `safety: 51`, `doc: 44`, `test: 14`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.965
  * `Choke Point (Betweenness):` 0.00256 | `Ripple Effect (Closeness):` 0.20554
  * `Imports (Out-Degree: 14):` __future__, _pytest, _pytest._code, _pytest._code.code, _pytest._io.saferepr, _pytest.compat, _pytest.config, _pytest.config.argparsing...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/src/_pytest/_code/code.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1294.36 | **LOC:** 1566 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.3429%), Tech Debt (14.974%)
**Top Internal Functions/Classes:**
  * `get_source` **(Many-Argument Workhorses)** (Impact: 41.6)
  * `_group_contains` **(Many-Argument Workhorses)** (Impact: 41.1)
  * `cut` **(Many-Argument Workhorses)** (Impact: 40.9)
  * `repr_traceback_entry` **(Many-Argument Workhorses)** (Impact: 38.5)
  * `repr_excinfo` **(Compute Cores)** (Impact: 31.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 159 instances
* *State Mutation (weighted view):* 519
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 366`, `args: 104`, `func_start: 103`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 2`, `state_mutation: 201`, `dead_code: 4`, `fragile_debt: 5`
* *Architecture:* `io: 12`, `api: 94`, `import: 46`
* *Defense:* `safety: 55`, `doc: 50`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.903
  * `Choke Point (Betweenness):` 0.003293 | `Ripple Effect (Closeness):` 0.238528
  * `Imports (Out-Degree: 5):` __future__, _pytest, _pytest._code.source, _pytest._io, _pytest._io.saferepr, _pytest.compat, _pytest.deprecated, _pytest.pathlib...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/src/_pytest/pytester.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1233.64 | **LOC:** 1792 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.4044%), Tech Debt (9.0308%)
**Top Internal Functions/Classes:**
  * `_match_lines` **(Many-Argument Workhorses)** (Impact: 40.0)
  * `_makefile` **(Many-Argument Workhorses)** (Impact: 28.7)
  * `matchreport` **(Many-Argument Workhorses)** (Impact: 28.3)
  * `copy_example` **(Compute Cores)** (Impact: 26.5)
    * *Intent:* """Copy file from project's directory into the testdir. :param name: The name of the file to copy. :...
  * `inline_run` **(Many-Argument Workhorses)** (Impact: 24.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 134 instances
* *High Risk Execution (weighted view):* 2
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 497
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 369`, `args: 120`, `func_start: 117`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 31`, `high_risk_execution: 4`, `state_mutation: 229`, `fragile_debt: 1`
* *Architecture:* `io: 48`, `api: 106`, `import: 65`
* *Defense:* `safety: 42`, `doc: 73`, `test: 10`, `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 26.541
  * `Choke Point (Betweenness):` 0.024773 | `Ripple Effect (Closeness):` 0.255042
  * `Imports (Out-Degree: 16):` __future__, _pytest, _pytest._code, _pytest.capture, _pytest.compat, _pytest.config, _pytest.config.argparsing, _pytest.deprecated...
  * `Imported By (In-Degree: 54):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/testing/_py/test_local.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1198.0 | **LOC:** 1580 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.6635%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_visit_breadthfirst` **(Defensive Guards)** (Impact: 10.9)
  * `test_make_numbered_dir` **(Defensive Guards)** (Impact: 9.4)
  * `test_chmod_rec_int` **(Defensive Guards)** (Impact: 7.7)
    * *Intent:* # XXX fragile test def recfilter(x): return x.check(dotfile=0, link=0) oldmodes = {} for x in path1....
  * `test_visit_sort` **(Defensive Guards)** (Impact: 7.4)
  * `test_move_file` **(Defensive Guards)** (Impact: 5.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 63 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 7
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 500
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 646`, `args: 203`, `func_start: 191`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 1`, `state_mutation: 374`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 3`, `unreferenced_by_name: 173`
* *Architecture:* `io: 31`, `api: 200`, `concurrency: 2`, `import: 25`
* *Defense:* `safety: 388`, `doc: 3`, `test: 221`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` .b, __future__, contextlib, grp, hashlib, multiprocessing, os, otherdir...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/testing/test_config.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1180.38 | **LOC:** 3053 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.8229%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_type_errors` **(Compute Cores)** (Impact: 32.2)
    * *Intent:* """Test all possible TypeError cases in getini."""
  * `test_disable_plugin_autoload` **(Many-Argument Workhorses)** (Impact: 30.7)
  * `test_pytest_plugins_in_non_top_level_conftest_unsupported_pyargs` **(Defensive Guards)** (Impact: 15.2)
  * `test_missing_required_plugins` **(Many-Argument Workhorses)** (Impact: 13.2)
  * `test_plugin_preparse_prevents_setuptools_loading` **(Defensive Guards)** (Impact: 11.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 380
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 599`, `args: 179`, `func_start: 167`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 290`, `duplicate_logic: 4`, `unreferenced_by_name: 143`
* *Architecture:* `io: 12`, `api: 198`, `import: 33`
* *Defense:* `safety: 246`, `doc: 182`, `test: 321`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` __future__, _pytest._code, _pytest.config, _pytest.config.argparsing, _pytest.config.exceptions, _pytest.config.findpaths, _pytest.monkeypatch, _pytest.pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/testing/python/fixtures.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1175.22 | **LOC:** 5368 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.8128%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_deterministic_fixture_collection` **(Many-Argument Workhorses)** (Impact: 12.2)
  * `test_non_relative_path` **(Many-Argument Workhorses)** (Impact: 8.2)
  * `test_request_subrequest_addfinalizer_exceptions` **(Many-Argument Workhorses)** (Impact: 5.7)
  * `test_funcarg_lookup_error` **(Many-Argument Workhorses)** (Impact: 5.3)
  * `test_request_garbage` **(Defensive Guards)** (Impact: 5.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 295
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 423`, `args: 228`, `func_start: 212`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 277`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 8`
* *Architecture:* `io: 4`, `api: 218`, `import: 20`
* *Defense:* `safety: 134`, `doc: 324`, `test: 266`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` .., __future__, _pytest.compat, _pytest.config, _pytest.fixtures, _pytest.monkeypatch, _pytest.pytester, _pytest.python...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/testing/test_terminal.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1126.0 | **LOC:** 3551 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.1729%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_tb_option` **(Defensive Guards)** (Impact: 13.3)
  * `test_execute_skipped_positive_2` **(Compute Cores)** (Impact: 9.6)
    * *Intent:* # expected: one test case per line (with file name), word describing result, full reason p = TestFin...
  * `test_pass_skip_fail` **(Defensive Guards)** (Impact: 9.4)
  * `test_line_with_reprcrash` **(C Struct Operations)** (Impact: 8.2)
  * `test_fail_extra_reporting` **(Many-Argument Workhorses)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 368
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 511`, `args: 212`, `func_start: 177`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 1`, `state_mutation: 338`, `unreferenced_by_name: 154`
* *Architecture:* `io: 16`, `api: 196`, `import: 34`
* *Defense:* `safety: 186`, `doc: 159`, `test: 265`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` Errlkjqweqwe, __future__, _pytest._io.wcwidth, _pytest.config, _pytest.monkeypatch, _pytest.pytester, _pytest.reports, _pytest.runner...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/src/_pytest/raises.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1081.5 | **LOC:** 1518 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.312%), Tech Debt (10.7409%)
**Top Internal Functions/Classes:**
  * `_check_exceptions` **(Many-Argument Workhorses)** (Impact: 97.1)
  * `__init__` **(Defensive Guards)** (Impact: 72.5)
  * `matches` **(Many-Argument Workhorses)** (Impact: 70.2)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 68.2)
  * `_parse_exc` **(Defensive Guards)** (Impact: 31.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 106 instances
* *State Mutation (weighted view):* 328
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `structural_boundaries: 292`, `args: 60`, `func_start: 59`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 116`, `dead_code: 6`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 27`, `import: 32`
* *Defense:* `safety: 57`, `doc: 16`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.906
  * `Choke Point (Betweenness):` 0.000414 | `Ripple Effect (Closeness):` 0.163735
  * `Imports (Out-Degree: 5):` __future__, _pytest._code, _pytest._code.code, _pytest.assertion.util, _pytest.outcomes, _pytest.warning_types, abc, collections.abc...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/testing/code/test_excinfo.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1052.02 | **LOC:** 2008 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.0478%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_exceptiongroup_common` **(Many-Argument Workhorses)** (Impact: 21.4)
  * `test_exc_chain_repr` **(Defensive Guards)** (Impact: 16.6)
  * `test_exc_chain_repr_cycle` **(Many-Argument Workhorses)** (Impact: 13.1)
  * `test_traceback_repr_style` **(Defensive Guards)** (Impact: 12.3)
  * `test_exc_repr_chain_suppression` **(Defensive Guards)** (Impact: 10.6)
    * *Intent:* """Check that exc repr does not show chained exceptions in Python 3. - When the exception is raised ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 75 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 474
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 631`, `args: 159`, `func_start: 137`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 5`, `state_mutation: 324`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 6`, `unreferenced_by_name: 98`
* *Architecture:* `io: 16`, `api: 120`, `import: 30`
* *Defense:* `safety: 369`, `doc: 48`, `test: 192`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, _pytest._code, _pytest._code.code, _pytest._io, _pytest.monkeypatch, _pytest.pathlib, _pytest.pytester, ast...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/src/_pytest/assertion/rewrite.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1019.06 | **LOC:** 1203 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.6828%), Tech Debt (11.1578%)
**Top Internal Functions/Classes:**
  * `run` **(Defensive Guards)** (Impact: 48.9)
    * *Intent:* """Find all assert statements in *mod* and rewrite them."""
  * `visit_Assert` **(Many-Argument Workhorses)** (Impact: 35.4)
    * *Intent:* """Return the AST statements to replace the ast.Assert instance. This rewrites the test of an assert...
  * `find_spec` **(Many-Argument Workhorses)** (Impact: 33.8)
  * `_get_assertion_exprs` **(Compute Cores)** (Impact: 30.9)
    * *Intent:* """Return a mapping from {lineno: "assertion test expression"}."""
  * `visit_Compare` **(Many-Argument Workhorses)** (Impact: 30.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 143 instances
* *High Risk Execution (weighted view):* 1
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 533
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 239`, `args: 52`, `func_start: 52`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 2`, `state_mutation: 247`, `dead_code: 4`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 28`, `api: 35`, `import: 44`
* *Defense:* `safety: 54`, `doc: 28`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.106
  * `Choke Point (Betweenness):` 0.000377 | `Ripple Effect (Closeness):` 0.014151
  * `Imports (Out-Degree: 9):` __future__, _pytest._io.saferepr, _pytest._version, _pytest.assertion, _pytest.assertion.util, _pytest.config, _pytest.fixtures, _pytest.main...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/testing/test_assertrewrite.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1013.88 | **LOC:** 2407 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.2508%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_boolop` **(Defensive Guards)** (Impact: 26.5)
  * `getmsg` **(Defensive Guards)** (Impact: 13.2)
  * `test_positions_are_preserved` **(Defensive Guards)** (Impact: 10.8)
    * *Intent:* """Ensure AST positions are preserved during rewriting (#12818)."""
  * `preserved` **(Defensive Guards)** (Impact: 10.6)
  * `test_place_initial_imports` **(Defensive Guards)** (Impact: 10.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 43 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 309
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 672`, `args: 216`, `func_start: 187`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 7`, `state_mutation: 223`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 8`, `duplicate_logic: 2`, `unreferenced_by_name: 113`
* *Architecture:* `io: 20`, `api: 187`, `import: 50`
* *Defense:* `safety: 333`, `doc: 127`, `test: 159`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` , __future__, _pytest._code, _pytest._io.saferepr, _pytest.assertion, _pytest.assertion.rewrite, _pytest.config, _pytest.pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/testing/test_assertion.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 938.34 | **LOC:** 2201 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.2968%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_installed_plugin_rewrite` **(Many-Argument Workhorses)** (Impact: 20.2)
  * `test_truncation_with_ini` **(Many-Argument Workhorses)** (Impact: 15.5)
  * `test_comparisons_handle_colors` **(Many-Argument Workhorses)** (Impact: 12.9)
  * `mock_config` **(C Struct Operations)** (Impact: 7.9)
  * `test_set_extra_item` **(Many-Argument Workhorses)** (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 55 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 376
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 442`, `args: 148`, `func_start: 133`, `class_start: 30`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 266`, `fragile_debt: 6`, `duplicate_logic: 2`, `unreferenced_by_name: 122`
* *Architecture:* `io: 3`, `api: 149`, `concurrency: 1`, `import: 15`
* *Defense:* `safety: 216`, `doc: 74`, `test: 158`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` __future__, _pytest, _pytest.assertion, _pytest.config, _pytest.monkeypatch, _pytest.pytester, attr, collections.abc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/testing/test_junitxml.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 880.46 | **LOC:** 1834 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.2512%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_failure_function` **(Many-Argument Workhorses)** (Impact: 15.5)
  * `test_xfail_captures_output_once` **(Many-Argument Workhorses)** (Impact: 12.5)
  * `test_logging_passing_tests_disabled_logs_output_for_failing_test_issue5430` **(Defensive Guards)** (Impact: 10.9)
  * `assert_attr` **(Defensive Guards)** (Impact: 9.2)
  * `test_junit_duration_report` **(Many-Argument Workhorses)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 368
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 316`, `args: 103`, `func_start: 99`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 234`, `fragile_debt: 3`, `unreferenced_by_name: 77`
* *Architecture:* `io: 7`, `api: 102`, `import: 25`
* *Defense:* `safety: 125`, `doc: 75`, `test: 121`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` __future__, _pytest, _pytest.config, _pytest.junitxml, _pytest.monkeypatch, _pytest.pytester, _pytest.reports, _pytest.stash...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/src/_pytest/main.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 838.94 | **LOC:** 1204 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.2473%), Tech Debt (8.4299%)
**Top Internal Functions/Classes:**
  * `collect` **(Compute Cores)** (Impact: 51.4)
    * *Intent:* # This is a cache for the root directories of the initial paths. # We can't use collection_cache for...
  * `resolve_collection_argument` **(Many-Argument Workhorses)** (Impact: 43.0)
  * `perform_collect` **(Many-Argument Workhorses)** (Impact: 38.8)
  * `pytest_addoption` **(Compute Cores)** (Impact: 30.8)
  * `pytest_ignore_collect` **(Compute Cores)** (Impact: 29.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 106 instances
* *State Mutation (weighted view):* 355
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 216`, `args: 43`, `func_start: 41`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 143`, `planned_debt: 1`
* *Architecture:* `io: 16`, `api: 41`, `import: 46`
* *Defense:* `safety: 30`, `doc: 19`, `test: 2`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 36.425
  * `Choke Point (Betweenness):` 0.009635 | `Ripple Effect (Closeness):` 0.294973
  * `Imports (Out-Degree: 10):` __future__, _pytest, _pytest._code, _pytest.config, _pytest.config.argparsing, _pytest.config.compat, _pytest.fixtures, _pytest.outcomes...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/testing/python/metafunc.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 804.76 | **LOC:** 2275 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.0577%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_parametrize_marked_value` **(Many-Argument Workhorses)** (Impact: 7.0)
  * `test_xfail_passing_is_xpass` **(Many-Argument Workhorses)** (Impact: 6.9)
  * `test_parametrize_indirect_wrong_type` **(Generic / Templated Code)** (Impact: 6.2)
  * `test_parametrize_request_name` **(Generic / Templated Code)** (Impact: 5.8)
    * *Intent:* """Show proper error when 'request' is used as a parameter name in parametrize (#6183)"""
  * `test_parametrize_error_iterator` **(Generic / Templated Code)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 214
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 380`, `args: 157`, `func_start: 151`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 156`, `fragile_debt: 6`, `duplicate_logic: 29`, `unreferenced_by_name: 109`
* *Architecture:* `api: 162`, `import: 24`
* *Defense:* `safety: 107`, `doc: 110`, `test: 187`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` __future__, _pytest, _pytest.compat, _pytest.outcomes, _pytest.pytester, _pytest.python, _pytest.scope, collections.abc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/testing/test_collection.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 782.66 | **LOC:** 2799 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.2922%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_testpaths_ini` **(Defensive Guards)** (Impact: 13.8)
  * `test_strict_parametrization_ids` **(Many-Argument Workhorses)** (Impact: 8.7)
  * `test_check_collect_hashes` **(Defensive Guards)** (Impact: 7.8)
  * `get_reported_items` **(Defensive Guards)** (Impact: 7.4)
    * *Intent:* """Return pytest.Item instances reported by the pytest_collectreport hook"""
  * `test_collect_short_file_windows` **(Tests & Verification)** (Impact: 6.8)
    * *Intent:* """Reproducer for #11895: short paths not collected on Windows."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 283
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 431`, `args: 153`, `func_start: 109`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 239`, `fragile_debt: 4`, `unreferenced_by_name: 102`
* *Architecture:* `io: 7`, `api: 122`, `import: 23`
* *Defense:* `safety: 188`, `doc: 149`, `test: 194`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` __future__, _pytest.compat, _pytest.config, _pytest.fixtures, _pytest.main, _pytest.monkeypatch, _pytest.nodes, _pytest.pathlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/src/_pytest/assertion/util.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 727.36 | **LOC:** 616 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.1243%), Tech Debt (11.3196%)
**Top Internal Functions/Classes:**
  * `assertrepr_compare` **(Many-Argument Workhorses)** (Impact: 67.1)
  * `_compare_eq_any` **(Defensive Guards)** (Impact: 50.9)
  * `_compare_eq_cls` **(Many-Argument Workhorses)** (Impact: 49.6)
  * `_compare_eq_dict` **(Many-Argument Workhorses)** (Impact: 42.4)
  * `_compare_eq_sequence` **(Many-Argument Workhorses)** (Impact: 29.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 107 instances
* *State Mutation (weighted view):* 335
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 117`, `args: 28`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 121`, `fragile_debt: 1`
* *Architecture:* `api: 13`, `import: 23`
* *Defense:* `safety: 22`, `doc: 9`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.359
  * `Choke Point (Betweenness):` 0.005568 | `Ripple Effect (Closeness):` 0.243028
  * `Imports (Out-Degree: 4):` __future__, _pytest, _pytest._code, _pytest._io.pprint, _pytest._io.saferepr, _pytest.compat, _pytest.config, _pytest.python_api...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/src/_pytest/pathlib.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 713.7 | **LOC:** 1064 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.9359%), Tech Debt (8.8745%)
**Top Internal Functions/Classes:**
  * `import_path` **(Many-Argument Workhorses)** (Impact: 44.2)
  * `_import_module_using_spec` **(Many-Argument Workhorses)** (Impact: 44.1)
  * `on_rm_rf_error` **(Many-Argument Workhorses)** (Impact: 25.2)
  * `resolve_pkg_root_and_module_name` **(Compute Cores)** (Impact: 21.2)
  * `fnmatch_ex` **(Compute Cores)** (Impact: 15.6)
    * *Intent:* """A port of FNMatcher from py.path.common which works with PurePath() instances. The difference bet...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 93 instances
* *State Mutation (weighted view):* 302
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 212`, `args: 45`, `func_start: 45`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 116`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `io: 64`, `api: 43`, `import: 41`
* *Defense:* `safety: 54`, `doc: 39`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 50.385
  * `Choke Point (Betweenness):` 0.009978 | `Ripple Effect (Closeness):` 0.330269
  * `Imports (Out-Degree: 6):` __future__, _pytest.compat, _pytest.outcomes, _pytest.warning_types, a, according, atexit, but...
  * `Imported By (In-Degree: 46):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/src/_pytest/capture.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 680.96 | **LOC:** 1145 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.0215%), Tech Debt (59.0235%)
**Top Internal Functions/Classes:**
  * `_windowsconsoleio_workaround` **(Defensive Guards)** (Impact: 16.8)
    * *Intent:* """Workaround for Windows Unicode console handling. Python 3.6 implemented Unicode console handling ...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 14.1)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 12.4)
  * `global_and_fixture_disabled` **(Defensive Guards)** (Impact: 10.6)
    * *Intent:* # Helper context managers """Context manager to temporarily disable global and current fixture captu...
  * `pytest_make_collect_report` **(Defensive Guards)** (Impact: 9.5)
    * *Intent:* # Hooks
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 194
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 284`, `args: 117`, `func_start: 117`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 88`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 34`, `api: 110`, `import: 37`
* *Defense:* `safety: 37`, `doc: 30`, `test: 9`, `immutability_locks: 2`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.529
  * `Choke Point (Betweenness):` 0.000237 | `Ripple Effect (Closeness):` 0.159207
  * `Imports (Out-Degree: 5):` __future__, _pytest.config, _pytest.config.argparsing, _pytest.deprecated, _pytest.fixtures, _pytest.nodes, _pytest.reports, abc...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `pytest-9.0.2/testing/test_capture.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 632.32 | **LOC:** 1736 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.656%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_disabled_capture_fixture` **(Many-Argument Workhorses)** (Impact: 14.7)
  * `StdCaptureFD` **(Compute Cores)** (Impact: 14.4)
    * *Intent:* # note: py.io capture tests where copied from # pylib 1.4.20.dev2 (rev 13d9af95547e)
  * `StdCapture` **(Compute Cores)** (Impact: 14.4)
  * `TeeStdCapture` **(Compute Cores)** (Impact: 14.4)
  * `test_capturing_basic_api` **(Defensive Guards)** (Impact: 8.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 190
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 352`, `args: 105`, `func_start: 101`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 156`, `planned_debt: 1`, `fragile_debt: 4`, `unreferenced_by_name: 85`
* *Architecture:* `io: 75`, `api: 113`, `import: 25`
* *Defense:* `safety: 150`, `doc: 69`, `test: 143`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` __future__, _pytest, _pytest.capture, _pytest.config, _pytest.monkeypatch, _pytest.pytester, collections.abc, contextlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pytest-9.0.2/src/_pytest/junitxml.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 608.9 | **LOC:** 696 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.1793%), Tech Debt (15.7724%)
**Top Internal Functions/Classes:**
  * `pytest_runtest_logreport` **(Many-Argument Workhorses)** (Impact: 38.8)
    * *Intent:* """Handle a setup/call/teardown report, generating the appropriate XML tags as necessary. Note: due ...
  * `write_captured_output` **(Compute Cores)** (Impact: 15.0)
  * `record_testreport` **(Many-Argument Workhorses)** (Impact: 13.6)
  * `append_skipped` **(Defensive Guards)** (Impact: 9.7)
  * `append_failure` **(Defensive Guards)** (Impact: 9.4)
    * *Intent:* # msg = str(report.longrepr.reprtraceback.extraline) if hasattr(report, "wasxfail"): self._add_simpl...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 316
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 122`, `args: 48`, `func_start: 47`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 140`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 8`, `api: 39`, `import: 21`
* *Defense:* `safety: 11`, `doc: 12`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.642
  * `Choke Point (Betweenness):` 0.000109 | `Ripple Effect (Closeness):` 0.004717
  * `Imports (Out-Degree: 7):` __future__, _pytest, _pytest._code.code, _pytest.config, _pytest.config.argparsing, _pytest.fixtures, _pytest.reports, _pytest.stash...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pytest-9.0.2/src/_pytest/pytester.py` -> **Severity: 2.477** (Bridge: 0.0248 * Flux: 100.0%)
- `pytest-9.0.2/src/_pytest/warnings.py` -> **Severity: 1.708** (Bridge: 0.0198 * Flux: 86.3867%)
- `pytest-9.0.2/src/_pytest/nodes.py` -> **Severity: 1.301** (Bridge: 0.013 * Flux: 99.9999%)
- `pytest-9.0.2/src/_pytest/fixtures.py` -> **Severity: 1.087** (Bridge: 0.0109 * Flux: 100.0%)
- `pytest-9.0.2/src/_pytest/terminal.py` -> **Severity: 1.06** (Bridge: 0.0106 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pytest-9.0.2/src/_pytest/pathlib.py` -> **Severity: 30.31** (Embedded: 0.3303 * Error Risk: 91.773%)
- `pytest-9.0.2/src/_pytest/compat.py` -> **Severity: 27.806** (Embedded: 0.3055 * Error Risk: 91.0295%)
- `pytest-9.0.2/src/_pytest/outcomes.py` -> **Severity: 27.401** (Embedded: 0.3116 * Error Risk: 87.931%)
- `pytest-9.0.2/src/_pytest/main.py` -> **Severity: 27.168** (Embedded: 0.295 * Error Risk: 92.1036%)
- `pytest-9.0.2/src/_pytest/nodes.py` -> **Severity: 26.325** (Embedded: 0.3007 * Error Risk: 87.5411%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pytest-9.0.2/src/_pytest/warnings.py` -> **Severity: 9559.638** (Blast Radius: 109.253 * Doc Risk: 87.5%)
- `pytest-9.0.2/src/_pytest/outcomes.py` -> **Severity: 3780.3** (Blast Radius: 37.803 * Doc Risk: 100.0%)
- `pytest-9.0.2/src/_pytest/main.py` -> **Severity: 3365.856** (Blast Radius: 36.425 * Doc Risk: 92.4051%)
- `pytest-9.0.2/src/_pytest/terminal.py` -> **Severity: 2735.817** (Blast Radius: 30.078 * Doc Risk: 90.9574%)
- `pytest-9.0.2/src/_pytest/tracemalloc.py` -> **Severity: 2595.4** (Blast Radius: 25.954 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
