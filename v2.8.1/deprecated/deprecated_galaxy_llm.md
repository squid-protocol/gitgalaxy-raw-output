# ARCHITECTURAL_BRIEF: deprecated
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
| Total Artifacts | 36 |
| Analyzed Artifacts (Scanned) | 21 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 15 |
| Total LOC | 1377 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 58.3% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5311 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.25 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 18 | 1349 | 85.7% |
| PLAINTEXT | 1 | 0 | 4.8% |
| MAKEFILE | 1 | 28 | 4.8% |
| MARKDOWN | 1 | 0 | 4.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 24%, Large Core Modules 14%, Parameter Forwarders Files 14%, Defensive Guards Files 10%, Interface Declarations Files 10%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 19 | 90.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 9.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 15*

**Composition by Extension & Reason:**
- `.rst`: 5x Excluded (Unsupported Extension: '.rst')
- `.cfg`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.cfg')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.spec`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 48.5 | 15.6 | 5.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.8 | 48.3 | 43.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 72.1 | 3.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 64.3 | 14.3 | 8.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 19.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 78.9 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 59.9 | 85.7 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 24 | 6 | 3 | `deprecated-1.3.1/tests/test_sphinx.py` |
| cleanup | 3 | 1 | 0 | `deprecated-1.3.1/Makefile` |
| guards | 187 | 13 | 30 | `deprecated-1.3.1/tests/test_sphinx.py` |
| danger | 69 | 14 | 13 | `deprecated-1.3.1/tests/test_deprecated.py` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 192 | 15 | 22 | `deprecated-1.3.1/tests/test_deprecated.py` |
| io | 12 | 5 | 1 | `deprecated-1.3.1/tests/test_sphinx_class.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 4 | 2 | 0 | `deprecated-1.3.1/deprecated/sphinx.py` |
| events | 0 | 0 | 0 | - |
| tests | 121 | 12 | 14 | `deprecated-1.3.1/tests/test_sphinx.py` |
| docs | 42 | 14 | 6 | `deprecated-1.3.1/deprecated/sphinx.py` |
| debt | 39 | 9 | 4 | `deprecated-1.3.1/tests/test_deprecated.py` |
| mutation | 475 | 16 | 51 | `deprecated-1.3.1/tests/test_sphinx.py` |
| dead_code | 60 | 11 | 8 | `deprecated-1.3.1/tests/test_sphinx.py` |
| credential | 0 | 0 | 0 | - |
| threat | 60 | 10 | 9 | `deprecated-1.3.1/tests/test_deprecated_class.py` |
| ml_ai | 3 | 2 | 0 | `deprecated-1.3.1/setup.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `deprecated-1.3.1/tests/test_sphinx_class.py` (Hits: 6)
- `deprecated-1.3.1/tests/test_sphinx.py` (Hits: 3)
- `deprecated-1.3.1/tests/deprecated_params/test_demo_paragraph.py` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **classic.py** (`deprecated-1.3.1/deprecated/classic.py`) — 5 inbound connections
2. **params.py** (`deprecated-1.3.1/deprecated/params.py`) — 5 inbound connections
3. **sphinx.py** (`deprecated-1.3.1/deprecated/sphinx.py`) — 5 inbound connections
4. **MANIFEST.in** (`deprecated-1.3.1/MANIFEST.in`) — 0 inbound connections
5. **Makefile** (`deprecated-1.3.1/Makefile`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **classic.py** (`deprecated-1.3.1/deprecated/classic.py`) — 8 outbound dependencies
2. **test_sphinx.py** (`deprecated-1.3.1/tests/test_sphinx.py`) — 7 outbound dependencies
3. **test_sphinx_class.py** (`deprecated-1.3.1/tests/test_sphinx_class.py`) — 7 outbound dependencies
4. **params.py** (`deprecated-1.3.1/deprecated/params.py`) — 5 outbound dependencies
5. **test_demo_paragraph.py** (`deprecated-1.3.1/tests/deprecated_params/test_demo_paragraph.py`) — 5 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__call__` **(Compute Cores)** (@ `deprecated-1.3.1/deprecated/sphinx.py`) -> Impact: **30.0** | LOC: 46
  * *Intent:* """ Add the Sphinx directive to your class or function. :param wrapped: Wrapped class or function. :return: the decorated class or function. """
- `get_deprecated_msg` **(Compute Cores)** (@ `deprecated-1.3.1/deprecated/classic.py`) -> Impact: **25.2** | LOC: 25
  * *Intent:* """ Get the deprecation warning message for the user. :param wrapped: Wrapped class or function. :param instance: The object to which the wrapped func...
- `__call__` **(Compute Cores)** (@ `deprecated-1.3.1/deprecated/classic.py`) -> Impact: **18.2** | LOC: 52
  * *Intent:* """ Decorate your class or function. :param wrapped: Wrapped class or function. :return: the decorated class or function. .. versionchanged:: 1.2.4 Do...
- `deprecated` **(Many-Argument Workhorses)** (@ `deprecated-1.3.1/deprecated/classic.py`) -> Impact: **15.0** | LOC: 93
  * *Intent:* """ This is a decorator which can be used to mark functions as deprecated. It will result in a warning being emitted when the function is used. **Clas...
- `test_has_sphinx_docstring` **(Many-Argument Workhorses)** (@ `deprecated-1.3.1/tests/test_sphinx.py`) -> Impact: **14.0** | LOC: 36
  * *Intent:* # The function: def foo(x, y): return x + y # with docstring: foo.__doc__ = docstring # is decorated with: decorator_factory = getattr(deprecated.sphi...
- `test_cls_has_sphinx_docstring` **(Many-Argument Workhorses)** (@ `deprecated-1.3.1/tests/test_sphinx.py`) -> Impact: **14.0** | LOC: 36
  * *Intent:* # The class: class Foo(object): pass # with docstring: Foo.__doc__ = docstring # is decorated with: decorator_factory = getattr(deprecated.sphinx, dir...
- `integrate` **(Type Conversions)** (@ `deprecated-1.3.1/tests/deprecated_params/test_demo_versions.py`) -> Impact: **10.8** | LOC: 4
- `populate_messages` **(Defensive Guards)** (@ `deprecated-1.3.1/deprecated/params.py`) -> Impact: **10.4** | LOC: 9
- `__init__` **(Many-Argument Workhorses)** (@ `deprecated-1.3.1/deprecated/classic.py`) -> Impact: **10.0** | LOC: 42
  * *Intent:* """ Construct a wrapper adapter. :type reason: str :param reason: Reason message which documents the deprecation in your library (can be omitted). :ty...
- `area` **(Type Conversions)** (@ `deprecated-1.3.1/tests/deprecated_params/test_demo_area.py`) -> Impact: **9.4** | LOC: 15

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Type Conversions**: cast- and conversion-heavy function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `deprecated-1.3.1/tests` | 8 | 635.88 | 14.71% | 0.0% |
| `deprecated-1.3.1/deprecated` | 4 | 373.12 | 36.1% | 0.0% |
| `deprecated-1.3.1/tests/deprecated_params` | 5 | 109.66 | 6.42% | 0.0% |
| `deprecated-1.3.1` | 4 | 35.44 | 0.73% | 18.02% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `deprecated-1.3.1/setup.py` -> **72.0768%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `deprecated-1.3.1/deprecated/classic.py` -> **100.0%** Exposure
- `deprecated-1.3.1/deprecated/params.py` -> **100.0%** Exposure
- `deprecated-1.3.1/deprecated/sphinx.py` -> **100.0%** Exposure
- `deprecated-1.3.1/deprecated/__init__.py` -> **68.9974%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `deprecated-1.3.1/tests/test_deprecated.py` -> **13** Orphaned Functions | **16** Duplicates
- `deprecated-1.3.1/tests/test_sphinx.py` -> **15** Orphaned Functions | **6** Duplicates
- `deprecated-1.3.1/tests/test_deprecated_metaclass.py` -> **5** Orphaned Functions | **4** Duplicates
- `deprecated-1.3.1/tests/test_sphinx_metaclass.py` -> **5** Orphaned Functions | **4** Duplicates
- `deprecated-1.3.1/tests/test_deprecated_class.py` -> **8** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `66` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `deprecated-1.3.1/deprecated/params.py` (PYTHON) -> Cumulative Risk: **555.48**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Parameter Forwarders Files` (z +0.52)
- **Magnitude:** 65.84 | **LOC:** 80 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (89.9735%)
- **Heaviest Functions:** `populate_messages` (Defensive Guards, Impact: 10.4), `check_params` (Compute Cores, Impact: 6.9), `__call__` (Annotated Framework Methods, Impact: 4.0)

### 2. `deprecated-1.3.1/deprecated/classic.py` (PYTHON) -> Cumulative Risk: **551.23**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +1.91)
- **Magnitude:** 171.98 | **LOC:** 302 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.7545%), Verification (80.0%)
- **Heaviest Functions:** `get_deprecated_msg` (Compute Cores, Impact: 25.2), `__call__` (Compute Cores, Impact: 18.2), `deprecated` (Many-Argument Workhorses, Impact: 15.0)

