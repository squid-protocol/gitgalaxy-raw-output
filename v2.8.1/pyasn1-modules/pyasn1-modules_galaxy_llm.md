# ARCHITECTURAL_BRIEF: pyasn1-modules
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
| Total Artifacts | 280 |
| Analyzed Artifacts (Scanned) | 276 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4 |
| Total LOC | 21939 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 98.6% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2083 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.1429 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 271 | 21939 | 98.2% |
| PLAINTEXT | 4 | 0 | 1.4% |
| MARKDOWN | 1 | 0 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Small Flat Repo` (z +0.16; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 43%, Interface Declarations Files 19%, Large Core Modules 16%, Compute Cores Files 10%, Data / Markup / Trivial 5%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 271 | 98.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 1.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4*

**Composition by Extension & Reason:**
- `no_extension`: 1x Unsupported Format (.undeterminable)
- `.py`: 1x Excluded (Machine-Generated Source Code Signature: 37 LOC)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 90.2 | 11.5 | 8.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.4 | 82.1 | 82.4 | 81.1 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.8 | 1.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.5 | 1.1 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 90.6 | 6.5 | 6.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 48.3 | 31.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 6.6 | 0.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 87.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 52.8 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 109 | 59 | 1 | `pyasn1_modules-0.4.2/pyasn1_modules/rfc2985.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 185 | 107 | 2 | `pyasn1_modules-0.4.2/pyasn1_modules/rfc7292.py` |
| danger | 1402 | 212 | 9 | `pyasn1_modules-0.4.2/pyasn1_modules/rfc3280.py` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 2206 | 237 | 17 | `pyasn1_modules-0.4.2/pyasn1_modules/rfc2459.py` |
| io | 264 | 138 | 2 | `pyasn1_modules-0.4.2/tools/snmpget.py` |
| crypto | 1 | 1 | 0 | `pyasn1_modules-0.4.2/tools/ocspclient.py` |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 0 | 0 | 0 | - |
| tests | 740 | 124 | 7 | `pyasn1_modules-0.4.2/tests/test_rfc3279.py` |
| docs | 192 | 124 | 2 | `pyasn1_modules-0.4.2/pyasn1_modules/rfc4210.py` |
| debt | 121 | 42 | 2 | `pyasn1_modules-0.4.2/tools/cmcdump.py` |
| mutation | 11280 | 269 | 95 | `pyasn1_modules-0.4.2/pyasn1_modules/rfc2459.py` |
| dead_code | 229 | 97 | 3 | `pyasn1_modules-0.4.2/tools/ocspclient.py` |
| credential | 9 | 7 | 0 | `pyasn1_modules-0.4.2/tools/ocspclient.py` |
| threat | 3 | 3 | 0 | `pyasn1_modules-0.4.2/tests/test_rfc2876.py` |
| ml_ai | 6 | 4 | 0 | `pyasn1_modules-0.4.2/tests/test_rfc2985.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pyasn1_modules-0.4.2/tools/snmpget.py` (Hits: 6)
- `pyasn1_modules-0.4.2/tools/cmpdump.py` (Hits: 3)
- `pyasn1_modules-0.4.2/tools/crmfdump.py` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **rfc2459.py** (`pyasn1_modules-0.4.2/pyasn1_modules/rfc2459.py`) — 5 inbound connections
2. **rfc2437.py** (`pyasn1_modules-0.4.2/pyasn1_modules/rfc2437.py`) — 1 inbound connections
3. **CHANGES.txt** (`pyasn1_modules-0.4.2/CHANGES.txt`) — 0 inbound connections
4. **LICENSE.txt** (`pyasn1_modules-0.4.2/LICENSE.txt`) — 0 inbound connections
5. **MANIFEST.in** (`pyasn1_modules-0.4.2/MANIFEST.in`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **test_rfc2876.py** (`pyasn1_modules-0.4.2/tests/test_rfc2876.py`) — 7 outbound dependencies
2. **ocspclient.py** (`pyasn1_modules-0.4.2/tools/ocspclient.py`) — 7 outbound dependencies
3. **test_rfc2631.py** (`pyasn1_modules-0.4.2/tests/test_rfc2631.py`) — 6 outbound dependencies
4. **test_rfc2985.py** (`pyasn1_modules-0.4.2/tests/test_rfc2985.py`) — 6 outbound dependencies
5. **test_rfc2986.py** (`pyasn1_modules-0.4.2/tests/test_rfc2986.py`) — 6 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `testDerCodec` **(Compute Cores)** (@ `pyasn1_modules-0.4.2/tests/test_rfc2985.py`) -> Impact: **35.3** | LOC: 113
- `testOpenTypes` **(Compute Cores)** (@ `pyasn1_modules-0.4.2/tests/test_rfc2985.py`) -> Impact: **33.8** | LOC: 82
- `testDerCodec` **(Compute Cores)** (@ `pyasn1_modules-0.4.2/tests/test_rfc3114.py`) -> Impact: **26.6** | LOC: 108
- `readPemBlocksFromFile` **(Callbacks & Closures)** (@ `pyasn1_modules-0.4.2/pyasn1_modules/pem.py`) -> Impact: **20.5** | LOC: 29
  * *Intent:* # The markers parameters is in form ('start1', 'stop1'), ('start2', 'stop2')... # Return is (marker-index, substrate)
- `testDerCodec` **(Compute Cores)** (@ `pyasn1_modules-0.4.2/tests/test_rfc5752.py`) -> Impact: **16.6** | LOC: 77
- `testDerCodec` **(Compute Cores)** (@ `pyasn1_modules-0.4.2/tests/test_rfc7229.py`) -> Impact: **16.3** | LOC: 44
- `testDerCodec` **(Compute Cores)** (@ `pyasn1_modules-0.4.2/tests/test_rfc3852.py`) -> Impact: **13.7** | LOC: 76
- `testDerCodec` **(Callbacks & Closures)** (@ `pyasn1_modules-0.4.2/tests/test_rfc4073.py`) -> Impact: **13.7** | LOC: 48
- `testDerCodec` **(Compute Cores)** (@ `pyasn1_modules-0.4.2/tests/test_rfc5280.py`) -> Impact: **13.7** | LOC: 48
- `testExtensionsMap` **(Compute Cores)** (@ `pyasn1_modules-0.4.2/tests/test_rfc3739.py`) -> Impact: **11.7** | LOC: 37

*Function archetypes referenced above:*
  * **Callbacks & Closures**: built around closures/callbacks (handlers, async continuations)
  * **Compute Cores**: dense algorithmic logic (high decision density per line)

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pyasn1_modules-0.4.2/pyasn1_modules` | 131 | 7705.16 | 6.1% | 2.11% |
| `pyasn1_modules-0.4.2/tests` | 125 | 4949.64 | 16.37% | 0.0% |
| `pyasn1_modules-0.4.2` | 6 | 23.0 | 0.0% | 0.0% |
| `pyasn1_modules-0.4.2/tools` | 14 | 0.35 | 20.05% | 7.13% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `pyasn1_modules-0.4.2/tools/ocspclient.py` -> **99.821%** Exposure
- `pyasn1_modules-0.4.2/pyasn1_modules/pem.py` -> **92.4142%** Exposure
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc2437.py` -> **81.7574%** Exposure
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc4210.py` -> **20.5776%** Exposure
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc2251.py` -> **20.1995%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `pyasn1_modules-0.4.2/pyasn1_modules/pem.py` -> **100.0%** Exposure
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc2985.py` -> **100.0%** Exposure
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc3279.py` -> **100.0%** Exposure
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc3370.py` -> **100.0%** Exposure
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc3560.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pyasn1_modules-0.4.2/tests/test_rfc5280.py` -> **2** Orphaned Functions | **6** Duplicates
- `pyasn1_modules-0.4.2/tests/test_rfc8419.py` -> **1** Orphaned Functions | **5** Duplicates
- `pyasn1_modules-0.4.2/tests/test_rfc3279.py` -> **0** Orphaned Functions | **5** Duplicates
- `pyasn1_modules-0.4.2/tests/test_rfc4055.py` -> **0** Orphaned Functions | **5** Duplicates
- `pyasn1_modules-0.4.2/tests/test_rfc2459.py` -> **0** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `pyasn1_modules-0.4.2/tools/ocspclient.py` -> **100.0%** Exposure
- `pyasn1_modules-0.4.2/tools/pkcs1dump.py` -> **100.0%** Exposure
- `pyasn1_modules-0.4.2/tools/pkcs8dump.py` -> **100.0%** Exposure
- `pyasn1_modules-0.4.2/tools/x509dump-rfc5280.py` -> **100.0%** Exposure
- `pyasn1_modules-0.4.2/tools/x509dump.py` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `926` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `pyasn1_modules-0.4.2/pyasn1_modules/pem.py` (PYTHON) -> Cumulative Risk: **741.36**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.44)
- **Magnitude:** 68.5 | **LOC:** 59 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Secrets Risk (99.97%)
- **Heaviest Functions:** `readPemBlocksFromFile` (Callbacks & Closures, Impact: 20.5), `readPemFromFile` (Parameter Forwarders, Impact: 2.2), `readBase64fromText` (Interface Declarations, Impact: 1.5)

