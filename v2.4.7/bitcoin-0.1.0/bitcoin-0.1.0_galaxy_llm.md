# ARCHITECTURAL_BRIEF: bitcoin-0.1.0
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/bitcoin-0.1.0` |
| **Timestamp** | `2026-08-07T03:47:07.596522+00:00` |
| **Scan Duration** | `0.41s` |
| **Git Branch** | `master` |
| **Git Commit** | `92ee8d9a994391d148733da77e2bbc2f4acc43cd` |
| **Git Remote** | `https://github.com/trottier/original-bitcoin.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 28 malicious artifacts.

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
| Total Artifacts | 50 |
| Analyzed Artifacts (Scanned) | 33 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 17 |
| Total LOC | 10505 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 66.0% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2008 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.8321 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 26 | 10404 | 78.8% |
| PLAINTEXT | 4 | 0 | 12.1% |
| MAKEFILE | 2 | 101 | 6.1% |
| MARKDOWN | 1 | 0 | 3.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.661`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 22 | 66.7% |
| file_cluster_13 | 3 | 9.1% |
| file_cluster_9 | 1 | 3.0% |
| file_cluster_16 | 1 | 3.0% |
| file_cluster_11 | 1 | 3.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 15.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 17*

**Composition by Extension & Reason:**
- `.bmp`: 9x Excluded (Explicitly Denied Extension: '.bmp')
- `.dll`: 2x Excluded (Explicitly Denied Extension: '.dll')
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.exe`: 1x Excluded (Explicitly Denied Extension: '.exe')
- `.rc`: 1x Unsupported Format (.rc)
- `.fbp`: 1x Unsupported Format (.fbp)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.7 | 52.3 | 57.1 | 0.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 83.6 | 95.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 69.8 | 99.9 | 100.0 |
| Testing Exposure | 0.5 | 80.0 | 52.2 | 80.0 | 80.0 |
| API Exposure | 0.0 | 10.5 | 4.1 | 4.5 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 89.3 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 38.6 | 4.2 | 0.0 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 97.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 6.2 | 86.4 | 25.7 | 13.1 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/serialize.h` (Hits: 6)
- `src/irc.cpp` (Hits: 4)
- `src/net.cpp` (Hits: 4)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **headers.h** (`src/headers.h`) — 8 inbound connections
2. **sha.h** (`src/sha.h`) — 2 inbound connections
3. **uibase.h** (`src/uibase.h`) — 2 inbound connections
4. **base58.h** (`src/base58.h`) — 1 inbound connections
5. **bignum.h** (`src/bignum.h`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **headers.h** (`src/headers.h`) — 50 outbound dependencies
2. **uibase.h** (`src/uibase.h`) — 28 outbound dependencies
3. **serialize.h** (`src/serialize.h`) — 4 outbound dependencies
4. **bignum.h** (`src/bignum.h`) — 3 outbound dependencies
5. **sha.cpp** (`src/sha.cpp`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `EvalScript` (@ `src/script.cpp`) -> Impact: **773.1** | LOC: 717
  * *Intent:* // // Script is a stack machine (like Forth) that evaluates a predicate // returning a bool indicating valid or not. There are no loops. // #define st...
- `CTransaction::DisconnectInputs` (@ `src/main.cpp`) -> Impact: **206.9** | LOC: 570
- `GetOpName` (@ `src/script.h`) -> Impact: **115.7** | LOC: 134
- `CheckTransaction` (@ `src/main.h`) -> Impact: **108.2** | LOC: 524
- `ThreadIRCSeed` (@ `src/irc.cpp`) -> Impact: **62.6** | LOC: 108
- `HtmlEscape` (@ `src/ui.cpp`) -> Impact: **62.1** | LOC: 29
- `CAddrDB::LoadAddresses` (@ `src/db.cpp`) -> Impact: **56.1** | LOC: 161
- `CRITICAL_BLOCK` (@ `src/db.cpp`) -> Impact: **47.7** | LOC: 133
- `ParseMoney` (@ `src/util.cpp`) -> Impact: **43.6** | LOC: 41
- `AddToWallet` (@ `src/main.cpp`) -> Impact: **32.8** | LOC: 56
  * *Intent:* ////////////////////////////////////////////////////////////////////////////// // // mapWallet //

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 30 | 12426.54 | 48.83% | 65.17% |
| `__monolith__` | 3 | 3.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/base58.h` -> **100.0%** Exposure
- `src/bignum.h` -> **100.0%** Exposure
- `src/main.h` -> **100.0%** Exposure
- `src/script.h` -> **100.0%** Exposure
- `src/serialize.h` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/base58.h` -> **100.0%** Exposure
- `src/bignum.h` -> **100.0%** Exposure
- `src/db.cpp` -> **100.0%** Exposure
- `src/db.h` -> **100.0%** Exposure
- `src/irc.cpp` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/uint256.h` -> **0** Orphaned Functions | **126** Duplicates
- `src/ui.cpp` -> **66** Orphaned Functions | **14** Duplicates
- `src/serialize.h` -> **0** Orphaned Functions | **73** Duplicates
- `src/main.h` -> **0** Orphaned Functions | **62** Duplicates
- `src/uibase.h` -> **0** Orphaned Functions | **52** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/script.cpp`** -> AI Confidence: **99.29%**
2. **`src/uibase.cpp`** -> AI Confidence: **99.29%**
3. **`src/util.cpp`** -> AI Confidence: **99.11%**
4. **`src/db.cpp`** -> AI Confidence: **99.06%**
5. **`src/irc.cpp`** -> AI Confidence: **99.06%**
6. **`src/main.cpp`** -> AI Confidence: **99.06%**
7. **`src/market.cpp`** -> AI Confidence: **99.06%**
8. **`src/net.cpp`** -> AI Confidence: **99.06%**
9. **`src/ui.cpp`** -> AI Confidence: **99.06%**
10. **`src/headers.h`** -> AI Confidence: **99.01%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `104` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/bignum.h` (CPP) -> Cumulative Risk: **628.08**
- **Archetype:** `file_cluster_8` (Distance: 14.296 IQR)
- **Magnitude:** 829.98 | **LOC:** 499 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.7151%)
- **Heaviest Functions:** `SetHex` (Impact: 17.4), `setint64` (Impact: 11.7), `SetCompact` (Impact: 8.6)

