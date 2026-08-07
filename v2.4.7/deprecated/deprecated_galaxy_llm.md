# ARCHITECTURAL_BRIEF: deprecated
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/deprecated` |
| **Timestamp** | `2026-08-07T05:22:09.326405+00:00` |
| **Scan Duration** | `0.13s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 19 malicious artifacts.

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
| Assortativity | inf | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.9583 | Hops between files. Lower = Tighter coupling. |
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
> **Architectural Drift Z-Score:** `4.422`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 7 | 33.3% |
| file_cluster_8 | 6 | 28.6% |
| file_cluster_0 | 6 | 28.6% |

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

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 45.0 | 12.2 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 59.7 | 22.6 | 13.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 99.6 | 9.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 2.6 | 0.7 | 0.0 | 0.0 |
| API Exposure | 0.0 | 11.0 | 4.8 | 4.4 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 99.8 | 15.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 87.0 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 85.0 | 7.3 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

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

- `__call__` (@ `deprecated-1.3.1/deprecated/sphinx.py`) -> Impact: **29.8** | LOC: 41
- `get_deprecated_msg` (@ `deprecated-1.3.1/deprecated/classic.py`) -> Impact: **24.9** | LOC: 18
- `__call__` (@ `deprecated-1.3.1/deprecated/classic.py`) -> Impact: **21.1** | LOC: 41
- `test_has_sphinx_docstring` (@ `deprecated-1.3.1/tests/test_sphinx.py`) -> Impact: **16.5** | LOC: 36
- `test_cls_has_sphinx_docstring` (@ `deprecated-1.3.1/tests/test_sphinx.py`) -> Impact: **16.5** | LOC: 36
- `deprecated` (@ `deprecated-1.3.1/deprecated/classic.py`) -> Impact: **11.2** | LOC: 17
- `test_classic_deprecated_class_method__wa` (@ `deprecated-1.3.1/tests/test_deprecated.py`) -> Impact: **11.0** | LOC: 13
  * *Intent:* # noinspection PyShadowingNames
- `integrate` (@ `deprecated-1.3.1/tests/deprecated_params/test_demo_versions.py`) -> Impact: **10.8** | LOC: 4
- `wrapped_cls` (@ `deprecated-1.3.1/deprecated/classic.py`) -> Impact: **10.7** | LOC: 13
- `populate_messages` (@ `deprecated-1.3.1/deprecated/params.py`) -> Impact: **10.4** | LOC: 9

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `deprecated-1.3.1/tests` | 8 | 623.38 | 11.73% | 0.0% |
| `deprecated-1.3.1/deprecated` | 4 | 228.32 | 28.26% | 0.0% |
| `deprecated-1.3.1/tests/deprecated_params` | 5 | 74.36 | 3.37% | 0.0% |
| `deprecated-1.3.1` | 4 | 23.24 | 2.12% | 42.92% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `deprecated-1.3.1/Makefile` -> **99.6072%** Exposure
- `deprecated-1.3.1/setup.py` -> **72.0768%** Exposure
### Highest State Flux (Mutation/Volatility)
- `deprecated-1.3.1/deprecated/classic.py` -> **99.8151%** Exposure
- `deprecated-1.3.1/deprecated/sphinx.py` -> **97.8032%** Exposure
- `deprecated-1.3.1/deprecated/params.py` -> **95.7929%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `deprecated-1.3.1/tests/test_deprecated.py` -> **13** Orphaned Functions | **16** Duplicates
- `deprecated-1.3.1/tests/test_sphinx.py` -> **15** Orphaned Functions | **7** Duplicates
- `deprecated-1.3.1/tests/test_deprecated_metaclass.py` -> **4** Orphaned Functions | **8** Duplicates
- `deprecated-1.3.1/tests/test_sphinx_metaclass.py` -> **4** Orphaned Functions | **8** Duplicates
- `deprecated-1.3.1/tests/test_deprecated_class.py` -> **7** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`deprecated-1.3.1/deprecated/classic.py`** -> AI Confidence: **99.31%**
2. **`deprecated-1.3.1/tests/test_sphinx_class.py`** -> AI Confidence: **99.08%**
3. **`deprecated-1.3.1/tests/test_sphinx.py`** -> AI Confidence: **99.07%**
4. **`deprecated-1.3.1/deprecated/sphinx.py`** -> AI Confidence: **99.0%**
5. **`deprecated-1.3.1/tests/deprecated_params/test_demo_area.py`** -> AI Confidence: **99.0%**
6. **`deprecated-1.3.1/tests/test_deprecated.py`** -> AI Confidence: **98.96%**
7. **`deprecated-1.3.1/deprecated/params.py`** -> AI Confidence: **98.93%**
8. **`deprecated-1.3.1/tests/deprecated_params/test_demo_paragraph.py`** -> AI Confidence: **98.93%**
9. **`deprecated-1.3.1/setup.py`** -> AI Confidence: **98.89%**
10. **`deprecated-1.3.1/tests/test_sphinx_adapter.py`** -> AI Confidence: **98.88%**

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