### 3. `deprecated-1.3.1/deprecated/sphinx.py` (PYTHON) -> Cumulative Risk: **461.93**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.84)
- **Magnitude:** 118.18 | **LOC:** 282 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.1788%), Api Exposure (50.0335%)
- **Heaviest Functions:** `__call__` (Compute Cores, Impact: 30.0), `__init__` (Many-Argument Workhorses, Impact: 9.1), `deprecated` (Many-Argument Workhorses, Impact: 4.7)

### 4. `deprecated-1.3.1/tests/test_deprecated_metaclass.py` (PYTHON) -> Cumulative Risk: **332.61**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Parameter Forwarders Files` (z -0.49)
- **Magnitude:** 69.74 | **LOC:** 116 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (85.7143%), Stability (50.0%), Safety Score (43.5414%)
- **Heaviest Functions:** `__call__` (Parameter Forwarders, Impact: 4.2), `test_with_singleton_metaclass` (Interface Declarations, Impact: 3.4), `with_metaclass` (Annotated Framework Methods, Impact: 2.5)

### 5. `deprecated-1.3.1/tests/test_sphinx_metaclass.py` (PYTHON) -> Cumulative Risk: **332.61**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Parameter Forwarders Files` (z -0.49)
- **Magnitude:** 69.74 | **LOC:** 116 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (85.7143%), Stability (50.0%), Safety Score (43.5414%)
- **Heaviest Functions:** `__call__` (Parameter Forwarders, Impact: 4.2), `test_with_singleton_metaclass` (Interface Declarations, Impact: 3.4), `with_metaclass` (Annotated Framework Methods, Impact: 2.5)