### 2. `src/util.h` (CPP) -> Cumulative Risk: **623.6**
- **Archetype:** `file_cluster_11` (Distance: 13.813 IQR)
- **Magnitude:** 384.18 | **LOC:** 400 | **CtrlFlow:** 42.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9943%), Safety Score (98.434%)
- **Heaviest Functions:** `OutputDebugStringF` (Impact: 18.7), `CRITICAL_BLOCK` (Impact: 8.8), `HexStr` (Impact: 8.5)

### 3. `src/script.h` (CPP) -> Cumulative Risk: **590.05**
- **Archetype:** `file_cluster_8` (Distance: 12.088 IQR)
- **Magnitude:** 475.02 | **LOC:** 598 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (89.0413%)
- **Heaviest Functions:** `GetOpName` (Impact: 115.7), `GetOp` (Impact: 16.6), `FindAndDelete` (Impact: 10.8)

### 4. `src/net.h` (CPP) -> Cumulative Risk: **577.75**
- **Archetype:** `file_cluster_8` (Distance: 12.602 IQR)
- **Magnitude:** 590.56 | **LOC:** 857 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9714%), Safety Score (95.3322%)
- **Heaviest Functions:** `operator<` (Impact: 12.8), `AdvertStartPublish` (Impact: 11.9), `IsValid` (Impact: 11.4)

### 5. `src/db.cpp` (CPP) -> Cumulative Risk: **571.33**
- **Archetype:** `file_cluster_8` (Distance: 12.532 IQR)
- **Magnitude:** 484.24 | **LOC:** 609 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9994%), Safety Score (88.6278%)
- **Heaviest Functions:** `CAddrDB::LoadAddresses` (Impact: 56.1), `CRITICAL_BLOCK` (Impact: 47.7), `CDB::CDB` (Impact: 29.7)

### 6. `src/base58.h` (CPP) -> Cumulative Risk: **569.82**
- **Archetype:** `file_cluster_8` (Distance: 12.833 IQR)
- **Magnitude:** 207.22 | **LOC:** 202 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (98.8368%)
- **Heaviest Functions:** `DecodeBase58` (Impact: 23.0), `EncodeBase58` (Impact: 10.5), `DecodeBase58Check` (Impact: 7.8)

