# ARCHITECTURAL_BRIEF: pyasn1
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
| Total Artifacts | 74 |
| Analyzed Artifacts (Scanned) | 68 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6 |
| Total LOC | 13272 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 91.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2383 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0617 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 65 | 13272 | 95.6% |
| MARKDOWN | 2 | 0 | 2.9% |
| PLAINTEXT | 1 | 0 | 1.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Small Flat Repo` (z -0.60; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 37%, Large Core Modules 22%, Defensive Guards Files 19%, Declarative / Non-Code 6%, Interface Declarations Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 65 | 95.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 4.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6*

**Composition by Extension & Reason:**
- `.rst`: 3x Excluded (Unsupported Extension: '.rst')
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 96.6 | 25.0 | 9.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.7 | 47.3 | 54.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 25.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 17.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 60.3 | 8.5 | 7.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 34.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 5.7 | 0.3 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 66.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 59.3 | 84.1 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 947 | 24 | 32 | `pyasn1-0.6.3/tests/codec/ber/test_decoder.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 2433 | 39 | 82 | `pyasn1-0.6.3/tests/type/test_univ.py` |
| danger | 485 | 35 | 14 | `pyasn1-0.6.3/pyasn1/type/univ.py` |
| concurrency | 108 | 6 | 0 | `pyasn1-0.6.3/pyasn1/codec/ber/decoder.py` |
| connectivity | 1985 | 43 | 61 | `pyasn1-0.6.3/tests/type/test_univ.py` |
| io | 76 | 23 | 3 | `pyasn1-0.6.3/tests/codec/ber/test_decoder.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 28 | 2 | 0 | `pyasn1-0.6.3/tests/type/test_useful.py` |
| serialization | 32 | 3 | 0 | `pyasn1-0.6.3/tests/type/test_univ.py` |
| regex | 0 | 0 | 0 | - |
| events | 8 | 2 | 0 | `pyasn1-0.6.3/pyasn1/debug.py` |
| tests | 109 | 26 | 3 | `pyasn1-0.6.3/tests/type/test_univ.py` |
| docs | 171 | 19 | 7 | `pyasn1-0.6.3/pyasn1/type/univ.py` |
| debt | 211 | 23 | 8 | `pyasn1-0.6.3/pyasn1/type/univ.py` |
| mutation | 4644 | 51 | 223 | `pyasn1-0.6.3/pyasn1/codec/ber/decoder.py` |
| dead_code | 539 | 37 | 19 | `pyasn1-0.6.3/tests/codec/ber/test_decoder.py` |
| credential | 0 | 0 | 0 | - |
| threat | 97 | 20 | 3 | `pyasn1-0.6.3/pyasn1/type/univ.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.7425**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pyasn1-0.6.3/tests/codec/ber/test_decoder.py` (Hits: 19)
- `pyasn1-0.6.3/pyasn1/codec/ber/decoder.py` (Hits: 12)
- `pyasn1-0.6.3/pyasn1/codec/streaming.py` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **base.py** (`pyasn1-0.6.3/tests/base.py`) — 18 inbound connections
2. **error.py** (`pyasn1-0.6.3/pyasn1/error.py`) — 13 inbound connections
3. **streaming.py** (`pyasn1-0.6.3/pyasn1/codec/streaming.py`) — 2 inbound connections
4. **integer.py** (`pyasn1-0.6.3/pyasn1/compat/integer.py`) — 1 inbound connections
5. **MANIFEST.in** (`pyasn1-0.6.3/MANIFEST.in`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_decoder.py** (`pyasn1-0.6.3/tests/codec/ber/test_decoder.py`) — 12 outbound dependencies
2. **decoder.py** (`pyasn1-0.6.3/pyasn1/codec/ber/decoder.py`) — 10 outbound dependencies
3. **test_univ.py** (`pyasn1-0.6.3/tests/type/test_univ.py`) — 8 outbound dependencies
4. **encoder.py** (`pyasn1-0.6.3/pyasn1/codec/ber/encoder.py`) — 7 outbound dependencies
5. **test_useful.py** (`pyasn1-0.6.3/tests/type/test_useful.py`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__call__` **(Many-Argument Workhorses)** (@ `pyasn1-0.6.3/pyasn1/codec/ber/decoder.py`) -> Impact: **368.9** | LOC: 357
- `indefLenValueDecoder` **(Many-Argument Workhorses)** (@ `pyasn1-0.6.3/pyasn1/codec/ber/decoder.py`) -> Impact: **226.7** | LOC: 234
- `valueDecoder` **(Many-Argument Workhorses)** (@ `pyasn1-0.6.3/pyasn1/codec/ber/decoder.py`) -> Impact: **219.7** | LOC: 220
- `valueDecoder` **(Many-Argument Workhorses)** (@ `pyasn1-0.6.3/pyasn1/codec/ber/decoder.py`) -> Impact: **103.3** | LOC: 105
- `encodeValue` **(Many-Argument Workhorses)** (@ `pyasn1-0.6.3/pyasn1/codec/ber/encoder.py`) -> Impact: **101.3** | LOC: 116
  * *Intent:* # TODO: handling three flavors of input is too much -- split over codecs