### 6. `deprecated-1.3.1/tests/deprecated_params/test_demo_pow2.py` (PYTHON) -> Cumulative Risk: **327.26**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +1.30)
- **Magnitude:** 15.14 | **LOC:** 59 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (67.6371%), Stability (50.0%)
- **Heaviest Functions:** `test_pow2` (Defensive Guards, Impact: 4.3), `pow2` (Parameter Forwarders, Impact: 2.1)

### 7. `deprecated-1.3.1/tests/test_sphinx.py` (PYTHON) -> Cumulative Risk: **316.45**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.44)
- **Magnitude:** 178.74 | **LOC:** 425 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Stability (50.0%), Safety Score (38.2991%)
- **Heaviest Functions:** `test_has_sphinx_docstring` (Many-Argument Workhorses, Impact: 14.0), `test_cls_has_sphinx_docstring` (Many-Argument Workhorses, Impact: 14.0), `test_sphinx_deprecated_class_method__warns` (Defensive Guards, Impact: 6.3)

### 8. `deprecated-1.3.1/tests/test_sphinx_adapter.py` (PYTHON) -> Cumulative Risk: **311.09**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.82)
- **Magnitude:** 35.12 | **LOC:** 129 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (85.7143%), Safety Score (67.3767%), Stability (50.0%)
- **Heaviest Functions:** `test_sphinx_adapter` (Defensive Guards, Impact: 3.0), `test_sphinx_adapter__empty_docstring` (Interface Declarations, Impact: 2.7), `test_decorator_accept_line_length` (Defensive Guards, Impact: 2.7)

### 9. `deprecated-1.3.1/tests/test_deprecated.py` (PYTHON) -> Cumulative Risk: **310.31**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.20)
- **Magnitude:** 157.6 | **LOC:** 325 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (92.3077%), Stability (50.0%), Safety Score (38.6986%)
- **Heaviest Functions:** `test_classic_deprecated_class_method__warns` (Defensive Guards, Impact: 7.7), `classic_deprecated_static_method` (Annotated Framework Methods, Impact: 5.2), `classic_deprecated_class_method` (Annotated Framework Methods, Impact: 5.2)