### 7. `src/main.h` (CPP) -> Cumulative Risk: **569.57**
- **Archetype:** `file_cluster_8` (Distance: 12.714 IQR)
- **Magnitude:** 865.42 | **LOC:** 1318 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (95.3486%)
- **Heaviest Functions:** `CheckTransaction` (Impact: 108.2), `IsNewerThan` (Impact: 17.4), `ReadFromDisk` (Impact: 11.1)

### 8. `src/util.cpp` (CPP) -> Cumulative Risk: **561.28**
- **Archetype:** `file_cluster_8` (Distance: 13.038 IQR)
- **Magnitude:** 389.26 | **LOC:** 380 | **CtrlFlow:** 70.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9102%), Safety Score (98.3734%)
- **Heaviest Functions:** `ParseMoney` (Impact: 43.6), `strprintf` (Impact: 15.4), `AddTimeData` (Impact: 13.7)

### 9. `src/net.cpp` (CPP) -> Cumulative Risk: **557.84**
- **Archetype:** `file_cluster_8` (Distance: 12.457 IQR)
- **Magnitude:** 363.02 | **LOC:** 1068 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.6788%), Safety Score (97.3069%)
- **Heaviest Functions:** `GetMyExternalIP2` (Impact: 24.5), `ConnectSocket` (Impact: 21.6), `GetMyExternalIP` (Impact: 20.6)

### 10. `src/serialize.h` (CPP) -> Cumulative Risk: **546.02**
- **Archetype:** `file_cluster_16` (Distance: 13.55 IQR)
- **Magnitude:** 740.04 | **LOC:** 1152 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (97.9829%)
- **Heaviest Functions:** `Rewind` (Impact: 31.8), `WriteCompactSize` (Impact: 13.6), `ReadCompactSize` (Impact: 13.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/script.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.868 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 3.741 IQR)
- **Top Global Matches:** file_cluster_8: 12.868, file_cluster_7: 13.283, file_cluster_13: 13.29
- **Magnitude:** 1284.96 | **LOC:** 1128 | **CtrlFlow:** 85.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.5562%), Tech Debt (9.4392%)
**Top Internal Functions/Classes:**
  * `EvalScript` (Impact: 773.1)
    * *Intent:* // // Script is a stack machine (like Forth) that evaluates a predicate // returning a bool indicati...
  * `SignatureHash` (Impact: 12.6)
  * `VerifySignature` (Impact: 7.4)
  * `MakeSameSize` (Impact: 3.4)
  * `CastToBool` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 308`, `structural_boundaries: 53`, `args: 10`, `func_start: 5`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 474`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `import: 1`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` headers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/uint256.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 98.79%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.706 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 6.377 IQR)
- **Top Global Matches:** file_cluster_8: 14.706, file_cluster_13: 14.878, file_cluster_7: 14.91
- **Magnitude:** 1209.06 | **LOC:** 751 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.103%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `SetHex` (Impact: 23.6)
  * `operator<<=` (Impact: 12.8)
  * `operator>>=` (Impact: 12.8)
  * `Testuint256AdHoc` (Impact: 10.0)
  * `uint160` (Impact: 7.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 276`, `args: 15`, `func_start: 140`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 903`, `duplicate_logic: 126`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `doc: 52`, `immutability_locks: 255`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` string, limits.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.003 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.49 IQR)