- `encodeValue` **(Many-Argument Workhorses)** (@ `pyasn1-0.6.3/pyasn1/codec/ber/encoder.py`) -> Impact: **93.2** | LOC: 100
- `setComponentByPosition` **(Many-Argument Workhorses)** (@ `pyasn1-0.6.3/pyasn1/type/univ.py`) -> Impact: **87.3** | LOC: 106
- `setComponentByPosition` **(Many-Argument Workhorses)** (@ `pyasn1-0.6.3/pyasn1/type/univ.py`) -> Impact: **79.6** | LOC: 110
- `indefLenValueDecoder` **(Many-Argument Workhorses)** (@ `pyasn1-0.6.3/pyasn1/codec/ber/decoder.py`) -> Impact: **70.1** | LOC: 74
- `valueDecoder` **(Many-Argument Workhorses)** (@ `pyasn1-0.6.3/pyasn1/codec/ber/decoder.py`) -> Impact: **64.0** | LOC: 79

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pyasn1-0.6.3/pyasn1/codec/ber` | 4 | 3585.66 | 50.85% | 31.5% |
| `pyasn1-0.6.3/pyasn1/type` | 12 | 3517.18 | 44.98% | 81.33% |
| `pyasn1-0.6.3/tests/type` | 10 | 1984.92 | 13.92% | 0.0% |
| `pyasn1-0.6.3/tests/codec/ber` | 4 | 1982.7 | 4.55% | 0.0% |
| `pyasn1-0.6.3/tests/codec/cer` | 4 | 705.1 | 8.0% | 0.0% |
| `pyasn1-0.6.3/tests/codec/der` | 4 | 552.38 | 7.55% | 0.0% |
| `pyasn1-0.6.3/pyasn1/codec/cer` | 3 | 377.4 | 49.71% | 41.61% |
| `pyasn1-0.6.3/pyasn1/codec/native` | 3 | 310.62 | 56.09% | 39.55% |
| `pyasn1-0.6.3/tests/codec/native` | 4 | 176.8 | 6.85% | 0.0% |
| `pyasn1-0.6.3/pyasn1` | 3 | 165.16 | 33.88% | 32.2% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `pyasn1-0.6.3/pyasn1/type/constraint.py` -> **100.0%** Exposure
- `pyasn1-0.6.3/pyasn1/type/namedval.py` -> **100.0%** Exposure
- `pyasn1-0.6.3/pyasn1/type/tagmap.py` -> **99.9999%** Exposure
- `pyasn1-0.6.3/pyasn1/type/opentype.py` -> **99.9996%** Exposure
- `pyasn1-0.6.3/pyasn1/type/univ.py` -> **99.9956%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `pyasn1-0.6.3/pyasn1/codec/ber/decoder.py` -> **100.0%** Exposure
- `pyasn1-0.6.3/pyasn1/codec/ber/encoder.py` -> **100.0%** Exposure
- `pyasn1-0.6.3/pyasn1/codec/cer/decoder.py` -> **100.0%** Exposure
- `pyasn1-0.6.3/pyasn1/codec/cer/encoder.py` -> **100.0%** Exposure
- `pyasn1-0.6.3/pyasn1/codec/der/decoder.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pyasn1-0.6.3/tests/codec/ber/test_decoder.py` -> **106** Orphaned Functions | **32** Duplicates
- `pyasn1-0.6.3/tests/type/test_univ.py` -> **83** Orphaned Functions | **10** Duplicates
- `pyasn1-0.6.3/pyasn1/type/univ.py` -> **27** Orphaned Functions | **36** Duplicates
- `pyasn1-0.6.3/tests/codec/ber/test_encoder.py` -> **37** Orphaned Functions | **10** Duplicates
- `pyasn1-0.6.3/tests/codec/cer/test_encoder.py` -> **15** Orphaned Functions | **23** Duplicates

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
- **Unknown Dependencies:** `189` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `pyasn1-0.6.3/pyasn1/debug.py` (PYTHON) -> Cumulative Risk: **724.75**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.18)
- **Magnitude:** 133.88 | **LOC:** 147 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (96.6401%)
- **Heaviest Functions:** `__init__` (Many-Argument Workhorses, Impact: 23.6), `__init__` (Many-Argument Workhorses, Impact: 9.8), `setLogger` (Compute Cores, Impact: 9.0)

### 2. `pyasn1-0.6.3/pyasn1/codec/native/encoder.py` (PYTHON) -> Cumulative Risk: **713.32**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.31)
- **Magnitude:** 174.4 | **LOC:** 286 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9985%), Tech Debt (99.9022%)
- **Heaviest Functions:** `__call__` (Defensive Guards, Impact: 15.9), `encode` (Many-Argument Workhorses, Impact: 14.1), `__init__` (Compute Cores, Impact: 11.3)

### 3. `pyasn1-0.6.3/pyasn1/type/namedval.py` (PYTHON) -> Cumulative Risk: **708.82**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.42)
- **Magnitude:** 128.86 | **LOC:** 193 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `__init__` (Many-Argument Workhorses, Impact: 30.5), `__repr__` (Interface Declarations, Impact: 4.6), `getValues` (Defensive Guards, Impact: 3.9)

### 4. `pyasn1-0.6.3/pyasn1/type/base.py` (PYTHON) -> Cumulative Risk: **676.65**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.32)
- **Magnitude:** 416.54 | **LOC:** 700 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9649%), Safety Score (95.8308%)
- **Heaviest Functions:** `subtype` (Many-Argument Workhorses, Impact: 15.3), `__new__` (Compute Cores, Impact: 13.8), `isSameTypeWith` (Many-Argument Workhorses, Impact: 12.3)

### 5. `pyasn1-0.6.3/pyasn1/type/univ.py` (PYTHON) -> Cumulative Risk: **666.68**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.45)
- **Magnitude:** 1893.54 | **LOC:** 3328 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Tech Debt (99.9956%), Safety Score (83.7845%)
- **Heaviest Functions:** `setComponentByPosition` (Many-Argument Workhorses, Impact: 87.3), `setComponentByPosition` (Many-Argument Workhorses, Impact: 79.6), `prettyIn` (Defensive Guards, Impact: 42.7)

### 6. `pyasn1-0.6.3/pyasn1/codec/ber/encoder.py` (PYTHON) -> Cumulative Risk: **660.69**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +1.01)
- **Magnitude:** 1054.2 | **LOC:** 955 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.8486%)
- **Heaviest Functions:** `encodeValue` (Many-Argument Workhorses, Impact: 101.3), `encodeValue` (Many-Argument Workhorses, Impact: 93.2), `encode` (Many-Argument Workhorses, Impact: 62.6)

### 7. `pyasn1-0.6.3/pyasn1/type/useful.py` (PYTHON) -> Cumulative Risk: **659.29**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Parameter Forwarders Files` (z +0.57)
- **Magnitude:** 146.68 | **LOC:** 191 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (95.8309%), Tech Debt (92.7296%)
- **Heaviest Functions:** `asDateTime` (Defensive Guards, Impact: 33.0), `fromDateTime` (Compute Cores, Impact: 17.0), `__init__` (Encapsulated Accessors, Impact: 2.1)

