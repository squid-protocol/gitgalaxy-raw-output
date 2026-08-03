# ARCHITECTURAL_BRIEF: bitcoin-0.1.0
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/bitcoin-0.1.0` |
| **Timestamp** | `2026-08-03T19:24:35.785246+00:00` |
| **Scan Duration** | `0.47s` |
| **Git Branch** | `master` |
| **Git Commit** | `92ee8d9a994391d148733da77e2bbc2f4acc43cd` |
| **Git Remote** | `https://github.com/trottier/original-bitcoin.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 28 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 99.8 | 53.7 | 58.9 | 0.0 |
| Error & Exception Exposure | 0.0 | 99.7 | 62.0 | 74.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 65.5 | 99.9 | 100.0 |
| Testing Exposure | 0.5 | 80.0 | 57.7 | 80.0 | 80.0 |
| API Exposure | 0.0 | 10.5 | 3.9 | 3.6 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 89.3 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 38.6 | 4.2 | 0.0 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 97.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 11.9 | 100.0 | 59.3 | 73.4 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 72.7 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 14.3 | 20.0 | 20.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.5 | 0.0 | 0.0 | 0.0 |
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

- `EvalScript` (@ `src/script.cpp`) -> Impact: **2616.4** | LOC: 717
  * *Intent:* // // Script is a stack machine (like Forth) that evaluates a predicate // returning a bool indicating valid or not. There are no loops. // #define st...
- `CTransaction::DisconnectInputs` (@ `src/main.cpp`) -> Impact: **652.9** | LOC: 570
- `CheckTransaction` (@ `src/main.h`) -> Impact: **313.2** | LOC: 524
- `IsValid` (@ `src/net.h`) -> Impact: **243.9** | LOC: 29
- `CAddrDB::LoadAddresses` (@ `src/db.cpp`) -> Impact: **214.2** | LOC: 161
- `ThreadIRCSeed` (@ `src/irc.cpp`) -> Impact: **205.5** | LOC: 108
- `GetOpName` (@ `src/script.h`) -> Impact: **170.2** | LOC: 134
- `AddToWallet` (@ `src/main.cpp`) -> Impact: **152.8** | LOC: 56
  * *Intent:* ////////////////////////////////////////////////////////////////////////////// // // mapWallet //
- `HtmlEscape` (@ `src/ui.cpp`) -> Impact: **122.7** | LOC: 29
- `DecodeBase58` (@ `src/base58.h`) -> Impact: **106.2** | LOC: 45

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `IsValid` (@ `src/net.h`) -> **O(2^N) [Recursive]**
- `DecodeBase58` (@ `src/base58.h`) -> **O(2^N) [Recursive]**
- `CTxDB::LoadBlockIndex` (@ `src/db.cpp`) -> **O(2^N) [Recursive]**
- `DBFlush` (@ `src/db.cpp`) -> **O(2^N) [Recursive]**
- `AddToWallet` (@ `src/main.cpp`) -> **O(2^N) [Recursive]**
  * *Intent:* ////////////////////////////////////////////////////////////////////////////// // // mapWallet //