- **Top Global Matches:** file_cluster_8: 14.003, file_cluster_7: 14.109, file_cluster_13: 14.17
- **Magnitude:** 1191.06 | **LOC:** 2661 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.2692%), Tech Debt (99.7482%)
**Top Internal Functions/Classes:**
  * `CTransaction::DisconnectInputs` (Impact: 206.9)
  * `AddToWallet` (Impact: 32.8)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////// // // mapWallet //
  * `CBlock::CheckBlock` (Impact: 24.4)
  * `GetNextWorkRequired` (Impact: 18.2)
  * `PrintBlockTree` (Impact: 18.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 103`, `args: 36`, `func_start: 54`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 560`, `dead_code: 4`, `duplicate_logic: 20`, `orphaned_logic: 21`
* *Architecture:* `io: 3`, `import: 2`
* *Defense:* `safety: 5`, `doc: 162`, `immutability_locks: 36`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` sha.h, headers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ui.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.218 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.691 IQR)
- **Top Global Matches:** file_cluster_8: 14.218, file_cluster_7: 14.327, file_cluster_13: 14.457
- **Magnitude:** 1013.56 | **LOC:** 3229 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.1103%), Tech Debt (99.9938%)
**Top Internal Functions/Classes:**
  * `HtmlEscape` (Impact: 62.1)
  * `CEditProductDialog::SetProduct` (Impact: 17.4)
  * `CRITICAL_BLOCK` (Impact: 15.7)
    * *Intent:* //m_listCtrlProductsSent->InsertColumn(0, "Category", wxLIST_FORMAT_LEFT, 100); //m_listCtrlProducts...
  * `CProductsDialog::OnButtonSearch` (Impact: 12.3)
  * `CEditProductDialog::GetProduct` (Impact: 9.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 132`, `args: 31`, `func_start: 94`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 1`, `state_mutation: 644`, `dead_code: 1`, `duplicate_logic: 14`, `orphaned_logic: 66`
* *Architecture:* `import: 2`
* *Defense:* `safety: 3`, `doc: 211`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` crtdbg.h, headers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main.h` (CPP | Tier 0 | 🚨 AI THREAT: 98.75%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.714 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.82 IQR)
- **Top Global Matches:** file_cluster_8: 12.714, file_cluster_7: 13.164, file_cluster_13: 13.226
- **Magnitude:** 865.42 | **LOC:** 1318 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.2866%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `CheckTransaction` (Impact: 108.2)
  * `IsNewerThan` (Impact: 17.4)
  * `ReadFromDisk` (Impact: 11.1)
  * `Set` (Impact: 10.8)
  * `WriteToDisk` (Impact: 9.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 114`, `args: 47`, `func_start: 82`, `class_start: 21`
* *Risk/State:* `state_mutation: 490`, `duplicate_logic: 62`
* *Architecture:* `api: 21`
* *Defense:* `immutability_locks: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/bignum.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 98.91%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.296 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.848 IQR)
- **Top Global Matches:** file_cluster_8: 14.296, file_cluster_13: 14.508, file_cluster_11: 14.664
- **Magnitude:** 829.98 | **LOC:** 499 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.5809%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `SetHex` (Impact: 17.4)
  * `setint64` (Impact: 11.7)
  * `SetCompact` (Impact: 8.6)
  * `setuint64` (Impact: 7.3)
  * `setuint256` (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 82`, `args: 54`, `func_start: 66`, `class_start: 3`
* *Risk/State:* `state_mutation: 574`, `duplicate_logic: 30`
* *Architecture:* `api: 28`, `import: 3`
* *Defense:* `immutability_locks: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` vector, bn.h, stdexcept
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/serialize.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 98.72%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.55 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 6.341 IQR)
- **Top Global Matches:** file_cluster_16: 13.55, file_cluster_8: 13.766, file_cluster_13: 13.804
- **Magnitude:** 740.04 | **LOC:** 1152 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.2873%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Rewind` (Impact: 31.8)
  * `WriteCompactSize` (Impact: 13.6)
  * `ReadCompactSize` (Impact: 13.5)
  * `GetSizeOfCompactSize` (Impact: 12.5)
    * *Intent:* // // Compact size // size < 253 -- 1 byte // size <= USHRT_MAX -- 3 bytes (253 + 2 bytes) // size <...
  * `read` (Impact: 7.3)
    * *Intent:* //
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 405`, `args: 111`, `func_start: 102`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 407`, `duplicate_logic: 73`
* *Architecture:* `io: 6`, `api: 22`, `import: 3`
* *Defense:* `doc: 21`, `immutability_locks: 68`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` vector, map, is_fundamental.hpp, iostream
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/net.h` (CPP | Tier 0 | 🚨 AI THREAT: 98.75%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.602 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.098 IQR)
- **Top Global Matches:** file_cluster_8: 12.602, file_cluster_0: 12.767, file_cluster_11: 12.831
- **Magnitude:** 590.56 | **LOC:** 857 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.1159%), Tech Debt (99.9714%)
**Top Internal Functions/Classes:**
  * `operator<` (Impact: 12.8)
  * `AdvertStartPublish` (Impact: 11.9)
    * *Intent:* // // Templates for the publish and subscription system. // The object being published as T& obj nee...
  * `IsValid` (Impact: 11.4)
  * `AdvertStopPublish` (Impact: 9.5)
  * `CAddress` (Impact: 8.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 143`, `args: 58`, `func_start: 57`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 8`, `state_mutation: 342`, `dead_code: 3`, `duplicate_logic: 27`
* *Architecture:* `api: 24`
* *Defense:* `safety: 10`, `doc: 1`, `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/db.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.532 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 3.988 IQR)
- **Top Global Matches:** file_cluster_8: 12.532, file_cluster_13: 12.824, file_cluster_0: 12.853
- **Magnitude:** 484.24 | **LOC:** 609 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.6202%), Tech Debt (99.9994%)
**Top Internal Functions/Classes:**
  * `CAddrDB::LoadAddresses` (Impact: 56.1)
  * `CRITICAL_BLOCK` (Impact: 47.7)
  * `CDB::CDB` (Impact: 29.7)
  * `CRITICAL_BLOCK` (Impact: 22.6)
  * `CTxDB::LoadBlockIndex` (Impact: 19.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 42`, `args: 13`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 213`, `dead_code: 2`, `fragile_debt: 1`, `duplicate_logic: 10`, `orphaned_logic: 15`
* *Architecture:* `io: 2`, `api: 1`, `import: 1`
* *Defense:* `safety: 9`, `doc: 6`, `immutability_locks: 9`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` headers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/script.h` (CPP | Tier 0 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.088 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.139 IQR)
- **Top Global Matches:** file_cluster_8: 12.088, file_cluster_0: 12.487, file_cluster_13: 12.489
- **Magnitude:** 475.02 | **LOC:** 598 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.2805%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `GetOpName` (Impact: 115.7)
  * `GetOp` (Impact: 16.6)
  * `FindAndDelete` (Impact: 10.8)
  * `operator<<` (Impact: 6.0)
  * `ToString` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 164`, `args: 31`, `func_start: 48`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 218`, `dead_code: 2`, `duplicate_logic: 36`
* *Architecture:* `api: 8`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/uibase.h` (CPP | Tier 0 | 🚨 AI THREAT: 99.01%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.15 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 5.573 IQR)
- **Top Global Matches:** file_cluster_13: 14.15, file_cluster_7: 14.336, file_cluster_12: 14.413
- **Magnitude:** 465.1 | **LOC:** 721 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `OnClose` (Impact: 1.1)
    * *Intent:* // Virtual event handlers, overide them in your derived class
  * `OnIdle` (Impact: 1.1)
  * `OnMouseEvents` (Impact: 1.1)
  * `OnPaint` (Impact: 1.1)
  * `OnMenuFileExit` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 250`, `func_start: 117`, `class_start: 16`
* *Risk/State:* `state_mutation: 245`, `duplicate_logic: 52`
* *Architecture:* `api: 81`, `import: 28`
* *Defense:* `doc: 923`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 48.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.173611
  * `Imports (Out-Degree: 0):` icon.h, colour.h, toolbar.h, stattext.h, richtextctrl.h, choice.h, treectrl.h, notebook.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/uibase.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.151 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 6.929 IQR)
