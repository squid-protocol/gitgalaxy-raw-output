# ARCHITECTURAL_BRIEF: @azure_msal-node
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
| Total Artifacts | 78 |
| Analyzed Artifacts (Scanned) | 77 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1 |
| Total LOC | 6699 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 98.7% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | n/a (not computed) | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 75 | 6699 | 97.4% |
| MARKDOWN | 1 | 0 | 1.3% |
| PLAINTEXT | 1 | 0 | 1.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Small Flat Repo` (z -0.76; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 22%, Data / Markup / Trivial 19%, Large Core Modules 14%, Many-Argument Workhorses Files 13%, Generic / Templated Code Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 75 | 97.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 2.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1*

**Composition by Extension & Reason:**
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 92.5 | 10.3 | 4.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 87.9 | 28.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 19.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 13.8 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.7 | 83.7 | 17.8 | 9.2 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 31.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 26.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 20.4 | 2.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 68.0 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 17.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 53 | 18 | 2 | `package/src/cache/NodeStorage.ts` |
| cleanup | 6 | 3 | 0 | `package/src/client/PublicClientApplication.ts` |
| guards | 242 | 38 | 10 | `package/src/client/ClientApplication.ts` |
| danger | 64 | 18 | 3 | `package/src/client/ManagedIdentitySources/AzureArc.ts` |
| concurrency | 273 | 30 | 10 | `package/src/client/ClientApplication.ts` |
| connectivity | 351 | 75 | 9 | `package/src/index.ts` |
| io | 24 | 11 | 1 | `package/src/network/LoopbackClient.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 2 | 1 | 0 | `package/src/client/ManagedIdentitySources/ServiceFabric.ts` |
| time | 17 | 8 | 0 | `package/src/cache/serializer/Deserializer.ts` |
| serialization | 7 | 3 | 0 | `package/src/cache/TokenCache.ts` |
| regex | 11 | 5 | 0 | `package/src/utils/EncodingUtils.ts` |
| events | 68 | 18 | 2 | `package/src/cache/TokenCache.ts` |
| tests | 0 | 0 | 0 | - |
| docs | 383 | 66 | 12 | `package/src/cache/NodeStorage.ts` |
| debt | 2 | 2 | 0 | `package/src/client/OnBehalfOfClient.ts` |
| mutation | 687 | 66 | 28 | `package/src/cache/NodeStorage.ts` |
| dead_code | 96 | 32 | 3 | `package/src/crypto/CryptoProvider.ts` |
| credential | 3 | 3 | 0 | `package/src/client/ClientAssertion.ts` |
| threat | 6 | 5 | 0 | `package/src/client/ClientAssertion.ts` |
| ml_ai | 4 | 2 | 0 | `package/src/retry/ExponentialRetryStrategy.ts` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/src/network/LoopbackClient.ts` (Hits: 6)
- `package/src/client/ManagedIdentitySources/AzureArc.ts` (Hits: 5)
- `package/src/error/ManagedIdentityError.ts` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
No file in this repository is imported by another file that GitGalaxy could resolve, so there is no blast-radius ranking to report. That is itself a finding: either the codebase genuinely has no internal dependency structure (a collection of scripts, documents or configuration rather than a coupled system), or its import style is one the engine does not resolve for this language. Do not infer that any file is load-bearing from this section.


### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`package/src/index.ts`) — 30 outbound dependencies
2. **PublicClientApplication.ts** (`package/src/client/PublicClientApplication.ts`) — 18 outbound dependencies
3. **ClientApplication.ts** (`package/src/client/ClientApplication.ts`) — 17 outbound dependencies
4. **ManagedIdentityClient.ts** (`package/src/client/ManagedIdentityClient.ts`) — 14 outbound dependencies
5. **ConfidentialClientApplication.ts** (`package/src/client/ConfidentialClientApplication.ts`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getCachedAuthenticationResult` **(Many-Argument Workhorses)** (@ `package/src/client/ClientCredentialClient.ts`) -> Impact: **55.3** | LOC: 100
  * *Intent:* /** * looks up cache if the tokens are cached already */
- `sendRequest` **(Many-Argument Workhorses)** (@ `package/src/network/HttpClient.ts`) -> Impact: **35.5** | LOC: 84
  * *Intent:* * * Error handling priority: * 1. Timeout errors (AbortError) are converted to "Request timeout" messages * 2. Network/connection errors are wrapped w...
- `acquireTokenWithManagedIdentity` **(Many-Argument Workhorses)** (@ `package/src/client/ManagedIdentitySources/BaseManagedIdentitySource.ts`) -> Impact: **32.8** | LOC: 120
  * *Intent:* * Acquires an access token using the managed identity endpoint for the specified resource. * This is the primary method for token acquisition, handlin...