- `SendMoney` (@ `src/main.cpp`) -> **O(2^N) [Recursive]**
- `IsFinal` (@ `src/main.h`) -> **O(2^N) [Recursive]**
- `CInv` (@ `src/net.h`) -> **O(2^N) [Recursive]**
- `erase` (@ `src/serialize.h`) -> **O(2^N) [Recursive]**
- `erase` (@ `src/serialize.h`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `EvalScript` (@ `src/script.cpp`) -> DB Complexity: **150**
  * *Intent:* // // Script is a stack machine (like Forth) that evaluates a predicate // returning a bool indicating valid or not. There are no loops. // #define st...
- `CheckTransaction` (@ `src/main.h`) -> DB Complexity: **132**
- `CTransaction::DisconnectInputs` (@ `src/main.cpp`) -> DB Complexity: **103**
- `CEditProductDialogBase::CEditProductDial` (@ `src/uibase.cpp`) -> DB Complexity: **89**
- `CEditProductDialog::CEditProductDialog` (@ `src/ui.cpp`) -> DB Complexity: **62**
- `Rewind` (@ `src/serialize.h`) -> DB Complexity: **56**
- `Testuint256AdHoc` (@ `src/uint256.h`) -> DB Complexity: **56**
- `CMainFrameBase::CMainFrameBase` (@ `src/uibase.cpp`) -> DB Complexity: **55**
  * *Intent:* // Distributed under the MIT/X11 software license, see the accompanying // file license.txt or http://www.opensource.org/licenses/mit-license.php. ///...
- `HtmlEscape` (@ `src/ui.cpp`) -> DB Complexity: **43**
- `CSendDialogBase::CSendDialogBase` (@ `src/uibase.cpp`) -> DB Complexity: **38**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 30 | 17949.24 | 50.14% | 61.15% |
| `__monolith__` | 3 | 3.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/base58.h` -> **100.0%** Exposure
- `src/bignum.h` -> **100.0%** Exposure
- `src/script.h` -> **100.0%** Exposure
- `src/serialize.h` -> **100.0%** Exposure
- `src/uibase.h` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/base58.h` -> **100.0%** Exposure
- `src/bignum.h` -> **100.0%** Exposure
- `src/db.cpp` -> **100.0%** Exposure
- `src/db.h` -> **100.0%** Exposure
- `src/irc.cpp` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/uint256.h` -> **0** Orphaned Functions | **126** Duplicates
- `src/ui.cpp` -> **66** Orphaned Functions | **7** Duplicates
- `src/serialize.h` -> **0** Orphaned Functions | **68** Duplicates
- `src/uibase.h` -> **0** Orphaned Functions | **52** Duplicates
- `src/main.h` -> **0** Orphaned Functions | **41** Duplicates

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

### Exploit Generation Surface
- `src/base58.h` -> **20.0%** Exposure
- `src/bignum.h` -> **20.0%** Exposure
- `src/db.cpp` -> **20.0%** Exposure
- `src/db.h` -> **20.0%** Exposure
- `src/irc.cpp` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `src/net.cpp` -> **100.0%** Exposure
### Raw Memory Manipulation
- `src/sha.cpp` -> **0.4943%** Exposure
- `src/main.cpp` -> **0.0021%** Exposure
- `src/util.h` -> **0.0007%** Exposure
- `src/util.cpp` -> **0.0002%** Exposure
- `src/serialize.h` -> **0.0001%** Exposure
### Algorithmic DoS Exposure
- `src/base58.h` -> **100.0%** Exposure
- `src/bignum.h` -> **100.0%** Exposure
- `src/db.cpp` -> **100.0%** Exposure
- `src/db.h` -> **100.0%** Exposure
- `src/irc.cpp` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `104` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/bignum.h` (CPP) -> Cumulative Risk: **784.22**
- **Archetype:** `file_cluster_8` (Distance: 14.313 IQR)
- **Magnitude:** 1100.48 | **LOC:** 499 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `setint64` (Impact: 96.6), `setuint64` (Impact: 58.2), `SetHex` (Impact: 33.5)

### 2. `src/util.h` (CPP) -> Cumulative Risk: **774.71**
- **Archetype:** `file_cluster_11` (Distance: 13.86 IQR)
- **Magnitude:** 409.78 | **LOC:** 400 | **CtrlFlow:** 42.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9943%)
- **Heaviest Functions:** `OutputDebugStringF` (Impact: 34.3), `HexStr` (Impact: 12.5), `HexNumStr` (Impact: 9.5)

### 3. `src/util.cpp` (CPP) -> Cumulative Risk: **765.03**
- **Archetype:** `file_cluster_8` (Distance: 13.072 IQR)
- **Magnitude:** 571.66 | **LOC:** 380 | **CtrlFlow:** 70.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9102%)
- **Heaviest Functions:** `ParseMoney` (Impact: 106.0), `FormatMoney` (Impact: 54.6), `RandAddSeed` (Impact: 29.5)

### 4. `src/key.h` (CPP) -> Cumulative Risk: **758.67**
- **Archetype:** `file_cluster_8` (Distance: 13.168 IQR)
- **Magnitude:** 245.52 | **LOC:** 157 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `Sign` (Impact: 16.4), `CKey` (Impact: 16.3), `GetPrivKey` (Impact: 12.6)

### 5. `src/net.h` (CPP) -> Cumulative Risk: **748.38**
- **Archetype:** `file_cluster_8` (Distance: 12.61 IQR)
- **Magnitude:** 1018.16 | **LOC:** 857 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9714%)
- **Heaviest Functions:** `IsValid` (Impact: 243.9), `operator<` (Impact: 31.0), `AdvertStartPublish` (Impact: 28.7)

### 6. `src/uint256.h` (CPP) -> Cumulative Risk: **745.06**
- **Archetype:** `file_cluster_8` (Distance: 14.851 IQR)
- **Magnitude:** 1719.76 | **LOC:** 751 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `SetHex` (Impact: 56.6), `operator<` (Impact: 40.1), `operator<=` (Impact: 40.1)

### 7. `src/net.cpp` (CPP) -> Cumulative Risk: **744.92**
- **Archetype:** `file_cluster_8` (Distance: 12.508 IQR)
- **Magnitude:** 511.72 | **LOC:** 1068 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `GetMyExternalIP2` (Impact: 69.2), `GetMyExternalIP` (Impact: 56.6), `ConnectSocket` (Impact: 40.6)