- **Top Global Matches:** file_cluster_8: 13.151, file_cluster_7: 13.403, file_cluster_1: 13.675
- **Magnitude:** 463.82 | **LOC:** 1807 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.4173%), Tech Debt (22.9357%)
**Top Internal Functions/Classes:**
  * `CAboutDialogBase::CAboutDialogBase` (Impact: 6.2)
  * `CSendDialogBase::CSendDialogBase` (Impact: 6.2)
  * `CYourAddressDialogBase::CYourAddressDial` (Impact: 4.3)
  * `CEditProductDialogBase::CEditProductDial` (Impact: 4.3)
  * `CMainFrameBase::CMainFrameBase` (Impact: 2.4)
    * *Intent:* // Distributed under the MIT/X11 software license, see the accompanying // file license.txt or http:...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `args: 400`, `func_start: 32`
* *Risk/State:* `state_mutation: 357`, `orphaned_logic: 16`
* *Architecture:* `import: 1`
* *Defense:* `doc: 75`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` uibase.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/util.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.038 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.39 IQR)
- **Top Global Matches:** file_cluster_8: 13.038, file_cluster_13: 13.414, file_cluster_7: 13.447
- **Magnitude:** 389.26 | **LOC:** 380 | **CtrlFlow:** 70.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.7424%), Tech Debt (99.9102%)
**Top Internal Functions/Classes:**
  * `ParseMoney` (Impact: 43.6)
  * `strprintf` (Impact: 15.4)
  * `AddTimeData` (Impact: 13.7)
  * `my_snprintf` (Impact: 9.7)
    * *Intent:* // Safer snprintf // - prints up to limit-1 characters // - output string is always null terminated ...
  * `FormatMoney` (Impact: 9.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 28`, `args: 20`, `func_start: 17`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 235`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 11`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 2`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` headers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/util.h` (CPP | Tier 0 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.813 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.312 IQR)
- **Top Global Matches:** file_cluster_11: 13.813, file_cluster_8: 13.839, file_cluster_0: 13.964
- **Magnitude:** 384.18 | **LOC:** 400 | **CtrlFlow:** 42.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.9613%), Tech Debt (99.9943%)
**Top Internal Functions/Classes:**
  * `OutputDebugStringF` (Impact: 18.7)
    * *Intent:* #else
  * `CRITICAL_BLOCK` (Impact: 8.8)
  * `HexStr` (Impact: 8.5)
  * `HexNumStr` (Impact: 6.5)
  * `atoi64` (Impact: 4.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 63`, `args: 18`, `func_start: 30`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 268`, `dead_code: 1`, `duplicate_logic: 13`
* *Architecture:* `io: 2`, `api: 15`
* *Defense:* `safety: 4`, `immutability_locks: 33`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/net.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.457 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.086 IQR)
- **Top Global Matches:** file_cluster_8: 12.457, file_cluster_13: 12.821, file_cluster_7: 12.987
- **Magnitude:** 363.02 | **LOC:** 1068 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.9318%), Tech Debt (99.6788%)
**Top Internal Functions/Classes:**
  * `GetMyExternalIP2` (Impact: 24.5)
  * `ConnectSocket` (Impact: 21.6)
  * `GetMyExternalIP` (Impact: 20.6)
  * `CNode::CancelSubscribe` (Impact: 14.0)
  * `AddAddress` (Impact: 11.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 43`, `args: 19`, `func_start: 16`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 189`, `duplicate_logic: 6`, `orphaned_logic: 6`
* *Architecture:* `io: 4`, `import: 2`
* *Defense:* `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` winsock2.h, headers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/db.h` (CPP | Tier 0 | 🚨 AI THREAT: 98.79%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.344 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.798 IQR)
- **Top Global Matches:** file_cluster_8: 12.344, file_cluster_13: 12.69, file_cluster_0: 12.755
- **Magnitude:** 339.56 | **LOC:** 421 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.9552%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ReadAtCursor` (Impact: 26.5)
  * `Write` (Impact: 7.3)
  * `Erase` (Impact: 7.0)
  * `Read` (Impact: 6.6)
  * `GetCursor` (Impact: 6.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 82`, `args: 48`, `func_start: 33`, `class_start: 15`