### 10. `deprecated-1.3.1/tests/deprecated_params/test_demo_paragraph.py` (PYTHON) -> Cumulative Risk: **309.66**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +1.44)
- **Magnitude:** 36.46 | **LOC:** 67 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (89.0067%), Stability (50.0%), Documentation (50.0%)
- **Heaviest Functions:** `paragraph` (Compute Cores, Impact: 8.4), `test_paragraph` (Defensive Guards, Impact: 4.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `deprecated-1.3.1/tests/test_sphinx.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 178.74 | **LOC:** 425 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.2661%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_has_sphinx_docstring` **(Many-Argument Workhorses)** (Impact: 14.0)
    * *Intent:* # The function: def foo(x, y): return x + y # with docstring: foo.__doc__ = docstring # is decorated...
  * `test_cls_has_sphinx_docstring` **(Many-Argument Workhorses)** (Impact: 14.0)
    * *Intent:* # The class: class Foo(object): pass # with docstring: Foo.__doc__ = docstring # is decorated with: ...
  * `test_sphinx_deprecated_class_method__warns` **(Defensive Guards)** (Impact: 6.3)
    * *Intent:* # noinspection PyShadowingNames
  * `test_sphinx_deprecated_function__warns` **(Defensive Guards)** (Impact: 3.2)
    * *Intent:* # noinspection PyShadowingNames
  * `test_sphinx_deprecated_static_method__warns` **(Defensive Guards)** (Impact: 3.2)
    * *Intent:* # noinspection PyShadowingNames
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 132`, `args: 34`, `func_start: 33`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 35`, `duplicate_logic: 6`, `unreferenced_by_name: 15`
* *Architecture:* `io: 3`, `api: 39`, `import: 7`
* *Defense:* `safety: 42`, `doc: 7`, `test: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, deprecated.sphinx, pytest, re, sys, textwrap, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/deprecated/classic.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 171.98 | **LOC:** 302 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.1121%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_deprecated_msg` **(Compute Cores)** (Impact: 25.2)
    * *Intent:* """ Get the deprecation warning message for the user. :param wrapped: Wrapped class or function. :pa...
  * `__call__` **(Compute Cores)** (Impact: 18.2)
    * *Intent:* """ Decorate your class or function. :param wrapped: Wrapped class or function. :return: the decorat...
  * `deprecated` **(Many-Argument Workhorses)** (Impact: 15.0)
    * *Intent:* """ This is a decorator which can be used to mark functions as deprecated. It will result in a warni...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 10.0)
    * *Intent:* """ Construct a wrapper adapter. :type reason: str :param reason: Reason message which documents the...
  * `wrapped_cls` **(Compute Cores)** (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 79
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 29`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `api: 7`, `import: 6`
* *Defense:* `safety: 3`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 231.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.333333
  * `Imports (Out-Degree: 0):` deprecated, deprecated.classic, functools, inspect, platform, warnings, wrapt, wrapt._wrappers
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `deprecated-1.3.1/tests/test_deprecated.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 157.6 | **LOC:** 325 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.2834%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_classic_deprecated_class_method__warns` **(Defensive Guards)** (Impact: 7.7)
    * *Intent:* # noinspection PyShadowingNames
  * `classic_deprecated_static_method` **(Annotated Framework Methods)** (Impact: 5.2)
  * `classic_deprecated_class_method` **(Annotated Framework Methods)** (Impact: 5.2)
  * `classic_deprecated_method` **(Annotated Framework Methods)** (Impact: 5.1)
  * `classic_deprecated_function` **(Annotated Framework Methods)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 137`, `args: 36`, `func_start: 36`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 17`, `duplicate_logic: 16`, `unreferenced_by_name: 13`
* *Architecture:* `io: 1`, `api: 46`, `import: 5`
* *Defense:* `safety: 39`, `doc: 2`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deprecated.classic, inspect, pytest, sys, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/deprecated/sphinx.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 118.18 | **LOC:** 282 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.7819%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__call__` **(Compute Cores)** (Impact: 30.0)
    * *Intent:* """ Add the Sphinx directive to your class or function. :param wrapped: Wrapped class or function. :...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 9.1)
  * `deprecated` **(Many-Argument Workhorses)** (Impact: 4.7)
    * *Intent:* """ This decorator can be used to insert a "deprecated" directive in your function/class docstring i...
  * `versionadded` **(Many-Argument Workhorses)** (Impact: 3.4)
    * *Intent:* """ This decorator can be used to insert a "versionadded" directive in your function/class docstring...
  * `versionchanged` **(Many-Argument Workhorses)** (Impact: 3.4)
    * *Intent:* """ This decorator can be used to insert a "versionchanged" directive in your function/class docstri...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 20`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 26`
* *Architecture:* `api: 7`, `import: 4`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 143.787
  * `Choke Point (Betweenness):` 0.013158 | `Ripple Effect (Closeness):` 0.25
  * `Imports (Out-Degree: 1):` deprecated.classic, re, textwrap
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `deprecated-1.3.1/tests/test_deprecated_metaclass.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 69.74 | **LOC:** 116 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.5798%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__call__` **(Parameter Forwarders)** (Impact: 4.2)
  * `test_with_singleton_metaclass` **(Interface Declarations)** (Impact: 3.4)
  * `with_metaclass` **(Annotated Framework Methods)** (Impact: 2.5)
    * *Intent:* """Create a base class with a metaclass."""
  * `__new__` **(Parameter Forwarders)** (Impact: 2.3)
  * `__new__` **(Parameter Forwarders)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 56`, `args: 14`, `func_start: 14`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`, `duplicate_logic: 4`, `unreferenced_by_name: 5`
* *Architecture:* `api: 12`, `import: 2`
* *Defense:* `safety: 15`, `doc: 1`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deprecated.classic, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/test_sphinx_metaclass.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 69.74 | **LOC:** 116 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.5798%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__call__` **(Parameter Forwarders)** (Impact: 4.2)
  * `test_with_singleton_metaclass` **(Interface Declarations)** (Impact: 3.4)
  * `with_metaclass` **(Annotated Framework Methods)** (Impact: 2.5)
    * *Intent:* """Create a base class with a metaclass."""
  * `__new__` **(Parameter Forwarders)** (Impact: 2.3)
  * `__new__` **(Parameter Forwarders)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 56`, `args: 14`, `func_start: 14`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`, `duplicate_logic: 4`, `unreferenced_by_name: 5`
* *Architecture:* `api: 12`, `import: 2`
* *Defense:* `safety: 15`, `doc: 1`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deprecated.sphinx, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/deprecated/params.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 65.84 | **LOC:** 80 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.5073%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `populate_messages` **(Defensive Guards)** (Impact: 10.4)
  * `check_params` **(Compute Cores)** (Impact: 6.9)
  * `__call__` **(Annotated Framework Methods)** (Impact: 4.0)
    * *Intent:* # type: (callable) -> callable signature = inspect.signature(f) @functools.wraps(f) def wrapper(*arg...
  * `warn_messages` **(Parameter Forwarders)** (Impact: 3.7)
    * *Intent:* # type: (list[str]) -> None for message in messages: warnings.warn(message, category=self.category, ...
  * `wrapper` **(Parameter Forwarders)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 16`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 11`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 132.147
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.25
  * `Imports (Out-Degree: 0):` collections, functools, inspect, inspect2, warnings
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `deprecated-1.3.1/tests/test_deprecated_class.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 63.98 | **LOC:** 156 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_class_deprecation_using_wrapper` **(Interface Declarations)** (Impact: 2.4)
    * *Intent:* # stream is used to store the deprecation message for testing stream = io.StringIO() class MyBaseCla...
  * `test_class_deprecation_using_a_simple_decorator` **(Interface Declarations)** (Impact: 2.4)
    * *Intent:* # stream is used to store the deprecation message for testing stream = io.StringIO() # To deprecated...
  * `__new__` **(Parameter Forwarders)** (Impact: 2.1)
  * `wrapped_new` **(Parameter Forwarders)** (Impact: 2.1)
  * `wrapped_new` **(Parameter Forwarders)** (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 74`, `args: 12`, `func_start: 12`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 16`, `unreferenced_by_name: 8`
* *Architecture:* `api: 22`, `import: 5`
* *Defense:* `safety: 29`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, deprecated.classic, inspect, io, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/test_sphinx_class.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 50.44 | **LOC:** 150 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_class_deprecation_using_a_simple_decorator` **(Interface Declarations)** (Impact: 2.4)
    * *Intent:* # stream is used to store the deprecation message for testing stream = io.StringIO() # To deprecated...
  * `wrapped_new` **(Parameter Forwarders)** (Impact: 2.1)
  * `simple_decorator` **(Interface Declarations)** (Impact: 1.9)
    * *Intent:* # To deprecated the class, we use a simple decorator # which patches the original ``__new__`` method...
  * `test_subclass_deprecation_using_deprecated_decorator` **(Tests & Verification)** (Impact: 1.9)
  * `test_class_deprecation_using_deprecated_decorator` **(Tests & Verification)** (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 67`, `args: 9`, `func_start: 9`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 10`, `unreferenced_by_name: 7`
* *Architecture:* `io: 6`, `api: 22`, `import: 7`
* *Defense:* `safety: 30`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, deprecated.sphinx, inspect, io, pytest, sys, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/deprecated_params/test_demo_paragraph.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 36.46 | **LOC:** 67 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.4437%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `paragraph` **(Compute Cores)** (Impact: 8.4)
    * *Intent:* """Create a styled HTML paragraphe."""
  * `test_paragraph` **(Defensive Guards)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 7 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 12`, `args: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 7`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 2`, `import: 5`
* *Defense:* `safety: 1`, `doc: 3`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deprecated.params, pytest, sys, warnings, xml.sax.saxutils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/test_sphinx_adapter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 35.12 | **LOC:** 129 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_sphinx_adapter` **(Defensive Guards)** (Impact: 3.0)
  * `test_sphinx_adapter__empty_docstring` **(Interface Declarations)** (Impact: 2.7)
  * `test_decorator_accept_line_length` **(Defensive Guards)** (Impact: 2.7)
  * `foo` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* """ Description of foo :return: nothing """
  * `foo` **(Interface Declarations)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 21`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 16`, `duplicate_logic: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 3`, `doc: 5`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deprecated.sphinx, pytest, textwrap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/deprecated_params/test_demo_versions.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 26.12 | **LOC:** 46 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.7331%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `integrate` **(Type Conversions)** (Impact: 10.8)
  * `test_only_one_warning_for_each_parameter` **(Callbacks & Closures)** (Impact: 2.8)
    * *Intent:* """ This unit test checks that only one warning message is emitted for each deprecated parameter. Ho...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 11`, `args: 3`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 1`, `doc: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deprecated.params, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/deprecated_params/test_demo_area.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 21.42 | **LOC:** 63 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.674%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `area` **(Type Conversions)** (Impact: 9.4)
  * `test_area` **(Defensive Guards)** (Impact: 4.3)
  * `_area_impl` **(Encapsulated Accessors)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 14`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 1`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 1`, `doc: 1`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deprecated.params, pytest, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/deprecated/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 17.12 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` deprecated.classic, deprecated.params
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 16.86 | **LOC:** 41 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `clean-pyc` **(I/O & Config Routines)** (Impact: 1.2)
  * `all` **(I/O & Config Routines)** (Impact: 1.1)
  * `install-dev` **(I/O & Config Routines)** (Impact: 1.1)
  * `test` **(Tests & Verification)** (Impact: 1.1)
  * `coverage` **(Tests & Verification)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 12`
* *Risk/State:* None
* *Architecture:* `api: 3`
* *Defense:* `test: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/setup.py` (PYTHON | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 16.16 | **LOC:** 200 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.9337%), Tech Debt (72.0768%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`
* *Risk/State:* `fragile_debt: 1`
* *Architecture:* `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deprecated, deprecated.sphinx, setuptools
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/deprecated_params/test_demo_pow2.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 15.14 | **LOC:** 59 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.2555%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_pow2` **(Defensive Guards)** (Impact: 4.3)
  * `pow2` **(Parameter Forwarders)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 11`, `args: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 2`, `import: 4`
* *Defense:* `safety: 1`, `doc: 2`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deprecated.params, pytest, sys, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/deprecated_params/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.42 | **LOC:** 71 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/MANIFEST.in` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 18 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.388
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

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `deprecated-1.3.1/deprecated/sphinx.py` -> **Severity: 1.316** (Bridge: 0.0132 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `deprecated-1.3.1/deprecated/classic.py` -> **Severity: 32.918** (Embedded: 0.3333 * Error Risk: 98.7545%)
- `deprecated-1.3.1/deprecated/sphinx.py` -> **Severity: 24.295** (Embedded: 0.25 * Error Risk: 97.1788%)
- `deprecated-1.3.1/deprecated/params.py` -> **Severity: 22.493** (Embedded: 0.25 * Error Risk: 89.9735%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `deprecated-1.3.1/deprecated/params.py` -> **Severity: 13214.7** (Blast Radius: 132.147 * Doc Risk: 100.0%)
- `deprecated-1.3.1/deprecated/classic.py` -> **Severity: 5501.994** (Blast Radius: 231.084 * Doc Risk: 23.8095%)
- `deprecated-1.3.1/tests/deprecated_params/test_demo_area.py` -> **Severity: 2738.8** (Blast Radius: 27.388 * Doc Risk: 100.0%)
- `deprecated-1.3.1/tests/deprecated_params/test_demo_pow2.py` -> **Severity: 2738.8** (Blast Radius: 27.388 * Doc Risk: 100.0%)
- `deprecated-1.3.1/tests/test_deprecated_class.py` -> **Severity: 2738.8** (Blast Radius: 27.388 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