- `getServerTokenResponseAsync` **(Many-Argument Workhorses)** (@ `package/src/client/ManagedIdentitySources/AzureArc.ts`) -> Impact: **30.4** | LOC: 117
  * *Intent:* * @param networkClient - Network client for making the retry request if needed * @param networkRequest - The original request parameters (modified wit...
- `continuePolling` **(Many-Argument Workhorses)** (@ `package/src/client/DeviceCodeClient.ts`) -> Impact: **30.1** | LOC: 42
  * *Intent:* /** * Breaks the polling with specific conditions * @param deviceCodeExpirationTime - expiration time for the device code request * @param userSpecifi...
- `constructor` **(Compute Cores)** (@ `package/src/client/ConfidentialClientApplication.ts`) -> Impact: **28.5** | LOC: 61
  * *Intent:* * - authority: the authority URL for your application. * - client credential: Must set either client secret, certificate, or assertion for confidentia...
- `acquireTokenInteractive` **(Compute Cores)** (@ `package/src/client/PublicClientApplication.ts`) -> Impact: **28.0** | LOC: 108
  * *Intent:* /** * Acquires a token interactively via the browser by requesting an authorization code then exchanging it for a token. */
- `constructor` **(Defensive Guards)** (@ `package/src/config/ManagedIdentityId.ts`) -> Impact: **26.0** | LOC: 40
- `listenForAuthCode` **(Compute Cores)** (@ `package/src/network/LoopbackClient.ts`) -> Impact: **25.1** | LOC: 52
  * *Intent:* /** * Spins up a loopback server which returns the server response when the localhost redirectUri is hit * @param successTemplate * @param errorTempla...
- `tryCreate` **(Many-Argument Workhorses)** (@ `package/src/client/ManagedIdentitySources/AzureArc.ts`) -> Impact: **24.8** | LOC: 72
  * *Intent:* * are supported for Azure Arc scenarios. The method performs comprehensive validation of * endpoint URLs and logs detailed information about the detec...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/src/client` | 13 | 1247.98 | 14.61% | 8.71% |
| `package/src/client/ManagedIdentitySources` | 7 | 436.14 | 7.32% | 45.58% |
| `package/src/cache` | 4 | 408.26 | 11.08% | 0.0% |
| `package/src/request` | 16 | 236.18 | 1.91% | 0.0% |
| `package/src/network` | 4 | 214.88 | 37.83% | 24.41% |
| `package/src/config` | 3 | 152.64 | 34.0% | 36.31% |
| `package/src/retry` | 5 | 97.26 | 16.91% | 21.3% |
| `package/src/cache/serializer` | 3 | 96.52 | 4.38% | 18.09% |
| `package/src/utils` | 4 | 91.84 | 7.91% | 56.54% |
| `package/src/error` | 4 | 85.1 | 0.92% | 46.02% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/src/crypto/CryptoProvider.ts` -> **100.0%** Exposure
- `package/src/error/NodeAuthError.ts` -> **99.9612%** Exposure
- `package/src/cache/distributed/DistributedCachePlugin.ts` -> **98.2014%** Exposure
- `package/src/config/ManagedIdentityRequestParameters.ts` -> **97.7023%** Exposure
- `package/src/utils/EncodingUtils.ts` -> **88.0797%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/src/config/ManagedIdentityId.ts` -> **100.0%** Exposure
- `package/src/config/ManagedIdentityRequestParameters.ts` -> **100.0%** Exposure
- `package/src/utils/NetworkUtils.ts` -> **100.0%** Exposure
- `package/src/client/ClientAssertion.ts` -> **99.9997%** Exposure
- `package/src/network/HttpClientWithRetries.ts` -> **87.262%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/src/crypto/CryptoProvider.ts` -> **12** Orphaned Functions | **0** Duplicates
- `package/src/error/NodeAuthError.ts` -> **10** Orphaned Functions | **0** Duplicates
- `package/src/client/PublicClientApplication.ts` -> **7** Orphaned Functions | **0** Duplicates
- `package/src/client/ConfidentialClientApplication.ts` -> **4** Orphaned Functions | **0** Duplicates
- `package/src/client/ManagedIdentitySources/AzureArc.ts` -> **4** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `package/src/client/ClientAssertion.ts` -> **99.9718%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `70` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `package/src/network/HttpClientWithRetries.ts` (TYPESCRIPT) -> Cumulative Risk: **630.83**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.34)
- **Magnitude:** 66.78 | **LOC:** 90 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (92.5084%)
- **Heaviest Functions:** `sendNetworkRequestAsync` (Many-Argument Workhorses, Impact: 9.6), `sendNetworkRequestAsyncHelper` (Generic / Templated Code, Impact: 8.6), `sendGetRequestAsync` (Generic / Templated Code, Impact: 3.8)

### 2. `package/src/retry/ImdsRetryPolicy.ts` (TYPESCRIPT) -> Cumulative Risk: **596.27**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.32)
- **Magnitude:** 47.4 | **LOC:** 123 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.6385%), Documentation (83.3333%), State Flux (75.026%)
- **Heaviest Functions:** `pauseForRetry` (Many-Argument Workhorses, Impact: 20.8), `isNewRequest` (State Mutators, Impact: 1.6), `MIN_EXPONENTIAL_BACKOFF_MS` (Interface Declarations, Impact: 1.1)

### 3. `package/src/config/ManagedIdentityRequestParameters.ts` (TYPESCRIPT) -> Cumulative Risk: **572.11**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.23)
- **Magnitude:** 37.24 | **LOC:** 68 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (97.7023%)
- **Heaviest Functions:** `constructor` (Generic / Templated Code, Impact: 6.7), `computeUri` (I/O & Config Routines, Impact: 2.9), `computeParametersBodyString` (Interface Declarations, Impact: 2.6)

### 4. `package/src/cache/distributed/DistributedCachePlugin.ts` (TYPESCRIPT) -> Cumulative Risk: **563.26**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.77)
- **Magnitude:** 49.68 | **LOC:** 73 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (98.2014%), State Flux (84.859%)
- **Heaviest Functions:** `afterCacheAccess` (Compute Cores, Impact: 7.0), `constructor` (State Mutators, Impact: 1.9), `beforeCacheAccess` (Interface Declarations, Impact: 1.8)

### 5. `package/src/cache/TokenCache.ts` (TYPESCRIPT) -> Cumulative Risk: **540.99**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.05)
- **Magnitude:** 191.38 | **LOC:** 399 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.8122%), Verification (80.0%), State Flux (77.2113%)
- **Heaviest Functions:** `mergeUpdates` (Compute Cores, Impact: 19.0), `removeAccount` (Defensive Guards, Impact: 13.2), `mergeRemovals` (Many-Argument Workhorses, Impact: 12.5)

### 6. `package/src/network/HttpClient.ts` (TYPESCRIPT) -> Cumulative Risk: **537.71**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +2.15)
- **Magnitude:** 85.94 | **LOC:** 222 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9926%), Verification (80.0%), State Flux (79.2213%)
- **Heaviest Functions:** `sendRequest` (Many-Argument Workhorses, Impact: 35.5), `sendGetRequestAsync` (Generic / Templated Code, Impact: 6.3), `getFetchHeaders` (Callbacks & Closures, Impact: 6.3)

### 7. `package/src/utils/NetworkUtils.ts` (TYPESCRIPT) -> Cumulative Risk: **534.51**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +2.35)
- **Magnitude:** 23.96 | **LOC:** 62 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (88.0797%)
- **Heaviest Functions:** `urlToHttpOptions` (Compute Cores, Impact: 12.5), `getNetworkResponse` (Generic / Templated Code, Impact: 2.5)

### 8. `package/src/client/ConfidentialClientApplication.ts` (TYPESCRIPT) -> Cumulative Risk: **530.32**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.50)
- **Magnitude:** 99.8 | **LOC:** 304 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (98.2014%), Verification (80.0%), State Flux (78.9336%)
- **Heaviest Functions:** `constructor` (Compute Cores, Impact: 28.5), `acquireTokenByClientCredential` (Compute Cores, Impact: 18.3), `acquireTokenOnBehalfOf` (Defensive Guards, Impact: 6.1)

### 9. `package/src/config/ManagedIdentityId.ts` (TYPESCRIPT) -> Cumulative Risk: **524.91**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +1.65)
- **Magnitude:** 62.62 | **LOC:** 74 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (85.542%)
- **Heaviest Functions:** `constructor` (Defensive Guards, Impact: 26.0), `id` (State Mutators, Impact: 1.6), `idType` (State Mutators, Impact: 1.6)

### 10. `package/src/client/ManagedIdentitySources/BaseManagedIdentitySource.ts` (TYPESCRIPT) -> Cumulative Risk: **509.6**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.34)
- **Magnitude:** 139.78 | **LOC:** 416 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (93.2507%), Verification (80.0%), State Flux (74.9214%)
- **Heaviest Functions:** `acquireTokenWithManagedIdentity` (Many-Argument Workhorses, Impact: 32.8), `getManagedIdentityUserAssignedIdQueryParameterKey` (Many-Argument Workhorses, Impact: 23.9), `getServerTokenResponse` (Compute Cores, Impact: 16.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `package/src/client/ClientApplication.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 217.8 | **LOC:** 684 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.038%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `acquireTokenByCode` **(Many-Argument Workhorses)** (Impact: 16.9)
    * *Intent:* /** * Acquires a token by exchanging the Authorization Code received from the first step of OAuth2.0...
  * `buildOauthClientConfiguration` **(Many-Argument Workhorses)** (Impact: 14.1)
    * *Intent:* /** * Builds the common configuration to be passed to the common component based on the platform con...
  * `initializeBaseRequest` **(Compute Cores)** (Impact: 12.9)
    * *Intent:* /** * Generates a request with the default scopes & generates a correlationId. * @param authRequest ...
  * `acquireTokenSilent` **(Defensive Guards)** (Impact: 12.0)
    * *Intent:* /** * Acquires a token silently when a user specifies the account the token is requested for. * * Th...
  * `createAuthority` **(Many-Argument Workhorses)** (Impact: 10.5)
    * *Intent:* /** * Create authority instance. If authority not passed in request, default to authority set on the...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 58
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 59`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`, `dead_code: 1`
* *Architecture:* `api: 9`, `concurrency: 43`, `import: 17`
* *Defense:* `safety: 15`, `doc: 21`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` NodeStorage.js, TokenCache.js, Configuration.js, CryptoProvider.js, NodeAuthError.js, packageMetadata.js, Authorize.js, AuthorizationCodeRequest.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/cache/TokenCache.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 191.38 | **LOC:** 399 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.5749%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mergeUpdates` **(Compute Cores)** (Impact: 19.0)
    * *Intent:* /** * Deep update of oldState based on newState values * @param oldState - cache before changes * @p...
  * `removeAccount` **(Defensive Guards)** (Impact: 13.2)
    * *Intent:* /** * API to remove a specific account and the relevant data from cache * @param account - AccountIn...
  * `mergeRemovals` **(Many-Argument Workhorses)** (Impact: 12.5)
    * *Intent:* /** * Removes entities in oldState that the were removed from newState. If there are any unknown val...
  * `getAccountByHomeId` **(Compute Cores)** (Impact: 9.2)
    * *Intent:* /** * Returns the signed in account matching homeAccountId. * (the account object is created at the ...
  * `getAccountByLocalId` **(Compute Cores)** (Impact: 9.2)
    * *Intent:* /** * Returns the signed in account matching localAccountId. * (the account object is created at the...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 33
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 41`, `args: 21`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 13`, `dead_code: 2`
* *Architecture:* `api: 11`, `concurrency: 18`, `import: 8`
* *Defense:* `safety: 4`, `doc: 17`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CryptoProvider.js, GuidGenerator.js, ITokenCache.js, NodeStorage.js, Deserializer.js, Serializer.js, SerializerTypes.js, node
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/cache/NodeStorage.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 183.7 | **LOC:** 566 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.1083%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `cacheToInMemoryCache` **(Compute Cores)** (Impact: 19.9)
    * *Intent:* /** * Converts cacheKVStore to InMemoryCache * @param cache - key value store */
  * `updateCredentialCacheKey` **(Compute Cores)** (Impact: 8.2)
    * *Intent:* /** * Updates a credential's cache key if the current cache key is outdated */
  * `constructor` **(State Mutators)** (Impact: 5.2)
  * `removeItem` **(Compute Cores)** (Impact: 5.2)
    * *Intent:* /** * Removes the cache item from memory with the given key. * @param key - lookup key to remove a c...
  * `getServerTelemetry` **(Compute Cores)** (Impact: 5.1)
    * *Intent:* /** * fetch server telemetry entity from the platform cache * @param serverTelemetrykey - lookup key...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 63`, `args: 43`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `api: 29`, `concurrency: 8`, `import: 5`
* *Defense:* `doc: 36`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CacheHelpers.js, Deserializer.js, Serializer.js, SerializerTypes.js, node
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/ClientCredentialClient.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 163.72 | **LOC:** 432 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.0475%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getCachedAuthenticationResult` **(Many-Argument Workhorses)** (Impact: 55.3)
    * *Intent:* /** * looks up cache if the tokens are cached already */
  * `createTokenRequestBody` **(Compute Cores)** (Impact: 16.8)
    * *Intent:* /** * generate the request to the server in the acceptable format * @param request - CommonClientCre...
  * `executeTokenRequest` **(Many-Argument Workhorses)** (Impact: 12.9)
    * *Intent:* /** * Makes a network call to request the token from the service * @param request - CommonClientCred...
  * `readAccessTokenFromCache` **(Many-Argument Workhorses)** (Impact: 11.3)
    * *Intent:* /** * Reads access token from the cache */
  * `acquireToken` **(Compute Cores)** (Impact: 10.6)
    * *Intent:* /** * Public API to acquire a token with ClientCredential Flow for Confidential clients * @param req...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 28
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 28`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`, `dead_code: 2`
* *Architecture:* `api: 4`, `concurrency: 18`, `import: 5`
* *Defense:* `safety: 5`, `doc: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Configuration.js, CommonClientCredentialRequest.js, Constants.js, BaseClient.js, node
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/ManagedIdentitySources/BaseManagedIdentitySource.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 139.78 | **LOC:** 416 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.0819%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `acquireTokenWithManagedIdentity` **(Many-Argument Workhorses)** (Impact: 32.8)
    * *Intent:* * Acquires an access token using the managed identity endpoint for the specified resource. * This is...
  * `getManagedIdentityUserAssignedIdQueryParameterKey` **(Many-Argument Workhorses)** (Impact: 23.9)
    * *Intent:* /** * Determines the appropriate query parameter name for user-assigned managed identity * based on ...
  * `getServerTokenResponse` **(Compute Cores)** (Impact: 16.5)
    * *Intent:* /** * Converts a managed identity token response to a standardized server authorization token respon...
  * `getValidatedEnvVariableUrlString` **(Defensive Guards)** (Impact: 3.4)
    * *Intent:* /** * Validates and normalizes an environment variable containing a URL string. * This static utilit...
  * `constructor` **(State Mutators)** (Impact: 3.1)
    * *Intent:* /** * Creates an instance of BaseManagedIdentitySource. * * @param logger - Logger instance for diag...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 17
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 27`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `dead_code: 1`
* *Architecture:* `api: 9`, `concurrency: 7`, `import: 11`
* *Defense:* `safety: 9`, `doc: 13`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` NodeStorage.js, ManagedIdentityId.js, ManagedIdentityRequestParameters.js, CryptoProvider.js, ManagedIdentityError.js, HttpClientWithRetries.js, ManagedIdentityRequest.js, ManagedIdentityTokenResponse.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/PublicClientApplication.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 138.96 | **LOC:** 406 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.5756%), Tech Debt (46.3539%)
**Top Internal Functions/Classes:**
  * `acquireTokenInteractive` **(Compute Cores)** (Impact: 28.0)
    * *Intent:* /** * Acquires a token interactively via the browser by requesting an authorization code then exchan...
  * `acquireTokenSilent` **(Compute Cores)** (Impact: 14.6)
    * *Intent:* /** * Returns a token retrieved either from the cache or by exchanging the refresh token for a fresh...
  * `waitForRedirectUri` **(Defensive Guards)** (Impact: 7.6)
    * *Intent:* /** * Attempts to retrieve the redirectUri from the loopback server. If the loopback server does not...
  * `constructor` **(State Mutators)** (Impact: 6.7)
    * *Intent:* * - authority: the authority URL for your application. * * AAD authorities are of the form https://l...
  * `signOut` **(Compute Cores)** (Impact: 6.5)
    * *Intent:* /** * Removes cache artifacts associated with the given account * @param request - developer provide...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 40
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 53`, `args: 13`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`, `unreferenced_by_name: 7`
* *Architecture:* `api: 2`, `concurrency: 30`, `import: 18`
* *Defense:* `safety: 9`, `doc: 10`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Configuration.js, NodeAuthError.js, ILoopbackClient.js, LoopbackClient.js, packageMetadata.js, AuthorizationCodeRequest.js, AuthorizationUrlRequest.js, CommonDeviceCodeRequest.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/OnBehalfOfClient.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 119.78 | **LOC:** 416 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.3333%), Tech Debt (9.3764%)
**Top Internal Functions/Classes:**
  * `getCachedAuthenticationResult` **(Compute Cores)** (Impact: 19.9)
    * *Intent:* /** * look up cache for tokens * Find idtoken in the cache * Find accessToken based on user assertio...
  * `createTokenRequestBody` **(Compute Cores)** (Impact: 15.8)
    * *Intent:* /** * generate a server request in accepable format * @param request - developer provided CommonOnBe...
  * `readAccessTokenFromCacheForOBO` **(Compute Cores)** (Impact: 14.3)
    * *Intent:* /** * Fetches the cached access token based on incoming assertion * @param clientId - client id * @p...
  * `acquireToken` **(Defensive Guards)** (Impact: 7.1)
    * *Intent:* /** * Public API to acquire tokens with on behalf of flow * @param request - developer provided Comm...
  * `executeTokenRequest` **(Many-Argument Workhorses)** (Impact: 5.0)
    * *Intent:* /** * Make a network call to the server requesting credentials * @param request - developer provided...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 30
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 25`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`, `planned_debt: 1`
* *Architecture:* `api: 3`, `concurrency: 15`, `import: 5`
* *Defense:* `safety: 5`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CommonOnBehalfOfRequest.js, Constants.js, EncodingUtils.js, BaseClient.js, node
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/DeviceCodeClient.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 110.66 | **LOC:** 415 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.5952%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `continuePolling` **(Many-Argument Workhorses)** (Impact: 30.1)
    * *Intent:* /** * Breaks the polling with specific conditions * @param deviceCodeExpirationTime - expiration tim...
  * `acquireTokenWithDeviceCode` **(Many-Argument Workhorses)** (Impact: 20.2)
    * *Intent:* /** * Creates token request with device code response and polls token endpoint at interval set by th...
  * `createTokenRequestBody` **(Many-Argument Workhorses)** (Impact: 13.0)
    * *Intent:* /** * Creates query parameters and converts to string. * @param request - developer provided CommonD...
  * `createQueryString` **(Compute Cores)** (Impact: 8.6)
    * *Intent:* /** * Create device code endpoint query parameters and returns string * @param request - developer p...
  * `executePostRequestToDeviceCodeEndpoint` **(Many-Argument Workhorses)** (Impact: 4.2)
    * *Intent:* /** * Executes POST request to device code endpoint * @param deviceCodeEndpoint - token endpoint * @...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 22`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `dead_code: 1`
* *Architecture:* `api: 4`, `concurrency: 13`, `import: 5`
* *Defense:* `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ClientAuthErrorCodes.js, CommonDeviceCodeRequest.js, Constants.js, BaseClient.js, node
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/ClientAssertion.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 106.78 | **LOC:** 203 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.565%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getJwt` **(Many-Argument Workhorses)** (Impact: 17.4)
    * *Intent:* /** * Update JWT for certificate based clientAssertion, if passed by the user, uses it as is * @para...
  * `createJwt` **(Many-Argument Workhorses)** (Impact: 10.2)
    * *Intent:* /** * JWT format and required claims specified: https://tools.ietf.org/html/rfc7523#section-3 */
  * `fromCertificate` **(Many-Argument Workhorses)** (Impact: 6.8)
    * *Intent:* /** * @deprecated Use fromCertificateWithSha256Thumbprint instead, with a SHA-256 thumprint * Initia...
  * `fromCertificateWithSha256Thumbprint` **(Many-Argument Workhorses)** (Impact: 6.8)
    * *Intent:* /** * Initialize the ClientAssertion class from the certificate passed by the user * @param thumbpri...
  * `parseCertificate` **(Compute Cores)** (Impact: 5.2)
    * *Intent:* /** * Extracts the raw certs from a given certificate string and returns them in an array. * @param ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 17`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 19`, `dead_code: 1`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CryptoProvider.js, ClientAuthErrorCodes.js, Constants.js, EncodingUtils.js, node, jsonwebtoken
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/ManagedIdentitySources/AzureArc.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 103.06 | **LOC:** 416 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.9633%), Tech Debt (29.2343%)
**Top Internal Functions/Classes:**
  * `getServerTokenResponseAsync` **(Many-Argument Workhorses)** (Impact: 30.4)
    * *Intent:* * @param networkClient - Network client for making the retry request if needed * @param networkReque...
  * `tryCreate` **(Many-Argument Workhorses)** (Impact: 24.8)
    * *Intent:* * are supported for Azure Arc scenarios. The method performs comprehensive validation of * endpoint ...
  * `getEnvironmentVariables` **(I/O & Config Routines)** (Impact: 4.8)
    * *Intent:* /** * Retrieves and validates Azure Arc environment variables for managed identity configuration. * ...
  * `constructor` **(Many-Argument Workhorses)** (Impact: 3.5)
    * *Intent:* /** * Creates a new instance of the AzureArc managed identity source. * * @param logger - Logger ins...
  * `createRequest` **(I/O & Config Routines)** (Impact: 2.3)
    * *Intent:* /** * Creates a properly formatted HTTP request for acquiring tokens from the Azure Arc identity end...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 27`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`, `dead_code: 2`, `unreferenced_by_name: 4`
* *Architecture:* `io: 5`, `api: 9`, `concurrency: 4`, `import: 11`
* *Defense:* `safety: 11`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` NodeStorage.js, ManagedIdentityId.js, ManagedIdentityRequestParameters.js, CryptoProvider.js, ManagedIdentityError.js, ManagedIdentityTokenResponse.js, Constants.js, BaseManagedIdentitySource.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/ConfidentialClientApplication.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 99.8 | **LOC:** 304 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.9529%), Tech Debt (37.2091%)
**Top Internal Functions/Classes:**
  * `constructor` **(Compute Cores)** (Impact: 28.5)
    * *Intent:* * - authority: the authority URL for your application. * - client credential: Must set either client...
  * `acquireTokenByClientCredential` **(Compute Cores)** (Impact: 18.3)
    * *Intent:* /** * Acquires tokens from the authority for the application (not for an end user). */
  * `acquireTokenOnBehalfOf` **(Defensive Guards)** (Impact: 6.1)
    * *Intent:* /** * Acquires tokens from the authority for the application. * * Used in scenarios where the curren...
  * `SetAppTokenProvider` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* /** * This extensibility point only works for the client_credential flow, i.e. acquireTokenByClientC...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 33`, `args: 5`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`, `unreferenced_by_name: 4`
* *Architecture:* `api: 3`, `concurrency: 13`, `import: 13`
* *Defense:* `safety: 7`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Configuration.js, ClientAuthErrorCodes.js, ClientCredentialRequest.js, CommonClientCredentialRequest.js, CommonOnBehalfOfRequest.js, OnBehalfOfRequest.js, Constants.js, ClientApplication.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/network/HttpClient.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 85.94 | **LOC:** 222 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.1543%), Tech Debt (40.1986%)
**Top Internal Functions/Classes:**
  * `sendRequest` **(Many-Argument Workhorses)** (Impact: 35.5)
    * *Intent:* * * Error handling priority: * 1. Timeout errors (AbortError) are converted to "Request timeout" mes...
  * `sendGetRequestAsync` **(Generic / Templated Code)** (Impact: 6.3)
    * *Intent:* * Sends an HTTP GET request to the specified URL. * * This method handles GET requests with optional...
  * `getFetchHeaders` **(Callbacks & Closures)** (Impact: 6.3)
    * *Intent:* /** * Converts NetworkRequestOptions headers to a fetch-compatible Headers object. * * The MSAL libr...
  * `sendPostRequestAsync` **(Generic / Templated Code)** (Impact: 3.8)
    * *Intent:* /** * Sends an HTTP POST request to the specified URL. * * This method handles POST requests with re...
  * `getHeaderDict` **(Callbacks & Closures)** (Impact: 1.9)
    * *Intent:* /** * Converts a fetch Headers object to a plain JavaScript object. * * The fetch API returns header...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 18`, `args: 8`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 9`, `import: 2`
* *Defense:* `safety: 5`, `doc: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Constants.js, node
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/network/HttpClientWithRetries.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 66.78 | **LOC:** 90 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.5084%), Tech Debt (30.7718%)
**Top Internal Functions/Classes:**
  * `sendNetworkRequestAsync` **(Many-Argument Workhorses)** (Impact: 9.6)
  * `sendNetworkRequestAsyncHelper` **(Generic / Templated Code)** (Impact: 8.6)
  * `sendGetRequestAsync` **(Generic / Templated Code)** (Impact: 3.8)
  * `sendPostRequestAsync` **(Generic / Templated Code)** (Impact: 3.8)
  * `constructor` **(State Mutators)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 14`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `concurrency: 11`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` IHttpRetryPolicy.js, Constants.js, node
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/ManagedIdentityClient.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 66.16 | **LOC:** 190 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.842%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `selectManagedIdentitySource` **(Many-Argument Workhorses)** (Impact: 21.6)
    * *Intent:* /** * Tries to create a managed identity source for all sources * @returns the managed identity Sour...
  * `sendManagedIdentityTokenRequest` **(Many-Argument Workhorses)** (Impact: 8.0)
  * `getManagedIdentitySource` **(I/O & Config Routines)** (Impact: 7.3)
    * *Intent:* /** * Determine the Managed Identity Source based on available environment variables. This API is co...
  * `constructor` **(State Mutators)** (Impact: 3.1)
  * `allEnvironmentVariablesAreDefined` **(Callbacks & Closures)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 22`, `args: 6`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `api: 5`, `concurrency: 2`, `import: 14`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` NodeStorage.js, ManagedIdentityId.js, CryptoProvider.js, ManagedIdentityError.js, ManagedIdentityRequest.js, Constants.js, AppService.js, AzureArc.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/ManagedIdentityApplication.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 65.28 | **LOC:** 270 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.6222%), Tech Debt (20.2725%)
**Top Internal Functions/Classes:**
  * `acquireToken` **(Compute Cores)** (Impact: 20.6)
    * *Intent:* /** * Acquire an access token from the cache or the managed identity * @param managedIdentityRequest...
  * `constructor` **(State Mutators)** (Impact: 8.2)
  * `acquireTokenFromManagedIdentity` **(Many-Argument Workhorses)** (Impact: 5.2)
    * *Intent:* /** * Acquires a token from a managed identity endpoint. * * @param managedIdentityRequest - The req...
  * `getManagedIdentitySource` **(Interface Declarations)** (Impact: 2.3)
    * *Intent:* /** * Determine the Managed Identity Source based on available environment variables. This API is co...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 22`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`, `dead_code: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 3`, `concurrency: 6`, `import: 12`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` NodeStorage.js, Configuration.js, ManagedIdentityId.js, CryptoProvider.js, HashUtils.js, packageMetadata.js, ManagedIdentityRequest.js, ManagedIdentityRequestParams.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/config/ManagedIdentityId.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 62.62 | **LOC:** 74 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.4614%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `constructor` **(Defensive Guards)** (Impact: 26.0)
  * `id` **(State Mutators)** (Impact: 1.6)
  * `idType` **(State Mutators)** (Impact: 1.6)
  * `id` **(Interface Declarations)** (Impact: 1.1)
  * `idType` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 8`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ManagedIdentityError.js, Constants.js, Configuration.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/config/Configuration.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 52.78 | **LOC:** 268 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.5604%), Tech Debt (11.215%)
**Top Internal Functions/Classes:**
  * `buildManagedIdentityConfiguration` **(Defensive Guards)** (Impact: 14.3)
  * `buildAppConfiguration` **(Defensive Guards)** (Impact: 12.9)
    * *Intent:* /** * Sets the default options when not explicitly configured from app developer * * @param auth - A...
  * `loggerCallback` **(I/O & Config Routines)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 30`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 2`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 13`, `import: 4`
* *Defense:* `safety: 5`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` NodeAuthError.js, HttpClient.js, ManagedIdentityId.js, node
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/cache/distributed/DistributedCachePlugin.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 49.68 | **LOC:** 73 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.5754%), Tech Debt (98.2014%)
**Top Internal Functions/Classes:**
  * `afterCacheAccess` **(Compute Cores)** (Impact: 7.0)
    * *Intent:* /** * Serializes the cache after accessing it * @param cacheContext - TokenCacheContext */
  * `constructor` **(State Mutators)** (Impact: 1.9)
  * `beforeCacheAccess` **(Interface Declarations)** (Impact: 1.8)
    * *Intent:* /** * Deserializes the cache before accessing it * @param cacheContext - TokenCacheContext */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 15`, `args: 4`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `concurrency: 9`, `import: 4`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TokenCache.js, ICacheClient.js, IPartitionManager.js, node
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/network/LoopbackClient.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 49.38 | **LOC:** 117 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.1277%), Tech Debt (26.6607%)
**Top Internal Functions/Classes:**
  * `listenForAuthCode` **(Compute Cores)** (Impact: 25.1)
    * *Intent:* /** * Spins up a loopback server which returns the server response when the localhost redirectUri is...
  * `getRedirectUri` **(I/O & Config Routines)** (Impact: 7.8)
    * *Intent:* /** * Get the port that the loopback server is running on * @returns */
  * `closeServer` **(I/O & Config Routines)** (Impact: 3.8)
    * *Intent:* /** * Close the loopback server */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Concurrency (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 15`, `args: 5`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 3`, `import: 5`
* *Defense:* `doc: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` NodeAuthError.js, Constants.js, ILoopbackClient.js, node, http
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 47.7 | **LOC:** 124 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 44`
* *Risk/State:* None
* *Architecture:* `api: 31`, `import: 31`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ITokenCache.js, TokenCache.js, DistributedCachePlugin.js, ICacheClient.js, IPartitionManager.js, SerializerTypes.js, ClientAssertion.js, ConfidentialClientApplication.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/retry/ImdsRetryPolicy.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 47.4 | **LOC:** 123 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.8362%), Tech Debt (57.7495%)
**Top Internal Functions/Classes:**
  * `pauseForRetry` **(Many-Argument Workhorses)** (Impact: 20.8)
    * *Intent:* /** * Pauses execution for a calculated delay before retrying a request. * * @param httpStatusCode -...
  * `isNewRequest` **(State Mutators)** (Impact: 1.6)
  * `MIN_EXPONENTIAL_BACKOFF_MS` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* /* * these are defined here as static variables despite being defined as constants outside of the * ...
  * `MAX_EXPONENTIAL_BACKOFF_MS` **(Interface Declarations)** (Impact: 1.1)
  * `EXPONENTIAL_DELTA_BACKOFF_MS` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 10
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 15`, `args: 7`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `dead_code: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `concurrency: 5`, `import: 3`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ExponentialRetryStrategy.js, IHttpRetryPolicy.js, node
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/cache/serializer/Deserializer.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 45.96 | **LOC:** 222 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.4759%), Tech Debt (23.1578%)
**Top Internal Functions/Classes:**
  * `deserializeAllCache` **(Compute Cores)** (Impact: 9.4)
    * *Intent:* /** * Deserialize an inMemory Cache * @param jsonCache - JSON blob cache */
  * `deserializeAccounts` **(Callbacks & Closures)** (Impact: 5.9)
    * *Intent:* /** * Deserializes accounts to AccountEntity objects * @param accounts - accounts of type Serialized...
  * `deserializeAccessTokens` **(Compute Cores)** (Impact: 4.5)
    * *Intent:* /** * Deserializes access tokens to AccessTokenEntity objects * @param accessTokens - access tokens ...
  * `deserializeRefreshTokens` **(Callbacks & Closures)** (Impact: 4.1)
    * *Intent:* /** * Deserializes refresh tokens to RefreshTokenEntity objects * @param refreshTokens - refresh tok...
  * `deserializeIdTokens` **(Callbacks & Closures)** (Impact: 3.9)
    * *Intent:* /** * Deserializes id tokens to IdTokenEntity objects * @param idTokens - credentials of type Serial...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 13`, `args: 13`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 1`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SerializerTypes.js, node
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/utils/Constants.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 45.22 | **LOC:** 187 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 39`
* *Risk/State:* None
* *Architecture:* `io: 2`, `api: 28`, `import: 2`
* *Defense:* `doc: 15`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DefaultManagedIdentityRetryPolicy.js, ImdsRetryPolicy.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/ManagedIdentitySources/MachineLearning.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 43.66 | **LOC:** 220 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.8104%), Tech Debt (50.9764%)
**Top Internal Functions/Classes:**
  * `tryCreate` **(Many-Argument Workhorses)** (Impact: 11.8)
    * *Intent:* * This method validates the Azure Machine Learning environment by checking for the required * MSI_EN...
  * `createRequest` **(Many-Argument Workhorses)** (Impact: 11.1)
    * *Intent:* * * - System-assigned: Uses the DEFAULT_IDENTITY_CLIENT_ID environment variable * - User-assigned: O...
  * `constructor` **(Many-Argument Workhorses)** (Impact: 3.8)
    * *Intent:* /** * Creates a new MachineLearning managed identity source instance. * * @param logger - Logger ins...
  * `getEnvironmentVariables` **(Interface Declarations)** (Impact: 1.4)
    * *Intent:* /** * Retrieves the required environment variables for Azure Machine Learning managed identity. * * ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 15`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `dead_code: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 5`, `import: 7`
* *Defense:* `safety: 2`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` NodeStorage.js, ManagedIdentityId.js, ManagedIdentityRequestParameters.js, CryptoProvider.js, Constants.js, BaseManagedIdentitySource.js, node
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/src/client/ManagedIdentitySources/ServiceFabric.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 42.72 | **LOC:** 218 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.1797%), Tech Debt (51.9831%)
**Top Internal Functions/Classes:**
  * `tryCreate` **(Many-Argument Workhorses)** (Impact: 18.4)
    * *Intent:* * is running in a properly configured Service Fabric cluster with managed identity enabled. * * Note...
  * `createRequest` **(Many-Argument Workhorses)** (Impact: 5.1)
    * *Intent:* * - The secret header for authentication with MITS * - API version parameter for the Service Fabric ...
  * `constructor` **(Many-Argument Workhorses)** (Impact: 3.8)
    * *Intent:* * Constructs a new ServiceFabric managed identity source for acquiring tokens from Azure Service Fab...
  * `getEnvironmentVariables` **(Interface Declarations)** (Impact: 1.9)
    * *Intent:* /** * Retrieves the environment variables required for Service Fabric managed identity authenticatio...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 14`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`, `unreferenced_by_name: 3`
* *Architecture:* `io: 1`, `api: 4`, `import: 7`
* *Defense:* `safety: 2`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.987
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` NodeStorage.js, ManagedIdentityId.js, ManagedIdentityRequestParameters.js, CryptoProvider.js, Constants.js, BaseManagedIdentitySource.js, node
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/src/cache/CacheHelpers.ts` -> **Severity: 1298.7** (Blast Radius: 12.987 * Doc Risk: 100.0%)
- `package/src/config/ManagedIdentityId.ts` -> **Severity: 1298.7** (Blast Radius: 12.987 * Doc Risk: 100.0%)
- `package/src/config/ManagedIdentityRequestParameters.ts` -> **Severity: 1298.7** (Blast Radius: 12.987 * Doc Risk: 100.0%)
- `package/src/crypto/HashUtils.ts` -> **Severity: 1298.7** (Blast Radius: 12.987 * Doc Risk: 100.0%)
- `package/src/error/ManagedIdentityError.ts` -> **Severity: 1298.7** (Blast Radius: 12.987 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