### 8. `pyasn1-0.6.3/pyasn1/type/namedtype.py` (PYTHON) -> Cumulative Risk: **654.73**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.40)
- **Magnitude:** 323.78 | **LOC:** 551 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.553%), Safety Score (91.5375%)
- **Heaviest Functions:** `__init__` (Compute Cores, Impact: 29.0), `__computeTagMaps` (Defensive Guards, Impact: 14.9), `__computeAmbiguousTypes` (Type Conversions, Impact: 10.5)

### 9. `pyasn1-0.6.3/pyasn1/type/tag.py` (PYTHON) -> Cumulative Risk: **637.1**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Parameter Forwarders Files` (z +1.18)
- **Magnitude:** 164.26 | **LOC:** 336 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Tech Debt (99.9922%), Safety Score (89.346%)
- **Heaviest Functions:** `__getitem__` (Compute Cores, Impact: 9.1), `tagExplicitly` (Compute Cores, Impact: 6.3), `__repr__` (Compute Cores, Impact: 6.1)

### 10. `pyasn1-0.6.3/pyasn1/codec/cer/decoder.py` (PYTHON) -> Cumulative Risk: **631.74**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +2.75)
- **Magnitude:** 76.76 | **LOC:** 150 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.4824%)
- **Heaviest Functions:** `valueDecoder` (Many-Argument Workhorses, Impact: 23.5), `__getattr__` (Interface Declarations, Impact: 3.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pyasn1-0.6.3/pyasn1/codec/ber/decoder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2502.46 | **LOC:** 2226 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.8011%), Tech Debt (21.2999%)
**Top Internal Functions/Classes:**
  * `__call__` **(Many-Argument Workhorses)** (Impact: 368.9)
  * `indefLenValueDecoder` **(Many-Argument Workhorses)** (Impact: 226.7)
  * `valueDecoder` **(Many-Argument Workhorses)** (Impact: 219.7)
  * `valueDecoder` **(Many-Argument Workhorses)** (Impact: 103.3)
  * `indefLenValueDecoder` **(Many-Argument Workhorses)** (Impact: 70.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 250 instances
* *State Mutation (weighted view):* 804
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 464`, `structural_boundaries: 195`, `args: 35`, `func_start: 35`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 304`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 3`, `unreferenced_by_name: 4`
* *Architecture:* `io: 12`, `api: 61`, `import: 19`
* *Defense:* `safety: 76`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` io, os, pyasn1, pyasn1.codec.ber, pyasn1.codec.streaming, pyasn1.compat, pyasn1.error, pyasn1.type...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/type/univ.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1893.54 | **LOC:** 3328 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.4408%), Tech Debt (99.9956%)
**Top Internal Functions/Classes:**
  * `setComponentByPosition` **(Many-Argument Workhorses)** (Impact: 87.3)
  * `setComponentByPosition` **(Many-Argument Workhorses)** (Impact: 79.6)
  * `prettyIn` **(Defensive Guards)** (Impact: 42.7)
  * `prettyIn` **(Defensive Guards)** (Impact: 38.3)
  * `getComponentByPosition` **(Many-Argument Workhorses)** (Impact: 29.2)
    * *Intent:* """Returns |ASN.1| type component by index. Equivalent to Python sequence subscription operation (e....
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 158 instances
* *State Mutation (weighted view):* 560
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 356`, `structural_boundaries: 625`, `args: 245`, `func_start: 245`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 244`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 36`, `unreferenced_by_name: 27`
* *Architecture:* `io: 2`, `api: 115`, `import: 11`
* *Defense:* `safety: 115`, `doc: 51`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` math, pyasn1, pyasn1.codec.ber, pyasn1.compat, pyasn1.type, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/tests/type/test_univ.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1316.52 | **LOC:** 2207 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.0493%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testBooleanEvaluation` **(Defensive Guards)** (Impact: 6.2)
  * `testGetItem` **(Defensive Guards)** (Impact: 5.4)
  * `testSetItem` **(Defensive Guards)** (Impact: 5.4)
  * `testComponentConstraintsMatching` **(Defensive Guards)** (Impact: 5.1)
  * `testComponentConstraintsMatching` **(Defensive Guards)** (Impact: 5.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 26 instances
* *Amplified Cascading Flux:* 19 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 342
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 978`, `args: 298`, `func_start: 298`, `class_start: 67`
* *Risk/State:* `safety_bypasses: 42`, `high_risk_execution: 26`, `state_mutation: 304`, `fragile_debt: 16`, `duplicate_logic: 10`, `unreferenced_by_name: 83`
* *Architecture:* `io: 2`, `api: 365`, `import: 14`
* *Defense:* `safety: 585`, `test: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` math, pickle, platform, pyasn1.error, pyasn1.type, sys, tests.base, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/tests/codec/ber/test_decoder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1134.88 | **LOC:** 2339 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.1716%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDefiniteLenNesting` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* """Deeply nested definite-length SEQUENCEs must raise PyAsn1Error."""
  * `testMixedNesting` **(Defensive Guards)** (Impact: 7.7)
    * *Intent:* """Mixed SEQUENCE and SET nesting must be caught."""
  * `testPartialReadingFromNonBlockingStream` **(Defensive Guards)** (Impact: 6.6)
  * `testNestingUnderLimitWorks` **(Defensive Guards)** (Impact: 6.4)
    * *Intent:* """Nesting within the limit must decode successfully."""
  * `testExpectedEoo` **(Defensive Guards)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 847`, `args: 316`, `func_start: 290`, `class_start: 48`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 137`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 32`, `unreferenced_by_name: 106`
* *Architecture:* `io: 19`, `api: 330`, `import: 18`
* *Defense:* `safety: 523`, `doc: 29`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` gzip, io, os, pyasn1, pyasn1.codec, pyasn1.codec.ber, pyasn1.type, sys...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/codec/ber/encoder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1054.2 | **LOC:** 955 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.5993%), Tech Debt (42.4365%)
**Top Internal Functions/Classes:**
  * `encodeValue` **(Many-Argument Workhorses)** (Impact: 101.3)
    * *Intent:* # TODO: handling three flavors of input is too much -- split over codecs
  * `encodeValue` **(Many-Argument Workhorses)** (Impact: 93.2)
  * `encode` **(Many-Argument Workhorses)** (Impact: 62.6)
  * `__call__` **(Many-Argument Workhorses)** (Impact: 43.1)
  * `encodeValue` **(Many-Argument Workhorses)** (Impact: 39.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 136 instances
* *State Mutation (weighted view):* 421
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 121`, `args: 25`, `func_start: 25`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 149`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 34`, `import: 11`
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pyasn1, pyasn1.codec.ber, pyasn1.compat, pyasn1.compat.integer, pyasn1.type, sys, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/tests/codec/ber/test_encoder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 820.66 | **LOC:** 1528 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.0166%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testEmpty` **(Defensive Guards)** (Impact: 3.3)
  * `testEmpty` **(Defensive Guards)** (Impact: 3.3)
  * `testImpossible1` **(Defensive Guards)** (Impact: 3.2)
  * `testImpossible2` **(Defensive Guards)** (Impact: 3.2)
  * `testImpossible3` **(Defensive Guards)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 510`, `args: 231`, `func_start: 231`, `class_start: 49`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 125`, `duplicate_logic: 10`, `unreferenced_by_name: 37`
* *Architecture:* `io: 5`, `api: 270`, `import: 10`
* *Defense:* `safety: 219`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pyasn1.codec.ber, pyasn1.error, pyasn1.type, sys, tests.base, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/tests/codec/cer/test_encoder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 535.96 | **LOC:** 956 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.6318%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testLocalTimezone` **(Defensive Guards)** (Impact: 3.3)
    * *Intent:* # def testExtraZeroInSeconds(self): # try: # assert encoder.encode( # useful.GeneralizedTime('201505...
  * `testMissingTimezone` **(Defensive Guards)** (Impact: 3.3)
  * `testDecimalCommaPoint` **(Defensive Guards)** (Impact: 3.3)
  * `testFractionOfSecond` **(Defensive Guards)** (Impact: 3.3)
  * `testMissingTimezone` **(Defensive Guards)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 176
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 283`, `args: 122`, `func_start: 122`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 174`, `dead_code: 2`, `duplicate_logic: 23`, `unreferenced_by_name: 15`
* *Architecture:* `io: 5`, `api: 125`, `import: 10`
* *Defense:* `safety: 111`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pyasn1.codec.cer, pyasn1.error, pyasn1.type, sys, tests.base, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/type/base.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 416.54 | **LOC:** 700 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.8451%), Tech Debt (99.9649%)
**Top Internal Functions/Classes:**
  * `subtype` **(Many-Argument Workhorses)** (Impact: 15.3)
    * *Intent:* """Create a specialization of |ASN.1| schema or value object. The subtype relationship between ASN.1...
  * `__new__` **(Compute Cores)** (Impact: 13.8)
  * `isSameTypeWith` **(Many-Argument Workhorses)** (Impact: 12.3)
    * *Intent:* """Examine |ASN.1| type for equality with other ASN.1 type. ASN.1 tags (:py:mod:`~pyasn1.type.tag`) ...
  * `__repr__` **(Compute Cores)** (Impact: 12.0)
  * `subtype` **(Many-Argument Workhorses)** (Impact: 11.8)
    * *Intent:* """Create a specialization of |ASN.1| schema object. The `subtype()` method accepts the same set arg...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 128`, `args: 58`, `func_start: 58`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 69`, `dead_code: 1`, `planned_debt: 3`, `unreferenced_by_name: 18`
