# ARCHITECTURAL_BRIEF: mdurl
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
| Total Artifacts | 11 |
| Analyzed Artifacts (Scanned) | 7 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4 |
| Total LOC | 342 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 63.6% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0714 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.7303 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 6 | 342 | 85.7% |
| MARKDOWN | 1 | 0 | 14.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 29%, Generic / Templated Code Files 29%, Compute Cores Files 14%, Data / Markup / Trivial 14%, Many-Argument Workhorses Files 14%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 6 | 85.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 14.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 94.4 | 44.9 | 47.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.8 | 70.4 | 81.0 | 62.6 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 13.0 | 2.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 15.5 | 2.7 | 2.3 |
| Connectivity (formerly API Exposure) | 3.5 | 35.6 | 23.9 | 25.3 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 63.5 | 75.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 11.7 | 2.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 83.3 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 66.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 10 | 1 | 0 | `mdurl-0.1.2/src/mdurl/_decode.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 7 | 2 | 1 | `mdurl-0.1.2/src/mdurl/_decode.py` |
| danger | 4 | 2 | 2 | `mdurl-0.1.2/src/mdurl/_decode.py` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 13 | 6 | 3 | `mdurl-0.1.2/src/mdurl/_parse.py` |
| io | 0 | 0 | 0 | - |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 7 | 2 | 1 | `mdurl-0.1.2/src/mdurl/_parse.py` |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 1 | 1 | 0 | `mdurl-0.1.2/src/mdurl/_parse.py` |
| mutation | 217 | 5 | 45 | `mdurl-0.1.2/src/mdurl/_parse.py` |
| dead_code | 2 | 1 | 0 | `mdurl-0.1.2/src/mdurl/_parse.py` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `mdurl-0.1.2/README.md` (Hits: 0)
- `mdurl-0.1.2/src/mdurl/__init__.py` (Hits: 0)
- `mdurl-0.1.2/src/mdurl/_decode.py` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **_url.py** (`mdurl-0.1.2/src/mdurl/_url.py`) — 3 inbound connections
2. **_decode.py** (`mdurl-0.1.2/src/mdurl/_decode.py`) — 1 inbound connections
3. **_encode.py** (`mdurl-0.1.2/src/mdurl/_encode.py`) — 1 inbound connections
4. **_format.py** (`mdurl-0.1.2/src/mdurl/_format.py`) — 1 inbound connections
5. **_parse.py** (`mdurl-0.1.2/src/mdurl/_parse.py`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`mdurl-0.1.2/src/mdurl/__init__.py`) — 5 outbound dependencies
2. **_decode.py** (`mdurl-0.1.2/src/mdurl/_decode.py`) — 4 outbound dependencies
3. **_encode.py** (`mdurl-0.1.2/src/mdurl/_encode.py`) — 4 outbound dependencies
4. **_parse.py** (`mdurl-0.1.2/src/mdurl/_parse.py`) — 4 outbound dependencies
5. **_format.py** (`mdurl-0.1.2/src/mdurl/_format.py`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `parse` **(Many-Argument Workhorses)** (@ `mdurl-0.1.2/src/mdurl/_parse.py`) -> Impact: **112.5** | LOC: 169
- `repl_func_with_cache` **(Defensive Guards)** (@ `mdurl-0.1.2/src/mdurl/_decode.py`) -> Impact: **32.7** | LOC: 66
- `encode` **(Many-Argument Workhorses)** (@ `mdurl-0.1.2/src/mdurl/_encode.py`) -> Impact: **32.0** | LOC: 41
  * *Intent:* # Encode unsafe characters with percent-encoding, skipping already # encoded sequences. # # - string - string to encode # - exclude - list of characte...
- `format` **(Compute Cores)** (@ `mdurl-0.1.2/src/mdurl/_format.py`) -> Impact: **22.2** | LOC: 19
- `get_encode_cache` **(Compute Cores)** (@ `mdurl-0.1.2/src/mdurl/_encode.py`) -> Impact: **9.5** | LOC: 20
  * *Intent:* # Create a lookup array where anything but characters in `chars` string # and alphanumeric chars is percent-encoded.
- `parse_host` **(Generic / Templated Code)** (@ `mdurl-0.1.2/src/mdurl/_parse.py`) -> Impact: **7.4** | LOC: 9
- `get_decode_cache` **(Generic / Templated Code)** (@ `mdurl-0.1.2/src/mdurl/_decode.py`) -> Impact: **6.5** | LOC: 16
- `url_parse` **(Defensive Guards)** (@ `mdurl-0.1.2/src/mdurl/_parse.py`) -> Impact: **3.9** | LOC: 8
- `decode` **(Generic / Templated Code)** (@ `mdurl-0.1.2/src/mdurl/_decode.py`) -> Impact: **1.9** | LOC: 4
  * *Intent:* # Decode percent-encoded string. #
- `__init__` **(Generic / Templated Code)** (@ `mdurl-0.1.2/src/mdurl/_parse.py`) -> Impact: **1.9** | LOC: 9

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Generic / Templated Code**: generic / type-parameterized (templated) function
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `mdurl-0.1.2/src/mdurl` | 6 | 582.34 | 44.89% | 2.16% |
| `mdurl-0.1.2` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `mdurl-0.1.2/src/mdurl/_parse.py` -> **12.957%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `mdurl-0.1.2/src/mdurl/_decode.py` -> **100.0%** Exposure
- `mdurl-0.1.2/src/mdurl/_encode.py` -> **100.0%** Exposure
- `mdurl-0.1.2/src/mdurl/_parse.py` -> **100.0%** Exposure
- `mdurl-0.1.2/src/mdurl/_format.py` -> **50.0%** Exposure
- `mdurl-0.1.2/src/mdurl/__init__.py` -> **31.0026%** Exposure

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
- **Unknown Dependencies:** `22` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `mdurl-0.1.2/src/mdurl/_parse.py` (PYTHON) -> Cumulative Risk: **684.58**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +1.54)
- **Magnitude:** 333.06 | **LOC:** 305 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.8366%)
- **Heaviest Functions:** `parse` (Many-Argument Workhorses, Impact: 112.5), `parse_host` (Generic / Templated Code, Impact: 7.4), `url_parse` (Defensive Guards, Impact: 3.9)

### 2. `mdurl-0.1.2/src/mdurl/_decode.py` (PYTHON) -> Cumulative Risk: **558.56**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.70)
- **Magnitude:** 108.56 | **LOC:** 105 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.0838%)
- **Heaviest Functions:** `repl_func_with_cache` (Defensive Guards, Impact: 32.7), `get_decode_cache` (Generic / Templated Code, Impact: 6.5), `decode` (Generic / Templated Code, Impact: 1.9)

### 3. `mdurl-0.1.2/src/mdurl/_encode.py` (PYTHON) -> Cumulative Risk: **558.27**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +1.72)
- **Magnitude:** 79.6 | **LOC:** 86 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.3403%)
- **Heaviest Functions:** `encode` (Many-Argument Workhorses, Impact: 32.0), `get_encode_cache` (Compute Cores, Impact: 9.5)

### 4. `mdurl-0.1.2/src/mdurl/_format.py` (PYTHON) -> Cumulative Risk: **408.41**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z -0.16)
- **Magnitude:** 26.56 | **LOC:** 28 | **CtrlFlow:** 83.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (64.5656%), State Flux (50.0%)
- **Heaviest Functions:** `format` (Compute Cores, Impact: 22.2)

### 5. `mdurl-0.1.2/src/mdurl/_url.py` (PYTHON) -> Cumulative Risk: **174.81**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Declarative / Non-Code` (z +0.45)
- **Magnitude:** 16.22 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (50.0%), Api Exposure (22.517%), Verification (2.2977%)