### 8. `src/script.h` (CPP) -> Cumulative Risk: **730.67**
- **Archetype:** `file_cluster_8` (Distance: 12.097 IQR)
- **Magnitude:** 620.72 | **LOC:** 598 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `GetOpName` (Impact: 170.2), `GetOp` (Impact: 44.5), `FindAndDelete` (Impact: 25.9)

### 9. `src/base58.h` (CPP) -> Cumulative Risk: **729.21**
- **Archetype:** `file_cluster_8` (Distance: 12.882 IQR)
- **Magnitude:** 328.32 | **LOC:** 202 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `DecodeBase58` (Impact: 106.2), `EncodeBase58` (Impact: 36.5), `DecodeBase58Check` (Impact: 11.3)

### 10. `src/main.h` (CPP) -> Cumulative Risk: **725.19**
- **Archetype:** `file_cluster_8` (Distance: 12.766 IQR)
- **Magnitude:** 1089.22 | **LOC:** 1318 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9993%)
- **Heaviest Functions:** `CheckTransaction` (Impact: 313.2), `IsNewerThan` (Impact: 49.4), `IsFinal` (Impact: 35.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/script.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.904 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 3.715 IQR)
- **Top Global Matches:** file_cluster_8: 12.904, file_cluster_7: 13.318, file_cluster_13: 13.324
- **Magnitude:** 3166.66 | **LOC:** 1128 | **CtrlFlow:** 85.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 150
- **Risk Profile:** Cognitive Load (95.7011%), Tech Debt (9.4392%)
**Top Internal Functions/Classes:**
  * `EvalScript` (Impact: 2616.4 | O(N^6) | DB: 150)
    * *Intent:* // // Script is a stack machine (like Forth) that evaluates a predicate // returning a bool indicati...
  * `SignatureHash` (Impact: 46.2 | O(2^N) | DB: 4)
  * `VerifySignature` (Impact: 10.7 | O(N^2) | DB: 6)
  * `MakeSameSize` (Impact: 4.9 | O(N^2) | DB: 2)
  * `CastToBool` (Impact: 1.9 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 308`, `structural_boundaries: 53`, `args: 18`, `func_start: 5`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 474`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `import: 1`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` headers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.051 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.527 IQR)
- **Top Global Matches:** file_cluster_8: 14.051, file_cluster_7: 14.158, file_cluster_13: 14.229
- **Magnitude:** 1719.96 | **LOC:** 2661 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 103
- **Risk Profile:** Cognitive Load (45.759%), Tech Debt (28.9343%)
**Top Internal Functions/Classes:**
  * `CTransaction::DisconnectInputs` (Impact: 652.9 | O(N^6) | DB: 103)
  * `AddToWallet` (Impact: 152.8 | O(2^N) | DB: 25)
    * *Intent:* ////////////////////////////////////////////////////////////////////////////// // // mapWallet //
  * `CWalletTx::GetTxTime` (Impact: 61.8 | O(N^4) | DB: 14)
  * `SendMoney` (Impact: 61.8 | O(2^N) | DB: 3)
  * `CMerkleTx::GetDepthInMainChain` (Impact: 28.9 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 103`, `args: 52`, `func_start: 54`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 564`, `dead_code: 4`, `orphaned_logic: 13`
* *Architecture:* `io: 3`, `import: 2`
* *Defense:* `safety: 5`, `doc: 162`, `immutability_locks: 36`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` sha.h, headers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/uint256.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 98.79%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.851 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 6.318 IQR)
- **Top Global Matches:** file_cluster_8: 14.851, file_cluster_13: 15.017, file_cluster_7: 15.051
- **Magnitude:** 1719.76 | **LOC:** 751 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 56
- **Risk Profile:** Cognitive Load (38.4697%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `SetHex` (Impact: 56.6 | O(N^4) | DB: 23)
  * `operator<` (Impact: 40.1 | O(N^4) | DB: 4)
  * `operator<=` (Impact: 40.1 | O(N^4) | DB: 4)
  * `operator>` (Impact: 40.1 | O(N^4) | DB: 4)
  * `operator>=` (Impact: 40.1 | O(N^4) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 276`, `args: 48`, `func_start: 140`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 903`, `duplicate_logic: 126`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `doc: 52`, `immutability_locks: 255`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` limits.h, string
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/ui.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.263 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.675 IQR)
- **Top Global Matches:** file_cluster_8: 14.263, file_cluster_7: 14.372, file_cluster_13: 14.503
- **Magnitude:** 1288.86 | **LOC:** 3229 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 62
- **Risk Profile:** Cognitive Load (44.5308%), Tech Debt (99.9492%)
**Top Internal Functions/Classes:**
  * `HtmlEscape` (Impact: 122.7 | O(N^3) | DB: 43)
  * `CEditProductDialog::OnButtonAddField` (Impact: 40.4 | O(N^4) | DB: 3)
    * *Intent:* //CTxDetailsDialog* pdialog = new CTxDetailsDialog(this, wtx); //pdialog->Show();
  * `CRITICAL_BLOCK` (Impact: 35.1 | O(N^4) | DB: 3)
    * *Intent:* //m_listCtrlProductsSent->InsertColumn(0, "Category", wxLIST_FORMAT_LEFT, 100); //m_listCtrlProducts...
  * `CEditProductDialog::SetProduct` (Impact: 33.5 | O(N^3) | DB: 8)
  * `CProductsDialog::OnButtonSearch` (Impact: 33.1 | O(N^5) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 132`, `args: 44`, `func_start: 94`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 1`, `state_mutation: 644`, `dead_code: 1`, `duplicate_logic: 7`, `orphaned_logic: 66`
* *Architecture:* `import: 2`
* *Defense:* `safety: 3`, `doc: 211`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` headers.h, crtdbg.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bignum.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 98.91%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.313 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.851 IQR)
- **Top Global Matches:** file_cluster_8: 14.313, file_cluster_13: 14.525, file_cluster_11: 14.68
- **Magnitude:** 1100.48 | **LOC:** 499 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (74.5809%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `setint64` (Impact: 96.6 | O(N^5) | DB: 26)
  * `setuint64` (Impact: 58.2 | O(N^5) | DB: 22)
  * `SetHex` (Impact: 33.5 | O(N^3) | DB: 17)
  * `setuint256` (Impact: 19.4 | O(N^5) | DB: 22)
  * `getuint256` (Impact: 18.0 | O(N^3) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 82`, `args: 57`, `func_start: 66`, `class_start: 3`
* *Risk/State:* `state_mutation: 574`, `duplicate_logic: 30`
* *Architecture:* `api: 28`, `import: 3`
* *Defense:* `immutability_locks: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` vector, bn.h, stdexcept
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main.h` (CPP | Tier 0 | 🚨 AI THREAT: 98.75%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.766 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.742 IQR)
- **Top Global Matches:** file_cluster_8: 12.766, file_cluster_7: 13.22, file_cluster_13: 13.289
- **Magnitude:** 1089.22 | **LOC:** 1318 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 132
- **Risk Profile:** Cognitive Load (73.9172%), Tech Debt (99.9993%)
**Top Internal Functions/Classes:**
  * `CheckTransaction` (Impact: 313.2 | O(N^6) | DB: 132)
  * `IsNewerThan` (Impact: 49.4 | O(N^5) | DB: 11)
  * `IsFinal` (Impact: 35.1 | O(2^N) | DB: 1)
  * `ToString` (Impact: 16.7 | O(2^N) | DB: 8)
  * `operator==` (Impact: 13.3 | O(N^4) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 114`, `args: 61`, `func_start: 82`, `class_start: 21`
* *Risk/State:* `state_mutation: 498`, `duplicate_logic: 41`
* *Architecture:* `api: 16`
* *Defense:* `immutability_locks: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/net.h` (CPP | Tier 0 | 🚨 AI THREAT: 98.75%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.61 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.099 IQR)
- **Top Global Matches:** file_cluster_8: 12.61, file_cluster_0: 12.774, file_cluster_11: 12.838
- **Magnitude:** 1018.16 | **LOC:** 857 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (55.9634%), Tech Debt (99.9714%)
**Top Internal Functions/Classes:**
  * `IsValid` (Impact: 243.9 | O(2^N) | DB: 3)
  * `operator<` (Impact: 31.0 | O(N^4) | DB: 3)
  * `AdvertStartPublish` (Impact: 28.7 | O(N^4) | DB: 3)
    * *Intent:* // // Templates for the publish and subscription system. // The object being published as T& obj nee...
  * `CInv` (Impact: 25.8 | O(2^N) | DB: 6)
  * `AdvertStopPublish` (Impact: 23.0 | O(N^4) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 143`, `args: 59`, `func_start: 57`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 8`, `state_mutation: 342`, `dead_code: 3`, `duplicate_logic: 27`
* *Architecture:* `api: 24`
* *Defense:* `safety: 10`, `doc: 1`, `immutability_locks: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/serialize.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 98.72%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.6 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 6.136 IQR)
- **Top Global Matches:** file_cluster_16: 13.6, file_cluster_8: 13.767, file_cluster_13: 13.851
- **Magnitude:** 790.94 | **LOC:** 1152 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 56
- **Risk Profile:** Cognitive Load (48.6015%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Rewind` (Impact: 57.8 | O(N^3) | DB: 56)
  * `erase` (Impact: 25.9 | O(2^N) | DB: 2)
  * `erase` (Impact: 20.8 | O(2^N) | DB: 2)
  * `WriteCompactSize` (Impact: 19.7 | O(N^2) | DB: 7)
  * `ReadCompactSize` (Impact: 19.6 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 405`, `args: 111`, `func_start: 102`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 417`, `duplicate_logic: 68`
* *Architecture:* `io: 6`, `api: 5`, `import: 3`
* *Defense:* `doc: 21`, `immutability_locks: 68`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` iostream, is_fundamental.hpp, vector, map
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/db.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.537 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.012 IQR)
- **Top Global Matches:** file_cluster_8: 12.537, file_cluster_13: 12.828, file_cluster_0: 12.858
- **Magnitude:** 752.54 | **LOC:** 609 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (80.8985%), Tech Debt (99.9818%)
**Top Internal Functions/Classes:**
  * `CAddrDB::LoadAddresses` (Impact: 214.2 | O(N^6) | DB: 18)
  * `CDB::CDB` (Impact: 94.7 | O(N^6) | DB: 26)
  * `CTxDB::LoadBlockIndex` (Impact: 83.4 | O(2^N) | DB: 22)
  * `DBFlush` (Impact: 62.2 | O(2^N) | DB: 7)
  * `CTxDB::ReadOwnerTxes` (Impact: 32.2 | O(N^4) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 42`, `args: 13`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 213`, `dead_code: 2`, `fragile_debt: 1`, `duplicate_logic: 6`, `orphaned_logic: 15`
* *Architecture:* `io: 2`, `api: 1`, `import: 1`
* *Defense:* `safety: 9`, `doc: 6`, `immutability_locks: 9`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` headers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/script.h` (CPP | Tier 0 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.097 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.122 IQR)
- **Top Global Matches:** file_cluster_8: 12.097, file_cluster_0: 12.501, file_cluster_13: 12.501
- **Magnitude:** 620.72 | **LOC:** 598 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (80.6458%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `GetOpName` (Impact: 170.2 | O(N^2))
  * `GetOp` (Impact: 44.5 | O(N^5) | DB: 21)
  * `FindAndDelete` (Impact: 25.9 | O(N^4) | DB: 8)
  * `ToString` (Impact: 25.9 | O(N^4) | DB: 4)
  * `operator<<` (Impact: 11.0 | O(N^3) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 164`, `args: 33`, `func_start: 48`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 218`, `dead_code: 2`, `duplicate_logic: 36`
* *Architecture:* `api: 7`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/util.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.072 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.394 IQR)
- **Top Global Matches:** file_cluster_8: 13.072, file_cluster_13: 13.446, file_cluster_7: 13.48
- **Magnitude:** 571.66 | **LOC:** 380 | **CtrlFlow:** 70.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (72.6173%), Tech Debt (99.9102%)
**Top Internal Functions/Classes:**
  * `ParseMoney` (Impact: 106.0 | O(N^4) | DB: 25)
  * `FormatMoney` (Impact: 54.6 | O(N^3) | DB: 6)
  * `RandAddSeed` (Impact: 29.5 | O(2^N) | DB: 13)
  * `strprintf` (Impact: 29.3 | O(N^3) | DB: 7)
  * `AddTimeData` (Impact: 25.8 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 28`, `args: 23`, `func_start: 17`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 235`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 11`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 2`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` headers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/irc.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.339 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.266 IQR)
- **Top Global Matches:** file_cluster_8: 12.339, file_cluster_13: 12.784, file_cluster_7: 12.854
- **Magnitude:** 518.84 | **LOC:** 289 | **CtrlFlow:** 66.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (77.4427%), Tech Debt (13.7145%)
**Top Internal Functions/Classes:**
  * `ThreadIRCSeed` (Impact: 205.5 | O(N^6) | DB: 17)
  * `RecvLine` (Impact: 53.7 | O(N^4) | DB: 19)
  * `RecvUntil` (Impact: 36.6 | O(N^3) | DB: 8)
  * `RecvLineIRC` (Impact: 22.8 | O(N^4) | DB: 4)
  * `Send` (Impact: 14.6 | O(N^3) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 32`, `args: 18`, `func_start: 9`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 153`, `orphaned_logic: 1`
* *Architecture:* `io: 4`, `import: 1`
* *Defense:* `test: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` headers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/net.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.508 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.183 IQR)
- **Top Global Matches:** file_cluster_8: 12.508, file_cluster_13: 12.883, file_cluster_7: 13.038
- **Magnitude:** 511.72 | **LOC:** 1068 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (72.1154%), Tech Debt (49.7605%)
**Top Internal Functions/Classes:**
  * `GetMyExternalIP2` (Impact: 69.2 | O(N^5) | DB: 10)
  * `GetMyExternalIP` (Impact: 56.6 | O(N^5) | DB: 15)
  * `ConnectSocket` (Impact: 40.6 | O(N^3) | DB: 28)
  * `CNode::CancelSubscribe` (Impact: 38.0 | O(N^5) | DB: 9)
  * `AbandonRequests` (Impact: 31.4 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 43`, `args: 23`, `func_start: 16`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 189`, `orphaned_logic: 6`
* *Architecture:* `io: 4`, `import: 2`
* *Defense:* `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` winsock2.h, headers.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/uibase.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.151 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 6.929 IQR)
- **Top Global Matches:** file_cluster_8: 13.151, file_cluster_7: 13.403, file_cluster_1: 13.675
- **Magnitude:** 486.22 | **LOC:** 1807 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 89
- **Risk Profile:** Cognitive Load (28.4173%), Tech Debt (22.9357%)
**Top Internal Functions/Classes:**
  * `CAboutDialogBase::CAboutDialogBase` (Impact: 6.2 | O(N^1) | DB: 12)
  * `CSendDialogBase::CSendDialogBase` (Impact: 6.2 | O(N^1) | DB: 38)
  * `CYourAddressDialogBase::CYourAddressDial` (Impact: 4.3 | O(N^1) | DB: 15)
  * `CEditProductDialogBase::CEditProductDial` (Impact: 4.3 | O(N^1) | DB: 89)
  * `CMainFrameBase` (Impact: 3.8 | O(2^N))
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

### `src/uibase.h` (CPP | Tier 0 | 🚨 AI THREAT: 99.01%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.15 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 5.573 IQR)
- **Top Global Matches:** file_cluster_13: 14.15, file_cluster_7: 14.336, file_cluster_12: 14.413
- **Magnitude:** 465.1 | **LOC:** 721 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `OnClose` (Impact: 1.1 | O(N^1) | DB: 1)
    * *Intent:* // Virtual event handlers, overide them in your derived class
  * `OnIdle` (Impact: 1.1 | O(N^1) | DB: 1)
  * `OnMouseEvents` (Impact: 1.1 | O(N^1) | DB: 1)
  * `OnPaint` (Impact: 1.1 | O(N^1) | DB: 1)
  * `OnMenuFileExit` (Impact: 1.1 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 250`, `func_start: 117`, `class_start: 16`
* *Risk/State:* `state_mutation: 245`, `duplicate_logic: 52`
* *Architecture:* `api: 81`, `import: 28`
* *Defense:* `doc: 923`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 48.102
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.173611
  * `Imports (Out-Degree: 0):` textctrl.h, checkbox.h, htmlwin.h, image.h, button.h, combobox.h, notebook.h, colour.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/db.h` (CPP | Tier 0 | 🚨 AI THREAT: 98.79%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.344 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.798 IQR)
- **Top Global Matches:** file_cluster_8: 12.344, file_cluster_13: 12.69, file_cluster_0: 12.755
- **Magnitude:** 415.16 | **LOC:** 421 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (78.5145%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ReadAtCursor` (Impact: 51.1 | O(N^3) | DB: 8)
  * `Write` (Impact: 13.3 | O(N^3) | DB: 8)
  * `Erase` (Impact: 12.9 | O(N^3) | DB: 4)
  * `GetCursor` (Impact: 12.5 | O(N^3) | DB: 3)
  * `TxnBegin` (Impact: 11.9 | O(N^3) | DB: 3)
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

### `src/util.h` (CPP | Tier 0 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.86 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.32 IQR)
- **Top Global Matches:** file_cluster_11: 13.86, file_cluster_8: 13.886, file_cluster_0: 14.01
- **Magnitude:** 409.78 | **LOC:** 400 | **CtrlFlow:** 42.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (83.9658%), Tech Debt (99.9943%)
**Top Internal Functions/Classes:**
  * `OutputDebugStringF` (Impact: 34.3 | O(N^3) | DB: 23)
    * *Intent:* #else
  * `HexStr` (Impact: 12.5 | O(N^2) | DB: 9)
  * `HexNumStr` (Impact: 9.5 | O(N^2) | DB: 8)
  * `Hash` (Impact: 8.7 | O(N^5) | DB: 11)
  * `Hash` (Impact: 7.4 | O(N^5) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 63`, `args: 25`, `func_start: 30`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 268`, `dead_code: 1`, `duplicate_logic: 13`
* *Architecture:* `io: 2`, `api: 15`
* *Defense:* `safety: 4`, `immutability_locks: 33`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/base58.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 98.75%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.882 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.202 IQR)
- **Top Global Matches:** file_cluster_8: 12.882, file_cluster_13: 13.354, file_cluster_7: 13.383
- **Magnitude:** 328.32 | **LOC:** 202 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (77.4089%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `DecodeBase58` (Impact: 106.2 | O(2^N) | DB: 21)
  * `EncodeBase58` (Impact: 36.5 | O(2^N) | DB: 14)
    * *Intent:* // Copyright (c) 2009 Satoshi Nakamoto // Distributed under the MIT/X11 software license, see the ac...
  * `DecodeBase58Check` (Impact: 11.3 | O(N^2) | DB: 4)
  * `AddressToHash160` (Impact: 11.0 | O(N^2) | DB: 4)
  * `EncodeBase58` (Impact: 2.2 | O(2^N) | DB: 3)
    * *Intent:* // Convert little endian string to big endian
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 33`, `args: 9`, `func_start: 13`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 142`, `duplicate_logic: 10`
* *Architecture:* `api: 1`
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/key.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.168 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.766 IQR)
- **Top Global Matches:** file_cluster_8: 13.168, file_cluster_13: 13.61, file_cluster_0: 13.621
- **Magnitude:** 245.52 | **LOC:** 157 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (58.5104%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `Sign` (Impact: 16.4 | O(2^N) | DB: 2)
  * `CKey` (Impact: 16.3 | O(2^N) | DB: 3)
  * `GetPrivKey` (Impact: 12.6 | O(2^N) | DB: 4)
  * `GetPubKey` (Impact: 12.6 | O(2^N) | DB: 4)
  * `CKey` (Impact: 11.6 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 20`, `args: 9`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 118`, `duplicate_logic: 7`
* *Architecture:* `api: 3`
* *Defense:* `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.308
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.148897
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/ui.h` (CPP | Tier 0 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.124 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.383 IQR)
- **Top Global Matches:** file_cluster_8: 11.124, file_cluster_7: 11.445, file_cluster_13: 11.696
- **Magnitude:** 192.9 | **LOC:** 419 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (40.0897%), Tech Debt (94.9722%)
**Top Internal Functions/Classes:**
  * `OnKeyDown` (Impact: 8.3 | O(N^3) | DB: 1)
  * `CGetTextFromUserDialog` (Impact: 7.9 | O(N^6) | DB: 8)
    * *Intent:* /** Constructor */
  * `GetValue` (Impact: 2.0 | O(2^N))
    * *Intent:* // Custom
  * `OnKeyDown` (Impact: 1.1 | O(N^1) | DB: 1)
  * `OnKeyDown` (Impact: 1.1 | O(N^1) | DB: 1)
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

### `src/market.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.65 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 4.583 IQR)
- **Top Global Matches:** file_cluster_13: 13.65, file_cluster_8: 13.666, file_cluster_11: 13.853
- **Magnitude:** 166.66 | **LOC:** 265 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (33.278%), Tech Debt (91.2033%)
**Top Internal Functions/Classes:**
  * `AddAtomsAndPropagate` (Impact: 35.5 | O(N^4) | DB: 19)
  * `CUser::AddAtom` (Impact: 29.4 | O(N^3))
  * `AdvertInsert` (Impact: 13.4 | O(N^3) | DB: 10)
  * `Union` (Impact: 8.1 | O(N^3) | DB: 4)
  * `AdvertErase` (Impact: 3.4 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 10`, `args: 7`, `func_start: 6`
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
- **Algorithmic:** O(N) | **DB Complexity:** 0
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
- **Global Archetype:** `file_cluster_8` (Drift: 11.81 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.293 IQR)
- **Top Global Matches:** file_cluster_8: 11.81, file_cluster_12: 12.075, file_cluster_7: 12.435
- **Magnitude:** 95.08 | **LOC:** 555 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (99.7527%), Tech Debt (23.6089%)
**Top Internal Functions/Classes:**
  * `SHA512::Transform` (Impact: 17.6 | O(N^2) | DB: 15)
  * `SHA1::InitState` (Impact: 2.1 | O(N^1) | DB: 5)
    * *Intent:* // This file is public domain // SHA routines extracted as a standalone file from: // Crypto++: a C+...
  * `SHA1::Transform` (Impact: 2.0 | O(N^1) | DB: 10)
  * `SHA512_SSE2_Transform` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 60`, `args: 98`, `func_start: 4`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 67`, `orphaned_logic: 3`
* *Architecture:* `io: 4`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 20.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` assert.h, sha.h, memory.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/market.h` (CPP | Tier 0 | 🚨 AI THREAT: 98.79%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.454 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.809 IQR)
- **Top Global Matches:** file_cluster_8: 10.454, file_cluster_7: 11.097, file_cluster_13: 11.245
- **Magnitude:** 67.08 | **LOC:** 183 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (59.2249%), Tech Debt (99.9997%)
**Top Internal Functions/Classes:**
  * `IMPLEMENT_SERIALIZE` (Impact: 8.6 | O(N^3) | DB: 2)
  * `SetNull` (Impact: 1.9 | O(N^2))
  * `CReview` (Impact: 1.9 | O(N^2) | DB: 4)
  * `CProduct` (Impact: 1.8 | O(N^2) | DB: 3)
  * `GetAtomCount` (Impact: 1.7 | O(N^2))
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
- **Global Archetype:** `file_cluster_8` (Drift: 10.785 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 2.977 IQR)
- **Top Global Matches:** file_cluster_8: 10.785, file_cluster_13: 11.137, file_cluster_0: 11.226
- **Magnitude:** 44.5 | **LOC:** 178 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (66.2154%), Tech Debt (99.9997%)
**Top Internal Functions/Classes:**
  * `ByteReverse` (Impact: 3.5 | O(N^1) | DB: 2)
  * `ByteReverse` (Impact: 2.1 | O(N^1))
  * `ByteReverse` (Impact: 1.2 | O(N^1))
    * *Intent:* #define CRYPTOPP_FAST_ROTATE(x) ((x) == 32) #elif defined(__GNUC__) && (CRYPTOPP_BOOL_X64 || CRYPTOP...
  * `public` (Impact: 1.2 | O(N^1))
  * `public` (Impact: 1.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 21`, `args: 6`, `func_start: 8`
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
- `src/util.h` (CPP) | Magnitude: 409.78 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 268, indent_spaces: 149, structural_boundaries: 63, branch: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/market.cpp` (CPP) | Magnitude: 166.66 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 75, indent_spaces: 73, branch: 14, structural_boundaries: 10
- `src/uibase.h` (CPP) | Magnitude: 465.1 | Delta: **0.186 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 923, indent_spaces: 341, structural_boundaries: 250, state_mutation: 245
- `src/headers.h` (CPP) | Magnitude: 16.28 | Delta: **0.257 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: import: 50, macros: 10, structural_boundaries: 4, reflection_metaprogramming: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/serialize.h` (CPP) | Magnitude: 790.94 | Delta: **0.167 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 417, structural_boundaries: 405, indent_spaces: 296, args: 111

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/main.cpp` (CPP) | Magnitude: 1719.96 | Delta: **0.107 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 710, state_mutation: 564, branch: 182, doc: 162
- `src/ui.cpp` (CPP) | Magnitude: 1288.86 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 644, indent_spaces: 591, doc: 211, pointers: 151
- `src/net.h` (CPP) | Magnitude: 1018.16 | Delta: **0.164 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 547, state_mutation: 342, structural_boundaries: 143, branch: 69
- `src/uint256.h` (CPP) | Magnitude: 1719.76 | Delta: **0.166 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 903, indent_spaces: 473, structural_boundaries: 276, immutability_locks: 255
- `src/bignum.h` (CPP) | Magnitude: 1100.48 | Delta: **0.212 IQR** | Secondary Pull: `file_cluster_13`
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

- `src/uint256.h` -> **Severity: 14.851** (Embedded: 0.1489 * Error Risk: 99.7395%)
- `src/bignum.h` -> **Severity: 14.769** (Embedded: 0.1489 * Error Risk: 99.1924%)
- `src/key.h` -> **Severity: 14.301** (Embedded: 0.1489 * Error Risk: 96.0474%)
- `src/base58.h` -> **Severity: 14.13** (Embedded: 0.1489 * Error Risk: 94.8975%)
- `src/util.h` -> **Severity: 13.829** (Embedded: 0.1489 * Error Risk: 92.8784%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/key.h` -> **Severity: 3030.8** (Blast Radius: 30.308 * Doc Risk: 100.0%)
- `src/bignum.h` -> **Severity: 3030.297** (Blast Radius: 30.308 * Doc Risk: 99.9834%)
- `src/uint256.h` -> **Severity: 3029.821** (Blast Radius: 30.308 * Doc Risk: 99.9677%)
- `src/db.h` -> **Severity: 3029.306** (Blast Radius: 30.308 * Doc Risk: 99.9507%)
- `src/net.h` -> **Severity: 3028.851** (Blast Radius: 30.308 * Doc Risk: 99.9357%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