* *Architecture:* `api: 37`, `import: 5`
* *Defense:* `safety: 4`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1, pyasn1.type, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/tests/codec/der/test_encoder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 346.98 | **LOC:** 666 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.42%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setUp` **(I/O & Config Routines)** (Impact: 2.6)
  * `setUp` **(I/O & Config Routines)** (Impact: 2.6)
  * `testWithUntaggedChoice` **(Defensive Guards)** (Impact: 2.4)
  * `testWithTaggedChoice` **(Defensive Guards)** (Impact: 2.4)
  * `setUp` **(I/O & Config Routines)** (Impact: 2.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 142
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 164`, `args: 68`, `func_start: 68`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 140`, `duplicate_logic: 11`, `unreferenced_by_name: 19`
* *Architecture:* `io: 5`, `api: 71`, `import: 9`
* *Defense:* `safety: 51`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pyasn1.codec.der, pyasn1.error, pyasn1.type, sys, tests.base, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/type/namedtype.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 323.78 | **LOC:** 551 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.5758%), Tech Debt (99.553%)
**Top Internal Functions/Classes:**
  * `__init__` **(Compute Cores)** (Impact: 29.0)
  * `__computeTagMaps` **(Defensive Guards)** (Impact: 14.9)
  * `__computeAmbiguousTypes` **(Type Conversions)** (Impact: 10.5)
  * `__computeTagToPosMap` **(Defensive Guards)** (Impact: 9.2)
  * `__computeMinTagSet` **(Defensive Guards)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 129`, `args: 54`, `func_start: 54`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 52`, `unreferenced_by_name: 18`
* *Architecture:* `io: 1`, `api: 28`, `import: 4`
* *Defense:* `safety: 18`, `doc: 11`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1, pyasn1.type, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/codec/cer/encoder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 290.12 | **LOC:** 332 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.0463%), Tech Debt (25.3592%)
**Top Internal Functions/Classes:**
  * `encodeValue` **(Many-Argument Workhorses)** (Impact: 57.3)
  * `encodeValue` **(Many-Argument Workhorses)** (Impact: 34.6)
    * *Intent:* # CER encoding constraints: # - minutes are mandatory, seconds are optional # - sub-seconds must NOT...
  * `_componentSortKey` **(Compute Cores)** (Impact: 10.7)
    * *Intent:* """Sort SET components by tag Sort regardless of the Choice value (static sort) """
  * `encodeValue` **(Many-Argument Workhorses)** (Impact: 10.6)
  * `encodeValue` **(Many-Argument Workhorses)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 136
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 47`, `args: 9`, `func_start: 8`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 60`, `unreferenced_by_name: 2`
* *Architecture:* `api: 17`, `import: 5`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1, pyasn1.codec.ber, pyasn1.type, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/type/constraint.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 226.9 | **LOC:** 752 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.877%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_testValue` **(Compute Cores)** (Impact: 10.5)
  * `_testValue` **(Defensive Guards)** (Impact: 8.6)
  * `_testValue` **(Defensive Guards)** (Impact: 8.3)
  * `_setValues` **(Defensive Guards)** (Impact: 7.4)
  * `isSuperTypeOf` **(Compute Cores)** (Impact: 7.2)
    * *Intent:* # TODO: fix possible comparison of set vs scalars here return (otherConstraint is self or not self._...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 91`, `args: 46`, `func_start: 46`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 18`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 4`, `unreferenced_by_name: 18`