* *Risk/State:* `high_risk_execution: 9`, `state_mutation: 191`
* *Architecture:* `api: 33`, `import: 1`
* *Defense:* `immutability_locks: 46`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` db_cxx.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/irc.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.282 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.259 IQR)
- **Top Global Matches:** file_cluster_8: 12.282, file_cluster_13: 12.729, file_cluster_7: 12.799
- **Magnitude:** 296.84 | **LOC:** 289 | **CtrlFlow:** 66.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.8665%), Tech Debt (13.7145%)
**Top Internal Functions/Classes:**
  * `ThreadIRCSeed` (Impact: 62.6)
  * `RecvLine` (Impact: 22.5)
  * `RecvUntil` (Impact: 18.7)
  * `RecvLineIRC` (Impact: 9.8)
  * `Send` (Impact: 7.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 32`, `args: 12`, `func_start: 9`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 153`, `orphaned_logic: 1`
* *Architecture:* `io: 4`, `import: 1`
* *Defense:* `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` headers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/base58.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 98.75%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.833 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.201 IQR)
- **Top Global Matches:** file_cluster_8: 12.833, file_cluster_13: 13.306, file_cluster_7: 13.335
- **Magnitude:** 207.22 | **LOC:** 202 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.8698%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `DecodeBase58` (Impact: 23.0)
  * `EncodeBase58` (Impact: 10.5)
    * *Intent:* // Copyright (c) 2009 Satoshi Nakamoto // Distributed under the MIT/X11 software license, see the ac...
  * `DecodeBase58Check` (Impact: 7.8)
  * `AddressToHash160` (Impact: 7.6)
  * `IsValidBitcoinAddress` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 33`, `args: 6`, `func_start: 13`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 142`, `duplicate_logic: 10`
* *Architecture:* `api: 1`
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/ui.h` (CPP | Tier 0 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.124 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.383 IQR)
- **Top Global Matches:** file_cluster_8: 11.124, file_cluster_7: 11.445, file_cluster_13: 11.696
- **Magnitude:** 183.0 | **LOC:** 419 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.0897%), Tech Debt (94.9722%)
**Top Internal Functions/Classes:**
  * `OnKeyDown` (Impact: 4.3)
  * `CGetTextFromUserDialog` (Impact: 2.9)
    * *Intent:* /** Constructor */
  * `OnKeyDown` (Impact: 1.1)
  * `OnKeyDown` (Impact: 1.1)
    * *Intent:* // Event handlers
  * `OnKeyDown` (Impact: 1.1)
    * *Intent:* // Event handlers
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 149`, `args: 16`, `func_start: 13`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 141`, `duplicate_logic: 6`
* *Architecture:* `api: 17`
* *Defense:* `doc: 14`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/key.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.147 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.764 IQR)
- **Top Global Matches:** file_cluster_8: 13.147, file_cluster_13: 13.59, file_cluster_0: 13.601
- **Magnitude:** 165.52 | **LOC:** 157 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.9541%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `CKey` (Impact: 4.3)
  * `operator=` (Impact: 4.3)
  * `SetPrivKey` (Impact: 4.3)
  * `Sign` (Impact: 4.3)
  * `GetPrivKey` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 20`, `args: 8`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 118`, `duplicate_logic: 7`
