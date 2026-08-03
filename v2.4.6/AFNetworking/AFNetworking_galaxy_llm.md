# ARCHITECTURAL_BRIEF: AFNetworking
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/AFNetworking` |
| **Timestamp** | `2026-08-03T19:04:27.017972+00:00` |
| **Scan Duration** | `0.61s` |
| **Git Branch** | `master` |
| **Git Commit** | `d9f589cc2c1fe9d55eb5eea00558010afea7a41e` |
| **Git Remote** | `https://github.com/AFNetworking/AFNetworking.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 80 malicious artifacts.

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
| Total Artifacts | 211 |
| Analyzed Artifacts (Scanned) | 128 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 83 |
| Total LOC | 8973 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 60.7% |
| Dominant Lang | PLAINTEXT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4755 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2374 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.8177 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| OBJECTIVE-C | 74 | 8797 | 57.8% |
| PLAINTEXT | 28 | 28 | 21.9% |
| XML | 16 | 0 | 12.5% |
| MARKDOWN | 4 | 0 | 3.1% |
| SWIFT | 4 | 140 | 3.1% |
| RUBY | 2 | 8 | 1.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.897`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 36 | 28.1% |
| file_cluster_13 | 32 | 25.0% |
| Unknown | 28 | 21.9% |
| file_cluster_0 | 19 | 14.8% |
| file_cluster_4 | 6 | 4.7% |
| file_cluster_16 | 3 | 2.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 3.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 83*

**Composition by Extension & Reason:**
- `.json`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 14x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.xcworkspacedata'), 1x Excluded (Unsupported Extension: '.entitlements')
- `.xcscheme`: 9x Excluded (Unsupported Extension: '.xcscheme')
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pbxproj`: 3x Excluded (Unsupported Extension: '.pbxproj')
- `.h`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.m`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pch`: 2x Excluded (Unsupported Extension: '.pch')
- `.podspec`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.modulemap`: 1x Excluded (Unsupported Extension: '.modulemap')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.catalyst`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.default`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.7 | 28.2 | 5.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 82.5 | 23.1 | 9.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 17.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.0 | 0.0 | 0.0 |
| API Exposure | 0.0 | 11.1 | 3.1 | 2.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 14.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 18.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 74.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 20.0 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 36.9 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 7.4 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.1 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `AFNetworking/AFURLSessionManager.m` (Hits: 70)
- `Tests/Tests/AFSecurityPolicyTests.m` (Hits: 42)
- `AFNetworking/AFURLRequestSerialization.m` (Hits: 22)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **AFTestCase.h** (`Tests/Tests/AFTestCase.h`) — 21 inbound connections
2. **AFURLResponseSerialization.h** (`AFNetworking/AFURLResponseSerialization.h`) — 13 inbound connections
3. **AFURLRequestSerialization.h** (`AFNetworking/AFURLRequestSerialization.h`) — 11 inbound connections
4. **AFURLSessionManager.h** (`AFNetworking/AFURLSessionManager.h`) — 11 inbound connections
5. **AFHTTPSessionManager.h** (`AFNetworking/AFHTTPSessionManager.h`) — 8 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **AFNetworking.h** (`Framework/AFNetworking.h`) — 19 outbound dependencies
2. **AFHTTPSessionManager.m** (`AFNetworking/AFHTTPSessionManager.m`) — 13 outbound dependencies
3. **UIKit+AFNetworking.h** (`UIKit+AFNetworking/UIKit+AFNetworking.h`) — 10 outbound dependencies
4. **AFNetworking.h** (`AFNetworking/AFNetworking.h`) — 9 outbound dependencies
5. **AFNetworkReachabilityManager.m** (`AFNetworking/AFNetworkReachabilityManager.m`) — 6 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `downloadImageForURLRequest` (@ `UIKit+AFNetworking/AFImageDownloader.m`) -> Impact: **187.6** | LOC: 115
- `evaluateServerTrust` (@ `AFNetworking/AFSecurityPolicy.m`) -> Impact: **171.9** | LOC: 73
  * *Intent:* #pragma mark -
- `init` (@ `AFNetworking/AFURLRequestSerialization.m`) -> Impact: **158.5** | LOC: 53
- `AFJSONObjectByRemovingKeysWithNullValues` (@ `AFNetworking/AFURLResponseSerialization.m`) -> Impact: **148.5** | LOC: 26
- `requestBySerializingRequest` (@ `AFNetworking/AFURLRequestSerialization.m`) -> Impact: **147.6** | LOC: 42
- `read` (@ `AFNetworking/AFURLRequestSerialization.m`) -> Impact: **147.1** | LOC: 32
- `AFInflatedImageFromResponseWithDataAtSca` (@ `AFNetworking/AFURLResponseSerialization.m`) -> Impact: **134.6** | LOC: 91
- `URLSession` (@ `AFNetworking/AFURLSessionManager.m`) -> Impact: **129.8** | LOC: 75
  * *Intent:* #pragma mark - NSURLSessionTaskDelegate
- `requestBySerializingRequest` (@ `AFNetworking/AFURLRequestSerialization.m`) -> Impact: **123.9** | LOC: 53
- `URLSession` (@ `AFNetworking/AFURLSessionManager.m`) -> Impact: **123.5** | LOC: 46

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `GET` (@ `AFNetworking/AFHTTPSessionManager.m`) -> **O(2^N) [Recursive]**
  * *Intent:* #pragma mark -
- `POST` (@ `AFNetworking/AFHTTPSessionManager.m`) -> **O(2^N) [Recursive]**
- `PATCH` (@ `AFNetworking/AFHTTPSessionManager.m`) -> **O(2^N) [Recursive]**
- `DELETE` (@ `AFNetworking/AFHTTPSessionManager.m`) -> **O(2^N) [Recursive]**
- `init` (@ `AFNetworking/AFNetworkReachabilityManager.m`) -> **O(2^N) [Recursive]**
- `requestBySerializingRequest` (@ `AFNetworking/AFURLRequestSerialization.m`) -> **O(2^N) [Recursive]**
- `requestBySerializingRequest` (@ `AFNetworking/AFURLRequestSerialization.m`) -> **O(2^N) [Recursive]**
- `appendPartWithFileURL` (@ `AFNetworking/AFURLRequestSerialization.m`) -> **O(2^N) [Recursive]**
- `responseObjectForResponse` (@ `AFNetworking/AFURLResponseSerialization.m`) -> **O(2^N) [Recursive]**
  * *Intent:* #pragma mark - AFURLResponseSerialization
- `uploadTaskWithRequest` (@ `AFNetworking/AFURLSessionManager.m`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `AFInflatedImageFromResponseWithDataAtSca` (@ `AFNetworking/AFURLResponseSerialization.m`) -> DB Complexity: **28**
- `read` (@ `AFNetworking/AFURLRequestSerialization.m`) -> DB Complexity: **23**
- `URLSession` (@ `AFNetworking/AFURLSessionManager.m`) -> DB Complexity: **21**
- `init` (@ `AFNetworking/AFURLRequestSerialization.m`) -> DB Complexity: **19**
- `appendPartWithFileURL` (@ `AFNetworking/AFURLRequestSerialization.m`) -> DB Complexity: **17**
- `testThatImageCacheIsPromptedShouldCacheN` (@ `Tests/Tests/AFImageDownloaderTests.m`) -> DB Complexity: **17**
- `testPolicyWithPublicKeyPinningAllowsHTTP` (@ `Tests/Tests/AFSecurityPolicyTests.m`) -> DB Complexity: **17**
- `testPolicyWithCertificatePinningAllowsHT` (@ `Tests/Tests/AFSecurityPolicyTests.m`) -> DB Complexity: **17**
- `downloadImageForURLRequest` (@ `UIKit+AFNetworking/AFImageDownloader.m`) -> DB Complexity: **17**
- `contentLength` (@ `AFNetworking/AFURLRequestSerialization.m`) -> DB Complexity: **16**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `Tests/Resources/Google.com` | 5 | 25000.0 | 0.0% | 0.0% |
| `Tests/Resources/HTTPBin.org` | 4 | 20000.0 | 0.0% | 0.0% |
| `Tests/Resources/HTTPBin.org/HTTPBinOrgServerTrustChain` | 4 | 20000.0 | 0.0% | 0.0% |
| `Example/Certificates` | 3 | 15000.0 | 0.0% | 0.0% |
| `Tests/Resources/ADN.net/ADNNetServerTrustChain` | 3 | 15000.0 | 0.0% | 0.0% |
| `Tests/Resources/Google.com/GoogleComServerTrustChainPath2` | 3 | 15000.0 | 0.0% | 0.0% |
| `Tests/Resources/SelfSigned` | 3 | 15000.0 | 0.0% | 0.0% |
| `Tests/Resources/Google.com/GoogleComServerTrustChainPath1` | 2 | 10000.0 | 0.0% | 0.0% |
| `AFNetworking` | 14 | 7961.6 | 39.25% | 40.7% |
| `fastlane` | 2 | 5001.28 | 2.5% | 50.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `AFNetworking/AFURLResponseSerialization.m` -> **100.0%** Exposure
- `Gemfile` -> **100.0%** Exposure
- `fastlane/Fastfile` -> **100.0%** Exposure
- `AFNetworking/AFURLRequestSerialization.m` -> **99.9993%** Exposure
- `UIKit+AFNetworking/UIRefreshControl+AFNetworking.m` -> **99.9715%** Exposure
### Highest State Flux (Mutation/Volatility)
- `AFNetworking/AFNetworkReachabilityManager.m` -> **100.0%** Exposure
- `AFNetworking/AFSecurityPolicy.m` -> **100.0%** Exposure
- `AFNetworking/AFURLRequestSerialization.m` -> **100.0%** Exposure
- `AFNetworking/AFURLResponseSerialization.m` -> **100.0%** Exposure
- `AFNetworking/AFURLSessionManager.m` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `AFNetworking/AFURLRequestSerialization.m` -> **25** Orphaned Functions | **29** Duplicates
- `AFNetworking/AFURLSessionManager.m` -> **27** Orphaned Functions | **26** Duplicates
- `Tests/Tests/AFSecurityPolicyTests.m` -> **19** Orphaned Functions | **29** Duplicates
- `AFNetworking/AFURLResponseSerialization.m` -> **2** Orphaned Functions | **41** Duplicates
- `Tests/Tests/AFHTTPSessionManagerTests.m` -> **29** Orphaned Functions | **12** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`AFNetworking/AFHTTPSessionManager.m`** -> AI Confidence: **99.48%**
2. **`AFNetworking/AFNetworking.h`** -> AI Confidence: **99.48%**
3. **`UIKit+AFNetworking/UIKit+AFNetworking.h`** -> AI Confidence: **99.48%**
4. **`Framework/AFNetworking.h`** -> AI Confidence: **99.44%**
5. **`AFNetworking/AFNetworkReachabilityManager.m`** -> AI Confidence: **99.34%**
6. **`AFNetworking/AFURLResponseSerialization.m`** -> AI Confidence: **99.34%**
7. **`AFNetworking/AFURLRequestSerialization.m`** -> AI Confidence: **99.32%**
8. **`Example/main.m`** -> AI Confidence: **99.32%**
9. **`Tests/Tests/AFURLSessionManagerTests.m`** -> AI Confidence: **99.32%**
10. **`UIKit+AFNetworking/AFImageDownloader.m`** -> AI Confidence: **99.32%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `Example/tvOS Example/ViewController.swift` -> **100.0%** Exposure
- `AFNetworking/AFHTTPSessionManager.m` -> **20.0%** Exposure
- `AFNetworking/AFNetworkReachabilityManager.m` -> **20.0%** Exposure
- `AFNetworking/AFSecurityPolicy.m` -> **20.0%** Exposure
- `AFNetworking/AFURLRequestSerialization.m` -> **20.0%** Exposure
### Raw Memory Manipulation
- `AFNetworking/AFURLRequestSerialization.h` -> **0.0836%** Exposure
- `Tests/Tests/AFJSONSerializationTests.m` -> **0.0018%** Exposure
### Algorithmic DoS Exposure
- `AFNetworking/AFHTTPSessionManager.m` -> **100.0%** Exposure
- `AFNetworking/AFNetworkReachabilityManager.m` -> **100.0%** Exposure
- `AFNetworking/AFSecurityPolicy.m` -> **100.0%** Exposure
- `AFNetworking/AFURLRequestSerialization.m` -> **100.0%** Exposure
- `AFNetworking/AFURLResponseSerialization.m` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `250` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `AFNetworking/AFURLRequestSerialization.m` (OBJECTIVE-C) -> Cumulative Risk: **842.45**
- **Archetype:** `file_cluster_0` (Distance: 14.134 IQR)
- **Magnitude:** 2427.8 | **LOC:** 1398 | **CtrlFlow:** 85.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Concurrency (99.9999%)
- **Heaviest Functions:** `init` (Impact: 158.5), `requestBySerializingRequest` (Impact: 147.6), `read` (Impact: 147.1)

### 2. `UIKit+AFNetworking/UIProgressView+AFNetworking.m` (OBJECTIVE-C) -> Cumulative Risk: **834.43**
- **Archetype:** `file_cluster_4` (Distance: 12.625 IQR)
- **Magnitude:** 173.6 | **LOC:** 127 | **CtrlFlow:** 90.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9998%), Algorithmic Dos (99.2544%)
- **Heaviest Functions:** `observeValueForKeyPath` (Impact: 80.8), `setProgressWithUploadProgressOfTask` (Impact: 18.8), `setProgressWithDownloadProgressOfTask` (Impact: 18.8)

### 3. `UIKit+AFNetworking/AFNetworkActivityIndicatorManager.m` (OBJECTIVE-C) -> Cumulative Risk: **808.95**
- **Archetype:** `file_cluster_4` (Distance: 12.387 IQR)
- **Magnitude:** 308.78 | **LOC:** 240 | **CtrlFlow:** 87.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9984%)
- **Heaviest Functions:** `setCurrentState` (Impact: 47.9), `updateCurrentStateForNetworkActivityChan` (Impact: 43.2), `setNetworkActivityIndicatorVisible` (Impact: 23.2)

### 4. `UIKit+AFNetworking/WKWebView+AFNetworking.m` (OBJECTIVE-C) -> Cumulative Risk: **797.19**
- **Archetype:** `file_cluster_4` (Distance: 13.912 IQR)
- **Magnitude:** 194.92 | **LOC:** 155 | **CtrlFlow:** 65.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `loadRequest` (Impact: 45.5), `loadRequest` (Impact: 44.4), `sessionManager` (Impact: 16.1)

### 5. `AFNetworking/AFURLResponseSerialization.m` (OBJECTIVE-C) -> Cumulative Risk: **773.76**
- **Archetype:** `file_cluster_8` (Distance: 14.686 IQR)
- **Magnitude:** 1655.0 | **LOC:** 837 | **CtrlFlow:** 90.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `AFJSONObjectByRemovingKeysWithNullValues` (Impact: 148.5), `AFInflatedImageFromResponseWithDataAtSca` (Impact: 134.6), `validateResponse` (Impact: 99.5)

### 6. `UIKit+AFNetworking/AFAutoPurgingImageCache.m` (OBJECTIVE-C) -> Cumulative Risk: **770.75**
- **Archetype:** `file_cluster_4` (Distance: 13.265 IQR)
- **Magnitude:** 227.84 | **LOC:** 206 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Concurrency (99.9972%)
- **Heaviest Functions:** `addImage` (Impact: 38.1), `removeImageWithIdentifier` (Impact: 11.0), `removeAllImages` (Impact: 10.9)

### 7. `UIKit+AFNetworking/UIActivityIndicatorView+AFNetworking.m` (OBJECTIVE-C) -> Cumulative Risk: **767.1**
- **Archetype:** `file_cluster_13` (Distance: 13.048 IQR)
- **Magnitude:** 85.0 | **LOC:** 115 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9999%), State Flux (99.9979%), Tech Debt (99.9613%)
- **Heaviest Functions:** `setAnimatingWithStateOfTask` (Impact: 22.8), `af_notificationObserver` (Impact: 16.0), `initWithActivityIndicatorView` (Impact: 8.2)

### 8. `UIKit+AFNetworking/AFImageDownloader.m` (OBJECTIVE-C) -> Cumulative Risk: **748.44**
- **Archetype:** `file_cluster_4` (Distance: 13.701 IQR)
- **Magnitude:** 665.66 | **LOC:** 422 | **CtrlFlow:** 78.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `downloadImageForURLRequest` (Impact: 187.6), `cancelTaskForImageDownloadReceipt` (Impact: 27.3), `safelyStartNextTaskIfNecessary` (Impact: 26.6)

### 9. `AFNetworking/AFURLSessionManager.m` (OBJECTIVE-C) -> Cumulative Risk: **740.65**
- **Archetype:** `file_cluster_0` (Distance: 14.394 IQR)
- **Magnitude:** 1672.2 | **LOC:** 1275 | **CtrlFlow:** 83.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Concurrency (99.997%)
- **Heaviest Functions:** `URLSession` (Impact: 129.8), `URLSession` (Impact: 123.5), `URLSession` (Impact: 61.9)

### 10. `AFNetworking/AFNetworkReachabilityManager.m` (OBJECTIVE-C) -> Cumulative Risk: **738.48**
- **Archetype:** `file_cluster_4` (Distance: 13.769 IQR)
- **Magnitude:** 347.86 | **LOC:** 270 | **CtrlFlow:** 83.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `AFStringFromNetworkReachabilityStatus` (Impact: 44.6), `AFNetworkReachabilityStatusForFlags` (Impact: 34.1), `keyPathsForValuesAffectingValueForKey` (Impact: 31.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `Example/Certificates/adn.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Example/Certificates/digicert_ca_3.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Example/Certificates/root_ca.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/ADN.net/ADNNetServerTrustChain/adn_0.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/ADN.net/ADNNetServerTrustChain/adn_1.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/ADN.net/ADNNetServerTrustChain/adn_2.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Google.com/Equifax_Secure_Certificate_Authority_Root.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Google.com/GeoTrust_Global_CA-cross.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Google.com/GeoTrust_Global_CA_Root.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Google.com/GoogleComServerTrustChainPath1/googlecom_0.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Google.com/GoogleComServerTrustChainPath1/googlecom_1.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Google.com/GoogleComServerTrustChainPath2/googlecom_0.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Google.com/GoogleComServerTrustChainPath2/googlecom_1.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Google.com/GoogleComServerTrustChainPath2/googlecom_2.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Google.com/GoogleInternetAuthorityG2.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/Google.com/google.com.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/HTTPBin.org/Amazon Root CA 1.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/HTTPBin.org/Amazon.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/HTTPBin.org/HTTPBinOrgServerTrustChain/httpbin_0.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/HTTPBin.org/HTTPBinOrgServerTrustChain/httpbin_1.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/HTTPBin.org/HTTPBinOrgServerTrustChain/httpbin_2.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/HTTPBin.org/HTTPBinOrgServerTrustChain/httpbin_3.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/HTTPBin.org/Starfield Services Root Certificate Authority - G2.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/HTTPBin.org/httpbinorg_02182021.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Tests/Resources/SelfSigned/AltName.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.543
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `Tests/Tests/AFPropertyListRequestSerializerTests.m` (OBJECTIVE-C) | Magnitude: 14.9 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, safety: 7, state_mutation: 7, structural_boundaries: 4
- `Tests/Tests/AFHTTPRequestSerializationTests.m` (OBJECTIVE-C) | Magnitude: 194.06 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 102, state_mutation: 78, args: 31, test: 23
- `Example/iOS Example/Views/PostTableViewCell.h` (OBJECTIVE-C) | Magnitude: 18.26 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, ownership: 3, explicit_casts: 2, args: 1
- `Tests/Tests/AFPropertyListResponseSerializerTests.m` (OBJECTIVE-C) | Magnitude: 30.82 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, args: 16, state_mutation: 16, test: 16
- `Tests/Tests/AFUIImageViewTests.m` (OBJECTIVE-C) | Magnitude: 70.66 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 95, state_mutation: 22, safety: 18, args: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `UIKit+AFNetworking/UIButton+AFNetworking.h` (OBJECTIVE-C) | Magnitude: 164.65 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 46, explicit_casts: 25, args: 23, indent_spaces: 14
- `UIKit+AFNetworking/UIImageView+AFNetworking.m` (OBJECTIVE-C) | Magnitude: 185.46 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 72, state_mutation: 45, explicit_casts: 25, branch: 23
- `UIKit+AFNetworking/AFImageDownloader.h` (OBJECTIVE-C) | Magnitude: 8.76 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 35, explicit_casts: 15, args: 14, func_start: 10
- `AFNetworking/AFNetworkReachabilityManager.h` (OBJECTIVE-C) | Magnitude: 17.64 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 48, func_start: 13, explicit_casts: 13, api: 8
- `Example/watchOS Example Extension/ExtensionDelegate.h` (OBJECTIVE-C) | Magnitude: 11.56 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: ownership: 3, structural_boundaries: 2, generics: 2, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `UIKit+AFNetworking/AFAutoPurgingImageCache.h` (OBJECTIVE-C) | Magnitude: 140.21 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 40, explicit_casts: 20, args: 16, func_start: 10
- `AFNetworking/AFHTTPSessionManager.h` (OBJECTIVE-C) | Magnitude: 180.63 | Delta: **0.144 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 77, args: 50, indent_spaces: 40, bitwise_ops: 22
- `AFNetworking/AFSecurityPolicy.h` (OBJECTIVE-C) | Magnitude: 7.42 | Delta: **0.153 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 36, explicit_casts: 8, args: 7, func_start: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `UIKit+AFNetworking/AFAutoPurgingImageCache.m` (OBJECTIVE-C) | Magnitude: 227.84 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 95, state_mutation: 87, explicit_casts: 36, args: 28
- `AFNetworking/AFNetworkReachabilityManager.m` (OBJECTIVE-C) | Magnitude: 347.86 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 115, state_mutation: 98, branch: 55, args: 38
- `UIKit+AFNetworking/WKWebView+AFNetworking.m` (OBJECTIVE-C) | Magnitude: 194.92 | Delta: **0.224 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 74, state_mutation: 45, args: 29, branch: 19
- `UIKit+AFNetworking/AFImageDownloader.m` (OBJECTIVE-C) | Magnitude: 665.66 | Delta: **0.227 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 245, state_mutation: 164, branch: 68, concurrency: 55
- `UIKit+AFNetworking/UIProgressView+AFNetworking.m` (OBJECTIVE-C) | Magnitude: 173.6 | Delta: **0.248 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 51, state_mutation: 30, branch: 20, explicit_casts: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `AFNetworking/AFURLResponseSerialization.m` (OBJECTIVE-C) | Magnitude: 1655.0 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 402, state_mutation: 353, branch: 204, explicit_casts: 102
- `Tests/Tests/AFHTTPResponseSerializationTests.m` (OBJECTIVE-C) | Magnitude: 49.3 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, args: 21, state_mutation: 21, test: 17
- `Tests/Tests/AFNetworkActivityManagerTests.m` (OBJECTIVE-C) | Magnitude: 112.68 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 124, state_mutation: 51, safety: 23, args: 17
- `Example/tvOS Example/Gravatar.swift` (SWIFT) | Magnitude: 48.28 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 61, state_mutation: 23, structural_boundaries: 18, branch: 13
- `Tests/Tests/AFAutoPurgingImageCacheTests.m` (OBJECTIVE-C) | Magnitude: 209.5 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 136, state_mutation: 108, test: 33, args: 30

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Tests/Tests/AFTestCase.h` -> **Severity: 13.228** (Embedded: 0.1654 * Error Risk: 80.0%)
- `AFNetworking/AFURLResponseSerialization.h` -> **Severity: 8.542** (Embedded: 0.1203 * Error Risk: 70.9836%)
- `AFNetworking/AFURLSessionManager.h` -> **Severity: 6.765** (Embedded: 0.1016 * Error Risk: 66.5854%)
- `AFNetworking/AFHTTPSessionManager.h` -> **Severity: 6.173** (Embedded: 0.0772 * Error Risk: 80.0%)
- `AFNetworking/AFNetworkReachabilityManager.h` -> **Severity: 3.736** (Embedded: 0.0819 * Error Risk: 45.625%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `UIKit+AFNetworking/AFNetworkActivityIndicatorManager.h` -> **Severity: 880.994** (Blast Radius: 9.993 * Doc Risk: 88.1611%)
- `AFNetworking/AFURLResponseSerialization.h` -> **Severity: 858.971** (Blast Radius: 36.425 * Doc Risk: 23.5819%)
- `AFNetworking/AFCompatibilityMacros.h` -> **Severity: 784.2** (Blast Radius: 14.043 * Doc Risk: 55.8428%)
- `AFNetworking/AFHTTPSessionManager.m` -> **Severity: 554.071** (Blast Radius: 5.543 * Doc Risk: 99.9587%)
- `UIKit+AFNetworking/AFImageDownloader.m` -> **Severity: 553.877** (Blast Radius: 5.543 * Doc Risk: 99.9236%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