### 1. `deprecated-1.3.1/deprecated/params.py` (PYTHON) -> Cumulative Risk: **424.11**
- **Archetype:** `file_cluster_13` (Distance: 11.717 IQR)
- **Magnitude:** 43.84 | **LOC:** 80 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (95.7929%), Documentation (85.0442%), Safety Score (53.9915%)
- **Heaviest Functions:** `populate_messages` (Impact: 10.4), `check_params` (Impact: 6.9), `__call__` (Impact: 4.0)

### 2. `deprecated-1.3.1/deprecated/classic.py` (PYTHON) -> Cumulative Risk: **370.92**
- **Archetype:** `file_cluster_13` (Distance: 11.925 IQR)
- **Magnitude:** 111.38 | **LOC:** 302 | **CtrlFlow:** 53.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8151%), Safety Score (59.6977%), Stability (50.0%)
- **Heaviest Functions:** `get_deprecated_msg` (Impact: 24.9), `__call__` (Impact: 21.1), `deprecated` (Impact: 11.2)

### 3. `deprecated-1.3.1/deprecated/sphinx.py` (PYTHON) -> Cumulative Risk: **353.6**
- **Archetype:** `file_cluster_13` (Distance: 11.352 IQR)
- **Magnitude:** 59.98 | **LOC:** 282 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (97.8032%), Safety Score (55.2832%), Stability (50.0%)
- **Heaviest Functions:** `__call__` (Impact: 29.8), `deprecated` (Impact: 2.7), `get_deprecated_msg` (Impact: 2.5)

### 4. `deprecated-1.3.1/Makefile` (MAKEFILE) -> Cumulative Risk: **277.72**
- **Archetype:** `file_cluster_8` (Distance: 6.845 IQR)
- **Magnitude:** 4.66 | **LOC:** 41 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.6072%), Stability (50.0%), Documentation (11.9203%)
- **Heaviest Functions:** `clean-pyc` (Impact: 1.1)

### 5. `deprecated-1.3.1/setup.py` (PYTHON) -> Cumulative Risk: **238.31**
- **Archetype:** `file_cluster_8` (Distance: 6.595 IQR)
- **Magnitude:** 16.16 | **LOC:** 200 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (72.0768%), Stability (50.0%), Documentation (11.9203%)

### 6. `deprecated-1.3.1/tests/deprecated_params/test_demo_versions.py` (PYTHON) -> Cumulative Risk: **214.2**
- **Archetype:** `file_cluster_13` (Distance: 9.932 IQR)
- **Magnitude:** 20.12 | **LOC:** 46 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (53.8078%), Stability (50.0%), Api Exposure (7.2013%)
- **Heaviest Functions:** `integrate` (Impact: 10.8), `test_only_one_warning_for_each_parameter` (Impact: 5.8)

### 7. `deprecated-1.3.1/tests/deprecated_params/test_demo_paragraph.py` (PYTHON) -> Cumulative Risk: **207.77**
- **Archetype:** `file_cluster_13` (Distance: 9.264 IQR)
- **Magnitude:** 12.16 | **LOC:** 67 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Safety Score (49.9741%), Api Exposure (5.2073%)
- **Heaviest Functions:** `paragraph` (Impact: 9.4)

### 8. `deprecated-1.3.1/tests/deprecated_params/test_demo_pow2.py` (PYTHON) -> Cumulative Risk: **207.07**
- **Archetype:** `file_cluster_13` (Distance: 8.972 IQR)
- **Magnitude:** 11.14 | **LOC:** 59 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Safety Score (49.5263%), Api Exposure (5.3665%)
- **Heaviest Functions:** `test_pow2` (Impact: 6.3), `pow2` (Impact: 2.1)