* *Architecture:* `api: 3`
* *Defense:* `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/market.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.6 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.59 IQR)
- **Top Global Matches:** file_cluster_13: 13.6, file_cluster_8: 13.615, file_cluster_11: 13.805
- **Magnitude:** 120.66 | **LOC:** 265 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.278%), Tech Debt (91.2033%)
**Top Internal Functions/Classes:**
  * `CUser::AddAtom` (Impact: 15.5)
  * `AddAtomsAndPropagate` (Impact: 11.1)
  * `AdvertInsert` (Impact: 7.4)
  * `Union` (Impact: 4.7)
  * `CRITICAL_BLOCK` (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 10`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 75`, `dead_code: 1`, `orphaned_logic: 4`
* *Architecture:* `import: 1`
* *Defense:* `doc: 9`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` headers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.158 IQR)
- **Top Global Matches:** file_cluster_8: 12.158, file_cluster_9: 12.46, file_cluster_0: 12.488
- **Magnitude:** 99.04 | **LOC:** 84 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.2781%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 10`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 3`, `dead_code: 2`
* *Architecture:* `api: 2`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sha.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.805 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.291 IQR)
- **Top Global Matches:** file_cluster_8: 11.805, file_cluster_12: 12.071, file_cluster_7: 12.431
- **Magnitude:** 91.48 | **LOC:** 555 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.7257%), Tech Debt (23.6089%)
**Top Internal Functions/Classes:**
  * `SHA512::Transform` (Impact: 14.0)
  * `SHA1::InitState` (Impact: 2.1)
    * *Intent:* // This file is public domain // SHA routines extracted as a standalone file from: // Crypto++: a C+...
  * `SHA1::Transform` (Impact: 2.0)
  * `SHA512_SSE2_Transform` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 62`, `args: 96`, `func_start: 4`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 67`, `orphaned_logic: 3`
* *Architecture:* `io: 4`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sha.h, assert.h, memory.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/market.h` (CPP | Tier 0 | 🚨 AI THREAT: 98.79%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.454 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.809 IQR)
- **Top Global Matches:** file_cluster_8: 10.454, file_cluster_7: 11.097, file_cluster_13: 11.245
- **Magnitude:** 61.08 | **LOC:** 183 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.2249%), Tech Debt (99.9997%)
**Top Internal Functions/Classes:**
  * `IMPLEMENT_SERIALIZE` (Impact: 4.6)
  * `SetNull` (Impact: 1.4)
  * `CReview` (Impact: 1.4)
  * `CProduct` (Impact: 1.3)
  * `GetAtomCount` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 17`, `args: 5`, `func_start: 13`, `class_start: 6`