### 2. `pyasn1_modules-0.4.2/tools/ocspclient.py` (PYTHON) -> Cumulative Risk: **672.04**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Parameter Forwarders Files` (z +0.93)
- **Magnitude:** 0.05 | **LOC:** 170 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Secrets Risk (100.0%), State Flux (99.9812%)
- **Heaviest Functions:** `mkOcspRequest` (Many-Argument Workhorses, Impact: 4.0), `parseOcspResponse` (Defensive Guards, Impact: 2.6), `encodeTag` (Parameter Forwarders, Impact: 1.8)

### 3. `pyasn1_modules-0.4.2/pyasn1_modules/rfc2985.py` (PYTHON) -> Cumulative Risk: **524.68**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +4.81)
- **Magnitude:** 207.56 | **LOC:** 589 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.2098%)
- **Heaviest Functions:** `_OID` (Type Conversions, Impact: 6.1)

### 4. `pyasn1_modules-0.4.2/pyasn1_modules/rfc8226.py` (PYTHON) -> Cumulative Risk: **520.11**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +4.85)
- **Magnitude:** 46.9 | **LOC:** 150 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9972%), Safety Score (97.0428%)
- **Heaviest Functions:** `_OID` (Type Conversions, Impact: 6.1)

### 5. `pyasn1_modules-0.4.2/pyasn1_modules/rfc4055.py` (PYTHON) -> Cumulative Risk: **513.92**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +4.87)
- **Magnitude:** 135.6 | **LOC:** 259 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.7112%)
- **Heaviest Functions:** `_OID` (Type Conversions, Impact: 6.1)