* *Architecture:* `api: 18`, `import: 2`
* *Defense:* `safety: 8`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/tests/type/test_constraint.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 214.36 | **LOC:** 421 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.1565%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testConst2` **(Defensive Guards)** (Impact: 5.3)
  * `testContains` **(Defensive Guards)** (Impact: 4.6)
  * `testBadVal` **(Defensive Guards)** (Impact: 3.5)
  * `testBadValExtraFields` **(Defensive Guards)** (Impact: 3.5)
  * `testConst1` **(Defensive Guards)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 137`, `args: 50`, `func_start: 50`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 33`, `planned_debt: 1`, `duplicate_logic: 11`, `unreferenced_by_name: 15`
* *Architecture:* `io: 1`, `api: 63`, `import: 5`
* *Defense:* `safety: 106`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pyasn1.type, sys, tests.base, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/tests/codec/der/test_decoder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 178.24 | **LOC:** 410 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.7769%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDefiniteLenNesting` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* """Deeply nested definite-length SEQUENCEs must raise PyAsn1Error."""
  * `testNoRecursionError` **(Defensive Guards)** (Impact: 6.6)
    * *Intent:* """Must raise PyAsn1Error, not RecursionError."""
  * `testDecodeOpenTypesUnknownType` **(Defensive Guards)** (Impact: 3.4)
  * `testDecodeOpenTypesUnknownType` **(Defensive Guards)** (Impact: 3.4)
  * `testIndefMode` **(Defensive Guards)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 138`, `args: 34`, `func_start: 34`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 23`, `duplicate_logic: 4`, `unreferenced_by_name: 4`
