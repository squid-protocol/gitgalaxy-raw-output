# ARCHITECTURAL_BRIEF: editables
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
| Total Artifacts | 10 |
| Analyzed Artifacts (Scanned) | 7 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3 |
| Total LOC | 297 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 70.0% |
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
| PYTHON | 4 | 297 | 57.1% |
| PLAINTEXT | 2 | 0 | 28.6% |
| MARKDOWN | 1 | 0 | 14.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 4 | 57.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 42.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3*

**Composition by Extension & Reason:**
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 29.2 | 67.4 | 49.8 | 51.3 | 67.4 |
| Guard Balance (formerly Error & Exception Exposure) | 69.8 | 98.4 | 82.6 | 81.1 | 98.4 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.6 | 1.2 | 1.2 | 0.0 |
| Connectivity (formerly API Exposure) | 9.7 | 66.4 | 35.4 | 32.7 | 66.4 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 49.8 | 49.6 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 11 | 3 | 4 | `editables-0.5/tests/test_editable.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 23 | 3 | 10 | `editables-0.5/tests/test_editable.py` |
| danger | 13 | 3 | 2 | `editables-0.5/src/editables/__init__.py` |
| concurrency | 6 | 3 | 2 | `editables-0.5/src/editables/__init__.py` |
| connectivity | 38 | 4 | 11 | `editables-0.5/src/editables/__init__.py` |
| io | 32 | 4 | 12 | `editables-0.5/tests/test_editable.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 2 | 1 | 0 | `editables-0.5/src/editables/__init__.py` |
| events | 0 | 0 | 0 | - |
| tests | 21 | 2 | 6 | `editables-0.5/tests/test_editable.py` |
| docs | 0 | 0 | 0 | - |
| debt | 5 | 2 | 1 | `editables-0.5/tests/test_editable.py` |
| mutation | 126 | 4 | 28 | `editables-0.5/tests/test_editable.py` |
| dead_code | 14 | 2 | 6 | `editables-0.5/tests/test_editable.py` |
| credential | 0 | 0 | 0 | - |
| threat | 4 | 1 | 0 | `editables-0.5/src/editables/redirector.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `editables-0.5/tests/test_editable.py` (Hits: 12)
- `editables-0.5/tests/test_redirects.py` (Hits: 12)
- `editables-0.5/src/editables/__init__.py` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **redirector.py** (`editables-0.5/src/editables/redirector.py`) — 2 inbound connections
2. **LICENSE.txt** (`editables-0.5/LICENSE.txt`) — 0 inbound connections
3. **requirements.txt** (`editables-0.5/tests/requirements.txt`) — 0 inbound connections
4. **README.md** (`editables-0.5/README.md`) — 0 inbound connections
5. **__init__.py** (`editables-0.5/src/editables/__init__.py`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_editable.py** (`editables-0.5/tests/test_editable.py`) — 9 outbound dependencies
2. **test_redirects.py** (`editables-0.5/tests/test_redirects.py`) — 7 outbound dependencies
3. **__init__.py** (`editables-0.5/src/editables/__init__.py`) — 6 outbound dependencies
4. **redirector.py** (`editables-0.5/src/editables/redirector.py`) — 6 outbound dependencies
5. **LICENSE.txt** (`editables-0.5/LICENSE.txt`) — 0 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `map` (@ `editables-0.5/src/editables/__init__.py`) -> Impact: **12.6** | LOC: 12
- `import_state` (@ `editables-0.5/tests/test_editable.py`) -> Impact: **8.1** | LOC: 21
  * *Intent:* # to test in-process: # Put stuff in somedir # sys.path.append("somedir") # site.addsitedir("somedir") # Check stuff is visible
- `build_project` (@ `editables-0.5/tests/test_editable.py`) -> Impact: **7.5** | LOC: 11
- `find_spec` (@ `editables-0.5/src/editables/redirector.py`) -> Impact: **7.4** | LOC: 13
- `build` (@ `editables-0.5/tests/test_redirects.py`) -> Impact: **7.3** | LOC: 8
- `files` (@ `editables-0.5/src/editables/__init__.py`) -> Impact: **6.0** | LOC: 7
- `install` (@ `editables-0.5/src/editables/redirector.py`) -> Impact: **6.0** | LOC: 6
- `save_import_state` (@ `editables-0.5/tests/test_redirects.py`) -> Impact: **5.0** | LOC: 19
- `pth_file` (@ `editables-0.5/src/editables/__init__.py`) -> Impact: **4.6** | LOC: 7
- `__init__` (@ `editables-0.5/src/editables/__init__.py`) -> Impact: **4.5** | LOC: 9

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `editables-0.5/tests` | 3 | 181.58 | 23.66% | 0.0% |
| `editables-0.5/src/editables` | 2 | 138.96 | 64.12% | 0.0% |
| `editables-0.5` | 2 | 2.28 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `editables-0.5/src/editables/__init__.py` -> **100.0%** Exposure
- `editables-0.5/src/editables/redirector.py` -> **99.1837%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `editables-0.5/tests/test_editable.py` -> **8** Orphaned Functions | **0** Duplicates
- `editables-0.5/tests/test_redirects.py` -> **6** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `28` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `editables-0.5/src/editables/__init__.py` (PYTHON) -> Cumulative Risk: **584.81**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 107.04 | **LOC:** 103 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.4393%)
- **Heaviest Functions:** `map` (Impact: 12.6), `files` (Impact: 6.0), `pth_file` (Impact: 4.6)

### 2. `editables-0.5/src/editables/redirector.py` (PYTHON) -> Cumulative Risk: **546.33**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 31.92 | **LOC:** 48 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.1837%), Safety Score (78.3421%)
- **Heaviest Functions:** `find_spec` (Impact: 7.4), `install` (Impact: 6.0), `map_module` (Impact: 2.1)

### 3. `editables-0.5/tests/test_editable.py` (PYTHON) -> Cumulative Risk: **372.86**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 122.46 | **LOC:** 163 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (83.9185%), Stability (50.0%)
- **Heaviest Functions:** `import_state` (Impact: 8.1), `build_project` (Impact: 7.5), `test_simple_pth` (Impact: 4.0)

### 4. `editables-0.5/tests/test_redirects.py` (PYTHON) -> Cumulative Risk: **371.26**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 58.12 | **LOC:** 92 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (69.7877%), Stability (50.0%)
- **Heaviest Functions:** `build` (Impact: 7.3), `save_import_state` (Impact: 5.0), `test_redirects` (Impact: 2.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `editables-0.5/tests/test_editable.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 122.46 | **LOC:** 163 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.1972%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `import_state` (Impact: 8.1)
    * *Intent:* # to test in-process: # Put stuff in somedir # sys.path.append("somedir") # site.addsitedir("somedir...
  * `build_project` (Impact: 7.5)
  * `test_simple_pth` (Impact: 4.0)
  * `test_make_project` (Impact: 4.0)
  * `test_subpackage_pth` (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 36`, `args: 11`, `func_start: 11`
* *Risk/State:* `state_mutation: 33`, `fragile_debt: 1`, `unreferenced_by_name: 8`
* *Architecture:* `io: 12`, `api: 11`, `import: 10`
* *Defense:* `safety: 11`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 114.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` a.b.foo, contextlib, editables, foo, os, pathlib, pytest, site...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editables-0.5/src/editables/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 107.04 | **LOC:** 103 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.4207%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `map` (Impact: 12.6)
  * `files` (Impact: 6.0)
  * `pth_file` (Impact: 4.6)
  * `__init__` (Impact: 4.5)
  * `bootstrap_file` (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 33`, `args: 12`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 19`
* *Architecture:* `io: 6`, `api: 14`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 114.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` editables.redirector, name, os, pathlib, re, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editables-0.5/tests/test_redirects.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 58.12 | **LOC:** 92 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.7742%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `build` (Impact: 7.3)
  * `save_import_state` (Impact: 5.0)
  * `test_redirects` (Impact: 2.7)
  * `test_double_install` (Impact: 1.3)
  * `test_cache_invalidation` (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 27`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 16`, `fragile_debt: 1`, `unreferenced_by_name: 6`
* *Architecture:* `io: 12`, `api: 8`, `import: 7`
* *Defense:* `safety: 10`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 114.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` contextlib, editables.redirector, importlib, mod, pkg, pkg.sub, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editables-0.5/src/editables/redirector.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 31.92 | **LOC:** 48 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.8259%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `find_spec` (Impact: 7.4)
  * `install` (Impact: 6.0)
  * `map_module` (Impact: 2.1)
  * `invalidate_caches` (Impact: 1.7)
    * *Intent:* # importlib.invalidate_caches calls finders' invalidate_caches methods, # and since we install this ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 19`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 5`
* *Architecture:* `io: 2`, `api: 5`, `import: 6`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 310.345
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.333333
  * `Imports (Out-Degree: 0):` importlib.abc, importlib.machinery, importlib.util, sys, types, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `editables-0.5/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.28 | **LOC:** 64 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 114.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editables-0.5/LICENSE.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 19 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 114.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editables-0.5/tests/requirements.txt` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 6 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 114.942
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

- `editables-0.5/src/editables/redirector.py` -> **Severity: 26.114** (Embedded: 0.3333 * Error Risk: 78.3421%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `editables-0.5/src/editables/redirector.py` -> **Severity: 31034.5** (Blast Radius: 310.345 * Doc Risk: 100.0%)
- `editables-0.5/src/editables/__init__.py` -> **Severity: 11494.2** (Blast Radius: 114.942 * Doc Risk: 100.0%)
- `editables-0.5/tests/test_editable.py` -> **Severity: 11494.2** (Blast Radius: 114.942 * Doc Risk: 100.0%)
- `editables-0.5/tests/test_redirects.py` -> **Severity: 11494.2** (Blast Radius: 114.942 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