### 6. `pyasn1_modules-0.4.2/pyasn1_modules/rfc5990.py` (PYTHON) -> Cumulative Risk: **511.89**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +4.87)
- **Magnitude:** 102.52 | **LOC:** 238 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.4228%)
- **Heaviest Functions:** `_OID` (Type Conversions, Impact: 6.1)

### 7. `pyasn1_modules-0.4.2/pyasn1_modules/rfc3279.py` (PYTHON) -> Cumulative Risk: **511.35**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +4.88)
- **Magnitude:** 111.5 | **LOC:** 261 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (97.3403%)
- **Heaviest Functions:** `_OID` (Type Conversions, Impact: 6.1)

### 8. `pyasn1_modules-0.4.2/pyasn1_modules/rfc7292.py` (PYTHON) -> Cumulative Risk: **510.24**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +4.87)
- **Magnitude:** 113.04 | **LOC:** 358 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.1471%)
- **Heaviest Functions:** `_OID` (Type Conversions, Impact: 6.1)

### 9. `pyasn1_modules-0.4.2/pyasn1_modules/rfc5751.py` (PYTHON) -> Cumulative Risk: **509.57**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Declarative / Non-Code` (z +6.46)
- **Magnitude:** 42.28 | **LOC:** 125 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.3718%)
- **Heaviest Functions:** `_OID` (Type Conversions, Impact: 6.1)