* *Architecture:* `io: 3`, `api: 43`, `import: 9`
* *Defense:* `safety: 82`, `doc: 3`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pyasn1.codec.der, pyasn1.error, pyasn1.type, sys, tests.base, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/codec/native/encoder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 174.4 | **LOC:** 286 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.2506%), Tech Debt (99.9022%)
**Top Internal Functions/Classes:**
  * `__call__` **(Defensive Guards)** (Impact: 15.9)
  * `encode` **(Many-Argument Workhorses)** (Impact: 14.1)
  * `__init__` **(Compute Cores)** (Impact: 11.3)
  * `encode` **(Compute Cores)** (Impact: 7.0)
  * `__getattr__` **(Interface Declarations)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 80`, `args: 18`, `func_start: 18`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 25`, `duplicate_logic: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 31`, `import: 10`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collections, pyasn1, pyasn1.compat, pyasn1.type, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/type/tag.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 164.26 | **LOC:** 336 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.4213%), Tech Debt (99.9922%)
**Top Internal Functions/Classes:**
  * `__getitem__` **(Compute Cores)** (Impact: 9.1)
  * `tagExplicitly` **(Compute Cores)** (Impact: 6.3)
    * *Intent:* """Return explicitly tagged *TagSet* Create a new *TagSet* representing callee *TagSet* explicitly t...
  * `__repr__` **(Compute Cores)** (Impact: 6.1)
  * `__getitem__` **(Compute Cores)** (Impact: 5.4)
  * `__init__` **(Encapsulated Accessors)** (Impact: 4.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 79`, `args: 36`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `state_mutation: 28`, `duplicate_logic: 2`, `unreferenced_by_name: 11`
* *Architecture:* `api: 13`, `import: 1`
* *Defense:* `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/type/useful.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 146.68 | **LOC:** 191 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.0927%), Tech Debt (92.7296%)
**Top Internal Functions/Classes:**
  * `asDateTime` **(Defensive Guards)** (Impact: 33.0)
    * *Intent:* """Create :py:class:`datetime.datetime` object from a |ASN.1| object. Returns ------- : new instance...
  * `fromDateTime` **(Compute Cores)** (Impact: 17.0)
    * *Intent:* """Create |ASN.1| object from a :py:class:`datetime.datetime` object. Parameters ---------- dt: :py:...
  * `__init__` **(Encapsulated Accessors)** (Impact: 2.1)
    * *Intent:* # defaulted arguments required # https: // docs.python.org / 2.3 / lib / datetime - tzinfo.html
  * `utcoffset` **(Parameter Forwarders)** (Impact: 1.8)
  * `tzname` **(Parameter Forwarders)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 28`, `args: 6`, `func_start: 6`, `class_start: 5`
* *Risk/State:* `state_mutation: 42`, `unreferenced_by_name: 5`
* *Architecture:* `api: 11`, `import: 5`
* *Defense:* `safety: 6`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` datetime, pyasn1, pyasn1.type
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/tests/codec/cer/test_decoder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 141.98 | **LOC:** 394 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.3503%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDecodeOpenTypesUnknownType` **(Defensive Guards)** (Impact: 3.4)
  * `testDecodeOpenTypesUnknownType` **(Defensive Guards)** (Impact: 3.4)
  * `testIndefLenNesting` **(Defensive Guards)** (Impact: 3.3)
    * *Intent:* """Deeply nested indefinite-length SEQUENCEs must raise PyAsn1Error."""
  * `setUp` **(I/O & Config Routines)** (Impact: 2.3)
  * `setUp` **(I/O & Config Routines)** (Impact: 2.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 138`, `args: 36`, `func_start: 36`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 15`, `planned_debt: 2`, `duplicate_logic: 6`, `unreferenced_by_name: 6`
* *Architecture:* `io: 3`, `api: 46`, `import: 9`
* *Defense:* `safety: 77`, `doc: 3`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pyasn1.codec.cer, pyasn1.error, pyasn1.type, sys, tests.base, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/debug.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 133.88 | **LOC:** 147 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.6401%), Tech Debt (96.614%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 23.6)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 9.8)
    * *Intent:* # noinspection PyShadowingNames
  * `setLogger` **(Compute Cores)** (Impact: 9.0)
  * `hexdump` **(Compute Cores)** (Impact: 5.9)
  * `registerLoggee` **(Parameter Forwarders)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 33`, `args: 15`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 26`, `unreferenced_by_name: 5`
* *Architecture:* `io: 1`, `api: 9`, `import: 4`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` logging, pyasn1, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/type/namedval.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 128.86 | **LOC:** 193 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.4534%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 30.5)
  * `__repr__` **(Interface Declarations)** (Impact: 4.6)
  * `getValues` **(Defensive Guards)** (Impact: 3.9)
  * `__contains__` **(Parameter Forwarders)** (Impact: 3.6)
  * `getName` **(Parameter Forwarders)** (Impact: 3.6)
    * *Intent:* # legacy protocol
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 45`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 15`, `fragile_debt: 1`, `unreferenced_by_name: 20`
* *Architecture:* `api: 9`, `import: 1`
* *Defense:* `safety: 7`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/codec/native/decoder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 125.7 | **LOC:** 245 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.0132%), Tech Debt (18.7625%)
**Top Internal Functions/Classes:**
  * `__call__` **(Defensive Guards)** (Impact: 15.4)
  * `__init__` **(Compute Cores)** (Impact: 11.3)
  * `__call__` **(Many-Argument Workhorses)** (Impact: 7.9)
  * `__call__` **(Many-Argument Workhorses)** (Impact: 7.8)
  * `__call__` **(Many-Argument Workhorses)** (Impact: 5.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 58`, `args: 10`, `func_start: 10`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 25`, `unreferenced_by_name: 1`
* *Architecture:* `api: 8`, `import: 9`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1, pyasn1.compat, pyasn1.type, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/codec/streaming.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 119.8 | **LOC:** 235 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.2379%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `readFromStream` **(Many-Argument Workhorses)** (Impact: 16.4)
    * *Intent:* """Read from the stream. Parameters ---------- substrate: :py:class:`IOBase` Stream to read from. Ke...
  * `peekIntoStream` **(Defensive Guards)** (Impact: 12.1)
    * *Intent:* """Peek into stream. Parameters ---------- substrate: :py:class:`IOBase` Stream to read from. size: ...
  * `asSeekableStream` **(Defensive Guards)** (Impact: 10.2)
    * *Intent:* """Convert object to seekable byte-stream. Parameters ---------- substrate: :py:class:`bytes` or :py...
  * `isEndOfStream` **(Compute Cores)** (Impact: 8.6)
    * *Intent:* """Check whether we have reached the end of a stream. Although it is more effective to read and catc...
  * `read` **(Compute Cores)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 33`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `io: 6`, `api: 13`, `import: 4`
* *Defense:* `safety: 9`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.24
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.029851
  * `Imports (Out-Degree: 0):` io, os, pyasn1, pyasn1.type
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyasn1-0.6.3/tests/type/test_useful.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 112.3 | **LOC:** 167 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.6723%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` **(Encapsulated Accessors)** (Impact: 2.1)
  * `utcoffset` **(Parameter Forwarders)** (Impact: 1.8)
  * `tzname` **(Parameter Forwarders)** (Impact: 1.8)
  * `dst` **(Parameter Forwarders)** (Impact: 1.8)
  * `testSchemaPickling` **(Defensive Guards)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 1 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 89`, `args: 32`, `func_start: 32`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 4`, `state_mutation: 20`, `unreferenced_by_name: 16`
* *Architecture:* `io: 1`, `api: 37`, `import: 7`
* *Defense:* `safety: 34`, `doc: 5`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` copy, datetime, pickle, pyasn1.type, sys, tests.base, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/pyasn1/type/char.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 101.06 | **LOC:** 289 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.6879%), Tech Debt (83.69%)
**Top Internal Functions/Classes:**
  * `prettyIn` **(Defensive Guards)** (Impact: 11.3)
  * `prettyPrint` **(Parameter Forwarders)** (Impact: 3.9)
    * *Intent:* # first see if subclass has its own .prettyOut() value = self.prettyOut(self._value) if value is not...
  * `__bytes__` **(Defensive Guards)** (Impact: 1.8)
  * `asOctets` **(Type Conversions)** (Impact: 1.8)
  * `asNumbers` **(Type Conversions)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 48`, `args: 8`, `func_start: 8`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 51`, `unreferenced_by_name: 5`
* *Architecture:* `api: 20`, `import: 4`
* *Defense:* `safety: 7`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1, pyasn1.type, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1-0.6.3/tests/type/test_char.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 99.94 | **LOC:** 159 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.1918%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testSizeConstraint` **(Defensive Guards)** (Impact: 3.5)
  * `testEmpty` **(Defensive Guards)** (Impact: 3.2)
  * `testSchemaPickling` **(Defensive Guards)** (Impact: 1.8)
  * `setUp` **(Type Conversions)** (Impact: 1.7)
  * `testInit` **(Defensive Guards)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 75`, `args: 20`, `func_start: 20`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 31`, `unreferenced_by_name: 20`
* *Architecture:* `io: 1`, `api: 26`, `import: 8`
* *Defense:* `safety: 35`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.534
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` pickle, pyasn1.error, pyasn1.type, sys, tests.base, unittest
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

- `pyasn1-0.6.3/pyasn1/error.py` -> **Severity: 10.614** (Embedded: 0.194 * Error Risk: 54.7004%)
- `pyasn1-0.6.3/pyasn1/codec/streaming.py` -> **Severity: 2.26** (Embedded: 0.0299 * Error Risk: 75.72%)
- `pyasn1-0.6.3/pyasn1/compat/integer.py` -> **Severity: 0.964** (Embedded: 0.0149 * Error Risk: 64.5656%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pyasn1-0.6.3/tests/base.py` -> **Severity: 13407.9** (Blast Radius: 134.079 * Doc Risk: 100.0%)
- `pyasn1-0.6.3/pyasn1/error.py` -> **Severity: 4007.95** (Blast Radius: 80.159 * Doc Risk: 50.0%)
- `pyasn1-0.6.3/pyasn1/compat/integer.py` -> **Severity: 2133.8** (Blast Radius: 21.338 * Doc Risk: 100.0%)
- `pyasn1-0.6.3/pyasn1/codec/streaming.py` -> **Severity: 1530.666** (Blast Radius: 26.24 * Doc Risk: 58.3333%)
- `pyasn1-0.6.3/pyasn1/codec/ber/encoder.py` -> **Severity: 1153.4** (Blast Radius: 11.534 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