### 6. `mdurl-0.1.2/src/mdurl/__init__.py` (PYTHON) -> Cumulative Risk: **149.41**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Declarative / Non-Code` (z +0.45)
- **Magnitude:** 18.34 | **LOC:** 19 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Safety Score (62.5811%), Stability (50.0%), State Flux (31.0026%), Api Exposure (3.5258%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `mdurl-0.1.2/src/mdurl/_parse.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 333.06 | **LOC:** 305 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.4152%), Tech Debt (12.957%)
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 112.5)
  * `parse_host` **(Generic / Templated Code)** (Impact: 7.4)
  * `url_parse` **(Defensive Guards)** (Impact: 3.9)
  * `__init__` **(Generic / Templated Code)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 199
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 18`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 75`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 118.914
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.166667
  * `Imports (Out-Degree: 1):` __future__, collections, mdurl._url, re
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mdurl-0.1.2/src/mdurl/_decode.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 108.56 | **LOC:** 105 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.9061%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `repl_func_with_cache` **(Defensive Guards)** (Impact: 32.7)
  * `get_decode_cache` **(Generic / Templated Code)** (Impact: 6.5)
  * `decode` **(Generic / Templated Code)** (Impact: 1.9)
    * *Intent:* # Decode percent-encoded string. #
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 17`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 23`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 118.914
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.166667
  * `Imports (Out-Degree: 0):` __future__, collections.abc, functools, re
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mdurl-0.1.2/src/mdurl/_encode.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 79.6 | **LOC:** 86 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.9283%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `encode` **(Many-Argument Workhorses)** (Impact: 32.0)
    * *Intent:* # Encode unsafe characters with percent-encoding, skipping already # encoded sequences. # # - string...
  * `get_encode_cache` **(Compute Cores)** (Impact: 9.5)
    * *Intent:* # Create a lookup array where anything but characters in `chars` string # and alphanumeric chars is ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 18`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 13`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 118.914
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.166667
  * `Imports (Out-Degree: 0):` __future__, collections.abc, string, urllib.parse
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mdurl-0.1.2/src/mdurl/_format.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 26.56 | **LOC:** 28 | **CtrlFlow:** 83.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.0818%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `format` **(Compute Cores)** (Impact: 22.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 8`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 118.914
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.166667
  * `Imports (Out-Degree: 1):` __future__, mdurl._url, typing
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `mdurl-0.1.2/src/mdurl/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 18.34 | **LOC:** 19 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 101.636
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` mdurl._decode, mdurl._encode, mdurl._format, mdurl._parse, mdurl._url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mdurl-0.1.2/src/mdurl/_url.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 16.22 | **LOC:** 15 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 321.07
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.5
  * `Imports (Out-Degree: 0):` __future__, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `mdurl-0.1.2/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 1.0 | **LOC:** 9 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 101.636
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

- `mdurl-0.1.2/src/mdurl/_parse.py` -> **Severity: 16.639** (Embedded: 0.1667 * Error Risk: 99.8366%)
- `mdurl-0.1.2/src/mdurl/_decode.py` -> **Severity: 16.347** (Embedded: 0.1667 * Error Risk: 98.0838%)
- `mdurl-0.1.2/src/mdurl/_encode.py` -> **Severity: 16.223** (Embedded: 0.1667 * Error Risk: 97.3403%)
- `mdurl-0.1.2/src/mdurl/_format.py` -> **Severity: 10.761** (Embedded: 0.1667 * Error Risk: 64.5656%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `mdurl-0.1.2/src/mdurl/_decode.py` -> **Severity: 11891.4** (Blast Radius: 118.914 * Doc Risk: 100.0%)
- `mdurl-0.1.2/src/mdurl/_encode.py` -> **Severity: 11891.4** (Blast Radius: 118.914 * Doc Risk: 100.0%)
- `mdurl-0.1.2/src/mdurl/_format.py` -> **Severity: 11891.4** (Blast Radius: 118.914 * Doc Risk: 100.0%)
- `mdurl-0.1.2/src/mdurl/_parse.py` -> **Severity: 11891.4** (Blast Radius: 118.914 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