### 10. `pyasn1_modules-0.4.2/pyasn1_modules/rfc5084.py` (PYTHON) -> Cumulative Risk: **509.56**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Declarative / Non-Code` (z +6.47)
- **Magnitude:** 33.02 | **LOC:** 98 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.587%)
- **Heaviest Functions:** `_OID` (Type Conversions, Impact: 6.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc5280.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 419.74 | **LOC:** 1659 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.5242%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_buildOid` **(Type Conversions)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 267
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 282`, `args: 1`, `func_start: 1`, `class_start: 126`
* *Risk/State:* `safety_bypasses: 132`, `state_mutation: 255`
* *Architecture:* `api: 126`, `import: 8`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc2459.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 411.94 | **LOC:** 1340 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (9.7855%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 192`, `class_start: 130`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 249`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 130`, `import: 8`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.018701
  * `Imports (Out-Degree: 0):` pyasn1.type
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc3280.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 407.9 | **LOC:** 1544 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.8208%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_OID` **(Type Conversions)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 256
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 283`, `args: 1`, `func_start: 1`, `class_start: 127`
* *Risk/State:* `safety_bypasses: 134`, `state_mutation: 244`
* *Architecture:* `api: 127`, `import: 7`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc7906.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 223.18 | **LOC:** 737 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 100`, `class_start: 34`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 166`
* *Architecture:* `api: 34`, `import: 13`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc2985.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 207.56 | **LOC:** 589 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.0987%), Tech Debt (14.5866%)
**Top Internal Functions/Classes:**
  * `_OID` **(Type Conversions)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 180
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 86`, `args: 1`, `func_start: 1`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 170`, `planned_debt: 3`
* *Architecture:* `api: 16`, `import: 12`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PKCS15Token, pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc5934.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 196.24 | **LOC:** 787 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.6936%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_OID` **(Type Conversions)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 106`, `args: 1`, `func_start: 1`, `class_start: 46`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 122`
* *Architecture:* `api: 46`, `import: 5`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc5652.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 180.52 | **LOC:** 762 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.4089%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_buildOid` **(Type Conversions)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 167`, `args: 1`, `func_start: 1`, `class_start: 70`
* *Risk/State:* `safety_bypasses: 83`, `state_mutation: 81`
* *Architecture:* `api: 70`, `import: 9`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc5126.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 173.34 | **LOC:** 578 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 94`, `class_start: 46`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 106`
* *Architecture:* `api: 46`, `import: 13`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc3852.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 163.8 | **LOC:** 707 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.9529%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_buildOid` **(Type Conversions)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 79
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 164`, `args: 1`, `func_start: 1`, `class_start: 70`
* *Risk/State:* `safety_bypasses: 77`, `state_mutation: 71`
* *Architecture:* `api: 70`, `import: 8`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc6402.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 154.12 | **LOC:** 629 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.1879%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_buildOid` **(Type Conversions)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 108`, `args: 1`, `func_start: 1`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 92`
* *Architecture:* `api: 38`, `import: 11`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc4357.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 147.7 | **LOC:** 478 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 67`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 102`
* *Architecture:* `api: 25`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc4055.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 135.6 | **LOC:** 259 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.7136%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_OID` **(Type Conversions)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 23`, `args: 1`, `func_start: 1`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 111`, `dead_code: 1`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc6031.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 127.96 | **LOC:** 470 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.4934%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_OID` **(Type Conversions)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 120`, `args: 1`, `func_start: 1`, `class_start: 45`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 61`
* *Architecture:* `api: 45`, `import: 10`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc2251.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 127.88 | **LOC:** 564 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.207%), Tech Debt (20.1995%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 80`, `class_start: 49`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 51`, `fragile_debt: 3`
* *Architecture:* `api: 49`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc3125.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 124.72 | **LOC:** 470 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 75`, `class_start: 48`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 55`
* *Architecture:* `api: 48`, `import: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc7292.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 113.04 | **LOC:** 358 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.5224%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_OID` **(Type Conversions)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 86
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 65`, `args: 1`, `func_start: 1`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 74`
* *Architecture:* `api: 17`, `import: 11`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc4210.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 111.7 | **LOC:** 804 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (20.5776%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 76`, `class_start: 43`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 45`, `fragile_debt: 3`
* *Architecture:* `api: 43`, `import: 10`
* *Defense:* `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc3279.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 111.5 | **LOC:** 261 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.764%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_OID` **(Type Conversions)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 82
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 40`, `args: 1`, `func_start: 1`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 72`
* *Architecture:* `api: 20`, `import: 4`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc5755.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 104.24 | **LOC:** 399 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 53`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 61`
* *Architecture:* `api: 23`, `import: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/tests/test_rfc7191.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 103.26 | **LOC:** 314 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.3813%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testOpenTypes` **(Compute Cores)** (Impact: 6.0)
  * `testOpenTypes` **(Compute Cores)** (Impact: 6.0)
  * `testDerCodec` **(Compute Cores)** (Impact: 5.6)
  * `testOpenTypes` **(Compute Cores)** (Impact: 5.2)
  * `testDerCodec` **(I/O & Config Routines)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 9 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 26`, `args: 9`, `func_start: 9`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 37`, `duplicate_logic: 3`
* *Architecture:* `io: 2`, `api: 12`, `import: 7`
* *Defense:* `doc: 3`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.codec.der.decoder, pyasn1.codec.der.encoder, pyasn1_modules, sys, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc5990.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 102.52 | **LOC:** 238 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (52.4773%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_OID` **(Type Conversions)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 35`, `args: 1`, `func_start: 1`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 73`
* *Architecture:* `api: 11`, `import: 4`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/tests/test_rfc5280.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 98.66 | **LOC:** 254 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.3995%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDerCodec` **(Compute Cores)** (Impact: 13.7)
  * `testDerCodec` **(Compute Cores)** (Impact: 8.7)
  * `testExtensionsMap` **(Compute Cores)** (Impact: 5.3)
  * `testDecodeOpenTypes` **(Interface Declarations)** (Impact: 2.1)
  * `testDerCodec` **(Interface Declarations)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 6 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 35`, `args: 11`, `func_start: 11`, `class_start: 5`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 27`, `duplicate_logic: 6`, `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `api: 16`, `import: 7`
* *Defense:* `doc: 5`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.codec.der.decoder, pyasn1.codec.der.encoder, pyasn1.type, pyasn1_modules, sys, unittest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc5275.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 97.62 | **LOC:** 405 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 56`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 56`
* *Architecture:* `api: 22`, `import: 12`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/pyasn1_modules/rfc4211.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 97.18 | **LOC:** 397 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.3442%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_buildOid` **(Type Conversions)** (Impact: 6.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 85`, `args: 1`, `func_start: 1`, `class_start: 30`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 44`
* *Architecture:* `api: 30`, `import: 8`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.type, pyasn1_modules
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyasn1_modules-0.4.2/tests/test_rfc2985.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 94.72 | **LOC:** 320 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.89%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDerCodec` **(Compute Cores)** (Impact: 35.3)
  * `testOpenTypes` **(Compute Cores)** (Impact: 33.8)
  * `setUp` **(Interface Declarations)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 37`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`, `unreferenced_by_name: 3`
* *Architecture:* `io: 1`, `api: 4`, `import: 10`
* *Defense:* `doc: 1`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.548
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pyasn1.codec.der.decoder, pyasn1.codec.der.encoder, pyasn1.type, pyasn1_modules, sys, unittest
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

- `pyasn1_modules-0.4.2/pyasn1_modules/rfc2437.py` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 99.9932%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pyasn1_modules-0.4.2/pyasn1_modules/rfc2459.py` -> **Severity: 1.715** (Embedded: 0.0187 * Error Risk: 91.6827%)
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc2437.py` -> **Severity: 0.316** (Embedded: 0.0036 * Error Risk: 86.8266%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pyasn1_modules-0.4.2/pyasn1_modules/pem.py` -> **Severity: 354.8** (Blast Radius: 3.548 * Doc Risk: 100.0%)
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc2985.py` -> **Severity: 354.8** (Blast Radius: 3.548 * Doc Risk: 100.0%)
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc3279.py` -> **Severity: 354.8** (Blast Radius: 3.548 * Doc Risk: 100.0%)
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc3280.py` -> **Severity: 354.8** (Blast Radius: 3.548 * Doc Risk: 100.0%)
- `pyasn1_modules-0.4.2/pyasn1_modules/rfc3281.py` -> **Severity: 354.8** (Blast Radius: 3.548 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