* *Risk/State:* `state_mutation: 35`, `duplicate_logic: 7`
* *Architecture:* `api: 5`
* *Defense:* `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sha.h` (CPP | Tier 0 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.826 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 2.985 IQR)
- **Top Global Matches:** file_cluster_8: 10.826, file_cluster_13: 11.174, file_cluster_11: 11.261
- **Magnitude:** 48.5 | **LOC:** 178 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.1293%), Tech Debt (99.9997%)
**Top Internal Functions/Classes:**
  * `ByteReverse` (Impact: 3.5)
  * `ByteReverse` (Impact: 2.1)
  * `rotlFixed` (Impact: 2.0)
    * *Intent:* #endif
  * `rotrFixed` (Impact: 2.0)
  * `ByteReverse` (Impact: 1.2)
    * *Intent:* #define CRYPTOPP_FAST_ROTATE(x) ((x) == 32) #elif defined(__GNUC__) && (CRYPTOPP_BOOL_X64 || CRYPTOP...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 21`, `args: 6`, `func_start: 10`
* *Risk/State:* `state_mutation: 24`, `dead_code: 1`, `duplicate_logic: 8`
* *Architecture:* `api: 5`, `import: 1`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 47.625
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0625
  * `Imports (Out-Degree: 0):` stdlib.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/util.h` (CPP) | Magnitude: 384.18 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 268, indent_spaces: 149, structural_boundaries: 63, branch: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/market.cpp` (CPP) | Magnitude: 120.66 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 75, indent_spaces: 73, branch: 14, structural_boundaries: 10
- `src/uibase.h` (CPP) | Magnitude: 465.1 | Delta: **0.186 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 923, indent_spaces: 341, structural_boundaries: 250, state_mutation: 245
- `src/headers.h` (CPP) | Magnitude: 16.28 | Delta: **0.257 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: import: 50, macros: 10, structural_boundaries: 4, reflection_metaprogramming: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/serialize.h` (CPP) | Magnitude: 740.04 | Delta: **0.216 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 407, structural_boundaries: 405, indent_spaces: 296, args: 111

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/main.cpp` (CPP) | Magnitude: 1191.06 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 710, state_mutation: 560, branch: 182, doc: 162
- `src/ui.cpp` (CPP) | Magnitude: 1013.56 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 644, indent_spaces: 591, doc: 211, pointers: 151
- `src/net.h` (CPP) | Magnitude: 590.56 | Delta: **0.165 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 547, state_mutation: 342, structural_boundaries: 143, branch: 69
- `src/uint256.h` (CPP) | Magnitude: 1209.06 | Delta: **0.172 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 903, indent_spaces: 473, structural_boundaries: 276, immutability_locks: 255
- `src/bignum.h` (CPP) | Magnitude: 829.98 | Delta: **0.212 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 574, indent_spaces: 378, structural_boundaries: 82, pointers: 82

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/irc.h` (CPP) | Magnitude: 12.56 | Delta: **0.264 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: globals: 3, structural_boundaries: 2, args: 2, safety_bypasses: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/uint256.h` -> **Severity: 14.871** (Embedded: 0.1489 * Error Risk: 99.8757%)
- `src/bignum.h` -> **Severity: 14.847** (Embedded: 0.1489 * Error Risk: 99.7151%)
- `src/key.h` -> **Severity: 14.748** (Embedded: 0.1489 * Error Risk: 99.0462%)
- `src/base58.h` -> **Severity: 14.717** (Embedded: 0.1489 * Error Risk: 98.8368%)
- `src/util.h` -> **Severity: 14.657** (Embedded: 0.1489 * Error Risk: 98.434%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/db.h` -> **Severity: 2617.256** (Blast Radius: 30.308 * Doc Risk: 86.3553%)
- `src/headers.h` -> **Severity: 2436.475** (Blast Radius: 154.389 * Doc Risk: 15.7814%)
- `src/bignum.h` -> **Severity: 1919.251** (Blast Radius: 30.308 * Doc Risk: 63.3249%)
- `src/sha.h` -> **Severity: 1481.133** (Blast Radius: 47.625 * Doc Risk: 31.0999%)
- `src/util.h` -> **Severity: 1365.778** (Blast Radius: 30.308 * Doc Risk: 45.0633%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