### 9. `deprecated-1.3.1/tests/test_deprecated_metaclass.py` (PYTHON) -> Cumulative Risk: **191.85**
- **Archetype:** `file_cluster_0` (Distance: 12.198 IQR)
- **Magnitude:** 65.34 | **LOC:** 116 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Cognitive Load (24.5477%), Safety Score (12.9945%)
- **Heaviest Functions:** `test_with_singleton_metaclass` (Impact: 6.6), `test_with_metaclass` (Impact: 4.6), `test_with_new` (Impact: 4.5)

### 10. `deprecated-1.3.1/tests/test_sphinx_metaclass.py` (PYTHON) -> Cumulative Risk: **191.85**
- **Archetype:** `file_cluster_0` (Distance: 12.198 IQR)
- **Magnitude:** 65.34 | **LOC:** 116 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Cognitive Load (24.5477%), Safety Score (12.9945%)
- **Heaviest Functions:** `test_with_singleton_metaclass` (Impact: 6.6), `test_with_metaclass` (Impact: 4.6), `test_with_new` (Impact: 4.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `deprecated-1.3.1/tests/test_deprecated.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.196 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.567 IQR)
- **Top Global Matches:** file_cluster_0: 11.196, file_cluster_8: 11.468, file_cluster_13: 11.686
- **Magnitude:** 183.3 | **LOC:** 325 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.9035%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_classic_deprecated_class_method__wa` (Impact: 11.0)
    * *Intent:* # noinspection PyShadowingNames
  * `test_classic_deprecated_function__warns` (Impact: 7.4)
    * *Intent:* # noinspection PyShadowingNames
  * `test_classic_deprecated_static_method__w` (Impact: 7.4)
    * *Intent:* # noinspection PyShadowingNames
  * `classic_deprecated_static_method` (Impact: 6.2)
  * `classic_deprecated_class_method` (Impact: 6.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 125`, `args: 36`, `func_start: 36`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 19`, `duplicate_logic: 16`, `orphaned_logic: 13`
* *Architecture:* `io: 1`, `api: 46`, `import: 5`
* *Defense:* `safety: 39`, `doc: 4`, `test: 55`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pytest, warnings, inspect, deprecated.classic, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/test_sphinx.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.165 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.333 IQR)
- **Top Global Matches:** file_cluster_0: 11.165, file_cluster_8: 11.28, file_cluster_13: 11.503
- **Magnitude:** 169.44 | **LOC:** 425 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.8043%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_has_sphinx_docstring` (Impact: 16.5)
  * `test_cls_has_sphinx_docstring` (Impact: 16.5)
  * `test_sphinx_deprecated_class_method__war` (Impact: 9.3)
    * *Intent:* # noinspection PyShadowingNames def test_sphinx_deprecated_static_method__warns(sphinx_deprecated_st...
  * `test_sphinx_deprecated_function__warns` (Impact: 5.6)
  * `test_sphinx_deprecated_static_method__wa` (Impact: 5.6)
    * *Intent:* # noinspection PyShadowingNames def test_sphinx_deprecated_method__warns(sphinx_deprecated_method): ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 119`, `args: 34`, `func_start: 33`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 14`, `duplicate_logic: 7`, `orphaned_logic: 15`
* *Architecture:* `io: 3`, `api: 39`, `import: 7`
* *Defense:* `safety: 44`, `doc: 20`, `test: 70`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, pytest, warnings, re, sys, deprecated.sphinx, textwrap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/deprecated/classic.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.925 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.354 IQR)
- **Top Global Matches:** file_cluster_13: 11.925, file_cluster_8: 12.205, file_cluster_12: 12.298
- **Magnitude:** 111.38 | **LOC:** 302 | **CtrlFlow:** 53.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.9696%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_deprecated_msg` (Impact: 24.9)
  * `__call__` (Impact: 21.1)
  * `deprecated` (Impact: 11.2)
  * `wrapped_cls` (Impact: 10.7)
  * `wrapper_function` (Impact: 9.4)
    * *Intent:* """ Construct a wrapper adapter. :type reason: str :param reason: Reason message which documents the...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 27`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 3`, `doc: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 231.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.333333
  * `Imports (Out-Degree: 0):` functools, warnings, inspect, deprecated, deprecated.classic, platform, wrapt._wrappers, wrapt
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `deprecated-1.3.1/tests/test_deprecated_metaclass.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.198 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.911 IQR)
- **Top Global Matches:** file_cluster_0: 12.198, file_cluster_13: 12.417, file_cluster_8: 12.461
- **Magnitude:** 65.34 | **LOC:** 116 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.5477%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_with_singleton_metaclass` (Impact: 6.6)
  * `test_with_metaclass` (Impact: 4.6)
  * `test_with_new` (Impact: 4.5)
  * `test_with_init` (Impact: 4.2)
  * `__call__` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 52`, `args: 14`, `func_start: 14`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 8`, `duplicate_logic: 8`, `orphaned_logic: 4`
* *Architecture:* `api: 12`, `import: 2`
* *Defense:* `safety: 15`, `doc: 2`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` warnings, deprecated.classic
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/test_sphinx_metaclass.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.198 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.911 IQR)
- **Top Global Matches:** file_cluster_0: 12.198, file_cluster_13: 12.417, file_cluster_8: 12.461
- **Magnitude:** 65.34 | **LOC:** 116 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.5477%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_with_singleton_metaclass` (Impact: 6.6)
  * `test_with_metaclass` (Impact: 4.6)
  * `test_with_new` (Impact: 4.5)
  * `test_with_init` (Impact: 4.2)
  * `__call__` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 52`, `args: 14`, `func_start: 14`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 8`, `duplicate_logic: 8`, `orphaned_logic: 4`
* *Architecture:* `api: 12`, `import: 2`
* *Defense:* `safety: 15`, `doc: 2`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` warnings, deprecated.sphinx
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/test_deprecated_class.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.874 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.97 IQR)
- **Top Global Matches:** file_cluster_0: 11.874, file_cluster_8: 12.008, file_cluster_13: 12.047
- **Magnitude:** 61.08 | **LOC:** 156 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.8601%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_class_deprecation_using_deprecated_` (Impact: 4.3)
  * `test_subclass_deprecation_using_deprecat` (Impact: 4.3)
  * `test_simple_class_deprecation_with_args` (Impact: 4.2)
  * `test_class_respect_global_filter` (Impact: 4.0)
  * `test_class_deprecation_using_wrapper` (Impact: 3.1)
    * *Intent:* # stream is used to store the deprecation message for testing stream = io.StringIO() class MyBaseCla...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 70`, `args: 12`, `func_start: 12`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1`, `duplicate_logic: 2`, `orphaned_logic: 7`
* *Architecture:* `api: 22`, `import: 5`
* *Defense:* `safety: 29`, `test: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, warnings, inspect, deprecated.classic, io
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/deprecated/sphinx.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.352 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.076 IQR)
- **Top Global Matches:** file_cluster_13: 11.352, file_cluster_8: 11.356, file_cluster_7: 11.41
- **Magnitude:** 59.98 | **LOC:** 282 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.7398%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__call__` (Impact: 29.8)
  * `deprecated` (Impact: 2.7)
    * *Intent:* # -- build the directive division
  * `get_deprecated_msg` (Impact: 2.5)
  * `versionadded` (Impact: 2.5)
  * `versionchanged` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 20`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `doc: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 143.787
  * `Choke Point (Betweenness):` 0.013158 | `Ripple Effect (Closeness):` 0.25
  * `Imports (Out-Degree: 1):` re, deprecated.classic, textwrap
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `deprecated-1.3.1/tests/test_sphinx_class.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.396 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.128 IQR)
- **Top Global Matches:** file_cluster_0: 11.396, file_cluster_13: 11.803, file_cluster_8: 11.854
- **Magnitude:** 49.24 | **LOC:** 150 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.1639%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_class_deprecation_using_deprecated_` (Impact: 4.3)
  * `test_subclass_deprecation_using_deprecat` (Impact: 4.3)
  * `test_class_deprecation_using_a_simple_de` (Impact: 3.1)
    * *Intent:* # stream is used to store the deprecation message for testing stream = io.StringIO() # To deprecated...
  * `test_isinstance_versionadded` (Impact: 2.4)
    * *Intent:* # https://github.com/laurent-laporte-pro/deprecated/issues/48 @deprecated.sphinx.versionadded(versio...
  * `test_isinstance_versionchanged` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 65`, `args: 9`, `func_start: 9`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 13`, `orphaned_logic: 7`
* *Architecture:* `io: 6`, `api: 22`, `import: 7`
* *Defense:* `safety: 30`, `test: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` __future__, pytest, warnings, inspect, sys, deprecated.sphinx, io
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/deprecated/params.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.717 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.683 IQR)
- **Top Global Matches:** file_cluster_13: 11.717, file_cluster_17: 12.157, file_cluster_0: 12.212
- **Magnitude:** 43.84 | **LOC:** 80 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.3473%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `populate_messages` (Impact: 10.4)
  * `check_params` (Impact: 6.9)
  * `__call__` (Impact: 4.0)
  * `warn_messages` (Impact: 3.7)
  * `wrapper` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 16`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 5`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `safety: 4`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 132.147
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.25
  * `Imports (Out-Degree: 0):` functools, warnings, inspect, collections, inspect2
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `deprecated-1.3.1/tests/deprecated_params/test_demo_area.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.356 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.112 IQR)
- **Top Global Matches:** file_cluster_8: 8.356, file_cluster_13: 8.653, file_cluster_0: 8.945
- **Magnitude:** 20.42 | **LOC:** 63 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.9038%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `area` (Impact: 9.4)
  * `test_area` (Impact: 6.3)
  * `_area_impl` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 13`, `args: 3`, `func_start: 3`
* *Risk/State:* `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 1`, `doc: 2`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` warnings, deprecated.params, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/deprecated_params/test_demo_versions.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.932 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.058 IQR)
- **Top Global Matches:** file_cluster_13: 9.932, file_cluster_8: 9.991, file_cluster_0: 10.086
- **Magnitude:** 20.12 | **LOC:** 46 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.188%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `integrate` (Impact: 10.8)
  * `test_only_one_warning_for_each_parameter` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 10`, `args: 3`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 1`, `doc: 4`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` warnings, deprecated.params
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/test_sphinx_adapter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.301 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.353 IQR)
- **Top Global Matches:** file_cluster_8: 9.301, file_cluster_13: 9.394, file_cluster_7: 9.637
- **Magnitude:** 19.12 | **LOC:** 129 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_sphinx_adapter` (Impact: 2.9)
  * `test_sphinx_adapter__empty_docstring` (Impact: 2.7)
  * `test_decorator_accept_line_length` (Impact: 2.5)
  * `foo` (Impact: 1.8)
  * `foo` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 21`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 3`, `doc: 13`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deprecated.sphinx, textwrap, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/setup.py` (PYTHON | Tier 1 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.595 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.732 IQR)
- **Top Global Matches:** file_cluster_8: 6.595, file_cluster_7: 7.221, file_cluster_1: 7.395
- **Magnitude:** 16.16 | **LOC:** 200 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.0194%), Tech Debt (72.0768%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`
* *Risk/State:* `fragile_debt: 1`
* *Architecture:* `import: 1`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deprecated, setuptools, deprecated.sphinx
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/deprecated/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.09 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 7.291 IQR)
- **Top Global Matches:** file_cluster_13: 8.09, file_cluster_8: 8.483, file_cluster_7: 8.757
- **Magnitude:** 13.12 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* None
* *Architecture:* `import: 2`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` deprecated.params, deprecated.classic
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/deprecated_params/test_demo_paragraph.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.264 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.559 IQR)
- **Top Global Matches:** file_cluster_13: 9.264, file_cluster_8: 9.455, file_cluster_0: 9.709
- **Magnitude:** 12.16 | **LOC:** 67 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.5899%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `paragraph` (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 11`, `args: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`
* *Architecture:* `io: 1`, `api: 2`, `import: 5`
* *Defense:* `safety: 1`, `doc: 8`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` deprecated.params, pytest, warnings, xml.sax.saxutils, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/deprecated_params/test_demo_pow2.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.86%)
- **Global Archetype:** `file_cluster_13` (Drift: 8.972 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.559 IQR)
- **Top Global Matches:** file_cluster_13: 8.972, file_cluster_8: 9.035, file_cluster_0: 9.296
- **Magnitude:** 11.14 | **LOC:** 59 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.174%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_pow2` (Impact: 6.3)
  * `pow2` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 10`, `args: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 2`, `import: 4`
* *Defense:* `safety: 1`, `doc: 4`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` warnings, deprecated.params, sys, pytest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deprecated-1.3.1/tests/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.581 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
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

### `deprecated-1.3.1/tests/deprecated_params/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.581 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 10.52 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
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

### `deprecated-1.3.1/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.845 IQR)
- **Top Global Matches:** file_cluster_8: 6.845, file_cluster_7: 7.999, file_cluster_1: 8.107
- **Magnitude:** 4.66 | **LOC:** 41 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.4619%), Tech Debt (99.6072%)
**Top Internal Functions/Classes:**
  * `clean-pyc` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 12`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `api: 3`
* *Defense:* `test: 2`, `cleanup: 3`
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

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `deprecated-1.3.1/tests/test_sphinx.py` (PYTHON) | Magnitude: 169.44 | Delta: **0.115 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 232, structural_boundaries: 119, test: 70, safety: 44
- `deprecated-1.3.1/tests/test_deprecated_class.py` (PYTHON) | Magnitude: 61.08 | Delta: **0.134 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 70, safety: 29, test: 28
- `deprecated-1.3.1/tests/test_deprecated_metaclass.py` (PYTHON) | Magnitude: 65.34 | Delta: **0.219 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 52, test: 19, encapsulation: 18
- `deprecated-1.3.1/tests/test_sphinx_metaclass.py` (PYTHON) | Magnitude: 65.34 | Delta: **0.219 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 52, test: 19, encapsulation: 18
- `deprecated-1.3.1/tests/test_deprecated.py` (PYTHON) | Magnitude: 183.3 | Delta: **0.272 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 188, structural_boundaries: 125, test: 55, api: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `deprecated-1.3.1/deprecated/sphinx.py` (PYTHON) | Magnitude: 59.98 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 71, doc: 50, structural_boundaries: 20, branch: 16
- `deprecated-1.3.1/tests/deprecated_params/test_demo_versions.py` (PYTHON) | Magnitude: 20.12 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 10, branch: 5, doc: 4
- `deprecated-1.3.1/tests/deprecated_params/test_demo_pow2.py` (PYTHON) | Magnitude: 11.14 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 10, test: 8, branch: 4
- `deprecated-1.3.1/tests/deprecated_params/test_demo_paragraph.py` (PYTHON) | Magnitude: 12.16 | Delta: **0.191 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 11, doc: 8, test: 7
- `deprecated-1.3.1/deprecated/classic.py` (PYTHON) | Magnitude: 111.38 | Delta: **0.28 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 74, branch: 31, structural_boundaries: 27, doc: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `deprecated-1.3.1/tests/test_sphinx_adapter.py` (PYTHON) | Magnitude: 19.12 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 21, doc: 13, test: 11
- `deprecated-1.3.1/tests/deprecated_params/test_demo_area.py` (PYTHON) | Magnitude: 20.42 | Delta: **0.297 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 13, branch: 10, test: 9
- `deprecated-1.3.1/setup.py` (PYTHON) | Magnitude: 16.16 | Delta: **0.626 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 53, doc: 8, structural_boundaries: 2, vectorized_math: 2

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `deprecated-1.3.1/deprecated/sphinx.py` -> **Severity: 1.287** (Bridge: 0.0132 * Flux: 97.8032%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `deprecated-1.3.1/deprecated/classic.py` -> **Severity: 19.899** (Embedded: 0.3333 * Error Risk: 59.6977%)
- `deprecated-1.3.1/deprecated/sphinx.py` -> **Severity: 13.821** (Embedded: 0.25 * Error Risk: 55.2832%)
- `deprecated-1.3.1/deprecated/params.py` -> **Severity: 13.498** (Embedded: 0.25 * Error Risk: 53.9915%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `deprecated-1.3.1/deprecated/params.py` -> **Severity: 11238.336** (Blast Radius: 132.147 * Doc Risk: 85.0442%)
- `deprecated-1.3.1/deprecated/classic.py` -> **Severity: 2754.591** (Blast Radius: 231.084 * Doc Risk: 11.9203%)
- `deprecated-1.3.1/deprecated/sphinx.py` -> **Severity: 1713.984** (Blast Radius: 143.787 * Doc Risk: 11.9203%)
- `deprecated-1.3.1/Makefile` -> **Severity: 326.473** (Blast Radius: 27.388 * Doc Risk: 11.9203%)
- `deprecated-1.3.1/setup.py` -> **Severity: 326.473** (Blast Radius: 27.388 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
